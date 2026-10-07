---
description: Open a facilitated session — brief the team on what's coming, confirm, then wait (does not run the gates).
agent: facilitator
---

Open a **facilitated (human-led)** session for this quest. This command does **the briefing only**. It must **not** research, run any gate, or create any artifact — those happen in later turns, one decision at a time, after the team replies.

**Quest: $ARGUMENTS** (if empty, ask the team, then read the quest card / `quest-card.md`).

**Do only this, then STOP:**

1. Read the quest card.
2. **Brief the team — explain clearly, in plain language, what is about to happen:**
   - **The task.** The client, the mission, and the target market, in your own words.
   - **The plan — four gates, walked one at a time, with the team deciding at each step:**
     1. **Insight** — AI researches and curates the market read + segments; the team **picks 2–3 audience segments**, then **2–3 key insights**. → `insight-brief.html`
     2. **Plan (+ poster)** — AI diverges ~6 ideas and builds **2 complete campaigns (A/B)**; the team **picks one**. → `campaign-plan.html` + `poster.html`
     3. **Prove** — AI produces the most reasonable numeric forecast (no team decision). → `proof.html`
     4. **Showcase** — the team picks a storyline; AI assembles the proposal, pitch deck, and prompt pack. → `proposal.html` + `pitch-deck.html` + `prompt-pack.html`
   - **What happens right now.** On the team's go-ahead you will research this quest (web + reports via `agent-reach` / the `researcher` subagent) and turn it into **~6 data-backed insights** for the team to choose from. Say plainly that this research **may take a few minutes**.
3. **Present this exact decision menu — verbatim, do not reword, reorder, add, or rename the options:**

   > **Your decision**
   >
   > 1. **Start the research** — AI researches the quest (~6 data-backed insights) for you to pick from. (Recommended; takes a few minutes.)
   > 2. **Skip research** — reuse the card's Scout Report as the seed and move straight to the Insight menus.
   > 3. **Reuse the card + add our own facts** — start from the Scout Report, and our team will contribute the extra evidence we already know.

**Then end your turn and wait for the team's reply.** Do **not** start research, do **not** build anything.

**When the team replies with their choice, log it and STOP** — do **not** research, do **not** build anything, do **not** advance into the next stage. End the turn with:

> **Briefing done.** Your choice is logged. Run **`/insight`** to begin.

> This is the *explanation* of the plan — not a to-do list. Walk the happy path **one decision per turn** (see `facilitator` → *Turn discipline*). To run the whole quest automatically instead, use `/run`.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
