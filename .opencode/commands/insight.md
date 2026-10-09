---
description: Run only the INSIGHT stage (AI researches and curates; the team makes TWO decisions — segments, then key insights).
agent: facilitator
---
Run **only the INSIGHT stage**.

> **Stage opening.** We're now in the **Insight** stage: I research the market and curate the audience segments + key insights; you make **two picks** — 2–3 segments, then 2–3 insights.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another stage.** (See `facilitator` → *Turn discipline*.)

**This stage has TWO team decisions:** (1) **pick the audience segments (2–3)**; then (2) **pick the key insights (2–3)**. The AI curates everything else. Each decision is its own turn.

Use the `insight` skill with `facilitation` (option menu) and `agent-reach` (or delegate to the `researcher` subagent).

**Recover upstream (resume) — do this first.** Determine the quest id (from `$ARGUMENTS` or the quest card) and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), say so in one line and continue — no need to ask. Ask **only when genuinely ambiguous** (a fresh session with no context, or several rounds exist): one line — "Resume from `QuestA-02`, or give me a round number." If an `insight-brief.html` already exists in that round, read its `id="capture"` and continue from there rather than starting over. (Insight has no upstream stage — it reads the quest card + team knowledge.)

0. **Research choice (HITL).** If the research mode was already chosen (e.g. from `/start`), honor it and proceed — do **not** re-ask. Otherwise, restate the quest in one or two lines (client · mission · market), note there are **two picks** (segments, then insights) and that research **may take a few minutes**, then present the **fixed start menu** (verbatim — do not reword/reorder/add): **1** Start the research · **2** Skip research (reuse the Scout Report) · **3** Reuse the card + add our own facts; **wait for the team's reply.** Honor the choice: **Start** → run the research chain; **Skip / Reuse** → skip research and seed the brief from the Scout Report.
1. **Seed the brief + research (no decision).** On the go-ahead, give the 30s scout summary, then run the research chain (`business-research` → `market-trends` → `audience-analysis` via `agent-reach`). **Create `insight-brief.html` as soon as the first block lands**, then rewrite it as research returns. Distil full data-backed menus: **market trends** (~6–8, one merged read: shifts + hard facts + external opportunities/threats, each tagged `kind`) **first**, then **segments** (~6–8). **Cap retries at 2–3 attempts per source.**
2. **DECISION 1 — the segments.** Present the **~6–8 segments** inline → the team **picks 2–3** to target. Rewrite the brief (chosen highlighted). **STOP.**
3. **Derive + draft (no decision).** Derive one **focus bundle** per selected segment (segment × moment × supporting trend + why); then draft **~6 key insights, each derived from a focus bundle** so it fuses a selected segment × its moment × a supporting trend (~2 per segment, different angles). Rewrite the brief.
4. **DECISION 2 — the key insights.** Present the **~6 key insights** inline → the team **picks 2–3** to carry into `plan` (or `+1 own`). Rewrite the brief (chosen highlighted). **STOP.**
5. Finalize the **seed insight**, then write the current round folder `artifacts/Quest<ID>-<NN>/` (reuse the latest round for this quest; create `-01` if none): **`insight-brief.html` only** — built progressively, with every menu listed in full and the decisions in the embedded `id="capture"` block (no YAML).

**The stage is exactly two decisions — the segments (2–3), then the key insights (2–3).** Market trends and focus bundles are AI-curated, shown in full, and overridable on request.

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap of what you did + the artifact name/path, then the **next decision printed inline in the chat**.
- After research → the **~6–8 segments** (pick 2–3). End with: **"Open `insight-brief.html` and review it with your team — choose the options that fit, or add your own — then reply here to continue."** then **"Reply with your pick (e.g. `1, 3, 5`), or type your own."**
- After the segment pick → the **~6 key insights** (pick 2–3). End with the **same two lines**.
Nothing after the pick prompt.

**Stage completion.** When the key-insights pick is finalized and `insight-brief.html` is complete, end with: **"Research and insight are complete — `artifacts/Quest<ID>-<NN>/insight-brief.html`. Next: run `/plan` to design the campaign."** Then STOP (do not advance into the next stage).

Choice-first, human-led. Do not decide for the team.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
