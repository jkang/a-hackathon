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
     1. **Insight** — AI researches the market; the team picks the trends, the audience segments, the moment of truth, and **2–3 key insights**. → `insight-brief.html`
     2. **Plan (+ poster)** — AI generates ~6 campaign ideas; the team picks 2–3 (or combines them); AI builds **A/B** plan versions; the team picks one and the poster direction. → `campaign-plan.html` + `poster.html`
     3. **Prove** — AI drafts candidate pilot metrics; the team picks **3–5**; AI writes how each number is derived. → `proof.html`
     4. **Showcase** — the team picks a storyline; AI assembles the proposal, pitch deck, and prompt pack. → `proposal.html` + `pitch-deck.html` + `prompt-pack.html`
   - **What happens right now.** On the team's go-ahead you will research this quest (web + reports via `agent-reach` / the `researcher` subagent) and turn it into **~6 data-backed insights** for the team to choose from. Say plainly that this research **may take a few minutes**.
3. **Ask the team to confirm** before research begins — or to skip research and reuse the card's Scout Report as the seed.

**Then end your turn and wait for the team's reply.** Do **not** start research, do **not** build anything, do **not** run ahead to the next gate. The team's answer drives the next turn.

> This is the *explanation* of the plan — not a to-do list. Walk the happy path **one decision per turn** (see `facilitator` → *Turn discipline*). To run the whole quest automatically instead, use `/run`.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
