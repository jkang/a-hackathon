# Segmentation Framework (marketing)

How to split an audience into segments, profile them, size them, and choose a target. Use with the `agent-reach` sub-skill for data.

---

## 1. Choose a segmentation basis

Pick **one primary basis** (you may layer a secondary). State it explicitly — vague segmentation produces useless segments.

| Basis | Splits by | Good when |
|---|---|---|
| **Motivation / need** | the job or need-state | consumer campaigns (most common here) |
| **Life-stage** | age / family / career stage | family, travel, gifting decisions |
| **Geography / culture** | market, language, diaspora | multi-market campaigns |
| **Behaviour** | usage / engagement level | loyalty, membership, fandom depth |
| **Value** | spend / propensity | pricing, premium tiers |

> Rule: a segment is only real if it has a **distinct job-to-be-done** and a **distinct trigger**. Otherwise it is just a demographic label.

---

## 2. Segment profile template

```markdown
### Segment {n} — {evocative name}
- **Who**: {demographics · psychographics · geography}
- **Job-to-be-done**:
  - Functional: {…}
  - Social: {…}
  - Emotional: {…}
- **Barriers**: {what stops them today}
- **Triggers**: {what flips them}
- **Channels**: {where to reach them}
- **Size & market potential**: {estimated reach → rough addressable TAM→SAM} (source, date)
```

---

## 3. Size each segment (rough, defensible)

Do not fake precision. Use a simple funnel:

```
Universe      = total addressable audience (e.g. regional fans, global fans of the cause / IP)   [source]
Reachable     = those you can actually reach with the channels               [% × source]
Serviceable   = those the offer fits (market, budget, intent)                 [% × assumption]
```

Then attach value: `potential ≈ serviceable × value_per_user`. Cite the universe number; label percentages as assumptions. If a number is unknown, write "no public data".

---

## 4. Frame the choice — attractiveness × fit (recommendation only)

You may score each segment 1–5 on attractiveness × fit to **help the team** compare — but **do not rank-pick**; the team chooses.

| Segment | Attractiveness *(size × growth × value)* | Fit *(offer, assets, channels)* |
|---|---|---|
| {A} | {1–5} | {1–5} |

- **Attractiveness** — how big / fast-growing / valuable the segment is.
- **Fit** — how well the org's offer, assets and channels match the segment.
- Flag where **both** are high as a soft recommendation; the team picks 2–3.

---

## 5. Segment Map — report template

```markdown
# Audience & Segment Map — {campaign}
> Objective: {…} · Market: {…} · As of: {date}

## Universe
- Total audience: {size} (source, date)
- Basis of segmentation: {motivation / life-stage / geography / behaviour}

## Segments
{repeat the Segment profile template for each of the 6–8 segments}

## Choice framing (soft recommendation)
| Segment | Attractiveness | Fit |
> The team picks 2–3 — the AI does not rank-pick.

## Data gaps
- {what we could not find and why}

---
Sources: {URL + date}
```

---

## 6. Where to look for audience data & trends

- **Digital / social reports** — platform & agency reports (audience size, platform mix, behaviour).
- **Tourism / sports bodies** — arrivals, traveller profiles, event attendance.
- **Fan / community data** — follower counts, community platforms, surveys.
- **Industry analyses** — category growth, consumer trends.
- Always: **source + date**; read the full report; separate fact from `[inference]`.

---

## 7. Self-check

- [ ] Basis of segmentation stated.
- [ ] 6–8 distinct, actionable segments.
- [ ] Each has a JTBD (functional · social · emotional) + barrier + trigger + channels.
- [ ] Sizes cited; percentages labelled as assumptions.
- [ ] Choice framed (attractiveness × fit) — but the **team** picks, not the AI.
- [ ] No fabricated numbers.
