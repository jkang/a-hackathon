---
name: insight
description: Run the INSIGHT gate of the Ascentium mini-hackathon quest — turn the quest-card Scout Report plus the team's own knowledge into a rich, defensible Insight Brief: market & trends, audience segments (who + jobs-to-be-done + barrier + trigger), the moment of truth, raw market truths, and a single seed insight. Human-led, AI-scaffolded. Use at the start of Quest A (Doha 2030 ticketing) or Quest B (Chengdu Panda global IP). Triggers: "insight gate", "seed insight", "audience analysis", "audience segments", "market trend", "trend analysis", "moment of truth", "market truth", "scout report", "quest insight".
---

# Quest Insight — the INSIGHT gate

Produce a one-page **Insight Brief** that seeds the creative gate. The AI scaffolds (reads the card, structures, formats); the **team supplies the market truth, the audience segments, the trends, and the moment of truth, and confirms the seed insight.**

> A thin insight produces a thin plan. This gate must surface **who** the audience is, **what job** they hire, **what's shifting**, and **when/where** the decision happens — before any creative work.

## When to use

- Right after kick-off, before `plan`.
- When the team wants to redo insight, or skip ahead (then reuse quest-card data as the fallback seed).

## Inputs

- The quest card (Quest A or B) — already contains the Scout Report, War Chest, and Victory Conditions. **Treat it as the primary data pack.**
- The team's own knowledge — the primary *human* source (they are the SEA business leaders / IP operators).

## Flow (uses the `facilitation` engine)

> **Choice-first**: every input step below opens with an **AI-drafted menu of 6–8 grounded options** (`facilitation` → `option-menu.md`); the team **selects** (pick N) and may add `+1 of our own`. Never ask a blank question.

1. **Kick-off + research (AI, ~2 min).** Read the card; deliver a 30-second scout summary + org profile/benchmark scaffold. Then **actively use `agent-reach`** to gather real facts — market/consumer-trend reports, benchmarks, and data relevant to the quest — and turn them into **data-backed insight options** (not generic labels). This grounds every menu below.
2. **Market & trends (team).** AI presents a **menu of ~8 shifts** → the team picks 2–3 (or +1 own), each `{trend, why_it_matters}`.
3. **Audience (team).** AI presents a **menu of ~8 fan segments** → the team picks 2–4, each with `who / job (functional, social, emotional) / barrier / trigger`.
4. **Moment of truth (team).** AI presents a **menu of ~8 candidate moments** → the team picks 1–2 (time / place / event).
5. **Truths (team).** AI presents a **menu of ~8 candidate field truths** → the team picks the ones that resonate (or +1 own); capture verbatim.
6. **Cluster & converge.** Affinity-cluster the picks → the team confirms **one seed insight** (a one-line tension).
7. **Capture.** Write `insight.yaml` (record the menu + the team's selection).

## HITL gates (mandatory)

- The AI presents the menus; the team **selects** the audience segments, trends, and the moment of truth.
- The team confirms the seed insight.
The AI must **not** choose any of these — it only drafts the menu. Always keep the `+1 of our own` channel open.

## Output

- `insight-brief.html` — Ascentium-branded one-pager (use `templates/insight-brief.html` + `ascentium-brand`).
- `insight.yaml` — structured capture for downstream gates.

### insight.yaml schema

```yaml
quest: A | B
client: "..."
mission: "one line from the card"
org_profile: {assets: [...], constraints: [...]}
benchmark: {gold_standard, cautionary_tale, arena}
market:
  trends: [{trend, why_it_matters}]          # 2–3 shifts
  truths: [{author, text}]                    # raw field truths, verbatim
segments:                                      # 2–4 audience segments
  - {name, who, job_functional, job_social, job_emotional, barrier, trigger}
moment_of_truth: {when, where, event}          # the decision scenario
clusters: [{theme, items}]                     # AI affinity clustering
seed_insight: "the one-line tension the team confirmed"
source_note: "Scout Report, Data as of 2026-09"
```

## Methodology anchors

- **STP — Segmentation**: 2–4 fan segments, by market + psychographic.
- **JTBD**: functional / social / emotional job for each segment.
- **Trend analysis**: behavior / culture / policy shifts.
- **Moment of truth**: the time-place-event where demand is manufactured.
- See `references/insight-method.md`.

## Research & restraint

- **The AI researches; the team doesn't.** In this gate, actively call `agent-reach` to gather facts, reports and data, then distill them into **valuable, data-backed insight options**. The team's effort goes into *selecting*, not researching.
- Restraint means: don't turn the room into a research marathon, and don't dump raw data — **distill each fact into a crisp, defensible option** (a number, a trend, a named behavior). Richer *analysis*, not more data.
- Ground every menu in the card + `agent-reach` findings; cite the source in the option.

## Design notes

- Sub-skills: `agent-reach` (live research), `business-research`, `swot-analysis` — used by this stage.
- Keep the brief to ONE page. It is a seed for creativity, not a research report.
