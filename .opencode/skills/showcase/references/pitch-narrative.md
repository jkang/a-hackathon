# Pitch Narrative — 5 storylines (pick one)

The deck is the **Showcase Report Agent (AUTO)** output. To avoid "every group shows the same template", the team picks **one of 5 storylines**, each with a distinct narrative shape and a **signature element** that carries the core idea as the emotional peak.

> Core rule: **the idea must be SHOWN, not described.** Every storyline ends on the idea as a *signature element* (poster / storyboard / prototype / lyric), not as a paragraph.

## The 5 storylines

| # | Storyline | Signature element | Beat order | Best for |
|---|---|---|---|---|
| S1 | **Classic** | poster + full plan | title → context → problem → insight → audience → keyvisual → **poster** → strategy → offering → moments → experiment → plan → funnel → proof → ask | data-driven, rational (full detail) |
| S2 | **Hero's Journey** | **storyboard (6-frame fan journey)** | title → context → problem → **storyboard** → keyvisual → insight → audience → strategy → offering → moments → experiment → plan → funnel → proof → ask | emotional, consumer campaigns |
| S3 | **Big Reveal** | poster | title → context → problem → keyvisual → **poster** → insight → audience → strategy → offering → moments → experiment → plan → funnel → proof → ask | bold, iconic |
| S4 | **Demo** | **prototype mock screens** | title → context → problem → **prototype** → insight → audience → strategy → offering → moments → experiment → plan → funnel → proof → ask | product / membership campaigns |
| S5 | **Trailer** | **lyric / anthem** | title → context → problem → **lyric** → insight → audience → strategy → offering → moments → experiment → plan → funnel → proof → ask | entertainment, experiential |

> The `plan` beat = the **budget bar chart** (it is the "plan" slide). All five storylines share the full detail set; they differ only in the **signature element** and the opening order.

> **Poster is always on.** The campaign poster always appears in the deck (`data-poster="yes"`). If the storyline doesn't already place it, the `poster` beat is inserted after the key visual. (The poster itself is built by the `poster` skill in the Plan stage — the showcase always embeds it.)

## Beat library (visual-first)

`title` · `context` (client + evidence) · `problem` (contrast stats) · `insight` (seed + trends) · `audience` (segments + moment) · `keyvisual` (full-bleed illustration) · `poster` · `storyboard` · `prototype` · `lyric` · `strategy` (positioning + 4Ps) · `offering` (the offer / tiers) · `moments` (scenario timeline) · `experiment` (treatment vs control) · `plan` (budget bar chart) · `funnel` (reach→outcome) · `proof` (pilot metric tiles + derivation logic) · `ask` (the ask).

## Illustrations

Brand flat illustrations (inline SVG, no external assets) render on the **title** and **keyvisual** beats — the quest's key-visual motif, supplied by the card's `key_visual_svg`. Accent icons on the moments timeline.

## Signature elements (the idea's carrier)

| Element | What it is | Template beat |
|---|---|---|
| Poster | full-bleed hero visual | `data-beat="poster"` |
| Storyboard | 6-frame sketch of the fan's journey (before → moment → after) | `data-beat="storyboard"` |
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

- A deck with no signature element (the idea is just text) — this is the "flat" failure mode.
- Same template feel for every group — the storyline pick exists to prevent this.
- Bonus media blocking the 6 required deliverables.
- Using iframes or CDN chart/video libs (breaks single-file, double-click).
