# Option Menu — choice-first input

**The default way to gather human input.** Never hand the team a blank page. At every gate the AI **drafts a menu of 6–8 grounded options**, the team **selects** (pick N), and may add **"+1 of our own."**

> Why: under time pressure, people freeze and lose minutes on open questions ("who should we target?"). A menu turns a 3-minute blank into a 30-second choice — while the humans still make every call.

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
3. **Pick prompt (one line) — aligned to the menu** — "Reply with your pick (e.g. `1, 3, 5`)." The example **must match the actual menu**: use its real option numbers and pick count (3-option single pick → *e.g. `1`*; 6–8-option pick-2–3 → *e.g. `1, 3, 5`*). Never cite numbers that aren't on the menu. Add nothing after it.

> The options always live in the chat — surface them yourself; never route the team through an artifact to choose.

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

**Insight · audience segments** — "Pick 2–3 fan segments."
1 First-time Gen-Z · 2 Families (school-holiday trips) · 3 Diaspora workers · 4 Sport super-fans · 5 Collector/fandom buyers · 6 Couples/content travellers · 7 Corporate/hospitality guests · 8 Local residents

**Insight · key insights** — "Pick 2–3 to carry into the plan."
1 "Sold out" ≠ attended — optimise for attendance · 2 The away crowd is already in the Gulf · 3 Asia travels for events, not for the Games · 4 Discovery + checkout live on short-video · 5 Qatar's hosting works — the gap is demand · 6 Hangzhou's money was mascot-led

> Market trends are **shown in full, not picked** — the AI curates the merged market read (shifts + hard facts + external opportunities/threats) into the brief.

**Plan · creative idea** — "Pick 2–3 starters to build on (or remix)."
1 Creator squads recruit crews · 2 Bundle a trip + tickets · 3 A branded standing section · 4 A founding-members club · 5 A live cams / behind-the-scenes play · 6 A loyalty/referral loop · 7 A "first time" concierge · 8 A family travel package

**Plan · pilot markets** — "Pick 2 markets."
1 China · 2 Indonesia · 3 Thailand · 4 Vietnam · 5 Philippines · 6 India · 7 Japan · 8 Malaysia

**Prove · forecast** — no menu: the AI produces the forecast directly (no team pick).
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
- ❌ Routing the team through an artifact to see the options — the menu must be printed in the chat.
