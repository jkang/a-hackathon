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
| Runtime | ~2:00 (10 scenes, timed auto-advance) |
| Stage | 1000 × 562 (16:9), full-bleed inside the deck |
| Audience | 8 guilds, non-technical business managers |
| Tone | Calm, concrete, business. Show the loop, name the skills, stop at each decision. |
| Language | English only (on-screen text and narration) |
| Brand | Ascentium tokens only — orange `#FF6611`, midnight `#0F1514`, Poppins / Noto Sans SC |
| Controls | Play / Pause · Restart · Prev / Next · progress bar |

---

## 2. Global conventions

- **Scene ID** — `S1`–`S10`, played in order.
- **Timing** — `dur` is seconds; the engine auto-advances after `dur`. Host can pause anytime.
- **Copy fields** — `headline` (large), `sub` (one supporting line), `skills` (the skills/commands
  active in this scene), `decision` (the call the team makes before moving on).
- **Image slot** — `IMG-xx`, resolved against the manifest in section 5. Every slot is optional:
  a scene with no slot renders headline-only.
- **Transitions** — default cross-fade 0.35s; the engine may add a subtle rise on the headline.
- **No inventing numbers** — any figure on screen must come from a real ticket or skill output.

---

## 3. Storyboard

### S1 · Title / cold open — 6s
- **Headline:** The Marketing AI Toolkit
- **Sub:** One loop. Five stages. Your team makes the calls.
- **Visual:** brand cover — Ascentium logo over `hero.png` (reuse), orange kicker.
- **Skills:** —
- **Decision:** —

### S2 · What the toolkit is — 12s
- **Headline:** One command line opens the whole loop
- **Sub:** Skills are reusable expert playbooks. Commands are the one-tap entries that run them.
- **Visual:** `IMG-01` (workspace with a command being typed) → `IMG-02` (the command list).
- **Skills:** `skills/` + `commands/` overview
- **Decision:** —

### S3 · Journey map + how Skills & Commands work — 12s
- **Headline:** One loop, five stages — with a decision at every gate
- **Sub:** `agent-reach` pulls real data, `creative-concept` builds the options,
  `poster` draws the hero image, `prove` fixes the pilot metrics, `showcase` assembles the pitch.
- **Visual:** `IMG-03` — 5-stage loop diagram with the HITL gate on each stage
  (reused from the deck's "One loop, five stages" flow).
- **Skills:** `insight` · `plan` · `poster` · `prove` · `showcase`
- **Decision:** —

### S4 · `/start A` — 10s
- **Headline:** Start the quest
- **Sub:** The toolkit reads the quest card and returns the first grounded menu. Claim a role, then go.
- **Visual:** `IMG-04` — `/start A` running and the first menu on screen.
- **Skills:** `/start`
- **Decision:** Read the quest; each member claims a lane.

### S5 · `/insight` — 14s
- **Headline:** Insight — a grounded menu, not a blank page
- **Sub:** Research first, then a shortlist of data-backed options. Pick 2–3 and the AI records your call.
- **Visual:** `IMG-05` (command + skill callout) → `IMG-06` (`insight-brief.html`).
- **Skills:** `agent-reach` · `business-research` · `audience-analysis` · `swot-analysis` · `insight`
- **Decision:** Choose 2–3 insights to build on (or add one of your own).

### S6 · `/plan` + `/poster` — 14s
- **Headline:** Plan — two concepts, one choice
- **Sub:** The AI drafts A/B concepts with markets and budget, then renders the hero poster in your chosen direction.
- **Visual:** `IMG-07` (command + skill callout) → `IMG-08` (`campaign-plan.html`) → `IMG-09` (`poster.html`).
- **Skills:** `creative-concept` · `opportunity-definition` · `poster` · `plan`
- **Decision:** Choose the concept, the plan, and the poster art direction.

### S7 · `/prove` — 12s
- **Headline:** Prove — the pilot metrics and the logic behind each
- **Sub:** Every target shows its benchmark, assumption, and formula. Confirm the numbers carry.
- **Visual:** `IMG-10` — `/prove` running and `proof.html` (single screen).
- **Skills:** `prove`
- **Decision:** Confirm the 3–5 pilot metrics and their reasoning.

### S8 · `/showcase` — 14s
- **Headline:** Showcase — proposal and pitch deck, ready to present
- **Sub:** The AI assembles everything into one report and a deck. Read it, adjust, approve before you submit.
- **Visual:** `IMG-11` — `/showcase` running, `proposal.html` and `pitch-deck.html`.
- **Skills:** `showcase`
- **Decision:** Approve the proposal and pitch.

### S9 · The loop you actually run — 10s
- **Headline:** The AI proposes. Your team decides. The AI executes.
- **Sub:** Same three steps at every gate: a grounded menu, a team choice, then the build.
- **Visual:** none — three-step HTML recap (menu → choose → execute).
- **Skills:** —
- **Decision:** —

### S10 · Close — 8s
- **Headline:** Your Facilitator walks the loop with you
- **Sub:** Stuck on a command or a choice? Raise a hand — one Facilitator per guild keeps it moving.
- **Visual:** `IMG-12` — a Facilitator beside a guild.
- **Skills:** —
- **Decision:** —

---

## 4. Full run-through (copy block)

For convenience when writing on-screen text, the scenes in reading order:

1. The Marketing AI Toolkit — one loop, five stages, your team makes the calls.
2. One command line opens the whole loop — skills are playbooks, commands are the entries.
3. One loop, five stages, with a decision at every gate.
4. `/start A` — read the quest, claim a role.
5. `/insight` — a grounded menu; pick 2–3 insights.
6. `/plan` + `/poster` — two concepts; choose the plan and the art direction.
7. `/prove` — pilot metrics and the logic behind each; confirm the numbers.
8. `/showcase` — proposal and deck; approve before submitting.
9. The AI proposes, your team decides, the AI executes.
10. Your Facilitator walks the loop with you.

---

## 5. Image manifest

All files go in `Hackathon-Design/hostdeck/assets/video/`, referenced relatively as
`assets/video/<filename>`. Preferred format: PNG, sRGB, 2× (retina). If a file is missing,
the engine shows the slot's placeholder label so the deck still runs.

| ID | Scene | What it shows | Type | Source | Suggested size | Filename |
|---|---|---|---|---|---|---|
| IMG-01 | S2 | OpenCode workspace with a command being typed | screenshot | NEW | 1800×1000 | `img-01.jpg` |
| IMG-02 | S2 | The command list / palette (8 commands) | screenshot | NEW | 1800×1000 | `img-02.jpg` |
| IMG-03 | S3 | 5-stage loop diagram with the HITL gate per stage | diagram | REUSE (deck flow at `host-deck.html` L517–569) | 1800×1000 | `img-03.jpg` |
| IMG-04 | S4 | `/start A` running + first grounded menu | screenshot | NEW | 1800×1000 | `img-04.jpg` |
| IMG-05 | S5 | `/insight` running + skill callout | screenshot | NEW | 1800×1000 | `img-05.png` |
| IMG-06 | S5 | `insight-brief.html` result | screenshot | NEW | 1800×1000 | `img-06-insight-brief.png` |
| IMG-07 | S6 | `/plan` running + skill callout | screenshot | NEW | 1800×1000 | `img-07-plan-cmd.png` |
| IMG-08 | S6 | `campaign-plan.html` (A/B) result | screenshot | NEW | 1800×1000 | `img-08-campaign-plan.png` |
| IMG-09 | S6 | `poster.html` hero result | screenshot | NEW | 1400×1000 | `img-09-poster.png` |
| IMG-10 | S7 | `/prove` running + `proof.html` result | screenshot | NEW | 1800×1000 | `img-10-proof.png` |
| IMG-11 | S8 | `/showcase` running + `proposal.html` / `pitch-deck.html` | screenshot | NEW | 1800×1000 | `img-11-showcase.png` |
| IMG-12 | S10 | A Facilitator beside a guild | photo | NEW (or reuse a team/venue shot) | 1400×1000 | `img-12-facilitator.png` |

**Reused, no file needed:** Ascentium logo (already inline in the deck) and `hero.png`
(already in `Hackathon-Design/assets/`).

**Notes**
- IMG-03 may be a fresh screenshot of the deck's own journey-map slide if you prefer a
  matching look; otherwise a clean standalone version of the same diagram.
- IMG-06 / IMG-08 / IMG-09 / IMG-10 / IMG-11 can be captured directly from the checked-in
  `demo-examples/QuestA-v2/*.html` files.
- Keep screenshots free of private tokens, account IDs, or local file paths.

---

## 6. Status

- [ ] Images IMG-01 … IMG-12 supplied
- [ ] Player built into `host-deck.html` (Phase B)
- [ ] Browser check passed (Phase C)

---

## 7. Player contract (Phase B spec)

The build adds a self-contained scene engine to `host-deck.html`. No external libraries.

**Markup** — one container inside slide `01`, replacing the `.video-ph` block:

```
<section class="slide demo" data-sec="1">
  <div class="demo-stage" id="toolkitDemo"> … scenes injected from JSON … </div>
</section>
```

**Scene data** — a JS array of objects mirroring section 3: `{ id, dur, eyebrow, headline, sub,
img, imgAlt, skills[], decision }`. Copy is data, not markup, so the script stays editable.

**Engine behaviour**
- Auto-advances on `dur`; cross-fades scenes; progress bar fills across the full runtime.
- Controls: Play/Pause, Restart, Prev, Next; Space toggles, ←/→ step, R restarts, F fullscreen.
- Auto-plays when slide `01` becomes active; pauses when the slide changes.
- Missing image → render the `IMG-xx` placeholder label instead of a broken image.
- Timer keeps running only while the slide is visible.

**Brand rules** — colours, fonts, radius, and spacing come from the existing `:root` tokens.
No new palettes, no decorative side bars.

**Deck integration** — reuse the deck's existing `show()`/`fit()`/rail logic; the demo is
one slide, so deck navigation, the rail, and page count stay unchanged.
