# Media Prompt Guide — bonus song / video / image

Bonus (optional) layer. Each group **optionally** generates a song, a video, or a hero image using external tools, then embeds the result in the Showcase report. The AI writes the prompts (from the `campaign-plan.html` capture); the human generates and curates.

## Tool list (1 primary + 1 backup each)

| Type | Primary | Backup | Output |
|---|---|---|---|
| Song | **Suno** (suno.com) | Udio | `.mp3` |
| Video | **Runway Gen-3** (runwayml.com) | Kling | `.mp4` |
| Image | **GPT** (ChatGPT image generation) | Kimi | `.png` |
| Storyboard | **Kimi** (kimi.moonshot.cn) | GPT (ChatGPT image generation) | `.png` (one 16:9 sheet) |

---

## 1. Song — Suno

Two inputs: **Style of Music** + **Lyrics**.

**Style of Music** (paste one line):
> anthemic stadium pop, crowd chant, driving percussion, uplifting, 110 BPM

**Lyrics** — use structural tags so Suno places sections correctly:
```
[Intro]
We don't visit... we arrive.

[Verse 1]
Late night, phone in my hand
A film drops — I see the stand

[Chorus]
THE AWAY END — your team, your continent, your moment
We don't visit, we arrive

[Outro]
(chant) A-WAY END! A-WAY END!
```

**Rules:**
- Slogan → the Chorus hook (it must be repeatable / chantable).
- The emotional job → the theme of the verse.
- Keep the whole lyric ≤ ~2000 characters.
- Generate 2 versions, pick one, download `.mp3`.

---

## 2. Video — Runway Gen-3

One natural-language scene prompt. Structure:

> Cinematic [N]-second shot: **[subject] [action] [setting] [lighting] [camera] [mood]**

Example:
```
Cinematic 5-second shot: a 22-year-old fan scrolls TikTok at midnight in a dim bedroom,
the phone glows the brand accent with the campaign's words, they look up with rising
excitement, camera whip-pans to the campaign's hero moment — warm brand grade, handheld energy, 16:9
```

**Rules:**
- Base the scene on the **moment of truth** (when / where / event).
- Keep to ONE shot, ≤ 15 seconds (short clips embed cleaner).
- Mention brand color and any on-screen text.
- Download `.mp4`.

---

## 3. Image — GPT (ChatGPT image generation)

One natural-language prompt (no Midjourney params). Describe the layout **and write out every word you want rendered**:

```
Generate a bold event poster. Giant white text "{{CAMPAIGN NAME}}" centered at the top,
subtitle "{{TAGLINE}}" right below it. Background is the brand accent hex (#FF6611).
At the bottom, a silhouetted hero motif. Clean modern typography, high contrast,
no watermark, no logo. 16:9.
```

**Rules:**
- Spell out all text verbatim (GPT renders text reliably when you give the exact words).
- Give the brand hex color.
- Add "no watermark, no logo".
- Download `.png`.

---

## 3b. Storyboard — Kimi / GPT (a richer story script → one self-contained HTML)

The storyboard is **shipped by default as a paginated 16:9 deck with inline SVG art** (from the `mediakit` stage) — no external image required. This section is the **optional upgrade** to a richer board.

> **Format rule — HTML only.** Every deliverable in this toolkit is a **single self-contained HTML file** that opens by double-clicking. Never ask for, produce, or hand off a **PPT / PPTX / Keynote / Google Slides** file (or any slide-deck export) — those formats may not open on the room's machines.

> **Content rule — a story script, not a visual spec.** The prompt describes **what happens** scene by scene and deliberately leaves **art direction, layout, palette and typography to the other tool**. Prescribing the visuals caps a stronger tool's output and produces worse work. (The same rule applies to the **richer-poster prompt** carried in `poster.html` — press **P** there.)

The prompt is **already built into `storyboard.html`** (the "Write a richer story script" overlay, press **P**). Paste it into **Kimi** (kimi.moonshot.cn) or **GPT**, **giving it `campaign-plan.html` as input first** (add `insight-brief.html` for audience + market context). It returns **one self-contained `.html`**; save it as `media/storyboard/storyboard-richer.html` and re-run the build — it is inlined as a page in the same deck.

**The one prompt** — the story content in one block; the look stays the other tool's decision:

```
You are writing the STORY SCRIPT for a campaign storyboard — the narrative only.
Do NOT design the visuals: the art direction, layout, palette and typography are entirely your call.
Nothing below is a visual spec.

=== GIVE THE MODEL THIS INPUT FIRST (best results) ===
Attach or paste the campaign plan — the contents of campaign-plan.html (campaign name, slogan,
proposition, offer, audiences, moments, budget). If you have it, paste insight-brief.html as well.

=== THE CAMPAIGN === {{CAMPAIGN NAME}}, {{slogan}}

=== WHAT TO WRITE: THE FAN JOURNEY, SCENE BY SCENE ===
Arc: {{6}} scenes in {{3}} chapters ({{chapter names}}).
For each scene write: number + a punchy title · the story beat (who, where, what happens, how it feels) ·
the product state at that moment (screen title, 1–2 lines, button) · a one-line quote in the fan's voice ·
four fields (Stage · Moment · Emotion · Goal) · the campaign action and the evidence it rests on.

Scene {{n}} · {{title}} — beat: {{scene}}; on screen "{{ui.title}} / {{ui.lines}} / {{ui.cta}}";
quote "{{quote}}"; {{stage}} · {{moment}} · {{emotion}} · {{goal}}; action {{action}} ({{source}}).
… (6–8 scenes)

=== HOW TO DELIVER IT ===
One complete, self-contained .html file that opens by double-clicking — all CSS and illustration inline,
no external files, no CDN, no build step. HTML ONLY: no PPT / PPTX / Keynote / Google Slides export.
It should page through a cover and then the scenes, at 16:9, scaled to any screen.

Everything visual — style, art, colour, layout — is your decision.
```

**Rules:**
- **One prompt, one file** — every scene comes from this single block, so the narrative stays consistent.
- **Never prescribe the visuals** — no palette, no "cinematic lighting", no layout instructions. Give the story and its content; let the tool design.
- **Feed `campaign-plan.html` first** — and say so in the prompt itself.
- **HTML only** — if the tool offers a "download as PPT/slides", decline it; save the raw `.html`.
- **6–8 scenes in 3 chapters** — more scenes slow generation for little gain.

## 4. Embedding back

The deck already has **media placeholder slots** (rendered as dashed "embed here" boxes). Bring the files into the run folder and the AI replaces the matching placeholder with the real player (relative path):

| Media | Deck placeholder | Beat | Inserted element |
|---|---|---|---|
| Image (GPT) | `{{MEDIA_IMAGE}}` | `poster` (and `keyvisual`) | `<img src="media/hero.png">` |
| Storyboard (Kimi / GPT) | one richer **self-contained HTML** | `visuals` / `storyboard` beat | save at `media/storyboard/storyboard-richer.html` → inlined as a page in the storyboard deck |
| Video (Runway) | `{{MEDIA_VIDEO}}` | `storyboard` | `<video controls src="media/video.mp4">` |
| Song (Suno) | `{{MEDIA_SONG}}` | `lyric` | `<audio controls src="media/song.mp3">` |
| Any bonus | `{{MEDIA_ASK}}` | `ask` | any of the above |

Rules:
- If a media type was **not** generated, set that placeholder to empty (`""`) — the `.media:empty` rule hides the slot cleanly.
- Keep single-file / relative-path output, double-click openable.
- The dashed placeholders are visible in the deck so the team can see exactly where each file goes.

## 5. Rules & etiquette

- Bonus is **optional** — never block the 6 required deliverables on a tool.
- Human curates: the AI writes prompts, the human picks which generation to use.
- Keep it on-brand (Ascentium colors, cause-first where the card's subject is an IP / conservation asset).
