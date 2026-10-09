---
name: campaign-storyboard
description: Assemble the campaign's standalone 16:9 STORYBOARD — an immersive dark, single-file HTML that presents the fan journey as ONE 6-panel storyboard sheet. It consumes the single sheet image (produced from the showcase prompt pack with one complete prompt) plus the campaign's journey captions, embeds the sheet as a data URI (self-contained), and writes `storyboard.html`. It is the Hero's-Journey signature artifact — the pitch deck embeds it and the proposal shows it as a panel. Triggers: "storyboard", "storyboard html", "16:9 storyboard", "fan journey sheet", "build the storyboard", "campaign storyboard".
---

# Storyboard — the standalone 16:9 viewer

Build the campaign's **storyboard**: a single self-contained HTML that presents the fan journey as **one 6-panel storyboard sheet** on a **16:9** screen. This is the Hero's-Journey signature: the pitch deck's `storyboard` beat embeds this file, and the proposal shows it as a panel.

> The sheet is generated externally from the showcase `prompt-pack.html` — **one complete prompt → one 6-panel image** (not one prompt per frame). This sub-skill **assembles** the returned sheet into the viewer and records the path.

## When to use

- In `showcase`, when the team's storyline is **Hero's Journey** (the storyboard is its signature), or whenever a standalone storyboard is requested.
- Standalone: "make a storyboard from this sheet".

## Inputs

- **The sheet image** — `media/storyboard/storyboard-sheet` (one image, six panels; `.png`/`.jpg`).
- **The campaign** (from the `campaign-plan.html` capture): `plan` → `name` · `slogan` · `visual_direction` · `one_liner`, plus the selected segments + moment of truth.
- **The journey steps** — six `{ n · label }` chips for the legend (Attract / Tease / Convert / Amplify / Belong / Deepen); the panel headlines live inside the sheet. If absent, use the six default labels.

## Flow

1. **Gather the sheet + steps.** Confirm the sheet path and the six-step order. The sheet already carries the panel headlines (written verbatim in the one prompt); the legend names the steps: `Attract → Tease → Convert → Amplify → Belong → Deepen`.
2. **Write the spec** `media/storyboard/storyboard.json` (see the schema in `references/storyboard-method.md` and `templates/storyboard.example.json`).
3. **Build** with `scripts/build-storyboard.py` — it downscales the sheet, JPEG-encodes it, embeds it as a data URI, and writes **`storyboard.html`** at the round root (self-contained).
4. **Record the path** in the showcase capture, and hand off: the pitch deck embeds `storyboard.html` on the `storyboard` beat; the proposal adds a **Storyboard** panel.

```bash
python3 .opencode/skills/showcase/sub-skills/campaign-storyboard/scripts/build-storyboard.py \
  --dir artifacts/Quest<ID>-<NN>
# defaults: --spec <dir>/media/storyboard/storyboard.json  --frames <dir>/media/storyboard
#           --out <dir>/storyboard.html  --width 1600
```

## Output

- **`storyboard.html`** (round root) — 16:9 stage (1280×720, auto-scaled), one dark stage showing the **6-panel sheet** plus a step legend, **F** fullscreen, print = one landscape page. Fully self-contained (sheet inlined as a data URI).

## Quality bar

- **One sheet** — the six panels arrive as a single image generated from one prompt; the whole board shares one look.
- **Anchored** — the legend names the six journey steps (time · place · event) the panels serve.
- **On-brand** — the accent comes from the quest card (`quest-card.md`); the dark surfaces are the midnight family (see `references/storyboard-method.md`).
- **Self-contained** — no external files; double-click opens; prints cleanly.

## Rules & anti-patterns

- **One complete prompt** generates the sheet (style + all six panels in one block) — not per-frame prompts.
- **Six panels in journey order** (3 columns × 2 rows); the script generalizes to any N for the legend.
- ❌ Six separate images stitched with mismatched styles.
- ❌ A light background (the dark, immersive stage is the point).
- ❌ Referencing the sheet by relative path (embed it — the output must stand alone).
