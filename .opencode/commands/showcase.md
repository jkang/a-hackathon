---
description: Run only the SHOWCASE gate (storyline → deck + prompt-pack).
agent: facilitator
---
Run **only the SHOWCASE gate**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another gate.** (See `facilitator` → *Turn discipline*.)

Use the `showcase` skill with `facilitation` (option menu). Requires the captures embedded in `insight-brief.html` + `campaign-plan.html` + `proof.html` (+ the poster from the `poster` skill).

**This gate has exactly TWO team decisions — the storyline and bonus media.** The AI decides everything else.

1. **Storyline** — present the 5-storyline menu (Classic / Hero's Journey / Big Reveal / Demo / Trailer); the team picks 1.
2. **Bonus media** — the team decides whether to attempt song / video / image (or none).
3. **AI settles the rest (no decision)** — the **signature element** (the storyline's default), the **visual direction**, the **one-liner**, and the **poster** (**always included** — `data-poster="yes"`; style = the final `poster` skill pick, default A).
4. Build the deck (`data-storyline` + `data-poster="yes"`).
5. If bonus media was chosen, write `prompt-pack.html` (Suno / Runway / GPT prompts) and embed returned files.
6. Write into the current round folder `artifacts/Quest<ID>-<NN>/`: `proposal.html` (the unified proposal viewer) + `pitch-deck.html` + `prompt-pack.html`; the showcase capture is embedded in `proposal.html`.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap + the artifact name/path, then the **next decision printed inline** — the **storyline menu** (pick 1) + **bonus media** (song / video / image / none). End with the pick prompt, aligned to the menu: **Reply with your pick (e.g. `1, 2`).** (the example reflects the actual choices — storyline + bonus media). — nothing after it.

Choice-first, human-led. Do not decide the storyline or the bonus-media choice for the team. The signature, visual direction, one-liner, and poster are **AI-decided** — never ask the team to choose them.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
