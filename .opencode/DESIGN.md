# Ascentium Hackathon Toolkit — 方案设计（v2 · 人机共创版）

> 版本：v2（2026-09-28）
> 状态：设计定稿待确认 → 确认后按 §11 顺序实现
> 定位：本文件是 toolkit 全部技能的**唯一实现规格**；实现时必须对照本文件，偏离需回写。

---

## 1. 背景与目标

Ascentium AI Transformation Mini-hackathon（2026-10-13 · 深圳）：112 人 / 8 组 × 14 人，50 分钟实战（40′ 产出 + 10′ Showcase 准备），围绕 Quest A（2030 多哈亚运 SEA 门票营销）与 Quest B（成都熊猫基地全球化 IP）产出商业方案并 Showcase PK。

Toolkit 目标：让**每组 14 个人的创意与判断**在 50 分钟内被充分激发、投票、拼装成一套可路演的方案；AI 全程只做「主持 + 排版 + 脚手架」，**不替团队做创意/判断类决定**。

---

## 2. 核心定位（锁定）

1. **AI = Robot Facilitator（机器人主持人）**，对应 run-sheet 的 FACI-01~08 设定：串场、出题、计时、记录、排版。
2. **人 = 创意与判断核心**：出大创意、选市场、定指标、定 Go/No-Go、选视觉方向。
3. **AI 做研究，团队做判断**：题卡已含核心数据；**insight 环节 AI 主动用 `agent-reach` 搜真实数据/报告/标杆**，把事实蒸馏成「带数字的洞察选项」供团队选择。研究工作量落在 AI，判断落在人。要避免的是**团队**做研究马拉松，不是 AI 做研究。
4. **6 个交付物 = 6 个「人的决定」**，AI 一次都不替团队拍板。
5. **品牌唯一来源**：`skills/ascentium-brand/brand-guideline.md`（Ascentium R1.10，含 Design Tokens §11）。
6. **流程弹性 > 流程纪律**：40 分钟节奏只是「建议 happy path」，不是硬脚本。现场有动态变化、时间吃紧、团队要跳关/换向/重来时，**人可自由调度任何元技能/阶段技能**，AI 必须顺应，不执拗于原定流程。
7. **全英文交付（English-only）**：受众语言为英文。所有技能正文（SKILL.md）、触发词、YAML 字段、输出 HTML、README/Playbook、Robot Facilitator 话术、HMW 提问**一律英文**。题卡本身即英文，保持一致。（仅 `brand-guideline.md` 为 Ascentium 官方中文源文件，作为唯一品牌依据保留中文，`ascentium-brand` 技能从中抽英文 token 与规则。）

---

## 3. 人机共创模型（双菱形 + 4 关卡）

每关遵循同一条共创回路：

```
AI 给脚手架/问题  →  团队发散(人人出点子)  →  团队收敛(投票/合并)  →  AI 结构化+排版  →  下一关
```

4 个关卡（对应 4 个 quest 技能）：
- **洞察门**（insight）：团队注入「市场真相」→ 收敛出「种子洞察」
- **创意门**（plan）：团队发散大创意 → 投票选赢家 → AI 搭成完整方案
- **论证门**（prove）：团队挑指标 + 定阈值 → AI 建 KPI 看板
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
| 2 | `insight` | 阶段技能 | brand + facilitation | insight-brief.html + insight.yaml |
| 3 | `plan` | 阶段技能 | insight | campaign-plan.html + plan.yaml |
| 3b | `poster` | 阶段技能（Create） | plan | poster.html |
| 4 | `prove` | 阶段技能 | plan | proof.html + metrics.yaml |
| 5 | `showcase` | 阶段技能 | 前三者 + poster | pitch-deck.html + prompt-pack.html（内嵌 poster） |
| 6 | `facilitator`（Agent） | 编排 | 全部 | 40 分钟一键串场 |
| 7 | `README.md` | 说明 | — | Quest Playbook（交付物↔技能↔模板） |

复用项（不新建，直接可用）：`agent-reach`（**insight 环节主动研究，为菜单提供数据依据**）、`creative-concept`（plan 阶段创意发散子技能，置于 `plan/sub-skills/`）。

---

## 4A. 交付物 ↔ 技能 覆盖核对（对照题卡原文）

> 题卡 §03「Deliverables · the MVP, not the master plan」。逐项核对，确保零遗漏。

| # | 交付物（A 原话 / B 原话） | 覆盖技能 | 人的决定 |
|---|---|---|---|
| 1 | Pilot **campaign** concept（2 SEA markets, 3mo）／Pilot **membership** design（2 overseas markets, 3mo） | `plan`（creative-concept → `offering`） | 大创意 + 会员设计 |
| 2 | Experiment plan & **measurement setup** | `plan`（`experiment.measurement_setup`）+ `prove` | 选市场 / 成功口径 |
| 3 | Hero visual / poster ／ **Founding-member offer** + hero visual | `plan`（`offering.founding_offer`）+ **`poster`**（hero visual） | 视觉方向 |
| 4 | **KPI dashboard mock**（仅 A 明列；B 由 measurement setup 隐含） | `prove`（dashboard） | 样例数字 |
| 5 | Go / no-go criteria for scale-up | `prove`（threshold_go/no_go） | 阈值 |
| 6 | **3–5 self-defined MVP sub-metrics**（no fixed numbers，用 Scout Report 标杆佐证，证明预测 Victory Conditions） | `prove`（metrics.benchmark_ref） | 挑指标 |

**题卡 Arsenal 技能链 ↔ 本设计映射**：

| 题卡 Arsenal | 本设计技能 | 覆盖方式 |
|---|---|---|
| Insight: Market Research · Audience Analysis · Benchmark Analysis（A）／Company Profiler (IP audit) · Audience Analysis · Market Research（B） | `insight` | AI 脚手架（组织画像/标杆对照）+ 团队「市场真相」 |
| Create: Creative Concept · MVP Pilot Design · Poster | `plan`（创意/试点）+ **`poster`**（海报） | 人发散投票 + AI 拼装 |
| Prove: Cost-Benefit · Data Analysis & Viz | `prove` | 子指标 + 看板 + 成本收益 |
| ★ Showcase Report Agent (AUTO) | `showcase`（AUTO） | 一键聚合 |

**本轮对照修正点（已回写 §7）**：
1. 交付物 #2「experiment + measurement setup」显式落到 `plan.yaml` 的 `experiment.measurement_setup` 字段（原设计漏了测量口径）。
2. 交付物 #3 B 的「Founding-member offer」落到 `plan.yaml` 的 `offering.founding_offer`，并由 showcase 打上海报（原设计只做了「海报」，漏了「offer」本体）。
3. 题卡明示「Budget allocation is part of the solution」→ `plan.yaml` 新增 `budget.allocation` 且为**人的决定**（原设计未显式）。
4. 题卡把「Cost-Benefit」归在 **Prove** → 成本收益/ROI 论证从 plan 移到 `prove`（原设计放在 plan 的「回本测算」）。
5. 指标必须「用 Scout Report 标杆佐证」→ `metrics` 增加 `benchmark_ref` 字段（原设计未要求对标）。



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
- 机器人 cosplay 设定：机械腔、FACI-0X 编号、cheerful one-liner（呼应 run-sheet）。
- **全英文**：提问、开场、时间提醒、鼓励语一律英文（受众为英文使用者）。
- 每关标准开场：一句话说清「本关要做什么 + 你有几分钟 + 你要产出什么」。
- 时间提醒话术：剩 3′ / 1′ 各播报一次。

### 5.6 采集契约（Capture Contract）
- **HITL 门**：AI 在每关发散/收敛后**必须停下**，显式请求团队输入，不得跳过。
- **采集卡（YAML）**：统一记录格式（见各 quest 技能的 capture schema）。
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
- **目标**：产出一份**厚洞察**：市场趋势 + 人群分层（含 JTBD）+ 关键时刻 + 市场真相 → 种子洞察。**光有真相不够，必须有人群与需求分析**，否则下游创意无根。
- **输入**：Quest 题卡（含 Scout Report）。
- **输出**：`insight-brief.html` + `insight.yaml`。
- **facilitate（串场）**：
  1. **研究（AI）**：读题卡 → **用 `agent-reach` 搜真实数据/报告/标杆**（市场、消费者趋势、出行、创作者经济等）→ 蒸馏成数据化洞察选项。这是所有菜单的数据底座。
  2. **市场趋势**：AI 出 **6–8 个带数据的趋势选项** → 团队**选 2–3**（可 +1 自选）`{trend, why_it_matters}`。
  3. **人群**：AI 出 **6–8 个候选人群** → 团队**选 2–4**，每类补 `who / job(功能·社会·情感) / barrier / trigger`。
  4. **关键时刻**：AI 出 **6–8 个候选时刻** → 团队**选 1–2**（时间/地点/事件）。
  5. **市场真相**：AI 出 **6–8 条候选洞察** → 团队勾选共鸣的（可 +1 自选），逐条 verbatim 采集。
  6. 聚类 + 团队确认**一句话种子洞察**。
  > 每步均为**选择题**（见 §5.3 Option Menu）；AI 不替团队选。
- **capture（insight.yaml）**：
  ```yaml
  quest: A|B
  org_profile: {assets, constraints}
  benchmark: {gold_standard, cautionary_tale, arena}
  market:
    trends: [ {trend, why_it_matters} ]        # 2–3 个变化
    truths: [ {author, text} ]                  # 原始真相
  segments: [ {name, who, job_functional, job_social, job_emotional, barrier, trigger} ]  # 2–4 类人群
  moment_of_truth: {when, where, event}         # 决策场景
  clusters: [ {theme, items} ]
  seed_insight: "一句话张力"                    # 团队确认
  ```
- **assemble**：insight-brief.html（战报速览 / 组织画像 / **市场趋势** / 标杆对照 / **人群分层卡** / 市场真相聚类 / **关键时刻** / 种子洞察高亮）。
- **吸收/改造**：`business-research`（仅作标杆对照脚手架）；`audience-analysis` 能力升级为 **STP + JTBD + 趋势 + 关键时刻**（见 `references/insight-method.md`）。

### 7.2 `plan`（创意门 · 14 分钟 · 最重）
- **目标**：**先锚定（人群 + 时刻）再发散**，让创意有根；再由 AI 拼成完整方案。
- **输入**：`insight.yaml`（含 segments + moment）。
- **输出**：`campaign-plan.html` + `plan.yaml`（含**实验计划与测量口径**）。
- **facilitate**：
  1. **锚定**：填创意 brief——「为【哪类人群】、其【情绪 job】、在【哪个时刻】、我们要【做什么机制】」。
  2. **场景画布**：列 3–5 个 campaign 时刻（时间/地点/事件），选 1–2 个作为创意主线。
  3. HMW 由锚点导出（"How might we help [segment] [job] at [moment]?"）。
  4. 静默发散 2′（每人 2 个大创意）→ 轮报上墙 6′ → 亲和聚类 → 点投票 2′（前 2–3 名）。
  5. 1-2-4-All 5′ 深挖赢家 → 「一句话主张 + 命名 + slogan + 它占领的时刻」。
  6. 团队选 2 个试点市场 + 成功口径（3′）。
  7. **团队做预算切分**（1.5M/1.1M 按市场/渠道/战术分配）——题卡明示「Budget allocation is part of the solution」。
- **capture（plan.yaml）**：
  ```yaml
  quest: A|B
  seed_insight: "..."
  audience: {primary_segment, job_to_be_done}          # 锚点
  scenario: [ {moment, time, place, event} ]           # 3–5 个 campaign 时刻
  creative_brief: "for [segment] whose [job] at [moment], we will [mechanic] — so they [desire]"
  hmw: "How might we ..."
  ideas: [ {author, concept}, ... ]
  votes: {idea -> count}
  winner: {concept, proposition, name, slogan, moment}
  offering:                                   # A=campaign concept；B=membership design + founding offer
    type: campaign | membership
    tiers: [...]                              # B 必填：会员分层/定价/权益
    founding_offer: "..."                     # B 必填：创始会员 offer
  pilot: {markets: [...], duration: "3mo", success_criteria}
  experiment: {hypothesis, treatment, control, measurement_setup}   # 实验计划 + 测量口径
  budget: {total: 1.5M|1.1M, allocation: [{market, channel, tactic, amount}...]}
  ```
- **assemble（AI 拼装，团队可快速覆盖）**：
  - **创意锚点 + 场景时刻**（audience & moment / time·place·event）
  - 定位（Geoffrey Moore 五句式）
  - 创意主体：A=营销活动概念；B=会员产品设计 + 创始会员 offer
  - 营销组合 4Ps（分层/定价渠道/内容节奏）
  - 试点实验设计（PoL probe：假设/测量/对照）+ **测量设置（instrumentation）**
  - 预算分配（1.5M/1.1M 切分表）
- **吸收/改造**：`opportunity-definition`（去 AI 口径→营销机会点）；`creative-concept`（人群+场景锚定 + HMW + 创意方法 → ~6 ideas，吸收自原 brainstorming + creative-concept.md）；`marketing-plan`（定位/4Ps）。

### 7.3 `prove`（论证门 · 8 分钟）
- **目标**：3–5 子指标 + Go/No-Go 阈值 + KPI 看板 mock + **成本收益（Cost-Benefit）**。
- **输入**：`plan.yaml`（含 budget）+ 题卡 Victory Conditions。
- **输出**：`proof.html` + `metrics.yaml`。
- **facilitate**：
  1. AI 展示「胜利条件 → 可证伪子指标」草稿（reach→engagement→conversion→售票/会员/特许）。
  2. 团队挑 3–5 个指标 + 定 Go/No-Go 阈值（辩论，4′）——**用 Scout Report 标杆佐证**。
  3. 团队给 1–2 个「样例数字」让看板有真实感。
  4. AI 用 budget + 指标算出**成本收益**：试点 ROI 是否支撑「解锁全额 30M/11M」。
- **capture（metrics.yaml）**：
  ```yaml
  victory_conditions: [...]
  metrics: [ {name, formula, benchmark_ref, target, threshold_go, threshold_no_go}, ... ]  # benchmark_ref 引用题卡标杆
  sample_data: {...}
  cost_benefit: {budget, projected_return, roi, unlock_verdict}
  ```
- **assemble**：proof.html + KPI 看板 mock（用 `data-visualizer-pro`，补手工录入数值路径）+ 成本收益小结。
  - Quest A：KPI 看板 mock 为**必交付物**；Quest B 题卡未单列看板，但「measurement setup + Data Analysis & Viz」隐含，仍出（可精简）。
- **吸收/改造**：`campaign-metrics`（→营销漏斗子指标 + Go/No-Go，保留其「解锁/门禁」框架）；`cost-benefit.md`（→成本收益/ROI 论证，reference）。

### 7.4 `showcase`（呈现门 · 8 分钟 · AUTO）＝题卡「Showcase Report Agent (AUTO)」
- **目标**：**多形态**呈现——5 种 storyline + signature element 承载核心创意 + 可选加分媒体（歌曲/视频/图片）。避免十组同一模板。
- **输入**：`insight.yaml + plan.yaml + metrics.yaml`。
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
  - prompt-pack.html（**提示词脚本包**）：歌曲/视频/图片三类，从 plan.yaml 自动填好，复制即用；媒体占位符预置在 deck（图→poster、视频→storyboard、歌→lyric、加分→ask）。
- **signature element（创意载体）**：poster（整屏海报）/ storyboard（6 帧旅程）/ prototype（手机 mock）/ lyric（anthem 歌词）——对应 5 storylines。
- **加分媒体工具**：歌曲 **Suno**、视频 **Runway Gen-3**、图片 **GPT**（每类 1 主 1 备）。
- **吸收/改造**：`pitch-narrative.md`（5 storylines + beat 库）、`media-prompts.md`（工具指南）。deck 直接由 `templates/pitch-deck.html` 产出；海报本体见 `poster`。无子技能。

---

## 8. 编排层：`facilitator`（Agent）

- **定位**：Robot Facilitator 的人格化 manifest + **建议路径**（非硬状态机）。
- **职责（happy path）**：按 §9 节奏依次调 `facilitation` 协议 + 4 个 quest 技能；维护 YAML 产物链；到点推进；打包提交。
- **职责（弹性）**：监听团队指令，支持「跳关 / 回退 / 重跑 / 单技能直调 / 快模式压缩」；见 §5.8。
- **人格**：FACI-0X 机械腔 + cheerful one-liner。
- **动态场景应对表（示例）**：

| 现场信号 | AI 应对 |
|---|---|
| 「研究够了，直接出创意」 | 跳过洞察发散，直接用题卡数据兜底种子洞察，进 `plan` |
| 「我们只剩 8 分钟」 | 切快模式：压缩发散/收敛，AI 后台并行拼装海报+看板 |
| 「这个投票结果不对，重来」 | 重跑 `facilitation` 点投票协议，不重跑整关 |
| 「只要一张海报」 | 只调 `poster`，用 plan.yaml 拼装 |
| 「换个试点市场」 | 只改 `plan.yaml` 的 pilot 字段，重出论证 |
| 「跳过 SWAT/研究，直接搞 slogan」 | 只调 `facilitation` 的 HMW + 静默发散出 slogan |



---

## 9. 40 分钟节奏总表

| 时间 | 关卡 | 谁主导 | AI 干什么 | 人的决定 |
|---|---|---|---|---|
| 0–2′ | 开题 | AI | 30″ 战报速览 + 抛第一问 | — |
| 2–10′ | 洞察门 | 人 | 聚类趋势/人群/时刻/真相 | 趋势 + 人群 + 时刻 + 种子洞察 |
| 10–22′ | 创意门 | 人 | 把赢家搭成方案框架 | 锚点 + 大创意 + 2 市场 + 预算 |
| 22–30′ | 论证门 | 人 | 建 KPI 看板 | 指标 + Go/No-Go 阈值 |
| 30–38′ | 呈现门 | 人 | 生成海报 + 路演稿 | 视觉方向 + 主张 |
| 38–40′ | 收敛提交 | AI | 一键打包 | 确认 |

> run-sheet 官方为「40′ 产出 + 10′ Showcase 准备」= 50′；本设计以 40 分钟为创意核心。

---

## 10. 文件结构约定

```
.opencode/
├── DESIGN.md · README.md            # 文档
├── skills/                          # 技能（扁平：一技能一目录 —— opencode 发现约定）
│   ├── insight/                     # 洞察门
│   ├── plan/                        # 策划门
│   ├── poster/                      # 海报（Create 阶段）
│   ├── prove/                       # 论证门
│   ├── showcase/                    # 呈现门
│   ├── agent-reach/                 # 实时研究（insight 使用）
│   ├── facilitation/                # 共创引擎（含 option-menu）
│   ├── ascentium-brand/             # 品牌执行器（tokens + 规则 + brand-guideline.md）
│   └── sub-skills/                 (per stage — e.g. insight/sub-skills/: agent-reach · business-research · swot-analysis)
├── agents/                          # facilitator.md · researcher.md
├── commands/                        # start · insight · plan · poster · prove · showcase · evaluate
└── evaluation-rubric.md             # 方案评分卡
```

> **opencode 发现约定 = 扁平** `skills/<name>/SKILL.md`。`agent-reach`、`poster` 作为同级技能平铺（逻辑上归 `insight` / `plan`，被它们引用）。
> 命名约定：**技能/Agent/Command 名一律不带 `quest`**（skill: `insight`/`plan`/`poster`/`prove`/`showcase`；agent: `facilitator`/`researcher`；command: `/start` 等）。

每个技能目录：`SKILL.md`（frontmatter `name` + `description`，**触发词全英文**）+ `references/` +（可选）`templates/`、`scripts/`。
`*/sources/` 仅作原料，改写产物写到上级 SKILL.md / references/，不改 sources。
**语言约定（English-only）**：所有 SKILL.md 正文、references、templates、scripts 注释、YAML schema 字段、输出 HTML 文本，一律英文；中文字样仅在 `brand-guideline.md` 源文件与本 DESIGN.md / AGENTS.md 内部文档出现。

---

## 11. 实施顺序与验收标准

| 顺序 | 技能 | 验收标准 |
|---|---|---|
| 1 | `ascentium-brand` | 能输出 tokens.css + 三类模板；抽查色值=手册一致 |
| 2 | `facilitation` | 协议/节奏/话术/采集契约齐全；4 个 quest 技能可调用 |
| 3 | `insight` | Quest A/B 各跑一遍：14 人洞察 → 种子洞察落 YAML + HTML |
| 4 | `plan` | 投票选赢家 → 完整方案框架（定位/4Ps/试点/预算） |
| 5 | `poster` | 专业 campaign poster（9 段式：客户 logo/主视觉/offer/数据带/CTA+QR） |
| 6 | `prove` | 3–5 指标 + Go/No-Go + 看板 mock |
| 7 | `showcase` | 5 storylines 路演稿 + 媒体占位符（内嵌 poster） |
| 8 | `facilitator` + `README` | 一键串全场 40 分钟，冒烟通过 |

---

## 12. 待确认点

1. `facilitation` 元技能的 5.2–5.8 设计是否 OK（尤其「主持人铁律」「协议库」「动态调度与降级」）。
2. 各 quest 技能的 capture（YAML schema）与 assemble 边界是否合理。
3. 40 分钟节奏时间盒是否需要微调。
4. 实现顺序是否按 §11。
5. 弹性调度（§3.1 / §5.8 / §8）是否到位：还有没有其他「现场动态」场景需要覆盖？
6. §4A 交付物覆盖核对是否无误：6 项交付物 + 5 处修正点是否都已闭环？
