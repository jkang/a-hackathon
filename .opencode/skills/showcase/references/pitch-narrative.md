# Pitch Narrative — 5 storylines (pick one)

The deck is the **Showcase Report Agent (AUTO)** output. To avoid "every group shows the same template", the team picks **one of 5 storylines**, each with a distinct narrative shape and a **signature element** that carries the core idea as the emotional peak.

> Core rule: **the idea must be SHOWN, not described.** Every storyline ends on the idea as a *signature element* (poster / storyboard / prototype / lyric), not as a paragraph.

## The 5 storylines

| # | Storyline | Signature element | Beat order | Best for |
|---|---|---|---|---|
| S1 | **Classic** | poster + full plan | title → problem → insight → keyvisual → **poster** → strategy → moments → experiment → budget → funnel → proof → ask | data-driven, rational (full detail) |
| S2 | **Hero's Journey** | **storyboard (6-frame fan journey)** | title → problem → **storyboard** → keyvisual → insight → moments → budget → proof → ask | emotional, consumer (Quest A) |
| S3 | **Big Reveal** | poster + manifesto | title → problem → keyvisual → **poster (reveal)** → strategy → proof → ask | bold, iconic |
| S4 | **Demo** | **prototype mock screens** | title → problem → **prototype** → experiment → budget → proof → ask | product / membership (Quest B) |
| S5 | **Trailer** | **lyric / anthem** | title → problem → **lyric** → funnel → proof → ask | entertainment, experiential |

> **Poster is optional.** The team chooses whether the campaign poster appears in the deck (`data-poster="yes|no"`). If **yes** and the storyline doesn't already include it, the `poster` beat is inserted after the key visual; if **no**, it is omitted entirely. (The poster itself is built by the `poster` skill in the Plan stage — the showcase only decides whether to show it.)

## Beat library (visual-first)

`title` · `problem` (contrast stats) · `insight` (segment/job/moment) · `keyvisual` (full-bleed illustration) · `poster` · `storyboard` · `prototype` · `lyric` · `strategy` (positioning + 4Ps quadrant) · `moments` (scenario timeline) · `experiment` (treatment vs control) · `budget` (bar chart) · `funnel` (reach→outcome) · `proof` (KPI tiles + sub-metric bars + Go/No-Go) · `ask` (big ROI).

## Illustrations

Brand flat illustrations (inline SVG, no external assets) render on the **title** and **keyvisual** beats — stadium + flying tickets for Quest A, panda + bamboo for Quest B. Accent icons on the moments timeline.

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

- Which **storyline** (S1–S5).
- Which **signature element** (usually tied to the storyline, but can mix).
- Whether to attempt **bonus media** (song / video / image / none) and which generated result to use.

## Anti-patterns

- A deck with no signature element (the idea is just text) — this is the "flat" failure mode.
- Same template feel for every group — the storyline pick exists to prevent this.
- Bonus media blocking the 6 required deliverables.
- Using iframes or CDN chart/video libs (breaks single-file, double-click).
