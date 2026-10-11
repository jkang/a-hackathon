---
name: showcase
description: Run the SHOWCASE stage of the Ascentium mini-hackathon quest — the team makes exactly TWO decisions (the storyline — Classic / Hero's Journey / Big Reveal / Demo / Trailer — and whether to attempt bonus media), while the AI decides the signature element, the visual direction and the one-liner, and always builds a deck that uses BOTH the poster and the storyboard (from the media kit). The AI assembles a full-screen, storyline-driven pitch deck (8 beats, visual-first, themed to match the poster + storyboard background) and optionally writes media prompt scripts (song / video / image) for the team to generate in external tools and embed back. To create the poster or the storyboard itself, use the `mediakit` skill. Triggers: "showcase", "pitch deck", "storyline", "storyboard", "proposal showcase", "presentation", "prompt pack", "showcase".
---

# Quest Showcase — the SHOWCASE stage (AUTO)

The final stage. The **team makes two decisions — the storyline and whether to attempt bonus media**; the AI **decides everything else and builds the artifacts**. Mirrors the quest card's "★ Proposal Showcase — Showcase Report Agent (AUTO)".

## When to use

- After `plan` (reads the captures embedded in `insight-brief.html` + `campaign-plan.html`).
- Standalone: "we just want a deck" — call this skill with whatever stage HTML exists.

## Inputs

- The captures embedded in `insight-brief.html`, `campaign-plan.html`.
- **The media kit** — `poster-<style>.html` (+ `poster.html`) and `storyboard.html` from the `mediakit` stage.
- **Resume (recover upstream).** If run on its own (`/showcase`), find the latest round `artifacts/Quest<ID>-*` and read those captures (plus `poster_style` from the `campaign-plan.html` capture) from that folder; if the round is unambiguous, state it and continue — ask only when genuinely ambiguous. If a capture is missing, say which and ask the team to run the missing stage first. **Media-kit fallback:** if no `poster-<style>.html` exists, build a **default poster (style A)**; if no `storyboard.html` exists, build a **default storyboard (SVG design sheet)** — so the deck's visual beats are always present.
- **Team decisions (only two): storyline** (S1–S5) and **bonus media** (song / video / image / none).
- **AI-decided** (never asked): the **signature element** (taken from the storyline's default), the **visual direction**, the **one-liner**, and the **deck theme** (matched to the poster style + the storyboard surface).

## Deck — the 8-beat shape (theme-matched)

The deck's theme is **set to match the chosen poster style and the storyboard surface**, so its background reads as one continuous canvas with the poster and the storyboard — immersive during the pitch. Set `data-theme` on the deck body (`light` · `cream` · `dark`; poster A→light · B→cream · C→dark) via `{{DECK_THEME}}`; optional `{{DECK_THEME_VARS}}` adds inline `--d-*` overrides. Both the poster (`poster-<style>.html?embed=1`) and the storyboard (`storyboard.html?embed=1`) embed in **embed mode**, so each fills its frame on that background. **Both assets always appear**: the storyline's **signature** is one full-bleed beat, and the **`visuals`** beat is a compact secondary that carries the kit asset(s) not already the signature — so the poster AND the storyboard are in every deck.

| # | Beat | Carries |
|---|---|---|
| 1 | `title` | concept name + slogan + client + pilot meta |
| 2 | `context` | client + evidence + the problem (contrast-stat tiles) |
| 3 | `insight` | seed insight + market trends |
| 4 | `audience` | segments + moment of truth |
| 5 | **signature** | the storyline's peak — `poster` / `storyboard` / `prototype` / `lyric`, shown **full** |
| 6 | `visuals` | the **secondary visual** — the kit asset(s) not already the signature |
| 7 | `strategy` | positioning + 4Ps + budget + pilot line |
| 8 | `ask` | the ask |

- The **poster beat** shows the chosen style (`poster-{{POSTER_STYLE}}.html?embed=1`) **complete** (scaled to fit, never cropped) beside the campaign copy.
- The **storyboard beat** is **full-bleed 16:9** — it embeds `storyboard.html?embed=1` (embed mode hides the storyboard's own chrome).
- The **`visuals`** beat shows thumbnails: fill `{{VIS_STORYBOARD}}` when the signature isn't the storyboard, `{{VIS_POSTER}}` when it isn't the poster, both when neither is. Thumb markup:
  - poster → `<div class="vframe poster"><iframe src="poster-<style>.html?embed=1"></iframe></div><div class="vlabel">Campaign poster</div>`
  - storyboard → `<div class="vframe board"><iframe src="storyboard.html?embed=1"></iframe></div><div class="vlabel">Storyboard</div>`
  - set `{{VISUALS_LABEL}}` to what the beat shows (e.g. `the storyboard`, `the poster`, `the poster &amp; storyboard`).
- **Hard cap 8 beats.** No proof/metrics slide (the pilot forecast + derivation chains live in `campaign-plan.html` and the proposal).

## Flow (uses the `facilitation` engine)

> **Choice-first**: the storyline and the bonus-media choice are presented as **menus** — the team selects (see `facilitation` → `option-menu.md`). Everything else the AI settles directly.

1. **Storyline pick (team, 1′).** AI presents the **menu of 5 storylines** (see `references/pitch-narrative.md`): Classic / Hero's Journey / Big Reveal / Demo / Trailer — pick 1. This sets the deck's signature and opening order.
2. **Bonus media (team, optional, 1′).** The team decides whether to attempt **bonus media** (song / video / image / none). The AI **always writes `prompt-pack.html`** (copy-paste prompts for Suno / Runway / GPT / Kimi) so the prompts are ready for the team to generate externally and bring back — even if they initially chose none.
3. **AI settles the rest (no decision).** The AI takes the **signature element** from the storyline's default and **reuses the plan's `visual_direction` + `one_liner`** (`plan` in the `campaign-plan.html` capture — do not re-derive). The deck theme **matches the chosen poster style + the storyboard surface** (A→light · B→cream · C→dark); the accent comes from the quest card.
4. **Build (AI, AUTO, 5′).** Assemble the deck (`pitch-deck.html` with `data-storyline` + `data-theme`) — **8 beats, visual-first, theme-matched**. The poster + storyboard beats embed the media-kit files (relative iframes).
5. **Embed (AI).** Embed any returned media files into the matching beat.
6. **Rehearse + media (team, 1′).** 30-second dry run + tweaks. Then — because the AI **cannot generate the media itself** — remind the team to **open `prompt-pack.html`** and run each ready-made prompt in its tool: **song → Suno · video → Runway Gen-3 · image / storyboard → GPT or Kimi**; the team brings the files back, and the AI embeds them (flip the matching `bonus_media` flag, then rebuild the proposal viewer). **Write `prompt-pack.html` now if the team initially chose none.** Do **not** default straight to "ready to submit" — the media reminder comes first.

## HITL checkpoints (mandatory)

Exactly **two** team decisions:

- The team picks the **storyline**.
- The team decides whether to attempt **bonus media** (and, later, which generated result to use).

Everything else is AI-decided: the **signature element** (the storyline's default), the **visual direction**, the **one-liner**, and the **deck theme**. The AI must not ask the team to choose any of these.

## Output

- `proposal.html` — **the unified proposal *viewer***: a single document with a **collapsible sidebar nav**; clicking a nav item renders that artifact's **full HTML** in the content area (embedded via `srcdoc` iframes). It contains only one authored section — the **Executive Summary** (the cover is merged into it). Panels: Executive Summary · Insight Brief · Plan & Offering · Campaign Poster · **Storyboard** · Pitch Deck · Media Prompt Pack. This is the **primary deliverable**.
- `pitch-deck.html` — full-screen, storyline-driven deck, **8 beats, visual-first, themed to match the poster + storyboard**; embeds both (see `references/pitch-narrative.md`).
- `prompt-pack.html` — bonus media prompt scripts (always written — the ready-made Suno / Runway / GPT / Kimi prompts; the media itself is generated by the team, not the AI).

> The **poster** and **storyboard** are produced by the `mediakit` stage (the media kit). The showcase **always embeds both** (the poster as a signature or `visuals` asset; the storyboard as signature or `visuals`).

### Building the proposal viewer

1. Fill the shell's Executive-Summary + nav placeholders in `templates/proposal.html`.
2. Keep the `{{SRCDOC_<NAME>}}` placeholders in the iframes.
3. Run the builder to inline each artifact's **full HTML** into the matching iframe:

```bash
python3 .opencode/skills/showcase/scripts/build-proposal.py --dir artifacts/Quest<ID>-<NN>/   # reads proposal.html + sibling artifacts, writes proposal.html in place
```

The builder escapes each artifact for an `srcdoc` attribute. Because `srcdoc` iframes inherit the parent origin, the viewer can auto-size each embedded artifact even from `file://` (double-click). The shell ships the auto-fit + collapse behavior.

**Viewer rules (locked):**
- **No cover** — the Executive Summary *is* the cover.
- **No "All Artifacts" section** — the sidebar nav is the index.
- Nav click → the artifact's complete HTML renders in the content pane.
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
  "deck_theme": "light | cream | dark",   # matched to the poster style + storyboard surface
  "visuals": ["poster", "storyboard"],
  "visual_direction": "…",
  "one_liner": "…",
  "bonus_media": {"song": false, "video": false, "image": false},
  "tweaks": []
}
</script>
```

> Only `storyline` and `bonus_media` are **team decisions**; `include_poster` is always `true`, the deck always shows **both** the poster and the storyboard (`visuals` names the non-signature one(s)), and `poster_style` · `signature` · `visual_direction` · `one_liner` are **AI-decided** (recorded for the record, not for a pick). The `visual_direction` + `one_liner` are **carried over from the plan** (`plan`).

## Storylines (the deck shapes)

**Rule (locked): 8 beats, visual-first.** The signature is the storyline's peak; the `visuals` beat always carries the other kit asset(s), so both the poster and the storyboard appear.

| # | Storyline | Signature | Beats (8) |
|---|---|---|---|
| S1 | Classic | poster | title → context → insight → audience → poster → visuals → strategy → ask |
| S2 | Hero's Journey | storyboard | title → context → insight → audience → storyboard → visuals → strategy → ask |
| S3 | Big Reveal | poster | title → context → insight → audience → poster → visuals → strategy → ask |
| S4 | Demo | prototype | title → context → insight → audience → prototype → visuals → strategy → ask |
| S5 | Trailer | lyric | title → context → insight → audience → lyric → visuals → strategy → ask |

- **`visuals` fill**: Classic/Big Reveal → the **storyboard** thumb; Hero's Journey → the **poster** thumb; Demo/Trailer → **both** thumbs.
- **Brand flat illustrations** (inline SVG) render on `title`.

## Bonus media (prompt pack)

- Song → **Suno** · Video → **Runway Gen-3** · Image → **GPT** · Storyboard → **GPT / Kimi**.
- The AI writes tailored prompts (brand name, slogan, segment, moment, colors) into `prompt-pack.html`; see `references/media-prompts.md`.
- **Media slots** are pre-placed in the deck (dashed "embed here" boxes); the AI replaces the matching placeholder with the real `<img>/<video>/<audio>` when the file comes back.

## Brand

All visual output uses `ascentium-brand`. The accent comes from the quest card's `accent` token (injected on each artifact's `<body>`), and the key visual from the card's `key_visual_svg` (see `quest-card.md`). The **deck theme is set to match the poster style + the storyboard surface** (A→light · B→cream · C→dark), so the deck background reads as one continuous canvas with both.

## Design notes

- Output is single-file and double-click openable. The deck + prompt pack need no tooling; the proposal viewer is assembled by one local inliner step (`scripts/build-proposal.py`) that embeds the artifacts — the *result* is still a single self-contained HTML file.
- **Media kit:** the poster + storyboard are built by the `mediakit` stage (`skills/mediakit/`). The showcase reference `references/pitch-narrative.md` holds the storylines/beats; `references/media-prompts.md` + `templates/prompt-pack.html` hold the media prompts; `templates/pitch-deck.html` + `templates/proposal.html` + `scripts/build-proposal.py` build the deck + proposal.
