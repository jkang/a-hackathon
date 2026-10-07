---
name: audience-analysis
description: Identify and segment the campaign audience — find relevant audience data and trend reports, split the audience into 3–5 segments, and profile each one (who they are, jobs-to-be-done, needs & motivations, barriers & triggers, where to reach them, size & market potential, trend). Produces the audience/segment menu for the insight gate; the TEAM then picks 2–3 segments to target (the gate's decision 1). Uses the agent-reach sub-skill for audience data & reports. Triggers: "audience analysis", "audience segments", "target audience", "segmentation", "persona", "audience research", "who is it for".
---

# Audience Analysis — find, segment & profile the audience

The insight gate's counterpart to `business-research`: research the **audience** the same way, then split it into segments and profile each. Output = an **audience/segment map** that seeds the campaign's targeting.

> One-liner: **who are they, what job do they hire us for, and how big is the prize?**

## When to use

- In the insight gate, to build the **audience / segment map**.
- Anytime a campaign needs to know who it is for and how to prioritise them.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Marketing objective | yes | what the campaign must achieve |
| Market / region | yes | e.g. Asia, overseas markets |
| Org profile | recommended | from `business-research` (offer, assets) |
| Audience data / trend reports | recommended | the user may supply; otherwise fetch via `agent-reach` |

## How to research (live, via `agent-reach`)

- Find **audience data + trend reports**: audience size, growth, behaviour, platform mix.
  - Exa search (`mcporter call exa.web_search_exa(query: "…")`), Jina reader for full pages (`curl -s "https://r.jina.ai/URL"`), YouTube, platform data.
  - Typical sources: digital/social reports, tourism & sports bodies, fan surveys, industry analyses.
- **Open the source and read the full report** — never rely on snippets.
- Attach a **source + date** to every size/trend number; separate fact from `[inference]`.

## Method (5 steps)

1. **Define the universe** — who is in scope (the total audience), and how large is it.
2. **Gather data & trend reports** — size, growth, behaviour, channels (live, via `agent-reach`).
3. **Segment** — split into **3–5 segments**; pick an explicit basis (motivation/need, life-stage, geography, or behaviour). Segments must be **distinct and actionable**.
4. **Profile each segment** — fill the profile fields below (esp. the **job-to-be-done** and **needs/motivations**).
5. **Prioritise (recommendation only — never auto-select)** — score **attractiveness × fit** (see framework) to order the segments, then hand them to the team as a **menu**. **The team picks 2–3** — this is the insight gate's **decision 1**.

## Segment profile fields

- **Name** — an evocative label
- **Who** — demographics + psychographics + geography
- **Job-to-be-done** — functional · social · emotional (JTBD)
- **Needs & motivations** — why they would act
- **Barriers** — what stops them today
- **Triggers** — what flips them into action
- **Channels** — where to reach them
- **Size** — estimated reach / addressable
- **Market potential** — size × value / propensity (rough TAM→SAM)
- **Trend** — growing / flat / declining, with evidence
- **Priority** — Tier 1 / 2 / 3

## Output

- A **Segment Map** (the segment cards, rendered into the insight brief; template + sizing/prioritisation in [`references/segmentation-framework.md`](references/segmentation-framework.md)).
- The structured `segments` object is embedded in the `insight-brief.html` capture (no separate file); the team's pick is recorded as `selected_segments`.

## Self-check

- [ ] **3–5 segments**, distinct and actionable (not overlapping).
- [ ] Each has an explicit **job-to-be-done** + **needs/motivations**.
- [ ] Each size/trend number has a **source + date**.
- [ ] **Market potential** stated per segment (rough is fine).
- [ ] Segments are **prioritised** (attractiveness × fit) as a menu — the **team** picks 2–3, not the AI.
- [ ] Facts vs `[inference]` separated; **no fabricated numbers**.

## Where it fits (insight research chain)

- **Upstream**: **`agent-reach`** (audience data + trend reports) and `business-research` (org offer / assets → **fit**).
- **Downstream**: `swot-analysis` (**external O/T**) and the `plan` gate (target segment).
