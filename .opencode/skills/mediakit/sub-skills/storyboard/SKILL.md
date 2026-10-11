---
name: storyboard
description: Build the campaign's standalone 16:9 STORYBOARD — a single self-contained HTML that presents the fan journey as ONE 16:9 scene sheet, told as 6–8 scenes grouped into 3 chapters. By DEFAULT it renders the sheet itself as an inline SVG design (scene panels with a title + a scene illustration + a phone/UI inset showing the product state), so the storyboard exists out of the box — AND it embeds one copyable prompt the team can take to Kimi / GPT for a richer rendered sheet that replaces the SVG. The theme is set from the campaign plan, not fixed. Part of the `mediakit` stage; the pitch deck embeds it and the proposal shows it as a panel. Triggers: "storyboard", "storyboard html", "16:9 storyboard", "scene sheet", "fan journey sheet", "build the storyboard", "storyboard draft".
---

# Storyboard — the 16:9 scene sheet

Build the campaign's **storyboard**: a single self-contained HTML that presents the fan journey as **one 16:9 scene sheet**, told as **6–8 scenes grouped into 3 chapters (default)**. It is the Hero's-Journey signature; the pitch deck's `storyboard` beat embeds this file, and the proposal shows it as a panel.

> **Default output = the storyboard HTML (an inline SVG design sheet) + one prompt.** The sheet is rendered in-page as SVG (scene panels: number + title + scene + a phone/UI inset), so the deliverable exists with **no external image**. The prompt (Kimi / GPT) is only for upgrading to a richer rendered sheet, which then replaces the SVG.

## When to use

- In the **`mediakit` stage** (after the poster style is picked), or whenever a standalone storyboard is requested.
- Standalone: "make a storyboard for this campaign".

## Inputs

- **The campaign** (from the `campaign-plan.html` capture): `plan` → `name` · `slogan` · `visual_direction` · `one_liner`, plus the selected segments + moment of truth.
- **The scenes** — 6 (up to 8) `{ n · chapter · title · scene · ui }` items, grouped into **3 chapters** `{ id · name }`. If absent, a default 6-scene / 3-chapter arc is used.
- **The theme** — `theme.surface` (light | dark) + optional palette, chosen by the AI **from the campaign plan's `visual_direction`**; the accent comes from the quest card.
- **Optional rendered sheet** — `media/storyboard/storyboard-sheet` (`.png`/`.jpg`). When present it replaces the SVG.

## Flow

1. **Write the spec** `media/storyboard/storyboard.json` (see `references/storyboard-method.md` + `templates/storyboard.example.json`) — 6 scenes / 3 chapters, `theme` set from the plan.
2. **Build** with `scripts/build-storyboard.py` — renders the **SVG scene sheet** (or embeds a rendered `board` if present) and writes **`storyboard.html`** at the round root, with the upgrade prompt.
3. **Hand off** — the pitch deck embeds `storyboard.html?embed=1`; the proposal shows it as a **Storyboard** panel. Tell the team they can paste the built-in prompt into **Kimi / GPT** for a richer sheet and bring it back to swap in.

```bash
python3 .opencode/skills/mediakit/sub-skills/storyboard/scripts/build-storyboard.py \
  --dir artifacts/Quest<ID>-<NN>
# defaults: --spec <dir>/media/storyboard/storyboard.json  --frames <dir>/media/storyboard
#           --out <dir>/storyboard.html
# rendered sheet later: drop media/storyboard/storyboard-sheet.png and re-run
```

## Output

- **`storyboard.html`** (round root) — 16:9 stage (1280×720, auto-scaled): brandbar + title, the **scene sheet** (inline SVG, or an embedded image) on a hairline card, and a **"Get a richer sheet"** overlay carrying the upgrade prompt (press **P**); **F** fullscreen, print = one landscape page. Fully self-contained.

## Quality bar

- **Both by default** — the complete HTML (SVG sheet) **and** the prompt are always produced.
- **6–8 scenes · 3 chapters** — a tight, readable arc (more scenes slow generation for little gain).
- **Every panel** carries a number, a title, a scene, and a UI inset.
- **Themed from the plan** — `theme` follows the campaign `visual_direction`; the accent follows the card.
- **Self-contained** — inline SVG; double-click opens; prints cleanly.

## Rules & anti-patterns

- **SVG sheet by default; rendered sheet when available** — never require an external image to produce a storyboard.
- **One complete prompt** generates a rendered sheet (style + all panels in one block).
- ❌ More than 8 scenes · ❌ a panel without title/scene/UI · ❌ a fixed palette that ignores the plan.
- ❌ Referencing the sheet by relative path (embed it — the output must stand alone).
