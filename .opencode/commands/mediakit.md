---
description: Create the campaign media kit — the poster (pick 1 of 3 styles) + the storyboard (16:9 paginated scene deck with inline SVG art + AI-upgrade prompt).
agent: facilitator
---

Create the **campaign media kit** using the `mediakit` skill (poster + storyboard), from the `campaign-plan.html` + `insight-brief.html` captures.

> **Stage opening.** We're now in the **Media Kit** stage: I build the **poster** in **three styles (Style A · Full-Bleed Hero / Style B · Belonging Passport / Style C · Midnight Minimal)** for you to **pick one** — then I build the **storyboard** (a 16:9 paginated scene deck — a cover + one page per 1–2 rich scenes, 6 scenes in 3 chapters — drawn as inline SVG art, plus a prompt to upgrade it).

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another stage.** (See `facilitator` → *Turn discipline*.)

**This stage has exactly ONE team decision — pick 1 of the 3 poster styles.** The AI builds all three posters first; the storyboard is then AI-generated (no second decision).

> **Plan vs style (don't conflate).** The **plan** (the single campaign in the `campaign-plan.html` capture, under `plan`) is the campaign content built from the team's concept keywords; `poster_style` = **a | b | c** is the poster design you offer here.

**Recover upstream (resume) — do this first.** Determine the quest id and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), state it in one line and continue — no need to ask. Ask **only when genuinely ambiguous**. Read the `campaign-plan.html` capture — **the plan** (`plan`: name · slogan · proposition · `offer` + its 3 cards · `visual_direction` · `one_liner`) — and the `insight-brief.html` capture (audience + moment). If either is missing, say so and ask the team to run `/plan` (or `/insight`) first.

1. Pull name · slogan · proposition · the structured `offer` (summary + 3 cards) from **`plan`** in the `campaign-plan.html` capture, and **reuse that plan's `visual_direction` + `one_liner`** — do **not** re-derive them and do **not** ask the team first.
2. Fill the 9-section poster anatomy **once** across the three style templates; set the accent vars + key visual from the quest card.
3. **Build all three posters at once** → `poster-a.html` · `poster-b.html` · `poster-c.html` + the `poster.html` tab page (fill the three per-style **richer-poster prompts** — a content script for each style, visuals left open, `campaign-plan.html` as the recommended input, HTML only). Self-check against the content checklist.
4. **DECIDE (team) — the single decision** — present the **three styles (Style A · Full-Bleed Hero / Style B · Belonging Passport / Style C · Midnight Minimal)** inline → the team **picks one** (or `+1 own`). Record it as `poster_style` (a | b | c) in the `campaign-plan.html` capture.
5. On the pick: **build the storyboard** — a **16:9 paginated scene deck** (a cover + one page per **1–2 rich scenes**, 6 scenes in 3 chapters; each scene = number · title · chapter · scene art · a phone/UI inset · a customer quote · a meta block (stage · moment · emotion · goal) · an action + source line) rendered as an **inline SVG design** (self-contained, no external image needed) in `storyboard.html`, and emit the **one complete prompt** the team can take to **Kimi / GPT** for a more visualized raster sheet (bring it back and I'll add it as a Board page). Default 2 scenes per page; the spec's `per_page` (or `--per-page 1`) switches to one scene per page.

Write into the current round folder `artifacts/Quest<ID>-<NN>/`: `poster.html` + `poster-a|b|c.html` + `storyboard.html` — single-file, Ascentium brand.

> **Both prompts are content scripts, not visual specs.** The poster's per-style prompt and the storyboard's prompt describe **what the campaign says** (the poster's content structure; the storyboard's scene-by-scene story) and deliberately **leave the art direction to the other tool**. Both must say: **feed it `campaign-plan.html` first** (add `insight-brief.html`), and it must return a **self-contained HTML** — **HTML only, never PPT/PPTX/Keynote/Slides**.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap + the artifact name/path, then the **poster-style decision printed inline** — the **three poster styles (A/B/C)** (pick 1). End with: **"Open `poster.html` (tab through Style A · B · C) and review it with your team — choose the style that fits, or add your own — then reply here to continue."** then **"Reply with your pick (e.g. `1`), or type your own."** Put nothing after it.

When the style pick is finalized and the storyboard is built → **"Your media kit is ready — `artifacts/Quest<ID>-<NN>/poster.html` (the chosen style) and `storyboard.html` (the 16:9 paginated scene deck). Open them with your team and review; send any feedback or changes and I'll revise. Tip: for a richer version, take the prompt in `storyboard.html` (or the per-style prompt in `poster.html`, press **P**) to Kimi / GPT with `campaign-plan.html` as input — it writes the story/content script and returns a self-contained HTML I can inline. When you're happy, run `/showcase` to assemble the proposal and pitch deck."** Then STOP (do not advance into the next stage; do **not** default straight to `/showcase` — offer the review first).

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
