# Collaboration Protocols

Seven lightweight protocols. **Run the Option Menu first at every stage**, then pick by intent. All timings assume **14 people**.

---

## 0. Option Menu — choice-first (DEFAULT, run FIRST)

**Use**: gather input at ANY stage without a blank-page stall.

**Mechanics**:
- The AI **drafts 6–8 grounded options** (from the card + methodology) BEFORE asking.
- Numbered, one line each, concrete and distinct.
- The team **selects** the pick count ("pick 3"), and may add **"+1 of our own."**
- Time: **30 s–1 min** (vs 3 min for an open prompt).

**AI instruction**: present the menu, state the pick count + time, capture the numbers, keep the "+1 own" channel open. See `option-menu.md` for the full design + examples. **Never open with a blank question.**

---

## 1. HMW — "How Might We"

**Use**: turn an insight/tension into a sharp, divergent question before brainstorming.

**Mechanics**:
- One sentence, starts with "How might we…".
- Positive frame (opportunity, not blame).
- Not too broad ("How might we make money?") and not too narrow ("How might we add a red button?").
- Derived directly from the seed insight.

**AI instruction**: output exactly 1 recommended HMW plus 2 alternates; ask the team to pick or edit.

---

## 2. Silent Brainstorm

**Use**: divergence — get ideas from everyone at once, avoid groupthink and anchoring.

**Mechanics**:
- Each person writes 1–2 ideas silently (sticky note / phone / paper).
- No talking during writing.
- Time: **2 min**.
- Then each idea is read out during round-robin.

**AI instruction**: post the prompt + rules, start a 2-minute timer, then say "Pens down — let's share."

---

## 3. Round-Robin

**Use**: collect every idea fast and give everyone airtime.

**Mechanics**:
- Go person by person; each gets ~15 seconds, one idea per turn.
- No critique during collection — record only.
- Repeat rounds until ideas run dry or time ends.

**AI instruction**: record each idea as `{author, text}`. Do not evaluate or reword into your own idea.

---

## 4. Affinity Clustering

**Use**: convergence step 1 — make sense of many ideas.

**Mechanics**:
- Group similar ideas into 3–4 themes.
- Name each theme in a few words.
- Keep original authors attached.

**AI instruction**: cluster faithfully; if a cluster is ambiguous, say so rather than forcing a fit. Do not silently drop ideas.

---

## 5. Dot-Vote

**Use**: convergence step 2 — democratically pick the winner(s).

**Mechanics**:
- Each person gets **2 votes** (dots).
- They may stack 2 votes on one idea or split across two.
- Top 2–3 ideas advance.
- Time: **2 min**.

**AI instruction**: show the tally live; announce the winner(s) without commentary. If the team says "re-vote", re-run immediately.

---

## 6. 1-2-4-All

**Use**: deepen one chosen idea through scaling participation.

**Mechanics**:
- 1 min: each person thinks/notes alone.
- 2 min: pairs merge ideas.
- 4 min: quads merge further.
- 5 min: all share back and consolidate one enriched version.

**AI instruction**: capture additions at each level; the output is one strengthened concept, not a new shortlist.

---

## Choosing a protocol (quick map)

| Goal | Protocol |
|---|---|
| **Gather input at any stage (start here)** | **Option Menu (pick N, +1 own)** |
| Frame the problem | HMW |
| Generate many ideas from all 10 | Option Menu → Silent Brainstorm → Round-Robin |
| Make sense of many ideas | Affinity Clustering |
| Choose the winner | Dot-Vote |
| Deepen one idea | 1-2-4-All |
| Re-run / override | call the single protocol directly |
