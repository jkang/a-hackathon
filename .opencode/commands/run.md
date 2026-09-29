---
description: Run the whole quest automatically end-to-end (autopilot — the AI makes every decision itself), and produce the complete deliverable set plus the unified proposal report.
agent: runner
---
Run the whole quest end-to-end **automatically** — no questions, no human input. At every decision node, decide yourself (per the `runner` agent).

**Quest: $ARGUMENTS** (if empty, default to A = Doha 2030 ticketing).

1. **Insight** — research via `agent-reach` → org + audience + trends + SWOT → ~6 key insights → pick 2–3.
2. **Plan** — `creative-concept` (anchor + HMW + methods → ~6 ideas) → pick 2–3/combine → opportunity + campaign plan → ≥2 A/B versions → pick A or B → `poster`.
3. **Prove** — `campaign-metrics` (pick 3–5 metrics + thresholds) → KPI dashboard → cost-benefit (ROI + verdict).
4. **Showcase** — pick a storyline → build `proposal.html` (unified report) + `pitch-deck.html` + `prompt-pack.html`.

Write all artifacts to an `auto-run/` folder, and log every decision + its reason in `RUN-LOG.md`. Grounded, no fabricated numbers; English; Ascentium-branded.
