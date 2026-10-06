---
name: plan
description: Run the PLAN/CREATIVE gate of the Ascentium mini-hackathon quest. The AI diverges to ~6 campaign ideas, narrows them into 2 complete, distinct campaign concepts (A/B), and builds each fully (positioning, offering, 4Ps, pilot, budget, hero visual). The team makes ONE decision — pick the campaign (A or B) at the end of the stage. Triggers: "creative concept", "brainstorm", "big idea", "pilot design", "campaign plan", "membership design", "marketing plan", "budget allocation".
---

# Plan — the PLAN/CREATIVE gate

The creative heart. Flow: **diverge → converge + build A/B (AI) → the team picks ONE**. The **team chooses the campaign**; the AI runs the divergence, the selection, and the full assembly.

## One decision only

The gate ends in **exactly one team decision**: **pick the campaign (A or B)** — two complete, distinct campaigns placed in front of the team. Everything else is AI-run: the ~6-idea divergence, the narrowing/combination, the opportunity definition, the full plan, the pilot design, the budget, and the hero visual.

> Fewer decisions, same judgment: instead of asking the team to pick raw ideas and *then* pick a plan, the AI does the work and the team makes the one call that matters — **which campaign to run**.

## Living plan — build it progressively

`campaign-plan.html` is **not** a one-shot final artifact. Like the insight brief, it is a **living document**:

- **Create it as soon as the first output lands** — once the anchor + the first concept draft exist, create/seed `campaign-plan.html`.
- **Rewrite it after every step** — divergence → A/B build → poster → decision. Each rewrite refreshes the page **and** its embedded `id="capture"` block.
- **The final page lists BOTH campaigns (A and B) in full**, with the **chosen one highlighted** (`SELECTED`); the other is dimmed (`is-parked`).

## When to use

- After `insight` (reads the `insight-brief.html` capture: `focus_bundles` + `key_insights` + `segments` + `moment_of_truth`).
- When the team wants only the poster — use the `poster` skill directly.

## Inputs

- The `insight-brief.html` capture — the chosen focus bundle(s) (segment × moment) + `selected_insights`.
- Quest card — the **How Might We** if present, War Chest budget (MVP unlock + full), Victory Conditions.

## Flow (uses the `facilitation` engine)

> **Choice-first**: the single decision opens with an **AI-drafted menu** (the two complete campaigns); the team picks 1 (and may `+1 of their own`).

1. **Diverge (AI).** Run the **`creative-concept`** sub-skill: anchor (the chosen focus bundle's audience × moment) + reframe into **one HMW**, then run creative-thinking methods (SCAMPER · analogies · reverse · mash-ups · Crazy 8 · brainwriting) to generate **~6 candidate ideas** (name · one-line · insight · mechanic).
2. **Converge + build A/B (AI).** Narrow the ~6 into **2 complete, distinct campaign concepts** (A / B — e.g. A = bold/experiential vs B = creator-led/community; or different audience/moment angles). Build each fully with **`opportunity-definition`** (5 elements) + the plan references: **positioning** (Moore, `references/marketing-plan.md`), **offering** (campaign concept *or* membership design + founding offer), **4Ps**, **2 pilot markets** (card-consistent, `references/pilot-experiment.md`), the **pilot experiment** (hypothesis / treatment / control / measurement), and the **budget** (`references/budget-model.md`, from the card's War Chest). Each concept also carries `{name, slogan, proposition, offer, mechanic}`.
3. **Render (AI).** Design a hero visual for each concept via the **`poster`** sub-skill (a default direction; the separate `/poster` stage can restyle and pick a final style).
4. **DECIDE (team) — the single decision.** Present the **two complete campaigns (A / B)** inline (each: concept · positioning · mix · 2 markets · budget headline · visual) → the team **picks ONE** (or `+1 own`). **That pick is the plan.**

## HITL gate (mandatory)

- Exactly **one**: the team **picks the campaign (A or B)**.
The AI drafts both campaigns fully but **never chooses** for the team. Keep the `+1 of our own` channel open.

## Output

- `campaign-plan.html` — **both concepts are listed in full** (chosen one highlighted), DOC_TYPE "Campaign Plan" / "Membership Design". **The only data artifact** — no separate file. Poster files (`poster-a|b|c.html` + `poster.html`) are rendered by the `poster` skill.
- The structured capture is embedded: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `prove` and `showcase` gates read it.

### capture block (embedded in `campaign-plan.html`)

```html
<script type="application/json" id="capture">
{
  "gate": "plan",
  "quest": "A",
  "selected_insights": [1, 4],
  "anchor": {"segment": "…", "job": "…", "moment": "…", "mechanic": "…", "desire": "…"},
  "hmw": "How might we …",
  "ideas": [{"id": 1, "name": "…", "one_line": "…", "insight": "…", "mechanic": "…"}],
  "ai_shortlist": [2, 5],
  "combination": "mechanic of 2 + audience of 5",
  "variants": {
    "A": {"name": "…", "slogan": "…", "proposition": "…", "offer": "…",
          "positioning": "…", "mix": {"product": "…", "price": "…", "place": "…", "promotion": "…"},
          "pilot": {"markets": ["…", "…"], "hypothesis": "…", "treatment": "…", "control": "…", "measurement_setup": "…"},
          "budget": {"total": "…", "allocation": [{"market": "…", "channel": "…", "tactic": "…", "amount": "…"}]}},
    "B": {"name": "…", "slogan": "…", "proposition": "…", "offer": "…",
          "positioning": "…", "mix": {"product": "…", "price": "…", "place": "…", "promotion": "…"},
          "pilot": {"markets": ["…", "…"], "hypothesis": "…", "treatment": "…", "control": "…", "measurement_setup": "…"},
          "budget": {"total": "…", "allocation": []}}
  },
  "chosen_variant": "A",
  "poster": {"visual_direction": "…", "one_liner": "…"}
}
</script>
```

## Assemble (AI fills the framework; the team overrides fast)

- **Positioning** — Geoffrey Moore (see `references/marketing-plan.md`).
- **Offering** — A/B: campaign concept, or membership design + founding offer.
- **4Ps** (see `references/marketing-plan.md`) · **Pilot experiment** — hypothesis / treatment / control / measurement (see `references/pilot-experiment.md`) · **Budget** — from the card's War Chest (see `references/budget-model.md`).

## Sub-skills to invoke (do not hand-roll)

`creative-concept` (anchor + HMW + creative methods → ~6 ideas) · `opportunity-definition` (5 elements) · `poster` (hero visual).
