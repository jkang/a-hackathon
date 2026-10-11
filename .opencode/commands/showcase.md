---
description: Run only the SHOWCASE stage (storyline → deck + prompt-pack).
agent: facilitator
---

Run **only the SHOWCASE stage**.

> **Stage opening.** We're now in the **Showcase** stage: I assemble the proposal + pitch deck (themed to match your poster + storyboard); you **pick a storyline** and decide whether to add **bonus media**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another stage.** (See `facilitator` → *Turn discipline*.)

Use the `showcase` skill with `facilitation` (option menu). Requires the captures embedded in `insight-brief.html` + `campaign-plan.html`, plus the media kit from the `mediakit` stage (`poster-<style>.html` + `storyboard.html`).

**Recover upstream (resume) — do this first.** Determine the quest id and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), state it in one line and continue — no need to ask. Ask **only when genuinely ambiguous**. Read the `insight-brief.html` + `campaign-plan.html` captures (and `poster_style` from `campaign-plan.html`), and locate `poster-<style>.html` + `storyboard.html`. If an upstream artifact is missing, say which and ask the team to run the missing stage first. **Media-kit fallback:** if no poster exists, build a **default poster (style A)**; if no storyboard exists, build a **default storyboard (SVG design sheet)** — so the deck's visual beats are always present.

**This stage has exactly TWO team decisions — the storyline and bonus media.** The AI decides everything else.

1. **Storyline** — present the 5-storyline menu (Classic / Hero's Journey / Big Reveal / Demo / Trailer); the team picks 1. It sets the signature.
2. **Bonus media** — the team decides whether to attempt song / video / image (or none).
3. **AI settles the rest (no decision)** — the **signature element** (the storyline's default), the **visual direction**, the **one-liner**, and the **deck theme** (light · cream · dark, matched to the chosen poster style + the storyboard surface). `poster_style` comes from the `campaign-plan.html` capture — do **not** re-ask.
4. Build the deck (`data-storyline` + `data-theme` set to match the poster style / storyboard surface) — **8 beats, visual-first, theme-matched**: title → context → insight → audience → **signature** → **visuals** → strategy → ask. The **poster beat** embeds `poster-<style>.html?embed=1` (shown complete); the **storyboard beat** is full-bleed, embedding `storyboard.html?embed=1`; the **`visuals` beat** carries the remaining kit asset(s) (fill `{{VIS_POSTER}}` / `{{VIS_STORYBOARD}}` with thumb iframes — storyboard thumb uses `?embed=1` — and set `{{VISUALS_LABEL}}`).
5. **Always write `prompt-pack.html`** (Suno / Runway / GPT / Kimi prompts) so the media prompts are ready even if the team initially chose none; embed any returned files.
6. Write into the current round folder `artifacts/Quest<ID>-<NN>/`: `proposal.html` (the unified proposal viewer) + `pitch-deck.html` + `prompt-pack.html`; the showcase capture is embedded in `proposal.html`. Build the proposal viewer with `python3 .opencode/skills/showcase/scripts/build-proposal.py --dir artifacts/Quest<ID>-<NN>/`.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap + the artifact name/path, then the **next decision printed inline** — the **storyline menu** (pick 1) + **bonus media** (song / video / image / none). End with: **"Open `insight-brief.html` / `campaign-plan.html` and review them with your team — choose the options that fit, or add your own — then reply here to continue."** then **"Reply with your pick (e.g. `1, 2`), or type your own."** (the example reflects the actual choices — storyline + bonus media). Put nothing after it.

When the deck + proposal are built and complete → **"Your proposal is packaged — `artifacts/Quest<ID>-<NN>/proposal.html` (deck + poster + storyboard + prompt-pack inside). Before you submit, add the creative media the deck still needs: open `prompt-pack.html`, copy each ready-made prompt into its tool — song → Suno, video → Runway Gen-3, image / storyboard → GPT or Kimi — generate the file, and bring it back; I'll embed it into the deck. (If the prompts aren't there yet, tell me and I'll write them now.) Once the media is in, you're ready to submit."** Then STOP. Do **not** default straight to "ready to submit" — the **generate-the-media reminder comes first**.

Choice-first, human-led. Do not decide the storyline or the bonus-media choice for the team. The signature, visual direction, one-liner, and theme are **AI-decided** — never ask the team to choose them.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
