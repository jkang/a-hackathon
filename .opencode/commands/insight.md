---
description: Run only the INSIGHT gate (AI researches and curates; the team makes TWO decisions — segments, then key insights).
agent: facilitator
---
Run **only the INSIGHT gate**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another gate.** (See `facilitator` → *Turn discipline*.)

**This gate has TWO team decisions:** (1) **pick the audience segments (2–3)**; then (2) **pick the key insights (2–3)**. The AI curates everything else. Each decision is its own turn.

Use the `insight` skill with `facilitation` (option menu) and `agent-reach` (or delegate to the `researcher` subagent).

**Recover upstream (resume) — do this first.** Determine the quest id (from `$ARGUMENTS` or the quest card), then find the latest round `artifacts/Quest<ID>-*` (or the round number the team gave). **Confirm with the team in one line** before proceeding: "I found `QuestA-02` as the latest round — resume from it? (or give me a round number)." If an `insight-brief.html` already exists in that round, read its `id="capture"` and continue from there rather than starting over. (Insight has no upstream stage — it reads the quest card + team knowledge.)

0. **Brief & confirm (HITL) — only if the session hasn't been briefed yet.** If you already opened with `/start` and the team confirmed, honor the choice they logged (Start research / Skip / Reuse) and go straight to research — do **not** re-ask the menu. Otherwise, before researching, restate the quest (client · mission · market), name the four stages, and say you will research it into **~6 data-backed insights** — noting there are **two picks** (segments, then insights) and that research **may take a few minutes**. Then present the **fixed start menu** (verbatim — do not reword/reorder/add): **1** Start the research · **2** Skip research (reuse the Scout Report) · **3** Reuse the card + add our own facts; **wait for the team's reply.**
1. **Seed the brief + research (no decision).** On the go-ahead, give the 30s scout summary, then run the research chain (`business-research` → `audience-analysis` → `swot-analysis` via `agent-reach`). **Create `insight-brief.html` as soon as the first block lands**, then rewrite it as research returns. Distil full data-backed menus: **market trends** (~6–8, one merged read: shifts + hard facts + external opportunities/threats) and **segments** (~6–8). **Cap retries at 2–3 attempts per source.**
2. **DECISION 1 — the segments.** Present the **~6–8 segments** inline → the team **picks 2–3** to target. Rewrite the brief (chosen highlighted). **STOP.**
3. **Derive + draft (no decision).** Derive one **focus bundle** per selected segment (segment × moment × supporting trend + why); draft **~6 key insights** from the org + trends + selected segments + focus. Rewrite the brief.
4. **DECISION 2 — the key insights.** Present the **~6 key insights** inline → the team **picks 2–3** to carry into `plan` (or `+1 own`). Rewrite the brief (chosen highlighted). **STOP.**
5. Finalize the **seed insight**, then write the current round folder `artifacts/Quest<ID>-<NN>/` (reuse the latest round for this quest; create `-01` if none): **`insight-brief.html` only** — built progressively, with every menu listed in full and the decisions in the embedded `id="capture"` block (no YAML).

**The gate is exactly two decisions — the segments (2–3), then the key insights (2–3).** Market trends and focus bundles are AI-curated, shown in full, and overridable on request.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap of what you did + the artifact name/path, then the **next decision printed inline in the chat**.
- After research → the **~6–8 segments** (pick 2–3). End with: **Reply with your pick (e.g. `1, 3, 5`).**
- After the segment pick → the **~6 key insights** (pick 2–3). End with: **Reply with your pick (e.g. `1, 3, 5`).**
- After the key-insights pick is finalized and `insight-brief.html` is complete → **"Research and insight are complete — `artifacts/Quest<ID>-<NN>/insight-brief.html`. Next: run `/plan` to design the campaign."** Then STOP (do not advance into the next stage).
Nothing after the pick prompt (or the completion line).

Choice-first, human-led. Do not decide for the team.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
