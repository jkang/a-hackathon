#!/usr/bin/env python3
"""
data_processor.py — Data Visualizer Pro 辅助预处理脚本

用途：对大型 CSV / Excel / JSON 文件进行清洗、聚合，输出适合
      ECharts 直接消费的轻量 JSON，避免将 5000+ 条原始数据内嵌 HTML。

用法：
    python data_processor.py --input data.csv --goal trend --dimension date --measure revenue
    python data_processor.py --input data.xlsx --goal compare --dimension region --measure sales,profit
    python data_processor.py --input data.json --goal distribution --measure score --bins 20

输出：
    打印聚合后的 JSON 到 stdout，Claude 读取后内嵌至 HTML。
    同时在 --input 同目录下生成 _processed.json 文件。
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("请先安装依赖：pip install pandas openpyxl numpy", file=sys.stderr)
    sys.exit(1)


# ─── 数据加载 ────────────────────────────────────────────────────────────────

def load_data(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(file_path)
    elif suffix in (".xlsx", ".xls"):
        df = pd.read_excel(file_path)
    elif suffix == ".json":
        with open(file_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        df = pd.DataFrame(raw) if isinstance(raw, list) else pd.DataFrame([raw])
    else:
        raise ValueError(f"不支持的文件格式: {suffix}。支持 csv / xlsx / json")

    print(f"[数据加载] 共 {len(df)} 行 × {len(df.columns)} 列", file=sys.stderr)
    return df


# ─── 数据清洗 ────────────────────────────────────────────────────────────────

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    original_rows = len(df)
    df = df.drop_duplicates()
    dup_removed = original_rows - len(df)
    if dup_removed > 0:
        print(f"[清洗] 删除重复行 {dup_removed} 条", file=sys.stderr)

    # 报告空值情况
    null_ratios = df.isnull().mean()
    high_null = null_ratios[null_ratios > 0.05]
    if not high_null.empty:
        print(f"[警告] 以下列空值比例 > 5%，建议检查：", file=sys.stderr)
        for col, ratio in high_null.items():
            print(f"  {col}: {ratio:.1%}", file=sys.stderr)

    # 尝试自动解析日期列
    for col in df.select_dtypes(include="object").columns:
        try:
            parsed = pd.to_datetime(df[col], infer_datetime_format=True, errors="raise")
            df[col] = parsed
            print(f"[清洗] 列 '{col}' 已解析为日期类型", file=sys.stderr)
        except Exception:
            pass

    return df


# ─── 聚合策略 ────────────────────────────────────────────────────────────────

def aggregate(df: pd.DataFrame, dimension: str, measures: list[str],
              agg_func: str = "sum") -> dict:
    """
    按 dimension 列分组，对 measures 列执行聚合。
    返回适合 ECharts category axis 的格式：
    { "categories": [...], "series": [{"name": col, "data": [...]}] }
    """
    func_map = {"sum": "sum", "mean": "mean", "count": "count", "max": "max", "min": "min"}
    fn = func_map.get(agg_func, "sum")

    if dimension not in df.columns:
        raise ValueError(f"维度列 '{dimension}' 不存在，可用列：{list(df.columns)}")
    for m in measures:
        if m not in df.columns:
            raise ValueError(f"度量列 '{m}' 不存在，可用列：{list(df.columns)}")

    grouped = df.groupby(dimension)[measures].agg(fn).reset_index()

    # 如果维度是日期，按时间排序
    if pd.api.types.is_datetime64_any_dtype(df[dimension]):
        grouped = grouped.sort_values(dimension)
        grouped[dimension] = grouped[dimension].dt.strftime("%Y-%m-%d")

    result = {
        "categories": grouped[dimension].astype(str).tolist(),
        "series": [
            {
                "name": m,
                "data": [round(v, 2) if not np.isnan(v) else None
                         for v in grouped[m].tolist()]
            }
            for m in measures
        ]
    }
    return result


def distribution(df: pd.DataFrame, measure: str, bins: int = 20) -> dict:
    """直方图数据：返回区间标签和频次"""
    if measure not in df.columns:
        raise ValueError(f"列 '{measure}' 不存在")
    series_data = df[measure].dropna()
    counts, edges = np.histogram(series_data, bins=bins)
    labels = [f"{edges[i]:.1f}~{edges[i+1]:.1f}" for i in range(len(counts))]
    return {
        "categories": labels,
        "series": [{"name": measure, "data": counts.tolist()}]
    }


def compare_categories(df: pd.DataFrame, dimension: str, measure: str) -> dict:
    """排名对比：单度量按值降序排列，适合水平条形图"""
    result = aggregate(df, dimension, [measure], agg_func="sum")
    # 排序（降序）
    paired = sorted(
        zip(result["categories"], result["series"][0]["data"]),
        key=lambda x: (x[1] or 0),
        reverse=True
    )
    cats, vals = zip(*paired) if paired else ([], [])
    return {
        "categories": list(cats),
        "series": [{"name": measure, "data": list(vals)}]
    }


def summary_stats(df: pd.DataFrame, measures: list[str]) -> dict:
    """KPI 卡片数据：每个度量的总和、均值、最大、最小"""
    stats = {}
    for m in measures:
        if m in df.columns and pd.api.types.is_numeric_dtype(df[m]):
            col = df[m].dropna()
            stats[m] = {
                "sum": round(float(col.sum()), 2),
                "mean": round(float(col.mean()), 2),
                "max": round(float(col.max()), 2),
                "min": round(float(col.min()), 2),
                "count": int(col.count())
            }
    return stats


# ─── CLI 入口 ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Data Visualizer Pro 预处理脚本")
    parser.add_argument("--input", required=True, help="输入文件路径 (csv/xlsx/json)")
    parser.add_argument("--goal", choices=["trend", "compare", "distribution", "summary"],
                        default="trend", help="分析目的")
    parser.add_argument("--dimension", default=None, help="维度列名（分组依据）")
    parser.add_argument("--measure", default=None,
                        help="度量列名，多个用逗号分隔，如 revenue,profit")
    parser.add_argument("--agg", default="sum",
                        choices=["sum", "mean", "count", "max", "min"],
                        help="聚合函数（默认：sum）")
    parser.add_argument("--bins", type=int, default=20, help="直方图分桶数（distribution 模式）")
    parser.add_argument("--limit", type=int, default=50,
                        help="输出最多保留多少个类别（避免图表过密，默认 50）")
    args = parser.parse_args()

    df = load_data(args.input)
    df = clean_data(df)

    measures = [m.strip() for m in args.measure.split(",")] if args.measure else []

    if args.goal == "trend":
        if not args.dimension or not measures:
            print("trend 模式需要 --dimension 和 --measure", file=sys.stderr)
            sys.exit(1)
        result = aggregate(df, args.dimension, measures, args.agg)

    elif args.goal == "compare":
        if not args.dimension or not measures:
            print("compare 模式需要 --dimension 和 --measure（单个）", file=sys.stderr)
            sys.exit(1)
        result = compare_categories(df, args.dimension, measures[0])
        # 限制类别数量
        if len(result["categories"]) > args.limit:
            result["categories"] = result["categories"][:args.limit]
            result["series"][0]["data"] = result["series"][0]["data"][:args.limit]
            print(f"[截断] 只保留前 {args.limit} 个类别", file=sys.stderr)

    elif args.goal == "distribution":
        if not measures:
            print("distribution 模式需要 --measure", file=sys.stderr)
            sys.exit(1)
        result = distribution(df, measures[0], bins=args.bins)

    elif args.goal == "summary":
        if not measures:
            measures = df.select_dtypes(include="number").columns.tolist()
        result = summary_stats(df, measures)

    # 写入同目录 _processed.json
    input_path = Path(args.input)
    output_path = input_path.with_name(input_path.stem + "_processed.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[输出] 已写入 {output_path}", file=sys.stderr)

    # stdout 输出 JSON 供 Claude 读取
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
