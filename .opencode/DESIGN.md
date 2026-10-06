# Ascentium Hackathon Toolkit — 方案设计（v2 · 人机共创版）

> 版本：v2（2026-09-28）
> 状态：设计定稿待确认 → 确认后按 §11 顺序实现
> 定位：本文件是 toolkit 全部技能的**唯一实现规格**；实现时必须对照本文件，偏离需回写。

---

## 1. 背景与目标

Ascentium AI Transformation Mini-hackathon（2026-10-13 · 深圳）：112 人 / 8 组 × 14 人，50 分钟实战（40′ 产出 + 10′ Showcase 准备），围绕 Quest A（2030 多哈亚运会门票营销）与 Quest B（成都熊猫基地全球化 IP）产出商业方案并 Showcase PK。

Toolkit 目标：让**每组 14 个人的创意与判断**在 50 分钟内被充分激发、投票、拼装成一套可路演的方案；AI 全程只做「主持 + 排版 + 脚手架」，**不替团队做创意/判断类决定**。

---

## 2. 核心定位（锁定）

1. **AI = Robot Facilitator（机器人主持人）**，对应 run-sheet 的 hackathon-robot 设定：串场、出题、计时、记录、排版。
2. **人 = 创意与判断核心**：出大创意、选市场、定 pilot 指标、选视觉方向。
3. **AI 做研究，团队做判断**：题卡已含核心数据；**insight 环节 AI 主动用 `agent-reach` 搜真实数据/报告/标杆**，把事实蒸馏成「带数字的洞察选项」供团队选择。研究工作量落在 AI，判断落在人。要避免的是**团队**做研究马拉松，不是 AI 做研究。
4. **6 个交付物 = 6 个「人的决定」**，AI 一次都不替团队拍板。
5. **品牌唯一来源**：`skills/ascentium-brand/brand-guideline.md`（Ascentium R1.10，含 Design Tokens §11）。
6. **流程弹性 > 流程纪律**：40 分钟节奏只是「建议 happy path」，不是硬脚本。现场有动态变化、时间吃紧、团队要跳关/换向/重来时，**人可自由调度任何元技能/阶段技能**，AI 必须顺应，不执拗于原定流程。
7. **全英文交付（English-only）**：受众语言为英文。所有技能正文（SKILL.md）、触发词、capture JSON 字段、输出 HTML、README/Playbook、Robot Facilitator 话术、HMW 提问**一律英文**。题卡本身即英文，保持一致。（仅 `brand-guideline.md` 为 Ascentium 官方中文源文件，作为唯一品牌依据保留中文，`ascentium-brand` 技能从中抽英文 token 与规则。）

---

## 3. 人机共创模型（双菱形 + 4 关卡）

每关遵循同一条共创回路：

```
AI 给脚手架/问题  →  团队发散(人人出点子)  →  团队收敛(投票/合并)  →  AI 结构化+排版  →  下一关
```

4 个关卡（对应 4 个 quest 技能）：
- **洞察门**（insight）：团队注入「市场真相」→ 收敛出「种子洞察」
- **创意门**（plan）：AI 发散并搭出 **2 套完整方案（A/B）** → 团队**选 A 或 B**（1 次决策）
- **论证门**（prove）：AI **直接出一版最合理的数字预测 + 推演**（无团队决策）
- **呈现门**（showcase）：团队选视觉/主张 → AI 生成海报 + 路演稿

### 3.1 灵活调度模型（关键）

所有技能/协议**原子化、可独立触发**，三种运行形态并存：

1. **全流程**：`facilitator` 按 happy path 串场（默认）。
2. **单关卡**：团队只要某阶段产物（如「直接做海报」），就只调 `poster`；只要路演稿就调 `showcase`。
3. **单协议**：团队只要某个协作动作（如「再投一次票」），就只调 `facilitation` 的「点投票」协议。

**人类的调度权**：随时可喊「跳过研究 / 直接创意 / 重投票 / 换市场 / 我们只剩 8 分钟 / 重来这关」，AI 立即顺应并调整，不追问「为什么偏离流程」。

---

## 4. 技能总览（7 个技能 + 1 个编排 Agent）

| # | 技能 | 类型 | 依赖 | 产出 |
|---|---|---|---|---|
| 0 | `ascentium-brand` | 地基 | 无 | tokens.css / 组件规则 / 三类模板 |
| 1 | `facilitation` | 元技能 | 无 | 协作协议库 + 节奏模板 + 串场话术 |
| 2 | `insight` | 阶段技能 | brand + facilitation | insight-brief.html |
| 3 | `plan` | 阶段技能 | insight | campaign-plan.html |
| 3b | `poster` | 阶段技能（Create） | plan | poster.html |
| 4 | `prove` | 阶段技能 | plan | proof.html |
| 5 | `showcase` | 阶段技能 | 前三者 + poster | pitch-deck.html + prompt-pack.html（内嵌 poster） |
| 6 | `facilitator`（Agent） | 编排 | 全部 | 40 分钟一键串场 |
| 7 | `README.md` | 说明 | — | Quest Playbook（交付物↔技能↔模板） |

复用项（不新建，直接可用）：`agent-reach`（**insight 环节主动研究，为菜单提供数据依据**）、`creative-concept`（plan 阶段创意发散子技能，置于 `plan/sub-skills/`）。

---

## 4A. 交付物 ↔ 技能 覆盖核对（对照题卡原文）

> 题卡 §03「Your 5-minute pitch — The MVP Plan」。逐项核对，确保零遗漏。

| # | 交付物（A 原话 / B 原话） | 覆盖技能 | 人的决定 |
|---|---|---|---|
| 1 | Pilot **campaign** concept（2 Asian markets, 3mo）／Pilot **membership** design（2 overseas markets, 3mo） | `plan`（creative-concept → `offering`） | 大创意 + 会员设计 |
| 2 | Experiment plan & **measurement setup** | `plan`（`experiment.measurement_setup`）+ `prove` | 选市场 / 成功口径 |
| 3 | Hero visual / poster ／ **Founding-member offer** + hero visual | `plan`（`offering.founding_offer`）+ **`poster`**（hero visual） | 视觉方向 |
| 4 | **A most-reasonable pilot forecast + derivation logic**（一版最合理的数字预测；每条用 Scout Report 标杆佐证并写出推演链 benchmark → assumption → formula） | `prove`（单屏 `proof.html`，capture 内嵌） | —（AI 出） |

**题卡 Arsenal 技能链 ↔ 本设计映射**：

| 题卡 Arsenal | 本设计技能 | 覆盖方式 |
|---|---|---|
| Insight: Market Research · Audience Analysis · Benchmark Analysis（A）／Company Profiler (IP audit) · Audience Analysis · Market Research（B） | `insight` | AI 脚手架（组织画像/标杆对照）+ 团队「市场真相」 |
| Create: Creative Concept · MVP Pilot Design · Poster | `plan`（创意/试点）+ **`poster`**（海报） | 人发散投票 + AI 拼装 |
| Prove: Cost-Benefit · Data Analysis & Viz | `prove` | Pilot 预期指标 + 推演逻辑（单屏看板）；Go/No-Go、成本收益、scale-up 已移除 |
| ★ Showcase Report Agent (AUTO) | `showcase`（AUTO） | 一键聚合 |

**本轮对照修正点（已回写 §7）**：
1. 交付物 #2「experiment + measurement setup」显式落到 `campaign-plan.html` capture 的 `experiment.measurement_setup` 字段（原设计漏了测量口径）。
2. 交付物 #3 B 的「Founding-member offer」落到 `campaign-plan.html` capture 的 `offering.founding_offer`，并由 showcase 打上海报（原设计只做了「海报」，漏了「offer」本体）。
3. 题卡明示「Budget allocation is part of the solution」→ capture 新增 `budget.allocation` 且为**人的决定**（原设计未显式）。
4. **Prove 简化（本轮）**：只保留 pilot 预期指标 + 推演逻辑；移除 Go/No-Go、Cost-Benefit/ROI、scale-up、KPI 看板 mock。
5. 指标必须「用 Scout Report 标杆佐证」并写出推演链 → `metrics` 用 `benchmark_ref` + `derivation`（benchmark → assumption → formula）。



---

## 5. 元技能设计：`facilitation`（重点）

> 这是本 toolkit 的「共创引擎」，4 个 quest 技能都调它。设计如下，**需用户确认后再建**。

### 5.1 定位
把任意 AI 变成「会主持 14 人 × 40 分钟共创工作坊的 Robot Facilitator」。它不产出内容，只提供**协议 + 节奏 + 话术 + 采集契约**。

### 5.2 主持人铁律（Prime Directives，硬约束）
1. **AI 不替团队做决定**：创意、选市场、定指标、定阈值、选视觉——一律由人投票/表态，AI 只记录与执行。
2. **先发散后收敛**：任何一关都先让多人出点子，再收敛，禁止上来就收敛。
3. **强制计时**：每关有硬时间盒，到点推进，防止完美主义与跑题。
4. **中立记录**：观点冲突时不偏向，如实聚类；不替团队「润色掉」分歧。
5. **AI 代为研究（choice-first 的数据底座）**：`agent-reach` 在 insight 环节**主动**用于搜集数据/报告，把事实变成有价值的**数据化洞察选项**；团队只做选择。克制 = **团队**不做研究马拉松、AI 不堆原始数据，而不是 AI 不研究。
6. **一轮一决策 + 回顾内联**：每个 turn **只出一个 menu 就停**、等团队回复（禁止自问自答、禁止一回合跑多关）；每轮结尾先**回顾**（过程 + 产物路径），再把下一步**选项直接打印在对话里**。**HTML 是记录，对话才是决策界面**（不让用户去浏览器打开 HTML 才知道要选什么）。

### 5.3 协议库（Protocol Library）
| 协议 | 用途 | 机制 | 默认时长（14 人） |
|---|---|---|---|
| **选项菜单 Option Menu**（默认，每关先跑） | 不让人面对空白页 | AI 先出 **6–8 个有依据的候选**（来自题卡+方法论），团队**选 N 个**，可 `+1` 自选 | 30″–1′ |
| **HMW 提问** | 把种子洞察转成发散问题 | 一句「How might we…」，正面框架、不过宽不过窄 | 即时 |
| **静默发散** | 人人出点子、避免从众 | 每人静默写 1–2 条，先写后说 | 2′ |
| **轮报 Round-robin** | 快速收集、人人有份 | 每人 15″ 报一条，AI 记关键词，期间不评判 | 3′ |
| **亲和聚类** | 把散点归主题 | AI 把 N 条点子聚成 3–4 个主题 | 即时（AI） |
| **点投票 Dot-vote** | 民主收敛 | 每人 2 票，票数前 2–3 名晋级 | 2′ |
| **1-2-4-All** | 深挖单一赢家创意 | 个人→两人→四人→全员，逐级合并补充 | 5′ |

> **Choice-first 铁律**：每个 HITL 关卡**先出菜单**（AI 用 research/方法论给出 6–8 个候选），团队**做选择题**而非填空题，并始终保留 `+1 of our own`。详见 `skills/facilitation/references/option-menu.md`。

### 5.4 节奏模板（Pacing Template）
14 人 × 40 分钟标准节奏（各关时间盒见 §9）。AI 每关按「**先出菜单 → 团队选 → 收敛 → 采集 → 推进**」执行，带 T-minus 倒计时提醒。

### 5.5 串场话术（Facilitator Script Patterns）
- 机器人 cosplay 设定：机械腔、hackathon-robot 签名、cheerful one-liner（呼应 run-sheet）。
- **全英文**：提问、开场、时间提醒、鼓励语一律英文（受众为英文使用者）。
- 每关标准开场：一句话说清「本关要做什么 + 你有几分钟 + 你要产出什么」。
- 时间提醒话术：剩 3′ / 1′ 各播报一次。

### 5.6 采集契约（Capture Contract）
- **HITL 门**：AI 在每关发散/收敛后**必须停下**，显式请求团队输入，不得跳过。
- **采集卡（内嵌 JSON in HTML）**：统一记录格式（见各 quest 技能的 capture schema）。
- **输入类型**：点子列表 / 票数 / 单选 / 阈值数字 / 一句话主张。

### 5.7 反模式（Anti-patterns）
- ❌ AI 自动替团队写出「大创意」并直接采用
- ❌ 跳过发散直接给答案
- ❌ 为凑信息量而长时间上网搜
- ❌ 让少数人包场发言（应强制轮报/静默发散）
- ❌ **执拗于流程**：团队已明确要跳过/加速/换向，AI 仍按原脚本追问

### 5.8 动态调度与降级（弹性）
AI 必须在每个关卡**持续感知剩余时间 + 团队意图**，动态调整，不把流程当死规则。

- **时间感知**：每关开始时对表，剩不足标准时长即自动切「快模式」。
- **降级模式（快模式）**：
  - 发散降级：静默发散 → 直接让 2–3 个活跃成员提主意（省 2′）。
  - 收敛降级：点投票 → 主持人直接提 2 个候选请团队点头（省 2′）。
  - 关卡跳过：团队说「研究够了」就跳过洞察发散，直接进创意。
  - 关卡合并：时间紧时把「论证 + 呈现」合并，AI 后台并行拼装。
- **人类可随时**：喊停、跳关、回退、重投票、换市场、换视觉方向、单独重跑某协议。
- **AI 的回应**：只确认一句「收到，切到 X」，不劝返、不解释偏离。

---

## 6. 地基技能设计：`ascentium-brand`

- **定位**：品牌唯一来源的执行器。
- **输入**：读 `skills/ascentium-brand/brand-guideline.md`。
- **输出**：
  - `references/tokens.css`（CSS 变量）
  - `references/typography.md`（字体层级）
  - `references/component-rules.md`（按钮/卡片/海报/PPT/看板组件规则）
- **关键 token**：`--ascentium-orange #FF6611`、`--ascentium-midnight #0F1514`、字体栈 `"Poppins","Noto Sans SC","PingFang SC","Microsoft YaHei",Arial,sans-serif`；Upward Arrow 只用品牌色、不拉伸、方向向上。
- **硬规则**：一切视觉色值/字体/间距必须引用本技能，禁止凭记忆写样式。

---

## 7. 阶段技能设计（每个含 facilitate / capture / assemble）

### 7.1 `insight`（洞察门 · 8 分钟）
- **目标**：产出一份**厚洞察**：市场趋势 + 人群分层（含 JTBD）+ 关键时刻 + 市场真相 → **焦点包（Focus Bundle）** + 数据化关键洞察 → 种子洞察。**光有真相不够，必须有人群与需求分析**，否则下游创意无根。
- **输入**：Quest 题卡（含 Scout Report）。
- **输出**：`insight-brief.html`（decisions 内嵌于 `id="capture"` 块）。**渐进式生成**：第一段研究产出即建文件，之后每步**重写**该文件（living brief）。
- **只做 1 个决策**（原为 5 个选择点）：
  - **关键洞察 Key Insights（选 2–3）**：AI 蒸馏 **~6 条数据化洞察**，团队**选 2–3** 进入 `plan` —— **唯一决策**。
  > **焦点包（Focus Bundle = 人群 × 时刻 × 趋势）/ trends / moments / truths 全部由 AI 策展**（标注 `AI pick`），brief 中**全量列出**，团队可随时一句「redo …」覆盖。
- **facilitate（串场）**：
  1. **建 brief + 研究（AI，无决策）**：读题卡 → `agent-reach`/`business-research`/`audience-analysis`/`swot-analysis` → 蒸馏**全量菜单**：趋势 ~6–8 · 人群 ~6–8 · 候选时刻 ~6–8 · 候选真相 ~6–8（各带事实/数字 + 来源）。第一段产出即**创建 `insight-brief.html`**，每步**重写**。
  2. **AI 策展焦点包（AI，无决策）**：合成 ~6 个焦点包 → **AI 选最强的 1–2 个**（`AI pick`）→ 重写 brief（全量列出，其余灰显）；由其导出**关键时刻**。
  3. **起草关键洞察（AI，无决策）**：蒸馏 ~6 条数据化洞察 → 重写 brief（全量列出）。
  4. **关键洞察（团队，唯一决策）**：内联呈现 ~6 条 → 团队**选 2–3** 进 `plan` → 重写 brief（选中高亮）。
  5. **种子洞察（AI）**：由所选洞察合成一句话张力。
  > 每个区块**全量列出候选**：选中 `SELECTED`（accent 高亮）/ 未选 `is-parked`（灰显）/ AI 策展 `AI PICK`。见 §5.3 Option Menu。
- **capture（内嵌于 `insight-brief.html` 的 `id="capture"` JSON 块）**：
  ```json
  quest: A|B
  org_profile: {assets, constraints}
  benchmark: {gold_standard, cautionary_tale, arena}
  trends:  [ {id, trend, why_it_matters, source, ai_pick} ]   # 全量，AI pick 标记
  truths:  [ {id, text, source, ai_pick} ]                    # 全量
  segments:[ {id, name, who, job_functional, job_social, job_emotional, barrier, trigger, selected} ]
  moments: [ {id, text, ai_pick} ]                            # 全量
  focus_bundles: [ {id, name, segment_ids, moment_id, trend_id, why, ai_pick} ]  # AI 策展，全量
  selected_focus: [1]
  moment_of_truth: {when, where, event}                       # 由所选焦点导出
  swot: {strengths, weaknesses, opportunities, threats}
  key_insights: [ {id, text, evidence, source, selected} ]    # 唯一决策，全量
  selected_insights: [1, 4]
  seed_insight: "一句话张力"                                   # AI 由所选焦点 + 洞察合成
  ```
- **assemble**：`insight-brief.html`（战报速览 / 组织画像 / **焦点包** / 市场趋势（全量）/ 标杆对照 / **人群分层卡**（全量）/ 市场真相与时刻（全量）/ **关键时刻** / 种子洞察高亮 / **关键洞察**（全量））。内容区 **80% 屏宽（上限 1600px）**；**禁用侧边装饰栏**（§5.2）。
- **吸收/改造**：`business-research`（仅作标杆对照脚手架）；`audience-analysis` 能力升级为 **STP + JTBD + 趋势 + 关键时刻**（见 `references/insight-method.md`）。

### 7.2 `plan`（创意门 · 14 分钟 · 最重）
- **目标**：**先锚定（人群 + 时刻）再发散**，让创意有根；AI 把创意拼成 **2 套完整方案（A/B）**，团队**只做 1 次决策 —— 选 A 或 B**。
- **输入**：`insight-brief.html` capture（所选焦点包 + key insights + moment）。
- **输出**：`campaign-plan.html`（**渐进式生成**：第一段产出即建文件，之后每步重写；最终**两套方案 A/B 全量列出**，选中高亮；capture 内嵌）+ `poster-a/b/c.html` + `poster.html`。
- **facilitate（AI 全跑，团队只决策 1 次）**：
  1. **发散（AI）**：`creative-concept` —— 锚定人群 × 时刻 → 1 个 HMW → 创意方法 → **~6 个候选创意**。
  2. **收敛 + 搭 A/B（AI）**：把 ~6 收敛为 **2 套完整、彼此不同的 campaign**（A/B）；各含 `opportunity-definition`(5 要素) + 定位(Moore) + offering + 4Ps + 2 试点市场 + 实验计划 + 预算（题卡 War Chest）。
  3. **制图（AI）**：用 `poster` 为每套出主视觉（默认方向；独立 `/poster` 阶段可再定风格）。
  4. **决策（团队 · 唯一 1 次）**：AI 内联呈现两套完整方案（A/B）→ 团队**选 1**（可 +1 自选）。
- **capture（内嵌于 `campaign-plan.html` 的 `id="capture"` JSON 块）**：
  ```json
  quest, selected_insights
  anchor: {segment, job, moment, mechanic, desire}
  hmw
  ideas: [ {id, name, one_line, insight, mechanic} ]   # ~6，全量
  ai_shortlist: [2, 5]                                  # AI 收敛
  variants: {                                           # 两套完整方案
    A: {name, slogan, proposition, offer, positioning, mix, pilot, budget},
    B: {name, slogan, proposition, offer, positioning, mix, pilot, budget}
  }
  chosen_variant: "A"                                   # 团队唯一决策
  poster: {visual_direction, one_liner}
  ```
- **assemble**：`campaign-plan.html`（**两套方案全量** + 选中高亮：锚点/场景 / 定位(Moore) / A=活动概念·B=会员设计 + 创始 offer / 4Ps / 试点实验 + 测量设置 / 预算切分）。
- **吸收/改造**：`opportunity-definition`（去 AI 口径→营销机会点）；`creative-concept`（人群+场景锚定 + HMW + 创意方法 → ~6 ideas，吸收自原 brainstorming + creative-concept.md）；`marketing-plan`（定位/4Ps）。

### 7.3 `prove`（论证门 · 8 分钟）
- **目标**：AI 依据 insights + plan **直接产出一版最合理的数字预测**（漏斗 reach→engagement→conversion→outcome + 指标目标 + 推演链），**无团队决策**。输出一屏 `proof.html`。**不含** Go/No-Go、成本收益/ROI、scale-up。
- **输入**：`insight-brief.html` capture（所选洞察 + 标杆）+ `campaign-plan.html` capture（pilot 市场/窗口/budget）+ 题卡 Scout Report 标杆。
- **输出**：`proof.html`（单屏，capture 内嵌）。
- **facilitate（AI 全跑，无 HITL）**：
  1. **选指标集（AI）**：从漏斗里挑最能证明本 pilot 假设的 3–5 个指标。
  2. **定最合理的目标（AI）**：每条锚定 Scout Report 标杆，取保守可辩护的数值。
  3. **写推演链（AI）**：`benchmark → assumption → formula → target` + 一句逻辑。
  4. AI 出单屏（漏斗 + 指标卡 + 推演行）。
- **capture（内嵌于 `proof.html` 的 `id="capture"` JSON 块）**：
  ```json
  pilot: {window, markets, budget}
  metrics: [ {name, dimension, target, derivation: {benchmark_ref, formula, assumptions, logic}} ]
  ```
- **assemble**：`proof.html` 单屏（pilot 漏斗 + 指标卡 + 推演行），品牌随题卡 accent。
- **保留但不再调用**：`sub-skills/campaign-metrics`、`sub-skills/data-visualizer-pro`、`references/cost-benefit.md` 留在库中（休眠），本门不调用。

### 7.4 `showcase`（呈现门 · 8 分钟 · AUTO）＝题卡「Showcase Report Agent (AUTO)」
- **目标**：**多形态**呈现——5 种 storyline + signature element 承载核心创意 + 可选加分媒体（歌曲/视频/图片）。避免十组同一模板。
- **输入**：上游三个 HTML 的内嵌 capture（`insight-brief.html` / `campaign-plan.html` / `proof.html`）。
- **输出**：`pitch-deck.html`（可配置 storyline）+ `prompt-pack.html`（可选）；**内嵌** `poster`（由 `poster` 技能产出）。
- **facilitate**：
  1. **团队选 storyline**（S1 Classic / S2 Hero's Journey / S3 Big Reveal / S4 Demo / S5 Trailer）——决定 deck 形状与 signature element。
  2. 团队选视觉方向 + 一句话主张。
  3. AI 拼装 signature + deck（`data-storyline` 驱动，AUTO）。
  4. **加分媒体（团队可选）**：AI 写 `prompt-pack.html`（Suno/Runway/GPT 提示词脚本）→ 团队到工具站生成 → 拿回文件。
  5. AI 把结果**按 storyline 分散嵌入对应 slide**（图→poster、视频→storyboard、歌→lyric）。
  6. 团队 30″ 预演 + 微调。
- **capture**：`{storyline, signature, visual_direction, one_liner, bonus_media, tweaks}`。
- **assemble**：
  - **内嵌** `poster.html`（由独立 `poster` 技能产出，作为 Classic / Big Reveal 的 `poster` beat + poster signature）。
  - pitch-deck.html（**可配置 5 storylines**）：title / problem / insight / **poster** / **storyboard** / **prototype** / **lyric** / strategy / moments / experiment / budget / funnel / proof / ask，按 storyline 选取顺序；全屏自适应 + ←/→ + F 全屏；**核心创意由 signature element 承载**（不靠文字描述）。
  - prompt-pack.html（**提示词脚本包**）：歌曲/视频/图片三类，从 campaign-plan capture 自动填好，复制即用；媒体占位符预置在 deck（图→poster、视频→storyboard、歌→lyric、加分→ask）。
- **signature element（创意载体）**：poster（整屏海报）/ storyboard（6 帧旅程）/ prototype（手机 mock）/ lyric（anthem 歌词）——对应 5 storylines。
- **加分媒体工具**：歌曲 **Suno**、视频 **Runway Gen-3**、图片 **GPT**（每类 1 主 1 备）。
- **吸收/改造**：`pitch-narrative.md`（5 storylines + beat 库）、`media-prompts.md`（工具指南）。deck 直接由 `templates/pitch-deck.html` 产出；海报本体见 `poster`。无子技能。

---

## 8. 编排层：`facilitator`（Agent）

- **定位**：Robot Facilitator 的人格化 manifest + **建议路径**（非硬状态机）。
- **职责（happy path）**：按 §9 节奏依次调 `facilitation` 协议 + 4 个 quest 技能；维护 HTML 产物链（decisions 内嵌于各自 `id="capture"` 块）；到点推进；打包提交。
- **职责（弹性）**：监听团队指令，支持「跳关 / 回退 / 重跑 / 单技能直调 / 快模式压缩」；见 §5.8。
- **人格**：hackathon-robot 机械腔 + cheerful one-liner。
- **动态场景应对表（示例）**：

| 现场信号 | AI 应对 |
|---|---|
| 「研究够了，直接出创意」 | 跳过洞察发散，直接用题卡数据兜底种子洞察，进 `plan` |
| 「我们只剩 8 分钟」 | 切快模式：压缩发散/收敛，AI 后台并行拼装海报+看板 |
| 「这个投票结果不对，重来」 | 重跑 `facilitation` 点投票协议，不重跑整关 |
| 「只要一张海报」 | 只调 `poster`，用 campaign-plan capture 拼装 |
| 「换个试点市场」 | 只改 `campaign-plan.html` capture 的 pilot 字段，重出论证 |
| 「跳过 SWAT/研究，直接搞 slogan」 | 只调 `facilitation` 的 HMW + 静默发散出 slogan |



---

## 9. 40 分钟节奏总表

| 时间 | 关卡 | 谁主导 | AI 干什么 | 人的决定 |
|---|---|---|---|---|
| 0–2′ | 开题 | AI | 30″ 战报速览 + 抛第一问 | — |
| 2–10′ | 洞察门 | 人 | 研究 → living brief → AI 策展 → ~6 关键洞察 | 关键洞察（2–3） |
| 10–22′ | 创意门 | 人 | 搭 2 套完整方案（A/B）+ 主视觉 | 选 A 或 B（1 次） |
| 22–30′ | 论证门 | AI | 出一版最合理的数字预测 + 推演 | — |
| 30–38′ | 呈现门 | 人 | 生成海报 + 路演稿 | 视觉方向 + 主张 |
| 38–40′ | 收敛提交 | AI | 一键打包 | 确认 |

> run-sheet 官方为「40′ 产出 + 10′ Showcase 准备」= 50′；本设计以 40 分钟为创意核心。

---

## 10. 文件结构约定

```
.opencode/
├── DESIGN.md · README.md            # 文档
├── quest-card.md                    # Quest 配置契约（数据 + 视觉参数 + Output layout）
├── evaluation-rubric.md             # 方案评分卡
├── skills/                          # 技能：一技能一目录；opencode 递归发现 **/SKILL.md
│   ├── insight/                     # 洞察门
│   │   └── sub-skills/  business-research · audience-analysis · swot-analysis
│   ├── plan/                        # 策划门
│   │   └── sub-skills/  creative-concept · opportunity-definition
│   ├── poster/                      # 海报（Create 阶段，独立）
│   ├── prove/                       # 论证门（单屏 pilot forecast A/B）
│   │   └── sub-skills/  campaign-metrics · data-visualizer-pro（保留·休眠，不调用）
│   ├── showcase/                    # 呈现门（AUTO）
│   ├── agent-reach/                 # 实时研究（insight 调用）
│   ├── facilitation/                # 共创引擎（含 option-menu）
│   └── ascentium-brand/             # 品牌执行器（tokens + 规则 + brand-guideline.md）
├── agents/                          # facilitator.md · runner.md · researcher.md
└── commands/                        # start · insight · plan · poster · prove · showcase · evaluate · run
```

**输出位置（运行约定）**：Facilitator 与 runner 两种模式都把本轮全部产物写入仓库根的 **`artifacts/Quest<ID>-<NN>/`**（每题一轮一子目录：`QuestA-01` → `QuestA-02` ……）。`/run` 新建轮次目录；`/start` **只做 briefing**（不建目录、不产产物），由**第一个写产物的关卡**建目录；单闸命令并入该题最新轮次目录（无则建 `-01`）；**不覆盖旧轮次**。每轮含各阶段 HTML 产物（decisions 内嵌于各自 `id="capture"` 块，**无 YAML/Markdown**）；构建脚本以 `--dir artifacts/Quest<ID>-<NN>/` 运行。`artifacts/` 已 gitignore；签入示例在 `demo-examples/`。详见 `quest-card.md` → *Output layout*。

> **opencode 发现约定 = 递归 `**/SKILL.md`**。四阶段技能 `insight` / `plan` / `prove` / `showcase` 各自带 `sub-skills/`；`poster`、`agent-reach` **平铺为顶层技能**（逻辑上归 `plan` / `insight`，被它们引用）。
> 命名约定：**技能/Agent/Command 名一律不带 `quest`**（skill: `insight`/`plan`/`poster`/`prove`/`showcase`；agent: `facilitator`/`runner`/`researcher`；command: `/start`、`/run` 等）。

每个技能目录：`SKILL.md`（frontmatter `name` + `description`，**触发词全英文**）+ `references/` +（可选）`templates/`、`scripts/`、`sub-skills/`。
**语言约定（English-only）**：所有 SKILL.md 正文、references、templates、scripts 注释、capture JSON 字段、输出 HTML 文本，一律英文；中文字样仅在 `brand-guideline.md` 源文件与本 DESIGN.md / AGENTS.md 内部文档出现。

---

## 11. 实施顺序与验收标准

| 顺序 | 技能 | 验收标准 |
|---|---|---|
| 1 | `ascentium-brand` | 能输出 tokens.css + 三类模板；抽查色值=手册一致 |
| 2 | `facilitation` | 协议/节奏/话术/采集契约齐全；4 个 quest 技能可调用 |
| 3 | `insight` | Quest A/B 各跑一遍：14 人洞察 → 种子洞察落 `insight-brief.html`（capture 内嵌） |
| 4 | `plan` | 投票选赢家 → 完整方案框架（定位/4Ps/试点/预算） |
| 5 | `poster` | 专业 campaign poster（9 段式：客户 logo/主视觉/offer/数据带/CTA+QR） |
| 6 | `prove` | 一版最合理的数字预测 + 推演逻辑（单屏） |
| 7 | `showcase` | 5 storylines 路演稿 + 媒体占位符（内嵌 poster） |
| 8 | `facilitator` + `README` | 一键串全场 40 分钟，冒烟通过 |

---

## 12. 待确认点

1. `facilitation` 元技能的 5.2–5.8 设计是否 OK（尤其「主持人铁律」「协议库」「动态调度与降级」）。
2. 各 quest 技能的 capture（内嵌 JSON）与 assemble 边界是否合理。
3. 40 分钟节奏时间盒是否需要微调。
4. 实现顺序是否按 §11。
5. 弹性调度（§3.1 / §5.8 / §8）是否到位：还有没有其他「现场动态」场景需要覆盖？
6. §4A 交付物覆盖核对是否无误：6 项交付物 + 5 处修正点是否都已闭环？
