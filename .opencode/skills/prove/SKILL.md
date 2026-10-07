---
name: prove
description: Run the PROVE stage of the Ascentium mini-hackathon quest — produce ONE most-reasonable numeric pilot forecast directly from the insight + plan, covering the funnel (reach → engagement → conversion → outcome) with the derivation logic behind every number (benchmark → assumption → formula → target). AI-only, no team decision. No Go/No-Go, no cost-benefit, no scale-up. Triggers: "prove stage", "pilot forecast", "pilot metrics", "expected metrics", "metric derivation", "measurement", "prove".
---

# Quest Prove — the PROVE stage (pilot forecast)

Show **what the pilot must hit, and how each number is derived** — as **one most-reasonable forecast**. The **AI produces it directly** from the insight + plan; there is **no team decision** in this stage.

## No team decision

This stage has **no user decision**. The AI reads the chosen insights + the chosen campaign, picks the metric set, sets the most reasonable target for each, and writes the derivation chains. The team reviews the finished board; the AI does **not** stop for a pick.

> Judgment still applies — it is just made by the AI and shown transparently (benchmark → assumption → formula), so the team can challenge any number.

## When to use

- After `plan` (reads the `campaign-plan.html` capture).
- When the team wants the pilot-forecast board refreshed after a plan change.

## Inputs

- The `insight-brief.html` capture — the chosen key insights (`selected_insights`) and the benchmark data.
- The `campaign-plan.html` capture — the **chosen variant** (`chosen_variant`), esp. its `pilot` (markets · hypothesis · treatment · control · measurement_setup) and `budget`.
- Quest card **pilot window / pilot markets / MVP budget** and **Scout Report benchmarks** (the anchors for every derivation).
- **Resume (recover upstream).** If run on its own (`/prove`), find the latest round `artifacts/Quest<ID>-*` and read both captures from that folder; if the round is unambiguous, state it and continue — ask only when genuinely ambiguous. If either is missing, say so and ask the team to run `/plan` (or `/insight`) first.

## Flow

1. **Frame (AI).** Read the pilot (2 markets · 3 months · MVP budget), the chosen campaign's hypothesis, and the card benchmarks.
2. **Choose the metric set (AI).** Map the funnel (reach → engagement → conversion → outcome) and pick the **3–5 metrics that best prove this pilot's hypothesis**. No menu.
3. **Set the most reasonable target (AI).** For each metric, pick a **conservative-but-defensible** target, anchored to a Scout Report benchmark. Prefer a benchmark-anchored number over an optimistic one.
4. **Derive (AI).** Write each metric's **derivation chain**: `benchmark → assumption(s) → formula → target`, plus a one-line logic ("why hitting this predicts the outcome").
5. **Build + capture (AI).** `proof.html` — one screen; decisions recorded in the artifact's embedded `id="capture"` block (see Output). No separate data file.

## Output

- `proof.html` — **one screen** (single viewport), in this order:
  1. pilot framing (client · markets · window · MVP budget)
  2. **pilot funnel** strip (reach → engagement → conversion → outcome) with each target placed on it
  3. **metric tiles** — metric name + target value + funnel tag
  4. **derivation logic** — one row per metric: `target ◀ benchmark · assumption(s) · formula`
  **The only artifact** — no separate data file.
- The structured capture is embedded in that artifact: an invisible `<script type="application/json" id="capture">` block just before `</body>`. The `showcase` stage reads it.

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
  ],
  "source_note": "Scout Report + live research · Data as of …"
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
- **No Go/No-Go, no cost-benefit, no scale-up** — out of scope for this stage.
- Every target must be **defensible**: a visible chain (benchmark → assumption → formula), never a bare assertion.
