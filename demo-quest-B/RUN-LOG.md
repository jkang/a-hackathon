# Quest B — Dry Run Log

**Facilitator:** ROBOT FACI-07 (quest-runner) · **Mode:** simulated 10-person team · **Duration:** 40:00
**Note:** Dry run. Team inputs below are *simulated* (10 global/IP marketers) to exercise the full chain, including the **membership / founding-offer** branch and the **teal** brand variant.

---

## 0:00–0:02 · Kick-off (AI)

> FACI-07 >> Gate **KICK-OFF**. Reading the Quest B card.

**Scout summary (30s):**
- Chengdu Panda Base: **200+ pandas**, ¥55 entry; weekends cap ~45K (capacity ceiling).
- 2024 Spring Festival: **442K visitors in 7 days**; tickets "gone in seconds".
- International share only **~5%**; fame is global but monetization is local.

**First question:** *"As a global/IP leader, what truth / opportunity / trap do you see in your market?"*

---

## 0:02–0:08 · INSIGHT gate (human)

**Protocol:** silent brainstorm (2′) → round-robin (3′) → affinity cluster → team confirms seed insight.

**10 market truths (verbatim):**
1. Fans want to belong, not just watch — Mei (Chengdu)
2. He Hua's fame is emotional, not transactional — Kenji (JP)
3. Japan fans already pay for panda merch (Xiang Xiang ¥2.7B) — Rina (JP)
4. Indonesians love Fu Bao clips but have nowhere to join — Budi (ID)
5. A membership must feel like adoption, not a subscription — Sari (ID)
6. Conservation-first — hard-sell risks backlash — Lucas (BR)
7. Arabic-language panda content barely exists — Aisha (SA)
8. Physical merch is the emotional proof of belonging — Tan (SG)
9. There is no English-first content engine today — Grace (US)
10. Fu Bao's Korea fanbase is an instant founding cohort — Nina (KR)

**Clusters:** Belonging > watching · Conservation-proofed monetization · Localized content & merch

> **TEAM DECISION (confirmed):** seed insight —
> *"Pandas are Earth's most beloved IP, but the Base captures almost none of that love beyond the ¥55 gate. Japan and Korea proved one panda can mint billions — turn 'the world's most famous zoo' into a global membership brand built on belonging."*

→ `yaml/insight.yaml` · `html/insight-brief.html`

---

## 0:08–0:22 · PLAN / CREATIVE gate (human · heaviest)

**HMW:** *"How might we turn millions of panda viewers into paying global members who feel they belong?"*

**Diverge — 12 ideas:** Panda Passport (Mei) · Adopt-a-Panda (Kenji) · Founding 100,000 (Rina) · Panda Cam+ (Budi) · Global merch store (Sari) · English-first engine (Grace) · Fu Bao fanbase funnel (Nina) · Conservation impact tracker (Lucas) · Arabic/ID feeds (Aisha) · Birthday live events (Tan) · Digital passport stamps (Budi) · Member-only BTS (Mei)

**Dot-vote (2 each):** Panda Passport **7** · Adopt-a-Panda **5** · Founding 100,000 **4** · Panda Cam+ **3** · Global store **2**

> **TEAM DECISION (winner):** **PANDA PASSPORT** — slogan *"One bear. One world. One membership."*

> **TEAM DECISION (offering — membership branch):**
> - **Panda Pal** (Free) — newsletter, digital badge, public content
> - **Founding Member** ($30/yr) — live cams, adoption certificate, 10% merch, Founder badge
> - **Patron** ($120/yr) — all + welcome kit, priority experiences
> - **Founding offer:** *Founding 100,000 — first 100,000 get a numbered digital passport, adoption certificate and welcome kit at $30/yr, Founder badge for life.*

> **TEAM DECISION (pilot):** markets **Japan + Indonesia** · 3 months · success = conversion ≥3% & CAC ≤$8, no No-Go.

> **TEAM DECISION (budget split of USD 1.1M):** JP paid 200K · JP partner 150K · ID paid 250K · ID partner 150K · Global content 200K · Merch 100K · Measurement 50K.

AI assembled: positioning + 4Ps (membership tiers) + experiment + measurement setup.

→ `yaml/plan.yaml` · `html/campaign-plan.html` (DOC_TYPE = "Membership Design")

---

## 0:22–0:30 · PROVE gate (human)

**Team picked 5 sub-metrics and set thresholds:**

| # | Sub-metric | Benchmark ref | Target | Go | No-Go |
|---|---|---|---|---|---|
| 1 | Member conversion rate | Card goal: 1M members | 4.0% | ≥3.0% | <1.5% |
| 2 | CAC per member | Fu Bao 2.7M merch units | ≤$6 | ≤$8 | >$12 |
| 3 | Merch sell-through | Fu Bao +60% units | 12% | ≥10% | <5% |
| 4 | Organic reach (3-mo) | Card goal: 10M followers | 2.0M | ≥1.5M | <0.8M |
| 5 | Overseas member share | Card goal: 20% overseas | 20% | ≥15% | <8% |

**Go/No-Go rule (set before data):** unlock if ≥3 of 5 hit Go and none hit No-Go; else iterate once; stop if any No-Go at mid-point.

**Sample numbers (W1→W6):** conversion 1.4%→4.1% · CAC $10.50→$6.10 · sell-through 4%→13% · reach 0.3M→2.4M · overseas 12%→23%.

**Cost-benefit (AI):** pilot USD 1.1M → projected USD 3.2M · **ROI 2.9x** · payback <10 months → **verdict GO**.

→ `yaml/metrics.yaml` · `html/proof.html` · `html/kpi-dashboard.html`

---

## 0:30–0:38 · SHOWCASE gate (human · AUTO build)

Directions offered: **(a) Founding membership** (teal, warm/premium) · (b) The panda passport (travel motif) · (c) Conservation impact (documentary).
> **TEAM DECISION:** direction **(a) Founding membership**. One-liner: *"Turn the world's most loved bear into the world's biggest membership."*

AI built the poster + 7-beat pitch deck (AUTO), **teal** brand variant.

→ `html/poster.html` · `html/pitch-deck.html`

---

## 0:38–0:40 · Converge (AI)

Packaged: 3 YAML captures + 6 branded HTML artifacts. Team confirmed.

---

## Artifacts

```
demo-quest-B/
├── yaml/   insight.yaml · plan.yaml · metrics.yaml
├── html/   insight-brief.html · campaign-plan.html · proof.html · kpi-dashboard.html · poster.html · pitch-deck.html
└── shots/  6 rendered screenshots (teal)
```

## Deliverable coverage check (Quest B)

| Card deliverable | Artifact | ✓ |
|---|---|---|
| Pilot membership design (2 overseas markets, 3mo) | campaign-plan.html | ✓ |
| Experiment plan & measurement setup | campaign-plan.html | ✓ |
| Founding-member offer + hero visual | campaign-plan.html + poster.html | ✓ |
| Go / No-Go criteria | proof.html | ✓ |
| 3–5 self-defined MVP sub-metrics | proof.html | ✓ |
| KPI dashboard (implied by measurement setup) | kpi-dashboard.html | ✓ (bonus) |

## Notes vs Quest A

- **Brand:** teal accent instead of orange (ascentium-brand token swap). ✓
- **Branch:** `offering.type = membership` → tiers + `founding_offer` rendered; DOC_TYPE = "Membership Design". ✓
- **No over-commercialization:** conservation-first framing kept central (a soft-sell tone throughout). ✓

## Human decision points exercised

seed insight · winning idea · membership tiers & founding offer · pilot markets · budget split · 5 metrics · Go/No-Go thresholds · visual direction & one-liner — **8 team decisions; the AI decided none of them.**

---

## v2 enrichment (audience · trend · demand · scenario)

**Insight gate now also captures:**
- **Market trends** (2–3): the fan-membership economy · cute-economy soft power · conservation-conscious spending.
- **Audience segments** (3, with JTBD): Panda Parents (protectiveness) · Global Collectors (status) · Wholesome Families (comfort) — each with barrier + trigger.
- **Moment of truth**: the 2 a.m. moment, when a panda clip goes viral · TikTok/Reels · a birthday livestream / World Panda Day.

**Plan gate now anchored before ideating:**
- **Creative brief**: *for Panda Parents, whose emotional need is protectiveness, at the moment a panda clip goes viral — we offer founding membership, so they adopt and belong.*
- **Scenario canvas** (time · place · event): the 2 a.m. viral clip → birthday livestream → holiday gifting.

**Pitch deck upgraded** to a visual-first, full-screen (16:9 auto-scale, ←/→ nav) deck that **embeds** the artifacts — all rendered in the **teal** brand variant.
