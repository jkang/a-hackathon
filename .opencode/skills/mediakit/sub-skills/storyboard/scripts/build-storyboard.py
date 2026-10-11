#!/usr/bin/env python3
"""Build a standalone 16:9 campaign STORYBOARD for the mediakit stage.

Two modes, chosen automatically:

  1. SVG DESIGN DRAFT (default — no image needed). If the spec's `board` image is
     absent/unresolvable, the script renders the six journey panels as ONE inline SVG
     "design draft" (a schematic 3x2 sheet: numbered panels, step labels, a simple scene
     sketch, and each panel's headline). Fully self-contained, works out of the box.

  2. RENDERED SHEET (upgrade). If `board` resolves to a raster image (.png/.jpg/.webp),
     the script downscales + JPEG-encodes it and embeds it as a data URI — this is the
     richer sheet the team generates from the included one-complete-prompt via Kimi / GPT.

Either way it writes a single self-contained `storyboard.html` (dark, immersive, 16:9) and
embeds a copyable "upgrade prompt" overlay the team can take to Kimi / GPT.

Usage:
    python3 build-storyboard.py [--dir DIR] [--spec FILE] [--frames DIR] [--out FILE]
                                [--template FILE] [--width N]

Defaults:
    --dir       .
    --spec      <dir>/media/storyboard/storyboard.json
    --frames    <dir>/media/storyboard
    --out       <dir>/storyboard.html
    --template  ../templates/storyboard.html  (relative to this script)
    --width     1600     (sheet width in px before JPEG encode)

Spec (JSON):
    {
      "quest": "B",
      "brand": "The Numbered Drop",              # logo text (a dot is appended)
      "crumb": "Campaign Media Kit · Storyboard · Chengdu Panda Base",
      "h1": "How we attract the target audience",
      "accent": {"accent":"#077069","tint":"#CDE2E1","line":"#83B8B4","deep":"#043835"},
      "board": "storyboard-sheet.png",           # OPTIONAL rendered sheet; omit → SVG draft
      "width": 1600,                             # optional override
      "upgrade_prompt": "…",                      # optional; derived from steps if absent
      "steps": [
        {"n":"01","label":"Attract","headline":"…","scene":"…"},
        …
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


DEFAULT_STEPS = [
    {"n": "01", "label": "Attract", "headline": "The always-on first touch"},
    {"n": "02", "label": "Tease", "headline": "The hook that builds anticipation"},
    {"n": "03", "label": "Convert", "headline": "The core offer moment"},
    {"n": "04", "label": "Amplify", "headline": "Social proof and word of mouth"},
    {"n": "05", "label": "Belong", "headline": "The membership step"},
    {"n": "06", "label": "Deepen", "headline": "The long-term payoff"},
]


def esc(t):
    return html.escape(str(t), quote=False)


def wrap(text, n, lines_max=3):
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
    return out[:lines_max]


# ---------------------------------------------------------------- SVG draft
def scene(x, y, w, h, i):
    """A schematic scene band for panel i (0..5): horizon + figures + an accent motif."""
    p = []
    p.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="10" fill="#0C1514" '
             'stroke="var(--sb-line)" stroke-opacity=".65"/>' % (x, y, w, h))
    base = y + h * 0.66
    p.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="var(--sb-line)" '
             'stroke-opacity=".7" stroke-width="1.5"/>' % (x + 14, base, x + w - 14, base))
    # three fan figures; the middle one is the accent focus
    for k, fx in enumerate((x + w * 0.30, x + w * 0.50, x + w * 0.70)):
        focus = (k == 1)
        col = "var(--accent-tint)" if focus else "var(--sb-muted)"
        r = 9 if focus else 7
        head = base - (28 if focus else 22)
        bw = 22 if focus else 18
        p.append('<circle cx="%.0f" cy="%.0f" r="%d" fill="%s" opacity=".85"/>' % (fx, head, r, col))
        p.append('<path d="M%.0f %.0f q%.0f -%.0f %.0f 0 z" fill="%s" opacity=".85"/>'
                 % (fx - bw, base, bw, bw + 6, 2 * bw, col))
    if i == 1:  # accent focus ring around the middle figure
        p.append('<circle cx="%.0f" cy="%.0f" r="30" fill="none" stroke="var(--accent)" '
                 'stroke-width="2" stroke-dasharray="4 5" opacity=".9"/>' % (x + w * 0.50, base - 26))
    # a small accent motif varying by step (upper-right), so panels are not identical
    mx, my = x + w - 38, y + 34
    if i % 6 == 0:      # device / feed
        p.append('<rect x="%.0f" y="%.0f" width="24" height="38" rx="4" fill="none" stroke="var(--accent)" stroke-width="2"/>' % (mx - 12, my - 19))
        p.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="var(--accent)" stroke-width="2"/>' % (mx - 5, my + 12, mx + 5, my + 12))
    elif i == 1:        # countdown ring
        p.append('<circle cx="%.0f" cy="%.0f" r="16" fill="none" stroke="var(--accent)" stroke-width="2.5"/>' % (mx, my))
        p.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="var(--accent)" stroke-width="2.5"/>' % (mx, my, mx, my - 9))
    elif i == 2:        # ticket / card
        p.append('<rect x="%.0f" y="%.0f" width="34" height="22" rx="4" fill="none" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4 3"/>' % (mx - 17, my - 11))
    elif i == 3:        # share nodes
        for dx, dy in ((-13, -10), (13, -10), (0, 12)):
            p.append('<circle cx="%.0f" cy="%.0f" r="5" fill="var(--accent)"/>' % (mx + dx, my + dy))
    elif i == 4:        # badge
        p.append('<circle cx="%.0f" cy="%.0f" r="14" fill="none" stroke="var(--accent)" stroke-width="2.4"/>' % (mx, my))
        p.append('<path d="M%.0f %.0f l4 8 9 1 -6 6 1 9 -8 -4 -8 4 1 -9 -6 -6 9 -1 z" fill="var(--accent)"/>' % (mx, my - 6))
    else:               # location pin
        p.append('<circle cx="%.0f" cy="%.0f" r="15" fill="none" stroke="var(--accent)" stroke-width="2.4"/>' % (mx, my - 4))
        p.append('<path d="M%.0f %.0f l-8 16 l8 -4 l8 4 z" fill="var(--accent)"/>' % (mx, my + 11))
    return "".join(p)


def svg_sheet(steps):
    W, H = 1600, 900
    PAD, GUT = 24, 16
    cols, rows = 3, 2
    pw = (W - 2 * PAD - (cols - 1) * GUT) / cols
    ph = (H - 2 * PAD - (rows - 1) * GUT) / rows
    out = ['<svg class="sheet" viewBox="0 0 %d %d" role="img" aria-label="Campaign storyboard draft" '
           'xmlns="http://www.w3.org/2000/svg">' % (W, H)]
    out.append('<rect width="%d" height="%d" fill="#0A1110"/>' % (W, H))
    for i in range(cols * rows):
        col, row = i % cols, i // cols
        x = PAD + col * (pw + GUT)
        y = PAD + row * (ph + GUT)
        s = steps[i] if i < len(steps) else {"n": "%02d" % (i + 1), "label": "", "headline": ""}
        out.append('<g>')
        out.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="16" fill="var(--sb-card)" '
                   'stroke="var(--sb-line)"/>' % (x, y, pw, ph))
        out.append('<text x="%.0f" y="%.0f" fill="var(--accent)" font-family="Poppins,Arial,sans-serif" '
                   'font-size="20" font-weight="800">%s</text>' % (x + 20, y + 36, esc(s.get("n", "%02d" % (i + 1)))))
        lab = esc(str(s.get("label", "")).upper())
        out.append('<text x="%.0f" y="%.0f" fill="var(--sb-muted)" font-family="Poppins,Arial,sans-serif" '
                   'font-size="12" font-weight="700" letter-spacing="2.5">%s</text>' % (x + 62, y + 35, lab))
        sx, sy = x + 16, y + 52
        sw, sh = pw - 32, ph - 52 - 92
        out.append(scene(sx, sy, sw, sh, i))
        ty = y + ph - 62
        for ln in wrap(s.get("headline", ""), 42, 3):
            out.append('<text x="%.0f" y="%.0f" fill="var(--sb-cream)" font-family="Poppins,Arial,sans-serif" '
                       'font-size="18" font-weight="700">%s</text>' % (x + 20, ty, esc(ln)))
            ty += 24
        out.append('</g>')
    out.append('</svg>')
    return "".join(out)


# ---------------------------------------------------------------- raster sheet
def data_uri(path, width):
    if Image is None:
        sys.exit("Pillow is required to embed a rendered sheet: pip install Pillow")
    im = Image.open(path).convert("RGB")
    ow, oh = im.size
    nh = max(1, round(oh * width / ow))
    im = im.resize((width, nh), Image.LANCZOS)
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


# ---------------------------------------------------------------- fragments
def legend_html(steps):
    if not steps:
        return ""
    chips = "".join(
        '<span class="lchip"><b>%s</b>%s</span>' % (esc(s.get("n", "")), esc(s.get("label", "")))
        for s in steps
    )
    return '\n  <div class="legend">%s</div>' % chips


def default_prompt(spec, steps):
    brand = spec.get("brand", "the campaign")
    acc = spec.get("accent", {}).get("accent", "#FF6611")
    lines = [
        'Create ONE 16:9 storyboard sheet: a 3-column × 2-row grid of six cinematic panels that '
        'follow one fan\'s journey for the campaign "%s".' % brand,
        '',
        'STYLE (all panels): brand accent %s, cinematic lighting, shallow depth of field, subtle '
        'film grain. Keep the left third of each panel clear for a white UPPERCASE headline. '
        'High contrast, no watermark, no logo.' % acc,
        '',
    ]
    for idx, s in enumerate(steps):
        n = s.get("n", "%02d" % (idx + 1))
        try:
            num = int(str(n))
        except ValueError:
            num = idx + 1
        scene_txt = s.get("scene", "") or s.get("headline", "")
        lines.append('Panel %d · %s — %s; headline "%s"'
                     % (num, str(s.get("label", "")).upper(), scene_txt, s.get("headline", "")))
    lines += ['', 'Number the panels 1–6 top-left; use one consistent style across all six; keep thin '
              'gutters between panels. 16:9. No watermark, no logo.']
    return "\n".join(lines)


def overlay_html(prompt):
    if not prompt:
        return ""
    return (
        '<div class="ph"><h2>Make the storyboard more visualized</h2>'
        '<button class="pclose" id="pclose">Close</button></div>'
        '<div class="note">This sheet is a schematic <b>SVG design draft</b>. For a richer, rendered '
        'board, copy the prompt below into <b>Kimi</b> (kimi.moonshot.cn) or <b>GPT</b> to generate '
        'one 6-panel sheet image, then bring the file back — the AI embeds it here.</div>'
        '<div class="promptbox"><button class="copy" id="pcopy">Copy prompt</button>'
        '<pre id="pprompt">%s</pre></div>' % esc(prompt)
    )


def build(directory, spec_path, frames_dir, out_path, template_path, width):
    spec = json.load(open(spec_path, encoding="utf-8"))
    width = int(spec.get("width", width))
    steps = spec.get("steps") or DEFAULT_STEPS
    panel_count = len(steps)

    board_file = spec.get("board")
    fp = resolve_image(frames_dir, board_file) if board_file else None
    if fp:
        sheet = '<img src="%s" alt="Campaign storyboard">' % data_uri(fp, width)
    else:
        sheet = svg_sheet(steps)

    prompt = spec.get("upgrade_prompt") or default_prompt(spec, steps)

    slide = (
        '<section class="slide" data-i="0">\n'
        '  <div class="brandbar"><div class="logo">%s<span>.</span></div><div class="tag">%s</div></div>\n'
        '  <div class="titlerow"><h1>%s</h1><div class="range">%d panels &middot; one sheet</div></div>\n'
        '  <div class="boardbox">%s</div>%s\n'
        '</section>'
        % (esc(spec.get("brand", "")), esc(spec.get("crumb", "")),
           esc(spec.get("h1", "")), panel_count, sheet, legend_html(steps))
    )

    tpl = open(template_path, encoding="utf-8").read()
    acc = spec.get("accent", {})
    repl = {
        "TITLE": spec.get("brand", "Campaign") + " Storyboard",
        "QUEST": spec.get("quest", ""),
        "SLIDES": slide,
        "PROMPT_OVERLAY": overlay_html(prompt),
        "ACCENT": acc.get("accent", "#077069"),
        "ACCENT_TINT": acc.get("tint", "#CDE2E1"),
        "ACCENT_LINE": acc.get("line", "#83B8B4"),
        "ACCENT_DEEP": acc.get("deep", "#043835"),
    }
    for k, v in repl.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", tpl)))
    if leftover:
        sys.exit("unfilled template tokens: " + ", ".join(leftover))

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(tpl)
    mode = "rendered sheet" if fp else "SVG design draft"
    print("wrote %s (%s, %d panels, %.2f MB)"
          % (out_path, mode, panel_count, len(tpl) / 1024 / 1024))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Build a standalone 16:9 campaign storyboard.")
    ap.add_argument("--dir", default=".")
    ap.add_argument("--spec", default=None)
    ap.add_argument("--frames", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--template", default=os.path.join(here, "..", "templates", "storyboard.html"))
    ap.add_argument("--width", type=int, default=1600)
    a = ap.parse_args()
    spec = a.spec or os.path.join(a.dir, "media", "storyboard", "storyboard.json")
    frames = a.frames or os.path.join(a.dir, "media", "storyboard")
    out = a.out or os.path.join(a.dir, "storyboard.html")
    build(a.dir, spec, frames, out, a.template, a.width)


if __name__ == "__main__":
    main()
