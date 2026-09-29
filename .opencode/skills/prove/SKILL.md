---
name: prove
description: Run the PROVE gate of the Ascentium mini-hackathon quest — turn the plan into a falsifiable proof package: 3–5 self-defined MVP sub-metrics (defended with Scout Report benchmarks), a KPI dashboard mock, Go/No-Go criteria, and a cost-benefit / ROI verdict on unlocking the full budget. Human-decided metrics and thresholds; AI builds the board and the math. Triggers: "prove gate", "MVP sub-metrics", "go no-go", "KPI dashboard", "cost-benefit", "measurement", "quest prove".
---

# Quest Prove — the PROVE gate

Prove the pilot predicts the Victory Conditions. The **team picks the metrics and thresholds**; the AI builds the dashboard and runs the cost-benefit math.

## When to use

- After `plan` (needs `plan.yaml`).
- When the team only wants the metrics/dashboard refreshed after a plan change.

## Inputs

- `plan.yaml` (esp. `budget`, `pilot`, `experiment`).
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

- `proof.html` — metrics + Go/No-Go + cost-benefit summary.
- `kpi-dashboard.html` — the KPI dashboard **mock** (deliverable #4; Quest A explicit, Quest B implied).
- `metrics.yaml` — structured capture.

### metrics.yaml schema

```yaml
quest: A | B
victory_conditions:
  - "400K tickets sold to SEA fans"          # from the card
metrics:
  - name: "Pilot ticket conversion rate"
    formula: "tickets / qualified site visits"
    benchmark_ref: "Hangzhou 92% attendance"  # Scout Report anchor
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

- **proof.html** — victory conditions, the 3–5 metrics table (with benchmark refs and thresholds), a simple Go/No-Go rule, and the cost-benefit verdict.
- **kpi-dashboard.html** — a mock board with KPI tiles + one trend line, built with `data-visualizer-pro` (manual-entry path — the team types numbers; no CSV needed).
- Use `ascentium-brand`.

## Methodology anchors

- **North Star alignment**: every sub-metric must trace to a Victory Condition.
- **Marketing funnel**: reach → engagement → conversion → outcome.
- **Go/No-Go gate**: define the rule before the data (hit → unlock; miss → iterate once or stop).
- See `references/metrics-method.md` and `references/cost-benefit.md`.

## Design notes

- Sub-skills: `mvp-metrics-generator`, `data-visualizer-pro`, `creating-financial-models`.
- Sub-metrics have "no fixed numbers" — but must be **defended with benchmarks** and shown to **predict** the Victory Conditions.
