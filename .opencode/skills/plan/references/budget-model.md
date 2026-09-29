# Budget Model

The card says: **"Budget allocation is part of the solution."** The team allocates the MVP budget; the AI turns it into a clean table and a first-pass return estimate.

## 1. The envelope

| Quest | Total approved | MVP unlock | Pilot window | Scope |
|---|---|---|---|---|
| A | USD 30M | 5% = **USD 1.5M** | 3 months | 2 SEA markets |
| B | USD 11M | 10% = **USD 1.1M** | 3 months | 2 overseas markets |

## 2. Allocation categories (starter menu)

Split the budget across some/all of these — the mix is the team's call:

| Category | Examples |
|---|---|
| Paid media | social ads, search, programmatic |
| Content & creators | hero film, KOL/creator seeding, UGC |
| Partnerships | airline (Qatar Airways), ticketing, retail, tourism boards |
| Activation / events | pop-ups, fan zones, roadshows |
| Localization | language, cultural adaptation (A: Bahasa/Thai/Vietnamese/Tagalog/English) |
| Measurement & tools | analytics, attribution, dashboarding |
| Contingency | buffer for what the pilot teaches |

## 3. Allocation worksheet

```yaml
budget:
  total: 1.5M
  allocation:
    - {market: "Indonesia", channel: "paid social", tactic: "creator-led countdown", amount: 300000}
    - {market: "Thailand",  channel: "partnership",  tactic: "airline co-promo",       amount: 250000}
    # ...
```

Rules:
- Every line ties to a market, a channel, and a tactic.
- Sum must equal the envelope.
- Reserve ~5–10% contingency.

## 4. First-pass return estimate (rough)

- For each major line, state the projected leading outcome (e.g. reach, sign-ups, ticket holds).
- Compare media cost to a benchmark cost-per-outcome from the card if available.
- This is a **sanity check**, not the final cost-benefit case.

## 5. Pricing anchor (membership / tiers)

Never invent a price. Anchor it to a comparable the audience already accepts:

- **Fan / idol memberships** (K-pop fan clubs, Weverse) — $25–50/yr for content + belonging.
- **Creator memberships** (Patreon, YouTube) — $5–15/mo tiers.
- **Zoo / museum memberships** — $50–120/yr for access + perks.
- **NGO / conservation** (WWF, panda adoption) — $25–60/yr to "fund the animal".

State it out loud: *"we price Founding at $30/yr because idol fan clubs charge ~$40 for belonging and WWF adoption is ~$50 — we sit under both."*

## 6. Scale path (2 markets → N markets)

The pilot must answer "why these 2, and where next." Give the replication logic:

1. **Why these 2** — one *proven* (Japan / Indonesia) + one *scale* (Indonesia / Brazil).
2. **The replication lever** — the portable thing that made the pilot work (a creator-squad playbook, a localized content engine, an airline bundle).
3. **The next 3–4 markets** + ordering (by fan density, travel ease, affinity).
4. **The compounding** — how the pilot's assets (crew network, membership cohort, content engine) compound into the 18-month rollout.

Without this, "2 markets → Victory Conditions" reads like magic.

## 7. Anti-patterns

- All budget in one channel with no test diversity.
- No measurement line (then the pilot can't prove anything).
- Allocation that ignores the 3-month timebox.
