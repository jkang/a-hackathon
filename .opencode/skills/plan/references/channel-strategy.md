# Channel Strategy (media / communication channels)

Select the **media / communication channels** a campaign variant uses to reach its audience — grounded in the insight, never invented. This is **AI-curated** (no team decision); it feeds each variant's `channel_mix` and the budget allocation's Channel column.

> **Media channel ≠ distribution (Place).** "Place" (4Ps) is *where the product is sold* (ticketing, retail, partners). A **channel** here is *where the message is delivered* (short-video, creators, search, partnerships, community, OTA funnels). Keep them distinct.

## Inputs (from the insight capture)

- The selected segment's **`channels`** field — *where to reach them*.
- The key insight's **trend** (via `trend_id` → `market-trends`) — the channel signals inside the market read (e.g. "short-video is discovery *and* checkout", "creator trust > paid ads", "fan travel is loyalty / partnership-led").
- The focus bundle's **`moment.where`** — the context of the moment of truth.

## Method

1. **List candidates** — union of the segment's `channels` and the channel facts named by the supporting trend.
2. **Match to the moment** — each channel must fit *where the moment happens*:
   - discovery scroll → short-video + creators;
   - booking / sale window → OTA, airline & ticketing partners, search;
   - event / journey moment → community, in-venue, creator collaboration;
   - loyalty / gifting window → membership, email/CRM, retail.
3. **Assign a funnel role** to each: **reach → engage → convert**.
4. **Pick the mix** — **one primary channel** + **2–3 supporting**, each with a one-line *why* tied to the insight.

## Output (capture → `variant.channel_mix`)

```
{ "primary": "…", "support": ["…", "…"], "why": "…", "moment": "…" }
```

- **primary** — the one channel the campaign is built around.
- **support** — 2–3 channels that amplify or convert.
- **why** — the insight-based reason (segment × trend × moment).
- **moment** — the moment of truth this mix serves.

Variants may differ: e.g. A = creator-led (short-video primary), B = partnership-led (airline/ticketing funnel primary). That is legitimate differentiation.

## Anti-patterns

- A channel with **no tie** to the segment / trend / moment ("we'll just do social").
- **"Be everywhere"** — a channel list with no primary and no roles.
- Conflating **media channel** with **distribution (Place)**.
- Channels that the segment's `channels` field and the trend do not support — i.e. invented reach.
