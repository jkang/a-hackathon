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
├── README.md · DESIGN.md              # 文档
├── skills/                            # 技能（扁平：一技能一目录 —— opencode 发现约定）
│   ├── insight/                       # 洞察门 → insight-brief.html + insight.yaml
│   │   └── sources/  business-research/ · swot-analysis/
│   ├── plan/                          # 策划门 → campaign-plan.html + plan.yaml
│   │   └── sources/  opportunity-definition/ · pol-probe-advisor/ · creating-financial-models/
│   ├── poster/                        # Poster（Create 阶段）→ poster.html
│   ├── prove/                         # 论证门 → proof.html + kpi-dashboard.html + metrics.yaml
│   │   └── sources/  mvp-metrics-generator/ · data-visualizer-pro/
│   ├── showcase/                      # 呈现门（AUTO）→ pitch-deck.html + prompt-pack.html（内嵌 poster）
│   │   └── sources/  ref-palette-slide/ · html-ppt-generator/
│   ├── agent-reach/                   # 实时研究（insight 使用；CLI 需预装）
│   ├── facilitation/                  # 共创引擎（协议库/节奏/话术/选项菜单/采集契约）
│   ├── ascentium-brand/               # 品牌执行器（tokens.css + 规则 + brand-guideline.md）
│   └── sub-skills/                 (per stage — e.g. insight/sub-skills/: agent-reach · business-research · swot-analysis)
├── agents/                            # facilitator.md（编排）· researcher.md（研究）
├── commands/                          # start · insight · plan · poster · prove · showcase · evaluate
└── evaluation-rubric.md               # 方案评分卡（7 维度）
```

每个技能含 `SKILL.md` + `references/` +（可选）`templates/`；`sources/` 仅作原料。
opencode 发现约定为**扁平** `skills/<name>/SKILL.md`；`agent-reach` / `poster` 平铺（逻辑归 `insight` / `plan`）。命名**一律不带 `quest`**。

---

## 4. 技能处置清单（锁定）

**对外只暴露 4 个阶段技能 + 品牌 + Meta**（方案甲，分阶段打包）：

| 阶段技能 | 对接 Arsenal 能力 | 吸收/改造的 sources |
|---|---|---|
| `insight` | Market Research · Audience Analysis · Benchmark Analysis · Company Profiler (IP audit) | `business-research`、`swot-analysis` |
| `plan` | Opportunity Definition · Creative Concept · MVP Pilot Design · Marketing Plan · Budget | `opportunity-definition`、`pol-probe-advisor`、`creating-financial-models` |
| `poster`（Create 阶段，独立） | Poster（Create 阶段） | `ref-palette-slide` |
| `prove` | Campaign Metrics · Go/No-Go · Cost-Benefit · Data Analysis & Viz | `mvp-metrics-generator`、`data-visualizer-pro` |
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

### 5.3 数据与安全
- 禁止把私有凭证、token、内部 ID 写入仓库文件；需要时只写「红acted 摘要 + 稳定指针」。
- 活动命题卡中的数据为公开报道口径，引用时保留来源与 `Data as of` 标注。

### 5.4 输出与命名
- **产物默认英文（English-only）**：技能正文、触发词、YAML 字段、输出 HTML、README/Playbook、Facilitator 话术一律英文；受众为英文使用者。仅 `brand-guideline.md` 源文件与本 AGENTS.md / DESIGN.md 内部文档保留中文。代码 / 命令 / 路径 / 色值保持原样。
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

**待办 · 命题修订（用户 2026-09-28 提出，回头更新 `quest-cards.html`）**
- **Quest A 的市场范围要放宽**：`目标市场`从「Southeast Asia (SEA)」扩为**亚运会覆盖的国家范围（Asia-wide）**，且**明确包含 China**（不再排除中国大陆）。Mission 措辞相应从 "make Southeast Asia Doha's biggest away crowd" 调整为「亚运会参赛国家（含中国 + 东南亚）成为多哈最大客队」一类。
- 影响面（更新命题卡时一并核对）：`quest-cards.html` 的 Quest A Scout Report / Mission / HWM / Deliverables 里的 SEA 表述；`toolkit` 里 Quest A 相关示例（insight/plan 的 segment 与 market 口径）如需同步。

---

## 7. 变更记录

- 2026-09-28：创建本文件；完成 toolkit 骨架与可复用技能复制。
- 2026-09-28：登记 Quest A 市场范围修订（SEA → 亚运覆盖国家范围、含 China），待更新 `quest-cards.html`。
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
