# Toolkit Video — Storyboard & Script

Built-in animation that replaces the `Toolkit demo — playing next` placeholder in
`host-deck.html` (slide `01 · Opening Brief`). It plays as a full-bleed 1000×562 stage
inside the deck: screenshots with captions, transitions, and a progress bar. It starts
playing as soon as the slide opens — there is no title/cover card.

This file is the single source of truth for the **content** (pages, copy, images).
The technical build is specified in section 7.

---

## 1. Video meta

| Field | Value |
|---|---|
| Title | The Marketing AI Toolkit (document title only; no on-screen title bar) |
| Runtime | ~1:45 (16 pages, timed auto-advance) |
| Stage | 1000 × 562 (16:9), full-bleed inside the deck |
| Audience | 8 guilds, non-technical business managers |
| Tone | Calm, concrete, business. Show the loop, name the skills, stop at each decision. |
| Language | English only (on-screen text) |
| Brand | Ascentium tokens only — orange `#FF6611`, midnight `#0F1514`, Poppins / Noto Sans SC |
| Controls | Play / Pause · Restart · Prev / Next · progress bar |
| Example run | Quest B (Chengdu Panda Base), session `QuestB-FullRun` |

---

## 2. Global conventions

- **Page** — `P01`–`P16`, played in order. Each page shows one image with a caption.
- **Timing** — `dur` is seconds; the engine auto-advances after `dur`. Dwell is short
  (~5–8s per page). The host can pause anytime.
- **Copy fields** — `eyebrow` (label), `head` (large), `sub` (one supporting line),
  `skills` (the skills/commands active on this page).
- **Image slot** — `IMG-xx`, resolved against the manifest in section 5. A missing file
  renders an `IMG-xx` placeholder tile.
- **Transitions** — cross-fade 0.45s; images get a slow zoom, captions fade up.
- **No inventing numbers** — any figure on screen comes from a real artifact or skill output.

---

## 3. Storyboard

Each page pairs one screenshot (right) with a caption (left). Durations are in seconds.

| Page | IMG | dur | eyebrow | head | sub | skills |
|---|---|---|---|---|---|---|
| P01 | IMG-01 | 6 | The toolkit | The toolkit sits in your editor | One workspace, pre-loaded with the quest card and the skills. | skills |
| P02 | IMG-04 | 5 | Start | Type /start and name the quest | The toolkit reads the quest card and opens the first gate. | /start |
| P03 | IMG-05 | 7 | Insight | Start the research | Choose how to open the Insight gate: live research, a fast start, or your own facts. | /insight |
| P04 | IMG-06 | 8 | Insight | Insights come as directions to build on | Six data-backed directions; the team picks two or three. | market-trends · audience-analysis |
| P05 | IMG-07 | 7 | The brief | The choice becomes the brief | Selected insights, focus bundles, and the seed insight on one screen. | insight |
| P06 | IMG-081 | 6 | Plan | Insight complete — on to the plan | Run /plan and the campaign design begins. | /plan |
| P07 | IMG-082 | 8 | Plan | Two complete plans, A and B | Each with positioning, channel mix, pilot markets, and budget. The team picks one. | creative-concept · channel-strategy · plan |
| P08 | IMG-083 | 7 | Plan | The chosen plan, written up | Concept, offer, campaign moments, budget and the pilot forecast on one page. | plan |
| P09 | IMG-091 | 5 | Poster | Plan complete — on to the poster | Run /poster and the campaign poster begins. | /poster |
| P10 | IMG-092 | 7 | Poster | Three poster styles, one choice | Full-Bleed Hero, Belonging Passport, or Midnight Minimal. The team keeps one. | poster |
| P11 | IMG-093 | 7 | Poster | The chosen poster | The selected style rendered on the Ascentium brand. | poster |
| P12 | IMG-101 | 6 | Prove | Poster complete — on to Prove | Run /prove; the pilot forecast is produced with no team decision. | /prove |
| P13 | IMG-111 | 6 | Showcase | Prove complete — on to Showcase | Run /showcase to assemble the proposal and pitch deck. | /showcase |
| P14 | IMG-112 | 7 | Showcase | Pick the storyline | Classic, Hero’s Journey, Big Reveal, Demo, or Trailer — plus optional bonus media. | showcase |
| P15 | IMG-121 | 6 | Showcase | The package is complete | Proposal, poster, proof, deck, and prompt pack — ready to submit. | showcase |
| P16 | IMG-131 | 7 | The package | One proposal, one deck, ready to pitch | A five-minute pitch, brand-compliant end to end. | showcase |

**Total: ~105s (~1:45).**

---

## 4. Full run-through (copy block)

1. The toolkit sits in your editor — one workspace, pre-loaded.
2. Type `/start` and name the quest.
3. Insight — start the research.
4. Insights come as directions; the team picks two or three.
5. The choice becomes the brief.
6. Insight complete — on to the plan.
7. Two complete plans, A and B.
8. The chosen plan, written up.
9. Plan complete — on to the poster.
10. Three poster styles, one choice.
11. The chosen poster.
12. Poster complete — on to Prove.
13. Prove complete — on to Showcase.
14. Pick the storyline.
15. The package is complete.
16. One proposal, one deck, ready to pitch.

---

## 5. Image manifest

All files live in `Hackathon-Design/hostdeck/assets/video/`, referenced relatively as
`assets/video/<filename>`. Format: JPG, sRGB. If a file is missing, the engine shows the
slot's placeholder label so the deck still runs.

| ID | Page | What it shows | Type | Filename |
|---|---|---|---|---|
| IMG-01 | P01 | OpenCode new session (toolkit workspace) | screenshot | `img-01.jpg` |
| IMG-04 | P02 | Typing `/start the Quest B - Chengdu Panda Base` | screenshot | `img-04.jpg` |
| IMG-05 | P03 | Insight gate — decision to start the research | screenshot | `img-05.jpg` |
| IMG-06 | P04 | Insights — multiple directions; pick 2–3 | screenshot | `img-06.jpg` |
| IMG-07 | P05 | `insight-brief.html` — insights selected | screenshot | `img-07.jpg` |
| IMG-081 | P06 | Plan handoff — run `/plan` | screenshot | `img-081.jpg` |
| IMG-082 | P07 | Plan · two versions — pick A or B | screenshot | `img-082.jpg` |
| IMG-083 | P08 | `campaign-plan.html` — plan selected | screenshot | `img-083.jpg` |
| IMG-091 | P09 | Poster handoff — run `/poster` | screenshot | `img-091.jpg` |
| IMG-092 | P10 | Pick the poster style A/B/C | screenshot | `img-092.jpg` |
| IMG-093 | P11 | `poster.html` — poster selected | screenshot | `img-093.jpg` |
| IMG-101 | P12 | Prove handoff — run `/prove` | screenshot | `img-101.jpg` |
| IMG-111 | P13 | Showcase handoff — run `/showcase` | screenshot | `img-111.jpg` |
| IMG-112 | P14 | Pick the showcase storyline | screenshot | `img-112.jpg` |
| IMG-121 | P15 | See the final package | screenshot | `img-121.jpg` |
| IMG-131 | P16 | Final proposal / pitch deck | screenshot | `img-131.jpg` |

**Notes**
- No reused deck assets in the video — every page is a supplied screenshot.
- Keep screenshots free of private tokens, account IDs, or local file paths.

---

## 6. Status

- [x] Images IMG-01 … IMG-131 supplied
- [x] Player built into `host-deck.html` (Phase B)
- [x] Browser check passed (Phase C)

---

## 7. Player contract (as built)

A self-contained scene engine in `host-deck.html`; no external libraries.

**Markup** — the `host-deck.html` slide `01` body holds one container. The engine adds the
`demo` / `plain` classes to the slide and removes its `sec-tag`, keeping the visitor logo:

```
<section class="slide" data-sec="1">
  <div class="logo">…</div>
  <div class="demo-stage" id="toolkitDemo"> … pages injected from SCENES … </div>
</section>
```

**Scene data** — a JS `SCENES` array of 16 objects: `{ id, dur, eyebrow, head, sub, img, alt,
skills[] }`. Copy is data, not markup. Image paths are `assets/video/<file>`. There is **no
intro/outro card** — `SCENES[0]` is IMG-01 and the video starts playing on entry.

**Engine behaviour**
- Every screenshot renders inside one fixed frame (`.dframe`, aspect `2520/1596`, white screen,
  `object-fit: contain`), so captures of different pixel sizes look uniform — the wider diagram
  and artifact shots letterbox onto the same white card.
- Auto-advances on `dur`; cross-fades pages; a progress bar fills across the full runtime.
- On-screen controls: Play/Pause, Restart, Prev, Next. Clicking the stage toggles play/pause.
- Starts on the first page and plays as soon as slide `01` becomes active; pauses when it
  changes. Implemented with a `MutationObserver` on the slide's `class`, so the deck's
  `show()` is untouched.
- Missing image → an `IMG-xx` placeholder tile renders in its place.
- The persistent on-screen title bar was removed; only the page counter (`01 / 16`) shows
  top-left. Keyboard is left to the deck (←/→ change slides, F fullscreen).

**Brand rules** — colours, fonts, radius, and spacing come from the existing `:root` tokens.
No new palettes, no decorative side bars.

**Deck integration** — the demo is one slide; the deck's `show()`/`fit()`/rail logic are
unchanged. The rail chips are clickable (jump to their section), and the prev/next pager is
shown on every slide except this full-bleed demo slide, which carries its own pager.

---

## 8. Standalone demo

`toolkit-demo.html` — the same 16-page video as a single shareable file. Every screenshot is
base64-embedded, so the file has no external dependencies and can be sent on its own.

- Generated by `build-toolkit-demo.py` (re-run it after changing the images or `SCENES`):
  it reads `SCENES` + the logo from `host-deck.html` and embeds `assets/video/*.jpg`.
- Layout: a 1000×562 stage scaled to the window, autoplay on open.
- Controls: on-screen Play/Pause · Prev · Next · Restart, plus keyboard —
  `←` / `→` step pages, `Space` play/pause, `R` restart, `F` fullscreen.
- Branded with the Ascentium logo; progress bar and page counter included.
