---
name: plan
description: Run the PLAN/CREATIVE gate of the Ascentium mini-hackathon quest — anchor the idea to an audience and a moment (scenario canvas), the team diverges on a big idea, dot-votes a winner, then the AI assembles it into a full pilot plan (positioning, offering, marketing mix, 3-month 2-market pilot, experiment + measurement setup, and budget allocation). Covers Quest A campaign concept and Quest B membership design + founding-member offer. Triggers: "creative concept", "big idea", "scenario canvas", "moment of truth", "pilot design", "campaign plan", "membership design", "marketing plan", "budget allocation", "quest plan".
---

# Quest Plan — the PLAN/CREATIVE gate

The heaviest gate. The **team creates the idea**; the AI **fills the framework**. Human-first: **anchor (audience + moment) → diverge → vote → deepen → decide**, then AI assembles the plan.

> A thin idea is an unanchored idea. Anchor the concept to a **specific audience** and a **specific moment** (time / place / event) before diverging — see `references/creative-concept.md`.

## When to use

- After `insight` (needs `insight.yaml`, which now carries segments + moment of truth).
- When the team wants only the creative step (call the `facilitation` protocols directly and stop).

## Inputs

- `insight.yaml` (seed insight, **audience segments, moment of truth**, trends).
- Quest card: War Chest budget (A: USD 1.5M / 5%; B: USD 1.1M / 10%), Victory Conditions, scale-up gate.

## Flow (uses the `facilitation` engine)

> **Choice-first**: every team step opens with an **AI-drafted menu of 6–8 grounded options** (`facilitation` → `option-menu.md`); the team **selects** and may add `+1 of our own`. The creative idea step gives the team **starters**, not a blank page.

1. **Anchor (team).** AI presents a **menu of ~4 candidate anchors** (segment × job × moment) → the team picks/remixes one, and fills the line *for [segment], whose [job], at [moment], we will [mechanic] — so they [desire]*.
2. **Scenario canvas (team).** AI presents a **menu of ~8 candidate moments** → the team picks 3–5 (time / place / event), then the 1–2 as the creative spine.
3. **HMW** — derive it from the anchor.
4. **Idea starters (team).** AI presents a **menu of ~8 idea starters** → the team picks 2–3 to build on, remixes, or adds `+1 own`. Then silent brainstorm 2′ → round-robin 6′ → affinity cluster.
5. **Converge** — dot-vote 2′ (2 votes each) → top 2–3.
6. **Deepen** — 1-2-4-All 5′ on the winner → *one-line proposition + name + slogan + the moment it owns*.
7. **Decide pilot** — AI presents a **menu of markets** → the team picks **2** + success criteria (3′).
8. **Allocate budget** — AI presents **allocation slices/scenarios** → the team adjusts and confirms the split. *The card states: "Budget allocation is part of the solution."*
9. **Capture** — write `plan.yaml` (record the menus + the team's selection).

## HITL gates (mandatory)

- The AI presents the menus; the team picks the creative brief anchor (segment + job + moment).
- The team chooses/remixes the winning idea (from the starters).
- The team picks the 2 pilot markets.
- The team allocates the budget.
The AI may propose the menus/starters but never decides these. Always keep the `+1 of our own` channel open.

## Output

- `campaign-plan.html` — Ascentium-branded one/two-pager (use `templates/campaign-plan.html`; set `{{DOC_TYPE}}` = "Campaign Plan" for Quest A, "Membership Design" for Quest B).
- `plan.yaml` — structured capture (includes the **experiment + measurement setup** required by deliverable #2).

### plan.yaml schema

```yaml
quest: A | B
seed_insight: "..."
audience: {primary_segment: "...", job_to_be_done: "..."}   # the anchor
scenario: [{moment: "...", time: "...", place: "...", event: "..."}]  # 3–5 campaign moments
creative_brief: "for [segment] whose [job] at [moment], we will [mechanic] — so they [desire]"
hmw: "How might we ..."
ideas: [{author: "...", concept: "..."}]      # RAW human divergence
votes: {idea_id: count}
winner: {concept: "...", proposition: "...", name: "...", slogan: "...", moment: "..."}
offering:                                      # A = campaign concept; B = membership design
  type: campaign | membership
  tiers: ["{name, price, benefits}", "..."]    # B only
  founding_offer: "..."                        # B only — deliverable #3
pilot:
  markets: ["...", "..."]                       # exactly 2
  duration: "3 months"
  success_criteria: "..."
experiment:
  hypothesis: "If ... then ..."
  treatment: "..."
  control: "..."
  measurement_setup: "what is instrumented, where, and how often"
budget:
  total: 1.5M | 1.1M
  allocation: [{market: "...", channel: "...", tactic: "...", amount: "..."}]
```

## Assemble (AI fills the framework; the team can override fast)

- **Creative brief + scenario** — the anchor and the campaign moments (see `references/creative-concept.md`).
- **Positioning** — Geoffrey Moore statement (see `references/marketing-plan.md`).
- **Offering** — A: campaign concept (name, slogan, hero idea); B: membership design (tiers/pricing/benefits) + founding-member offer.
- **Marketing mix (4Ps)** — product/offering, price, place/channels, promotion/content rhythm.
- **Pilot experiment** — PoL-style marketing pilot: hypothesis, treatment vs control, 2 markets × 3 months, measurement setup (see `references/pilot-experiment.md`).
- **Budget allocation** — the team's split of the 1.5M / 1.1M (see `references/budget-model.md`).
- (Cost-benefit / ROI **proof** is produced in `prove`, not here.)

## Research restraint

Use card data + team knowledge. `agent-reach` only if a specific fact is missing.

## Design notes

- Output shape differs by quest: **A = campaign concept**; **B = membership design + founding offer**.
- Sub-skills: `brainstorming`, `opportunity-definition`, `pol-probe-advisor`, `poster`. (Cost-benefit / `creating-financial-models` now lives under `prove`.)
