---
description: Run the whole quest automatically end-to-end (autopilot — the AI makes every decision itself), and produce the complete deliverable set plus the unified proposal report.
agent: runner
---
Run the whole quest end-to-end **automatically** — no questions, no human input. At every decision node, decide yourself (per the `runner` agent).

**Quest: $ARGUMENTS** (if empty, read the quest card / `quest-card.md` for the challenge).

1. **Insight** — research via `agent-reach` → org + audience + trends + SWOT → ~6 key insights → pick 2–3.
2. **Plan** — `creative-concept` (anchor + HMW + methods → ~6 ideas) → pick 2–3/combine → opportunity + campaign plan → ≥2 A/B versions → pick A or B → `poster`.
3. **Prove** — `prove` (pick 3–5 expected pilot metrics) → write the derivation logic → one-screen `proof.html`.
4. **Showcase** — pick a storyline → build `proposal.html` (unified report) + `pitch-deck.html` + `prompt-pack.html`.

**Output: `artifacts/Quest<ID>-<NN>/`** — create the new round folder for this run and write all artifacts there; record every decision + its reason in each artifact's embedded `id="capture"` block (no YAML/Markdown files). Grounded, no fabricated numbers; **English only** (artifacts and any reply); Ascentium-branded.
