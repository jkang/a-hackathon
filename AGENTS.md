# AGENTS.md — Ascentium Hackathon 工作规则

本文件记录 `Ascentium Hackathon/` 目录下的工作规则与已锁定决策，供所有 Agent / 协作者遵循。
若与其他说明冲突，以本文件 + 上级 `Ascentium Omni/AGENTS.md` 为准。

---

## 1. 目录用途

本目录承载 **Ascentium AI Transformation Mini-hackathon**（2026-10-13 · 深圳）的活动物料与配套工具包：

- 活动页面 / 命题卡：`quest-cards.html`、`app/`、`Ascentium Workshop v2.html`
- 运营物料：`Ascentium_Mini-hackathon_Run-Sheet_准备工作.xlsx`、`Quest_Cards_A3_Print.pdf`
- **参赛工具包：`.opencode/`**（本目录工作的主要对象）

活动形态：112 人 / 8 组 × 14 人 / 50 分钟实战（40′ 用 Toolkit 完成整个输出 + 10′ 整理 Showcase 输出与形式、提交），围绕 Quest A（2030 多哈亚运门票营销）与 Quest B（成都熊猫基地全球化 IP）产出商业方案并 Showcase PK。

---

## 2. 设计原则（锁定）

1. **场景是「营销商业方案」挑战，不是「AI 产品」挑战。** 一切技能以营销咨询口径设计，禁止直接套用 AI 产品 / FDE 口径。
2. **低门槛、开箱即用。** 目标参与者为非技术业务管理者，50 分钟内可跑通；技能粒度采用 **分阶段打包（方案甲）**。
3. **方案甲结构**：对外只暴露 4 个阶段技能 + 品牌 + Meta，降低选择成本。
   - `insight`（洞察）→ `plan`（策划，战略与创意合并）→ `prove`（论证）→ `showcase`（呈现，AUTO）
4. **改造类技能一律「复制后在本库内改写」**，不直接引用外部源库；源库文件仅作原料，不改动源库。
5. **品牌唯一来源**：`.opencode/skills/ascentium-brand/brand-guideline.md`（Ascentium Brand Guidelines R1.10，含 Design Tokens）。所有海报 / PPT / 看板 / 页面必须引用该文件，禁止凭记忆写样式。
6. **不使用 Inspire 品牌技能**（那是另一套），本场景统一用 Ascentium 品牌。

---

## 3. .opencode 目录结构与用途

> `toolkit/` 已改名并重排为项目运行时配置 **`.opencode/`**（opencode 项目级：`skills/` · `agents/` · `commands/`）。

```
.opencode/
├── README.md · DESIGN.md              # 文档（Facilitator 手册 · 设计说明）
├── quest-card.md                      # Quest 配置契约（client/mission/War Chest/Victory Conditions/Scout Report + accent/key_visual/poster_styles）
├── evaluation-rubric.md               # 方案评分卡（7 维度）
├── skills/                            # 技能：一技能一目录；opencode 递归发现 **/SKILL.md
│   ├── insight/                       # 洞察门 → insight-brief.html
│   │   └── sub-skills/  business-research · market-trends · audience-analysis
│   ├── plan/                          # 策划门 → campaign-plan.html
│   │   └── sub-skills/  creative-concept
│   │       （references: marketing-plan · channel-strategy · pilot-experiment · budget-model）
│   ├── poster/                        # Poster（Create 阶段，独立）→ poster-a/b/c.html + poster.html
│   ├── prove/                         # 论证门 → proof.html（单屏 pilot 指标）
│   │   └── sub-skills/  campaign-metrics · data-visualizer-pro（保留·休眠）
│   ├── showcase/                      # 呈现门（AUTO）→ proposal / pitch-deck / prompt-pack / storyboard（内嵌 poster）
│   │   └── sub-skills/                # campaign-storyboard（6 面板单图 → standalone 16:9 看板 → storyboard.html）
│   ├── agent-reach/                   # 实时研究（insight 调用；CLI 需预装）
│   ├── facilitation/                  # 共创引擎（协议库/节奏/话术/选项菜单/采集契约）
│   └── ascentium-brand/               # 品牌执行器（tokens.css + 规则 + brand-guideline.md）
├── agents/                            # facilitator.md（编排）· runner.md（自动）· researcher.md（研究）
├── commands/                          # start · insight · plan · poster · prove · showcase · evaluate · run
└── package.json · node_modules/       # opencode 运行时（已 gitignore）
```

每个技能含 `SKILL.md` + `references/` +（可选）`templates/` `scripts/`；子技能嵌在所属阶段的 `sub-skills/`。
`poster` 与 `agent-reach` **平铺为顶层技能**（逻辑上归 `plan` / `insight`，被它们引用）。命名**一律不带 `quest`**。

**输出位置（运行约定）**：Facilitator 与 runner 两种模式都把产物写入仓库根的 **`artifacts/Quest<ID>-<NN>/`**（每题一轮一子目录，如 `QuestA-01`、`QuestA-02`）。`/run` 新建轮次目录；`/start` **只做 briefing**（不建目录、不产产物），由**第一个写产物的阶段**建目录；单阶段命令写入该题最新轮次目录（无则建 `-01`）；**不覆盖旧轮次**。`artifacts/` 已 gitignore；签入示例保留在 `demo-examples/`。详见 `.opencode/quest-card.md` → *Output layout*。

---

## 4. 技能处置清单（锁定）

**对外只暴露 4 个阶段技能 + 品牌 + Meta**（方案甲，分阶段打包）：

| 阶段技能 | 对接 Arsenal 能力 | 吸收/改造的 sources |
|---|---|---|
| `insight` | Market Research · Audience Analysis · Benchmark Analysis · Company Profiler (IP audit) | `business-research`、`market-trends`、`audience-analysis` |
| `plan` | Creative Concept · Channel Strategy · MVP Pilot Design · Marketing Plan · Budget | `creative-concept`、`channel-strategy` |
| `poster`（Create 阶段，独立） | Poster（Create 阶段） | `ref-palette-slide` |
| `prove` | Pilot Metrics（pilot 预期指标 + 推演逻辑；单屏） | `mvp-metrics-generator`→campaign-metrics、`data-visualizer-pro`（保留·休眠） |
| `showcase` | Showcase Report Agent (AUTO) | `html-ppt-generator` |

支撑技能：`ascentium-brand`（品牌执行器）、`facilitation`（共创引擎）、`agent-reach`（实时研究）、`brainstorming`（plan 阶段发散子技能）。
> Poster 归 Create 阶段（题卡 Create: Creative Concept · MVP Pilot Design · **Poster**），故独立成 `poster`；showcase 只**内嵌** poster，不重复产出。

**明确弃用**：`persona-journey-designer`（产品 UX 口径）、`ai-roi-calculator`（AI 项目 ROI 口径）、`company-ai-maturity-research`（AI 就绪度口径）、`unified-report-dashboard`（过重）。

---

## 5. 工作规则（Rules）

### 5.1 文件与技能
- `*/sources/` **只作原料**，保持与源库一致的复制态；改写产物写到上级 `quest-*/SKILL.md` 及其 `references/`，**不要就地修改 sources/**。
- 不修改任何外部源库（`~/MyCoding/Skills/**`、`~/.claude/skills/**`、`~/.agents/skills/**`、`Ascentium Omni/OmniDesign/**`）。
- 每个技能目录至少含 `SKILL.md`，frontmatter 使用 `name` + `description`（**触发词全英文**）。

### 5.2 品牌与视觉
- 一切视觉产出的色值 / 字体 / 间距，必须来自 `.opencode/skills/ascentium-brand/brand-guideline.md` 第 11 节 Design Tokens，禁止自造样式。
- 关键 token：`--ascentium-orange #FF6611`、`--ascentium-midnight #0F1514`、字体栈 `"Poppins","Noto Sans SC","PingFang SC","Microsoft YaHei",Arial,sans-serif`。
- **禁用「侧边装饰栏」**：不得使用 `border-left` 色条、左侧竖条等纯装饰性竖栏。强调信息一律用「色块底色 + 圆角卡片 + 加粗文字」表达（如 `.ruleband` 改为整块 tint 背景 + 细边框，不带左侧色条）。

### 5.3 数据与安全
- 禁止把私有凭证、token、内部 ID 写入仓库文件；需要时只写「红acted 摘要 + 稳定指针」。
- 活动命题卡中的数据为公开报道口径，引用时保留来源与 `Data as of` 标注。

### 5.4 输出与命名
- **产物默认英文（English-only）**：技能正文、触发词、capture JSON 字段、输出 HTML、README/Playbook、Facilitator 话术一律英文；受众为英文使用者。仅 `brand-guideline.md` 源文件与本 AGENTS.md / DESIGN.md 内部文档保留中文。代码 / 命令 / 路径 / 色值保持原样。
- 阶段产物落在对应 `quest-*/` 下；报告类文件名体现「任务-产物类型」，如 `quest-A-insight-brief.html`。
- HTML 产物优先单文件、可双击打开、无构建依赖。

### 5.5 交付前校验
- 改动技能后，至少跑一次对应命题（Quest A / Quest B）的冒烟验证，确认链路可用。
- 复制 / 移动类操作后，用 `find` 核对目标目录与 SKILL.md 完整性。

### 5.6 文案措辞（business 口径 · 拒绝油腔滑调）
- **一切 hackathon 相关文案一律用朴实、准确、专业的 business 语言。** 覆盖范围：`facilitator_guide.html`、题卡 / workshop 页、`README.md` / `DESIGN.md`、技能与命令正文（SKILL.md）、现场话术、示例产物文案。
- **禁止**口语化、网络化、俏皮化、比喻化的措辞，例如（黑名单，非穷举）：
  - 俚语 / 网感：`局里`、`上桌`、`整活`、`搞事情`、`拿捏`、`破防`、`上头`、`大招`
  - 比喻化口语：`干重活`、`甩手掌柜`、`死胡同`、`拉进局里`、`手里都有活`、`够好`
  - 语气过硬的口语指令：`别问`、`别等`、`绝不甩`、`卡住就降级`、`用嘴说出来`、`拍板`
- **改用**（正例）：`参与其中` · `承担主要执行工作` · `推进` · `降低选择难度` · `帮助团队走出僵局` · `口头提醒` · `由团队决定` · `达到可用水平`。
- **禁止「否定式对比补白」**（`X, not Y` / `NOT the …` / `不是…而是…`）：把「不是什么」当强调是多余的废话，直接给结论。
  - 反例：`THE MVP, NOT THE MASTER PLAN` → 正例：`THE MVP PLAN`
  - 同义清理：`not the master plan` → 直接写 `the MVP` / `the pilot plan`，不写否定半句。
- **判断标准**：这句话能否原样放进一份交给客户或管理层的商业方案？不能就重写。
- **例外**：机制 / 产品专有名词（如「菜单 Option Menu」「洞察 Insight」）与英文术语保持原样。

---

## 6. 进度与下一步

**已完成（2026-09-28）**
1. `ascentium-brand`：从 brand-guideline.md 抽出 Design Tokens，落地 `references/tokens.css` + `typography.md` + `component-rules.md`。
2. `facilitation`：协议库（HMW/静默发散/轮报/亲和聚类/点投票/1-2-4-All）+ 节奏/降级 + 英文话术 + 采集契约。
3. 4 个 `quest-*` 阶段技能（英文 SKILL.md + references + templates）+ `agents/facilitator.md` + `README.md`。
4. 冒烟验证：Quest A 全链路 6 个 HTML 模板渲染通过（零残留占位符、Ascentium 品牌），Quest B teal 海报变体通过。

**待做**
1. `agent-reach` 为原样复用的双语工具技能，如需严格 English-only 需另行本地化；并确认目标机预装（`agent-reach`/xreach/yt-dlp，当前仅 `mcporter` 可用）。
2. 在真实设备上用 Quest A / Quest B 做一次端到端彩排（含 facilitator 台词与计时）。
3. 视需要补充 output HTML 的打印/截图样式。

**已完成 · 命题修订（2026-09-29）**
- **Quest A 市场范围已放宽为 Asia-wide**：Mission 改为「make Asia's away crowd Doha's biggest in Asian Games history」；Scout / HWM / KPI / pilot / 语言表一并调整。
- 已同步文件：`quest-cards.html`、`index.html`、`ascentium-hackathon-standalone.html`、`ascentium-hackathon-standalone-zh.html`，以及 `.opencode` 内 Quest A 示例（insight-method / creative-methods / budget-model / pilot-experiment / metrics-method / cost-benefit / prove SKILL / DESIGN）。
- **概念澄清（重要）**：**「参与者来自 SEA」≠「Quest 受众限于 SEA」**——参与地区与命题的目标市场是两个独立概念；每个 Quest 自行定义目标市场（Quest A = Asia-wide；Quest B = 全球）。

---

## 7. 变更记录

- 2026-09-28：创建本文件；完成 toolkit 骨架与可复用技能复制。
- 2026-09-28：登记 Quest A 市场范围修订（SEA → 亚运覆盖国家范围），待更新 `quest-cards.html`。
- 2026-09-28：facilitation 新增「选项菜单 Option Menu」choice-first 机制（AI 先出 6–8 候选、团队选择题、+1 自选），并同步更新 4 个 quest 技能的 HITL 流程、facilitator、DESIGN.md。
- 2026-09-28：insight 环节要求 **AI 主动用 `agent-reach` 搜真实数据/报告**，把事实蒸馏成「带数字的洞察选项」再让团队选（菜单必须有数据依据，非机械标签）。已更新 facilitation/insight/insight-method/DESIGN。
- 2026-09-28：`toolkit/` 改名为项目运行时配置 **`.opencode/`**（opencode 项目级）。技能扁平化为 `skills/<name>/SKILL.md`；**命名一律去掉 `quest`**（skill: `insight`/`plan`/`poster`/`prove`/`showcase`；agent: `facilitator`/`researcher`；command: `/start` 等）；`agent-reach`/`poster` 平铺（逻辑归 insight/plan）。新增 `commands/`（7 个）与 `agents/`（facilitator · researcher）。
- 2026-09-28：完成方案设计（DESIGN.md v2，人机共创版 + 弹性调度 + 全英文）；实现 `ascentium-brand` / `facilitation` / 4 个 `quest-*` / `facilitator` / README；Quest A 冒烟验证通过。
- 2026-09-28：**四阶段技能 review + 重构**（营销口径统一 + 全英文 + 去无效文件）：
  - **insight**：研究链 `agent-reach → business-research → audience-analysis → swot-analysis`；产出 **~6 条关键 insight → 团队选 2–3 条** 深挖做 plan；insight-brief 模板加 Key Insights 卡。
  - **plan**：`brainstorming` 并入并改名 **`creative-concept`**（内嵌 HMW + 创意方法 → ~6 ideas → 选/综合）；删 `pol-probe-advisor`；**campaign plan 出 ≥2 套 A/B → 团队选**；`campaign-plan.html` 改为含两套 A/B；3 个 references（budget/marketing-plan/pilot-experiment）接线。
  - **prove**：删 `creating-financial-models`（投资估值口径，无效）；`mvp-metrics-generator` 改名 **`campaign-metrics`**；成本收益由 `references/cost-benefit.md` 承担。
  - **showcase**：删 `ref-palette-slide`（PPTX 口径）与 `html-ppt-generator`（冗余）；storyline/beat 表三处统一为模板权威版；**`proposal.html` 为统一报告**（整合所有 HTML，非 deck）。
  - 全库 skills/agents/commands **英文**（仅 `brand-guideline.md` 源文件 + AGENTS/DESIGN 内部文档保留中文）。
- 2026-09-29：**活动口径统一**：**112 人 = 8 组 × 14 人 · 每组 1 名 Facilitator（FACI-01~08）· 50 分钟（40′ Toolkit 产出 + 10′ Showcase 整理 / 形式 / 提交）**。同步 `AGENTS.md` / `DESIGN.md` / `Run Sheet.csv`。
- 2026-09-29：`guide.html` 更名为 **`facilitator_guide.html`**；新增「Facilitator 核心职责」（4 条）+ 分类 `Facilitator Tips`（6 类）；`auto-run` 并入现场模式作为机动备用；§3 目录树按真实仓库重写。
- 2026-09-29：**新增 §5.6 文案措辞规范**（business 口径，拒绝油腔滑调：`局里`/`干重活`/`死胡同`/`兜底`/`拍板` 等黑名单 + 正例 + 判断标准）；据此清理 `facilitator_guide.html` 全篇措辞。
- 2026-09-29：**目录结构对齐** —— `poster`（原 `plan/sub-skills/poster`）与 `agent-reach`（原 `insight/sub-skills/agent-reach`）**平铺为顶层技能** `skills/poster/` · `skills/agent-reach/`，与 AGENTS/DESIGN/README 的设计意图（「平铺，逻辑归 plan/insight」）一致；同步 AGENTS.md / README.md / DESIGN.md / facilitator_guide 四处目录树（并移除已废弃的 `sources/` 说法）。
- 2026-09-29：**Quest A 市场口径 SEA → Asia-wide**；明确「参与者来自 SEA ≠ Quest 受众限于 SEA」；Quest B 保持全球定位。quest-cards / index / standalone(en+zh) / `.opencode` Quest A 示例全部同步。
- 2026-09-29：**Quest 解耦（toolkit 复用化）**：新增 **`quest-card.md`**（Quest 配置契约：client/mission/War Chest/Victory Conditions/Scout Report + 视觉参数 `accent`/`key_visual_svg`/`poster_styles`），确立「技能=引擎 · 题卡=数据」分层。落点：① 7 个 HTML 模板的 accent 从 `data-quest="A|B"` 硬编码改为「题卡注入 `--accent/--accent-tint/--accent-line/--accent-deep` 内联变量」（并修正 pitch-deck 缺 teal 覆盖的 bug）；② pitch-deck 插画从硬编码 stadium/panda 改为单一 `{{KEY_VISUAL_SVG}}` 槽位，旧插画迁至 `showcase/references/motifs-examples.md`；③ poster 三风格名（Matchday Roar/Supporter Passport/Midnight Minimal）改为「tone 原型 + `{{STYLE_*}}` 占位」，题卡可重命名；④ SKILL/command/README 触发词与 references 里的 Doha/熊猫/SEA 具体数据清空为「from the card」指针。冒烟验证：合成 Quest C（teal）poster 构建 + pitch-deck/proposal 构建均通过。
- 2026-09-29：**统一运行输出位置**：Facilitator 与 runner 均写入 **`artifacts/Quest<ID>-<NN>/`**（每题一轮一子目录；`/start`、`/run` 新建轮次，单闸命令并入最新轮次，不覆盖旧轮次）；两种模式均产出 `RUN-LOG.md`。同步 `agents/facilitator.md` · `runner.md`、7 个 command、README、quest-card.md、poster/showcase SKILL、DESIGN.md；`.gitignore` 加 `/artifacts/`；删除空目录 `runs/quest-b`。
- 2026-09-30：**Prove 环节简化**：只保留 **pilot 预期指标 + 每个指标数值的推演逻辑**（benchmark → assumption → formula → target），输出**一屏** `proof.html`；**移除** Go/No-Go、Cost-Benefit/ROI、scale-up、KPI 看板 mock。`prove` 单技能不再调用 `campaign-metrics` / `data-visualizer-pro` / `cost-benefit.md`（三者**保留但休眠**）。同步：prove SKILL/template/references · facilitator/runner · commands（prove/run/start）· facilitation refs · showcase（deck 的 proof+ask beat、proposal、pitch-narrative）· evaluation-rubric/evaluate · README/DESIGN/quest-card · participant 物料（quest-cards / index / standalone）· `demo-examples/QuestA-v2`（proof / metrics / deck / proposal / RUN-LOG）。
- 2026-09-30：**环节输出只留 HTML**：各阶段产物不再有 `.yaml` / `.md`——每个阶段的 decisions 以**内嵌 JSON**（`<script type="application/json" id="capture">`）写进该阶段 HTML；下游关卡读取上游 HTML 的 `id="capture"` 块。移除 `insight.yaml` / `plan.yaml` / `metrics.yaml` / `RUN-LOG.md`。同步：4 个阶段 SKILL + 模板 · `facilitation/references/capture-contract.md`（重写）· facilitator/runner/researcher · 8 个 command · README/DESIGN/quest-card · `facilitator_guide.html`（+ standalone）· `demo-examples/QuestA-v2`。
- 2026-09-30：**题卡 §03 修订**：① 标题 `the MVP, not the master plan` → **`The MVP Plan`**（否定式对比补白，见 §5.6 新规则）；② **移除 `Scale-up gate` 栏**——toolkit 已不做 scale-up，门禁机制已由 §02 War Chest 的 Phase 2（hit sub-metrics → vendor list → unlock full budget）承载；其中「语言覆盖 / conservation-first」保留为题卡 `vc-note` 约束行，`.dc .meta` 由 3 栏改 2 栏。同步 `quest-cards.html` · `.opencode/skills/plan/SKILL.md` · `plan/references/pilot-experiment.md` · `.opencode/DESIGN.md`。
- 2026-09-30：**新增 §5.6 规则「禁止否定式对比补白」**（`X, not Y` / `NOT the …` / `不是…而是…`）：直接给结论，例 `THE MVP, NOT THE MASTER PLAN` → `THE MVP PLAN`。
- 2026-09-30：**participant 物料修订（index / standalone）**：① 章节标签 `LEVEL 01–07` → **`SECTION 01–07`**（本页是流程说明，无进阶关系）；② Guild Setup 的 Facilitator 描述去掉「AI BOT / cosplay / robot one-liners」，改为「每桌 1 名 Facilitator（FACI-01~08）协助团队」，与 `facilitator_guide` 对齐；③ 每组设备 `×2–3` → **`×2`**（桌面示意图由 3 台改 2 台）。连带在 `facilitator_guide.html` 把 `Robot Facilitator` → `Facilitator`、`三台设备` → `两台设备`。重建 `ascentium-hackathon-standalone.html` 与 `facilitator_guide_standalone.html`。
- 2026-09-30：**新增 §5.2 规则「禁用侧边装饰栏」**：视觉产出不得使用 `border-left` 色条 / 左侧竖条等纯装饰性竖栏，强调信息改用「色块底色 + 圆角卡片 + 加粗文字」。
- 2026-09-30：**新增 Host 大屏引导 Deck**：仓库根新增 `host-deck.html`（单文件、无构建、无外部依赖），Host 投屏用；与 Showcase `pitch-deck` 同一表达引擎（1000×562 舞台 + ←/→/0–7/F 导航 + 底部 rail/进度条），但**版式有意区分**——封面 / 标题 / 分节页**居中展示**，并采用 standalone Hackathon（`index.html`）的设计元素（`hero.png` 全屏视觉封面、橘色 kicker、`SECTION` 胶囊分节页、`goal` / `flow` / 圆桌示意 / 题卡配图 / 积分榜 / 奖杯 / honors chips）。含 8 段 32 屏：Standby（封面 · 预演时钟 · 议程）→ Opening Brief（Welcome / Why / Map / Quests / Rules / Process / Rhythm / Toolkit 视频占位）→ Pick & Roles → Gold Rush Build（含 20′ / 10′ 提醒屏）→ Converge & Submit → Showcase Rules & Voting Demo → Arena（对阵表 · 单场控场 · 实时计分）→ Victory（榜单 · Hall of Fame · 闭幕）。每张控场屏带**可交互倒计时**（预设 20/10/5/2/1′、Start/Pause、Reset、±30s，≤60s 变红）、墙钟、选手/Duel 选择由顶部 `CONFIG` 驱动。品牌 logo 统一用 `ascentium_global_logo.jpeg`（原「white」logo 实为浅底，深色页会露出白块，已弃用）。
- 2026-10-06：**/start 增加「先讲解、后研究」体验 + 研究重试上限**：① `/start` 现在先执行 **Step 0 — Brief & confirm (HITL)**：复述 mission（client · mission · market）→ 说明四个阶段（Insight → Plan + poster → Prove → Showcase）→ 预告接下来将 research 本 Quest 并产出 **~6 条 data-backed insights**、**可能耗时数分钟** → **等团队确认后再创建轮次目录 / 启动 research**（原为直接后台跑 researcher，全程无互动）。② 研究新增硬性 **重试上限：单个外部来源最多重试 2–3 次**，失败即标 `unreachable` 并改用其他来源，禁止对同一死链反复尝试；若网络大范围不可用，回退题卡 Scout Report 并注明未能核实。落点：`commands/start.md` · `commands/insight.md` · `agents/facilitator.md`（Prime Directive 8 + happy path + How-to-run step 0/1）· `agents/runner.md` · `agents/researcher.md`（Rules）· `skills/insight/SKILL.md` · `skills/agent-reach/SKILL.md`（Troubleshooting）· `README.md`（mermaid `H0` + 流程表）· `facilitation/references/pacing.md`。
- 2026-10-06：**修复 Facilitator 模式「一口气跑完全程」的失控**（`/start` 把 6 步 happy path 当 checklist，模型一次 turn 直接产出全部产物、全程无互动）。措施：① **`facilitator` 新增置顶章节「Turn discipline — one decision per turn」**（每个 turn 只允许：研究 → 输出**一个** menu → **结束 turn 等团队回复**；禁止自问自答、禁止一个 turn 跑多个关卡、禁止在团队确认前产出产物；「全自动」只属于 `/run` / `runner`），并加 Prime Directive 9；happy path 表标注为「sequencing reference，非 to-do list」。② **`/start` 重定义为「只做 briefing」**：复述 mission + 四阶段 + 预告 research（~6 insights、数分钟）→ 请团队确认 → **结束 turn**；明确「不研究、不建目录、不产产物」；**轮次目录改由第一个写产物的关卡创建**（`quest-card.md`/`facilitator` Output/DESIGN/README 同步）。③ 4 个单闸命令（`insight`/`plan`/`prove`/`showcase`）各加「One decision per turn — present one menu, then STOP」提示；`run.md` 保持全自动。落点：`agents/facilitator.md` · `commands/start.md` · `commands/{insight,plan,prove,showcase}.md` · `quest-card.md` · `README.md` · `DESIGN.md`。
- 2026-10-06：**每轮 response 统一「回顾 + 内联选项」格式**（不再让用户去浏览器打开 HTML 才知道要选什么）。① `facilitator` 新增 **「Response format — recap + inline decision (every turn)」** 章节 + Prime Directive 10：每轮结尾固定三段——**Recap**（刚做了什么 + 产物名/路径 + 关键结论）→ **把下一步 menu 直接打印在对话里**（6–8 项、带依据）→ **一句选择提示**；并给「每关该内联什么」清单（insight=~6 insights；plan=~6 ideas + A/B；prove=metrics；showcase=storyline/poster/方向；poster=方向 + 一句话）。核心原则：**HTML 是记录，对话才是决策界面**。② `facilitation` 三件套同步：`option-menu.md` 加「Deliver the menu in the chat」+ anti-pattern；`facilitator-scripts.md` 加「Turn wrap-up (recap + inline choice)」脚本；`capture-contract.md` HITL 模板加 recap 行。③ 5 个 gate 命令（`insight`/`plan`/`prove`/`showcase`/`poster`）各加「结尾必须 recap + 内联下一步选项」段；`evaluate.md` 要求把 scorecard + top 3 fixes 内联打印。④ `README.md` non-negotiables 3→4（加「Recap + inline options, every turn」）。落点：`agents/facilitator.md` · `skills/facilitation/references/{option-menu,facilitator-scripts,capture-contract}.md` · `commands/{insight,plan,prove,showcase,poster,evaluate}.md` · `README.md`。
- 2026-10-06：**复审修复（一致性）**：① **`facilitation` SKILL 补齐两条铁律**（原 7 条滞后于 agent 的 10 条）：#8 One decision per turn、#9 Recap + inline options，并更新 co-creation loop 说明。② **消除 `/insight` 重复 briefing**：`/insight` 与 `insight` SKILL 的「Brief & confirm」改为**条件执行**（已用 `/start` 确认过则跳过，直接 research）。③ `commands/poster.md` 补「One decision per turn」提示 + 修正「set `data-quest`」措辞（accent 来自题卡注入的内联变量）。④ `facilitator.md` 修正 `poster (poster)` 冗余、step 0 补「确认后下一轮进入 insight gate」。⑤ `quest-card.md` 修正 key-visual 的 viewBox 说明（deck `480×360` / poster `1200×500`）；`AGENTS.md §3` 与 `DESIGN.md` 同步「`/start` 只 briefing、轮次目录由第一个写产物的关卡建」。⑥ `README.md` contract 5→6 条（加 recap）。⑦ `facilitator_guide.html` + `_standalone.html` 同步 `/start` 新语义并重建 standalone。
- 2026-10-06：**强制全英文响应**：`facilitator` / `runner` agent 顶部加 **「Language: English only」**（即便团队用中文提问也一律英文回复）；8 个 command 各加英文约束（`start`/`insight`/`plan`/`poster`/`prove`/`showcase` 加 **Language: English only** 行，`run`/`evaluate` 已有 English only）。已 grep 确认 `commands/` · `agents/` · `skills/` 无中文字符（仅 `brand-guideline.md` 源文件除外）。
 - 2026-10-06：**Facilitator 编号统一为 `hackathon-robot`**（原 `FACI-0X` / `FACI-01~08` 缩写对非技术参与者不易理解；改为统一、易读的身份标识）。替换全部出现处：`.opencode/agents/facilitator.md` · `.opencode/README.md` · `.opencode/skills/facilitation/references/{facilitator-scripts,capture-contract}.md` · `.opencode/DESIGN.md` · `facilitator_guide.html`（+ `_standalone.html`）· `Hackathon-Design/index.html`（+ `ascentium-hackathon-standalone.html` · `ascentium-hackathon-standalone-zh.html`）· `Hackathon-Design/Ascentium-Mini-hackathon Run Sheet.csv`。（`host-deck.html` 无真实引用，grep 命中为内嵌 base64 图片误报。）
- 2026-10-06：**`/start` 起始决策菜单固定化**：`/start` 结尾的选项由自由生成改为**逐字固定**的 3 项菜单（原 step 3 只写「ask the team to confirm — or to skip」，导致每次措辞/项数不一致）。固定菜单：**1** Start the research · **2** Skip research · **3** Reuse the card + add our own facts。同步 `commands/start.md`（内联逐字菜单）· `agents/facilitator.md`（How-to-run step 0）· `commands/insight.md` + `skills/insight/SKILL.md`（未 brief 时的同一菜单）。
- 2026-10-06：**Showcase 收敛为两次团队决策（storyline + bonus media）**。原 showcase 的 HITL 门有 5 项（storyline · poster on/off · signature · visual direction · one-liner · bonus media）。现改为：**团队只决策 storyline 与 bonus media**；**poster 恒为 On**（`data-poster="yes"`），**signature（取 storyline 默认）· visual direction · one-liner 全部由 AI 决定**，capture 中仅记录不询问。同步：`skills/showcase/SKILL.md`（description/Inputs/Flow/HITL/capture 注）· `commands/showcase.md` · `agents/facilitator.md`（inline 清单 · 编排表 · happy path · Prime Directive 1 例外）· `skills/facilitation/{SKILL.md（Prime Directive 1 例外）,references/{pacing,facilitator-scripts}.md}` · `agents/runner.md` · `README.md`（mermaid 去掉 `H8` + 流程表）· `DESIGN.md §7.4` · `skills/showcase/references/pitch-narrative.md` · `skills/showcase/templates/pitch-deck.html`（注释）· `skills/poster/{SKILL.md,references/poster-method.md}`（移除「在 showcase deck 选海报风格」的过时说法——海报风格仍在 `poster` 阶段决策，showcase 仅内嵌已选风格）。另修 `facilitator_guide.html` 决策行（`poster on/off · 一句话` → `选 storyline` / `选加分媒体`）并重建 `facilitator_guide_standalone.html`。Poster 阶段维持「一次决策（选风格 A/B/C）」不变。
- 2026-10-07：**Insight 环节逻辑重构（顺序纠正 + 双决策）**。原逻辑顺序倒挂且决策点错位：Focus Bundle（人群 × 时刻 × 趋势的合成物）排在 trends/segments/moments **之前**；Truths 与 Trends 大量重复；Moments 独立于人群单独 pick；团队唯一决策是「在 AI 写好的洞察里挑 2–3 条」（反直觉）。**新逻辑**：① 背景（Scout Summary **并入 Benchmark** + Org/IP Profile）→ ② **Market Trends**（合并原 trends + truths + SWOT 的 O/T，每条含 `kind=shift|fact|opportunity|threat`，**全量展示、无 pick**）→ ③ **Audience Segments（团队决策 1：选 2–3）** → ④ **Focus Bundles**（由已选人群各推导 1 个，含其时/地/事件 Moment + 支撑 Trend，**无 pick**）→ ⑤ **Key Insights（团队决策 2：选 2–3）** → ⑥ Seed Insight。**Truths 块、独立 SWOT 块、独立 Moments 菜单全部取消**（S/W→Org Profile，O/T→Market Trends，Moment→每人群 1 条）。capture 新增 `selected_segments`，删除 `truths` / `swot` / `moments` / `selected_focus` / 各 `ai_pick`；`trends[]` 增 `kind`；`focus_bundles[]` 改为 `{segment_id, moment:{when,where,event}, trend_id, why}`。落点：`skills/insight/{SKILL.md,references/insight-method.md,templates/insight-brief.html}` · `skills/insight/sub-skills/{audience-analysis,swot-analysis}/SKILL.md` · `commands/insight.md` · `agents/{facilitator,runner,researcher}.md` · `skills/facilitation/references/{pacing,facilitator-scripts,option-menu,capture-contract}.md` · `README.md`（mermaid `H1/H1b` + 流程表）· `DESIGN.md §7.1/§7.2` · `skills/plan/SKILL.md`（+ `commands/plan.md`）· `skills/showcase/templates/pitch-deck.html`（`{{TRUTHS}}`/`{{CLUSTERS}}` → `{{MARKET_TRENDS}}`）。冒烟验证：`demo-examples/{QuestA-v2,QuestA-01,QuestB-01}/insight-brief.html` 按新结构重建，capture JSON 校验通过（无残留 `truths/swot/moments/selected_focus`），HTML 标签平衡；Accent 验通过（Quest A orange / Quest B teal）。注：同目录的 `proposal.html` / `pitch-deck.html` 为下游产物、内嵌旧版 insight brief，将在下次 `/run` 时随新模板重建。
- 2026-10-07：**阶段边界显式化 + 单闸命令自动恢复上游**。① **不自动进入下一阶段**：每个阶段 artifact 定稿后，收尾用**自然语言完成态**（如「Research and insight are complete — `insight-brief.html`. Next: run `/plan`」）并 STOP，团队自己用下一条命令启动下一阶段（刻意**不用「Gate」措辞**，只描述完成态）；`/start` 保留 3 项菜单（B 方案），团队选完后**只记录选择并提示 run `/insight`**，不自动跑 research。② **单闸命令恢复上游**：`/insight`…`/showcase` 各自内联「Recover upstream」——确定 quest id → glob `artifacts/Quest<ID>-*` 取**最新轮次**（用户可给轮次号覆盖）→ **先跟用户确认一句**（resume from `QuestA-02`?）→ 读上游 HTML 的 `id="capture"`；上游缺失则明说并回退/询问。**不新建 reference、不动 quest-card.md**（上一轮结果本就在上一轮输出里）。落点：`commands/{start,insight,plan,poster,prove,showcase}.md` · `agents/facilitator.md`（Response format 加「Stage completion handoff」映射表 + Prime Directive 12/13 + How-to-run step 0/7）· `facilitation/references/facilitator-scripts.md`（Stage completion 脚本）· 5 个阶段 `SKILL.md` 的 Inputs 段（Resume 说明）。
- 2026-10-07：**流程复审修订（确认频次 / Plan 不产 poster / 阶段开场 / 措辞 sweep）**。接上一条落地后的复审：① **修复 `/insight` 的 Skip/Reuse 矛盾**（原「honor the logged choice … go straight to research」对 Skip/Reuse 正好相反）——改为 Start → 跑 research；Skip/Reuse → 跳过 research、用 Scout Report 作 seed 进 segments 菜单（`commands/insight.md` + `skills/insight/SKILL.md`）。② **`/start` 菜单文案修正**：选项 1 明确为「the Insight stage researches …」（不再暗示选完立即研究）；「logged」→「noted」。③ **确认频次取 (b)**：单闸命令只有**歧义时**（新 session / 多轮次）才一行确认，否则直接声明「Continuing in `QuestA-01`」继续（`commands/*` + 5 个 SKILL 的 Resume 段 + `facilitator.md` PD13）。④ **Plan 不再写 poster 文件（方案 a）**：`campaign-plan.html` 内嵌 hero visual；独立的 `poster-a|b|c.html` / `poster.html` 只由 `/poster` 产出；plan 完成态提示「run `/poster` … or `/prove` to continue without one」（`commands/plan.md` + `skills/plan/SKILL.md`）。⑤ **Showcase poster 兜底**：若本轮无 `poster.html`（团队跳过 `/poster`），showcase 自动生成默认 poster（style A）（`commands/showcase.md` + `skills/showcase/SKILL.md`）。⑥ **新增阶段开场宣告**（Prime Directive 14 + 5 个 command 开头 + `facilitator-scripts.md`「Stage opener」）。⑦ **「gate / 关卡」措辞 sweep**：`.opencode/**` 规范性文本 `gate`→`stage`、`HITL gate`→`HITL checkpoint`、`single-gate`→`single-stage`、`gate-by-gate`→`stage by stage`，**保留 capture 的 `"gate":` JSON 键**（脚本 `(?<!")\b[Gg]ates?\b(?!")`，覆盖 29 个文件）；DESIGN.md 中文「关卡」→「阶段」、「单闸」→「单阶段」；**不动** brand-guideline.md、休眠 sub-skills（campaign-metrics/data-visualizer-pro）、AGENTS.md 历史条目、参与者物料。⑧ **文档同步**：`README.md`（mermaid 加 STOP/handoff 节点 + §3/§5 表 + §6 恢复上游说明）、`facilitator.md` happy path 行 0–2′。**不接 `/evaluate`**（按用户要求）。
- 2026-10-07：**`/start` 入口菜单明确化（选 1 / 输入 `/insight` 即开始 Insight）**。针对「选了 research 之后又提示 run `/insight`」的重复：`/start` 改为 **brief + 入口菜单**，菜单首项明确为「**Start `/insight`**」（含 research / 无研究复用 Scout Report / 复用+补充 三档）；团队选 **1**（或直接输入 **`/insight`**）即**直接进入 Insight 阶段**（`/start` 不再打印「Briefing done. Run /insight…」这类多余提示）。`/insight` 的 step 0 改为**条件执行**：research 模式已在 `/start` 选定则直接继续，否则才呈现同一菜单。落点：`commands/start.md`（重写：Turn 1 = brief + menu，Turn 2 = 进入 insight）· `commands/insight.md` step 0 · `skills/insight/SKILL.md`（Research choice 条件化）· `agents/facilitator.md`（PD8 + How-to-run step 0 + 完成表去掉 Briefing 行）· `facilitation/references/facilitator-scripts.md` · `README.md`（mermaid `H0/HR` + §2/§3/§5 表）。
- 2026-10-07：**Insight 子技能重构（Key Insights 综合化 + SWOT 移除 + Market Trends 独立 + 顺序纠正）**。针对「Key Insights 偏颇（只是把 Market Trends 换皮，未综合 audience × trend × moment）」与「skill 与输出对不上」两个问题：① **Key Insight 重新定义为综合式张力**——每条**由 Focus Bundle 派生**，硬性融合 **已选人群 × 其时刻 × 支撑趋势**，约每个已选人群 2 条；公式 `「[Segment] [job] — but at [moment], [trend] → [tension] — so [implication]」`；「只重述趋势」列为 anti-pattern。capture `key_insights[]` 增 `segment_id`/`trend_id`/`moment`；模板 Key Insights 卡加「Audience · Moment」锚点 chips。② **新增 `market-trends` 子技能**（承担合并市场读数：shifts + hard facts + 外部 opportunities/threats，各带 `kind`，全量无 pick），**移除 `swot-analysis`**（S/W 已在组织画像的 assets/constraints，O/T 已由 `kind` 承载）。③ **顺序纠正**：研究链改为 `agent-reach → business-research → market-trends → audience-analysis`（market-trends 在 audience 之前，趋势为人群分层提供吸引力/背景）；brief 顺序 = Org → Market Trends → Segments（决策 1）→ Focus Bundles → Key Insights（决策 2）→ Seed。④ **audience-analysis 对齐**：segment 数 `3–5` → `6–8`；画像字段与 capture 对齐（保留 who/JTBD/barrier/trigger，新增 `channels` + `size_potential`，去掉 orphan 的 Needs/Trend/Priority，AI 不再 rank-pick）；模板 segment 卡加 Reach/Prize 两行。⑤ **同步**：`skills/insight/{SKILL.md,references/insight-method.md,templates/insight-brief.html}` · `skills/insight/sub-skills/{business-research,audience-analysis,market-trends}/SKILL.md`（+ `audience-analysis/references/segmentation-framework.md`）· `skills/facilitation/references/option-menu.md`（Key Insights 示例改为综合式 + segments 6–8）· `commands/insight.md` · `agents/{facilitator,runner,researcher}.md` · `README.md`（mermaid + 流程表 + §3 树）· `DESIGN.md §7.1 + §3 树` · 本文件 §3 树 + §4 表。**demo-examples 未重建**（按用户「仅 insight 技能」范围）。
- 2026-10-07：**文档同步（Insight 重构 → README / Facilitator guide / 事件物料）**。把上一条落地到全部对外文档：① 根 `README.md`：`insight/sub-skills/` 改为 **business-research · market-trends · audience-analysis**；`insight` 输出改为「market trends → segments → key insights」；目录名 `Hackathon Design/` → `Hackathon-Design/`；构建脚本标注为 `Hackathon-Design/build-hackathon-standalone.py`。② `facilitator_guide.html`：§3 目录树；§4 旅程图（真实数据研究 → 组织/IP 画像 → **市场趋势** → 受众分群 → **焦点包 · 关键洞察 + 种子洞察**；Skill 行 `audience-analysis`/`swot-analysis` → `market-trends`/`audience-analysis`；HITL 行补齐**两处**：`选 2–3 人群` + `选 2–3 关键洞察`）；§6 现场话术与「背后 Skill」表去掉 `swot-analysis`、补 `market-trends`，并把 insight 决策话术改为「先选人群、再选洞察」——随后重新生成 `facilitator_guide_standalone.html`。③ 事件物料：`Hackathon-Design/index.html` 的 Arsenal Insight Loadout「SWOT Analysis」→「Market Trends」并重建 `ascentium-hackathon-standalone.html`；`ascentium-hackathon-standalone-zh.html`「SWOT 分析」→「市场趋势」；`hostdeck/host-deck.html`（客户机 mini + storyboard skills）与 `hostdeck/toolkit-video-scripts.md`（S7/S8）的 `swot-analysis` → `market-trends`、insight 决策改为两次。④ 修正 `Hackathon-Design/build-hackathon-standalone.py` 的目录路径（`Hackathon Design` → 脚本自身目录）。注：`demo-examples/*/proposal.html` 仍内嵌旧版 insight brief（capture 含 `swot` key），按既有约定下次 `/run` 随新模板重建；本轮仅先修正其**可见** seed 标签措辞。
- 2026-10-07：**Plan 阶段重构（创意概念 → 渠道策略；退役 opportunity-definition）**。针对「plan 只锚定 人群+时刻、遗漏渠道；opportunity-definition 与 insight/creative-concept/prove 重叠且未落产物」两个问题：① **确立 campaign kernel = 人群 · 时刻 · 趋势 · 渠道 · 概念**，由 insight 的 key insight（segment × moment × trend）+ 人群 `channels` + 市场趋势贯穿到 plan。② **移除 `opportunity-definition` 子技能**（5 要素与 insight/creative-concept/prove 重叠、且未渲染进 `campaign-plan.html`）。③ **新增 `channel-strategy` 方法**（`references/channel-strategy.md`）：由 人群 `channels` + 洞察趋势 + 时刻 `where` 推导 **渠道组合**（primary + support + why），AI 策展、无团队决策（仍只保留 A/B 一次决策）。④ **`creative-concept`** 创意简报扩展为 `For [segment] at [moment], riding [trend], via [channel] with [mechanic] → [desire]`，质量栏加「Channeled」，反例加「无渠道」。⑤ **`plan` SKILL capture**：`anchor` 增 `trend`/`channel`；每套 `variant` 增 `channel_mix`；assemble 增渠道组合。**模板 `campaign-plan.html`**：锚点行加 趋势+渠道、每套方案加「Channel & Moment」卡；`marketing-plan.md` 明确 Place=分销（媒介渠道归 channel-strategy）；`budget-model.md` 渠道列取自 `channel_mix`。⑥ **同步**：`commands/plan.md` · `DESIGN.md §7.2 + §3 树` · `README.md`（根 + `.opencode` 树）· `agents/{facilitator,runner}` · 本文件 §3 树 + §4 表 · `facilitator_guide.html`（目录树 + 旅程图「机会定义→渠道策略」+ §6 表）+ 重建 standalone · `Hackathon-Design/index.html` Create Loadout「Opportunity Definition→Channel Strategy」+ 重建 standalone · `hostdeck/{host-deck,toolkit-video-scripts}`。**demo-examples 未重建**（下次 `/run` 刷新）。
- 2026-10-07：**Plan/Poster 输入契约澄清（去「variant」+ 结构化 offer + 复用视觉方向）**。针对「poster 输入是否取自 plan 所选方案」的核查做四项优化（并顺带修一处 plan↔海报风格字母撞车）：① **去掉抽象词「variant」**：capture `variants`→**`plans`**、`chosen_variant`→**`chosen_plan`**；可见文案 `Variant A/B`→**`Plan A/B`**（`campaign-plan.html` 的 CSS `.variant`→`.plan` + 标题 + footer）；`references/{budget-model,channel-strategy}.md` 的「variant」→「plan」。② **poster 明确点名所选 plan**：`commands/poster.md` + `skills/poster/SKILL.md` 改为读 **`plans[chosen_plan]`**；`prove` 同步用 `chosen_plan`（原 `chosen_variant`）。③ **消歧**：`chosen_plan`（A|B=campaign）与 `poster_style`（a|b|c=设计）是两个概念，海报风格呈现带名称（Style A · Full-Bleed Hero …）。④ **结构化 offer（3b）**：每套 plan 的 `offer` 由字符串改为 **`{summary, cards:[3×{title,detail}]}`**（会员制即 tiers）；`campaign-plan.html` 新增「The Offer」卡；poster 1:1 映射（summary→LEAD、cards→3 卡）。⑤ **视觉方向/一句话下沉到每套 plan**：`plans.<X>.visual_direction` + `.one_liner`（原顶层 `poster` 单值对两套有歧义）；poster 与 showcase 兜底都**复用、不再 re-derive**；海报设计风格改用顶层 **`poster_style`**（a|b|c，由 `/poster` 写入，默认 a；与 showcase capture 一致）。落点：`skills/plan/{SKILL.md,templates/campaign-plan.html,references/{budget-model,channel-strategy}.md}` · `commands/{plan,poster,prove}.md` · `skills/poster/{SKILL.md,references/poster-method.md}` · `skills/prove/SKILL.md` · `skills/showcase/SKILL.md` · `DESIGN.md`。冒烟：capture JSON 解析通过（keys: plans/chosen_plan/poster_style），模板 `.variant`=0。
- 2026-10-09：**新增 `showcase` 子技能 `campaign-storyboard`**（生成独立 16:9 看板）。把 6 帧图片 + 走查文案装配为单文件 `storyboard.html`（**2 steps/页 · 3 页 · 深色沉浸 · 帧内嵌 data URI 自包含**）：新增 `skills/showcase/sub-skills/campaign-storyboard/{SKILL.md（name+英文触发词）,references/storyboard-method.md（帧/文案 schema · 6 步 journey · 版式/深色 token）,templates/{storyboard.html,storyboard.example.json},scripts/build-storyboard.py}`；脚本 `--dir/--spec/--frames/--out/--width/--per-page`，默认读 `media/storyboard/storyboard.json`，写 round 根 `storyboard.html`。同步：`skills/showcase/SKILL.md`（「No sub-skills」→ 子技能引用）· `skills/showcase/templates/prompt-pack.html`（新增 Storyboard 媒体类型：共享 STYLE + 6 帧提示词）· `skills/showcase/references/media-prompts.md`（工具表 + §3b Storyboard + 嵌入行）· `README.md`（§3 树 + §5 表）· `DESIGN.md`（§7.4 输出 + 吸收段 + §10 树）· 本文件 §3 树。冒烟验证：从既有 `demo-examples/QuestB-02/storyboard.html` 抽出 6 帧 → `build-storyboard.py --dir /tmp/sbtest` 重建（3 页 / 6 帧内嵌 / accent teal / 无残留占位符）。约定：pitch deck 的 `storyboard` beat 以 srcdoc 内嵌该文件，proposal 加「Storyboard」面板；**命名不带 quest**。
- 2026-10-09：**Host 大屏 Toolkit 演示去掉「Commands」一步**。`hostdeck/host-deck.html` 的 `SCENES` 移除 `IMG-02`（`Commands · Eight commands run the whole loop`）→ 由 18 场景减为 17（`IMG-01` 直连 `IMG-03`）；`hostdeck/toolkit-video-scripts.md` 删 P02 行并顺延编号（P01–P17）、运行时 `~2:00` → `~1:53`、manifest 去掉 `IMG-02`、player contract `18 objects` → `17 objects`；重新运行 `hostdeck/build-toolkit-demo.py` 重建 `toolkit-demo.html`（`img-02.jpg` 保留在盘、不再内嵌）。
- 2026-10-09：**Storyboard 的 prompt 改为「一条完整 prompt → 一张 6 面板单图」**（原为「共享 STYLE + 逐帧 6 条 prompt」，生成 6 张独立图）。① `skills/showcase/templates/prompt-pack.html`：Storyboard 卡由「STYLE + FRAME 01–06」7 段改为**单段完整 prompt**（`{{SB_PROMPT}}`），文案改为「paste it once → 单张 6 面板 sheet」。② `skills/showcase/references/media-prompts.md §3b`：重写为「one prompt → one 6-panel sheet（3×2 网格，style 一次锁定 + 六面板顺序 + verbatim 标题）」；工具表输出 `.png × 6` → `.png (one 6-panel sheet)`；嵌入表改为单图。③ **子技能 `campaign-storyboard` 改为单图模型**：`templates/storyboard.html`（单屏 16:9：brandbar + title + 居中 sheet + 六步 legend chip；不再分页/`per_page`）· `scripts/build-storyboard.py`（读 `board` 单图 → 内嵌 data URI → 单 `section`；移除 `--per-page` 分组；`--width` 默认 900→1600）· `templates/storyboard.example.json`（`steps[].file` → 顶层 `board`，steps 变为 `{n,label,headline}` legend）· `SKILL.md` + `references/storyboard-method.md` 全面改写。④ 同步：`skills/showcase/references/pitch-narrative.md`（signature「6-frame fan journey」→「6-panel fan-journey sheet」）· `skills/showcase/templates/pitch-deck.html`（CSS 注释）· `README.md`（§3 树）· `DESIGN.md §7.4` · 本文件 §3 树。⑤ `demo-examples/QuestB-02`：从旧 `storyboard.html` 抽出 6 帧拼成 3×2 单图 → 按新脚本重建 `storyboard.html`（1 sheet / 6 legend chips / accent teal / 无残留占位符）；`prompt-pack.html` 的 Storyboard 卡改为填入的单条完整 prompt。冒烟：`build-storyboard.py` 默认 `--dir` 布局与显式 `--spec/--frames/--out` 两种调用均通过。
