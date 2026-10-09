---
name: showcase
description: Run the SHOWCASE stage of the Ascentium mini-hackathon quest — the team makes exactly TWO decisions (the storyline — Classic / Hero's Journey / Big Reveal / Demo / Trailer — and whether to attempt bonus media), while the AI decides the signature element, the visual direction, the one-liner, and always includes the poster. The AI then assembles a full-screen, storyline-driven Ascentium-branded pitch deck (≤ 8 slides, visual-first) and optionally writes media prompt scripts (song / video / image) for the team to generate in external tools and embed back. To create the poster itself, use the `poster` skill. Triggers: "showcase", "pitch deck", "storyline", "storyboard", "proposal showcase", "presentation", "prompt pack", "showcase".
---

# Quest Showcase — the SHOWCASE stage (AUTO)

The final stage. The **team makes two decisions — the storyline and whether to attempt bonus media**; the AI **decides everything else and builds the artifacts**. Mirrors the quest card's "★ Proposal Showcase — Showcase Report Agent (AUTO)".

## When to use

- After `plan` (reads the captures embedded in `insight-brief.html` + `campaign-plan.html`).
- Standalone: "we just want a deck" — call this skill with whatever stage HTML exists.

## Inputs

- The captures embedded in `insight-brief.html`, `campaign-plan.html`.
- **Resume (recover upstream).** If run on its own (`/showcase`), find the latest round `artifacts/Quest<ID>-*` and read those captures (plus the poster style from `campaign-plan.html`) from that folder; if the round is unambiguous, state it and continue — ask only when genuinely ambiguous. If a capture is missing, say which and ask the team to run the missing stage first. **Poster fallback:** if no `poster.html` exists in the round, build a **default poster (style A)** so the always-on poster beat is present.
- **Team decisions (only two): storyline** (S1–S5) and **bonus media** (song / video / image / none).
- **AI-decided** (never asked): the **signature element** (taken from the storyline's default), the **visual direction**, the **one-liner**, and the **poster** (always included).

## Flow (uses the `facilitation` engine)

> **Choice-first**: the storyline and the bonus-media choice are presented as **menus** — the team selects (see `facilitation` → `option-menu.md`). Everything else the AI settles directly.

1. **Storyline pick (team, 1′).** AI presents the **menu of 5 storylines** (see `references/pitch-narrative.md`): Classic / Hero's Journey / Big Reveal / Demo / Trailer — pick 1. This sets the deck's shape, the signature element, and the opening order.
2. **Bonus media (team, optional, 1′).** The team decides whether to attempt **bonus media** (song / video / image / none). If yes, the AI writes `prompt-pack.html` (copy-paste prompts for Suno / Runway / GPT); the team generates externally and brings files back.
3. **AI settles the rest (no decision).** The AI takes the **signature element** from the storyline's default, **reuses the plan's `visual_direction` + `one_liner`** (`plan` in the `campaign-plan.html` capture — do not re-derive), and **always includes the poster** in the deck (the `poster` beat, using `poster_style` from the capture — default `a` if none was picked).
4. **Build (AI, AUTO, 5′).** Assemble the signature element + the deck (`pitch-deck.html` with `data-storyline` and `data-poster="yes"`) — **hard cap 8 slides, visual-first** (fewer text blocks, more full-bleed visual).
5. **Embed (AI).** Embed any returned media files into the matching slide.
6. **Rehearse (team, 1′).** 30-second dry run + tweaks.

## HITL checkpoints (mandatory)

Exactly **two** team decisions:

- The team picks the **storyline**.
- The team decides whether to attempt **bonus media** (and, later, which generated result to use).

Everything else is AI-decided: the **signature element** (the storyline's default), the **visual direction**, the **one-liner**, and the **poster** (always included). The AI must not ask the team to choose any of these.

## Output

- `proposal.html` — **the unified proposal *viewer***: a single document with a **collapsible sidebar nav**; clicking a nav item renders that artifact's **full HTML** in the content area (embedded via `srcdoc` iframes). It contains only one authored section — the **Executive Summary** (the cover is merged into it; there is no separate cover and no "all artifacts" index). Everything else is the live artifact. This is the **primary deliverable**.
- `pitch-deck.html` — full-screen, storyline-driven deck, **≤ 8 slides, visual-first**; the poster is **always included** (`data-poster="yes"`) (see `references/pitch-narrative.md`).
- `prompt-pack.html` — bonus media prompt scripts (optional).

> The **poster** is produced by the separate `poster` skill (Create stage), since Poster is a Create-stage deliverable. The showcase **always embeds** it as the `poster` beat (default On) — no team toggle.
> **`proposal.html` is the umbrella viewer**: the Executive Summary is the one inline section; the Insight Brief, Campaign Plan, Poster, Pitch Deck and Prompt Pack are embedded as **full artifacts** (not links, not summaries).

### Building the proposal viewer

1. Fill the shell's Executive-Summary + nav placeholders in `templates/proposal.html`.
2. Keep the `{{SRCDOC_<NAME>}}` placeholders in the iframes.
3. Run the builder to inline each artifact's **full HTML** into the matching iframe:

```bash
python3 scripts/build-proposal.py --dir artifacts/Quest<ID>-<NN>/   # reads proposal.html + sibling artifacts, writes proposal.html in place
```

The builder escapes each artifact for an `srcdoc` attribute. Because `srcdoc` iframes inherit the parent origin, the viewer can auto-size each embedded artifact even from `file://` (double-click). The shell ships the auto-fit + collapse behavior; no further wiring is needed.

**Viewer rules (locked):**
- **No cover** — the Executive Summary *is* the cover.
- **No "All Artifacts" section** — the sidebar nav is the index.
- Nav click → the artifact's complete HTML renders in the content pane (vertical height auto-fits the artifact; horizontal scrollbar appears only when needed).
- The sidebar is **collapsible**.

### capture (embedded in `proposal.html`)

```html
<script type="application/json" id="capture">
{
  "gate": "showcase",
  "quest": "A",
  "storyline": "classic | hero | reveal | demo | trailer",
  "include_poster": true,
  "poster_style": "a | b | c",
  "signature": "poster | storyboard | prototype | lyric",
  "visual_direction": "…",
  "one_liner": "…",
  "bonus_media": {"song": false, "video": false, "image": false},
  "tweaks": []
}
</script>
```

> Only `storyline` and `bonus_media` are **team decisions**; `include_poster` is always `true`, and `poster_style` · `signature` · `visual_direction` · `one_liner` are **AI-decided** (recorded for the record, not for a pick). The `visual_direction` + `one_liner` are **carried over from the plan** (`plan`) — not re-derived.

## Storylines (the deck shapes)

**Rule (locked): the deck is ≤ 8 slides, visual-first.** A 5-minute pitch cannot carry every detail — the deck is the headline, the artifacts are the depth. The locked core is **7 beats**; the poster is always on, so a storyline whose signature isn't the poster runs at 8.

| # | Storyline | Signature | Beats (≤8) |
|---|---|---|---|
| S1 | Classic | poster | title → context → insight → audience → poster → strategy → ask |
| S2 | Hero's Journey | storyboard | title → context → insight → audience → storyboard → strategy → ask |
| S3 | Big Reveal | poster | title → context → insight → audience → poster → strategy → ask |
| S4 | Demo | prototype | title → context → insight → audience → prototype → strategy → ask |
| S5 | Trailer | lyric | title → context → insight → audience → lyric → strategy → ask |

- **Core beats (7)**: title · context (client + evidence + problem) · insight · audience · signature (poster / storyboard / prototype / lyric) · strategy (positioning + 4Ps + budget + pilot line) · ask.
- **Poster always on**: when the signature isn't the poster, the `poster` beat is inserted after `audience` (8 slides).
- **No proof/metrics slide** — the pilot forecast + derivation chains live in `campaign-plan.html` and the proposal.
- **Retired beats** (removed to keep ≤ 8): `keyvisual` · `offering` · `moments` · `experiment` · `funnel` · `plan` · `proof`. Brand flat illustrations (inline SVG) render on `title`.

## Bonus media (prompt pack)

- Song → **Suno** · Video → **Runway Gen-3** · Image → **GPT**.
- The AI writes tailored prompts (brand name, slogan, segment, moment, colors) into `prompt-pack.html`; see `references/media-prompts.md`.
- **Media slots** are pre-placed in the deck (dashed "embed here" boxes): image → `poster`/`keyvisual`, video → `storyboard`, song → `lyric`, plus a bonus slot on `ask`. The AI replaces the matching placeholder with the real `<img>/<video>/<audio>` (relative path) when the file comes back; empty slots hide via `.media:empty`.

## Brand

All visual output uses `ascentium-brand`. The accent comes from the quest card's `accent` token (injected on each artifact's `<body>`), and the key visual from the card's `key_visual_svg` (see `quest-card.md`).

## Design notes

- Output is single-file and double-click openable. The deck and prompt pack need no tooling; the proposal viewer is assembled by one local inliner step (`scripts/build-proposal.py`) that embeds the artifacts — the *result* is still a single self-contained HTML file.
- **Sub-skills:** `sub-skills/campaign-storyboard/` builds the standalone 16:9 storyboard (`storyboard.html`) — the Hero's-Journey signature (see `sub-skills/campaign-storyboard/SKILL.md`). The deck + proposal + prompt pack themselves are built directly from `templates/pitch-deck.html` / `templates/proposal.html` / `templates/prompt-pack.html` (see `references/pitch-narrative.md` + `references/media-prompts.md`), then the proposal is inlined via `scripts/build-proposal.py`.
