# Capture Contract

How the robot facilitator records human input, and the rule that keeps it human-in-the-loop.

## The HITL gate (mandatory)

After every divergence and every convergence, the AI **must stop** and explicitly request the team's input. It must never:

- invent ideas on the team's behalf,
- pick the winner itself,
- silently proceed past a decision.

**Menu-first rule**: every HITL gate is opened with an **AI-drafted menu of 6–8 grounded options** (see `option-menu.md`), and the team **selects** (pick N) — not a blank question. Always offer `+1 of our own`.

Template:

> **FACI-0X >>** MENU · [gate] — **pick [N]** (30s), or `+1` your own. `1)` … `2)` … `3)` … `4)` … `5)` … `6)`

## Input types

| Type            | Used for                         | Captured as            |
|-----------------|----------------------------------|------------------------|
| Menu selection  | any gate's choice                | `{chosen: [...], own: [...]}` |
| Idea list       | brainstorm output                | `[{author, text}]`     |
| Vote tally      | dot-vote result                  | `{idea_id: count}`     |
| Single choice   | winner / markets / direction     | one value              |
| Threshold       | Go/No-Go numbers                 | `{metric: value}`      |
| One-liner       | proposition / slogan             | string                 |

## Shared capture card (YAML)

Every gate writes into the stage's YAML file. Minimum shape:

```yaml
gate: insight | creative | proof | showcase
menu: ["1) ...", "2) ...", "..."]         # the AI-drafted options presented
inputs:
  - {type: selection, chosen: [1,4,6], own: ["+1 custom"]}   # team's pick, verbatim
votes: {idea_id: count}                     # if a vote happened
decision: "the team's explicit choice"
timestamp_min: 12                           # minute on the 40-min clock
```

## Rules

- **Menu first** — never open a gate with a blank question.
- Store the team's selection **verbatim**; never swap a menu item for the AI's own preference.
- Keep the `+1 of our own` channel open and record those additions too.
- If the team overrides an AI draft, record both: `ai_draft` and `team_override`.
- Attach every decision to a `timestamp_min` so the run can be replayed.
- Output goes to the stage YAML (e.g. `insight.yaml`, `plan.yaml`, `metrics.yaml`); never overwrite the `sources/` materials.
