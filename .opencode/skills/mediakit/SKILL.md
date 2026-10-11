---
name: mediakit
description: Run the MEDIA KIT stage of the Ascentium mini-hackathon quest — the campaign's visual-asset stage. It produces the two hero visuals: (1) the POSTER (the AI builds all three styles at once; the team's single decision is which one to keep), then (2) the STORYBOARD (the AI renders a 6-panel fan-journey sheet as an inline SVG design draft, self-contained, and emits one complete prompt the team can take to Kimi / GPT for a more visualized raster sheet). Reads the `campaign-plan.html` + `insight-brief.html` captures. One team decision only (the poster style). Triggers: "media kit", "mediakit", "campaign poster", "hero visual", "storyboard", "fan journey sheet", "make the media assets".
---

# Media Kit — the campaign's visual-asset stage

The stage that produces the campaign's **visual assets**, in order:

1. **Poster** — the AI builds **all three styles at once**; the team's **single decision** is which one to keep.
2. **Storyboard** — the AI renders the fan journey as **one 6-panel sheet**: by default an **inline SVG design draft** (self-contained, no external image), plus **one complete prompt** the team can take to **Kimi / GPT** for a more visualized raster sheet.

> This stage absorbed the old `poster` stage and the `campaign-storyboard` sub-skill (previously under `showcase`). The Showcase deck now embeds **both** assets (the poster is always on; the storyboard is the Hero's-Journey signature or a secondary visual beat).

## When to use

- After `plan` (reads the captures embedded in `insight-brief.html` + `campaign-plan.html`).
- Standalone: "make the media assets / poster / storyboard for this campaign".

## Inputs

- The `campaign-plan.html` capture — **the plan** (`plan`): name, slogan, proposition, `offer` (a one-line `summary` + exactly 3 `cards`), pilot markets, budget, and its `visual_direction` + `one_liner`.
- The `insight-brief.html` capture — audience + moment of truth.
- Quest card — `accent` (the four injected accent vars), `key_visual_svg`, `poster_styles`.
- **Resume (recover upstream).** If run on its own (`/mediakit`), find the latest round `artifacts/Quest<ID>-*` and read both captures from that folder; if the round is unambiguous, state it and continue — ask only when genuinely ambiguous. If either capture is missing, say so and ask the team to run `/plan` (or `/insight`) first.

## Flow (uses the `facilitation` engine)

> **One decision per turn.** Present the poster-style menu, then STOP and wait — the storyboard is AI-generated (no second decision).

1. **Build all three posters (AI).** Invoke the **`poster` sub-skill** (`sub-skills/poster/`): fill the shared content pack once, emit `poster-a.html` · `poster-b.html` · `poster-c.html` + the `poster.html` tab page.
2. **DECIDE (team) — the single decision.** Present the **three styles (Style A · Full-Bleed Hero / Style B · Belonging Passport / Style C · Midnight Minimal)** inline → the team **picks one** (or `+1 own`). Record it as **`poster_style` (a | b | c)** in the `campaign-plan.html` capture.
3. **Build the storyboard (AI).** Invoke the **`storyboard` sub-skill** (`sub-skills/storyboard/`): render the fan journey as one 6-panel sheet — **inline SVG design draft by default** — and emit the **one complete prompt** for a Kimi / GPT upgrade. Write `storyboard.html` at the round root.
4. **Hand off for review (no further pick).** Announce both assets; invite the team to open `poster.html` and `storyboard.html`, review them, and send feedback/changes (revise on reply). Point to `/showcase` as the step to take **once they're happy** — do **not** default straight to `/showcase`.

## Output

- `poster-a.html` · `poster-b.html` · `poster-c.html` — three standalone, clean single-poster pages (portrait, single-file).
- `poster.html` — the tab page switching between the three styles (the browsable entry point).
- `storyboard.html` — the standalone 16:9 storyboard viewer (dark immersive stage) showing the 6-panel sheet (SVG design draft by default) + the upgrade prompt.

Write into the current round folder `artifacts/Quest<ID>-<NN>/` (see `quest-card.md` → *Output layout*).

## Sub-skills

- **`sub-skills/poster/`** — the poster deliverable (three styles → the team picks one). See `sub-skills/poster/SKILL.md` + `references/poster-method.md`.
- **`sub-skills/storyboard/`** — the 6-panel fan-journey sheet (SVG design draft by default; Kimi/GPT upgrade prompt). See `sub-skills/storyboard/SKILL.md` + `references/storyboard-method.md`.

## Brand

Uses `ascentium-brand`. The accent comes from the quest card's `accent` token (orange is the brand default; teal for quests that declare it) — never a self-invented colour. The poster follows the plan's `visual_direction` + `one_liner`; the deck (later) reuses both assets with the same accent and a dark midnight baseline.
