# Pitch Narrative — 5 storylines (pick one)

The deck is the **Showcase Report Agent (AUTO)** output. To avoid "every group shows the same template", the team picks **one of 5 storylines**, each with a distinct **signature element** that carries the core idea as the emotional peak.

> Core rule: **the idea must be SHOWN, not described.** Every storyline features the idea as a *signature element* (poster / storyboard / prototype / lyric), not as a paragraph.

## The 5 storylines

**Hard cap: the deck is ≤ 8 slides, visual-first.** The locked core is **7 beats**; the poster is always on, so a storyline whose signature isn't the poster runs at 8.

| # | Storyline | Signature element | Beat order | Best for |
|---|---|---|---|---|
| S1 | **Classic** | poster | title → context → insight → audience → **poster** → strategy → ask | data-driven, rational |
| S2 | **Hero's Journey** | **storyboard (6-panel fan-journey sheet)** | title → context → insight → audience → **storyboard** → strategy → ask | emotional, consumer campaigns |
| S3 | **Big Reveal** | poster | title → context → insight → audience → **poster** → strategy → ask | bold, iconic |
| S4 | **Demo** | **prototype mock screens** | title → context → insight → audience → **prototype** → strategy → ask | product / membership campaigns |
| S5 | **Trailer** | **lyric / anthem** | title → context → insight → audience → **lyric** → strategy → ask | entertainment, experiential |

> All five storylines share the same 7-beat core and differ only in the **signature element** (and the opening treatment). The `strategy` beat carries **positioning + 4Ps + the budget bar chart** (the plan is folded in — there is no separate plan slide).

> **Poster is always on.** The campaign poster always appears in the package (`data-poster="yes"`) and is embedded in the proposal. When the storyline's signature *isn't* the poster (Hero's Journey / Demo / Trailer), the poster beat is inserted after `audience` (8 slides total). When the signature *is* the poster (Classic / Big Reveal), it is the poster beat (7 slides).

## Beat library (visual-first)

`title` · `context` (client + evidence + the problem, with contrast-stat tiles) · `insight` (seed + trends) · `audience` (segments + moment of truth) · `poster` · `storyboard` · `prototype` · `lyric` · `strategy` (positioning + 4Ps + budget + pilot line) · `ask`.

> The pilot metrics + derivation chains live in `campaign-plan.html` and the proposal — **not** as a deck slide. Optional beats (keyvisual · moments · offering · experiment · funnel) are **retired** to hold the deck at ≤ 8 slides.

## Illustrations

Brand flat illustrations (inline SVG, no external assets) render on the **title** and **keyvisual** beats — the quest's key-visual motif, supplied by the card's `key_visual_svg`. Accent icons on the moments timeline.

## Signature elements (the idea's carrier)

| Element | What it is | Template beat |
|---|---|---|
| Poster | full-bleed hero visual | `data-beat="poster"` |
| Storyboard | one 6-panel storyboard sheet of the fan's journey (before → moment → after) | `data-beat="storyboard"` |
| Prototype | 2–3 phone mock screens of the product | `data-beat="prototype"` |
| Lyric / anthem | a jingle sheet with a chantable hook | `data-beat="lyric"` |

## Media embeds (bonus · per storyline)

Optional generated media (song / video / image) slots into the matching beat:

| Media | Embeds into | HTML |
|---|---|---|
| Image (GPT) | **poster** beat | `<img>` |
| Video (Runway) | **storyboard** beat (the moment) | `<video controls>` |
| Song (Suno) | **lyric** beat (the anthem) | `<audio controls>` |

The AI writes the prompts (see `references/media-prompts.md` + `templates/prompt-pack.html`); the human generates and brings files back; the AI embeds them.

## The deck template

One configurable `templates/pitch-deck.html` with all beats; the `<body data-storyline="...">` selects the order. Single-file, full-screen auto-scale, ←/→ nav, F fullscreen.

## Human decisions (new)

Exactly **two**:

- Which **storyline** (S1–S5).
- Whether to attempt **bonus media** (song / video / image / none) and which generated result to use.

> The **signature element** (the storyline's default), the **visual direction**, and the **one-liner** are **AI-decided**; the **poster** is always included.

## Anti-patterns

- More than 8 slides, or a metrics/proof slide (the numbers live in the plan + proposal).
- A deck with no signature element (the idea is just text) — this is the "flat" failure mode.
- Same template feel for every group — the storyline pick exists to prevent this.
- Bonus media blocking the deliverables.
- Using iframes or CDN chart/video libs (breaks single-file, double-click).
