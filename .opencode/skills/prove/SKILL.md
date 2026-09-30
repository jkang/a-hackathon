---
name: prove
description: Run the PROVE gate of the Ascentium mini-hackathon quest — turn the plan into a one-screen PILOT METRICS board: the 3–5 metrics the pilot expects to hit (across the marketing funnel), each with the derivation logic behind its number (benchmark → assumption → formula → target). No Go/No-Go, no cost-benefit, no scale-up. Human-decided metrics; AI builds the board and writes the math. Triggers: "prove gate", "pilot metrics", "expected metrics", "metric derivation", "measurement", "prove".
---

# Quest Prove — the PROVE gate (pilot metrics)

Show **what the pilot must hit, and how each number is derived**. The **team picks the metrics**; the AI writes the derivation chain and builds a single one-screen board.

## When to use

- After `plan` (reads the `campaign-plan.html` capture).
- When the team only wants the pilot-metrics board refreshed after a plan change.

## Inputs

- The `campaign-plan.html` capture — the **chosen variant** (`chosen_variant`), esp. its `pilot` (markets · hypothesis · treatment · control · measurement_setup) and `budget`.
- Quest card **pilot window / pilot markets / MVP budget** and **Scout Report benchmarks** (the anchors for every derivation).

## Flow (uses the `facilitation` engine)

> **Choice-first**: the AI **drafts the menu** (candidate pilot metrics + a suggested target each); the team **selects** and may add `+1 own`.

1. **Frame (AI, 1′).** Read the pilot (2 markets · 3 months · MVP budget) and the card benchmarks.
2. **Menu (AI, 2′).** Map the pilot's funnel (reach → engagement → conversion → outcome) and present a **menu of ~6–8 candidate pilot metrics**, each with a **suggested target** and a one-line derivation sketch.
3. **Choose (team, 3′).** The team **picks 3–5** (or `+1 own`). There are no thresholds to set.
4. **Derive (AI, 2′).** For each pick, write the **derivation chain**: `benchmark → assumption(s) → formula → target`, plus a one-line logic ("why hitting this predicts the outcome").
5. **Capture** — record the metrics in the artifact's embedded `id="capture"` block (see Output). No separate data file.

## HITL gates (mandatory)

- The AI presents the menu; the team **selects** the 3–5 pilot metrics.
- The team may edit any target; the AI never fixes a number alone.
Always keep the `+1 of our own` channel open.

## Output

- `proof.html` — **one screen** (single viewport), in this order:
  1. pilot framing (client · markets · window · MVP budget)
  2. **pilot funnel** strip (reach → engagement → conversion → outcome) with each target placed on it
  3. **metric tiles** — metric name + target value + funnel tag
  4. **derivation logic** — one row per metric: `target ◀ benchmark · assumption(s) · formula`
  **The only artifact** — no separate data file.
- The structured capture is embedded in that artifact: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `showcase` gate reads it.

### capture block (embedded in `proof.html`)

```html
<script type="application/json" id="capture">
{
  "gate": "prove",
  "quest": "A",
  "pilot": {"window": "3 months", "markets": ["…", "…"], "budget": "{mvp_unlock}"},
  "metrics": [
    {"name": "…", "dimension": "reach | engagement | conversion | outcome", "target": "…",
     "derivation": {"benchmark_ref": "…", "formula": "…", "assumptions": ["…"], "logic": "…"}}
  ]
}
</script>
```

## Assemble

- **proof.html** — a one-screen page built directly from `templates/proof.html`: pilot framing → funnel with targets → metric tiles → derivation rows. Keep it to a single viewport (no scrolling at desktop width).
- Use `ascentium-brand`.

## Methodology anchors

- **Pilot-first**: the numbers are the pilot's expected values over the 3-month window — not full-scale projections.
- **Funnel**: reach → engagement → conversion → outcome.
- **Benchmark-anchored**: every target cites a Scout Report benchmark and shows its derivation chain.
- See `references/metrics-method.md`.

## Design notes

- **No sub-skills.** Build the page directly from `templates/proof.html` (the retained `sub-skills/` are not invoked here).
- **No Go/No-Go, no cost-benefit, no scale-up** — out of scope for this gate.
- Every target must be **defensible**: a visible chain (benchmark → assumption → formula), never a bare assertion.
