---
name: plan
description: Run the PLAN/CREATIVE stage of the Ascentium mini-hackathon quest. Threads the campaign kernel from the insight (audience · moment · trend · channel · concept): the AI diverges to ~6 campaign ideas, selects the channel mix, narrows them into 2 complete, distinct campaign concepts (A/B), and builds each fully (positioning, channel mix, offering, 4Ps, pilot, budget, hero visual). The team makes ONE decision — pick the campaign (A or B) at the end of the stage. Triggers: "creative concept", "brainstorm", "big idea", "channel strategy", "media plan", "pilot design", "campaign plan", "membership design", "marketing plan", "budget allocation".
---

# Plan — the PLAN/CREATIVE stage

The creative heart. Flow: **diverge → converge + build A/B (AI) → the team picks ONE**. The **team chooses the campaign**; the AI runs the divergence, the selection, and the full assembly.

## One decision only

The stage ends in **exactly one team decision**: **pick the campaign (A or B)** — two complete, distinct campaigns placed in front of the team. Everything else is AI-run: the ~6-idea divergence, the narrowing/combination, the channel selection, the full plan, the pilot design, the budget, and the hero visual.

> Fewer decisions, same judgment: instead of asking the team to pick raw ideas and *then* pick a plan, the AI does the work and the team makes the one call that matters — **which campaign to run**.

## Living plan — build it progressively

`campaign-plan.html` is **not** a one-shot final artifact. Like the insight brief, it is a **living document**:

- **Create it as soon as the first output lands** — once the anchor + the first concept draft exist, create/seed `campaign-plan.html`.
- **Rewrite it after every step** — divergence → A/B build → embedded hero visual → decision. Each rewrite refreshes the page **and** its embedded `id="capture"` block.
- **The final page lists BOTH plans (A and B) in full**, with the **chosen one highlighted** (`chosen`); the other is dimmed (`parked`).

## When to use

- After `insight` (reads the `insight-brief.html` capture: `selected_segments` + `focus_bundles` + `key_insights` + `segments` + `moment_of_truth`).
- When the team wants only the poster — use the `poster` skill directly.

## Inputs

- The `insight-brief.html` capture — the team's chosen segments (`selected_segments`) + the derived focus bundle(s) (segment × moment) + `selected_insights`. Note the channel raw material it carries: each segment's **`channels`** field and each insight's **trend** (the market read's channel facts).
- Quest card — the **How Might We** if present, War Chest budget (MVP unlock + full), Victory Conditions.
- **Resume (recover upstream).** If run on its own (`/plan`), determine the quest id and find the latest round `artifacts/Quest<ID>-*`; if it's unambiguous, state it and continue — ask only when genuinely ambiguous. Read `insight-brief.html`'s `id="capture"` from that folder. If it's missing, say so and ask the team to run `/insight` first.

## Flow (uses the `facilitation` engine)

> **Choice-first**: the single decision opens with an **AI-drafted menu** (the two complete campaigns); the team picks 1 (and may `+1 of their own`).

1. **Diverge (AI).** Run the **`creative-concept`** sub-skill: anchor (the chosen focus bundle's audience × moment) + reframe into **one HMW**, then run creative-thinking methods (SCAMPER · analogies · reverse · mash-ups · Crazy 8 · brainwriting) to generate **~6 candidate ideas** (name · one-line · insight · mechanic).
2. **Converge + build A/B (AI).** Narrow the ~6 into **2 complete, distinct campaign concepts** (A / B — e.g. A = bold/experiential vs B = creator-led/community; or different audience/moment angles). Build each fully, threading the **campaign kernel** (`audience · moment · trend · channel · concept`): **positioning** (Moore, `references/marketing-plan.md`), the **channel mix** (`references/channel-strategy.md` — grounded in the segment's `channels` + the insight's trend), **offering** (a structured `offer`: a one-line `summary` + exactly **3** `cards` — offer / markets / access, or the membership **tiers**), **4Ps**, **2 pilot markets** (card-consistent, `references/pilot-experiment.md`), the **pilot experiment** (hypothesis / treatment / control / measurement), and the **budget** (`references/budget-model.md`, from the card's War Chest). Each plan also carries its own **`visual_direction`** + **`one_liner`**.
3. **Render (AI).** Design a hero visual for each concept and **embed it inside `campaign-plan.html`** — do **not** write standalone poster files here; those are produced only by the `/poster` stage.
4. **DECIDE (team) — the single decision.** Present the **two complete campaigns (A / B)** inline (each: concept · positioning · mix · 2 markets · budget headline · visual) → the team **picks ONE** (or `+1 own`). **That pick is the plan.**

## HITL checkpoint (mandatory)

- Exactly **one**: the team **picks the campaign (A or B)**.
The AI drafts both campaigns fully but **never chooses** for the team. Keep the `+1 of our own` channel open.

## Output

- `campaign-plan.html` — **both concepts are listed in full** (chosen one highlighted), DOC_TYPE "Campaign Plan" / "Membership Design". **The only artifact of this stage** — no separate data file and **no poster files** (the hero visual is embedded inline; the standalone poster is created by the `/poster` skill).
- The structured capture is embedded: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `prove` and `showcase` stages read it.

### capture block (embedded in `campaign-plan.html`)

```html
<script type="application/json" id="capture">
{
  "gate": "plan",
  "quest": "A",
  "selected_segments": [3, 1],
  "selected_insights": [1, 4],
  "anchor": {"segment": "…", "job": "…", "trend": "…", "moment": "…", "channel": "…", "mechanic": "…", "desire": "…"},
  "hmw": "How might we …",
  "ideas": [{"id": 1, "name": "…", "one_line": "…", "insight": "…", "mechanic": "…"}],
  "ai_shortlist": [2, 5],
  "combination": "mechanic of 2 + audience of 5",
  "plans": {
    "A": {"name": "…", "slogan": "…", "proposition": "…",
          "offer": {"summary": "one-line offer",
                    "cards": [{"title": "…", "detail": "…"}, {"title": "…", "detail": "…"}, {"title": "…", "detail": "…"}]},
          "positioning": "…",
          "channel_mix": {"primary": "…", "support": ["…", "…"], "why": "…", "moment": "…"},
          "mix": {"product": "…", "price": "…", "place": "…", "promotion": "…"},
          "pilot": {"markets": ["…", "…"], "hypothesis": "…", "treatment": "…", "control": "…", "measurement_setup": "…"},
          "budget": {"total": "…", "allocation": [{"market": "…", "channel": "…", "tactic": "…", "amount": "…"}]},
          "visual_direction": "…", "one_liner": "…"},
    "B": {"name": "…", "slogan": "…", "proposition": "…",
          "offer": {"summary": "one-line offer",
                    "cards": [{"title": "…", "detail": "…"}, {"title": "…", "detail": "…"}, {"title": "…", "detail": "…"}]},
          "positioning": "…",
          "channel_mix": {"primary": "…", "support": ["…", "…"], "why": "…", "moment": "…"},
          "mix": {"product": "…", "price": "…", "place": "…", "promotion": "…"},
          "pilot": {"markets": ["…", "…"], "hypothesis": "…", "treatment": "…", "control": "…", "measurement_setup": "…"},
          "budget": {"total": "…", "allocation": []},
          "visual_direction": "…", "one_liner": "…"}
  },
  "chosen_plan": "A",
  "poster_style": "a"
}
</script>
```

> **Keys**: `chosen_plan` = the team's pick (A | B). `offer.cards` = exactly **3** cards (offer / markets / access — or the membership **tiers**). `visual_direction` + `one_liner` live **inside each plan** (the plan derives one per plan); `poster_style` (a | b | c) is written later by the `/poster` stage (default `a`).

## Assemble (AI fills the framework; the team overrides fast)

- **Positioning** — Geoffrey Moore (see `references/marketing-plan.md`).
- **Channel mix** — primary + supporting channels + why, grounded in the insight (see `references/channel-strategy.md`).
- **Offering** — the structured `offer`: a one-line `summary` + exactly **3** `cards` (offer / markets / access — or the membership **tiers**).
- **4Ps** (see `references/marketing-plan.md`) · **Pilot experiment** — hypothesis / treatment / control / measurement (see `references/pilot-experiment.md`) · **Budget** — from the card's War Chest (see `references/budget-model.md`).

## Sub-skills & methods

- **Invoke the sub-skill**: `creative-concept` (anchor + HMW + creative methods → ~6 ideas) · `ascentium-brand` (the embedded hero visual).
- **Plan methods (references, not sub-skills)**: `marketing-plan.md` (positioning + 4Ps) · `channel-strategy.md` (channel mix) · `pilot-experiment.md` · `budget-model.md`.
