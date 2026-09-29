# Ascentium Component & Artifact Rules

Source: Brand Guidelines R1.10, §3 (color), §6 (graphic device), §7 (iconography), §9 (applications).
Apply together with `tokens.css` and `typography.md`.

## 1. Buttons & CTAs

- Primary CTA: Vibrant Orange `#FF6611` background + Midnight Green `#0F1514` or white text (contrast 6.29, passes AA).
- Never use error red or sky blue as a primary action color.
- Key actions must show **icon + text** (never icon-only for critical actions).

## 2. Cards & surfaces

- Page background: `#F7F6F4` (`--bg-page`). Card background: `#FFFFFF` (`--bg-card`).
- Brand tint surfaces: light orange `#FFF0E7` / `#FFD1B8`; Quest B may use teal tint `#CDE2E1`.
- Border/divider: `#E4E8E7` (`--line`). Body text: `#0F1514`; muted text: `#5A6663`.
- Rounded corners: cards ~12–18px (digital), consistent across an artifact.

## 3. Graphic device — Upward Arrow

- Symbolizes growth/progress. Use only in brand colors.
- **Never** stretch, distort, recolor, add shadow/3D/gradient, or change direction — always points **up**.
- Integrate naturally with content; do not leave floating/detached.

## 4. Iconography

- Two families: **Pictograms** (actions/objects) and **Functional icons** (navigation/UI).
- Build on a **400×400px grid with 10px subdivisions**; keep stroke weight uniform.
- Flat, single color (or same-hue shades); **no** 3D, shadow, or mixing line + fill styles.
- Scale cleanly; do not distort.

## 5. Poster (single-page hero visual)

- Canvas: A3-ish portrait or 1080×1080 square; keep **54px margin** on 1080×1080, **48px** on 1200×628.
- Structure: brand bar (logo) → big headline → hero line / offer → 1 supporting stat → CTA → footer.
- Dominant color = Vibrant Orange (Quest A) or Teal (Quest B); text Midnight Green or white.
- One clear focal point; do not crowd.

## 6. Pitch deck / HTML slides

- 16:9. Slide rhythm: title slide → problem → insight → big idea → plan → proof → ask.
- Every slide: consistent margin, logo in a fixed corner, one idea per slide.
- Use orange for emphasis in Quest A decks; teal for Quest B.
- Body ≥16px equivalent; headline via `.headline` scale.

## 7. KPI dashboard / board

- Light background; Midnight Green headings; orange/teal for the primary metric trend.
- KPI tiles: big number + short caption; use `--error` only for real breaches, `--info` for neutral notes.
- Chart line 3.4 (a): one accent color per chart; avoid rainbow palettes.

## 8. Accessibility pairings (verified AA/AAA)

| Background        | Text color     | Contrast | Level |
|-------------------|----------------|----------|-------|
| White             | Midnight Green | 18.58    | AA/AAA |
| Vibrant Orange    | Midnight Green | 6.29     | AA/AAA |
| Teal Green        | Midnight Green | 3.12     | AA |
| Sky Blue          | Midnight Green | 4.39     | AA |

## 9. Final self-check

- [ ] No pure black body text (must be `#0F1514`).
- [ ] Primary CTA is Vibrant Orange.
- [ ] Arrow (if used) is up, brand-colored, undistorted.
- [ ] Icons flat, single-color, uniform stroke.
- [ ] Type scale and font stack from `typography.md`.
- [ ] All colors traceable to `tokens.css`.
