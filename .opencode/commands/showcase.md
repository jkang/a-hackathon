---
description: Run only the SHOWCASE stage (storyline → deck + prompt-pack).
agent: facilitator
---
Run **only the SHOWCASE stage**.

> **Stage opening.** We're now in the **Showcase** stage: I assemble the proposal + pitch deck; you **pick a storyline** and decide whether to add **bonus media**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another stage.** (See `facilitator` → *Turn discipline*.)

Use the `showcase` skill with `facilitation` (option menu). Requires the captures embedded in `insight-brief.html` + `campaign-plan.html` + `proof.html` (+ the poster from the `poster` skill).

**Recover upstream (resume) — do this first.** Determine the quest id and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), state it in one line and continue — no need to ask. Ask **only when genuinely ambiguous**. Read the `insight-brief.html` + `campaign-plan.html` + `proof.html` captures (and the poster style from `campaign-plan.html`). If an upstream artifact is missing, say which and ask the team to run the missing stage first. **Poster fallback:** if no `poster.html` exists in the round (the team skipped `/poster`), build a **default poster (style A)** before assembling the proposal, so the always-on poster beat is present.

**This stage has exactly TWO team decisions — the storyline and bonus media.** The AI decides everything else.

1. **Storyline** — present the 5-storyline menu (Classic / Hero's Journey / Big Reveal / Demo / Trailer); the team picks 1.
2. **Bonus media** — the team decides whether to attempt song / video / image (or none).
3. **AI settles the rest (no decision)** — the **signature element** (the storyline's default), the **visual direction**, the **one-liner**, and the **poster** (**always included** — `data-poster="yes"`; style = the final `poster` skill pick, default A).
4. Build the deck (`data-storyline` + `data-poster="yes"`).
5. If bonus media was chosen, write `prompt-pack.html` (Suno / Runway / GPT prompts) and embed returned files.
6. Write into the current round folder `artifacts/Quest<ID>-<NN>/`: `proposal.html` (the unified proposal viewer) + `pitch-deck.html` + `prompt-pack.html`; the showcase capture is embedded in `proposal.html`.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap + the artifact name/path, then the **next decision printed inline** — the **storyline menu** (pick 1) + **bonus media** (song / video / image / none). End with the pick prompt, aligned to the menu: **Reply with your pick (e.g. `1, 2`).** (the example reflects the actual choices — storyline + bonus media). — nothing after it.

When the deck + proposal are built and complete → **"Your proposal is packaged — `artifacts/Quest<ID>-<NN>/proposal.html` (deck + prompt-pack inside). You're ready to submit."** Then STOP.

Choice-first, human-led. Do not decide the storyline or the bonus-media choice for the team. The signature, visual direction, one-liner, and poster are **AI-decided** — never ask the team to choose them.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
