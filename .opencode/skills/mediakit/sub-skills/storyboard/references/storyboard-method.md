# Storyboard method — draft sheet, legend, prompt, theme

## 1. What this produces

A single self-contained HTML that presents the campaign's fan journey as **one 6-panel storyboard sheet** on a **16:9** screen. It is the Hero's-Journey signature: the pitch deck's `storyboard` beat embeds it; the proposal shows it as a panel.

Two render modes, chosen automatically:

1. **SVG design draft (default).** The skill draws the six panels itself as a schematic **inline SVG** sheet — numbered panels, step labels, a simple scene sketch, and each panel's headline. No external image required; the storyboard exists out of the box.
2. **Rendered sheet (upgrade).** If a generated image is present, it is embedded instead. The team produces it from the built-in **one complete prompt** (Kimi / GPT) and brings it back.

## 2. The inputs

1. **The journey steps** — six `{ n · label · headline · scene }` items:

| # | label | what its panel shows |
|---|---|---|
| 01 | Attract | the ambient entry point — the always-on feed / first touch |
| 02 | Tease | the hook — a creator countdown / anticipation |
| 03 | Convert | the core offer moment — the sale / conversion |
| 04 | Amplify | social proof — unboxing, UGC, word of mouth |
| 05 | Belong | the membership / community step |
| 06 | Deepen | the offline / long-term payoff (e.g. the visit) |

`headline` is the panel caption (rendered in the draft and written verbatim into the prompt); `scene` is a one-line description used by the prompt (and as the draft's scene hint).

2. **Optional rendered sheet** — `media/storyboard/storyboard-sheet` (`.png`/`.jpg`). When present it replaces the SVG draft.

## 3. The spec (`media/storyboard/storyboard.json`)

```json
{
  "quest": "B",
  "brand": "The Numbered Drop",
  "crumb": "Campaign Media Kit · Storyboard · Chengdu Panda Base",
  "h1": "How we attract the target audience",
  "accent": {"accent":"#077069","tint":"#CDE2E1","line":"#83B8B4","deep":"#043835"},
  "board": "storyboard-sheet.png",
  "width": 1600,
  "upgrade_prompt": "…optional; derived from the steps if omitted…",
  "steps": [
    {"n":"01","label":"Attract","headline":"…","scene":"…"}
  ]
}
```

- `accent` comes from the quest card (`quest-card.md`): teal for Quest B, orange for Quest A.
- `board` is **optional**; when omitted (or unresolvable) the SVG design draft is rendered. When present it is resolved relative to `--frames` (default `media/storyboard`); `.png/.jpg/.jpeg/.webp` are tried.
- `upgrade_prompt` is optional; if absent it is derived from `brand` + `accent` + the six steps.

## 4. The upgrade prompt (one complete prompt → one sheet)

The draft page carries a copyable prompt (the **"Get a richer sheet"** overlay, press **P**). Paste it **once** into **Kimi** (kimi.moonshot.cn) or **GPT**; it returns **one** 6-panel 16:9 image:

```
Create ONE 16:9 storyboard sheet: a 3-column × 2-row grid of six cinematic panels that follow
one fan's journey for the campaign "{{BRAND}}".

STYLE (all panels): brand accent {{#ACCENT}}, cinematic lighting, shallow depth of field, subtle
film grain. Keep the left third of each panel clear for a white UPPERCASE headline. High contrast,
no watermark, no logo.

Panel 1 · ATTRACT — {{scene 1}}; headline "{{verbatim}}"
Panel 2 · TEASE — {{scene 2}}; headline "{{verbatim}}"
Panel 3 · CONVERT — {{scene 3}}; headline "{{verbatim}}"
Panel 4 · AMPLIFY — {{scene 4}}; headline "{{verbatim}}"
Panel 5 · BELONG — {{scene 5}}; headline "{{verbatim}}"
Panel 6 · DEEPEN — {{scene 6}}; headline "{{verbatim}}"

Number the panels 1–6 top-left; use one consistent style across all six; keep thin gutters between
panels. 16:9. No watermark, no logo.
```

**Rules:** one prompt, one sheet (consistent look); spell out every headline verbatim; give the
brand hex; keep the left third clear; journey order `Attract → Tease → Convert → Amplify → Belong →
Deepen`. Download one image, drop it at `media/storyboard/storyboard-sheet.png`, and re-run the
build to embed it.

## 5. Layout

- One **16:9 stage (1280×720)**, auto-scaled with `transform: scale(min(w/1280, h/720))` so it fills any screen.
- Top: brandbar + title row (`h1` + `6 panels · one sheet`).
- Middle: the sheet — the SVG draft (or the embedded image) centered, `object-fit: contain` (never cropped), on a hairline card.
- Bottom: a **step legend** of six chips (`01 Attract` …).
- **P** toggles the upgrade-prompt overlay · **F** fullscreen · **Print** = one landscape page.

## 6. Theme — immersive dark

The storyboard is deliberately dark so the cinematic sheet reads with depth. Surfaces are the **midnight family**, accent comes from the quest card:

| token | value | use |
|---|---|---|
| `--sb-page` | `#050A0A` | page behind the deck |
| `--sb-deck` | `#0B1211` | deck background |
| `--sb-card` | `#101B19` | card panel |
| `--sb-line` | `#1F2E2C` | hairlines / card border |
| `--sb-cream` | `#F4EFE4` | titles |
| `--sb-text` | `#C7D4D1` | body |
| `--sb-muted` | `#8FA8A3` | crumb / meta |
| `--accent` | from the card | brandbar, legend, draft scene |

A soft **radial accent glow** sits behind the deck, giving the immersive ambience without competing with the sheet.

## 7. Quality bar & anti-patterns

- **Draft first** — a storyboard is always produced (SVG draft), never blocked on an external tool.
- **One look** — the draft uses one style across all six panels; a rendered sheet is one image from one prompt.
- **Sequenced** — the six panels tell one journey; the legend names the moment, it does not restate the headline.
- **Self-contained** — the sheet is inline SVG or an embedded data URI; no `frames/` folder dependency at view time.
- ❌ Six separately generated frames stitched with mixed styles · ❌ light background · ❌ cropped panels · ❌ relative image paths.
