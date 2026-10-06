# Poster Method — professional campaign poster

A campaign poster is not a slogan on a colour block. It is the **single most-seen asset** of the campaign and must carry the full proposition: who it is for, what the offer is, the proof, and the call to action — at a glance, from a distance.

> The failure mode we are fixing: a poster with only a name + slogan + one number. That is a *banner*, not a poster. A poster must be **self-contained** — a stranger should understand the campaign, the offer and the next step without any other slide.

## Poster anatomy (top → bottom)

| # | Section | What it carries | Filled from |
|---|---|---|---|
| 1 | **Masthead** | creator logo (Ascentium) + **client logo** + edition | card / client |
| 2 | **Hero lockup** | kicker (edition) + **campaign name** (dominant) + **tagline** | plan capture |
| 3 | **Key visual** | the brand illustration (the quest's key-visual motif) | template |
| 4 | **Lead** | the proposition in one sentence | plan / insight captures |
| 5 | **Offer panel** | 3 cards: the offer / markets / access. For membership: the **tiers** | plan capture |
| 6 | **Bullets** | 3 concrete benefits / proof points | plan capture |
| 7 | **Stats band** | 4 hard numbers (target, market, benchmark, window) | card / proof |
| 8 | **CTA band** | action button + **hashtag** + **URL** + **QR** | team |
| 9 | **Footer** | partners + sources + data-as-of | card |

## Hierarchy rules

1. **One dominant element**: the campaign name. Everything else is secondary.
2. **Read at 3 distances**: name (10 m) → tagline + visual (3 m) → offer/details (1 m).
3. **Numbers sell**: at least 4 distinct proof numbers (or facts) must appear.
4. **Always show the next step**: CTA + channel (hashtag / URL / QR).
5. **Brand-locked**: accent colour comes from the quest card's `accent` token (orange default / teal where declared); body text Midnight Green; Poppins. Never a self-invented colour.

## Content checklist (a poster is incomplete without these)

- [ ] Client + creator identity
- [ ] Campaign name + tagline
- [ ] Key visual
- [ ] One-line proposition
- [ ] The offer (with price/tiers/dates for membership)
- [ ] ≥3 benefits or proof points
- [ ] ≥4 key numbers
- [ ] Call to action + channel (hashtag/URL/QR)
- [ ] Partners + sources + data-as-of

## Format

- Portrait, 1080px wide (scales to A3/A2). Print-safe margins (~54px).
- Single-file HTML, inline tokens + inline SVG illustrations — no external assets.
- **Three standalone pages** — `poster-a.html` / `poster-b.html` / `poster-c.html` (one clean poster each, ideal for cropping/embedding) — plus `poster.html`, the **tab page** that switches between them. Built by `scripts/build-posters.py`.

## Styles (art direction, not colourways)

| # | Style | Reads as | Built for |
|---|---|---|---|
| A | **Full-Bleed Hero** | editorial · accent hero · wide key art · dark stats band | mass energy |
| B | **Belonging Passport** | cream paper · perforations · stamp motifs · checklist | membership / bundle / belonging |
| C | **Midnight Minimal** | dark Swiss type · hairline rules · one motif · negative space | premium / brand-led |

> Style names are tone archetypes, not quest labels — a card may rename them via `poster_styles` (see `quest-card.md`).

All three carry the **same** 9 sections. Vary: colour balance, typographic scale, art motif, section chrome (rules vs filled bands), bullet style.

## Hero-art aspect rule (fixes the crop bug)

- The art band is `aspect-ratio: 1200 / 500`.
- Every illustration `<symbol>` uses `viewBox="0 0 1200 500"`.
- Equal ratios + `preserveAspectRatio="xMidYMid slice"` ⇒ **no crop, ever**.
- Changing the band height means changing the `viewBox` to match (or switching to `meet`). Never mix a 4:3 art with a wide `slice` frame — that cropped the old stadium illustration top-and-bottom.

## Choosing a style (HITL)

- Present all three; do **not** decide.
- Preview them in the **tab page** (`poster.html`); each style is also its own clean page (`poster-a|b|c.html`) for cropping/embedding.
- Record `poster.style: a|b|c` in the plan capture; the deck and proposal embed the matching page.

## Anti-patterns

- **Too sparse** — name + slogan + one stat only (the mistake we fixed). ❌
- Multiple competing focal points.
- Low-contrast text.
- No CTA or no channel.
- Unbranded colours / stock-photo look.
- Cramming paragraph text — use short bullets and numbers.
