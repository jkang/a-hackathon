#!/usr/bin/env python3
"""
Build a single-file, shareable version of the Facilitator Guide.

Inlines every file facilitator_guide.html references (the demo outputs
under demo-examples/QuestB-02/) so the result can be emailed / dropped
into a chat and opened with a double-click — no repo, no server, no sibling files.

Usage:  python3 build-facilitator-standalone.py
Output: facilitator_guide_standalone.html  (repo root)
"""
import io, json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.join(ROOT, "facilitator_guide.html")
V2 = os.path.join(ROOT, "demo-examples", "QuestB-02")
OUT = os.path.join(ROOT, "facilitator_guide_standalone.html")

# the seven panels embedded in the guide (title -> file)
DEMOS = ["insight-brief.html", "campaign-plan.html", "poster.html",
         "proposal.html", "pitch-deck.html", "prompt-pack.html"]

def rd(p):
    return io.open(p, encoding="utf-8").read()

def esc(s):
    """Escape a string for use inside a double-quoted HTML attribute value.
    The browser decodes entities in attribute values, so escaping < > & " keeps
    nested markup intact while remaining safe for any parser."""
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))

# injected into every embedded demo: report its height to the parent so the
# guide can auto-fit the iframe even when file:// blocks contentDocument access.
INJECT = ("<script>(function(){function h(){try{parent.postMessage("
          "{__fit:Math.max(document.documentElement.scrollHeight,document.body.scrollHeight)},\"*\");}"
          "catch(e){}}window.addEventListener(\"load\",h);window.addEventListener(\"resize\",h);"
          "setInterval(h,1500);})();</scr" + "ipt>")


def prep(name):
    """Return a demo's HTML with its own sub-references inlined / neutralised."""
    c = rd(os.path.join(V2, name))

    if name == "poster.html":
        # the posters are already inlined; the "open standalone" link would 404
        c = c.replace(
            '<a class="open" id="open" href="poster-a.html" target="_blank">Open standalone ↗</a>',
            '<span class="open" id="open">3 styles inlined</span>')
        c = c.replace("open.setAttribute('href', 'poster-' + key + '.html');",
                      "/* single-file build: styles inlined */")

    if name == "pitch-deck.html":
        # inline the poster + make the A/B/C picker swap srcdoc instead of src
        c = c.replace(
            '<iframe id="posterFrame" src="poster-a.html" title="Campaign poster"></iframe>',
            '<iframe id="posterFrame" srcdoc="' + esc(posters["a"]) + '" title="Campaign poster"></iframe>')
        js = "var POSTERS = {" + ", ".join(
            "%s:%s" % (k, json.dumps(posters[k])) for k in "abc") + "};"
        c = c.replace("  var frame = document.getElementById('posterFrame');",
                      "  " + js + "\n  var frame = document.getElementById('posterFrame');")
        c = c.replace("frame.setAttribute('src', 'poster-' + b.getAttribute('data-pstyle') + '.html');",
                      "frame.setAttribute('srcdoc', POSTERS[b.getAttribute('data-pstyle')]);")

    if name == "proposal.html":
        # proposal inlines a poster page + a pitch-deck; both still point at
        # poster-a.html. Depth here is one extra srcdoc layer, hence double esc().
        c = c.replace('href=&quot;poster-a.html&quot;', 'href=&quot;#&quot;')
        c = c.replace('src=&quot;poster-a.html&quot;',
                      'srcdoc=&quot;' + esc(esc(posters["a"])) + '&quot;')

    return c.replace("</body>", INJECT + "\n</body>")


posters = {k: rd(os.path.join(V2, "poster-%s.html" % k)) for k in "abc"}

guide = rd(GUIDE)

# 1) swap every guide iframe src=... for an inline srcdoc=...
def repl(m):
    pre, fn, post = m.group(1), m.group(2), m.group(3)
    if fn not in DEMOS:
        return m.group(0)
    return '<iframe%ssrcdoc="%s"%s></iframe>' % (pre, esc(prep(fn)), post)

guide, n_if = re.subn(
    r'<iframe([^>]*?)src="demo-examples/QuestB-02/([^"]+)"([^>]*?)></iframe>',
    repl, guide)

# 2) drop the "open ↗" links (their target files are gone)
guide, n_ln = re.subn(r'<a href="demo-examples/[^"]+" target="_blank">打开 ↗</a>', '', guide)

# 3) add a cross-origin auto-fit listener (postMessage from the iframes)
listener = ('\n  window.addEventListener("message", function(e){var d=e.data;'
            'if(!d||typeof d.__fit!=="number")return;'
            'Array.prototype.slice.call(document.querySelectorAll("iframe")).forEach(function(f){'
            'if(f.contentWindow===e.source){f.style.height=Math.min(d.__fit+10,2800)+"px";}});});\n')
guide = guide.replace("  window.addEventListener('load', function(){",
                      listener + "  window.addEventListener('load', function(){", 1)

guide = guide.replace("<title>Facilitator Guide · Ascentium Mini-Hackathon</title>",
                      "<title>Facilitator Guide · Ascentium Mini-Hackathon (single file)</title>")

io.open(OUT, "w", encoding="utf-8").write(guide)
print("iframes inlined: %d · open-links removed: %d · wrote %s (%d KB)"
      % (n_if, n_ln, os.path.basename(OUT), os.path.getsize(OUT) // 1024))
