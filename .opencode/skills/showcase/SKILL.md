---
name: showcase
description: Run the SHOWCASE gate of the Ascentium mini-hackathon quest — the team picks a storyline (Classic / Hero's Journey / Big Reveal / Demo / Trailer) and a signature element (poster / storyboard / prototype / lyric), the AI assembles a full-screen, storyline-driven Ascentium-branded pitch deck, and optionally writes media prompt scripts (song / video / image) for the team to generate in external tools and embed back. To create the poster itself, use the `poster` skill. Triggers: "showcase", "pitch deck", "storyline", "storyboard", "proposal showcase", "presentation", "prompt pack", "quest showcase".
---

# Quest Showcase — the SHOWCASE gate (AUTO)

The final gate. The **team picks the storyline + signature element**; the AI **builds the artifacts**. Mirrors the quest card's "★ Proposal Showcase — Showcase Report Agent (AUTO)".

## When to use

- After `prove` (needs `insight.yaml` + `plan.yaml` + `metrics.yaml`).
- Standalone: "we just want a deck" — call this skill with whatever YAML exists.

## Inputs

- `insight.yaml`, `plan.yaml`, `metrics.yaml`.
- Team choices: **storyline** (S1–S5), **include the poster?** (yes/no), **signature element**, **visual direction**, and **one-liner**.

## Flow (uses the `facilitation` engine)

> **Choice-first**: storyline, poster on/off, and visual direction are all presented as **menus** — the team selects (see `facilitation` → `option-menu.md`).

1. **Storyline pick (team, 1′).** AI presents the **menu of 5 storylines** (see `references/pitch-narrative.md`): Classic / Hero's Journey / Big Reveal / Demo / Trailer — pick 1. This sets the deck's shape and signature element.
2. **Poster choice (team, 1′).** Decide whether the **campaign poster** appears in the deck. If yes, the `poster` beat is included (inserted after the key visual for storylines that don't already have it); if no, it is omitted. (The poster itself is produced by the separate `poster` skill in the Plan stage.)
3. **Direction + one-liner (team, 1′).** Visual direction (AI offers 2–3) + the single ask line.
4. **Build (AI, AUTO, 5′).** Assemble the signature element + the deck (`pitch-deck.html` with `data-storyline` and `data-poster`).
5. **Bonus media (team, optional).** If the team wants a song / video / image, the AI writes `prompt-pack.html` (copy-paste prompts for Suno / Runway / GPT); the team generates externally and brings files back.
6. **Embed (AI).** Embed returned files into the matching slide.
7. **Rehearse (team, 1′).** 30-second dry run + tweaks.

## HITL gates (mandatory)

- The team picks the storyline.
- The team decides **whether to include the poster**.
- The team picks the signature element (if different from the storyline default).
- The team picks the visual direction and the one-liner.
- The team decides whether to attempt bonus media and which result to use.
The AI must not choose these.

## Output

- `proposal.html` — **the complete unified proposal**: a single navigable document (sidebar nav) that aggregates the whole case — cover + executive summary + insight + plan/offer + poster + proof/metrics + an index linking every artifact. This is the **primary deliverable**.
- `pitch-deck.html` — full-screen, storyline-driven deck; poster included or not per the team's choice (`data-poster`) (see `references/pitch-narrative.md`).
- `prompt-pack.html` — bonus media prompt scripts (optional).

> The **poster** is produced by the separate `poster` skill ((Create stage)), since Poster is a Create-stage deliverable. The showcase **optionally embeds** it as the `poster` beat — the team decides whether it appears.
> **`proposal.html` is the umbrella**: the deck is one view; the proposal binds all HTML into one proposal package (unified-report style).

### capture

```yaml
showcase:
  quest: A | B
  storyline: classic | hero | reveal | demo | trailer
  include_poster: true | false
  signature: poster | storyboard | prototype | lyric
  visual_direction: "..."
  one_liner: "..."
  bonus_media: {song: bool, video: bool, image: bool}
  tweaks: [...]
```

## Storylines (the deck shapes)

| # | Storyline | Signature | Beats |
|---|---|---|---|
| S1 | Classic | poster | title → problem → insight → keyvisual → poster → strategy → moments → experiment → budget → funnel → proof → ask |
| S2 | Hero's Journey | storyboard | title → problem → storyboard → keyvisual → insight → moments → budget → proof → ask |
| S3 | Big Reveal | poster | title → problem → keyvisual → poster → strategy → proof → ask |
| S4 | Demo | prototype | title → problem → prototype → experiment → budget → proof → ask |
| S5 | Trailer | lyric | title → problem → lyric → funnel → proof → ask |

Beat library: title · problem · insight · keyvisual · poster · storyboard · prototype · lyric · strategy (positioning + 4Ps) · moments (timeline) · experiment (treatment vs control) · budget (bars) · funnel · proof (KPIs + bars + Go/No-Go) · ask. Brand flat illustrations (inline SVG) render on `title` + `keyvisual`.

## Bonus media (prompt pack)

- Song → **Suno** · Video → **Runway Gen-3** · Image → **GPT**.
- The AI writes tailored prompts (brand name, slogan, segment, moment, colors) into `prompt-pack.html`; see `references/media-prompts.md`.
- **Media slots** are pre-placed in the deck (dashed "embed here" boxes): image → `poster`/`keyvisual`, video → `storyboard`, song → `lyric`, plus a bonus slot on `ask`. The AI replaces the matching placeholder with the real `<img>/<video>/<audio>` (relative path) when the file comes back; empty slots hide via `.media:empty`.

## Brand

All visual output uses `ascentium-brand`. Quest A accent = orange; Quest B accent = teal.

## Design notes

- Single-file, double-click openable, no build step.
- Sub-skills: `ref-palette-slide`, `html-ppt-generator`.
- The deck is **configurable** (`data-storyline`), so 10 groups can present the same content in 5 different shapes.
