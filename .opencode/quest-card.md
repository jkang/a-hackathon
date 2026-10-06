# Quest Card — the single source of quest truth

This toolkit is a **reusable marketing-hackathon engine**. The stage skills, sub-skills, `facilitation` engine, and `ascentium-brand` executor are **quest-agnostic**: they know *how* to run insight → plan → prove → showcase, but they do **not** know *which* client, mission, market, budget, or Victory Conditions a run is about.

All quest-specific facts live in **one place**: the **quest card** (the challenge brief handed to each team). The skills read the card — never their own hard-coded assumptions.

## Where quest data lives

- **The activity material** (e.g. `quest-cards.html` in this project) is the canonical card: it carries the Scout Report, War Chest, Victory Conditions, and the How Might We.
- **This file** is the *contract* — the schema a card must provide so every gate and every template can consume it.
- **The `.opencode/` skills contain no quest facts.** Any concrete client, market, budget, or benchmark in a skill or template is a placeholder (`{{...}}`) to be filled from the card at run time.

## The contract (fields every card must provide)

```yaml
# quest.yaml — the data a card supplies; the engine consumes it.
quest:
  id: "A"                          # short label shown in artifacts (e.g. "Quest A")
  client: "{client / brand / IP holder}"
  mission: "{one-line mission from the card}"
  market_scope: "{e.g. Asia-wide, global}"       # the challenge's own target market
  doc_type: "Campaign Plan | Membership Design"  # plan-gate artifact flavor

  war_chest:
    full: "{USD full approved budget}"          # the unlock target the pilot de-risks
    mvp_unlock: "{USD pilot budget}"            # a % of full (the pilot envelope)
    pilot_window: "3 months"
    pilot_markets_hint: "{how many markets, e.g. 2}"

  victory_conditions: [ "{4–5 full-scale targets the metrics must predict}" ]

  scout_report:                                  # benchmarks the metrics must cite
    gold_standard: "{best-in-class benchmark}"
    cautionary_tale: "{what went wrong elsewhere}"
    arena: "{the market / competition context}"
    benchmarks: [ "{named benchmark facts + numbers}" ]

  how_might_we: "{the HMW from the card}"

  # ---- visual contract: drives the accent + key visual in EVERY artifact ----
  accent: "{brand accent token}"                 # "orange" (default) | "teal" — from tokens.css
  accent_values:                                 # concrete CSS values (must come from tokens.css)
    accent: "#FF6611"
    tint:   "#FFF0E7"
    line:   "#FFD1B8"
    deep:   "#B24000"

  key_visual_motif: "{the hero illustration topic, e.g. 'stadium + tickets'}"
  key_visual_svg: |                              # inline SVG <symbol id="illo"> for the motif
                                                # deck frame = 480×360; poster style arts = 1200×500 (match each frame)
    <symbol id="illo" viewBox="0 0 480 360" preserveAspectRatio="xMidYMid slice">…</symbol>

  poster_styles:                                 # optional override of the 3 poster style names
    a: "{style A name}"  b: "{style B name}"  c: "{style C name}"

  pilot_market_hints: [ "{candidate markets for the pilot menu}" ]
  language_hints: [ "{localization languages}" ]
```

## How the engine consumes it

| Consumer | Reads from the card |
|---|---|
| `/start`, `/run` | `quest.id`, `client`, `mission`, `market_scope` |
| `insight` gate | `scout_report` + `client` + `market_scope` (the research chain) |
| `plan` gate | `how_might_we`, `war_chest.mvp_unlock`, `victory_conditions`, `pilot_market_hints` |
| `prove` gate | `scout_report.benchmarks`, `war_chest.mvp_unlock`, `war_chest.pilot_window`, `war_chest.pilot_markets_hint` |
| `showcase` gate | `accent`, `key_visual_motif`, `key_visual_svg`, `poster_styles` |
| **every HTML template** | `accent` + `accent_values` (injected as `--accent` / `--accent-tint` / `--accent-line` / `--accent-deep`) and `key_visual_svg` |

## Accent & key-visual rules (locked)

1. **Accent is a quest property, not a fixed A/B enum.** A card declares `accent` (one of the brand's accent tokens in `ascentium-brand/references/tokens.css`). The agent injects `accent_values` as inline CSS variables on each artifact's `<body>`:
   `--accent` · `--accent-tint` · `--accent-line` · `--accent-deep`.
2. **No self-invented colours.** `accent_values` must trace to `tokens.css`. If a quest genuinely needs a new accent, add the token to `tokens.css` first, then reference it.
3. **Key visual is a quest property.** The card ships `key_visual_svg` (one inline `<symbol id="illo">`; the deck frame uses `viewBox="0 0 480 360"`, the poster style arts use `viewBox="0 0 1200 500"` — match each frame). The templates have a single `{{KEY_VISUAL_SVG}}` slot; the agent fills it. The built-in stadium / panda illustrations are **example motifs only**, not part of the engine.
4. **Poster styles are tone descriptors, not quest labels.** The three styles (A/B/C) are art directions the team maps to the current quest; a card may rename them via `poster_styles`.

## Output layout (where a run writes)

Every run writes into **one round folder** at the repo root:

```
artifacts/Quest<ID>-<NN>/
```

- `<ID>` = the card's `id`, normalized: strip any leading "Quest" and spaces, then prefix `Quest` (e.g. id `A` → `QuestA`, id `C` → `QuestC`).
- `<NN>` = a 2-digit round number. Pick the **next free** one by scanning `artifacts/Quest<ID>-*` (none → `01`; existing `01`,`02` → `03`).
- **`/run`** creates a new round folder at the start and writes every artifact into it. **`/start`** is a briefing only — it creates **no** folder and **no** artifact; the **first gate that writes** creates the round folder. A **single-gate command** (`/insight` … `/showcase`) writes into the **latest** round for that quest — create `-01` if none exists.
- **Never overwrite a previous round.** A repeat run always increments `<NN>`.
- Round contents (**HTML only** — no YAML/Markdown): `insight-brief.html` · `campaign-plan.html` · `poster.html` (+ `poster-a|b|c.html`) · `proof.html` · `pitch-deck.html` · `prompt-pack.html` · `proposal.html`. Each stage HTML carries its decisions in an embedded `<script type="application/json" id="capture">` block.
- Builder steps run with `--dir artifacts/Quest<ID>-<NN>/` (`build-posters.py`, `build-proposal.py`).

`artifacts/` is gitignored (live run output); checked-in examples live under `demo-examples/`.

## When adding a new quest

1. Write a new card (a challenge brief) that fills every field above.
2. Do **not** edit any skill or template — the engine is already generic.
3. If the new quest needs an accent or illustration not already available, add the token/SVG to the card (and, for a brand colour, to `tokens.css`), not to a template.
