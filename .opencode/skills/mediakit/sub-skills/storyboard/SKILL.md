---
name: storyboard
description: Build the campaign's standalone 16:9 STORYBOARD — an immersive dark, single-file HTML that presents the fan journey as ONE 6-panel storyboard sheet. By DEFAULT it renders the six panels as an inline SVG design draft (self-contained, no external image needed) and embeds a copyable "one complete prompt" the team can take to Kimi / GPT for a richer rendered sheet (which, when brought back, replaces the draft). Part of the `mediakit` stage; the pitch deck embeds it and the proposal shows it as a panel. Triggers: "storyboard", "storyboard html", "16:9 storyboard", "fan journey sheet", "build the storyboard", "storyboard draft".
---

# Storyboard — the standalone 16:9 viewer

Build the campaign's **storyboard**: a single self-contained HTML that presents the fan journey as **one 6-panel storyboard sheet** on a **16:9** screen. It is the Hero's-Journey signature; the pitch deck's `storyboard` beat embeds this file, and the proposal shows it as a panel.

> **Default output = an inline SVG design draft.** The skill renders the six panels itself as a schematic SVG sheet — so the storyboard is produced **out of the box, with no external image**. It also emits **one complete prompt** the team can take to **Kimi / GPT** to generate a richer, rendered 6-panel sheet; when that file comes back it **replaces** the SVG draft.

## When to use

- In the **`mediakit` stage** (after the poster style is picked), or whenever a standalone storyboard is requested.
- Standalone: "make a storyboard for this campaign".

## Inputs

- **The campaign** (from the `campaign-plan.html` capture): `plan` → `name` · `slogan` · `visual_direction` · `one_liner`, plus the selected segments + moment of truth.
- **The journey steps** — six `{ n · label · headline · scene }` items (Attract / Tease / Convert / Amplify / Belong / Deepen). If absent, the six default labels are used. `headline` is the panel caption; `scene` is a one-line description for the prompt (and the draft).
- **Optional rendered sheet** — `media/storyboard/storyboard-sheet` (`.png`/`.jpg`). When present it is embedded; when absent the SVG draft is rendered.

## Flow

1. **Write the spec** `media/storyboard/storyboard.json` (see `references/storyboard-method.md` + `templates/storyboard.example.json`).
2. **Build** with `scripts/build-storyboard.py` — with no `board` image it renders the **SVG design draft**; with a `board` image it embeds the rendered sheet. Either way it writes **`storyboard.html`** at the round root and embeds the **upgrade prompt**.
3. **Hand off** — the pitch deck embeds `storyboard.html`; the proposal shows it as a **Storyboard** panel. Tell the team they can paste the built-in prompt into **Kimi / GPT** for a richer sheet and bring it back to swap in.

```bash
python3 .opencode/skills/mediakit/sub-skills/storyboard/scripts/build-storyboard.py \
  --dir artifacts/Quest<ID>-<NN>
# defaults: --spec <dir>/media/storyboard/storyboard.json  --frames <dir>/media/storyboard
#           --out <dir>/storyboard.html  --width 1600
# add a rendered sheet later: drop media/storyboard/storyboard-sheet.png and re-run
```

## Output

- **`storyboard.html`** (round root) — 16:9 stage (1280×720, auto-scaled): brandbar + title, the **6-panel sheet** (SVG draft or embedded image) on a hairline card, a step **legend**, and a **"Get a richer sheet"** overlay carrying the upgrade prompt (press **P**), **F** fullscreen, print = one landscape page. Fully self-contained.

## Quality bar

- **One sheet** — the six panels share one look (a single draft SVG, or one generated image).
- **Anchored** — the legend names the six journey steps; each panel carries its headline.
- **On-brand** — the accent comes from the quest card (`quest-card.md`); the dark surfaces are the midnight family (see `references/storyboard-method.md`).
- **Self-contained** — no external files; double-click opens; prints cleanly.

## Rules & anti-patterns

- **SVG draft by default; rendered sheet when available** — never require an external image to produce a storyboard.
- **One complete prompt** generates the rendered sheet (style + all six panels in one block) — not per-frame prompts.
- **Six panels in journey order** (3 columns × 2 rows); the script generalizes to any N for the legend.
- ❌ A light background (the dark, immersive stage is the point).
- ❌ Referencing the sheet by relative path (embed it — the output must stand alone).
- ❌ A rendered sheet that is not the one-prompt 6-panel 16:9 layout.
