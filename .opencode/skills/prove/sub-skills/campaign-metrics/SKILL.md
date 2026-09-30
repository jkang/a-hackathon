---
name: campaign-metrics
description: Design the campaign pilot's success-metric system and Go/No-Go gate — a small set of falsifiable sub-metrics across the funnel (reach → engagement → conversion → outcome, plus economics), each with a binary threshold, a rubric, and a one-line Go/No-Go statement. Triggers: "campaign metrics", "success metrics", "go/no-go", "gate", "sub-metrics".
---

# Campaign Metrics — pilot validation

> **Dormant.** Retained for reference only. The `prove` gate no longer calls this sub-skill — it outputs a single one-screen `proof.html` (pilot metrics + derivation logic) with decisions in its embedded `id="capture"` block. If revived, write **HTML only** — no YAML sidecars.

Design a compact, quantifiable validation system so a pilot can prove (or kill) the trajectory. From "can it work" to "is it proven".

## Output — three parts

1. **Sub-metrics** — across the funnel and economics:
   - dimensions: **Reach · Engagement · Conversion · Outcome** (+ **Cost/Economics**)
   - each: `name · dimension · logic · threshold · benchmark · source`
   - keep it to **3–5 metrics**; each must trace to a Victory Condition and cite a Scout Report benchmark.
2. **Rubric** — binary pass/fail per metric (`threshold` = ✓ / ✗). Any metric failing means Go is not met. No vague wording ("works well").
3. **Go/No-Go statement** — one punchy, decision-ready line, e.g. *"Go if ticket-intent ≥2.5% and CAC ≤$10 and no metric hits No-Go."*

## YAML spec

```yaml
title: "..."
product_name: "{campaign / pilot name}"
go_no_go_statement: "..."
target_metrics:
  - {name, dimension, logic, threshold, benchmark, source}
monitoring_plan:
  - {name, layer, logic, range, alert, meaning}
```

## Quick use

1. Provide the campaign / pilot description (offer, markets, funnel).
2. Generate the YAML per the spec.
3. Compile the HTML report (or render it directly with the Ascentium brand).

## Dev notes

- Visual style: premium decision dashboard.
- Render the report directly with the Ascentium brand (single-file HTML); no build step required.
