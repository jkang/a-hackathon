---
name: market-trends
description: Research and curate the MARKET TRENDS block of the insight stage — the single merged market read that spans directional shifts, hard field facts, and external opportunities/threats. Produces ~6–8 data-backed trend items, each tagged by kind (shift / fact / opportunity / threat), shown in full with no team pick. Owns the market context that feeds audience segmentation and the key insights. Uses the agent-reach sub-skill for live facts/reports. Triggers: "market trends", "market read", "trend analysis", "market research", "what's shifting", "opportunities and threats", "market context".
---

# Market Trends — the market read

Research the **market** the campaign competes in and distill it into one merged read: the **Market Trends** block. This is the **external, market-facing** view — it answers:

> *What is happening in this market, what is shifting, and which external forces help or hinder us?*

It is **not** a generic industry report. Every item is a **decision-grade** trend — a fact/number + why it matters for this campaign.

## When to use

- In the insight stage, to build the **Market Trends** block — the context that comes *before* audience segmentation (trends set the market backdrop and the "attractiveness" signals for segments).
- Anytime a campaign needs a defensible external market read (shifts, hard facts, opportunities, threats).

## Inputs

| Input | Required | Notes |
|---|---|---|
| Quest card | yes | already carries market size, benchmark, arena — **the primary data pack** |
| Marketing objective | yes | which business the campaign targets |
| Market / region | yes | e.g. Asia-wide, global — from the card |
| Org profile | recommended | from `business-research` — what the org can leverage (shapes which opportunities matter) |
| Live sources | recommended | fetched via `agent-reach` |

## How to research (live, via `agent-reach`)

- Use the **`agent-reach`** sub-skill / the `researcher` subagent for real sources: Exa web search (`mcporter call exa.web_search_exa …`), Jina reader for any page (`curl -s "https://r.jina.ai/URL"`), YouTube, reports.
- **Open the source and read the full report** — never rely on search snippets.
- Default data window: **the last ~24 months**, computed from the current year.
- The **quest card is the primary pack** — research *supplements* it; do not re-collect what the card already gives.
- If live tools are unavailable, continue from the quest card + team knowledge and label the report accordingly; **cap retries at 2–3 attempts per source** (mark unreachable and move on).

## Method

1. **Start from the card** — market size, benchmark, arena, and the challenge's stated context.
2. **Scan the categories** (see the reference) — behavior / culture / technology-policy — and pull **hard field facts** (attendance, spend, platform data).
3. **Classify each item** by `kind`:
   - `shift` — a directional behavior/culture move,
   - `fact` — a hard number/field fact,
   - `opportunity` — an external force the campaign can exploit,
   - `threat` — an external force that works against the campaign.
4. **Attach evidence** — every item gets a fact/number + a source + as-of date.
5. **Show in full** — all items stay in the brief; there is **no pick** for trends.

## Trend item schema (each item)

```
{trend, why_it_matters, kind, source}
```

- **trend** — a short label of the shift/fact/opportunity/threat.
- **why_it_matters** — the "so what" for this campaign (one line).
- **kind** — `shift` | `fact` | `opportunity` | `threat`.
- **source** — the source + as-of date.

Aim for **~6–8 items**, balanced across the kinds. The block is a **merged read** — there is **no separate "truths" block and no separate SWOT block**.

## Output

- The **Market Trends** items rendered into the insight brief's "Market Trends" card (all shown, no pick).
- The structured `trends[]` array embedded in the `insight-brief.html` capture (no separate file).

## Self-check

- [ ] **~6–8 items**, each carrying a **fact/number + source + date**.
- [ ] Every item is tagged with a **`kind`** (`shift` / `fact` / `opportunity` / `threat`).
- [ ] Market-focused and **decision-grade** — no generic industry filler.
- [ ] The card's data is used, not duplicated; `[inference]` separated from facts.
- [ ] No fabricated numbers; unreachable sources labelled.

## Where it fits (insight research chain)

- **Upstream**: the quest card + **`agent-reach`** (live facts) + `business-research` (what the org can leverage).
- **Downstream**: `audience-analysis` (**segments** — trends provide the market backdrop + attractiveness signals) and the **focus bundles / key insights** (each bundle and insight references a `trend_id`).
