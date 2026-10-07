---
name: swot-analysis
description: Structured SWOT synthesis for a marketing campaign — combine the organization profile (internal Strengths/Weaknesses) with the audience + market context (external Opportunities/Threats), and produce an evidence-backed SO/WO/ST/WT cross-strategy matrix. The synthesis step of the insight gate. It produces no standalone block: Strengths/Weaknesses feed the Org/IP Profile and Opportunities/Threats fold into Market Trends. Triggers: "SWOT", "strengths weaknesses", "competitive analysis", "business diagnosis", "cross-strategy".
---

# SWOT Analysis — campaign synthesis

Turn the insight research into a strategic read. **Internal** factors come from the organization profile; **external** factors come from the audience map + market. Its output is **distributed, not a standalone block**: **S/W → the Org / IP Profile**, **O/T → the Market Trends block**. (A cross-strategy matrix remains an optional scaffold.)

## Inputs

| Input | Required | Notes |
|---|---|---|
| Organization profile | recommended | from `business-research` — the **internal** base (assets, offer, constraints) |
| Audience map | recommended | from `audience-analysis` — the **external** base (segments, needs) |
| Market context | recommended | the quest card + research (size, trends, benchmarks) |
| Comparables / competitors | no | for benchmarking |

If inputs are missing, gather the essentials via `agent-reach`; if tools are unavailable, proceed from the quest card + team knowledge and label it.

## Steps

1. **Confirm the facts** — pull from `business-research` (internal) + `audience-analysis` + market (external).
2. **Analyse S/W/O/T** — for the specific business/market in the quest, not a generic company read.
3. **Attach evidence** — every point gets a fact/number + an impact rating + a source.
4. **Build the cross-strategy matrix** — SO / WO / ST / WT → concrete moves.
5. **Self-check** — verify against the checklist before output.

## Framework

### Strengths (internal — from the org profile)
| Dimension | Look for |
|---|---|
| Assets | venues, IP, mascots, superstars, content, data |
| Capabilities | brand recognition, operations, reach |
| Ecosystem | partners, sponsors, distribution, platform effects |
| Scale | audience base, share, cost position |

### Weaknesses (internal)
| Dimension | Look for |
|---|---|
| Capability gaps | missing channels, skills, tools |
| Structural | slow decisions, org limits, capacity |
| Financial | budget pressure, ROI constraints |
| Market limits | narrow segment, weak awareness, regulation |

### Opportunities (external — audience + market)
| Dimension | Look for |
|---|---|
| Market trends | growth, rising demand, new behaviours |
| Audience | under-served segments, unmet needs, triggers |
| Technology / channels | new platforms, content formats |
| White space | competitor blind spots, unclaimed positions |

### Threats (external)
| Dimension | Look for |
|---|---|
| Competition | new entrants, substitutes, price pressure |
| Regulation | policy, compliance, visa/entry rules |
| Reputation / ethics | backlash risk (e.g., conservation-first) |
| Macro | economy, geopolitics, seasonality |

### Evidence requirement
Every S/W/O/T point: **claim** (one line) · **evidence** (fact/number) · **impact** (high/med/low) · **source**.

### Cross-strategy matrix

| | Opportunities | Threats |
|---|---|---|
| **Strengths** | **SO** — use strengths to seize opportunities | **ST** — use strengths to counter threats |
| **Weaknesses** | **WO** — fix weaknesses to unlock opportunities | **WT** — avoid weaknesses and threats |

Produce 1–2 concrete, adoptable moves per quadrant.

## Output

The synthesis **feeds the insight brief — there is no standalone SWOT block**:
- **Internal Strengths / Weaknesses** → the **Org / IP Profile** (assets = strengths, constraints = weaknesses).
- **External Opportunities / Threats** → the **Market Trends** block (the merged market read).
Cross-strategy moves remain an optional scaffold; template in [`references/analysis_framework.md`](references/analysis_framework.md).

## Self-check

- [ ] Each S/W/O/T point has **evidence** (not a feeling).
- [ ] **Campaign/business-focused**, not a generic company analysis.
- [ ] **3–5 points** per quadrant; balanced.
- [ ] Cross-strategy moves are **concrete and adoptable**.
- [ ] Impact ratings justified; **sources** traceable.

## Where it fits (insight research chain)

- **Upstream**: `business-research` (**internal S/W**) + `audience-analysis` + market context (**external O/T**).
- **Downstream**: the **key insights** → the `plan` gate (strategic move). S/W are written into the org profile; O/T into the market trends.
- **Note**: SWOT is the **synthesis** layer — it comes *after* both the org profile and the audience map, because O/T need the external view. It does **not** produce its own brief block.
