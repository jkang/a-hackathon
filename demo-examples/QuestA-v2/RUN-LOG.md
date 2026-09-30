# Quest A — RUN-LOG (runner · autopilot)

**Mode**: `runner` — fully automated; every choice made by the AI (no human input, no HITL stops).
**Quest**: A — Doha 2030 ticketing. **Client**: OCA — Doha 2030 Ticketing & Fan Engagement Unit.
**Data as of**: 2026-09-29 (live research via `agent-reach` → Exa search + Jina Reader).
**Output**: `QuestA-v2/` — `insight.yaml` · `plan.yaml` · `metrics.yaml` · `insight-brief.html` · `campaign-plan.html` · `poster.html` · `proof.html` · `pitch-deck.html` · `prompt-pack.html` · `proposal.html`.

---

## GATE 1 · INSIGHT — research → ~6 insights → auto-pick 2–3

**Live research (agent-reach → Exa / Jina), highlights used:**
- Thailand outbound **13.06M in 2025** (+11.4%, all-time high; spend +29.5%) — Nation Thailand 2026.
- Indonesia outbound **8.947M in 2024** (+19.0%) — BPS / statbase 2025.
- Aichi–Nagoya 2026: planned 2.75M tickets, **~700–800K sold by late Aug**; **<60% sold for 8 big-stadium sports incl. football**, badminton/fencing >90% — Kyodo 2026-09-25.
- TikTok **460M MAU in Asia** (ID 160M, VN 70M, TH 50M) — TikTok Newsroom 2025.
- Qatar 2022: **1.4M international visitors, 3.18M tickets, 96.3% attendance** — FIFA Annual Report 2022.
- Hangzhou 2022/23: **3.05M tickets, RMB 610M ticket revenue, ~90% attendance, RMB 5.316B market development, RMB 700M merch** — card + China Daily 2023.
- Qatar visa-free map: **CN/ID/SG/TH/MY yes; PH/VN no** — Visit Qatar 2026.

**~6 key insights drafted (all data-backed, sourced):**
1. Asia outbound is at a record high, but no Games host has ever aimed it at Doha.
2. Demand must be manufactured — and it fails by sport (Nagoya: football <60%, badminton >90%).
3. Asia is the most mobile-first, creator-trusting fan base on earth (460M TikTok MAU; 74% football fans).
4. Qatar's visa-free map — not desire — decides the addressable market (PH/VN excluded).
5. Doha already proved it can fill a stadium with the world (Qatar 2022: 96.3% attendance).
6. Belonging beats browsing: paid supporter clubs + early group booking convert fandom into ticket priority.

**Auto-picked to deep-dive:** `#1, #2, #3`.
> *Reason*: these three carry the strongest benchmark backing (outbound records + the Nagoya demand warning + the creator channel), and together they dictate both the market choice (visa-free, high-volume Asia) and the method (creator-led recruitment). #4 is used as a market-selection constraint; #5/#6 support the proof and the offer.

`chosen 1,2,3 because` they are the most defensible and they map 1:1 to the campaign's market, method and metric design.

---

## GATE 2 · PLAN — 6 ideas → auto-pick/combine → A/B → auto-pick → poster

**~6 ideas diverged:**
1. THE AWAY END — creator squads recruit national away crews.
2. THE SUPPORTER PASSPORT — paid fan membership with priority tickets.
3. FLY TOGETHER — Qatar Airways fly-stay-ticket bundle.
4. THE FAMILY STAND — Nov cool-season family bundles.
5. GOLDEN TICKET DROPS — limited national allocations in waves.
6. #MYDOHA2030 — UGC fan-film challenge.

**Auto-picked / combined:** `1 + 2 + 3` → **THE AWAY END** (creator-led crews + Supporter Passport + Fly Together bundle).
> *Reason*: #1 is the only idea that builds an **owned audience** (reusable for the 18-month rollout); #2 monetises the "belonging" insight and creates early group bookings; #3 removes the cost/visa friction that stalls Asia Gen-Z. Combined, they cover reach → conversion → retention in one system.

**Pilot markets:** Indonesia + Thailand; **control**: Malaysia.
> *Reason*: ID and TH are the two largest, fastest-growing, **visa-free** Asia outbound markets with the biggest TikTok bases (ID 160M, TH 50M). Malaysia is a matched, visa-free market, so holding it out cleanly isolates the treatment.

**A/B versions:**
- **A · THE AWAY END** — creator-led crews + Supporter Passport (community-led; insights 1+3+6).
- **B · FLY TOGETHER** — bundle-led, OTA/price play (insights 1+4/5).

**Auto-picked:** **A**.
> *Reason*: A builds a durable, owned fan pipeline and is the most reach-efficient under USD 1.5M (Asia's creator economy is the cheapest distribution, 460M TikTok MAU). B depends on partner-funded discounting and buys reach rather than an audience — parked as the alternative.

**Poster direction:** "Stadium roar" (packed, loud national away end) · one-liner: *"Book with your crew. Arrive as a nation."*

**Poster styles (3 offered → auto-picked A):** A · **Matchday Roar** (bold sports editorial), B · **Supporter Passport** (travel/ticket), C · **Midnight Minimal** (Swiss typographic). Auto-picked **A**.
> *Reason*: this is a mass fan-energy campaign, so the loud accent-hero sports editorial carries the "away end" idea best; B/C remain in `poster.html#style-b|#style-c` for the team to swap in the Showcase deck. The crop bug was also fixed (hero frame and art are both locked to a 1200:500 ratio).

`chosen A because` it is the most defensible (benchmark-backed) and best fits the Victory Conditions; `chosen ID+TH because` they are the biggest visa-free creator markets.

---

## GATE 3 · PROVE — pilot metrics → auto-pick → derivation logic

**Pilot-metrics menu (auto-picked 5, each benchmark-defended):**
1. **Creator reach (6 wks)** — target 150M *(benchmark: TikTok 460M Asia MAU; VC = 500M impressions)*
2. **Crew sign-up rate** — target 4.0% *(benchmark: Meta lead conv. 7.72%; arts & events FB 9.34%)*
3. **Group-booking ratio** — target 45% *(benchmark: Asian fans travel as crews; ~4 in 5 group trips via agent)*
4. **Cost per crew member (CAC)** — target ≤$10 *(benchmark: FB arts CPL $18.17; Google Events $26.84)*
5. **Fly-stay bundle attach rate** — target 20% *(benchmark: Discover Qatar stopover from $14/night; QR 170+ destinations)*

**Derivation logic:** each target shows its chain — **benchmark → assumption → formula → target** (see `proof.html` and `metrics.yaml`).

`chosen these 5 because` each is a pilot target measurable weekly over 3 months, each cites a credible external benchmark, and each carries a visible derivation chain. Output is a single one-screen board; no Go/No-Go, cost-benefit or scale-up.

---

## GATE 4 · SHOWCASE — storyline → auto-pick → build

- **Storyline:** **Hero's Journey** (`hero`) — the fan's transformation from alone-on-the-feed → away-crew member → stadium roar.
  > *Reason*: the campaign's core is a change in *belonging*, which is a narrative arc, not a discount; hero fits a consumer fan-engagement pitch and defaults to the storyboard signature.
- **Poster on/off:** **yes** (the poster is a Create-stage deliverable and the campaign's key visual).
- **Signature element:** storyboard (6 frames) + poster beat.
- **Visual direction:** "Stadium roar." · **One-liner:** "Book with your crew. Arrive as a nation."
- **Bonus media:** song (Suno) + video (Runway) + image (GPT) prompts written to `prompt-pack.html`.

**Built:** `proposal.html` (unified report) + `pitch-deck.html` (**11-slide** hero deck — 5-minute cap, ≤12) + `prompt-pack.html`.

`chosen hero because` it best carries the belonging narrative; `poster on because` it is a required Create-stage visual.

---

## Auto-decisions summary (13)

| # | Node | Choice | Reason (one line) |
|---|---|---|---|
| 1 | Key insights | 1, 2, 3 | Strongest benchmarks; dictate market + method |
| 2 | Idea | 1+2+3 combined | Owned audience + monetised belonging + friction removed |
| 3 | Pilot markets | Indonesia + Thailand | Biggest, fastest-growing, visa-free, biggest TikTok bases |
| 4 | Control | Malaysia | Matched + visa-free → clean isolation |
| 5 | Variant | A (THE AWAY END) | Builds an owned pipeline; most reach-efficient under $1.5M |
| 6 | Poster direction | "Stadium roar" | Makes the away crowd visible and loud |
| 7 | Metric 1 | Crew sign-up rate | Reach → conversion proxy; Meta 7.72% benchmark |
| 8 | Metric 2 | CAC per crew | Efficiency gate; FB/Google CPL benchmarks |
| 9 | Metric 3 | Creator reach | Feeds the 500M-impression VC |
| 10 | Metric 4 | Group-booking ratio | Proves the crew behaviour |
| 11 | Metric 5 | Bundle attach rate | Proves monetisation, not just intent |
| 12 | Derivation logic | benchmark → assumption → formula → target | Every number shows its chain; no bare claims |
| 13 | Storyline | Hero's Journey | Belonging is an arc, not a discount |

---

## Grounding, sources & caveats

- **No fabricated numbers.** Every figure carries a source; see `insight.yaml` `source_note` and each HTML footer.
- **Date risk (flagged, not resolved):** the OCA proposes moving the Asian Games to the year before the Olympics — **Doha 2030 → 2031** (Xinhua, 2026-04-27). The pilot budget should stay phased and the campaign clock kept flexible.
- **Unverifiable:** Doha 2030 ticket prices are not public → the USD 60 blended ticket value is a stated assumption (between Hangzhou ~USD 22 and Qatar 2022 ~USD 215).
- **Scope:** the card is Asia-wide; the MVP pilot runs in 2 priority Asian markets (ID + TH), with China as the phase-2 beachhead. PH/VN are excluded from paid push because they are not visa-free.
- **Benchmark honesty:** each pilot target is set *below* raw channel benchmarks (cold audience discount) and shows its derivation chain, so the number is defensible.
