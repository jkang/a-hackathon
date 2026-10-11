#!/usr/bin/env python3
"""Build a standalone 16:9 campaign STORYBOARD for the mediakit stage.

By default the script renders the storyboard itself as ONE inline SVG "design
sheet" — a 16:9 board split into chapter columns, each holding its scene cards
(number + title + a scene illustration + a phone/UI inset showing the product
state). Fully self-contained; no external image needed.

If the spec's `board` resolves to a rendered image (.png/.jpg), that image is
embedded instead (the richer sheet the team generates from the built-in prompt
via Kimi / GPT).

Either way it writes `storyboard.html` (dark-or-light per the campaign theme),
and embeds a copyable "upgrade prompt" overlay.

Usage:
    python3 build-storyboard.py [--dir DIR] [--spec FILE] [--frames DIR] [--out FILE]
                                [--template FILE] [--width N]

Defaults: --dir .  --spec <dir>/media/storyboard/storyboard.json
          --frames <dir>/media/storyboard  --out <dir>/storyboard.html  --width 1600

Spec (JSON):
{
  "quest":"A", "brand":"The Date-Certain Pass", "crumb":"…", "h1":"…",
  "accent": {"accent":"#FF6611","tint":"#FFF0E7","line":"#FFD1B8","deep":"#B24000"},
  "theme":  {"surface":"light"},              # light | dark  (derive from the campaign plan)
  "board":  "storyboard-sheet.png",           # OPTIONAL rendered sheet; omit → SVG design sheet
  "chapters": [ {"id":"I","name":"The Hook"} ],
  "steps": [
    {"n":"01","chapter":"I","title":"…","scene":"…",
     "ui":{"screen":"…","title":"…","lines":["…"],"cta":"…"}}
  ]
}
"""
import argparse
import base64
import html
import json
import os
import re
import sys
import tempfile

try:
    from PIL import Image
except Exception:  # pragma: no cover
    Image = None

W, H = 1600, 900
PAD, GUT = 26, 16
HEAD_H = 40
CARD_GAP = 12

DEFAULT_STEPS = [
    {"n": "01", "chapter": "I", "title": "The first spark", "scene": "the everyday trigger",
     "ui": {"screen": "Discover", "title": "A reason to go", "lines": ["See it for yourself"], "cta": "Learn more"}},
    {"n": "02", "chapter": "I", "title": "It feels personal", "scene": "she sees herself in it",
     "ui": {"screen": "For you", "title": "Made for your family", "lines": ["Your dates, your plan"], "cta": "Continue"}},
    {"n": "03", "chapter": "II", "title": "The offer, unmissable", "scene": "the product reveal",
     "ui": {"screen": "The offer", "title": "One pass, all in", "lines": ["Seats + fare together"], "cta": "Reserve"}},
    {"n": "04", "chapter": "II", "title": "The decision is shared", "scene": "the family agrees",
     "ui": {"screen": "Family bundle", "title": "One price", "lines": ["Up to 4 people"], "cta": "Choose"}},
    {"n": "05", "chapter": "III", "title": "Reassurance, visible", "scene": "a calm confirmation",
     "ui": {"screen": "Flex", "title": "No penalties", "lines": ["Flexible dates"], "cta": "See terms"}},
    {"n": "06", "chapter": "III", "title": "A memory they keep", "scene": "the shared payoff",
     "ui": {"screen": "Your memory", "title": "Saved", "lines": ["Everything in one place"], "cta": "Open"}},
]


def esc(t):
    return html.escape(str(t), quote=False)


def wrap(text, n, max_lines=3):
    words = str(text).split()
    out, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= n:
            cur = (cur + " " + w).strip()
        else:
            if cur:
                out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out[:max_lines]


# ------------------------------------------------------------------ theme
def derive_theme(spec):
    t = spec.get("theme") or {}
    surface = str(t.get("surface", "light")).lower()
    acc = spec.get("accent") or {}
    if surface == "dark":
        base = {"page": "#050A0A", "card": "#101B19", "scene": "#0C1514",
                "line": "#22312F", "title": "#F4EFE4", "text": "#C7D4D1", "muted": "#8FA8A3"}
    else:
        base = {"page": "#F1ECE2", "card": "#FFFFFF", "scene": "#F6F1E7",
                "line": "#E3DCCE", "title": "#16130D", "text": "#4A463D", "muted": "#8B8574"}
    for k in ("page", "card", "scene", "line", "title", "text", "muted"):
        if t.get(k):
            base[k] = t[k]
    base["surface"] = surface
    base["accent"] = acc.get("accent", "#FF6611")
    base["accent_tint"] = acc.get("tint", "#FFF0E7")
    return base


# ------------------------------------------------------------------ SVG pieces
def scene(x, y, w, h, i, th):
    """A schematic scene band: gradient sky + a lit skyline + foreground figures."""
    fig = th["muted"] if th["surface"] == "light" else "#3A5852"
    win = th["card"] if th["surface"] == "light" else "#0A1211"
    p = ['<g clip-path="url(#clip%d)">' % i]
    p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="url(#sky%d)"/>' % (x, y, w, h, i))
    # soft accent spotlight / glow
    p.append('<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s" opacity="%s"/>'
             % (x + w * 0.70, y + h * 0.30, h * 0.40,
                th["accent_tint"] if th["surface"] == "light" else th["accent"],
                ".45" if th["surface"] == "light" else ".28"))
    # skyline (varied buildings + windows) sitting on the ground line
    base = y + h * 0.70
    buildings = ((0.06, 0.34, 0.10), (0.19, 0.52, 0.08), (0.30, 0.28, 0.09),
                 (0.58, 0.44, 0.10), (0.71, 0.60, 0.09), (0.83, 0.30, 0.11))
    for bx, bh, bw in buildings:
        sx = x + w * bx
        sy = base - h * bh
        bwid = w * bw
        p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="%s" opacity=".7"/>'
                 % (sx, sy, bwid, h * bh, th["muted"]))
        # windows
        wcol = max(1, min(5, int(bwid / 12)))
        wrow = max(1, min(6, int((h * bh) / 14)))
        dx = bwid / wcol
        dy = (h * bh) / wrow
        for c in range(wcol):
            for r in range(wrow):
                p.append('<rect x="%.1f" y="%.1f" width="2.6" height="3.4" fill="%s" opacity=".45"/>'
                         % (sx + dx * (c + 0.5) - 1.3, sy + dy * (r + 0.5) - 1.7, win))
    p.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="1.5" opacity=".8"/>'
             % (x, base, x + w, base, th["muted"]))
    # foreground figures (middle one is the focus, in accent)
    figx = (x + w * 0.26, x + w * 0.46, x + w * 0.66)
    for k, fx in enumerate(figx):
        focus = (k == 1)
        col = th["accent"] if focus else fig
        r = 11 if focus else 8.5
        head = base - (34 if focus else 27)
        bwid = 27 if focus else 22
        p.append('<circle cx="%.0f" cy="%.0f" r="%.1f" fill="%s"/>' % (fx, head, r, col))
        p.append('<path d="M%.0f %.0f q%.0f -%.0f %.0f 0 z" fill="%s"/>'
                 % (fx - bwid, base, bwid, bwid + 7, 2 * bwid, col))
    p.append('</g>')
    return "".join(p)


def phone(x, y, w, h, ui, i, th):
    """A phone / UI inset showing the product state."""
    p = ['<g filter="url(#shadow)">']
    p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="16" fill="%s" stroke="%s"/>'
             % (x, y, w, h, th["card"], th["line"]))
    p.append('</g>')
    # notch
    p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="5" rx="2.5" fill="%s"/>'
             % (x + w / 2 - 14, y + 8, 28, th["line"]))
    sx, sy, sw = x + 10, y + 22, w - 20
    lab = esc(str(ui.get("screen", "")).upper())
    p.append('<text x="%.0f" y="%.0f" fill="%s" font-family="Poppins,Arial,sans-serif" font-size="8" '
             'font-weight="700" letter-spacing="1">%s</text>' % (sx, sy + 8, th["accent"], lab))
    ty = sy + 26
    for ln in wrap(ui.get("title", ""), max(10, int(sw / 6.2)), 2):
        p.append('<text x="%.0f" y="%.0f" fill="%s" font-family="Poppins,Arial,sans-serif" font-size="11.5" '
                 'font-weight="800">%s</text>' % (sx, ty, th["title"], esc(ln)))
        ty += 14
    ty += 4
    for ln in wrap(" · ".join(ui.get("lines", [])), max(12, int(sw / 5.4)), 3):
        p.append('<text x="%.0f" y="%.0f" fill="%s" font-family="Poppins,Arial,sans-serif" font-size="8.5">%s</text>'
                 % (sx, ty, th["text"], esc(ln)))
        ty += 11
    # CTA pill at the bottom
    ch = 18
    cy = y + h - ch - 10
    p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%d" rx="9" fill="%s"/>' % (sx, cy, sw, ch, th["accent"]))
    p.append('<text x="%.0f" y="%.0f" fill="#fff" font-family="Poppins,Arial,sans-serif" font-size="9" '
             'font-weight="700" text-anchor="middle">%s</text>' % (sx + sw / 2, cy + 12.5, esc(ui.get("cta", ""))))
    return "".join(p)


def step_card(x, y, w, h, step, i, th):
    p = ['<g>']
    p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="14" fill="%s" stroke="%s"/>'
             % (x, y, w, h, th["card"], th["line"]))
    # number badge
    p.append('<rect x="%.0f" y="%.0f" width="30" height="22" rx="6" fill="%s"/>' % (x + 14, y + 13, th["accent"]))
    p.append('<text x="%.0f" y="%.0f" fill="#fff" font-family="Poppins,Arial,sans-serif" font-size="12" '
             'font-weight="800" text-anchor="middle">%s</text>' % (x + 29, y + 28, esc(step.get("n", ""))))
    # title
    ty = y + 30
    tl = wrap(step.get("title", ""), max(20, int((w - 70) / 7.6)), 2)
    for ln in tl:
        p.append('<text x="%.0f" y="%.0f" fill="%s" font-family="Poppins,Arial,sans-serif" font-size="14.5" '
                 'font-weight="800">%s</text>' % (x + 54, ty, th["title"], esc(ln)))
        ty += 17
    # scene band
    sy = y + 30 + (len(tl) - 1) * 17 + 12
    sh = h - (sy - y) - 14
    sw = w - 28
    sky_top = th["accent_tint"] if th["surface"] == "light" else "#0F1D1A"
    sky_bot = th["scene"] if th["surface"] == "light" else "#0A1211"
    p.append('<defs>'
             '<clipPath id="clip%d"><rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="10"/></clipPath>'
             '<linearGradient id="sky%d" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
             '</defs>' % (i, x + 14, sy, sw, sh, i, sky_top, sky_bot))
    p.append(scene(x + 14, sy, sw, sh, i, th))
    p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="10" fill="none" stroke="%s"/>'
             % (x + 14, sy, sw, sh, th["line"]))
    # phone inset
    pw = 118
    ph = min(sh - 22, 212)
    p.append(phone(x + 14 + sw - pw - 12, sy + (sh - ph) / 2, pw, ph, step.get("ui", {}), i, th))
    p.append('</g>')
    return "".join(p)


def svg_sheet(spec, steps, chapters, th):
    nch = max(1, len(chapters))
    colw = (W - 2 * PAD - (nch - 1) * GUT) / nch
    content_top = PAD + HEAD_H + 8
    content_h = H - PAD - content_top
    by_ch = {}
    for s in steps:
        by_ch.setdefault(s.get("chapter"), []).append(s)
    rows = max(1, max((len(v) for v in by_ch.values()), default=1))
    card_h = (content_h - (rows - 1) * CARD_GAP) / rows

    out = ['<svg class="sheet" viewBox="0 0 %d %d" role="img" aria-label="Campaign storyboard" '
           'xmlns="http://www.w3.org/2000/svg" font-family="Poppins,Arial,sans-serif">' % (W, H)]
    out.append('<defs><filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">'
               '<feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#000" flood-opacity=".28"/></filter></defs>')
    out.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, th["page"]))
    idx = 0
    for ci, chdef in enumerate(chapters):
        cx = PAD + ci * (colw + GUT)
        cid = esc(chdef.get("id", ""))
        cname = esc(chdef.get("name", ""))
        out.append('<text x="%.0f" y="%.0f" fill="%s" font-size="20" font-weight="800">%s</text>'
                   % (cx, PAD + 22, th["accent"], cid))
        out.append('<text x="%.0f" y="%.0f" fill="%s" font-size="14" font-weight="700" letter-spacing="1.5">%s</text>'
                   % (cx + 38, PAD + 21, th["muted"], cname.upper()))
        out.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="2"/>'
                   % (cx, PAD + HEAD_H - 6, cx + colw, PAD + HEAD_H - 6, th["accent"]))
        ch_steps = by_ch.get(chdef.get("id"), [])
        for ri, step in enumerate(ch_steps):
            cy = content_top + ri * (card_h + CARD_GAP)
            out.append(step_card(cx, cy, colw, card_h, step, idx, th))
            idx += 1
    out.append('</svg>')
    return "".join(out)


# ------------------------------------------------------------------ raster
def data_uri(path):
    if Image is None:
        sys.exit("Pillow is required to embed a rendered sheet: pip install Pillow")
    im = Image.open(path).convert("RGB")
    tmp = os.path.join(tempfile.gettempdir(), "_sb_sheet_%d.jpg" % os.getpid())
    im.save(tmp, "JPEG", quality=88, optimize=True)
    with open(tmp, "rb") as fh:
        return "data:image/jpeg;base64," + base64.b64encode(fh.read()).decode()


def resolve_image(frames_dir, name):
    if not name:
        return None
    p = os.path.join(frames_dir, name)
    if os.path.isfile(p):
        return p
    stem, _ = os.path.splitext(p)
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        if os.path.isfile(stem + ext):
            return stem + ext
    return None


# ------------------------------------------------------------------ prompt
def default_prompt(spec, steps):
    brand = spec.get("brand", "the campaign")
    acc = (spec.get("accent") or {}).get("accent", "#FF6611")
    chs = spec.get("chapters", [])
    lines = [
        'Create ONE 16:9 storyboard DESIGN SHEET for the campaign "%s".' % brand,
        '',
        'LAYOUT: split the sheet into %d vertical chapters%s. Inside each chapter stack its scene panels. '
        'Each panel shows a cinematic scene + a small phone/UI inset (the app screenshot at that moment).'
        % (max(1, len(chs)), ' (' + ' / '.join(str(c.get("name", "")) for c in chs) + ')' if chs else ''),
        '',
        'STYLE: brand accent %s, cinematic lighting, shallow depth of field, subtle film grain; keep a clear '
        'left margin in each panel for a bold title. Consistent style across every panel. No watermark, no logo.' % acc,
        '',
    ]
    for idx, s in enumerate(steps):
        n = s.get("n", "%02d" % (idx + 1))
        ui = s.get("ui", {})
        lines.append('Panel %s · %s — %s; phone inset: "%s / %s / %s"' % (
            n, str(s.get("title", "")), s.get("scene", ""),
            ui.get("title", ""), " ".join(ui.get("lines", [])), ui.get("cta", "")))
    lines += ['', 'Number the panels in order; one consistent look; thin gutters. 16:9. No watermark, no logo.']
    return "\n".join(lines)


def overlay_html(prompt):
    if not prompt:
        return ""
    return (
        '<div class="ph"><h2>Make the storyboard more visualized</h2>'
        '<button class="pclose" id="pclose">Close</button></div>'
        '<div class="note">This sheet is an <b>SVG design sheet</b> (the full storyboard, generated in-page). '
        'For a richer, rendered board, copy the prompt below into <b>Kimi</b> (kimi.moonshot.cn) or <b>GPT</b>, '
        'generate one 16:9 sheet image, and bring the file back — the AI swaps it into this page.</div>'
        '<div class="promptbox"><button class="copy" id="pcopy">Copy prompt</button>'
        '<pre id="pprompt">%s</pre></div>' % esc(prompt)
    )


# ------------------------------------------------------------------ build
def build(directory, spec_path, frames_dir, out_path, template_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    th = derive_theme(spec)
    steps = spec.get("steps") or DEFAULT_STEPS
    chapters = spec.get("chapters") or [
        {"id": "I", "name": "The Hook"}, {"id": "II", "name": "The Offer"}, {"id": "III", "name": "Belonging"}]

    board_file = spec.get("board") or "storyboard-sheet"
    fp = resolve_image(frames_dir, board_file)
    if fp:
        sheet = '<img src="%s" alt="Campaign storyboard">' % data_uri(fp)
        mode = "rendered sheet"
    else:
        sheet = svg_sheet(spec, steps, chapters, th)
        mode = "SVG design sheet"

    prompt = spec.get("upgrade_prompt") or default_prompt(spec, steps)

    slide = (
        '<section class="slide" data-i="0">\n'
        '  <div class="brandbar"><div class="logo">%s<span>.</span></div><div class="tag">%s</div></div>\n'
        '  <div class="titlerow"><h1>%s</h1><div class="range">%d scenes &middot; %d chapters</div></div>\n'
        '  <div class="boardbox">%s</div>\n'
        '</section>'
        % (esc(spec.get("brand", "")), esc(spec.get("crumb", "")),
           esc(spec.get("h1", "")), len(steps), max(1, len(chapters)), sheet)
    )

    tpl = open(template_path, encoding="utf-8").read()
    acc = spec.get("accent") or {}
    repl = {
        "TITLE": spec.get("brand", "Campaign") + " Storyboard",
        "QUEST": spec.get("quest", ""),
        "SURFACE": th["surface"],
        "SLIDES": slide,
        "PROMPT_OVERLAY": overlay_html(prompt),
        "ACCENT": acc.get("accent", "#FF6611"),
        "ACCENT_TINT": acc.get("tint", "#FFF0E7"),
        "ACCENT_LINE": acc.get("line", "#FFD1B8"),
        "ACCENT_DEEP": acc.get("deep", "#B24000"),
        "PAGE": th["page"], "CARD": th["card"], "LINE": th["line"],
        "TITLE_C": th["title"], "TEXT": th["text"], "MUTED": th["muted"],
    }
    for k, v in repl.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", tpl)))
    if leftover:
        sys.exit("unfilled template tokens: " + ", ".join(leftover))

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(tpl)
    print("wrote %s (%s, %d scenes, %d chapters, %.2f MB)"
          % (out_path, mode, len(steps), len(chapters), len(tpl) / 1024 / 1024))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Build a standalone 16:9 campaign storyboard.")
    ap.add_argument("--dir", default=".")
    ap.add_argument("--spec", default=None)
    ap.add_argument("--frames", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--template", default=os.path.join(here, "..", "templates", "storyboard.html"))
    a = ap.parse_args()
    spec = a.spec or os.path.join(a.dir, "media", "storyboard", "storyboard.json")
    frames = a.frames or os.path.join(a.dir, "media", "storyboard")
    out = a.out or os.path.join(a.dir, "storyboard.html")
    build(a.dir, spec, frames, out, a.template)


if __name__ == "__main__":
    main()
