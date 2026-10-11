# Storyboard method — the 16:9 scene sheet

## 1. What this produces

A single self-contained HTML that presents the campaign's fan journey as **one 16:9 storyboard sheet**. The sheet is an **inline SVG generated in-page** — no external image required — so the storyboard (the deliverable) exists out of the box. The page also carries **one complete prompt** the team can take to **Kimi / GPT** for a richer, rendered sheet; if that image comes back it **replaces** the SVG.

So the default output is **both**: the storyboard HTML (SVG design sheet) **and** the prompt.

## 2. The outline — chapters + scenes (derived from the campaign)

The story is told as **6 scenes (default; up to 8), grouped into 3 chapters (default)**. Each **scene panel** is a card:

| element | what it is |
|---|---|
| **number** | the scene's order (01… ) |
| **title** | the scene's punchy line (e.g. "The pass that holds the date") |
| **scene** | a cinematic scene illustration (SVG) of that moment |
| **UI inset** | a phone / app screenshot showing the **product state at that moment** (`ui`: screen · title · lines · CTA) |

> Keep it **6–8 scenes**: more scenes make both the design sheet and the prompt slower to produce, for little extra story.

Default chapter arc (map to the campaign): **I. The Hook** (scenes 1–2) → **II. The Offer** (scenes 3–4) → **III. Belonging** (scenes 5–6). Rename the chapters to fit the campaign.

## 3. Theme — set from the campaign plan, not fixed

`theme.surface` is **`light` or `dark`**, chosen by the AI from the campaign plan's **`visual_direction`** (and the chosen poster style) — not hard-coded. Optional palette overrides:

```json
"theme": {"surface":"light", "page":"#F1ECE2", "card":"#FFFFFF", "line":"#E3DCCE",
          "title":"#16130D", "text":"#4A463D", "muted":"#8B8574"}
```

`accent` (the 4 tokens) still comes from the quest card. Any omitted key falls back to a sensible default for the surface.

## 4. The spec (`media/storyboard/storyboard.json`)

```json
{
  "quest": "A",
  "brand": "The Date-Certain Pass",
  "crumb": "Campaign Media Kit · Storyboard · Quest A",
  "h1": "From the first spark to a shared memory",
  "accent": {"accent":"#FF6611","tint":"#FFF0E7","line":"#FFD1B8","deep":"#B24000"},
  "theme": {"surface": "light"},
  "board": "storyboard-sheet.png",
  "chapters": [ {"id":"I","name":"The Hook"}, {"id":"II","name":"The Offer"}, {"id":"III","name":"Belonging"} ],
  "steps": [
    {"n":"01","chapter":"I","title":"The moment the trip feels possible",
     "scene":"an everyday family scene, a phone glowing between them",
     "ui":{"screen":"Next big memory","title":"Flights + tickets, one plan",
           "lines":["Split it month by month","Hold today's price"],"cta":"Start a plan"}}
  ]
}
```

- `board` is **optional**; when omitted (or unresolvable) the **SVG design sheet** is rendered. When present it is embedded instead (resolved relative to `--frames`, default `media/storyboard`).
- `upgrade_prompt` is optional; if absent it is derived from `brand` + `accent` + the chapters/scenes.

## 5. The upgrade prompt (one prompt → one sheet)

The page carries a copyable prompt (the **"Get a richer sheet"** overlay, press **P**). Paste it once into **Kimi** (kimi.moonshot.cn) or **GPT**; it returns **one 16:9 sheet**:

```
Create ONE 16:9 storyboard DESIGN SHEET for the campaign "{{BRAND}}".
LAYOUT: split into {{N}} vertical chapters ({{chapter names}}); each chapter stacks its scene panels;
        each panel = a cinematic scene + a small phone/UI inset (the app state at that moment).
STYLE: brand accent {{#ACCENT}}, cinematic lighting, shallow depth of field, subtle film grain; keep a
       clear left margin per panel for a bold title; one consistent style; no watermark, no logo.
Panel {{n}} · {{title}} — {{scene}}; phone inset: "{{ui.title}} / {{ui.lines}} / {{ui.cta}}"
…
16:9. No watermark, no logo.
```

Download one image, drop it at `media/storyboard/storyboard-sheet.png`, and re-run the build to embed it.

## 6. Layout (16:9 sheet)

- Sheet viewBox **1600 × 900** (16:9). Columns = chapters; each column has a **chapter header** (roman numeral + name) and its **scene cards** stacked.
- Each scene card = number badge + title + a **scene band** (gradient sky, lit skyline, foreground figures — the middle figure in the accent) + a **phone inset** (screen label · title · lines · CTA pill).
- One sheet, print = one landscape page; **F** fullscreen; the viewer auto-scales to any screen.

## 7. Quality bar & anti-patterns

- **Draft first** — a storyboard is always produced (SVG sheet); never blocked on an external tool.
- **Themed, not fixed** — surfaces come from the campaign plan (`theme`), the accent from the quest card.
- **6–8 scenes / 3 chapters** — a tight arc; every panel carries a title, a scene and a UI inset.
- **Self-contained** — the sheet is inline SVG or an embedded data URI; no `frames/` dependency at view time.
- ❌ More than 8 scenes · ❌ a panel without a title, scene, or UI inset · ❌ a fixed palette that ignores the plan · ❌ relative image paths.
