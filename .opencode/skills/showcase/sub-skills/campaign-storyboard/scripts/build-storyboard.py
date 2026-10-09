#!/usr/bin/env python3
"""Build a standalone 16:9 campaign STORYBOARD from a spec + one 6-panel sheet image.

Reads a JSON spec + a single storyboard-sheet image, downscales the image, embeds it as a
data URI (so the result is a single self-contained HTML), and writes storyboard.html.
The sheet is generated externally from ONE complete prompt (see the showcase prompt pack),
so the whole journey arrives as one image rather than six separate frames.

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
      "crumb": "Campaign Storyboard · Chengdu Panda Base",
      "h1": "How we attract the target audience",
      "accent": {"accent":"#077069","tint":"#CDE2E1","line":"#83B8B4","deep":"#043835"},
      "board": "storyboard-sheet.png",           # one image, six panels
      "width": 1600,                             # optional override
      "steps": [                                  # optional legend (six journey steps)
        {"n":"01","label":"Attract"},
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
    sys.exit("Pillow is required: pip install Pillow")


def esc(t):
    return html.escape(str(t), quote=False)


def data_uri(path, width):
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


def legend_html(steps):
    if not steps:
        return ""
    chips = "".join(
        '<span class="lchip"><b>%s</b>%s</span>' % (esc(s.get("n", "")), esc(s.get("label", "")))
        for s in steps
    )
    return '\n    <div class="legend">%s</div>' % chips


def build(directory, spec_path, frames_dir, out_path, template_path, width):
    spec = json.load(open(spec_path, encoding="utf-8"))
    width = int(spec.get("width", width))

    board_file = spec.get("board")
    if not board_file:
        sys.exit("spec has no board image: " + spec_path)
    fp = resolve_image(frames_dir, board_file)
    if not fp:
        sys.exit("board image not found: %s" % board_file)

    uri = data_uri(fp, width)
    steps = spec.get("steps", [])
    panel_count = len(steps) or 6

    slide = (
        '<section class="slide" data-i="0">\n'
        '  <div class="brandbar"><div class="logo">%s<span>.</span></div><div class="tag">%s</div></div>\n'
        '  <div class="titlerow"><h1>%s</h1><div class="range">%d panels &middot; one sheet</div></div>\n'
        '  <div class="boardbox"><img src="%s" alt="Campaign storyboard"></div>%s\n'
        '</section>'
        % (esc(spec.get("brand", "")), esc(spec.get("crumb", "")),
           esc(spec.get("h1", "")), panel_count, uri, legend_html(steps))
    )

    tpl = open(template_path, encoding="utf-8").read()
    acc = spec.get("accent", {})
    repl = {
        "TITLE": spec.get("brand", "Campaign") + " Storyboard",
        "QUEST": spec.get("quest", ""),
        "SLIDES": slide,
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
    print("wrote %s (1 sheet, %d panels, %.2f MB)"
          % (out_path, panel_count, len(tpl) / 1024 / 1024))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Build a standalone 16:9 campaign storyboard sheet.")
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
