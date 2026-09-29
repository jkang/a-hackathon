---
name: ascentium-brand
description: Apply the Ascentium brand (colors, typography, graphic device, iconography) to any generated artifact — posters, pitch decks, dashboards, one-pagers, or web pages. Use whenever a visual output must follow the Ascentium Brand Guidelines R1.10. Triggers: "ascentium brand", "brand colors", "apply the brand", "make it Ascentium", "poster", "pitch deck", "dashboard", "kpi board".
---

# Ascentium Brand

Applies the **Ascentium Brand Guidelines (R1.10)** to visual artifacts. This skill is the **single source of truth** for colors, typography, spacing, and visual rules. Never write brand styles from memory — always pull from the references below.

## When to use

- Any HTML / PPT / poster / dashboard / KPI-board output in the hackathon toolkit.
- When the team says "make it look like Ascentium" or "apply the brand".

## Source of truth

The canonical brand document is `brand-guideline.md` (Chinese; replicated from the official R1.10 PDF). The extracted, ready-to-use assets are in `references/`:

- `references/tokens.css` — all CSS variables (`:root`).
- `references/typography.md` — font stack + type scale.
- `references/component-rules.md` — buttons / cards / poster / deck / dashboard rules.

## Core tokens (memorize these)

- Primary orange: `#FF6611` (CTA, brand accent)
- Midnight green: `#0F1514` (dark backgrounds, primary text — **NOT** pure black)
- Teal: `#077069` (secondary accent token)
- Sky: `#1877F2` (info only)
- Error: `#DC3545` (errors only)
- Font stack: `"Poppins", "Noto Sans SC", "PingFang SC", "Microsoft YaHei", Arial, sans-serif`

## Hard rules (DO NOT break)

1. Body text = Midnight Green `#0F1514`, never pure black `#000000`.
2. Primary CTA = Vibrant Orange background + Midnight Green or white text.
3. Light orange `#FFF0E7` / `#FFD1B8` = brand light / card backgrounds.
4. Error red `#DC3545` only for real errors; Sky blue `#1877F2` only for informational hints.
5. Upward Arrow graphic device: brand colors only, never stretched, never shadowed/gradiented, always pointing up.
6. Icons: flat, single-color, consistent stroke weight; key actions = icon + text.
7. Never stretch / tilt / recolor the logo; keep clear space ≥ half the logo height.

## Workflow

1. Read `references/tokens.css` and inject the `:root` variables into any generated HTML `<style>` block.
2. Apply `references/typography.md` for the heading/body scale.
3. Follow `references/component-rules.md` for the specific artifact type (poster vs deck vs dashboard).
4. Before finishing, self-check against the **Hard rules** above.
