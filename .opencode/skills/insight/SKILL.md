---
name: insight
description: Run the INSIGHT stage of the Ascentium mini-hackathon quest — turn the quest-card Scout Report plus the team's own knowledge into a rich, defensible Insight Brief. The AI researches and curates the market trends, audience segments, focus bundles, and key insights. The stage has TWO team decisions: (1) pick the audience segments (2–3) to target, and (2) pick the key insights (2–3) to carry into the plan. Human-led, AI-scaffolded. Use at the start of any quest (reads the quest card). Triggers: "insight stage", "seed insight", "audience analysis", "audience segments", "focus bundle", "market trend", "moment of truth", "scout report", "insight".
---

# Quest Insight — the INSIGHT stage

Produce a one-page **Insight Brief** that seeds the creative stage. The AI does all the research; the **team makes TWO decisions** — **which audience segments to target (2–3)**, then **which key insights to carry into the plan (2–3)**.

> Rationale: in a marketing challenge the team's first and most valuable call is *who to target*; the second is *which segment × moment × trend tension to run with*. The AI curates everything else, and the brief always lists every option.

## When to use

- Right after kick-off, before `plan`.
- When the team wants to redo insight, or skip ahead (then reuse quest-card data as the fallback seed).

## Inputs

- The quest card (the challenge brief) — already contains the Scout Report, War Chest, and Victory Conditions. **Treat it as the primary data pack.**
- The team's own knowledge — the primary *human* source (the market / business experts in the room).
- **Resume (recover upstream).** If this stage is run on its own (`/insight`), determine the quest id and find the latest round `artifacts/Quest<ID>-*`; if it's unambiguous, state it and continue — ask only when genuinely ambiguous. If an `insight-brief.html` already exists there, read its `id="capture"` and continue from it instead of starting over. (Insight has no upstream stage.)

## Two decisions

1. **Select the audience segments** — pick 2–3 from ~6–8 AI-drafted, data-backed segments. *(This defines who the campaign targets — the anchor for `plan`.)*
2. **Select the key insights** — pick 2–3 from ~6 AI-drafted insights, each fusing a selected segment × its moment × a supporting trend. *(These carry into `plan`.)*

Everything else is **AI-curated and shown in full** in the brief, overridable on request:
- the **Market Trends** — a merged market read (directional shifts + hard facts + the external opportunities/threats) — shown in full, no pick;
- the **Focus Bundles** — one per selected segment (audience × moment × shift), derived *after* the segment pick;
- the **Seed Insight** — synthesized from the picked insights.

## Living brief — build it progressively

`insight-brief.html` is **not** a one-shot final artifact. It is a **living brief**:

- **Create it as soon as the first research block lands** — right after the brief is confirmed and the kick-off / org research returns, create the round folder `artifacts/Quest<ID>-<NN>/` and write the skeleton (scout summary + org profile) with short `researching…` placeholders for the rest.
- **Rewrite it after every step** — market trends + segments → (team picks segments) → focus bundles → key insights → (team picks insights) → seed. Each rewrite refreshes the page **and** its embedded `id="capture"` block.
- **Always list every candidate option** in each block, not just the picks: chosen → highlighted (`SELECTED`); not chosen → dimmed (`is-parked`).

## Flow (uses the `facilitation` engine)

> **Choice-first**: each decision opens with an **AI-drafted menu of 6–8 grounded options** (`facilitation` → `option-menu.md`); the team **selects** and may add `+1 of our own`. Never ask a blank question.

**Research chain (sub-skills):** `agent-reach` → `business-research` → `market-trends` → `audience-analysis`.
- `agent-reach` is the **shared data engine**; the research skills call it.
- `business-research` (internal) → the **organization profile** (assets = strengths, constraints = weaknesses) + the **benchmark**.
- `market-trends` (external) → the **Market Trends** block — one merged market read (directional shifts + hard facts + external opportunities/threats), each item tagged `shift` / `fact` / `opportunity` / `threat`. **Trends come before segments**: the market read sets the backdrop and the attractiveness signals for segmentation.
- `audience-analysis` (external) → the **segments** (STP + JTBD).
- Use the `researcher` subagent to run `agent-reach` and return **data-backed menus**.

**Research choice (HITL).** If the mode was already chosen (e.g. from `/start`), honor it and proceed. Otherwise, on the first turn, tell the team in a few plain lines: (1) what this quest is — client, mission, market; (2) the four stages — Insight → Plan (+ poster) → Prove → Showcase; (3) what happens next — you will research this quest and turn it into **~6 data-backed insights**, and the stage has **two picks** (segments, then insights); (4) that the research **may take a few minutes**. Then present the **fixed start menu** (verbatim — do not reword/reorder/add): **1** Start the research · **2** Skip research (reuse the Scout Report) · **3** Reuse the card + add our own facts; **wait for the team's reply.** Honor the choice: **Start** → run the research chain; **Skip / Reuse** → skip research and seed the brief from the Scout Report.

1. **Seed the brief (AI).** After the go-ahead, deliver a 30-second scout summary and run **`business-research`** (via `agent-reach`) for the **organization profile** + benchmark. **Create `insight-brief.html` now** with the scout summary (benchmark folded in) + org profile (placeholders for what's still coming).
2. **Research & build the market read, then the segments (AI, no decision).** First run **`market-trends`** via `agent-reach` and distil the **Market Trends** (~6–8 — one merged read spanning directional shifts, hard field facts, and external opportunities/threats, each tagged `kind` + fact/number + source). Then run **`audience-analysis`** and distil the **segments** (~6–8 — STP + JTBD), using the trends as the attractiveness backdrop. **Rewrite the brief** after each, listing every option.
3. **DECISION 1 (team) — select the segments.** Present the **~6–8 segments** inline → the team **picks 2–3** to target. **Rewrite the brief** (chosen highlighted).
4. **Derive the focus bundles (AI, no decision).** For each **selected** segment, derive one **Focus Bundle** — segment × its **moment of truth** (when / where / event) × the supporting trend — plus the strategic why. **Rewrite the brief.**
5. **Draft key insights (AI, no decision).** Distil **~6 key insights**, each **derived from a focus bundle** so every insight fuses **a selected segment × its moment × a supporting trend** into a tension. Aim for **~2 insights per selected segment** (different trend/moment angles). Formula: **"[Segment] [job/desire] — but at [moment], [trend/fact] → [tension/gap] — so [implication]."** Carry each insight's `segment_id` + `trend_id` + `moment` + evidence + source. A trend restated without an audience or a moment is **not** a key insight. **Rewrite the brief** listing all ~6.
6. **DECISION 2 (team) — select the key insights.** Present the **~6 key insights** inline → the team **picks 2–3** to carry into `plan` (the rest are parked). **Rewrite the brief** (chosen highlighted).
7. **Seed insight (AI).** Synthesize the one-line overarching tension from the chosen insights. Finalize the brief + capture.

## HITL checkpoints (mandatory)

- **Before research begins**, the team makes the research choice (start the research / reuse the Scout Report / reuse + add facts).
- **Two decisions**: (1) the team **picks 2–3 segments**; (2) the team **picks 2–3 key insights**.
The AI must **not** make either pick — it drafts the menus. The market trends and focus bundles are AI-curated but always **shown in full** and overridable on request (e.g. the team says "redo the trends"). Always keep the `+1 of our own` channel open.

## Output

- `insight-brief.html` — Ascentium-branded one-pager (use `templates/insight-brief.html` + `ascentium-brand`). **The only artifact** — no separate data file. Built **progressively** (created on the first research block, rewritten at every step).
- The structured capture is embedded in that artifact: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `plan` stage reads it.

### capture block (embedded in `insight-brief.html`)

```html
<script type="application/json" id="capture">
{
  "gate": "insight",
  "quest": "A",
  "client": "…",
  "mission": "one line from the card",
  "org_profile": {"assets": ["…"], "constraints": ["…"]},
  "benchmark": {"gold_standard": "…", "cautionary_tale": "…", "arena": "…"},
  "trends": [{"id": 1, "trend": "…", "why_it_matters": "…", "kind": "shift | fact | opportunity | threat", "source": "…"}],
  "segments": [{"id": 1, "name": "…", "who": "…", "job_functional": "…", "job_social": "…", "job_emotional": "…", "barrier": "…", "trigger": "…", "channels": "…", "size_potential": "…", "source": "…", "selected": false}],
  "selected_segments": [3, 1],
  "focus_bundles": [{"id": 1, "name": "…", "segment_id": 3, "moment": {"when": "…", "where": "…", "event": "…"}, "trend_id": 4, "why": "…"}],
  "moment_of_truth": {"when": "…", "where": "…", "event": "…"},
  "key_insights": [{"id": 1, "segment_id": 3, "trend_id": 4, "moment": {"when": "…", "where": "…", "event": "…"}, "text": "segment × moment × trend tension", "evidence": "…", "source": "…", "selected": true}],
  "selected_insights": [1, 4],
  "seed_insight": "the one-line overarching tension",
  "source_note": "Scout Report, Data as of 2026-09"
}
</script>
```

> **Every menu carries all its options**, each with a `selected` flag — never only the winner. `selected_segments` and `selected_insights` are the **team's two decisions**. Each `key_insights` item fuses a `segment_id` + a `trend_id` + its `moment` — so no insight is trend-only. `moment_of_truth` is the **primary** selected focus's moment. The `plan` stage consumes `selected_segments`, `selected_insights`, `focus_bundles`, and `moment_of_truth`.

## Methodology anchors

- **STP — Segmentation**: ~6–8 fan segments, by market + psychographic.
- **JTBD**: functional / social / emotional job for each segment.
- **Trend analysis**: behavior / culture / policy shifts — merged with hard field facts and the external opportunities/threats into one market read, each item tagged `kind`.
- **Moment of truth**: the time-place-event where demand is manufactured (derived per selected segment, inside its focus bundle).
- **Focus bundle**: audience × moment × shift, one per selected segment.
- **Key insight**: a tension that fuses a selected segment × its moment × a supporting trend (derived from the focus bundles).
- See `references/insight-method.md`.

## Research & restraint

- **The AI researches; the team doesn't.** In this stage, actively call `agent-reach` to gather facts, reports and data, then distill them into **valuable, data-backed options**. The team's effort goes into *the two decisions*, not research.
- Restraint means: don't turn the room into a research marathon, and don't dump raw data — **distill each fact into a crisp, defensible option** (a number, a trend, a named behavior). Richer *analysis*, not more data.
- **Cap retries at 2–3 attempts per source.** If a site / report keeps failing, mark it **unreachable**, move on, and use another source — never loop on one dead link. If the web is largely unreachable, fall back to the card's Scout Report and say what could not be verified.
- Ground every menu in the card + `agent-reach` findings; cite the source in the option.

## Design notes

- **Invoke these sub-skills** (do not hand-roll their output): `agent-reach` (live research → data-backed options), `business-research` (organization profile + benchmark), `market-trends` (the merged market read — shifts + hard facts + opportunities/threats), `audience-analysis` (segment the audience — profiles, needs, market potential).
- Keep the brief to ONE page. It is a seed for creativity, not a research report.
- Content area is **80% of the viewport width** (max 1600px) — see the template's `.page`. Do not reintroduce decorative side bars (`border-left`) — AGENTS §5.2.
