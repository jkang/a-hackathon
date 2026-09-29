---
name: plan
description: Run the PLAN/CREATIVE gate of the Ascentium mini-hackathon quest — diverge to ~6 campaign ideas (How Might We + creative-thinking methods), the team picks 2–3 (or combines several), then the AI scopes the opportunity and builds a full campaign plan (positioning, offering, 4Ps, pilot, budget), produces ≥2 A/B plan versions, and the team picks A or B to design the poster. Triggers: "creative concept", "brainstorm", "big idea", "pilot design", "campaign plan", "membership design", "marketing plan", "budget allocation".
---

# Plan — the PLAN/CREATIVE gate

The creative heart. Flow: **diverge → pick → define + plan → A/B → poster**. The **team creates and chooses**; the AI scaffolds and formats.

## When to use

- After `insight` (needs `insight.yaml`: key insights + selected insights + audience/moment).
- When the team wants only the brainstorm, or only the poster — call the relevant sub-skill directly.

## Inputs

- `insight.yaml` — especially `key_insights` + `selected_insights` (the 2–3 chosen).
- Quest card — the **How Might We**, War Chest budget (A: 1.5M / B: 1.1M), Victory Conditions, scale-up gate.

## Flow (uses the `facilitation` engine)

> **Choice-first**: every team step opens with an **AI-drafted menu**; the team **selects** (and may `+1 of their own`).

1. **Diverge (AI + team).** Run the **`creative-concept`** sub-skill: anchor (audience × moment) + reframe into **one HMW**, then run creative-thinking methods (SCAMPER · analogies · reverse · mash-ups · Crazy 8 · brainwriting) to generate **~6 candidate ideas** (each = name · one-line · insight it answers · mechanic).
2. **Pick (team).** The team **selects 2–3** of the ~6 — and may **combine several into a hybrid** ("the mechanic of 2 with the audience of 4").
3. **Define + plan (AI + team).** Run **`opportunity-definition`** (5 elements) on the chosen idea(s), then build the **campaign plan**: anchor (segment × job × moment), positioning (see `references/marketing-plan.md`), offering, 4Ps, 2 pilot markets (see `references/pilot-experiment.md`), and budget (see `references/budget-model.md`).
4. **A/B versions (AI → team).** Produce **≥2 distinct plan versions** (e.g. A = bold/experiential vs B = creator-led/community; or different audiences/angles), each with its own positioning + mix + pilot + budget. The team **picks A or B** (or mixes).
5. **Poster (poster skill).** For the chosen plan, design the hero visual via the **`poster`** sub-skill (team picks the visual direction + one-liner).

## HITL gates (mandatory)

- The team **selects 2–3 ideas** (and / or combines several).
- The team **picks A or B** from the plan versions.
- The team picks the 2 pilot markets, the budget split, and the poster visual direction.
The AI drafts the menus/versions but **never decides** for the team.

## Output

- `campaign-plan.html` — the chosen plan (DOC_TYPE: "Campaign Plan" / "Membership Design").
- `plan.yaml` — structured capture (ideas, selection, opportunity, the A/B variants + the chosen one, pilot, budget, poster direction).

### plan.yaml schema

```yaml
quest: A | B
selected_insights: [1, 4]                     # from insight.yaml
anchor:                                       # from creative-concept (the brief)
  {segment: "...", job: "...", moment: "...", mechanic: "...", desire: "..."}
scenario:                                     # 3–5 campaign moments (time · place · event)
  - {moment: "...", time: "...", place: "...", event: "..."}
hmw: "How might we ..."
ideas:                                        # ~6 diverged (name, one-line, insight, mechanic)
  - {id: 1, name: "...", one_line: "...", insight: "...", mechanic: "..."}
selected_ideas: [2, 5]                        # 2–3 chosen (or a combination note)
combination: "mechanic of 2 + audience of 5"  # optional, if the team combined
concept:                                      # the chosen concept
  {name: "...", slogan: "...", proposition: "...", offer: "..."}
opportunity:                                  # from opportunity-definition (5 elements)
  e1: "one-line opportunity"
  e2: "segment & scenario"
  e3: "pain / tension"
  e4: "solution hypothesis + guardrail"
  e5: "value / return"
  value_breakdown: [scope, frequency, per_instance, cumulative]
variants:                                     # ≥2 A/B plan versions
  A: {positioning: "...", offering: "...", mix: "...", pilot: "...", budget: "..."}
  B: {positioning: "...", offering: "...", mix: "...", pilot: "...", budget: "..."}
chosen_variant: A
poster: {visual_direction: "...", one_liner: "..."}
```

## Assemble (AI fills the framework; the team overrides fast)

- **Positioning** — Geoffrey Moore (see `references/marketing-plan.md`).
- **Offering** — A: campaign concept; B: membership design + founding offer.
- **4Ps** (see `references/marketing-plan.md`) · **Pilot experiment** — hypothesis / treatment / control / measurement (see `references/pilot-experiment.md`) · **Budget** — the team's split (see `references/budget-model.md`).

## Sub-skills to invoke (do not hand-roll)

`creative-concept` (anchor + HMW + creative methods → ~6 ideas) · `opportunity-definition` (5 elements) · `poster` (hero visual).
