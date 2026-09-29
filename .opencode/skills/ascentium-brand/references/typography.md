# Ascentium Typography

Source: Brand Guidelines R1.10, §4. Font stack and scale below are authoritative — do not invent type sizes.

## Font stack

```
"Poppins", "Noto Sans SC", "PingFang SC", "Microsoft YaHei", Arial, sans-serif
```

- English primary: **Poppins** (Light / Regular / Medium / SemiBold / Bold)
- Simplified Chinese: **Noto Sans SC**
- Fallbacks: Arial (English), PingFang SC (macOS/iOS CN), Microsoft YaHei (Windows CN)
- **Never substitute Poppins** with an unapproved typeface.

## Digital type scale

| Level        | Weight    | Size | Line height | Tracking |
|--------------|-----------|------|-------------|----------|
| Headline     | SemiBold  | 48px | 58px        | -1%      |
| Sub-heading  | SemiBold  | 31px | 38px        | 0%       |
| Large body   | Medium    | 20px | 28px        | 0%       |
| Small body   | Regular   | 16px | 24px        | 0%       |
| Tagline      | Medium    | 14px | 18px        | 0%       |

## Print type scale (reference)

| Level       | Weight   | Size | Line height | Tracking |
|-------------|----------|------|-------------|----------|
| Headline    | SemiBold | 48pt | 56pt        | -1%      |
| Sub-heading | SemiBold | 28pt | 36pt        | 0%       |
| Large body  | Medium   | 24pt | 32pt        | 0%       |
| Small body  | Regular  | 18pt | 32pt        | 0%       |
| Label       | Regular  | 14pt | 20pt        | 0%       |

## Rules

- **Weights**: titles = SemiBold; body = Regular; inline emphasis = Medium.
- **Tracking**: large headlines may loosen slightly; body stays standard or slightly tight.
- High contrast and consistent hierarchy across platforms.

## Misuse (do NOT)

- ❌ Unapproved fonts
- ❌ ALL-CAPS body text
- ❌ Stretched / distorted type
- ❌ Excessive letter-spacing
- ❌ Misaligned text
- ❌ Low text/background contrast
- ❌ Too many fonts or wrong weights

## Ready-to-use CSS classes

```css
.headline    { font-weight: 600; font-size: 48px; line-height: 58px; letter-spacing: -0.01em; }
.sub-heading { font-weight: 600; font-size: 31px; line-height: 38px; letter-spacing: 0; }
.large-body  { font-weight: 500; font-size: 20px; line-height: 28px; }
.small-body  { font-weight: 400; font-size: 16px; line-height: 24px; }
.tagline     { font-weight: 500; font-size: 14px; line-height: 18px; }
body         { font-family: "Poppins","Noto Sans SC","PingFang SC","Microsoft YaHei",Arial,sans-serif;
               color: var(--text-primary); }
```
