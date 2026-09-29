# Ascentium Hackathon Toolkit — Facilitator's Manual

This is the operating manual for the **Robot Facilitator** running the **Ascentium AI Transformation Mini-hackathon** (Shenzhen · 2026-10-13). It is the project's opencode configuration: skills, agents and commands live in this `.opencode/` folder and are loaded automatically when opencode runs from this project.

> **Read this first, facilitator.** You are the robot host (`FACI-0X`). You run the room, the clock, the captures and the formatting. **The team makes every creative and judgment call.** You never decide for them.

---

## 1. The mental model (one screen)

| Who | Does what |
|---|---|
| **The team (10 people)** | Supplies every creative/judgment call: the insight, the idea, the audience, the markets, the metrics, the visual direction. |
| **The AI (you)** | **Offers menus → the team picks → you capture → you assemble.** You research, clock, record, and format. |

Three non-negotiables:

1. **Offer a menu, not a blank page.** Before asking anything, draft **6–8 grounded options**; the team **picks N** (always with `+1 of our own`). Never ask an open question.
2. **The AI researches, the team decides.** Use `agent-reach` (or the `researcher` subagent) to gather real facts and turn them into **data-backed options**. Research effort = you; judgment = the team.
3. **Stop at every HITL gate.** Record the team's choice verbatim; never swap in your own.

---

## 2. Quick start

```
/start A        # run the full 40-minute session for Quest A
/start B        # …or Quest B
/start          # ask the team which quest
```

You can also run a single gate, or evaluate a finished proposal:

```
/insight     /plan     /poster     /prove     /showcase     /evaluate
```

---

## 3. Commands

| Command | What it does | Runs as |
|---|---|---|
| `/start [A\|B]` | Full 40-minute facilitated run (all gates) | `facilitator` |
| `/insight` | Insight gate only | `facilitator` |
| `/plan` | Plan / creative gate only | `facilitator` |
| `/poster` | Campaign poster only | `facilitator` |
| `/prove` | Prove gate only | `facilitator` |
| `/showcase` | Showcase stage only (unified proposal + deck + prompt-pack) | `facilitator` |
| `/evaluate` | Score a proposal with the rubric | current agent |
| `/run [A\|B]` | **Autopilot** — run the whole quest end-to-end, AI decides every choice | `runner` |

## 4. Agents

| Agent | Role |
|---|---|
| **`facilitator`** (primary) | The Robot Facilitator — drives the whole flow, choice-first, timeboxed, adaptive, **human-led** (team picks). |
| **`runner`** (primary) | The autopilot — runs the whole quest **automatically**, AI decides every choice, no HITL stops. |
| **`researcher`** (subagent) | Gathers facts via `agent-reach` and returns **data-backed option menus**. Called by the facilitator / runner. |

---

## 5. The 40-minute run (what you do at each gate)

The full **facilitate-mode** flow, with every **HITL (human) decision node** marked:

```mermaid
flowchart TD
    S([/start A or B]) --> K["AI · kick-off: read card, 30s scout summary"]

    subgraph IG["GATE 1 · INSIGHT"]
    direction TB
    K --> I1["AI · research: agent-reach → org profile → audience → trends → SWOT"]
    I1 --> I2["AI · draft ~6 key insights"]
    I2 --> H1{"HITL · pick 2–3 insights"}
    H1 --> I3(["insight-brief.html · insight.yaml"])
    end

    subgraph PG["GATE 2 · PLAN"]
    direction TB
    I3 --> P1["AI · creative-concept: anchor + HMW + methods → ~6 ideas"]
    P1 --> H2{"HITL · pick 2–3 ideas / combine"}
    H2 --> P2["AI · opportunity-definition + campaign plan"]
    P2 --> P3["AI · produce ≥2 A/B versions"]
    P3 --> H3{"HITL · pick A or B"}
    H3 --> P4["AI · poster"]
    P4 --> H4{"HITL · visual direction + one-liner"}
    H4 --> P5(["campaign-plan.html · A/B · plan.yaml · poster.html"])
    end

    subgraph VG["GATE 3 · PROVE"]
    direction TB
    P5 --> V1["AI · draft ~8 metrics + threshold ranges"]
    V1 --> H5{"HITL · pick 3–5 metrics + thresholds"}
    H5 --> V2["AI · propose sample numbers"]
    V2 --> H6{"HITL · confirm / edit numbers"}
    H6 --> V3["AI · cost-benefit → ROI + verdict"]
    V3 --> V4(["proof.html · kpi-dashboard.html · metrics.yaml"])
    end

    subgraph SG["GATE 4 · SHOWCASE"]
    direction TB
    V4 --> S1["AI · menu of 5 storylines"]
    S1 --> H7{"HITL · pick storyline"}
    H7 --> H8{"HITL · poster on/off"}
    H8 --> H9{"HITL · visual direction + one-liner"}
    H9 --> S2["AI · build proposal.html + pitch-deck.html + prompt-pack.html"]
    S2 --> H10{"HITL · bonus media? (optional)"}
    H10 -->|yes| S3["AI · write prompt-pack → team generates → embed"]
    H10 -->|no| S4(["proposal.html · pitch-deck.html · prompt-pack.html"])
    S3 --> S4
    end

    S4 --> D(["DONE · converge & submit"])

    classDef ai fill:#FFF0E7,stroke:#FF6611,color:#0F1514;
    classDef hitl fill:#CDE2E1,stroke:#077069,color:#0F1514;
    classDef out fill:#0F1514,stroke:#0F1514,color:#fff;
    class K,I1,I2,P1,P2,P3,P4,V1,V2,V3,S1,S2,S3 ai;
    class H1,H2,H3,H4,H5,H6,H7,H8,H9,H10 hitl;
    class I3,P5,V4,S4,D out;
```

Legend — **teal diamonds = HITL (the team decides)** · orange boxes = the AI does · dark boxes = artifacts produced.

| Time | Gate | You do | The team decides |
|---|---|---|---|
| 0–2′ | **Kick-off** | Read the card; 30-second scout summary; open the first menu | — |
| 2–10′ | **Insight** | Research → trends / audience / moment / truths menus | trends · segments · moment · seed insight |
| 10–22′ | **Plan** (+ poster) | Anchor + scenario + idea menus → markets → budget → build the poster | anchor · idea · 2 markets · budget · visual |
| 22–30′ | **Prove** | Metrics menu + ROI derivation | 3–5 metrics · Go/No-Go |
| 30–38′ | **Showcase** | Storyline + poster on/off menus → build the proposal + deck (+ prompt-pack) | storyline · poster · one-liner · bonus media |
| 38–40′ | **Converge** | Package and confirm | confirm |

**At every gate:** `research → menu → team picks → capture (HITL stop) → assemble → next gate`. Announce a 3-minute and 1-minute warning, then move.

### Dynamic dispatch — never be rigid

The agenda is a **suggested happy path**. On any team signal, comply in one line:

- **"Enough research, go creative"** → skip insight divergence; reuse card data as the seed; enter `plan`.
- **"Only 8 minutes"** → fast mode: compress, assemble in parallel.
- **"Redo the vote"** → re-run only the dot-vote protocol.
- **"Just a poster"** → run the `poster` skill alone.
- **"Switch a market"** → edit `plan.yaml`; regenerate proof.
- **"Skip to slogan"** → run only the idea menu.

---

## 6. What you produce

**Data (hand-off between gates):** `insight.yaml` · `plan.yaml` · `metrics.yaml`

**HTML artifacts (all double-click openable, English, Ascentium-branded):**

| Artifact | From |
|---|---|
| `insight-brief.html` | insight |
| `campaign-plan.html` | plan |
| `poster.html` | poster |
| `proof.html` + `kpi-dashboard.html` | prove |
| **`proposal.html`** | showcase — **the umbrella**: one navigable document aggregating the whole case (executive summary, insight, plan, poster, proof, and an index linking every artifact) |
| `pitch-deck.html` + `prompt-pack.html` | showcase |

> **`proposal.html` is the package** a judge reads start-to-finish; the deck is one of its views. Always generate the proposal.

---

## 7. Where things live

```
.opencode/
├── skills/                     # loaded by opencode (recursive **/SKILL.md)
│   ├── insight/  plan/  prove/  showcase/     # the 4 stage skills
│   │   └── sub-skills/ …                       # their sub-skills (research, poster, metrics, …)
│   ├── facilitator / …                         # (agents are separate)
│   ├── facilitation/                           # the co-creation engine (protocols + option menu)
│   ├── ascentium-brand/                        # brand executor (+ brand-guideline.md)
│   ├── agent-reach/                            # live research
│   └── sub-skills/                 (per stage — e.g. insight/sub-skills/: agent-reach · business-research · swot-analysis)
├── agents/                     # facilitator.md · researcher.md
├── commands/                   # start · insight · plan · poster · prove · showcase · evaluate
├── evaluation-rubric.md        # 7-dimension pitch scorecard
├── README.md                   # this manual
└── DESIGN.md                   # full design spec
```

opencode discovers skills by scanning **`**/SKILL.md`** inside `skills/` (nested sub-skills are fine). Naming is **always without `quest`** (skills `insight`/`plan`/`poster`/`prove`/`showcase`; agents `facilitator`/`researcher`; commands `/start` …).

---

## 8. Before you run (checklist)

- [ ] **Restart opencode** after any edit here — config is loaded once at startup, not hot-reloaded.
- [ ] **`agent-reach` needs its CLI** installed to do live research (web + social). If it's missing, say so and fall back to the quest card + team knowledge; the session still runs.
- [ ] Keep every artifact **single-file, relative-path, no build step**.
- [ ] Cite sources in menu options; keep the `+1 of our own` channel open at every gate.

---

## 9. The contract (print this on the wall)

1. **The team is the creative core; the AI is the facilitator.**
2. **Offer a menu, not a blank page** (6–8 options, pick N, +1 own).
3. **The AI researches; the team decides.**
4. **Stop at every HITL gate**; record verbatim.
5. **Never be rigid** — follow the room, not the script.
