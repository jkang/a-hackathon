---
description: Run the whole quest automatically end-to-end (autopilot — the AI makes every decision itself), and produce the complete deliverable set plus the unified proposal report.
agent: runner
---
Run the whole quest end-to-end **automatically** — no questions, no human input. At every decision node, decide yourself (per the `runner` agent).

**Quest: $ARGUMENTS** (if empty, read the quest card / `quest-card.md` for the challenge).

1. **Insight** — research → org profile + benchmark → merged market trends + segments → pick 2–3 segments → derive focus bundles (one per pick) + draft ~6 key insights → pick 2–3; build `insight-brief.html` progressively, listing every option.
2. **Plan** — pick 1–2 concept keywords → `creative-concept` (~6 ideas) → build one complete campaign + channel mix + plan + budget + the **pilot forecast** (funnel metrics + derivation chains) → `poster`.
3. **Showcase** — pick a storyline → build `proposal.html` (unified report) + `pitch-deck.html` (≤ 8 slides, visual-first) + `prompt-pack.html`.

**Output: `artifacts/Quest<ID>-<NN>/`** — create the new round folder for this run and write all artifacts there; record every decision + its reason in each artifact's embedded `id="capture"` block (no YAML/Markdown files). Grounded, no fabricated numbers; **English only** (artifacts and any reply); Ascentium-branded.
