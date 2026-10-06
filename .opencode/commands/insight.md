---
description: Run only the INSIGHT gate (research → trends / audience / moment / seed insight).
agent: facilitator
---
Run **only the INSIGHT gate**.

> **One decision per turn.** Present one menu, then **STOP and wait** for the team's reply. **Never answer your own menu; never run another gate.** (See `facilitator` → *Turn discipline*.)

Use the `insight` skill with `facilitation` (option menu) and `agent-reach` (or delegate to the `researcher` subagent).

0. **Brief & confirm (HITL) — only if the session hasn't been briefed yet.** If you already opened with `/start` and the team confirmed, skip straight to research. Otherwise, before researching, restate the quest (client · mission · market), name the four gates, and say you will research it into **~6 data-backed insights** — noting this may take a few minutes. Then present the **fixed start menu** (verbatim — do not reword/reorder/add): **1** Start the research · **2** Skip research (reuse the Scout Report) · **3** Reuse the card + add our own facts; **wait for the team's reply.**
1. **Research first** — gather real facts/reports, distil into data-backed options. **Cap retries at 2–3 attempts per source**; if a site keeps failing, mark it unreachable and move on.
2. Present menus: **trends** (pick 2–3), **audience segments** (pick 2–4), **moment of truth** (pick 1–2), **field truths** (pick the ones that resonate). Always `+1 of our own`.
3. Converge → the team confirms **one seed insight**.
4. Write into the current round folder `artifacts/Quest<ID>-<NN>/` (reuse the latest round for this quest; create `-01` if none): **`insight-brief.html` only** — its decisions go in the embedded `id="capture"` block (no YAML).

**End every turn with a wrap-up (see `facilitator` → *Response format*):** a 2–4 line recap of what you did + the artifact name/path, then the **next decision printed inline in the chat** — for this gate, the **~6 key insights** (pick 2–3), and each sub-menu as it comes (trends · segments · moment · truths). Add a one-line pick prompt. **Never ask the team to open the HTML to choose.**

Choice-first, human-led. Do not decide for the team.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
