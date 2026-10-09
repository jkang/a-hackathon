---
name: plan
description: Run the PLAN/CREATIVE stage of the Ascentium mini-hackathon quest. Threads the campaign kernel from the insight (audience · moment · trend · channel · concept): the team gives 1–2 concept keywords up front, and the AI runs `creative-concept` to diverge to ~6 keyword-driven ideas, selects the channel mix, converges them into ONE complete campaign, and builds it fully (positioning, channel mix, offering, 4Ps, pilot, budget, hero visual). There is no A/B pick — the campaign is generated directly from the team's keywords. Triggers: "creative concept", "brainstorm", "big idea", "concept keywords", "channel strategy", "media plan", "pilot design", "campaign plan", "membership design", "marketing plan", "budget allocation".
---

# Plan — the PLAN/CREATIVE stage

The creative heart. Flow: **ask concept keywords (team, 1–2) → diverge (AI) → converge + build ONE campaign (AI) → hand off (no decision)**. The **team supplies the concept keywords**; the AI runs the divergence, the selection, and the full assembly.

## One input only

The stage opens with **exactly one team input**: **1–2 concept keywords** that should steer the campaign (given up front). Everything else is AI-run: the ~6-idea divergence, the convergence, the channel selection, the full plan, the pilot design, the budget, and the hero visual. There is **no A/B pick and no end-of-stage menu** — the campaign is generated directly from the team's keywords.

> The keywords are the team's creative authorship; the AI's job is to execute them into a complete, buildable campaign. Asking for 1–2 keywords replaces the old "pick A or B" decision with something the team can author from the start.

## Living plan — build it progressively

`campaign-plan.html` is **not** a one-shot final artifact. Like the insight brief, it is a **living document**:

- **Create it as soon as the first output lands** — once the concept keywords are in and the first concept draft exists, create/seed `campaign-plan.html`.
- **Rewrite it after every step** — divergence → convergence + full build → embedded hero visual. Each rewrite refreshes the page **and** its embedded `id="capture"` block.
- **The final page presents the single plan in full**, with the team's **concept keywords** shown alongside it.

## When to use

- After `insight` (reads the `insight-brief.html` capture: `selected_segments` + `focus_bundles` + `key_insights` + `segments` + `moment_of_truth`).
- When the team wants only the poster — use the `poster` skill directly.

## Inputs

- The `insight-brief.html` capture — the team's chosen segments (`selected_segments`) + the derived focus bundle(s) (segment × moment) + `selected_insights`. Note the channel raw material it carries: each segment's **`channels`** field and each insight's **trend** (the market read's channel facts).
- **The team's concept keywords (1–2)** — supplied at the stage's opening turn; the creative driver.
- Quest card — the **How Might We** if present, War Chest budget (MVP unlock + full), Victory Conditions.
- **Resume (recover upstream).** If run on its own (`/plan`), determine the quest id and find the latest round `artifacts/Quest<ID>-*`; if it's unambiguous, state it and continue — ask only when genuinely ambiguous. Read `insight-brief.html`'s `id="capture"` from that folder. If it's missing, say so and ask the team to run `/insight` first.

## Flow (uses the `facilitation` engine)

> **One input**: the stage opens by asking the team for **1–2 concept keywords** (with an example list, not a blank page), then stops for their reply. Everything after that is AI-run.

1. **Ask the keywords (team, up front).** Present a short **example list** (e.g. *national pride · first-timers · family · creators · collectors · eco/cause · nostalgia · underdogs · belonging · unmissable*) and ask for **1–2 keywords that should steer the campaign** — or their own. STOP and wait. Do not build yet.
2. **Diverge (AI).** On the reply, run the **`creative-concept`** sub-skill **on the concepts**: anchor (the chosen focus bundle's audience × moment) + reframe into **one HMW** that folds in the keywords, then run creative-thinking methods (SCAMPER · analogies · reverse · mash-ups · Crazy 8 · brainwriting) to generate **~6 candidate ideas** (name · one-line · insight · mechanic), each visibly reflecting the team's keywords.
3. **Converge + build (AI).** Converge the ~6 into **ONE complete campaign** aligned to the keywords, threading the **campaign kernel** (`audience · moment · trend · channel · concept`): **positioning** (Moore, `references/marketing-plan.md`), the **channel mix** (`references/channel-strategy.md` — grounded in the segment's `channels` + the insight's trend), **offering** (a structured `offer`: a one-line `summary` + exactly **3** `cards` — offer / markets / access, or the membership **tiers**), **4Ps**, **2 pilot markets** (card-consistent, `references/pilot-experiment.md`), the **pilot experiment** (hypothesis / treatment / control / measurement), the **budget** (`references/budget-model.md`, from the card's War Chest), and the **pilot forecast** — **3–5 funnel metrics**, each with its derivation chain (`benchmark → assumption → formula → target`, `references/pilot-forecast.md`). The plan carries its own **`visual_direction`** + **`one_liner`**.
4. **Render (AI).** Design a hero visual for the campaign and **embed it inside `campaign-plan.html`** — do **not** write standalone poster files here; those are produced only by the `/poster` stage.
5. **Complete (no decision).** Write the capture (`concept_keywords` + the single `plan` + its `pilot_forecast`, the `ideas` for the record). Hand off for **review**: invite the team to open `campaign-plan.html`, send feedback or changes (revise on reply), then run `/poster` and `/showcase`. No menu.

## HITL checkpoint (mandatory)

- Exactly **one**: the team supplies the **concept keywords (1–2)** at the opening turn.
The AI executes the keywords into the campaign but **never picks the keywords** for the team.

## Output

- `campaign-plan.html` — the **single plan** presented in full, with the team's **concept keywords** shown. DOC_TYPE "Campaign Plan" / "Membership Design". **The only artifact of this stage** — no separate data file and **no poster files** (the hero visual is embedded inline; the standalone poster is created by the `/poster` skill).
- Two template slots take small HTML fragments: `{{CONCEPT_KEYWORDS}}` = one `<span class="pill">…</span>` per keyword; `{{IDEAS_ROWS}}` = one `<div class="idea-row"><span class="n">n</span><div><b>name</b> — one-line · mechanic · keyword</div></div>` per candidate idea. The **Pilot Forecast** block uses `{{PF_n_NAME}}` / `{{PF_n_DIM}}` / `{{PF_n_TARGET}}` / `{{PF_n_DERIV}}` — fill 3–5 rows and **delete the unused rows**.
- The structured capture is embedded: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `showcase` stage reads it.

### capture block (embedded in `campaign-plan.html`)

```html
<script type="application/json" id="capture">
{
  "gate": "plan",
  "quest": "A",
  "selected_segments": [3, 1],
  "selected_insights": [1, 4],
  "concept_keywords": ["…", "…"],
  "anchor": {"segment": "…", "job": "…", "trend": "…", "moment": "…", "channel": "…", "mechanic": "…", "desire": "…"},
  "hmw": "How might we …",
  "ideas": [{"id": 1, "name": "…", "one_line": "…", "insight": "…", "mechanic": "…"}],
  "convergence": "how the AI converged the ideas into the plan, and how the keywords shaped it",
  "plan": {"name": "…", "slogan": "…", "proposition": "…",
           "offer": {"summary": "one-line offer",
                     "cards": [{"title": "…", "detail": "…"}, {"title": "…", "detail": "…"}, {"title": "…", "detail": "…"}]},
           "positioning": "…",
           "channel_mix": {"primary": "…", "support": ["…", "…"], "why": "…", "moment": "…"},
           "mix": {"product": "…", "price": "…", "place": "…", "promotion": "…"},
           "pilot": {"markets": ["…", "…"], "hypothesis": "…", "treatment": "…", "control": "…", "measurement_setup": "…"},
           "budget": {"total": "…", "allocation": [{"market": "…", "channel": "…", "tactic": "…", "amount": "…"}]},
           "pilot_forecast": [{"name": "…", "dimension": "reach | engagement | conversion | outcome", "target": "…",
                               "derivation": {"benchmark_ref": "…", "assumption": "…", "formula": "…"}}],
           "visual_direction": "…", "one_liner": "…"},
  "poster_style": "a"
}
</script>
```

> **Keys**: `concept_keywords` = the team's 1–2 keywords (the creative driver). There is a **single** `plan` object (no `plans` / `chosen_plan`). `offer.cards` = exactly **3** cards (offer / markets / access — or the membership **tiers**). `visual_direction` + `one_liner` live **inside the plan**; `poster_style` (a | b | c) is written later by the `/poster` stage (default `a`).

## Assemble (AI fills the framework; the team authors the keywords)

- **Positioning** — Geoffrey Moore (see `references/marketing-plan.md`).
- **Channel mix** — primary + supporting channels + why, grounded in the insight (see `references/channel-strategy.md`).
- **Offering** — the structured `offer`: a one-line `summary` + exactly **3** `cards` (offer / markets / access — or the membership **tiers**).
- **4Ps** (see `references/marketing-plan.md`) · **Pilot experiment** — hypothesis / treatment / control / measurement (see `references/pilot-experiment.md`) · **Budget** — from the card's War Chest (see `references/budget-model.md`) · **Pilot forecast** — 3–5 funnel metrics, each with its benchmark-anchored derivation chain (see `references/pilot-forecast.md`).

## Sub-skills & methods

- **Invoke the sub-skill**: `creative-concept` (concept keywords + anchor + HMW + creative methods → ~6 ideas) · `ascentium-brand` (the embedded hero visual).
- **Plan methods (references, not sub-skills)**: `marketing-plan.md` (positioning + 4Ps) · `channel-strategy.md` (channel mix) · `pilot-experiment.md` · `budget-model.md` · `pilot-forecast.md` (expected metrics + derivation chains).
