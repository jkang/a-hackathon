---
name: prove
description: Run the PROVE gate of the Ascentium mini-hackathon quest — turn the plan into a falsifiable proof package: 3–5 self-defined campaign sub-metrics (defended with Scout Report benchmarks), a KPI dashboard mock, Go/No-Go criteria, and a cost-benefit / ROI verdict on unlocking the full budget. Human-decided metrics and thresholds; AI builds the board and the math. Triggers: "prove gate", "campaign sub-metrics", "go no-go", "KPI dashboard", "cost-benefit", "measurement", "prove".
---

# Quest Prove — the PROVE gate

Prove the pilot predicts the Victory Conditions. The **team picks the metrics and thresholds**; the AI builds the dashboard and runs the cost-benefit math.

## When to use

- After `plan` (needs `plan.yaml`).
- When the team only wants the metrics/dashboard refreshed after a plan change.

## Inputs

- `plan.yaml` — the **chosen variant** (`chosen_variant`), esp. its `budget` and `pilot` (markets · hypothesis · treatment · control · measurement_setup).
- Quest card **Victory Conditions** and **War Chest / MVP Unlock**.

## Flow (uses the `facilitation` engine)

> **Choice-first**: the AI **drafts the menu** (candidate metrics + suggested threshold ranges); the team **selects** and may add `+1 own`.

1. **Draft (AI, 2′).** Map Victory Conditions → a marketing funnel, then present a **menu of ~8 candidate sub-metrics** (reach → engagement → conversion → outcome) with a **suggested Go/No-Go range** for each.
2. **Choose (team, 4′).** The team **picks 3–5** from the menu (or +1 own) and confirms/sets the **Go/No-Go thresholds**. Each metric must cite a **benchmark from the Scout Report**.
3. **Sample numbers (team, 2′).** AI proposes plausible weekly values; the team confirms or edits, so the dashboard feels real.
4. **Cost-benefit (AI).** Using the budget + metrics, compute the ROI (see `references/cost-benefit.md` derivation) and the unlock verdict.
5. **Capture** — write `metrics.yaml` (record the menu + the team's selection).

## HITL gates (mandatory)

- The AI presents the menu; the team **selects** the 3–5 sub-metrics.
- The team confirms the Go/No-Go thresholds (AI may suggest ranges, never fix them alone).
The AI must not pick them. Always keep the `+1 of our own` channel open.

## Output

- `proof.html` — **one proof page** that binds the whole gate, in this order:
  1. Victory Conditions
  2. Sub-Metrics &amp; thresholds (definition table, benchmark-defended)
  3. Go/No-Go rule
  4. **KPI Dashboard (MOCK)** — the board as it will look in-flight (tiles + progress vs Go + weekly trajectory + read)
  5. Cost-Benefit &amp; verdict
- `metrics.yaml` — structured capture.

> The KPI dashboard is **not** a separate artifact anymore — it is a `MOCK` section inside `proof.html` (the definition table shows the rules; the dashboard shows the same metrics running with sample data; the cost-benefit lands the verdict last).

### metrics.yaml schema

```yaml
quest: A | B
victory_conditions:
  - "{one full-scale target from the card}"       # from the card
metrics:
  - name: "Pilot conversion rate"
    formula: "{outcome} / {qualified reach}"
    benchmark_ref: "{a Scout Report benchmark}"    # Scout Report anchor
    target: "3.0%"
    threshold_go: ">=2.5%"
    threshold_no_go: "<1.5%"
sample_data: {week1: "...", week2: "..."}
cost_benefit:
  budget: 1500000
  projected_return: "..."     # from metrics + card economics
  roi: "..."
  unlock_verdict: "go | iterate | stop"
```

## Assemble

- **proof.html** — a single page in this order: victory conditions → the 3–5 metrics table (with benchmark refs and thresholds) → Go/No-Go rule → the **mock KPI dashboard** (tiles + progress bars vs Go + weekly trajectory, labelled `MOCK`) → the cost-benefit verdict. The dashboard section is built with `data-visualizer-pro` (manual-entry path — the team types numbers; no CSV needed).
- Use `ascentium-brand`.

## Methodology anchors

- **North Star alignment**: every sub-metric must trace to a Victory Condition.
- **Marketing funnel**: reach → engagement → conversion → outcome.
- **Go/No-Go gate**: define the rule before the data (hit → unlock; miss → iterate once or stop).
- See `references/metrics-method.md` and `references/cost-benefit.md`.

## Design notes

- **Invoke these sub-skills**: `campaign-metrics` (sub-metrics + Go/No-Go), `data-visualizer-pro` (KPI dashboard). (Cost-benefit / ROI uses `references/cost-benefit.md`.)
- Sub-metrics have "no fixed numbers" — but must be **defended with benchmarks** and shown to **predict** the Victory Conditions.
