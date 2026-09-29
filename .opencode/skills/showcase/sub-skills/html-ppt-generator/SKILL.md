---
name: html-ppt-generator
description: Convert markdown content into a high-fidelity HTML presentation (mobile/desktop slides) with local images and "visual intelligence" layout. Used by the showcase stage to build an HTML slide deck from a markdown outline. Triggers: "html ppt", "markdown to slides", "html presentation", "build slides".
---

# HTML PPT Generator (v3.0 - Visual Intelligence)

## 核心任务
将 Markdown 内容转化为高保真的、支持本地配图、且具备“视觉智能布局”的移动端/桌面演示 PPT (HTML格式)。

## 1. 处理流程 (Mandatory Steps)
1. **内容分片**：将 Markdown 按照标题或逻辑块划分为幻灯片。
2. **角色识别**：识别每页的角色 (Cover, Agenda, Chapter, Content, QA)。
3. **视觉逻辑分析 (Visual Logic)**：
   - 检查该页图片的**数量**。
   - 分析图片的**纵横比 (Orientation)**：
     - 如果是**扁平图/横图** (Aspect Ratio > 1)，优先使用上下布局。
     - 如果是**竖图/长图** (Aspect Ratio < 1)，优先使用左右布局。
     - 如果是**超大图/高信息量图**，单独占一页全屏展示。
     - 如果是**连续多图**，采用堆叠布局。
4. **输出 JSON**：根据分析结果，选择最匹配的 `type` 并输出 JSON 数据。

## 2. 布局字典 (Atomic Layouts)

### 基础页面
- `cover`: 封面 (title, subtitle, author, date)。
- `agenda`: 目录 (title, items: [{title, subtitle}])。
- `chapter`: 章节过渡 (chapter_label, title, subtitle)。**注意：不再支持背景图。**
- `qa`: 结语页 (title, subtitle)。

### 内容与配图布局
- `layout_h_split`: **上下布局**。适用于横向配图。文字在上，图片在下。
- `layout_v_split`: **左右布局**。适用于纵向配图。文字在左，图片在右。
- `layout_full_media`: **全屏大图**。适用于复杂图表。图片居中占满，下方可配一句话描述。
- `layout_double_stack`: **多图堆叠**。适用于连续 2 张图片，垂直堆叠排列。
- `content_two_column`: 纯文字对比。
- `content_tiled`: 3 列卡片墙。

## 3. 输出格式要求 (JSON Only)
输出一个合法的 JSON 代码块，包含 `title` 和 `slides` 数组。
**严禁输出任何 HTML 代码，严禁使用图片作为背景。**

```json
{
  "title": "标题",
  "slides": [
    {
      "type": "layout_v_split",
      "title": "竖图案例",
      "content": "<p>描述文字</p>",
      "image": "path/to/vertical_img.jpg"
    }
  ]
}
```
