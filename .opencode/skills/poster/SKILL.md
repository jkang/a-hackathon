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

- `poster-a.html` · `poster-b.html` · `poster-c.html` — **three standalone, clean single-poster pages** (portrait, ~1080px, single-file, inline tokens + inline SVG). One page = one design, nothing else — easy to **screenshot / crop / embed**.
- `poster.html` — the **tab page**: a slim tab bar (Style A / B / C) that switches between the three standalone pages in an iframe + an "open standalone ↗" link. This is the browsable entry point.
- Built with `scripts/build-posters.py` from two templates (`templates/poster-page.html` = one poster, `templates/poster-tabs.html` = the tab shell). Fill the content once; the script emits all four files.

## Three styles (scenario-driven — not three colourways)

Offer **3 genuinely different designs**, each matched to a campaign tone. Keep one content pack (anatomy) across all three; vary the art direction, layout and typography.

| # | Style | Art direction | Fits |
|---|---|---|---|
| A | **Matchday Roar** | bold sports editorial — full-bleed accent hero, wide crowd/stadium illustration, dark stats band, big name | loud, mass-reach, fan/energy campaigns (Quest A) |
| B | **Supporter Passport** | travel / ticket — cream paper, dashed "perforation", ticket & stamp motifs, checklist bullets, passport-card offer | membership, bundles, "belong/passport" offers (Quest A); conservation/cute IP (Quest B) |
| C | **Midnight Minimal** | Swiss typographic — dark canvas, huge type, hairline rules, one small art motif, lots of negative space | premium, brand-led, image-light or sensitive-topic campaigns |

- Set the accent with `data-quest="A|B"` (orange / teal); the art symbol follows the style token.
- Each style is a full, self-contained poster (all 9 anatomy sections) — never a partial.
- **The team picks one**; record it as `poster.style` in `plan.yaml` and in the showcase capture.
- In the **Showcase deck** the `poster` beat carries a 3-way picker that previews `poster-a|b|c.html` live, so the choice is made there.

## Workflow

1. Pull name / slogan / proposition / offer from `plan.yaml`.
2. Fill the shared content pack once into `templates/poster-page.html` (leave the `{{POSTER_STYLE}}` tokens) and the few fields in `templates/poster-tabs.html`; set `data-quest="A|B"`.
3. Build the deliverable: `python3 scripts/build-posters.py --dir <out> [--default a]` → `poster-a.html` · `poster-b.html` · `poster-c.html` · `poster.html`.
4. **Team previews the 3 styles and picks one** (HITL — the AI does not choose), via the tab page and/or the Showcase deck.
5. Record the choice in `plan.yaml` (`poster.style`) so the deck/proposal embed the right page.
6. Self-check against `references/poster-method.md`.

## Brand

Uses `ascentium-brand`. Quest A = orange accent; Quest B = teal accent. Body text Midnight Green; Poppins. Every style stays inside the token set — different *design*, same brand.

## Hero-art rule (the crop bug — do not regress)

The hero art band is locked to **aspect-ratio `1200/500`**, and every illustration `<symbol>` is authored at **`viewBox="0 0 1200 500"`**. Because the frame and the art share the same ratio, `preserveAspectRatio="xMidYMid slice"` never crops.

> **Never** put a differently-proportioned `viewBox` in a fixed-height frame with `slice` — that is what chopped the old 4:3 stadium art top-and-bottom inside a 2.16:1 band. If you change the band height, change the art `viewBox` to match (or switch to `meet` and accept letterboxing). Keep the two numbers equal.

## Anti-patterns

- **Too sparse** (name + slogan + one stat only). ❌
- **Three colourways of one layout** — the styles must differ in layout *and* art, not just colour. ❌
- A cropped/lopsided hero visual (see the art rule above). ❌
- No client identity, no key visual, no CTA/channel.
- Paragraph text instead of short bullets + numbers.
- Off-brand colours; low contrast.
