# Example Key-Visual Motifs (reference only)

These are **example** flat-illustration motifs shipped with the toolkit for the two demo quests. They are **not** part of the engine — a real run pulls its key visual from the quest card (`key_visual_svg` in `quest-card.md`), injected into the templates' `{{KEY_VISUAL_SVG}}` slot.

Each motif is a single `<symbol id="illo">`. The deck's title / keyvisual frames use `viewBox="0 0 480 360"`; the poster's three style arts use `viewBox="0 0 1200 500"`. Resize / re-art as the quest requires, keeping the `xMidYMid slice` frame ratio in sync.

## Motif 1 — stadium + tickets (sports / travel)

```html
<symbol id="illo" viewBox="0 0 480 360" preserveAspectRatio="xMidYMid slice">
  <rect width="480" height="360" fill="#FFF6EC"/>
  <circle cx="66" cy="74" r="11" fill="#FF6611"/>
  <circle cx="416" cy="96" r="8" fill="#077069"/>
  <path d="M120 44 l20 11 -20 11z" fill="#077069"/>
  <path d="M356 44 l-20 11 20 11z" fill="#FF6611"/>
  <circle cx="250" cy="40" r="6" fill="#0F5D57"/>
  <rect x="98" y="132" width="9" height="122" fill="#0F5D57"/>
  <rect x="70" y="104" width="64" height="36" rx="6" fill="#077069"/>
  <g fill="#FFF6EC"><circle cx="85" cy="115" r="4"/><circle cx="102" cy="115" r="4"/><circle cx="119" cy="115" r="4"/><circle cx="85" cy="130" r="4"/><circle cx="102" cy="130" r="4"/><circle cx="119" cy="130" r="4"/></g>
  <path d="M64 104 l-16 -18 7 -4 17 15z" fill="#FF6611"/>
  <path d="M140 104 l16 -18 -7 -4 -17 15z" fill="#FF6611"/>
  <rect x="373" y="132" width="9" height="122" fill="#0F5D57"/>
  <rect x="346" y="104" width="64" height="36" rx="6" fill="#077069"/>
  <g fill="#FFF6EC"><circle cx="361" cy="115" r="4"/><circle cx="378" cy="115" r="4"/><circle cx="395" cy="115" r="4"/><circle cx="361" cy="130" r="4"/><circle cx="378" cy="130" r="4"/><circle cx="395" cy="130" r="4"/></g>
  <path d="M340 104 l-16 -18 7 -4 17 15z" fill="#FF6611"/>
  <path d="M416 104 l16 -18 -7 -4 -17 15z" fill="#FF6611"/>
  <path d="M112 176 Q240 104 368 176 Z" fill="#0F5D57"/>
  <ellipse cx="240" cy="176" rx="128" ry="28" fill="#077069"/>
  <ellipse cx="240" cy="176" rx="128" ry="28" fill="none" stroke="#FFF6EC" stroke-width="5"/>
  <path d="M112 176 Q240 206 368 176 L354 268 Q240 298 126 268 Z" fill="#0F5D57"/>
  <path d="M112 176 Q240 206 368 176" fill="none" stroke="#FFF6EC" stroke-width="6"/>
  <g fill="#FF6611">
    <rect x="150" y="196" width="15" height="60" transform="skewY(5)"/>
    <rect x="196" y="200" width="15" height="66" transform="skewY(4)"/>
    <rect x="269" y="200" width="15" height="66" transform="skewY(-4)"/>
    <rect x="315" y="196" width="15" height="60" transform="skewY(-5)"/>
  </g>
  <rect x="216" y="236" width="48" height="42" rx="4" fill="#FFF6EC"/>
  <path d="M126 300 Q240 276 354 300 L400 360 L80 360 Z" fill="#CDE2E1"/>
  <path d="M210 300 L270 300 L300 360 L180 360 Z" fill="#FFF6EC"/>
  <ellipse cx="70" cy="250" rx="26" ry="20" fill="#077069"/>
  <ellipse cx="410" cy="246" rx="24" ry="18" fill="#077069"/>
  <g transform="rotate(-20 250 78)"><rect x="214" y="58" width="76" height="38" rx="7" fill="#FF6611"/><line x1="248" y1="64" x2="248" y2="90" stroke="#FFF6EC" stroke-width="3" stroke-dasharray="4 4"/></g>
  <g transform="rotate(16 130 110)"><rect x="96" y="92" width="66" height="34" rx="7" fill="#FF6611"/><line x1="125" y1="97" x2="125" y2="121" stroke="#FFF6EC" stroke-width="3" stroke-dasharray="4 4"/></g>
  <g transform="rotate(-12 366 120)"><rect x="332" y="102" width="66" height="34" rx="7" fill="#FF6611"/><line x1="361" y1="107" x2="361" y2="131" stroke="#FFF6EC" stroke-width="3" stroke-dasharray="4 4"/></g>
</symbol>
```

## Motif 2 — panda + bamboo (wildlife / IP)

```html
<symbol id="illo" viewBox="0 0 480 360" preserveAspectRatio="xMidYMid slice">
  <rect width="480" height="360" fill="#FFF6EC"/>
  <rect x="70" y="60" width="20" height="260" rx="8" fill="#077069"/>
  <rect x="70" y="140" width="20" height="6" fill="#FFF6EC"/>
  <rect x="70" y="220" width="20" height="6" fill="#FFF6EC"/>
  <path d="M90 120 q40 -18 62 6 q-40 14 -62 -6z" fill="#398D87"/>
  <path d="M70 190 q-42 -16 -64 8 q42 12 64 -8z" fill="#398D87"/>
  <rect x="390" y="80" width="20" height="240" rx="8" fill="#077069"/>
  <rect x="390" y="160" width="20" height="6" fill="#FFF6EC"/>
  <path d="M390 150 q-42 -18 -66 6 q42 14 66 -6z" fill="#398D87"/>
  <path d="M410 220 q42 -16 66 8 q-42 12 -66 -8z" fill="#398D87"/>
  <g fill="#FF6611">
    <path d="M300 70 c-10 -14 -32 -8 -32 8 c0 12 20 24 32 32 c12 -8 32 -20 32 -32 c0 -16 -22 -22 -32 -8z" transform="scale(0.55) translate(430 60)"/>
    <path d="M300 70 c-10 -14 -32 -8 -32 8 c0 12 20 24 32 32 c12 -8 32 -20 32 -32 c0 -16 -22 -22 -32 -8z" transform="scale(0.4) translate(160 120)"/>
    <path d="M300 70 c-10 -14 -32 -8 -32 8 c0 12 20 24 32 32 c12 -8 32 -20 32 -32 c0 -16 -22 -22 -32 -8z" transform="scale(0.45) translate(770 300)"/>
  </g>
  <ellipse cx="240" cy="250" rx="96" ry="80" fill="#0F1514"/>
  <ellipse cx="240" cy="262" rx="70" ry="60" fill="#FFFFFF"/>
  <ellipse cx="150" cy="238" rx="30" ry="42" fill="#0F1514" transform="rotate(18 150 238)"/>
  <ellipse cx="330" cy="238" rx="30" ry="42" fill="#0F1514" transform="rotate(-18 330 238)"/>
  <ellipse cx="196" cy="322" rx="34" ry="22" fill="#0F1514"/>
  <ellipse cx="284" cy="322" rx="34" ry="22" fill="#0F1514"/>
  <ellipse cx="196" cy="326" rx="14" ry="9" fill="#FFF6EC"/>
  <ellipse cx="284" cy="326" rx="14" ry="9" fill="#FFF6EC"/>
  <circle cx="240" cy="150" r="78" fill="#FFFFFF"/>
  <circle cx="186" cy="92" r="26" fill="#0F1514"/>
  <circle cx="294" cy="92" r="26" fill="#0F1514"/>
  <ellipse cx="206" cy="146" rx="20" ry="26" fill="#0F1514" transform="rotate(18 206 146)"/>
  <ellipse cx="274" cy="146" rx="20" ry="26" fill="#0F1514" transform="rotate(-18 274 146)"/>
  <circle cx="206" cy="148" r="7" fill="#FFF6EC"/>
  <circle cx="274" cy="148" r="7" fill="#FFF6EC"/>
  <ellipse cx="240" cy="172" rx="9" ry="6" fill="#0F1514"/>
  <path d="M228 188 q12 10 24 0" fill="none" stroke="#0F1514" stroke-width="4" stroke-linecap="round"/>
  <path d="M168 200 q72 34 144 0 q-6 26 -24 30 l-96 0 q-18 -4 -24 -30z" fill="#FF6611"/>
  <rect x="236" y="222" width="16" height="44" rx="6" fill="#FF6611"/>
  <rect x="252" y="196" width="12" height="86" rx="5" fill="#398D87" transform="rotate(24 258 240)"/>
</symbol>
```
