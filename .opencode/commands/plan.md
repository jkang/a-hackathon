---
description: Run only the PLAN / creative stage (AI builds 2 complete campaigns A/B; the team picks one).
agent: facilitator
---

Run **only the PLAN stage** (the creative heart). Use the `plan` skill + `facilitation` (option menu). Requires the `insight-brief.html` capture (selected segments + chosen focus bundle + selected insights).

> **Stage opening.** We're now in the **Plan** stage: I diverge ~6 ideas and build **two complete campaigns (A/B)**; you **pick one**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another stage.** (See `facilitator` → *Turn discipline*.)

**This stage has exactly ONE team decision — pick the campaign (A or B).** The AI does everything else.

**Recover upstream (resume) — do this first.** Determine the quest id and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), state it in one line and continue — no need to ask. Ask **only when genuinely ambiguous**. Read the `insight-brief.html` capture (`selected_segments` · `selected_insights` · `focus_bundles` · `moment_of_truth`). If it's missing, say so and ask the team to run `/insight` first.

1. **Diverge (AI)** — run `creative-concept`: anchor (from the chosen focus bundle) + one HMW + creative methods → **~6 candidate ideas**. **Create `campaign-plan.html` as soon as the first output lands**, then rewrite it each step.
2. **Converge + build A/B (AI)** — narrow the ~6 into **2 complete, distinct campaigns** (A/B). Build each fully: `opportunity-definition` (5 elements) + positioning (Moore) + offering + 4Ps + 2 pilot markets + pilot experiment + budget (card War Chest).
3. **Render (AI)** — design a hero visual for each campaign and **embed it inside `campaign-plan.html`**. Do **not** write standalone poster files here — those are produced later by `/poster`.
4. **DECIDE (team) — the single decision** — present the **two complete campaigns (A/B)** inline → the team **picks ONE** (or `+1 own`). That pick is the plan. Rewrite the brief (chosen highlighted, the other dimmed).

Choice-first, human-led. Do not decide for the team.

Write into the current round folder `artifacts/Quest<ID>-<NN>/`: **`campaign-plan.html` only** (built progressively; both campaigns A/B listed in full, chosen one highlighted; decisions in its embedded `id="capture"` block). No poster files here and no YAML — the poster is created by `/poster`.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap + the artifact name/path, then the **next decision printed inline** — the **two complete campaigns (A/B)** (pick 1). End with the pick prompt, aligned to the menu: **Reply with your pick (e.g. `1`).** (the A/B menu has 2 options; pick 1). — nothing after it.

**Stage completion.** When the campaign pick is finalized and `campaign-plan.html` is complete → **"The plan is ready — `artifacts/Quest<ID>-<NN>/campaign-plan.html`. Next: run `/poster` to design and pick the campaign poster, or `/prove` to continue without one."** Then STOP (do not advance into the next stage).

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
