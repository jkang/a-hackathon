---
description: Run only the PLAN / creative stage (the team gives 1–2 concept keywords; the AI builds one complete campaign from them).
agent: facilitator
---

Run **only the PLAN stage** (the creative heart). Use the `plan` skill + `facilitation` (option menu). Requires the `insight-brief.html` capture (selected segments + chosen focus bundle + selected insights).

> **Stage opening.** We're now in the **Plan** stage: you give me **1–2 concept keywords**; I run the creative methods and build **one complete campaign** from them.

> **One input per turn.** Ask for the concept keywords, then **STOP and wait** for the team's reply. **Never answer your own prompt; never run another stage.** (See `facilitator` → *Turn discipline*.)

**This stage's only team input is the concept keywords (1–2), given up front.** The AI does everything else, and there is **no end-of-stage menu**.

**Recover upstream (resume) — do this first.** Determine the quest id and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), state it in one line and continue — no need to ask. Ask **only when genuinely ambiguous**. Read the `insight-brief.html` capture (`selected_segments` · `selected_insights` · `focus_bundles` · `moment_of_truth`). If it's missing, say so and ask the team to run `/insight` first.

0. **Ask for the concept keywords (team) — the single input.** After recovering upstream, present a short **example list** so the team isn't facing a blank page (e.g. *national pride · first-timers · family · creators · collectors · eco/cause · nostalgia · underdogs · belonging · unmissable*), and ask for **1–2 keywords that should steer the campaign** (or their own). Then **end the turn and wait** — do not research, diverge, or build yet.
1. **Diverge (AI)** — on the team's reply, run `creative-concept` **using the concept keywords as the creative driver**: anchor (from the chosen focus bundle) + one HMW + creative methods → **~6 candidate ideas**, each visibly reflecting the keywords. **Create `campaign-plan.html` as soon as the first output lands**, then rewrite it each step.
2. **Converge + build (AI)** — converge the ~6 into **ONE complete campaign** aligned to the keywords, threading the **campaign kernel** (`audience · moment · trend · channel · concept`): positioning (Moore) + **channel mix** (grounded in the segment's `channels` + the insight's trend, per `references/channel-strategy.md`) + **offer** (structured: a one-line `summary` + exactly 3 `cards` — offer / markets / access, or membership tiers) + 4Ps + 2 pilot markets + pilot experiment + budget (card War Chest) + the **pilot forecast with derivation chains** (3–5 funnel metrics, each `benchmark → assumption → formula → target`, per `references/pilot-forecast.md`) + its **`visual_direction`** + **`one_liner`**.
3. **Render (AI)** — design a hero visual for the campaign and **embed it inside `campaign-plan.html`**. Do **not** write standalone poster files here — those are produced later by `/poster`.
4. **Complete (no team decision)** — there is no A/B menu: the campaign is generated directly from the team's keywords. Write the capture (`concept_keywords` + the single `plan`) and hand off.

Human-led at the input: the keywords are the team's; the campaign is the AI's execution of them. Do not choose the keywords for the team.

Write into the current round folder `artifacts/Quest<ID>-<NN>/`: **`campaign-plan.html` only** (built progressively; the single plan; decisions in its embedded `id="capture"` block). No poster files here and no YAML — the poster is created by `/poster`.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** on the **keyword turn**, a 1–2 line recap, then **"Open `insight-brief.html` with your team and discuss — then reply here with your concept keywords to continue."** + the inline **example prompt** (an open ask, not a menu). On the **build turn**, a 2–4 line recap + the artifact name/path — **no menu**; the plan is ready for review.

**Stage completion.** When the campaign is built and `campaign-plan.html` is complete (with its pilot forecast + derivation) → **"The plan is ready — `artifacts/Quest<ID>-<NN>/campaign-plan.html`. Open it with your team and review it together; send any feedback or changes and I'll revise it. When you're happy with it, run `/poster` to design and pick the campaign poster, then `/showcase` to assemble the proposal and deck."** Then STOP (do not advance into the next stage).

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
