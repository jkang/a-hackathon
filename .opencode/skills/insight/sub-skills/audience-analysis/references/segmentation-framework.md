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
- **Needs & motivations**: {why they act}
- **Barriers**: {what stops them today}
- **Triggers**: {what flips them}
- **Channels**: {where to reach them}
- **Size**: {estimated reach} (source, date)
- **Market potential**: {size × value / propensity → rough TAM→SAM}
- **Trend**: {growing / flat / declining} — {evidence, source, date}
- **Priority**: Tier {1/2/3}
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

## 4. Prioritise — attractiveness × fit

Score each segment 1–5 and plot; recommend the **Tier 1** target(s).

| Segment | Attractiveness *(size × growth × value)* | Fit *(offer, assets, channels)* | Priority |
|---|---|---|---|
| {A} | {1–5} | {1–5} | Tier 1 / 2 / 3 |

- **Attractiveness** — how big / fast-growing / valuable the segment is.
- **Fit** — how well the org's offer, assets and channels match the segment.
- Pick the segment(s) where **both** are high; call out why others are deferred.

---

## 5. Segment Map — report template

```markdown
# Audience & Segment Map — {campaign}
> Objective: {…} · Market: {…} · As of: {date}

## Universe
- Total audience: {size} (source, date)
- Basis of segmentation: {motivation / life-stage / geography / behaviour}

## Segments
{repeat the Segment profile template for each of the 3–5 segments}

## Prioritisation
| Segment | Attractiveness | Fit | Priority |

## Target recommendation
- **Primary target (Tier 1):** {segment} — because {reason}
- **Secondary:** {segment}
- **Deferred:** {segment} — because {reason}

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
- [ ] 3–5 distinct, actionable segments.
- [ ] Each has a JTBD + needs + triggers.
- [ ] Sizes/trends cited; percentages labelled as assumptions.
- [ ] Target recommendation made (attractiveness × fit).
- [ ] No fabricated numbers.
