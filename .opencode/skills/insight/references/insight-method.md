# Insight Method — market read → segments (decision 1) → focus bundles → key insights (decision 2)

The AI does the research; the team makes **two decisions**:

- **Segments** — pick 2–3 *(who the campaign targets)*.
- **Key Insights** — pick 2–3 *(the segment × moment × trend tensions to deep-dive in the plan)*.

Everything else — the **market trends** (a merged read), the **focus bundles** (audience × moment × shift), and the **seed insight** — is **AI-curated**, shown in full in the brief, and overridable on request.

## Research chain (sub-skills)

`agent-reach` → `business-research` → `market-trends` → `audience-analysis`

- `agent-reach` = the shared data engine (feeds the research skills).
- `business-research` = organization profile + benchmark (internal) — its **assets / constraints are the strengths / weaknesses**.
- `market-trends` = the merged market read (external) — **shifts + hard facts + opportunities/threats**, each tagged `kind`; **runs before segments** (sets the attractiveness backdrop).
- `audience-analysis` = audience & segments (external).

## The living brief — building blocks → focus bundles → key insights

| Block | Question it answers | Source | Decision? |
|---|---|---|---|
| 1 · Organization profile | who is the client, what do they own & offer? | `business-research` | AI |
| 2 · Market Trends | what's the market, what's shifting, and what are the hard facts + external opportunities/threats? | card + `agent-reach` + `market-trends` | AI, shown in full |
| 3 · Audience Segments | who are the segments, and what job do they hire? | `audience-analysis` | **DECISION 1 · pick 2–3** |
| → Focus bundles | **selected segment × moment × shift** | AI derives from the picks | AI |
| → Key insights | **~6 tensions fusing segment × moment × trend** | AI derives from the focus bundles | **DECISION 2 · pick 2–3** |
| → Seed insight | the one-line overarching tension | AI | AI (from the picks) |

> Every option and insight carries a **fact, number, or named behavior + a source** — not a generic label. See `facilitation/references/option-menu.md`.

---

## 1. Market Trends (merged — the market read)

Run the `market-trends` sub-skill. Start from the card (market size, benchmark, arena), then add ~6–8 items. This single block is the **merged market read** — directional shifts, hard field facts, and the external **opportunities / threats**. There is **no separate truths block and no separate SWOT block** — everything market-facing lives here. **This block comes before the segments** (it sets the market backdrop and the attractiveness signals).

Categories to scan (pick what's real for the quest):
- **Behavior**: mobile-first, short-video, social/group travel, experience economy.
- **Culture**: creator trust > ads; national pride; "cute economy" / soft-power IP.
- **Technology/Policy**: visa liberalization, hub airlines, digital collectibles, livestream commerce.

Capture each item as `{trend, why_it_matters, kind, source}` — **all** of them stay in the brief. Mark each item's `kind` (`shift` / `fact` / `opportunity` / `threat`).

## 2. Audience — STP + JTBD (DECISION 1)

For each of **~6–8 segments**, fill one line each:

- **Who** (STP segmentation): demographic + psychographic + geography.
- **Job** (JTBD — three lenses):
  - *Functional*: what they're trying to get done.
  - *Social*: how they want to be seen.
  - *Emotional*: the feeling they're chasing.
- **Barrier**: what stops them today.
- **Trigger**: what would flip them into action.
- **Channels**: where to reach them.
- **Size & market potential**: estimated reach → rough addressable (with source).

> A segment with no emotional job and no trigger is not a real segment — it's a demo label. Force the emotional job. List all segments in the brief, then **the team picks 2–3** (the AI does not rank-pick).

## 3. Focus Bundles — derived from the selected segments (AI)

After the team selects 2–3 segments, derive **one focus bundle per selected segment**:

- **Name** — a short strategic label.
- **Audience** — the selected segment.
- **Moment** — the time / place / event where that segment decides.
- **Shift** — the supporting trend.
- **Why** — one line on why this combination is the opportunity.

The **Moment of Truth** is derived here (audience × moment) — **no separate moment menu**; each selected segment contributes one moment. All focus bundles stay listed in full and the team may override ("redo the focus").

## 4. Key Insights — DECISION 2 (pick 2–3)

Distil **~6 key insights** — **derive each from a focus bundle**, so every insight fuses a **selected segment × its moment × a supporting trend** into a tension (~2 per selected segment, different angles). Formula:

> "[Segment] [job/desire] — but at **[moment]**, **[trend/fact]** → **[tension/gap]** — so **[implication]**."

Each carries its `segment_id` + `trend_id` + `moment` + evidence + source. The team picks **2–3** to deep-dive in `plan`; the rest are parked (still listed).

## 5. The seed insight

A **tension**, not a summary. It connects the chosen audience's job ↔ market gap ↔ trend:

> "[Audience] already [feels/does X], yet [barrier/gap] — so [mission] at [moment]."

Synthesized by the AI from the focus + chosen insights; no extra decision.

## Anti-patterns

- Long web research instead of card + team knowledge.
- Segments with no emotional job / no trigger.
- A separate "truths" block duplicating the trends — keep the market read in one block.
- A key insight that **restates a trend** (with no audience and no moment) — every insight must fuse segment × moment × trend.
- Key insights that all come from one kind of source (all market facts) — distribute them across the selected segments (~2 each).
- No moment of truth (everything "in general").
- A seed insight that restates the card instead of forming a tension.
- **Hiding the losing options** — every menu must be listed in full with its selection state.
- **Asking the team beyond the two decisions** — segments, then insights.

## Running it in ~8 minutes (facilitation)

1. AI: 30s scout + org/benchmark scaffold → **create the brief**.
2. AI: research → draft the market read (trends) + segments. No decision.
3. AI: present the segments → **team picks 2–3** (decision 1).
4. AI: derive the focus bundles + draft ~6 key insights. No decision.
5. AI: present the ~6 key insights → **team picks 2–3** (decision 2).
6. AI: seed insight + finalize the brief.

## Source materials (reference only)

- `sub-skills/business-research` — org/benchmark research structure.
- `sub-skills/market-trends` — the market-read scan framework.
- `sub-skills/audience-analysis` — the segmentation framework.
