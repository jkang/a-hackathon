---
name: poster
description: Create a professional campaign poster — the "hero visual" / poster deliverable from the Create (Plan) stage. Produces a self-contained portrait poster: masthead (creator + client), campaign name + tagline + key visual, lead proposition, offer panel (or membership tiers), benefit bullets, a stats band of 4 numbers, CTA + hashtag + URL + QR, and a partner/source footer. Use whenever a campaign poster or hero visual is needed. Triggers: "poster", "hero visual", "campaign poster", "key visual", "make a poster".
---

# Poster — professional campaign poster

The **most-seen asset** of a campaign. It must be **self-contained**: a stranger should understand the campaign, the offer, and the next step from the poster alone. It is the poster / hero-visual deliverable of the Create stage.

> Not a banner. A name + slogan on a colour block is not a poster — the full proposition, offer, proof and CTA must all be present.

## When to use

- During the Create/Plan gate (the poster belongs with the creative concept, not the showcase).
- When the team wants the hero visual, or the Big Reveal storyline needs a poster.
- Standalone: "make a poster for this campaign".

## Inputs

- `plan.yaml` — the chosen variant: campaign name, slogan, proposition, offering/tiers, pilot markets, budget.
- `insight.yaml` — audience + moment (for the anchor).
- Team choices: visual direction + the one-liner/CTA.

## Anatomy (top → bottom)

| # | Section | Carries |
|---|---|---|
| 1 | Masthead | Ascentium logo + client logo + edition |
| 2 | Hero lockup | kicker + **campaign name** + **tagline** |
| 3 | Key visual | brand illustration (stadium / panda) |
| 4 | Lead | the proposition in one sentence |
| 5 | Offer panel | 3 cards (offer / markets / access) — or **membership tiers** |
| 6 | Bullets | 3 concrete benefits / proof points |
| 7 | Stats band | **4 hard numbers** |
| 8 | CTA band | action button + hashtag + URL + QR |
| 9 | Footer | partners + sources + data-as-of |

See `references/poster-method.md` for the full method and checklist.

## Output

- `poster.html` — portrait, ~1080px wide (scales to A3/A2), single-file, inline tokens + inline SVG illustrations.

## Workflow

1. Pull name / slogan / proposition / offer from `plan.yaml`.
2. **Team picks visual direction + the one-liner** (HITL — the AI does not choose).
3. Fill the 9 sections; set `data-quest="A|B"` for the accent + illustration.
4. Self-check against the content checklist in `references/poster-method.md`.

## Brand

Uses `ascentium-brand`. Quest A = orange accent; Quest B = teal accent. Body text Midnight Green; Poppins.

## Anti-patterns

- **Too sparse** (name + slogan + one stat only). ❌
- No client identity, no key visual, no CTA/channel.
- Paragraph text instead of short bullets + numbers.
- Off-brand colours; low contrast.
