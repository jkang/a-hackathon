# Storyboard method — sheet, legend, theme

## 1. What this produces

A single self-contained HTML that presents the campaign's fan journey as **one 6-panel storyboard sheet** on a **16:9** screen. It is the **Hero's-Journey signature** (see `showcase/references/pitch-narrative.md`): the pitch deck's `storyboard` beat embeds it; the proposal lists it as a panel.

## 2. The two inputs

1. **The sheet** — one image (3 columns × 2 rows, six panels) produced from the showcase **prompt pack**: a **single complete prompt** that locks the style and describes all six panels in order (see `showcase/references/media-prompts.md` §3b). One image keeps the whole board consistent.
2. **The legend** — six `{ n · label }` steps mapping to the journey:

| # | label | what its panel shows |
|---|---|---|
| 01 | Attract | the ambient entry point — the always-on feed / first touch |
| 02 | Tease | the hook — a creator countdown / anticipation |
| 03 | Convert | the core offer moment — the sale / conversion |
| 04 | Amplify | social proof — unboxing, UGC, word of mouth |
| 05 | Belong | the membership / community step |
| 06 | Deepen | the offline / long-term payoff (e.g. the visit) |

Each step's panel **headline** is written verbatim into the sheet by the one prompt; the spec carries `n` + `label` (and optionally `headline`) for the legend beneath the sheet.

## 3. The spec (`media/storyboard/storyboard.json`)

```json
{
  "quest": "B",
  "brand": "The Numbered Drop",
  "crumb": "Campaign Storyboard · Chengdu Panda Base",
  "h1": "How we attract the target audience",
  "accent": {"accent":"#077069","tint":"#CDE2E1","line":"#83B8B4","deep":"#043835"},
  "board": "storyboard-sheet.png",
  "width": 1600,
  "steps": [
    {"n":"01","label":"Attract","headline":"…"},
    {"n":"02","label":"Tease","headline":"…"}
  ]
}
```

- `accent` comes from the quest card (`quest-card.md`): teal for Quest B, orange for Quest A.
- `board` is resolved relative to `--frames` (default `media/storyboard`); `.png/.jpg/.jpeg/.webp` are tried.
- `width` (default 1600) is an optional override for the embedded sheet.
- `steps` is optional — it renders the six-chip legend; the panel headlines themselves are baked into the sheet.

## 4. Layout

- One **16:9 stage (1280×720)**, auto-scaled with `transform: scale(min(w/1280, h/720))` so it fills any screen.
- Top: brandbar + title row (`h1` + `6 panels · one sheet`).
- Middle: the sheet image centered, `object-fit: contain` (never cropped), on a hairline card.
- Bottom: a **step legend** of six chips (`01 Attract` …).
- **F** fullscreen. **Print** = one landscape page (`print-color-adjust: exact`).

## 5. Theme — immersive dark

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
| `--accent` | from the card | brandbar, legend chips, range |

A soft **radial accent glow** sits behind the deck (`color-mix(accent 16%, page)`), giving the immersive ambience without competing with the sheet.

## 6. Quality bar & anti-patterns

- **One sheet, one look** — the six panels come from a single prompt, so the board reads as one piece.
- **Sequenced** — the six panels tell one journey; the legend names the moment, it does not restate the headline.
- **Self-contained** — the sheet embedded as a data URI; no `frames/` folder dependency.
- ❌ Six separately generated frames stitched with mixed styles · ❌ light background · ❌ cropped panels · ❌ relative image paths.
