# Pacing Template — 14 people × 40 minutes

The default **happy path**. It is a suggestion, not a script (see Prime Directive 6). Each gate = one co-creation loop (see `protocols.md`).

| Time   | Gate          | Lead  | AI does                                   | Human decision                  |
|--------|---------------|-------|-------------------------------------------|---------------------------------|
| 0–2′   | Kick-off      | AI    | 30s scout summary + first question        | —                               |
| 2–8′   | Insight gate  | human | cluster market truths                     | confirm the seed insight        |
| 8–22′  | Creative gate | human | assemble the winner into a plan           | big idea + 2 pilot markets      |
| 22–30′ | Pilot metrics | human | write the derivation chains               | 3–5 expected pilot metrics      |
| 30–38′ | Showcase gate | human | generate poster + pitch deck              | visual direction + one-liner    |
| 38–40′ | Converge      | AI    | package and submit                        | confirm                         |

> The run-sheet allows "45′ hands-on + 10′ converge". This design uses **40 minutes** as the creative core and leaves 5–10 min as a submission buffer.

## Per-gate timebox (announce at gate start)

| Gate          | Diverge        | Converge        |
|---------------|----------------|-----------------|
| Insight (8′)  | trends 2′ + audience 2′ + moment 1′ + truths 2′ | cluster + confirm 1′ |
| Creative (14′) | anchor + scenario 2′ + silent 2′ + round-robin 6′ | affinity + dot-vote 2′ + 1-2-4-All 5′ + market pick 3′ |
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
