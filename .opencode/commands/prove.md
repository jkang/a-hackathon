---
description: Run only the PROVE stage (AI produces one most-reasonable numeric forecast; no team decision).
agent: facilitator
---
Run **only the PROVE stage**. Requires the `insight-brief.html` + `campaign-plan.html` captures.

> **Stage opening.** We're now in the **Prove** stage: I produce **one most-reasonable pilot forecast** (funnel targets + the derivation chain behind each number). **No team decision** — you review the finished board.

**Recover upstream (resume) — do this first.** Determine the quest id and find the latest round `artifacts/Quest<ID>-*`. If it's unambiguous (a single round, or the round already established in this session), state it in one line and continue — no need to ask. Ask **only when genuinely ambiguous**. Read the `campaign-plan.html` capture (chosen variant: `pilot` · `budget`) and the `insight-brief.html` capture (`selected_insights` + benchmark). If either is missing, say so and ask the team to run `/plan` (or `/insight`) first.

**This stage has NO team decision.** The AI reads the chosen insights + the chosen campaign and produces **one most-reasonable numeric forecast** — the funnel targets + a derivation chain per metric.

1. Read the insight + plan captures for the pilot hypothesis, markets, budget, and Scout Report benchmarks.
2. Choose the **3–5 funnel metrics** that best prove this pilot's hypothesis (no menu).
3. Set the **most reasonable target** for each — conservative-but-defensible, anchored to a benchmark.
4. Write each metric's **derivation chain**: benchmark → assumption(s) → formula → target.
5. Output **`proof.html`** (**one screen**: pilot framing → funnel with targets → metric tiles → derivation rows); the capture is embedded in its `id="capture"` block — no YAML.

**End the turn with a recap** (what you did + the artifact name/path + the forecast headline). Do **not** present a menu and do **not** ask for a pick. End with: **"The pilot forecast is ready — `artifacts/Quest<ID>-<NN>/proof.html`. Next: run `/showcase`."** Then STOP (do not advance into the next stage).

**Language: English only.** Reply to the team in **English**, regardless of the language they use.
