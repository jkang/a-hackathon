#!/usr/bin/env python3
"""Build the single-file version of the Host deck.

- Reads `host-deck.html` and inlines every external asset as a base64 data URI:
  * the toolkit-demo screenshots referenced in the scene engine as
    `P+'img-XX.jpg'` (assets/video/*.jpg)
  * any `src="assets/*"` images (e.g. the seating chart)
- Writes `host-deck-standalone.html` — one shareable file with no external
  image dependencies, so the built-in toolkit demo plays on its own.

Usage:  python3 build-host-standalone.py
"""
import base64
import mimetypes
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "host-deck.html")
OUT = os.path.join(HERE, "host-deck-standalone.html")
VID = os.path.join(HERE, "assets", "video")

missing = []


def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


def inline_scene_img(m):
    fn = m.group(1)
    path = os.path.join(VID, fn)
    if not os.path.isfile(path):
        missing.append(fn)
        return m.group(0)
    return "'" + data_uri(path) + "'"


def inline_src(m):
    rel = m.group(1)
    path = os.path.join(HERE, rel)
    if not os.path.isfile(path):
        missing.append(rel)
        return m.group(0)
    return 'src="' + data_uri(path) + '"'


src = open(SRC, encoding="utf-8").read()

# toolkit-demo screenshots (JS: img:P+'img-XX.jpg')
out = re.sub(r"P\+'(img-[\w.-]+\.jpg)'", inline_scene_img, src)
# any remaining src="assets/..." images
out = re.sub(r'src="(assets/[^"]+)"', inline_src, out)

open(OUT, "w", encoding="utf-8").write(out)
print("wrote", OUT, "({:.1f} MB)".format(os.path.getsize(OUT) / 1e6))
if missing:
    print("WARNING: could not inline (left as-is):", ", ".join(missing))
