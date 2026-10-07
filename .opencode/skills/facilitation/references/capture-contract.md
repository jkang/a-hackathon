# Capture Contract

How the robot facilitator records human input, and the rule that keeps it human-in-the-loop.

## The HITL gate (mandatory)

After every divergence and every convergence, the AI **must stop** and explicitly request the team's input. It must never:

- invent ideas on the team's behalf,
- pick the winner itself,
- silently proceed past a decision.

**Menu-first rule**: every HITL gate is opened with an **AI-drafted menu of 6–8 grounded options** (see `option-menu.md`), and the team **selects** (pick N) — not a blank question. Always offer `+1 of our own`.

Template:

> **hackathon-robot >>** Done: [what I just did]. Artifact: `artifacts/QuestA-01/[file].html`.
> **MENU · [gate]** — **pick [N]** (30s), or `+1` your own. `1)` … `2)` … `3)` … `4)` … `5)` … `6)`
> **Reply with your pick (e.g. `1, 3, 5`).**

> The example must match the actual menu — use its real option numbers and pick count (a 3-option single pick → *e.g. `1`*; a 6–8-option pick-2–3 → *e.g. `1, 3, 5`*). Never cite options that aren't there.

The recap + inline menu are the team's interface; the HTML is only the **record** — the team always chooses in the chat.

## Where the capture lives — inside the HTML

There are **no separate data files** (no `.yaml`, no `.md`). Each stage records its decisions in the **stage's HTML artifact**, as a single embedded JSON block placed just before `</body>`:

```html
<script type="application/json" id="capture">
{ "gate": "insight", "quest": "A", "decision": "…" }
</script>
```

- The block is **invisible** in the rendered page (browsers do not display `application/json` scripts).
- The next gate reads the upstream artifact's `id="capture"` block (grep `id="capture"`, parse the JSON) instead of a YAML file.
- Never write `.yaml` / `.md` sidecars — the HTML is the single source of truth.

## Input types

| Type            | Used for                         | Captured as            |
|-----------------|----------------------------------|------------------------|
| Menu selection  | any gate's choice                | `{chosen: [...], own: [...]}` |
| Idea list       | brainstorm output                | `[{author, text}]`     |
| Vote tally      | dot-vote result                  | `{idea_id: count}`     |
| Single choice   | winner / markets / direction     | one value              |
| Target          | expected pilot value             | `{metric: value}`      |
| One-liner       | proposition / slogan             | string                 |

## Capture block shape

```json
{
  "gate": "insight | plan | prove | showcase",
  "quest": "A",
  "menu": ["1) …", "2) …", "…"],
  "inputs": [{"type": "selection", "chosen": [1, 4, 6], "own": ["+1 custom"]}],
  "votes": {"idea_id": 3},
  "decision": "the team's explicit choice",
  "timestamp_min": 12,
  "reasons": ["chosen X because Y"]
}
```

## Rules

- **Menu first** — never open a gate with a blank question.
- **List the full menu in the artifact** — every candidate option is written into the HTML (not only the winner), each with a `selected` flag. Chosen items are highlighted; the rest are dimmed.
- Store the team's selection **verbatim**; never swap a menu item for the AI's own preference.
- Keep the `+1 of our own` channel open and record those additions too.
- If the team overrides an AI draft, record both: `ai_draft` and `team_override`.
- Attach every decision to a `timestamp_min` so the run can be replayed.
- Output goes into the stage HTML (`insight-brief.html`, `campaign-plan.html`, `proof.html`, `proposal.html`); never overwrite the `sources/` materials.
