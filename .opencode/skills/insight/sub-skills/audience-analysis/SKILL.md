---
name: audience-analysis
description: Identify and segment the campaign audience — find relevant audience data and trend reports, split the audience into 6–8 segments, and profile each one (who they are, jobs-to-be-done, barriers & triggers, where to reach them, size & market potential). Produces the audience/segment menu for the insight stage; the TEAM then picks 2–3 segments to target (the stage's decision 1). Uses the agent-reach sub-skill for audience data & reports. Triggers: "audience analysis", "audience segments", "target audience", "segmentation", "persona", "audience research", "who is it for".
---

# Audience Analysis — find, segment & profile the audience

The insight stage's counterpart to `business-research`: research the **audience** the same way, then split it into segments and profile each. Output = an **audience/segment map** that seeds the campaign's targeting.

> One-liner: **who are they, what job do they hire us for, and how big is the prize?**

## When to use

- In the insight stage, to build the **audience / segment map**.
- Anytime a campaign needs to know who it is for and how to compare segments.

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
3. **Segment** — split into **6–8 segments**; pick an explicit basis (motivation/need, life-stage, geography, or behaviour). Segments must be **distinct and actionable**.
4. **Profile each segment** — fill the profile fields below (esp. the **job-to-be-done**, **barrier / trigger**, and **channels**).
5. **Present as a menu (never auto-select)** — hand the segments to the team as a **menu** (you may flag a soft recommendation, but never rank-pick). **The team picks 2–3** — this is the insight stage's **decision 1**.

## Segment profile fields

- **Name** — an evocative label
- **Who** — demographics + psychographics + geography
- **Job-to-be-done** — functional · social · emotional (JTBD)
- **Barriers** — what stops them today
- **Triggers** — what flips them into action
- **Channels** — where to reach them
- **Size & market potential** — estimated reach → rough addressable (TAM→SAM), with source

> These are the fields the insight brief captures verbatim (`{name, who, job_functional, job_social, job_emotional, barrier, trigger, channels, size_potential, source}`). Market **trend** is owned by `market-trends`; the AI does not rank segments (the **team** picks) — so no "priority" field.

## Output

- A **Segment Map** (the segment cards, rendered into the insight brief; template + sizing/choice-framing in [`references/segmentation-framework.md`](references/segmentation-framework.md)).
- The structured `segments` object is embedded in the `insight-brief.html` capture (no separate file); the team's pick is recorded as `selected_segments`.

## Self-check

- [ ] **6–8 segments**, distinct and actionable (not overlapping).
- [ ] Each has an explicit **job-to-be-done** (functional · social · emotional) + **barrier** + **trigger**.
- [ ] Each size number has a **source + date**.
- [ ] **Channels** and **size & market potential** stated per segment (rough is fine).
- [ ] Handed to the team as a **menu** — the **team** picks 2–3, not the AI (no AI rank-pick).
- [ ] Facts vs `[inference]` separated; **no fabricated numbers**.

## Where it fits (insight research chain)

- **Upstream**: **`agent-reach`** (audience data + trend reports) + `market-trends` (the market backdrop that frames segmentation) + `business-research` (org offer / assets → **fit**).
- **Downstream**: the **focus bundles** (segment × moment × trend, one per selected segment) and the `plan` stage (target segment).
