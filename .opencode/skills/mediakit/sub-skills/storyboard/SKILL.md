---
name: storyboard
description: Build the campaign's standalone 16:9 STORYBOARD — a self-contained HTML that pages through the fan journey as rich SCENE cards (a cover + one page per 1–2 scenes, default 2). Each scene carries a number, title, chapter, inline-SVG scene art, a phone/UI inset, a customer pull-quote, a meta block (stage · moment · emotion · goal) and an action + source line. By default the art is drawn in-page as inline SVG, so the deliverable exists with no external image; the page also embeds one copyable prompt — a story-script brief (visuals deliberately left open) the team can take to Kimi / GPT, fed with campaign-plan.html. The theme is set from the campaign plan, not fixed. Part of the `mediakit` stage; the pitch deck embeds it and the proposal shows it as a panel. Triggers: "storyboard", "storyboard html", "16:9 storyboard", "scene sheet", "fan journey", "build the storyboard", "storyboard draft".
---

# Storyboard — the paginated 16:9 scene deck

Build the campaign's **storyboard**: a single self-contained HTML that presents the fan journey as a **16:9 paginated deck** — a **cover** plus **one page per 1–2 scenes** (default 2). Each scene is a **rich card**, not a thumbnail. It is the Hero's-Journey signature; the pitch deck's `storyboard` beat embeds this file, and the proposal shows it as a panel.

> **Default output = the storyboard HTML (paginated, inline SVG art) + one prompt.** Every scene, phone inset, quote and metric is rendered in-page, so the deliverable exists with **no external image**. The prompt (Kimi / GPT) is a **story-script brief for a richer version** — it leaves the visuals open for that tool to invent, and returns a self-contained **HTML** (never PPT), which is added as a page.

## When to use

- In the **`mediakit` stage** (after the poster style is picked), or whenever a standalone storyboard is requested.
- Standalone: "make a storyboard for this campaign".

## Inputs

- **The campaign** (from the `campaign-plan.html` capture): `plan` → `name` · `slogan` · `proposition` · `visual_direction` · `one_liner`, plus the selected segments + moment of truth.
- **The arc** — 3 chapters `{ id · name · blurb }` and 6 (up to 8) scenes `{ n · chapter · title · scene · art · ui · quote · meta · action · source }`.
- **The theme** — `theme.surface` (light | dark) + optional palette, chosen by the AI **from the campaign plan's `visual_direction`** and the chosen poster style (A → light, B → light/cream, C → dark); the accent comes from the quest card.
- **Optional** — `facts` (4 cover numbers), `cover_art` (the cover illustration kind), `per_page` (1 | 2), and a rendered `media/storyboard/storyboard-sheet.png` when the team has one.

## Flow

1. **Write the spec** `media/storyboard/storyboard.json` (see `references/storyboard-method.md` + `templates/storyboard.example.json`) — cover fields + 3 chapters + 6 rich scenes; `theme` set from the plan.
2. **Build** with `scripts/build-storyboard.py` — renders the **cover + the scene pages** as inline SVG art (or, when a `board` image resolves, a cover + a Board page) and writes **`storyboard.html`** at the round root, with the upgrade prompt.
3. **Hand off** — the pitch deck embeds `storyboard.html?embed=1`; the proposal shows it as a **Storyboard** panel. Tell the team they can paste the built-in prompt into **Kimi / GPT** (feeding it `campaign-plan.html`) for a richer story script; it returns a self-contained HTML, saved as `media/storyboard/storyboard-richer.html` → inlined as a page.

```bash
python3 .opencode/skills/mediakit/sub-skills/storyboard/scripts/build-storyboard.py \
  --dir artifacts/Quest<ID>-<NN>            # 2 scenes per page
  --per-page 1                             # or one scene per page
# defaults: --spec <dir>/media/storyboard/storyboard.json  --frames <dir>/media/storyboard
#           --out <dir>/storyboard.html
# rendered sheet later: drop media/storyboard/storyboard-sheet.png and re-run
```

## Output

- **`storyboard.html`** (round root) — 16:9 stage (1280×720, auto-scaled) with **pages**: a **cover** (campaign name · slogan · premise · hero art · 4 facts · the 3-chapter arc) then one page per **1–2 scene cards**, plus a **pager rail** (page dots, counter, prev/next) and the **"Write a richer story script"** overlay (press **P**). Keyboard ← / → to page, **F** fullscreen, print = one page per scene. Fully self-contained.
- Each **scene card** carries: number · title · chapter chip · inline-SVG scene art · phone/UI inset · customer pull-quote · meta (stage / moment / emotion / goal) · action + source.

## Quality bar

- **Both by default** — the complete paginated HTML **and** the prompt are always produced.
- **Legible, not cramped** — 1–2 scenes per page (never a squeezed grid); every scene reads at a glance.
- **Every scene** carries a number, a title, a scene, a UI inset, a quote and a meta block.
- **Themed from the plan** — `theme` follows the campaign `visual_direction`; the accent follows the card.
- **Self-contained** — inline SVG; double-click opens; prints cleanly; pages inside an iframe.

## Rules & anti-patterns

- **Pages, not one cramped sheet** — 6–8 scenes spread over pages; default 2 per page.
- **SVG art by default; a rendered sheet when available** — never require an external image to produce a storyboard.
- **One complete prompt** returns a richer story script (content + all scenes in one block); it fixes no visual direction, and asks for HTML only (never PPT).
- ❌ More than 8 scenes · ❌ a scene without title / scene / UI inset · ❌ a fixed palette that ignores the plan · ❌ cramming every scene into a single page.
- ❌ Referencing art by relative path (embed it — the output must stand alone).
