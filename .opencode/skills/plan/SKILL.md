---
name: plan
description: Run the PLAN/CREATIVE gate of the Ascentium mini-hackathon quest — diverge to ~6 campaign ideas (How Might We + creative-thinking methods), the team picks 2–3 (or combines several), then the AI scopes the opportunity and builds a full campaign plan (positioning, offering, 4Ps, pilot, budget), produces ≥2 A/B plan versions, and the team picks A or B to design the poster. Triggers: "creative concept", "brainstorm", "big idea", "pilot design", "campaign plan", "membership design", "marketing plan", "budget allocation".
---

# Plan — the PLAN/CREATIVE gate

The creative heart. Flow: **diverge → pick → define + plan → A/B → poster**. The **team creates and chooses**; the AI scaffolds and formats.

## When to use

- After `insight` (reads the `insight-brief.html` capture: key insights + selected insights + audience/moment).
- When the team wants only the brainstorm, or only the poster — call the relevant sub-skill directly.

## Inputs

- The `insight-brief.html` capture — especially `key_insights` + `selected_insights` (the 2–3 chosen).
- Quest card — the **How Might We**, War Chest budget (MVP unlock + full, from the card), Victory Conditions.

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

- `campaign-plan.html` — the chosen plan (DOC_TYPE: "Campaign Plan" / "Membership Design"). **The only data artifact** — no separate file.
- The structured capture is embedded in that artifact: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `prove` and `showcase` gates read it.

### capture block (embedded in `campaign-plan.html`)

```html
<script type="application/json" id="capture">
{
  "gate": "plan",
  "quest": "A",
  "selected_insights": [1, 4],
  "anchor": {"segment": "…", "job": "…", "moment": "…", "mechanic": "…", "desire": "…"},
  "scenario": [{"moment": "…", "time": "…", "place": "…", "event": "…"}],
  "hmw": "How might we …",
  "ideas": [{"id": 1, "name": "…", "one_line": "…", "insight": "…", "mechanic": "…"}],
  "selected_ideas": [2, 5],
  "combination": "mechanic of 2 + audience of 5",
  "concept": {"name": "…", "slogan": "…", "proposition": "…", "offer": "…"},
  "opportunity": {"e1": "…", "e2": "…", "e3": "…", "e4": "…", "e5": "…"},
  "variants": {
    "A": {"positioning": "…", "offering": "…", "mix": {"product": "…", "price": "…", "place": "…", "promotion": "…"},
          "pilot": {"markets": ["…", "…"], "hypothesis": "…", "treatment": "…", "control": "…", "measurement_setup": "…"},
          "budget": {"total": "…", "allocation": [{"market": "…", "channel": "…", "tactic": "…", "amount": "…"}]}},
    "B": {"positioning": "…", "offering": "…", "mix": {"product": "…", "price": "…", "place": "…", "promotion": "…"},
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
- **Offering** — A: campaign concept; B: membership design + founding offer.
- **4Ps** (see `references/marketing-plan.md`) · **Pilot experiment** — hypothesis / treatment / control / measurement (see `references/pilot-experiment.md`) · **Budget** — the team's split (see `references/budget-model.md`).

## Sub-skills to invoke (do not hand-roll)

`creative-concept` (anchor + HMW + creative methods → ~6 ideas) · `opportunity-definition` (5 elements) · `poster` (hero visual).
