#!/usr/bin/env python3
"""Build a standalone campaign STORYBOARD for the mediakit stage.

Output = a 16:9 PAGINATED DECK (storyboard.html):
  • a COVER page (campaign name + slogan + premise + the 3-chapter arc), then
  • one page per 1–2 SCENE cards, each card carrying a rich, legible block:
      number · title · chapter · scene art (inline SVG) · phone/UI inset ·
      customer pull-quote · meta (stage / moment / emotion / goal) · action + source
  • an optional Board page when a rendered sheet image is supplied.

By default the scene art is drawn in-page as inline SVG — the deliverable exists
with no external image. The page also carries a copyable prompt the team can take
to Kimi / GPT for a richer RENDERED version.

Usage:
    python3 build-storyboard.py [--dir DIR] [--spec FILE] [--frames DIR] [--out FILE]
                                [--template FILE] [--per-page 1|2]

Defaults: --dir .  --spec <dir>/media/storyboard/storyboard.json
          --frames <dir>/media/storyboard  --out <dir>/storyboard.html  --per-page 2

Spec (JSON):
{
  "quest":"B", "brand":"The Panda Family", "crumb":"Campaign Media Kit · Storyboard · Quest B",
  "h1":"From watching the cam to meeting the family",
  "slogan":"Adopt the family. Collect the fun.",
  "premise":"One or two sentences on the arc.",
  "accent": {"accent":"#077069","tint":"#CDE2E1","line":"#83B8B4","deep":"#043835"},
  "theme":  {"surface":"light"},              # light | dark  (derive from the campaign plan)
  "board":  "storyboard-sheet.png",           # OPTIONAL rendered sheet; omit → inline SVG art
  "chapters": [ {"id":"I","name":"The Hook","blurb":"…"} ],
  "steps": [
    {"n":"01","chapter":"I","title":"…","scene":"…","art":"cam",
     "quote":"…","action":"…","source":"…",
     "meta":{"stage":"Trigger","moment":"…","emotion":"…","goal":"…"},
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

ART_KINDS = ("cam", "plan", "adopt", "home", "drop", "meet", "spotlight")

DEFAULT_STEPS = [
    {"n": "01", "chapter": "I", "title": "The first spark", "scene": "the everyday trigger", "art": "spotlight",
     "ui": {"screen": "Discover", "title": "A reason to go", "lines": ["See it for yourself"], "cta": "Learn more"}},
    {"n": "02", "chapter": "I", "title": "It feels personal", "scene": "she sees herself in it", "art": "spotlight",
     "ui": {"screen": "For you", "title": "Made for your family", "lines": ["Your dates, your plan"], "cta": "Continue"}},
]


def esc(t):
    return html.escape(str(t if t is not None else ""), quote=False)


def m(x):
    return ("%.1f" % x).rstrip("0").rstrip(".")


# ------------------------------------------------------------------ theme
def derive_theme(spec):
    t = spec.get("theme") or {}
    surface = str(t.get("surface", "light")).lower()
    acc = spec.get("accent") or {}
    if surface == "dark":
        base = {"page": "#07100F", "card": "#0E1918", "scene": "#0B1514",
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
    base["accent_line"] = acc.get("line", "#FFD1B8")
    base["accent_deep"] = acc.get("deep", "#B24000")
    base["light"] = surface != "dark"
    base["body"] = "#FFFFFF" if base["light"] else "#EAE4D8"
    base["dark"] = "#0F1514" if base["light"] else "#060B0B"
    base["fig"] = base["muted"] if base["light"] else "#3A5852"
    base["sky_top"] = base["accent_tint"] if base["light"] else "#12211E"
    base["sky_bot"] = base["scene"] if base["light"] else "#0A1211"
    return base


# ------------------------------------------------------------------ art pieces
def panda(cx, cy, r, th, gid):
    """A giant-panda glyph (ears · head · eye patches · muzzle)."""
    body = th["body"]
    dark = th["dark"]
    p = ['<g>']
    p.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (m(cx - 0.66 * r), m(cy - 0.70 * r), m(0.45 * r), dark))
    p.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (m(cx + 0.66 * r), m(cy - 0.70 * r), m(0.45 * r), dark))
    p.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (m(cx), m(cy), m(r), body))
    p.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" transform="rotate(-16 %s %s)"/>'
             % (m(cx - 0.35 * r), m(cy - 0.10 * r), m(0.25 * r), m(0.31 * r), dark, m(cx - 0.35 * r), m(cy - 0.10 * r)))
    p.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" transform="rotate(16 %s %s)"/>'
             % (m(cx + 0.35 * r), m(cy - 0.10 * r), m(0.25 * r), m(0.31 * r), dark, m(cx + 0.35 * r), m(cy - 0.10 * r)))
    p.append('<circle cx="%s" cy="%s" r="%s" fill="#fff"/>' % (m(cx - 0.34 * r), m(cy - 0.07 * r), m(0.085 * r)))
    p.append('<circle cx="%s" cy="%s" r="%s" fill="#fff"/>' % (m(cx + 0.34 * r), m(cy - 0.07 * r), m(0.085 * r)))
    p.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s"/>' % (m(cx), m(cy + 0.30 * r), m(0.20 * r), m(0.14 * r), dark))
    p.append('<path d="M%s %s q%s %s %s 0" stroke="%s" stroke-width="%s" fill="none" stroke-linecap="round"/>'
             % (m(cx - 0.20 * r), m(cy + 0.58 * r), m(0.20 * r), m(0.19 * r), m(0.40 * r), dark, m(max(2, 0.09 * r))))
    p.append('</g>')
    return "".join(p)


def figure(x, base, s, col, th):
    """A simple standing silhouette (head + shoulders)."""
    r = 11 * s
    head = base - 36 * s
    bw = 26 * s
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
            '<path d="M%s %s q%s %s %s 0 z" fill="%s"/>'
            % (m(x), m(head), m(r), col, m(x - bw), m(base), m(bw), m(bw + 8 * s), m(2 * bw), col))


def confetti(uid, th, seed=0):
    xs = [40, 96, 168, 250, 322, 470, 560, 636, 700, 748, 130, 610]
    ys = [58, 30, 92, 44, 118, 36, 84, 52, 106, 30, 138, 132]
    cols = [th["accent"], th["accent_line"], th["accent"], th["accent_line"]]
    out = []
    for i, (x, y) in enumerate(zip(xs, ys)):
        k = (i + seed) % 4
        w, h = (7, 7) if k % 2 == 0 else (5, 9)
        out.append('<rect x="%s" y="%s" width="%d" height="%d" rx="2" fill="%s" opacity="%s" transform="rotate(%d %s %s)"/>'
                   % (m(x), m(y), w, h, cols[k], ".55" if th["light"] else ".4", (i * 37) % 90, m(x), m(y)))
    return "".join(out)


def _base(uid, th, w=800, h=420):
    """Scene backdrop: gradient sky + accent glow + ground line."""
    return (
        '<defs><linearGradient id="sky%s" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
        '<clipPath id="cp%s"><rect width="%d" height="%d" rx="0"/></clipPath></defs>'
        '<rect width="%d" height="%d" fill="url(#sky%s)"/>'
        % (uid, th["sky_top"], th["sky_bot"], uid, w, h, w, h, uid)
    )


def art_cam(uid, th):
    """The always-on panda cam, watched from home."""
    p = [_base(uid, th)]
    p.append('<circle cx="560" cy="150" r="150" fill="%s" opacity="%s"/>' % (th["accent_tint"] if th["light"] else th["accent"], ".5" if th["light"] else ".22"))
    # sofa + household
    p.append('<rect x="40" y="286" width="300" height="66" rx="20" fill="%s" opacity=".55"/>' % th["fig"])
    p.append(figure(96, 292, 1.25, th["fig"], th))
    p.append(figure(200, 292, 1.35, th["accent"], th))
    p.append(figure(292, 292, 1.15, th["fig"], th))
    # monitor
    p.append('<rect x="452" y="104" width="292" height="188" rx="14" fill="%s"/>' % th["dark"])
    p.append('<rect x="464" y="116" width="268" height="150" rx="8" fill="%s"/>' % th["body"])
    p.append(panda(598, 190, 34, th, uid))
    p.append('<rect x="544" y="276" width="108" height="10" rx="5" fill="%s"/>' % th["dark"])
    p.append('<rect x="584" y="286" width="28" height="22" rx="4" fill="%s"/>' % th["dark"])
    p.append('<rect x="474" y="124" width="46" height="17" rx="8" fill="%s" opacity=".16"/>' % th["accent"])
    p.append('<circle cx="485" cy="132.5" r="4" fill="%s"/><text x="494" y="136" font-size="9.5" font-weight="800" fill="%s" font-family="Poppins,Arial">LIVE</text>' % (th["accent"], th["accent"]))
    p.append('<line x1="0" y1="352" x2="800" y2="352" stroke="%s" stroke-width="1.5" opacity=".7"/>' % th["fig"])
    p.append(confetti(uid, th, 1)[:0])
    return "".join(p)


def art_plan(uid, th):
    """Planning the visa-free trip on a phone."""
    p = [_base(uid, th)]
    p.append('<circle cx="230" cy="140" r="128" fill="%s" opacity="%s"/>' % (th["accent_tint"] if th["light"] else th["accent"], ".5" if th["light"] else ".22"))
    p.append('<path d="M60 300 C 220 210, 400 250, 700 96" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="3 12"/>' % th["accent"])
    p.append('<path d="M700 96 l-30 8 18 16z" fill="%s"/>' % th["accent"])
    p.append(figure(150, 356, 1.5, th["fig"], th))
    p.append('<g transform="rotate(-6 500 232)">')
    p.append('<rect x="392" y="86" width="216" height="292" rx="24" fill="%s"/>' % th["dark"])
    p.append('<rect x="402" y="96" width="196" height="272" rx="18" fill="%s"/>' % th["body"])
    p.append('<rect x="452" y="102" width="96" height="7" rx="3.5" fill="%s" opacity=".5"/>' % th["dark"])
    p.append('<path d="M420 300 l60 -54 54 26 46 -58" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % th["accent"])
    p.append('<circle cx="500" cy="246" r="9" fill="%s"/><circle cx="500" cy="246" r="3.4" fill="%s"/>' % (th["accent"], th["body"]))
    p.append('<rect x="420" y="318" width="160" height="34" rx="10" fill="%s" opacity=".45"/>' % th["accent_line"])
    p.append('</g>')
    p.append('<g transform="translate(660,300)"><circle r="46" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="7 6"/>'
             '<text x="0" y="-2" text-anchor="middle" font-size="11" font-weight="800" fill="%s" font-family="Poppins,Arial">VISA</text>'
             '<text x="0" y="13" text-anchor="middle" font-size="11" font-weight="800" fill="%s" font-family="Poppins,Arial">FREE</text></g>'
             % (th["accent"], th["accent"], th["accent"]))
    p.append('<line x1="0" y1="356" x2="800" y2="356" stroke="%s" stroke-width="1.5" opacity=".7"/>' % th["fig"])
    return "".join(p)


def art_adopt(uid, th):
    """Adopting a named panda — certificate + confetti."""
    p = [_base(uid, th)]
    p.append(confetti(uid, th, 0))
    p.append('<circle cx="400" cy="210" r="170" fill="%s" opacity="%s"/>' % (th["accent_tint"] if th["light"] else th["accent"], ".55" if th["light"] else ".24"))
    p.append(panda(238, 210, 62, th, uid))
    p.append('<g transform="rotate(-3 520 210)">')
    p.append('<rect x="374" y="96" width="316" height="230" rx="16" fill="%s" stroke="%s" stroke-width="2"/>' % (th["body"], th["accent_line"]))
    p.append('<rect x="374" y="96" width="316" height="40" rx="16" fill="%s"/>' % th["accent"])
    p.append('<rect x="374" y="120" width="316" height="16" fill="%s"/>' % th["accent"])
    p.append('<text x="392" y="122" font-size="13" font-weight="800" fill="#fff" font-family="Poppins,Arial" letter-spacing="1.4">FAMILY CERTIFICATE</text>')
    p.append('<rect x="620" y="144" width="52" height="20" rx="10" fill="%s"/>' % th["accent"])
    p.append('<text x="646" y="158" font-size="10" font-weight="800" fill="#fff" text-anchor="middle" font-family="Poppins,Arial">No. 001</text>')
    p.append('<rect x="392" y="180" width="120" height="11" rx="5" fill="%s" opacity=".45"/>' % th["dark"])
    p.append('<rect x="392" y="202" width="200" height="9" rx="4" fill="%s" opacity=".22"/>' % th["dark"])
    p.append('<rect x="392" y="220" width="164" height="9" rx="4" fill="%s" opacity=".22"/>' % th["dark"])
    p.append(panda(440, 276, 22, th, uid + "c"))
    p.append('<rect x="530" y="252" width="140" height="9" rx="4" fill="%s" opacity=".22"/>' % th["dark"])
    p.append('<rect x="530" y="270" width="112" height="9" rx="4" fill="%s" opacity=".22"/>' % th["dark"])
    p.append('</g>')
    return "".join(p)


def art_home(uid, th):
    """One membership for the whole household."""
    p = [_base(uid, th)]
    p.append('<circle cx="400" cy="170" r="158" fill="%s" opacity="%s"/>' % (th["accent_tint"] if th["light"] else th["accent"], ".5" if th["light"] else ".22"))
    # four figures around a tablet
    p.append(figure(150, 344, 1.35, th["fig"], th))
    p.append(figure(250, 344, 1.6, th["accent"], th))
    p.append(figure(556, 344, 1.6, th["accent"], th))
    p.append(figure(656, 344, 1.35, th["fig"], th))
    p.append('<g transform="rotate(-4 404 250)">')
    p.append('<rect x="304" y="150" width="200" height="150" rx="14" fill="%s"/>' % th["dark"])
    p.append('<rect x="313" y="159" width="182" height="118" rx="8" fill="%s"/>' % th["body"])
    p.append(panda(404, 214, 26, th, uid))
    p.append('<rect x="322" y="286" width="164" height="8" rx="4" fill="%s" opacity=".4"/>' % th["dark"])
    p.append('</g>')
    p.append('<line x1="0" y1="358" x2="800" y2="358" stroke="%s" stroke-width="1.5" opacity=".7"/>' % th["fig"])
    return "".join(p)


def art_drop(uid, th):
    """The numbered seasonal drop the family collects."""
    p = [_base(uid, th)]
    p.append(confetti(uid, th, 2))
    p.append('<circle cx="400" cy="220" r="164" fill="%s" opacity="%s"/>' % (th["accent_tint"] if th["light"] else th["accent"], ".5" if th["light"] else ".22"))
    p.append('<g transform="rotate(-10 340 226)">')
    p.append('<rect x="262" y="112" width="176" height="228" rx="16" fill="%s" stroke="%s" stroke-width="2"/>' % (th["body"], th["accent_line"]))
    p.append('<rect x="262" y="112" width="176" height="34" rx="16" fill="%s"/><rect x="262" y="132" width="176" height="14" fill="%s"/>' % (th["accent"], th["accent"]))
    p.append(panda(350, 236, 44, th, uid))
    p.append('<rect x="284" y="300" width="132" height="10" rx="5" fill="%s" opacity=".4"/>' % th["dark"])
    p.append('</g>')
    p.append('<g transform="rotate(8 512 244)">')
    p.append('<rect x="424" y="130" width="176" height="228" rx="16" fill="%s" stroke="%s" stroke-width="2"/>' % (th["body"], th["accent_line"]))
    p.append('<rect x="424" y="130" width="176" height="34" rx="16" fill="%s"/><rect x="424" y="150" width="176" height="14" fill="%s"/>' % (th["accent"], th["accent"]))
    p.append(panda(512, 254, 44, th, uid + "2"))
    p.append('<rect x="446" y="318" width="132" height="10" rx="5" fill="%s" opacity=".4"/>' % th["dark"])
    p.append('</g>')
    p.append('<g fill="%s"><path d="M690 118 l5 14 14 5 -14 5 -5 14 -5 -14 -14 -5 14 -5z"/><path d="M96 128 l4 11 11 4 -11 4 -4 11 -4 -11 -11 -4 11 -4z"/></g>' % th["accent"])
    return "".join(p)


def art_meet(uid, th):
    """Meeting the family in Chengdu."""
    p = [_base(uid, th)]
    p.append('<circle cx="410" cy="150" r="150" fill="%s" opacity="%s"/>' % (th["accent_tint"] if th["light"] else th["accent"], ".55" if th["light"] else ".24"))
    # bamboo
    p.append('<g stroke="%s" stroke-width="7" opacity=".55"><line x1="86" y1="80" x2="86" y2="352"/><line x1="126" y1="150" x2="126" y2="352"/></g>' % th["accent"])
    p.append('<g fill="%s" opacity=".6"><ellipse cx="102" cy="120" rx="20" ry="7" transform="rotate(-24 102 120)"/><ellipse cx="70" cy="160" rx="20" ry="7" transform="rotate(24 70 160)"/></g>' % th["accent"])
    p.append(panda(420, 216, 82, th, uid))
    p.append(figure(250, 356, 1.6, th["accent"], th))
    p.append(figure(560, 356, 1.7, th["accent"], th))
    p.append(figure(634, 356, 1.4, th["fig"], th))
    p.append(figure(190, 356, 1.3, th["fig"], th))
    # camera flashes
    p.append('<g fill="%s" opacity=".9"><path d="M660 150 l6 16 16 6 -16 6 -6 16 -6 -16 -16 -6 16 -6z"/><path d="M180 196 l4 11 11 4 -11 4 -4 11 -4 -11 -11 -4 11 -4z"/></g>' % th["accent"])
    p.append('<line x1="0" y1="356" x2="800" y2="356" stroke="%s" stroke-width="1.5" opacity=".7"/>' % th["fig"])
    return "".join(p)


def art_spotlight(uid, th):
    p = [_base(uid, th)]
    p.append(confetti(uid, th, 0))
    p.append('<circle cx="400" cy="212" r="166" fill="%s" opacity="%s"/>' % (th["accent_tint"] if th["light"] else th["accent"], ".55" if th["light"] else ".24"))
    p.append(panda(400, 216, 88, th, uid))
    p.append('<line x1="0" y1="358" x2="800" y2="358" stroke="%s" stroke-width="1.5" opacity=".7"/>' % th["fig"])
    return "".join(p)


ART = {"cam": art_cam, "plan": art_plan, "adopt": art_adopt, "home": art_home,
       "drop": art_drop, "meet": art_meet, "spotlight": art_spotlight}


def scene_art(kind, uid, th):
    fn = ART.get(str(kind or "").strip().lower(), art_spotlight)
    return fn(uid, th)


# ------------------------------------------------------------------ page builders
def phone_html(step):
    ui = step.get("ui") or {}
    lines = ui.get("lines") or []
    if not (ui.get("title") or lines or ui.get("cta")):
        return ""
    h = ['<div class="phone">']
    if ui.get("screen"):
        h.append('<div class="pl">%s</div>' % esc(ui["screen"]))
    if ui.get("title"):
        h.append('<div class="pt">%s</div>' % esc(ui["title"]))
    if lines:
        h.append('<div class="px">%s</div>' % esc(" · ".join(str(x) for x in lines)))
    if ui.get("cta"):
        h.append('<div class="pc">%s</div>' % esc(ui["cta"]))
    h.append('</div>')
    return "".join(h)


def meta_html(step, th, chapter_name):
    meta = step.get("meta") or {}
    rows = [
        ("Stage", meta.get("stage") or chapter_name),
        ("Moment", meta.get("moment")),
        ("Emotion", meta.get("emotion")),
        ("Goal", meta.get("goal")),
    ]
    rows = [(k, v) for k, v in rows if v]
    if not rows:
        return ""
    return '<dl class="meta">%s</dl>' % "".join(
        '<div><dt>%s</dt><dd>%s</dd></div>' % (esc(k), esc(v)) for k, v in rows)


def scene_card(step, i, th, chmap, one=False):
    ch_id = step.get("chapter", "")
    ch_name = chmap.get(ch_id, "")
    stage = ("%s · %s" % (ch_id, ch_name)) if ch_name else ch_id
    quote = step.get("quote")
    action = step.get("action")
    source = step.get("source")
    scene_line = step.get("scene")
    body = (
        '<div class="shead">'
        '<span class="snum">%s</span>'
        '<div class="stitle"><h3>%s</h3><span class="stag">%s</span></div>'
        '</div>'
        % (esc(step.get("n", "%02d" % (i + 1))), esc(step.get("title", "")), esc(stage))
    )
    art = ('<div class="sart"><svg viewBox="0 0 800 420" preserveAspectRatio="xMidYMid slice" '
           'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">%s</svg>%s</div>'
           % (esc(scene_line or ""), scene_art(step.get("art"), "a%d" % i, th), phone_html(step)))
    extra = ('<blockquote class="quote">%s</blockquote>' % esc(quote)) if quote else ""
    scene_html = ('<div class="sceneline">%s</div>' % esc(scene_line)) if (scene_line and not one) else ""
    saction = ""
    if action or source:
        saction = ('<div class="saction"><span class="act">%s</span><span class="src">%s</span></div>'
                   % (esc(action or ""), esc(source or "")))
    if one:
        scene_html_one = ('<div class="sceneline" style="margin:0;">%s</div>' % esc(scene_line)) if scene_line else ""
        return ('<article class="scene">%s<div class="ctext"><div class="inner">%s%s%s%s%s</div></div></article>'
                % (art, body, scene_html_one, extra, meta_html(step, th, ch_name), saction))
    return ('<article class="scene">%s%s%s%s%s%s</article>'
            % (body, art, scene_html, extra, meta_html(step, th, ch_name), saction))


def cover_page(spec, chapters, steps, th):
    brand = esc(spec.get("brand", "The Campaign"))
    crumb = esc(spec.get("crumb", ""))
    slogan = spec.get("slogan")
    premise = spec.get("premise")
    by_ch = {}
    for s in steps:
        by_ch.setdefault(s.get("chapter"), []).append(s)
    cards = []
    for ch in chapters:
        ns = [str(s.get("n", "")) for s in by_ch.get(ch.get("id"), [])]
        cards.append(
            '<div class="arcch"><span class="rn">%s</span><b>%s</b>'
            '<div class="sc">%s</div><p>%s</p></div>'
            % (esc(ch.get("id", "")), esc(ch.get("name", "")),
               esc(" · ".join(ns)) if ns else "", esc(ch.get("blurb", ""))))
    slogan_html = ('<div class="coslogan">&ldquo;%s&rdquo;</div>' % esc(slogan)) if slogan else ""
    premise_html = ('<div class="premise">%s</div>' % esc(premise)) if premise else ""
    hero_kind = spec.get("cover_art") or (steps[0].get("art") if steps else "spotlight")
    hero = ('<div class="coverhero"><svg viewBox="0 0 800 420" preserveAspectRatio="xMidYMid slice" '
            'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="campaign key visual">%s</svg></div>'
            % scene_art(hero_kind, "cov", th))
    facts = spec.get("facts") or []
    facts_html = ""
    if facts:
        facts_html = ('<div class="coverfacts">%s</div>'
                      % "".join('<div class="cfact"><div class="n">%s</div><div class="c">%s</div></div>'
                                % (esc(f.get("n", "")), esc(f.get("c", ""))) for f in facts[:4]))
    return (
        '<section class="slide cover">'
        '<div class="brandbar"><div class="logo">Ascentium<span>.</span></div><div class="tag">%s</div></div>'
        '<div class="coverbody">'
        '<div class="covertext">'
        '<div class="kicker">%s</div>'
        '<div class="confname">%s</div>%s%s'
        '</div>%s'
        '</div>%s'
        '<div class="arcgrid">%s</div>'
        '<div class="covernote"><span>%d scenes &middot; %d chapters &middot; scene-by-scene fan journey</span>'
        '<span><b>%s</b></span></div>'
        '</section>'
        % (crumb, esc(spec.get("h1", "")), brand, slogan_html, premise_html, hero, facts_html,
           "".join(cards), len(steps), max(1, len(chapters)),
           esc(spec.get("one_liner", "")))
    )


def scene_pages(steps, chapters, th, per_page):
    chmap = {c.get("id"): c.get("name", "") for c in chapters}
    out = []
    for pg in range(0, len(steps), per_page):
        group = steps[pg:pg + per_page]
        nums = "–".join([str(group[0].get("n", "")), str(group[-1].get("n", ""))]) if len(group) > 1 else str(group[0].get("n", ""))
        ch_ids = []
        for s in group:
            c = s.get("chapter", "")
            if c and c not in ch_ids:
                ch_ids.append(c)
        head_c = " &nbsp;/&nbsp; ".join("%s · %s" % (c, chmap.get(c, "")) for c in ch_ids)
        cards = "".join(scene_card(s, pg + k, th, chmap, one=(per_page == 1)) for k, s in enumerate(group))
        out.append(
            '<section class="slide">'
            '<div class="brandbar"><div class="logo">Ascentium<span>.</span></div>'
            '<div class="tag">%s &middot; Storyboard</div></div>'
            '<div class="titlerow"><h1>%s</h1><div class="range">Scenes %s</div></div>'
            '<div class="cards %s">%s</div>'
            '</section>'
            % (esc(chmap.get(group[0].get("chapter", ""), "Scene")),
               esc(head_c or "Scene"), esc(nums), "one" if per_page == 1 else "two", cards)
        )
    return out


def board_page(spec, sheet_src, steps, chapters):
    return (
        '<section class="slide">'
        '<div class="brandbar"><div class="logo">Ascentium<span>.</span></div>'
        '<div class="tag">%s</div></div>'
        '<div class="titlerow"><h1>%s</h1><div class="range">%d scenes &middot; %d chapters</div></div>'
        '<div class="boardbox"><img src="%s" alt="Campaign storyboard"></div>'
        '</section>'
        % (esc(spec.get("crumb", "")), esc(spec.get("h1", "")), len(steps), max(1, len(chapters)), sheet_src)
    )


def richer_page(spec, doc, steps, chapters):
    """A page that inlines a richer self-contained HTML storyboard (srcdoc, so the deck stays single-file)."""
    return (
        '<section class="slide">'
        '<div class="brandbar"><div class="logo">Ascentium<span>.</span></div>'
        '<div class="tag">%s</div></div>'
        '<div class="titlerow"><h1>%s</h1><div class="range">richer board &middot; %d scenes</div></div>'
        '<div class="boardbox"><iframe title="Richer storyboard" srcdoc="%s"></iframe></div>'
        '</section>'
        % (esc(spec.get("crumb", "")), esc(spec.get("h1", "")), len(steps), html.escape(doc, quote=True))
    )


# ------------------------------------------------------------------ raster + prompt
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


def resolve_html(frames_dir, name):
    """Resolve a richer self-contained HTML storyboard (the upgrade the team generates in Kimi / GPT).
    HTML only — a PPT/slide-deck file is never accepted."""
    if not name:
        return None
    stem = os.path.splitext(os.path.join(frames_dir, name))[0]
    for ext in (".html", ".htm"):
        if os.path.isfile(stem + ext):
            return stem + ext
    return None


def default_prompt(spec, steps, chapters):
    brand = spec.get("brand", "the campaign")
    ch_names = " / ".join("%s. %s" % (c.get("id", ""), c.get("name", "")) for c in chapters)
    lines = [
        '=== THE CAMPAIGN ===',
        '%s.' % brand,
        '',
        '=== WHAT TO WRITE: THE FAN JOURNEY, SCENE BY SCENE ===',
        'Arc: %d scenes grouped into %d chapters — %s. Rename the chapters if the campaign reads better that way.'
        % (len(steps), max(1, len(chapters)), ch_names),
        '',
        'For each scene, write:',
        '  • Number and a short, punchy title.',
        '  • The story beat: who is in the scene, where they are, what is happening, and what they feel.',
        '  • The product state at that moment: the app/phone screen title, one or two supporting lines, and '
        'the button label.',
        '  • A one-line quote in the fan\'s own voice.',
        '  • Four fields — Stage · Moment · Emotion · Goal.',
        '  • The campaign action taken in that scene, and the evidence it rests on.',
        '',
        'THE SCENES (use this content, keep the order):',
    ]
    for idx, s in enumerate(steps):
        n = s.get("n", "%02d" % (idx + 1))
        ui = s.get("ui") or {}
        meta = s.get("meta") or {}
        quote = s.get("quote")
        lines.append('')
        lines.append('Scene %s · %s' % (n, str(s.get("title", ""))))
        lines.append('  Beat: %s' % str(s.get("scene", "")))
        lines.append('  On screen: "%s" — %s — button "%s"'
                     % (ui.get("title", ""), " / ".join([str(x) for x in (ui.get("lines") or [])]), ui.get("cta", "")))
        if quote:
            lines.append('  Fan quote: "%s"' % quote)
        lines.append('  Fields: Stage "%s" · Moment "%s" · Emotion "%s" · Goal "%s"'
                     % (meta.get("stage", ""), meta.get("moment", ""), meta.get("emotion", ""), meta.get("goal", "")))
        if s.get("action") or s.get("source"):
            lines.append('  Action: %s  (evidence: %s)' % (s.get("action", ""), s.get("source", "")))
    lines += [
        '',
        '=== HOW TO DELIVER IT ===',
        'One complete, self-contained .html file that opens by double-clicking on any machine — all CSS and '
        'illustration inline, no external files, no CDN, no build step. HTML ONLY: do not output a PPT / PPTX / '
        'Keynote / Google Slides file or any slide-deck export.',
        'It should page through a cover and then the scenes, at 16:9, scaled to any screen.',
        '',
        'Design it completely — the art, the colour, the typography and the layout — to fit the campaign.',
        '',
        'Generate one image for each step, and output the entire Storyboard as one complete, self-contained HTML file with every image embedded.',
    ]
    return "\n".join(lines)


def overlay_html(prompt):
    if not prompt:
        return ""
    return (
        '<div class="ph"><h2>Write a richer storyboard</h2>'
        '<button class="pclose" id="pclose">Close</button></div>'
        '<div class="note"><b>=== GIVE THE MODEL THIS INPUT FIRST (best results) ===</b><br>'
        'Attach or paste the campaign plan — the contents of <code>campaign-plan.html</code> (its capture block '
        'holds the campaign name, slogan, proposition, offer, audiences, moments and budget). If you have it, '
        'paste <code>insight-brief.html</code> as well for the audience and the market context. <b>Then paste '
        'this prompt</b> into <b>Kimi</b> (kimi.moonshot.cn) or <b>GPT</b>. It returns a '
        '<b>self-contained .html</b> (HTML only, never a PPT/slide file); save it as '
        '<b>media/storyboard/storyboard-richer.html</b> and re-run the build to add it as a page.</div>'
        '<div class="promptbox"><button class="copy" id="pcopy">Copy prompt</button>'
        '<pre id="pprompt">%s</pre></div>' % esc(prompt)
    )


# ------------------------------------------------------------------ build
def build(spec_path, frames_dir, out_path, template_path, per_page):
    spec = json.load(open(spec_path, encoding="utf-8"))
    th = derive_theme(spec)
    steps = spec.get("steps") or DEFAULT_STEPS
    chapters = spec.get("chapters") or [
        {"id": "I", "name": "The Hook"}, {"id": "II", "name": "The Offer"}, {"id": "III", "name": "Belonging"}]
    per_page = per_page if per_page else int(spec.get("per_page") or 2)
    per_page = 1 if per_page <= 1 else 2

    chapters = [c if isinstance(c, dict) else {"id": str(c), "name": ""} for c in chapters]

    board_file = spec.get("board") or "storyboard-sheet"
    fp = resolve_image(frames_dir, board_file)
    rich_file = spec.get("richer") or "storyboard-richer"
    fr = resolve_html(frames_dir, rich_file)

    slides = [cover_page(spec, chapters, steps, th)]
    mode_bits = []
    if fr:
        # a richer self-contained HTML board (HTML only — never a PPT) is inlined as its own page
        slides.append(richer_page(spec, open(fr, encoding="utf-8").read(), steps, chapters))
        mode_bits.append("richer HTML board")
    if fp:
        slides.append(board_page(spec, data_uri(fp), steps, chapters))
        mode_bits.append("rendered sheet")
    if not fr and not fp:
        slides += scene_pages(steps, chapters, th, per_page)
        mode_bits.append("SVG pages (%d/page)" % per_page)
    mode = "cover + " + " + ".join(mode_bits)

    prompt = spec.get("upgrade_prompt") or default_prompt(spec, steps, chapters)

    tpl = open(template_path, encoding="utf-8").read()
    acc = spec.get("accent") or {}
    repl = {
        "TITLE": spec.get("brand", "Campaign") + " Storyboard",
        "QUEST": spec.get("quest", ""),
        "SURFACE": th["surface"],
        "PERPAGE": str(per_page),
        "SLIDES": "\n".join(slides),
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
    print("wrote %s (%s, %d scenes, %d chapters, %d pages, %.0f KB)"
          % (out_path, mode, len(steps), max(1, len(chapters)), len(slides), len(tpl) / 1024))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Build a standalone 16:9 paginated campaign storyboard.")
    ap.add_argument("--dir", default=".")
    ap.add_argument("--spec", default=None)
    ap.add_argument("--frames", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--per-page", dest="per_page", type=int, default=None, choices=(1, 2),
                    help="scenes per page (default: the spec's per_page, else 2)")
    ap.add_argument("--template", default=os.path.join(here, "..", "templates", "storyboard.html"))
    a = ap.parse_args()
    spec = a.spec or os.path.join(a.dir, "media", "storyboard", "storyboard.json")
    frames = a.frames or os.path.join(a.dir, "media", "storyboard")
    out = a.out or os.path.join(a.dir, "storyboard.html")
    build(spec, frames, out, a.template, a.per_page)


if __name__ == "__main__":
    main()
