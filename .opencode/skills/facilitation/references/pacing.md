# Pacing Template — 14 people × 40 minutes

The default **happy path**. It is a suggestion, not a script (see Prime Directive 6). Each gate = one co-creation loop (see `protocols.md`).

| Time   | Gate          | Lead  | AI does                                   | Human decision                  |
|--------|---------------|-------|-------------------------------------------|---------------------------------|
| 0–2′   | Kick-off      | AI    | confirm brief (mission · 4 gates · research time) → wait for go-ahead → 30s scout summary + first question | —                               |
| 2–8′   | Insight gate  | AI    | research → living brief → AI curates focus bundle + menus → ~6 key insights | key insights (2–3)              |
| 8–22′  | Creative gate | AI    | diverge ~6 ideas → build 2 complete campaigns (A/B) + visuals | the campaign (A or B)           |
| 22–30′ | Pilot metrics | human | write the derivation chains               | 3–5 expected pilot metrics      |
| 30–38′ | Showcase gate | human | generate poster + pitch deck              | visual direction + one-liner    |
| 38–40′ | Converge      | AI    | package and submit                        | confirm                         |

> The run-sheet allows "45′ hands-on + 10′ converge". This design uses **40 minutes** as the creative core and leaves 5–10 min as a submission buffer.

## Per-gate timebox (announce at gate start)

| Gate          | Diverge        | Converge        |
|---------------|----------------|-----------------|
| Insight (8′)  | AI: research + curate all + draft insights 6′ | team picks key insights 2′ |
| Creative (14′) | AI: diverge ~6 ideas + build A/B 10′ | team picks the campaign (A/B) 4′ |
| Pilot metrics (8′) | draft review 2′ | debate 4′ + write derivations 2′ |
| Showcase (8′) | direction pick 2′ | auto-build 5′ + rehearse 1′ |

## Fast mode (when time is tight)

Switch automatically when remaining time < the standard gate budget, or when the team asks to compress.

- **Diverge downgrade**: silent brainstorm → ask just 2–3 active members for ideas (saves ~2′).
- **Converge downgrade**: dot-vote → facilitator proposes 2 candidates and asks for a nod (saves ~2′).
- **Gate skip**: if the team says "we have enough insight", skip the divergence and reuse quest-card data as the seed.
- **Gate merge**: under ~8 min left, merge Pilot metrics + Showcase and assemble poster + board in parallel.

## Dynamic dispatch (human has full control)

The AI must continuously sense remaining time + team intent. On any of these signals, comply immediately:

| Signal | AI action |
|---|---|
| "Enough research, go straight to creative" | skip insight divergence; fall back to quest-card data as seed; enter `plan` |
| "We have only 8 minutes" | enter fast mode; compress gates; assemble in parallel |
| "That vote was wrong — redo it" | re-run the dot-vote protocol only (not the whole gate) |
| "We just want a poster" | call `showcase` alone, using the existing stage HTML captures |
| "Switch the pilot market" | edit the `campaign-plan.html` capture's pilot field; regenerate proof |
| "Skip SWOT, just do a slogan" | call HMW + silent brainstorm from `facilitation` only |

**Response style**: one line — "Got it, switching to X." Never explain the deviation or push back.
