# Market Read — trend scan framework

How to turn market research into the **Market Trends** block: scan, classify, evidence, and phrase each item. Use with the `agent-reach` sub-skill for data.

---

## 1. Scan the categories

Start from the quest card (market size, benchmark, arena), then scan for ~6–8 real items:

| Category | Look for |
|---|---|
| **Behavior** | mobile-first, short-video, social/group travel, experience economy, creator-led discovery |
| **Culture** | creator trust > ads, national pride, "cute economy" / soft-power IP, fandom |
| **Technology / Policy** | visa liberalization, hub airlines, digital collectibles, livestream commerce, entry rules |
| **Hard field facts** | attendance, spend, platform data, sell-through — the numbers that prove the read |

---

## 2. Classify by `kind`

Every item gets exactly one `kind`:

| kind | Meaning | Example shape |
|---|---|---|
| `shift` | a directional behavior / culture move | "Event-led travel is taking a larger share of APAC trips" |
| `fact` | a hard number / field fact | "Nagoya's sell-out still produced empty seats" |
| `opportunity` | an external force the campaign can exploit | "A warm diaspora crowd already lives in-market" |
| `threat` | an external force working against the campaign | "A date freeze pushes long-lead bookings into limbo" |

> The **external opportunities/threats live here** — tagged `kind: opportunity` / `threat`. There is no separate SWOT block.

---

## 3. Evidence requirement

Every item: **trend** (one short line) · **why_it_matters** (the so-what) · **kind** · **source** (URL/doc + as-of date).

- ❌ "Group travel is growing" → ✅ "Group/crew travel is rising — ~X% of travellers now book in groups (source, date)".
- ❌ "Social media matters" → ✅ "Short-video is discovery *and* checkout in the target market — platform GMV ≈ US$X (source, date)".
- ❌ "Entry is hard" → ✅ "Visa-free / low-friction entry since YYYY removes the #1 booking barrier (source, date)".

---

## 4. Report template (the Market Trends block)

```markdown
# Market Trends — {campaign / market}
> Market: {…} · As of: {date} · Status: shown in full, no pick

1. {trend} — {why_it_matters} · [{kind}] (source, date)
2. …
```

---

## 5. Self-check

- [ ] ~6–8 items, balanced across `shift` / `fact` / `opportunity` / `threat`.
- [ ] Each item has a fact/number + source + date.
- [ ] Decision-grade and campaign-specific — no generic industry report filler.
- [ ] Card data used, not duplicated; `[inference]` separated; no fabricated numbers.
