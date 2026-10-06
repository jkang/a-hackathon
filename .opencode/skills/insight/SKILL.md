---
name: insight
description: Run the INSIGHT gate of the Ascentium mini-hackathon quest — turn the quest-card Scout Report plus the team's own knowledge into a rich, defensible Insight Brief: market & trends, audience segments, the moment of truth, raw market truths, focus bundles, and data-backed key insights. The AI curates everything (focus bundle · trends · segments · moments · truths); the brief is built progressively and always lists every option. The team makes ONE decision — the Key Insights (2–3) to carry into the plan. Human-led, AI-scaffolded. Use at the start of any quest (reads the quest card). Triggers: "insight gate", "seed insight", "audience analysis", "focus bundle", "market trend", "moment of truth", "scout report", "insight".
---

# Quest Insight — the INSIGHT gate

Produce a one-page **Insight Brief** that seeds the creative gate. The AI does all the research and **every selection** (focus bundle · trends · segments · moments · truths, plus the SWOT). The **team makes ONE decision** — which **key insights** to carry into the plan.

> Rationale: 40 minutes is tight. The AI curates everything and the team makes a **single, high-value call at the end** of the gate — instead of five separate picks.

## When to use

- Right after kick-off, before `plan`.
- When the team wants to redo insight, or skip ahead (then reuse quest-card data as the fallback seed).

## Inputs

- The quest card (the challenge brief) — already contains the Scout Report, War Chest, and Victory Conditions. **Treat it as the primary data pack.**
- The team's own knowledge — the primary *human* source (the market / business experts in the room).

## One decision only

The gate ends in **exactly one team decision**: **pick 2–3 key insights** (from ~6 AI-drafted, data-backed insights).

Everything upstream is **AI-curated and shown in full** in the brief, each option marked `AI pick` and overridable on request:
- the **focus bundle(s)** (audience × moment × shift) — the AI selects the strongest;
- **trends**, **segments**, **moments of truth**, **truths**, and the **SWOT**.

## Living brief — build it progressively

`insight-brief.html` is **not** a one-shot final artifact. It is a **living brief**:

- **Create it as soon as the first research block lands** — right after the brief is confirmed and the kick-off / org research returns, create the round folder `artifacts/Quest<ID>-<NN>/` and write the skeleton (scout summary + org profile) with short `researching…` placeholders for the rest.
- **Rewrite it after every step** — audience & trends → moments & truths & SWOT → focus bundle (AI) → key insights → seed. Each rewrite refreshes the page **and** its embedded `id="capture"` block.
- **Always list every candidate option** in each block, not just the picks: chosen → highlighted (`SELECTED`); not chosen → dimmed (`is-parked`); AI-curated → tagged (`AI pick`).

## Flow (uses the `facilitation` engine)

> **Choice-first**: the single decision opens with an **AI-drafted menu of 6–8 grounded options** (`facilitation` → `option-menu.md`); the team **selects** and may add `+1 of our own`. Never ask a blank question.

**Research chain (sub-skills):** `agent-reach` → `business-research` → `audience-analysis` → `swot-analysis`.
- `agent-reach` is the **shared data engine**; `business-research` and `audience-analysis` both call it.
- `business-research` (internal) feeds `audience-analysis` (fit) and `swot-analysis` (S/W).
- `audience-analysis` (external) feeds `swot-analysis` (O/T).
- Use the `researcher` subagent to run `agent-reach` and return **data-backed menus**.

**Before any research (only if the session hasn't been briefed yet): brief & confirm (HITL).** If the team already confirmed the brief via `/start`, skip this and go straight to research. Otherwise, read the card, then tell the team in a few plain lines: (1) what this quest is — client, mission, market; (2) the four gates — Insight → Plan (+ poster) → Prove → Showcase; (3) what happens next — you will research this quest and turn it into **~6 data-backed insights**; (4) that the research **may take a few minutes**. Then present the **fixed start menu** (verbatim — do not reword/reorder/add): **1** Start the research · **2** Skip research (reuse the Scout Report) · **3** Reuse the card + add our own facts; **wait for the team's reply.**

1. **Seed the brief (AI).** After the go-ahead, deliver a 30-second scout summary and run **`business-research`** (via `agent-reach`) for the **organization profile** + benchmark. **Create `insight-brief.html` now** with the scout summary + org profile (placeholders for what's still coming).
2. **Research & curate all menus (AI, no decision).** Run **`audience-analysis`** + trend + truth research via `agent-reach`; then run **`swot-analysis`**. Distil, as **full data-backed menus**: trends (~6–8), segments (~6–8), candidate moments (~6–8), candidate field truths (~6–8), each with a fact/number/behavior + source. **Select the focus bundle(s)** (audience × moment × shift) and mark your `AI pick`s. **Rewrite the brief** listing every option.
3. **Draft key insights (AI, no decision).** Distil **~6 key insights** from the org profile + trends + audience + focus + SWOT. Each insight = a **data-backed tension** (a fact/trend + its "so what") with a source. **Rewrite the brief** listing all ~6.
4. **DECIDE (team) — the single decision.** Present the **~6 key insights** inline → the team **picks 2–3** to carry into `plan` (the rest are parked). **Rewrite the brief** (chosen highlighted).
5. **Seed insight (AI).** Synthesize the one-line overarching tension from the chosen insights. Finalize the brief + capture.
6. **Capture.** Every rewrite refreshes the artifact's embedded `id="capture"` block (see Output). No separate data file.

## HITL gate (mandatory)

- **Before research begins**, the team confirms the brief (mission + four gates + that research may take a few minutes).
- Exactly **one** decision: the team **picks 2–3 key insights**.
The AI must **not** make that pick — it drafts the menu. The focus bundle, trends, moments, and truths are AI-curated but always **shown in full** and overridable on request (e.g. the team says "redo the trends"). Always keep the `+1 of our own` channel open.

## Output

- `insight-brief.html` — Ascentium-branded one-pager (use `templates/insight-brief.html` + `ascentium-brand`). **The only artifact** — no separate data file. Built **progressively** (created on the first research block, rewritten at every step).
- The structured capture is embedded in that artifact: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `plan` gate reads it.

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
  "trends": [{"id": 1, "trend": "…", "why_it_matters": "…", "source": "…", "ai_pick": true}],
  "truths": [{"id": 1, "text": "…", "source": "…", "ai_pick": true}],
  "segments": [{"id": 1, "name": "…", "who": "…", "job_functional": "…", "job_social": "…", "job_emotional": "…", "barrier": "…", "trigger": "…", "source": "…", "ai_pick": false}],
  "moments": [{"id": 1, "text": "…", "ai_pick": true}],
  "focus_bundles": [{"id": 1, "name": "…", "segment_ids": [3], "moment_id": 2, "trend_id": 4, "why": "…", "ai_pick": true}],
  "selected_focus": [1],
  "moment_of_truth": {"when": "…", "where": "…", "event": "…"},
  "swot": {"strengths": ["…"], "weaknesses": ["…"], "opportunities": ["…"], "threats": ["…"]},
  "key_insights": [{"id": 1, "text": "fact/trend + so-what", "evidence": "…", "source": "…", "selected": true}],
  "selected_insights": [1, 4],
  "seed_insight": "the one-line overarching tension",
  "source_note": "Scout Report, Data as of 2026-09"
}
</script>
```

> **Every menu carries all its options**, each with a `selected` / `ai_pick` flag — never only the winner. `selected_focus` is an **AI pick**; `selected_insights` is the **team's single decision**. The `plan` gate consumes `selected_insights`, `segments`, and `moment_of_truth`.

## Methodology anchors

- **STP — Segmentation**: 2–4 fan segments, by market + psychographic.
- **JTBD**: functional / social / emotional job for each segment.
- **Trend analysis**: behavior / culture / policy shifts.
- **Moment of truth**: the time-place-event where demand is manufactured.
- **Focus bundle**: audience × moment × shift, in one coherent package (AI-selected).
- See `references/insight-method.md`.

## Research & restraint

- **The AI researches; the team doesn't.** In this gate, actively call `agent-reach` to gather facts, reports and data, then distill them into **valuable, data-backed insight options**. The team's effort goes into *one decision*, not research.
- Restraint means: don't turn the room into a research marathon, and don't dump raw data — **distill each fact into a crisp, defensible option** (a number, a trend, a named behavior). Richer *analysis*, not more data.
- **Cap retries at 2–3 attempts per source.** If a site / report keeps failing, mark it **unreachable**, move on, and use another source — never loop on one dead link. If the web is largely unreachable, fall back to the card's Scout Report and say what could not be verified.
- Ground every menu in the card + `agent-reach` findings; cite the source in the option.

## Design notes

- **Invoke these sub-skills** (do not hand-roll their output): `agent-reach` (live research → data-backed options), `business-research` (organization profile), `audience-analysis` (segment the audience — profiles, needs, market potential), `swot-analysis`.
- Keep the brief to ONE page. It is a seed for creativity, not a research report.
- Content area is **80% of the viewport width** (max 1600px) — see the template's `.page`. Do not reintroduce decorative side bars (`border-left`) — AGENTS §5.2.
