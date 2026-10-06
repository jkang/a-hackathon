---
description: Run only the INSIGHT gate (AI curates everything; the team's single decision is the key insights).
agent: facilitator
---
Run **only the INSIGHT gate**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another gate.** (See `facilitator` → *Turn discipline*.)

**This gate has exactly ONE team decision — the Key Insights (pick 2–3).** The AI curates everything else.

Use the `insight` skill with `facilitation` (option menu) and `agent-reach` (or delegate to the `researcher` subagent).

0. **Brief & confirm (HITL) — only if the session hasn't been briefed yet.** If you already opened with `/start` and the team confirmed, skip straight to research. Otherwise, before researching, restate the quest (client · mission · market), name the four gates, and say you will research it into **~6 data-backed insights** — noting this may take a few minutes. Then present the **fixed start menu** (verbatim — do not reword/reorder/add): **1** Start the research · **2** Skip research (reuse the Scout Report) · **3** Reuse the card + add our own facts; **wait for the team's reply.**
1. **Seed the brief + research (no decision).** On the go-ahead, give the 30s scout summary, then run the research chain (`business-research` → `audience-analysis` → `swot-analysis` via `agent-reach`). **Create `insight-brief.html` as soon as the first block lands**, then rewrite it as research returns. Distil full data-backed menus: trends · segments · moments · truths (each with a fact/source), **select the focus bundle(s) and mark your `AI pick`s**. **Cap retries at 2–3 attempts per source.**
2. **Draft key insights (no decision).** Distil **~6 key insights** from the org + trends + audience + focus + SWOT. Rewrite the brief (all ~6 listed).
3. **DECISION — the single decision.** Present the **~6 key insights** inline → the team **picks 2–3** to carry into `plan` (or `+1 own`). Rewrite the brief (chosen highlighted).
4. Finalize the **seed insight**, then write the current round folder `artifacts/Quest<ID>-<NN>/` (reuse the latest round for this quest; create `-01` if none): **`insight-brief.html` only** — built progressively, with every menu listed in full and the decisions in the embedded `id="capture"` block (no YAML).

**The gate is exactly one decision — the Key Insights (2–3).** Focus bundle / trends / moments / truths are AI-curated, shown in full, and overridable on request.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap of what you did + the artifact name/path, then the **next decision printed inline in the chat** — the **~6 key insights** (pick 2–3). End with the pick prompt, verbatim: **Reply with your pick (e.g. `1, 2`).** — nothing after it.

Choice-first, human-led. Do not decide for the team.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
