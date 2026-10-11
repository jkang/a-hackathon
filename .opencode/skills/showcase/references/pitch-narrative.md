# Pitch Narrative — 5 storylines (pick one)

The deck is the **Showcase Report Agent (AUTO)** output. To avoid "every group shows the same template", the team picks **one of 5 storylines**, each with a distinct **signature element** that carries the core idea as the emotional peak.

> Core rule: **the idea must be SHOWN, not described.** Every storyline features the idea as a *signature element* (poster / storyboard / prototype / lyric), and the **`visuals` beat always carries the other media-kit asset(s)** — so the poster and the storyboard both appear.

## The 5 storylines

**8 beats, visual-first.** Every storyline shares the same shape: **title → context → insight → audience → signature → visuals → strategy → ask**. The `visuals` beat is the secondary visual (the media-kit asset not already the signature).

| # | Storyline | Signature element | `visuals` fills | Best for |
|---|---|---|---|---|
| S1 | **Classic** | poster | storyboard | data-driven, rational |
| S2 | **Hero's Journey** | **storyboard (16:9 scene sheet, 6–8 scenes)** | poster | emotional, consumer campaigns |
| S3 | **Big Reveal** | poster | storyboard | bold, iconic |
| S4 | **Demo** | **prototype mock screens** | poster + storyboard | product / membership campaigns |
| S5 | **Trailer** | **lyric / anthem** | poster + storyboard | entertainment, experiential |

> All five storylines share the same 8 beats and differ in the **signature element** (and the opening treatment). The `strategy` beat carries **positioning + 4Ps + the budget bars** (the plan is folded in — there is no separate plan slide).

> **Both assets always appear.** The storyline's signature is one full beat; the `visuals` beat carries the kit asset(s) that aren't the signature. The poster and the storyboard are therefore in every deck.

## Theme — matched to the poster + storyboard

The deck is themed to **match the chosen poster style and the storyboard surface**, so its background reads as one continuous canvas with the poster and the storyboard (immersive during the pitch). Set `data-theme` on the deck body:

| `data-theme` | Background | Matches |
|---|---|---|
| `light` | warm near-white (`#F4F1EA`) | poster Style A · a light storyboard |
| `cream` | cream (`#FFF6EC`) | poster Style B |
| `dark` | midnight (`#0F1514`) | poster Style C · a dark storyboard |

- The accent comes from the quest card (`--accent` + tints, injected on `<body>`); optional inline `--d-*` overrides tune the surfaces.
- The **poster beat** embeds `poster-<style>.html?embed=1` (embed mode drops the poster's page margin) and the **storyboard beat** embeds `storyboard.html?embed=1`, so both fill their frames on the deck background.

## Beat library (visual-first)

`title` · `context` (client + evidence + the problem, with contrast-stat tiles) · `insight` (seed + trends) · `audience` (segments + moment of truth) · `poster` · `storyboard` · `prototype` · `lyric` · `visuals` (secondary) · `strategy` (positioning + 4Ps + budget + pilot line) · `ask`.

> The pilot metrics + derivation chains live in `campaign-plan.html` and the proposal — **not** as a deck slide.

## Illustrations

Brand flat illustrations (inline SVG, no external assets) render on the **title** beat — the quest's key-visual motif, supplied by the card's `key_visual_svg`.

## Signature elements (the idea's carrier)

| Element | What it is | Template beat |
|---|---|---|
| Poster | the chosen full-bleed hero poster (complete) | `data-beat="poster"` |
| Storyboard | the 16:9 scene sheet (full-bleed) | `data-beat="storyboard"` |
| Prototype | 3 phone mock screens of the product | `data-beat="prototype"` |
| Lyric / anthem | a jingle sheet with a chantable hook | `data-beat="lyric"` |
| Visuals (secondary) | thumbnails of the kit asset(s) not already the signature | `data-beat="visuals"` |

## Media embeds (bonus · per storyline)

Optional generated media (song / video / image) slots into the matching beat:

| Media | Embeds into | HTML |
|---|---|---|
| Image (GPT) | **poster** beat | `<img>` |
| Video (Runway) | `visuals` / `storyboard` beat | `<video controls>` |
| Song (Suno) | **lyric** beat (the anthem) | `<audio controls>` |

The AI writes the prompts (see `references/media-prompts.md` + `templates/prompt-pack.html`); the human generates and brings files back; the AI embeds them.

## The deck template

One configurable `templates/pitch-deck.html` with all beats; `<body data-storyline="..." data-theme="light|cream|dark">` selects the order (8 beats) and the theme. Single-file, full-screen auto-scale, ←/→ nav, F fullscreen.

## Human decisions

Exactly **two** — asked **together in ONE turn**:

- Which **storyline** (S1–S5).
- Whether to attempt **bonus media** (song / video / image / none) and which generated result to use.

> Present both as a single menu; the team answers both at once — never split them into two turns.

> The **signature element** (the storyline's default), the **visual direction**, the **one-liner**, and the **deck theme** are **AI-decided**; the **poster** and **storyboard** are always included.

## Anti-patterns

- More than 8 beats, or a metrics/proof slide (the numbers live in the plan + proposal).
- A deck with no signature element (the idea is just text) — the "flat" failure mode.
- Cropping the poster, or embedding the storyboard at a size that breaks its 16:9 stage.
- Same template feel for every group — the storyline pick exists to prevent this.
- Bonus media blocking the deliverables.
- Using CDN chart/video libs (breaks single-file, double-click).
