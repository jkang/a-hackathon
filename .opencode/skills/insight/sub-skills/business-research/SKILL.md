---
name: business-research
description: Marketing-oriented research on an ORGANIZATION (not a financial enterprise profile) — the client, brand, or IP holder behind a campaign. Gathers the org's identity & mission, offer & pricing, audience & community, owned assets / IP, routes to market & partners, market & competitive context, and recent activity, proof & watch-outs — then returns a structured Organization Profile that seeds a campaign. Uses the agent-reach sub-skill for live sources. Triggers: "organization research", "org profile", "brand research", "client profile", "market research", "IP audit", "business research".
---

# Business Research — Organization Profile (marketing purpose)

Research the **organization** behind the quest — the client, brand, or IP holder — to support **marketing** decisions. This is **not** a financial/enterprise due-diligence profile. It answers:

> *Who are they? What do they offer? Whom do they serve? What can we leverage? What limits us?*

## When to use

- In the insight stage, to build the **organization / IP profile** and the **benchmark baseline**.
- Anytime a campaign needs grounding on the client, brand, or IP holder.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Organization / client | yes | the entity to profile |
| Marketing objective | yes | which business (ticketing, membership, IP…) the campaign targets |
| Market / region | no | narrows the search |
| Comparable orgs / events | no | gold-standard & cautionary-tale benchmarks |

## How to research (live, via `agent-reach`)

- Use the **`agent-reach`** sub-skill for real sources: Exa web search (`mcporter call exa.web_search_exa …`), Jina reader for any page (`curl -s "https://r.jina.ai/URL"`), etc.
- **Open the source and read the full text** — never rely on search snippets alone.
- Default data window: **the last ~24 months**, computed from the current year (do not use stale years).
- The **quest card is the primary pack** — research *supplements* it; do not re-collect what the card already gives.
- If live tools are unavailable, continue from the quest card + team knowledge and label the report accordingly.

## Collect framework — 7 marketing dimensions

Details + report template in [`references/collection_framework.md`](references/collection_framework.md).

1. **Identity & Mission** — who the org is; mission / brand promise; positioning.
2. **Offer & Pricing** — what they sell (tickets, memberships, experiences, IP/licensing); tiers; price points.
3. **Audience & Community** — existing fans / customers; segments; community & fandom size.
4. **Assets & IP** — owned, marketable assets (venues, IP, mascots, superstars, media, data).
5. **Routes to Market & Partners** — channels + distribution / sponsorship partners (airlines, retail, platforms, tourism boards).
6. **Market & Competitive Context** — market size / reach, share, competitors, benchmark events.
7. **Recent Activity, Proof & Watch-outs** — recent campaigns / sponsorships / press, benchmark wins, and constraints & risks (budget, capacity, regulation, reputation).

## Output

A structured **Organization Profile** in Markdown (template in the reference). Every key claim carries a **source + an "as of" date**; separate facts from `[inference]`; never invent numbers.

## Self-check

- [ ] Each key data point has a **source (URL / doc) + date**.
- [ ] Data sits within the **last ~24 months**.
- [ ] All **7 dimensions** covered (mark "no public data" where missing).
- [ ] **Marketing-focused**, not a generic company introduction.
- [ ] Facts vs `[inference]` separated; **no fabricated numbers or rankings**.

## Where it fits (insight research chain)

- **Upstream**: the quest card + **`agent-reach`** (data collection).
- **Downstream**: `market-trends` (the org's assets shape which external opportunities matter) and `audience-analysis` (the org's offer / assets / constraints set **fit** — which segments we can win).
