# Cost-Benefit Method

Prove the pilot is worth unlocking the full budget. Keep the math simple and grounded in card economics.

## 1. Inputs

- `budget.total` from `plan.yaml` (A: 1.5M, B: 1.1M).
- The team's sub-metrics (leading indicators).
- Card economics for the payoff path:
  - A: 400K tickets, $40M merch+hospitality, 500M impressions (full scale); Hangzhou ticket revenue ¥610M.
  - B: $28M licensing/merch, 1M members, non-ticket spend $6→15; Fu Bao 2.7M merch units; Xiang Xiang ≈ ¥2.7B.

## 2. Derivation — de-risk the big bet (never assert a number)

A 3-month pilot's real value is **de-risking the full unlock** (USD 30M / 11M), not its own revenue. Build the case in two layers so every number has a visible chain:

**Layer 1 — the pilot validates the rates** (do NOT claim big pilot revenue):
- reach → intent → conversion, CAC, attach — all measured in the 3-month pilot.

**Layer 2 — full-scale projection** (extrapolate with the pilot-validated rates):
```
full_return = full_target_units × unit_value + merch
roi         = (full_return − full_budget) / full_budget
```

Worked example (Quest A):
```
pilot validates: intent 3.2%, CAC $7.40, group ratio 41%
full scale (18 mo, 6 priority Asian markets, USD 30M):
  tickets = 400K (Victory Condition) × ~$85 avg bundle value = $34M
  merch   = $40M (Victory Condition)
  return  = $34M + $40M = $74M
  roi     = ($74M − $30M) / $30M ≈ 1.5x over 18 months
verdict: GO — pilot rates imply the full-scale ROI clears the bar; unlock.
```

**Rules:**
- Every number in the chain must trace to (a) a card benchmark, (b) a pilot sub-metric, or (c) an explicit assumption you can state out loud.
- If you can't show the chain, drop the number — a claim is not a case.

## 3. Unlock verdict

| Verdict | When |
|---|---|
| **Go** | Trajectory predicts the Victory Conditions at acceptable ROI. |
| **Iterate** | Promising but one or two metrics missed; one more cycle. |
| **Stop** | Economics don't close or a No-Go threshold is breached. |

State the verdict in one line, with the number that drives it.

## 4. Presentation

- One small table: cost / projected return / ROI / verdict.
- One sentence tying the ROI to the specific unlock (USD 30M / USD 11M).

## 5. Anti-patterns

- ROI with no unit values shown.
- Confusing pilot return with full-scale return.
- Burying the verdict.
