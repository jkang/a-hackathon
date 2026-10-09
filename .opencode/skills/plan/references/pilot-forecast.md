# Pilot Forecast & Derivation Method

Folded into the **plan** stage: the plan carries a **pilot forecast** — the expected numbers the pilot must hit, and the derivation logic behind each one. The AI produces it as part of building the plan (**no separate team decision**).

## 1. What the plan produces

For the chosen campaign, a set of **3–5 pilot-forecast metrics** over the 3-month, 2-market window, each with its **derivation chain**. This is the "proof" the pitch rests on: a single, most-reasonable forecast on the funnel — not a full-scale projection.

Nothing else: no Go/No-Go, no cost-benefit, no scale-up.

## 2. Choose the metric set (3–5)

Pick the **3–5 metrics that best prove this pilot's hypothesis**. Each metric must:

1. Sit on the funnel: reach → engagement → conversion → outcome.
2. Be an **expected pilot value** over the 3-month window (not a full-scale target).
3. Cite a **Scout Report benchmark** from the card (a named event, a % change, a unit count — with its source).
4. Carry a **target** and a **derivation chain** (benchmark → assumption → formula).

Suggested candidates (AI picks 3–5):

| Funnel stage | Campaign example | Membership example |
|---|---|---|
| Reach | social impressions per market | organic follower growth |
| Engagement | content saves/shares; waitlist sign-ups | content engagement; community joins |
| Conversion | intent hold → purchase rate | visitor → member conversion |
| Outcome | units sold / CAC | members acquired / merch sell-through |

## 3. The derivation chain (mandatory)

Every target must show how it was reached:

> **benchmark → assumption → formula → target**

- **benchmark** — the anchor fact from the card (with source).
- **assumption** — the explicit bridge from the benchmark to our pilot (e.g. "our 2 pilot markets behave like ~8% of the benchmark base").
- **formula** — how the target is computed.
- **target** — the resulting pilot number.

Never assert a number without the chain. If you can't show the chain, drop the number.

## 4. Where it lives

- The metrics + derivation are written into `campaign-plan.html` (a "Pilot Forecast" block under the plan) and into the plan capture's `pilot_forecast` field, so the showcase stage can reuse them.
- The showcase deck carries no separate metrics slide; the full metrics live in the plan and the proposal.

## 5. Anti-patterns

- More than 5 metrics (focus is lost).
- A metric with no benchmark reference or no derivation chain.
- Full-scale projections dressed up as pilot targets.
- Vanity metrics that say nothing about the pilot's outcome.
