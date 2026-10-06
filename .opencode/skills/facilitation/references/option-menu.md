# Option Menu — choice-first input

**The default way to gather human input.** Never hand the team a blank page. At every gate the AI **drafts a menu of 6–8 grounded options**, the team **selects** (pick N), and may add **"+1 of our own."**

> Why: under time pressure, people freeze and lose minutes on open questions ("what truths do you see?"). A menu turns a 3-minute blank into a 30-second choice — while the humans still make every call.

## How to build a menu (AI does this BEFORE asking)

1. **Source** the options from the quest card + the stage's methodology (+ `agent-reach` only if a fact is missing). Options must be *grounded*, not random.
2. **6–8 options**, each **one short line**, **concrete and distinct** (no two that say the same thing).
3. **Number them** so people can reply with numbers ("1, 4, 6").
4. **Always append**: `+1 of our own` — the team may add 1–2 items the menu missed.
5. State the **pick count** ("pick 3") and the **time** ("30 seconds").

## Ground the menu in research (mandatory in the insight gate)

A menu is only as good as its options. **Generic labels are worthless.** Before drafting the menu — especially in the **insight gate** — the AI **gathers real facts** via `agent-reach` (web / social / reports) plus the quest card, and turns them into **data-backed mini-insights**.

- ❌ "Group travel" → ✅ "Crew/group travel is rising — ~X% of travellers now book in groups (source)".
- ❌ "Fans like creators" → ✅ "Creator-led content out-converts brand ads in the target market (platform benchmark)".
- ❌ "Entry is hard" → ✅ "Visa-free / low-friction entry for the target market since YYYY → removes the #1 booking barrier".

Each option should carry a **fact, number, or named behavior**; cite the source in the option (or keep it in the capture) so it is defensible.

> The team still **selects**; the AI **grounds** the options. Research effort sits with the AI; judgment sits with the team.

## Deliver the menu in the chat (never send them to the HTML)

The menu lives in the **chat message**, not in an artifact. Print the numbered options directly in your response so the team can reply with numbers. **The HTML is the record of the outcome, not the interface for making the choice.**

Every turn that produces output ends with a short wrap-up:

1. **Recap (2–4 lines)** — what you just did + the artifact produced (name + path) + the key takeaways.
2. **The menu, inline** — print it in the message (numbered, with each option's supporting fact).
3. **Pick prompt** — "Reply with your pick (e.g. `1, 4, 6`) — no need to open the HTML."

> Never tell the team to open `insight-brief.html` / `campaign-plan.html` / `proof.html` / `proposal.html` to see the options and then come back. Surface the options yourself.

## Anatomy

```
MENU · <gate> — pick <N> (30s), or +1 of your own
1) <option>            5) <option>
2) <option>            6) <option>
3) <option>            7) <option>
4) <option>            8) <option>
+1) ________________
```

## Menu examples (per gate)

> These are **format examples only** — replace each list with options grounded in the current quest card (+ `agent-reach` findings).

**Insight · trends** — "Which 3 shifts matter most?"
1 Mobile-first short-video is where fans decide · 2 Creator trust beats ads · 3 Group/experience travel · 4 Visa liberalization · 5 The fan-membership economy · 6 Diaspora return-travel · 7 Post-event tourism rebound · 8 AI-personalized content

**Insight · audience** — "Pick 3 fan segments."
1 First-time Gen-Z · 2 Families (school-holiday trips) · 3 Diaspora workers · 4 Sport super-fans · 5 Collector/fandom buyers · 6 Couples/content travellers · 7 Corporate/hospitality guests · 8 Local residents

**Insight · moment of truth** — "Pick 1–2 moments."
1 Team-qualification news · 2 Ticket-sale day · 3 The creator film drop · 4 The airline stopover · 5 School-holiday booking window · 6 Match day · 7 The medal moment · 8 The 2 a.m. viral clip

**Plan · creative idea** — "Pick 2–3 starters to build on (or remix)."
1 Creator squads recruit crews · 2 Bundle a trip + tickets · 3 A branded standing section · 4 A founding-members club · 5 A live cams / behind-the-scenes play · 6 A loyalty/referral loop · 7 A "first time" concierge · 8 A family travel package

**Plan · pilot markets** — "Pick 2 markets."
1 China · 2 Indonesia · 3 Thailand · 4 Vietnam · 5 Philippines · 6 India · 7 Japan · 8 Malaysia

**Prove · metrics** — "Pick 3–5 sub-metrics."
1 Ticket-intent rate · 2 CAC per hold/member · 3 Creator reach · 4 Group-booking ratio · 5 Bundle attach · 6 Conversion rate · 7 Merch sell-through · 8 Organic reach

**Showcase · storyline** — the 5 storylines are already a menu (Classic / Hero's Journey / Big Reveal / Demo / Trailer).

## Rules

- **Never open with a blank question.** A menu always comes first.
- Keep it **6–8** — fewer feels thin, more overwhelms.
- Options must be **specific**, never generic filler.
- The **"+1 own"** channel is mandatory — it preserves human creativity beyond the menu.
- The AI **records the selection verbatim** and never quietly swaps a menu item for its own idea.

## Anti-patterns

- ❌ An open "what do you think?" with no menu.
- ❌ 15+ options (decision paralysis).
- ❌ Vague options ("do better marketing").
- ❌ No "+1 own" escape hatch (menus shouldn't cap creativity).
- ❌ The AI picking the options for the team instead of the team picking.
- ❌ Sending the team to open the HTML to see the options — the menu must be printed in the chat.
