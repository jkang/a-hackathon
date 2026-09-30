# Media Prompt Guide — bonus song / video / image

Bonus (optional) layer. Each group **optionally** generates a song, a video, or a hero image using external tools, then embeds the result in the Showcase report. The AI writes the prompts (from the `campaign-plan.html` capture); the human generates and curates.

## Tool list (1 primary + 1 backup each)

| Type | Primary | Backup | Output |
|---|---|---|---|
| Song | **Suno** (suno.com) | Udio | `.mp3` |
| Video | **Runway Gen-3** (runwayml.com) | Kling | `.mp4` |
| Image | **GPT** (ChatGPT image generation) | — | `.png` |

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

## 4. Embedding back

The deck already has **media placeholder slots** (rendered as dashed "embed here" boxes). Bring the files into the run folder and the AI replaces the matching placeholder with the real player (relative path):

| Media | Deck placeholder | Beat | Inserted element |
|---|---|---|---|
| Image (GPT) | `{{MEDIA_IMAGE}}` | `poster` (and `keyvisual`) | `<img src="media/hero.png">` |
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
