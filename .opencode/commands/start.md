---
description: Open a facilitated session — brief the team, then start the Insight stage on their pick.
agent: facilitator
---

Open a **facilitated (human-led)** session for this quest. This command **briefs the team, then starts the Insight stage** on their pick — it runs **no other stage** and never decides for the team.

**Quest: $ARGUMENTS** (if empty, ask the team, then read the quest card / `quest-card.md`).

**Turn 1 — brief + present the entry menu, then STOP:**

1. Read the quest card.
2. **Brief the team — explain clearly, in plain language, what is about to happen:**
   - **The task.** The client, the mission, and the target market, in your own words.
   - **The plan — four stages, walked one at a time, with the team deciding at each step:**
     1. **Insight** — AI researches and curates the market read + segments; the team **picks 2–3 audience segments**, then **2–3 key insights**. → `insight-brief.html`
     2. **Plan (+ optional poster)** — AI diverges ~6 ideas and builds **2 complete campaigns (A/B)**; the team **picks one**. → `campaign-plan.html` (the poster is a separate optional step → `poster.html`).
     3. **Prove** — AI produces the most reasonable numeric forecast (no team decision). → `proof.html`
     4. **Showcase** — the team picks a storyline; AI assembles the proposal, pitch deck, and prompt pack. → `proposal.html` + `pitch-deck.html` + `prompt-pack.html`
   - **What happens next.** The first option below **starts the Insight stage**: it researches the quest into **~6 data-backed insights** for the team to choose from. Say plainly that this research **may take a few minutes**.
3. **Present this exact menu — verbatim, do not reword/reorder/add:**

   > **Your decision**
   >
   > 1. **Start `/insight`** — research the quest (~6 data-backed insights) for you to pick from. (Recommended; takes a few minutes.)
   > 2. **Start `/insight` without live research** — reuse the card's Scout Report as the seed.
   > 3. **Start `/insight` from the Scout Report + add our own facts.**

4. End with the pick prompt — **Reply with your pick (e.g. `1`).** — then STOP.

**Turn 2 — start the Insight stage (do not just point at the command; do not print a "run `/insight`" line):**
- Take the team's pick and **enter the `insight` skill** with that research mode (**1** → run the research chain; **2** → reuse the Scout Report; **3** → reuse + add facts): restate the quest in one or two lines, create the round folder `artifacts/Quest<ID>-<NN>/`, and start the brief.
- The team may also start it by typing **`/insight`** directly — same stage.

> This is the *explanation* of the plan — not a to-do list. Walk the happy path **one decision per turn** (see `facilitator` → *Turn discipline*). To run the whole quest automatically instead, use `/run`.

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
