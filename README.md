# Ascentium AI Transformation Mini-hackathon

Materials and the participant toolkit for the **Ascentium AI Transformation Mini-hackathon**
(Shenzhen · 2026-10-13).

- **Format:** 112 people · 8 teams × 14 · one 50-minute run (40′ build with the toolkit + 10′ assemble the Showcase and submit).
- **Challenges:** Quest A — 2030 Asian Games (Doha) ticketing & fan engagement; Quest B — Chengdu Panda Base global IP.
- **Deliverable:** a marketing business proposal per team, presented and voted on in the Showcase.

Working rules and locked decisions live in [`AGENTS.md`](./AGENTS.md). The facilitator-facing
operating manual lives in [`.opencode/README.md`](./.opencode/README.md).

---

## Repository map

```
Ascentium Hackathon/
├── README.md                         ← this file
├── AGENTS.md                         working rules & locked decisions (internal)
│
├── Hackathon-Design/                 event pages & print assets (participant facing)
│   ├── index.html · quest-cards.html · invitation-email.html
│   ├── ascentium-hackathon-standalone.html · ascentium-hackathon-standalone-zh.html
│   ├── Quest_Cards_A3_Print.pdf · assets/
│   ├── hostdeck/host-deck.html       HOST big-screen guide deck
│   └── build-hackathon-standalone.py bundler: event page → single file
├── .opencode/                        the participant toolkit (opencode project config)
├── demo-examples/                    signed-in sample outputs (Quest A v2)
│
├── facilitator_guide.html            Facilitator guide
├── facilitator_guide_standalone.html Facilitator guide, single self-contained file
└── build-facilitator-standalone.py   bundler: facilitator guide → single file
```

---

## Event materials — `Hackathon-Design/`

Participant-facing event pages, quest cards and print files. Brand logo is
`assets/ascentium_global_logo.jpeg`.

| File | What it is |
|---|---|
| `index.html` | Event landing page (schedule, teams, quests, rules). |
| `quest-cards.html` | The two Quest Cards (Mission, War Chest, Victory Conditions, Scout Report). |
| `invitation-email.html` | Attendee invitation email. |
| `ascentium-hackathon-standalone.html` | `index.html` with all images inlined — one file, double-click to open. |
| `ascentium-hackathon-standalone-zh.html` | Chinese one-file version. |
| `Quest_Cards_A3_Print.pdf` | Print-ready A3 quest cards. |
| `assets/` | Logos, hero image, quest topic images (`topic-a.png`, `topic-b.png`), trophy, robot. |

## Participant toolkit — `.opencode/`

The opencode project configuration the teams run. It loads automatically when opencode
runs from this folder. Full manual: [`.opencode/README.md`](./.opencode/README.md).

| File | What it is |
|---|---|
| `README.md` | Facilitator's manual — mental model, quick start, stages, timeline. |
| `DESIGN.md` | Toolkit design spec (internal, Chinese). |
| `quest-card.md` | Quest configuration contract — client / mission / War Chest / Victory Conditions / Scout Report + accent, key visual, poster styles. |
| `evaluation-rubric.md` | 7-dimension scoring rubric for proposals. |

**Skills** — `skills/<name>/SKILL.md` (+ `references/`, `templates/`, `scripts/`, `sub-skills/`):

| Skill | Stage | Output |
|---|---|---|
| `insight` | Insight stage | `insight-brief.html` — market trends → segments → key insights (team's two picks) |
| `plan` | Plan stage | `campaign-plan.html` — two A/B options for the team to pick |
| `poster` | Create | `poster.html` + `poster-a/b/c.html` (three styles) |
| `prove` | Prove stage | `proof.html` — one-screen pilot metrics with derivation logic |
| `showcase` | Showcase (AUTO) | `proposal.html` · `pitch-deck.html` · `prompt-pack.html` |
| `ascentium-brand` | support | Design tokens + brand rules (single source of truth: `brand-guideline.md`) |
| `facilitation` | support | Co-creation protocols, pacing, scripts, option menu, capture contract |
| `agent-reach` | support | Live research (used by `insight`) |

Sub-skills sit under their stage: `insight/sub-skills/` (business-research · market-trends · audience-analysis),
`plan/sub-skills/` (creative-concept), `prove/sub-skills/` (campaign-metrics · data-visualizer-pro — retained, dormant).

**Agents** — `agents/`: `facilitator.md` (orchestrator) · `runner.md` (automated run) · `researcher.md` (research).

**Commands** — `commands/`: `/start` · `/insight` · `/plan` · `/poster` · `/prove` · `/showcase` · `/evaluate` · `/run`.

## Sample outputs — `demo-examples/`

Signed-in reference outputs from a Quest A run, used by the facilitator guide and as a
worked example. Live runs are written to a per-round `artifacts/Quest<ID>-<NN>/` folder
(gitignored) and never overwrite an earlier round.

`demo-examples/QuestA-v2/`: `insight-brief.html` · `campaign-plan.html` · `poster.html` ·
`poster-a.html` · `poster-b.html` · `poster-c.html` · `proof.html` · `proposal.html` ·
`pitch-deck.html` · `prompt-pack.html`.

## Host & facilitator decks

| File | What it is |
|---|---|
| `Hackathon-Design/hostdeck/host-deck.html` | Host big-screen guide deck (Standby → Opening → Build → Showcase → Arena → Victory), with interactive timers. 16:9 stage. |
| `facilitator_guide.html` | Facilitator guide — responsibilities, tips, links into the toolkit. |
| `facilitator_guide_standalone.html` | Same guide with the demo outputs inlined — one shareable file. |

## Build scripts

| Script | Produces |
|---|---|
| `Hackathon-Design/build-hackathon-standalone.py` | `Hackathon-Design/ascentium-hackathon-standalone.html` (inlines `assets/`). |
| `build-facilitator-standalone.py` | `facilitator_guide_standalone.html` (inlines the Quest A demo outputs). |

Both are plain `python3` scripts with no dependencies: `python3 Hackathon-Design/build-hackathon-standalone.py`.
