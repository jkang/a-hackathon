---
name: opportunity-definition
description: Define a marketing opportunity in 5 structured elements — ① a one-line description, ② the target segment & scenario, ③ the pain/tension, ④ the solution hypothesis, ⑤ the value/return — plus a 4-row value-breakdown table. Use in the plan gate to scope a single, focused opportunity from the insight. Triggers: "opportunity definition", "define the opportunity", "scope the campaign", "opportunity".
---

# Opportunity Definition (marketing · 5 elements)

After the insight gate has produced **~6 key insights**, scope the opportunity the plan will pursue into something **structured, reviewable, and fundable**.

## The 5 elements

| # | Element | Defined as | Test |
|---|---|---|---|
| ① | **One-line opportunity** | for whom + what we build/do + to achieve what | subject = the target; "move X from … to …" |
| ② | **Target segment & scenario** | the audience + a typical trigger scenario | a named segment + a when/where moment |
| ③ | **Pain / tension** | the specific unmet need | traces to the selected insight |
| ④ | **Solution hypothesis** | the approach + the main risk / guardrail | says what we do and what could go wrong |
| ⑤ | **Value / return** | the business payoff | directional but quantifiable |

## Value breakdown (4 rows)

| Dimension | Quantifies |
|---|---|
| **Scope** | which markets / segments / channels it touches |
| **Frequency** | how often the need occurs × volume |
| **Per-instance value** | the gain per occurrence (time, cost, revenue) |
| **Cumulative impact** | the KPI it moves, at scale |

## Output

**Dual output**: structured **YAML** + an interactive **HTML** card (light mode, Ascentium brand): card head (name · type · the insight it answers) → elements ①–⑤ → value-breakdown table.

## Workflow

1. **Parse input** — the selected insight(s) + the opportunity; if only natural language is given, infer the tension.
2. **Derive the YAML** (5 elements + value breakdown).
3. **Compile the HTML** (single file).
4. **Deliver** — note the opportunity card structure; include a "copy YAML" affordance.

## Where it fits

- **Upstream**: the plan gate — the chosen idea(s) from `creative-concept`.
- **Downstream**: the campaign plan (positioning, offering, 4Ps, pilot, budget) → the A/B variants.

## QA

- [ ] YAML parses; 5 elements present, in order.
- [ ] ① is self-explanatory (for whom · what · outcome).
- [ ] ⑤ is quantifiable; value breakdown has all 4 rows.
- [ ] Forecast/return cites a basis (benchmark, assumption, or pilot rate) — no invented numbers.
