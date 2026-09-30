#!/usr/bin/env python3
"""
Build the single-file versions of the hackathon page.

- Reads Hackathon Design/index.html and inlines every `assets/*` image it
  references as a base64 data URI -> Hackathon Design/ascentium-hackathon-standalone.html
  (title gets a " (single file)" suffix, mirroring the existing build).

Usage:  python3 build-hackathon-standalone.py
"""
import base64, mimetypes, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
HD = os.path.join(ROOT, "Hackathon Design")


def inline_assets(html):
    def repl(m):
        rel = m.group(1)
        path = os.path.join(HD, rel)
        mime = mimetypes.guess_type(path)[0] or "image/png"
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode()
        return 'src="data:%s;base64,%s"' % (mime, b64)
    return re.sub(r'src="(assets/[^"]+)"', repl, html)


def build(src_name, out_name):
    src = os.path.join(HD, src_name)
    html = open(src, encoding="utf-8").read()
    html = inline_assets(html)
    html = html.replace("</title>", " (single file)</title>", 1)
    out = os.path.join(HD, out_name)
    open(out, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB)" % (os.path.relpath(out, ROOT), len(html) // 1024))


if __name__ == "__main__":
    build("index.html", "ascentium-hackathon-standalone.html")
