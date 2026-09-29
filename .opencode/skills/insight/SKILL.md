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

**Research chain (sub-skills):** `agent-reach` → `business-research` → `audience-analysis` → `swot-analysis` → seed insight.
- `agent-reach` is the **shared data engine**; `business-research` and `audience-analysis` both call it.
- `business-research` (internal) feeds `audience-analysis` (fit) and `swot-analysis` (S/W).
- `audience-analysis` (external) feeds `swot-analysis` (O/T).
- Use the `researcher` subagent to run `agent-reach` and return **data-backed menus**.

1. **Kick-off + org research (AI, ~2 min).** Read the card; deliver a 30-second scout summary. Then run **`business-research`** (via `agent-reach`): build the **organization profile** (identity, offer, assets, routes, constraints) and the benchmark baseline.
2. **Audience research (AI).** Run **`audience-analysis`** (via `agent-reach`, using the org profile for fit): find audience data + trend reports, then draft the **segment menu** (3–5 segments with who / JTBD / needs / barriers / triggers / size / potential).
3. **Market & trends (team).** AI presents a **menu of ~8 shifts** → the team picks 2–3 (or +1 own), each `{trend, why_it_matters}`.
4. **Audience (team).** Present the **segment menu** → the team picks 2–4 and confirms/edits the profiles.
5. **Moment of truth (team).** AI presents a **menu of ~8 candidate moments** → the team picks 1–2 (time / place / event).
6. **Truths (team).** AI presents a **menu of ~8 candidate field truths** → the team picks the ones that resonate (or +1 own); capture verbatim.
7. **SWOT synthesis (AI drafts → team confirms).** Run **`swot-analysis`**: internal S/W (from `business-research`) × external O/T (from `audience-analysis` + market) → the strategic read.
8. **Key insights (AI drafts → team confirms).** Distil **~6 key insights** from the org profile + trends + audience + SWOT. Each insight = a **data-backed tension** (a fact/trend + its "so what"), with a source.
9. **Pick 2–3 to deep-dive.** The team **selects 2–3 of the ~6** to carry into the `plan` gate (the rest are parked). This is the gate's destination.
10. **Capture.** Write `insight.yaml` (record the menus, the ~6 insights, and the team's selection).

## HITL gates (mandatory)

- The AI presents the menus; the team **selects** the audience segments, trends, and the moment of truth.
- The team reviews the **~6 key insights** and **picks 2–3** to deep-dive into the plan.
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
swot: {strengths: [...], weaknesses: [...], opportunities: [...], threats: [...]}  # from swot-analysis
key_insights:                                   # ~6 AI-drafted, data-backed insights
  - {id: 1, text: "fact/trend + so-what", evidence: "...", source: "..."}
selected_insights: [1, 4]                       # 2–3 the team chose to deep-dive in the plan
seed_insight: "the one-line overarching tension (optional, ties the 6 together)"
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

- **Invoke these sub-skills** (do not hand-roll their output): `agent-reach` (live research → data-backed options), `business-research` (organization profile), `audience-analysis` (segment the audience — profiles, needs, market potential), `swot-analysis`.
- Keep the brief to ONE page. It is a seed for creativity, not a research report.
