---
description: Create the campaign poster only (AI builds all 3 styles; the team picks one).
agent: facilitator
---
Create the **campaign poster** using the `poster` skill (from the `campaign-plan.html` + `insight-brief.html` captures).

> **Stage opening.** We're now in the **Poster** stage: I build **three poster styles (Style A · Full-Bleed Hero / Style B · Belonging Passport / Style C · Midnight Minimal)**; you **pick one**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another stage.** (See `facilitator` → *Turn discipline*.)

**This stage has exactly ONE team decision — pick 1 of the 3 poster styles.** The AI builds all three styles first.

> **Plan vs style (don't conflate).** The **plan** (the single campaign in the `campaign-plan.html` capture, under `plan`) is the campaign content built from the team's concept keywords; `poster_style` = **a | b | c** is the poster design you offer here.

**Recover upstream (resume) — do this first.** Determine the quest id and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), state it in one line and continue — no need to ask. Ask **only when genuinely ambiguous**. Read the `campaign-plan.html` capture — **the plan** (`plan`: name · slogan · proposition · `offer` + its 3 cards · `visual_direction` · `one_liner`) — and the `insight-brief.html` capture (audience + moment). If either is missing, say so and ask the team to run `/plan` (or `/insight`) first.

1. Pull name · slogan · proposition · the structured `offer` (summary + 3 cards) from **`plan`** in the `campaign-plan.html` capture, and **reuse that plan's `visual_direction` + `one_liner`** — do **not** re-derive them and do **not** ask the team first.
2. Fill the 9-section poster anatomy **once** across the three style templates; set the accent vars + key visual from the quest card.
3. **Build all three at once** → `poster-a.html` · `poster-b.html` · `poster-c.html` + the `poster.html` tab page. Self-check against the content checklist.
4. **DECIDE (team) — the single decision** — present the **three styles (Style A · Full-Bleed Hero / Style B · Belonging Passport / Style C · Midnight Minimal)** inline → the team **picks one** (or `+1 own`). Record it as `poster_style` (a | b | c).

Write into the current round folder `artifacts/Quest<ID>-<NN>/`: `poster.html` + `poster-a|b|c.html` — portrait, single-file, Ascentium brand.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap + the artifact name/path, then the **next decision printed inline** — the **three poster styles (A/B/C)** (pick 1). End with: **"Open `poster.html` (tab through Style A · B · C) and review it with your team — choose the style that fits, or add your own — then reply here to continue."** then **"Reply with your pick (e.g. `1`), or type your own."** Put nothing after it.

When the style pick is finalized and `poster.html` is complete → **"The poster is ready — `artifacts/Quest<ID>-<NN>/poster.html`. Open it with your team and review it; send any feedback or changes and I'll revise it. When you're happy with it, run `/showcase` to assemble the proposal and pitch deck."** Then STOP (do not advance into the next stage; do **not** default straight to `/showcase` — offer the review first).

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
