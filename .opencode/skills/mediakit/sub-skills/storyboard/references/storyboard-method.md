# Storyboard method — the paginated 16:9 scene deck

## 1. What this produces

A single self-contained HTML that presents the campaign's fan journey as a **16:9 paginated deck**:

- **Cover page** — campaign name · slogan · premise · hero art · 4 hard facts · the 3-chapter arc.
- **Scene pages** — one page per **1–2 scenes** (default 2), each a **rich card**.
- **Board page** (optional) — when a rendered sheet image is supplied it is embedded on its own page.

Every scene is drawn in-page as **inline SVG art**, so the storyboard (the deliverable) exists out of the box with no external image. The page also carries **one complete prompt** the team can take to **Kimi / GPT** for a richer rendered sheet; if that image comes back it is added as a Board page.

## 2. The outline — chapters + scenes (derived from the campaign)

The story is told as **6 scenes (default; up to 8), grouped into 3 chapters (default)**. Each **scene card** carries a full block:

| element | what it is | filled from |
|---|---|---|
| **number** | the scene's order (01 …) | spec |
| **title** | the scene's punchy line | spec |
| **chapter chip** | `II · The Offer` | `chapters[]` |
| **scene art** | a cinematic illustration of that moment (inline SVG) | `art` **kind** (see §3) |
| **phone / UI inset** | the app screenshot showing the **product state at that moment** (`ui`: screen · title · lines · CTA) | `ui` |
| **pull-quote** | the fan's voice in that moment | `quote` |
| **meta block** | **Stage · Moment · Emotion · Goal** | `meta` |
| **action + source** | what the campaign does there, and the evidence | `action` · `source` |

> Keep it **6–8 scenes**. Every scene must carry a title, a scene, and a UI inset — a bare thumbnail is a defect.

Default chapter arc (map to the campaign): **I. The Hook** (scenes 1–2) → **II. The Offer** (scenes 3–4) → **III. Belonging** (scenes 5–6). Rename the chapters to fit the campaign, and give each a `blurb` for the cover.

## 3. Scene art — kinds (inline SVG, campaign-aware)

`art` picks one of the built-in scene illustrations, all drawn at **viewBox `0 0 800 420`**:

| kind | scene |
|---|---|
| `cam` | the always-on live cam watched at home (monitor + household) |
| `plan` | planning the trip (phone map + flight path + visa stamp) |
| `adopt` | adoption (numbered family certificate + confetti) |
| `home` | the household decision (family around a tablet) |
| `drop` | the seasonal collectible drop (numbered cards + sparkles) |
| `meet` | the in-person meeting (panda + family + camera flashes + bamboo) |
| `spotlight` | fallback — a centred panda |

Pick the kind that matches the moment. The cover uses `cover_art` (default: scene 01's kind).

## 4. Theme — set from the campaign plan, not fixed

`theme.surface` is **`light` or `dark`**, chosen by the AI from the campaign plan's **`visual_direction`** (and the chosen poster style) — not hard-coded. Optional palette overrides:

```json
"theme": {"surface":"light", "page":"#F1ECE2", "card":"#FFFFFF", "line":"#E3DCCE",
          "title":"#16130D", "text":"#4A463D", "muted":"#8B8574"}
```

`accent` (the 4 tokens) still comes from the quest card. Any omitted key falls back to a sensible default for the surface.

> **Match the poster style.** Set `theme.surface` to the chosen poster style's surface (A → light, B → light/cream, C → dark) so the **showcase deck** can inherit the same background and the pitch stays immersive.

## 5. The spec (`media/storyboard/storyboard.json`)

```json
{
  "quest": "B",
  "brand": "The Panda Family",
  "crumb": "Campaign Media Kit · Storyboard · Quest B",
  "h1": "From watching the cam to meeting the family",
  "slogan": "Adopt the family. Collect the fun.",
  "premise": "One or two sentences on the arc.",
  "one_liner": "The world's most-loved animal — now part of your family.",
  "accent": {"accent":"#077069","tint":"#CDE2E1","line":"#83B8B4","deep":"#043835"},
  "theme": {"surface": "light"},
  "per_page": 2,
  "cover_art": "meet",
  "facts": [{"n":"$161.8B","c":"character / entertainment licensing market"}],
  "board": "",
  "chapters": [{"id":"I","name":"The Hook","blurb":"…"}],
  "steps": [
    {"n":"01","chapter":"I","art":"cam","title":"A million viewers, no way to belong",
     "scene":"a household watching the always-on panda cam together",
     "quote":"We've watched them for years. I just wish there was a way to be part of it.",
     "action":"Turn ambient affection into a membership front door",
     "source":"iPanda · ~9.5M subscribers, >40% outside China",
     "meta":{"stage":"Trigger","moment":"The always-on cam","emotion":"Warm, habitual affection","goal":"Open a door"},
     "ui":{"screen":"The cam","title":"You have watched them for years","lines":["Now meet the family that already feels yours"],"cta":"Join the family"}}
  ]
}
```

- `board` is **optional**; when omitted (or unresolvable) the **inline SVG pages** are rendered. When present it is embedded as a **Board page** (resolved relative to `--frames`, default `media/storyboard`).
- `per_page` (1 | 2) sets the scene density; `--per-page` on the CLI overrides it.
- `facts` (up to 4) fills the cover strip; `cover_art` picks the cover illustration.
- `upgrade_prompt` is optional; if absent it is derived from `brand` + `accent` + the chapters/scenes.

## 6. The upgrade prompt (a richer STORY SCRIPT — visuals left open)

The page carries a copyable prompt (the **"Write a richer story script"** overlay, press **P**).

**What it is:** a **story-script brief** — the narrative to be realised, **not a visual specification**. It tells the other tool *what happens* scene by scene (beats, on-screen copy, fan quotes, the four fields, the action + evidence) and explicitly leaves **art direction, layout, palette and typography to that tool**. Prescribing the visuals here would only cap a stronger tool.

**Input hint (in the note and in the prompt):** best results come from feeding the target tool **`campaign-plan.html`** first (its capture holds name, slogan, proposition, offer, audiences, moments, budget); add **`insight-brief.html`** for audience + market context.

**Format:** the prompt asks for **one self-contained `.html`** — *HTML only; never PPT / PPTX / Keynote / Slides or any slide-deck export* (those may not open on the room's machines). Save the answer as `media/storyboard/storyboard-richer.html` and re-run the build — it is inlined as a **page** in the same deck.

## 7. Layout (16:9 pages)

- Deck **1280 × 720**, auto-scaled to any screen; keyboard ← / → to page, **F** fullscreen, print = **one page per scene**.
- **Cover** — name · slogan · premise · hero art · 4 facts · the arc cards.
- **Scene page (2-up)** — two cards side by side: title row, art band (`800/420`), caption, quote, meta row, action + source footer.
- **Scene page (1-up)** — one card: art on the left, and a wider text column (title · scene · quote · 2×2 meta · action + source) on the right.
- **Board page** — the rendered sheet, centred.

## 8. Quality bar & anti-patterns

- **Draft first** — a storyboard is always produced (inline SVG pages); never blocked on an external tool.
- **Legible, not cramped** — 1–2 scenes per page; never squeeze 6 scenes into one sheet.
- **Themed, not fixed** — surfaces come from the campaign plan (`theme`), the accent from the quest card.
- **Rich scenes** — number, title, art, UI inset, quote, meta, action + source.
- **Self-contained** — inline SVG or an embedded data URI; no `frames/` dependency at view time.
- ❌ More than 8 scenes · ❌ a scene without a title, scene, or UI inset · ❌ a fixed palette that ignores the plan · ❌ relative image paths.
