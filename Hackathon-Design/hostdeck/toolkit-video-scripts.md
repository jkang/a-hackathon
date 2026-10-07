# Toolkit Video — Storyboard & Script

Built-in animation that replaces the `Toolkit demo — playing next` placeholder in
`host-deck.html` (slide `01 · Opening Brief`). It plays as a full-bleed 1000×562 stage
inside the deck, like a short walkthrough video: headline text, screenshots, transitions,
and a progress bar.

This file is the single source of truth for the **content** (scenes, copy, images).
The technical build is specified in section 7.

---

## 1. Video meta

| Field | Value |
|---|---|
| Title | The Marketing AI Toolkit |
| Subtitle | Insight → Plan → Poster → Prove → Showcase |
| Runtime | ~2:30 (15 scenes, timed auto-advance) |
| Stage | 1000 × 562 (16:9), full-bleed inside the deck |
| Audience | 8 guilds, non-technical business managers |
| Tone | Calm, concrete, business. Show the loop, name the skills, stop at each decision. |
| Language | English only (on-screen text and narration) |
| Brand | Ascentium tokens only — orange `#FF6611`, midnight `#0F1514`, Poppins / Noto Sans SC |
| Controls | Play / Pause · Restart · Prev / Next · progress bar |

---

## 2. Global conventions

- **Scene ID** — `S1`–`S15`, played in order.
- **Timing** — `dur` is seconds; the engine auto-advances after `dur`. Host can pause anytime.
- **Copy fields** — `headline` (large), `sub` (one supporting line), `skills` (the skills/commands
  active in this scene), `decision` (the call the team makes before moving on).
- **Image slot** — `IMG-xx`, resolved against the manifest in section 5. Every slot is optional:
  a scene with no slot renders headline-only.
- **Transitions** — default cross-fade 0.35s; the engine may add a subtle rise on the headline.
- **No inventing numbers** — any figure on screen must come from a real ticket or skill output.

---

## 3. Storyboard

Each scene shows one screenshot (except S1 and S15) with a headline and one supporting line.
The example run uses Quest B (Chengdu Panda Base).

### S1 · Title / cold open — 6s
- **Headline:** The Marketing AI Toolkit
- **Sub:** One loop. Five stages. Your team makes the calls.
- **Visual:** brand cover — Ascentium logo over `hero.png` (reuse), orange kicker.
- **Skills:** — · **Decision:** —

### S2 · Where the toolkit lives — 10s
- **Headline:** The toolkit sits in your editor
- **Sub:** One workspace, pre-loaded with the quest card and the skills. No setup.
- **Visual:** `IMG-01` — OpenCode new session.
- **Skills:** `skills/` + `commands/` · **Decision:** —

### S3 · One command line — 10s
- **Headline:** Eight commands run the whole loop
- **Sub:** `/start · /insight · /plan · /poster · /prove · /showcase` — plus `/run` and `/evaluate`.
- **Visual:** `IMG-02` — the command palette.
- **Skills:** `commands/` · **Decision:** —

### S4 · The loop — 12s
- **Headline:** One loop, five stages — a decision at every gate
- **Sub:** `agent-reach` pulls real data, `creative-concept` builds options, `poster` draws the hero,
  `prove` fixes the metrics, `showcase` assembles the pitch.
- **Visual:** `IMG-03` — the five-stage journey map.
- **Skills:** `insight` · `plan` · `poster` · `prove` · `showcase` · **Decision:** —

### S5 · Kick off — 9s
- **Headline:** Type `/start` and name the quest
- **Sub:** The toolkit reads the quest card and opens the first gate.
- **Visual:** `IMG-04` — typing `/start the Quest B - Chengdu Panda Base`.
- **Skills:** `/start` · **Decision:** Read the quest; each member claims a lane.

### S6 · The first decision — 10s
- **Headline:** It answers with a decision, not a wall of text
- **Sub:** Run the research, take the fast start, or add your own angle. The team picks.
- **Visual:** `IMG-05` — the `/start` reply and its three options.
- **Skills:** `/start` · **Decision:** Choose how to open the Insight gate.

### S7 · Insight — a grounded menu — 12s
- **Headline:** Insight returns a grounded menu of options
- **Sub:** Eight findings, each with its source. The team picks two or three to build on.
- **Visual:** `IMG-06` — the market-trends menu; the team replies `2, 4, 7`.
- **Skills:** `agent-reach` · `business-research` · `audience-analysis` · `swot-analysis` · `insight`
- **Decision:** Pick 2–3 insights (or add one of your own).

### S8 · The brief — 10s
- **Headline:** The choice becomes the brief
- **Sub:** Moment of truth, seed insight, and the selected insights on one screen.
- **Visual:** `IMG-07` — `insight-brief.html`.
- **Skills:** `insight` · **Decision:** Confirm the brief; move to Plan.

### S9 · Plan — fix who and when — 10s
- **Headline:** Plan starts by fixing who and when
- **Sub:** Seven segment × moment anchors. The team picks the one that answers the insights.
- **Visual:** `IMG-08` — the Plan · Anchor menu.
- **Skills:** `creative-concept` · `opportunity-definition` · **Decision:** Choose the anchor.

### S10 · Plan — two versions — 12s
- **Headline:** Then two complete plans, A and B
- **Sub:** Positioning, offer, 4Ps, pilot, budget. The team picks one or mixes.
- **Visual:** `IMG-09` — Plan · two versions (A "Belong Anywhere" / B "Passport to Chengdu").
- **Skills:** `plan` · **Decision:** Pick A, B, or a mix.

### S11 · Poster — 10s
- **Headline:** The hero poster, in three styles
- **Sub:** Same message, three art directions. The team keeps one.
- **Visual:** `IMG-10` — `poster.html`.
- **Skills:** `poster` · **Decision:** Keep one poster style.

### S12 · Prove — 11s
- **Headline:** Prove — pilot metrics with the logic behind each
- **Sub:** Benchmark → assumption → formula for every target.
- **Visual:** `IMG-11` — `proof.html` written, plus the recap.
- **Skills:** `prove` · **Decision:** Confirm the pilot metrics and their reasoning.

### S13 · Showcase — the package — 11s
- **Headline:** Showcase assembles the package
- **Sub:** Proposal, poster, proof, and deck — then a final check before submitting.
- **Visual:** `IMG-12` — the package summary, one-line pitch, and Converge · Final check.
- **Skills:** `showcase` · **Decision:** Confirm and submit, or request a change.

### S14 · One report, one deck — 11s
- **Headline:** One report, one deck, ready to pitch
- **Sub:** A five-minute pitch, brand-compliant end to end.
- **Visual:** `IMG-13` — the final proposal / pitch deck.
- **Skills:** `showcase` · **Decision:** —

### S15 · Close — 7s
- **Headline:** Your Facilitator walks the loop with you
- **Sub:** Stuck on a command or a choice? Raise a hand — one Facilitator per guild keeps it moving.
- **Visual:** none — HTML closing card.
- **Skills:** — · **Decision:** —

---

## 4. Full run-through (copy block)

1. The Marketing AI Toolkit — one loop, five stages, your team makes the calls.
2. The toolkit sits in your editor — pre-loaded, no setup.
3. Eight commands run the whole loop.
4. One loop, five stages, with a decision at every gate.
5. Type `/start` and name the quest.
6. It answers with a decision, not a wall of text.
7. Insight returns a grounded menu; the team picks two or three.
8. The choice becomes the brief.
9. Plan starts by fixing who and when.
10. Then two complete plans, A and B.
11. The hero poster, in three styles.
12. Prove — pilot metrics with the logic behind each.
13. Showcase assembles the package.
14. One report, one deck, ready to pitch.
15. Your Facilitator walks the loop with you.

---

## 5. Image manifest

All files live in `Hackathon-Design/hostdeck/assets/video/`, referenced relatively as
`assets/video/<filename>`. Format: JPG, sRGB. If a file is missing, the engine shows the
slot's placeholder label so the deck still runs.

| ID | Scene | What it shows | Type | Filename |
|---|---|---|---|---|
| IMG-01 | S2 | OpenCode new session (toolkit workspace) | screenshot | `img-01.jpg` |
| IMG-02 | S3 | Command palette — the eight commands | screenshot | `img-02.jpg` |
| IMG-03 | S4 | "One loop, five stages" journey map | diagram | `img-03.jpg` |
| IMG-04 | S5 | Typing `/start the Quest B - Chengdu Panda Base` | screenshot | `img-04.jpg` |
| IMG-05 | S6 | `/start` reply — how to open the Insight gate | screenshot | `img-05.jpg` |
| IMG-06 | S7 | Insight market-trends menu (team picks 2,4,7) | screenshot | `img-06.jpg` |
| IMG-07 | S8 | `insight-brief.html` — insights selected | screenshot | `img-07.jpg` |
| IMG-08 | S9 | Plan · two versions — pick A or B | screenshot | `img-08.jpg` |
| IMG-09 | S10 | continue with the posters | screenshot | `img-09.jpg` |
| IMG-10 | S11 | `poster.html` — three styles + hero | screenshot | `img-10.jpg` |
| IMG-11 | S12 | `proof.html` written + Pick up the showcase story line | screenshot | `img-11.jpg` |
| IMG-12 | S13 | Showcase package + final check | screenshot | `img-12.jpg` |
| IMG-13 | S14 | Final proposal / pitch deck | screenshot | `img-13.jpg` |

**Reused, no file needed:** Ascentium logo (already inline in the deck) and `hero.png`
(already in `Hackathon-Design/assets/`).

**Alternates on disk (not in the manifest):**
- `img-071.jpg` — internal "thinking" screen for the anchor menu. Rough; not recommended.
- `img-101.jpg` — Poster · Style decision menu (pick A/B/C). Can slot in **before** `IMG-10`
  as a "Poster — pick a style" scene if a 16th scene is wanted.

**Notes**
- Keep screenshots free of private tokens, account IDs, or local file paths.
- Use `demo-examples/QuestA-v2/*.html` if a Quest A variant is ever needed.

---

## 6. Status

- [x] Images IMG-01 … IMG-13 supplied
- [x] Player built into `host-deck.html` (Phase B)
- [x] Browser check passed (Phase C)

---

## 7. Player contract (Phase B spec)

Built. A self-contained scene engine was added to `host-deck.html`; no external libraries.

**Markup (as built)** — the old `.video-ph` body in slide `01` was replaced by one container.
The engine then adds the `demo` / `plain` classes to the slide and removes its `sec-tag`, so the
visitor logo stays but the slide content is the full-bleed stage:

```
<section class="slide" data-sec="1">
  <div class="logo">…</div>
  <div class="demo-stage" id="toolkitDemo"> … scenes injected from SCENES … </div>
</section>
```

**Scene data** — a JS `SCENES` array of objects mirroring section 3: `{ id, dur, layout, eyebrow,
head, sub, img, alt, skills[] }`. Copy is data, not markup. Image paths are `assets/video/<file>`;
`S1` (intro) uses `../assets/hero.png`; `S15` (outro) has no image.

**Engine behaviour**
- Auto-advances on `dur`; cross-fades scenes; a progress bar fills across the full runtime.
- On-screen controls: Play/Pause, Restart, Prev, Next. Clicking the stage toggles play/pause.
- Auto-plays (from the first scene) when slide `01` becomes active; pauses when it changes.
  Implemented with a `MutationObserver` on the slide's `class`, so the deck's `show()` is untouched.
- Missing image → an `IMG-xx` placeholder tile renders in its place; the deck still runs.
- Keyboard is left to the deck (←/→ change slides, F fullscreen) so the host is never trapped;
  scene stepping is via the on-screen buttons.

**Brand rules** — colours, fonts, radius, and spacing come from the existing `:root` tokens.
No new palettes, no decorative side bars.

**Deck integration** — reuse the deck's existing `show()`/`fit()`/rail logic; the demo is
one slide, so deck navigation, the rail, and page count stay unchanged.
