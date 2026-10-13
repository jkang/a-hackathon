#!/usr/bin/env python3
"""
Build visualized, single-file HTML versions of the two Quest facilitator scripts.

Reads the bilingual markdown scripts at the repo root and writes a styled,
self-contained HTML page for each (Ascentium brand, no build/runtime deps).
The Facilitator Guide links to / embeds these pages.

Usage:  python3 build-quest-scripts.py
Output: doha-quest-facilitator-script.html  ·  panda-quest-facilitator-script.html
"""
import io, os, re
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))

# EN / ZH chips use a fixed orange / teal pair (matches the Facilitator Guide);
# the page accent is the Ascentium orange across both scripts.
EN_TINT, EN_LINE, EN_DEEP = "#FFF0E7", "#FFD1B8", "#B24000"
ZH_BG, ZH_FG, ZH_LINE = "#E6F2F1", "#05554F", "#BFDEDA"
ACCENT = "#FF6611"

CJK = re.compile(r"[\u4e00-\u9fff]")

SCRIPTS = [
    dict(
        md="DOHA_quest-facilitator_script.md",
        out="doha-quest-facilitator-script.html",
        kicker="Facilitator Script · Quest A",
        title="Doha 2030 · Quest A",
        sub="Short bilingual facilitator script · 简短双语话术 · 门票与球迷互动营销",
    ),
    dict(
        md="Panda_Quest_Facilitator_Script.md",
        out="panda-quest-facilitator-script.html",
        kicker="Facilitator Script · Quest B",
        title="Chengdu Panda Base · Quest B",
        sub="Short bilingual facilitator script · 简短双语话术 · 全球化 IP 会员 Campaign",
    ),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Facilitator Script · Ascentium Mini-Hackathon</title>
<style>
  :root{{
    --ascentium-orange:{accent}; --ascentium-midnight:#0F1514;
    --line:#E4E8E7; --bg:#F7F6F4; --card:#FFFFFF; --mut:#5A6663;
    --accent:{accent}; --accent-tint:{en_tint}; --accent-line:{en_line}; --accent-deep:{en_deep};
    --zh-bg:{zh_bg}; --zh-fg:{zh_fg}; --zh-line:{zh_line};
  }}
  *{{margin:0;padding:0;box-sizing:border-box;}}
  html{{scroll-behavior:smooth;}}
  body{{font-family:"Poppins","Noto Sans SC","PingFang SC","Microsoft YaHei",Arial,sans-serif;
       background:var(--bg);color:var(--ascentium-midnight);line-height:1.7;-webkit-font-smoothing:antialiased;}}
  a{{color:var(--accent);}}

  .topbar{{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.94);backdrop-filter:blur(8px);
          border-bottom:1px solid var(--line);}}
  .topbar .in{{display:flex;align-items:center;gap:14px;padding:12px 32px;flex-wrap:wrap;}}
  .logo{{font-weight:800;font-size:18px;}} .logo span{{color:var(--accent);}}
  .topbar .back{{margin-left:auto;font-size:12px;font-weight:600;color:var(--mut);text-decoration:none;
        border:1px solid var(--line);border-radius:999px;padding:5px 13px;background:#fff;}}
  .topbar .back:hover{{border-color:var(--accent-line);color:var(--accent);background:var(--accent-tint);}}

  .page{{max-width:1000px;margin:0 auto;padding:34px 32px 84px;}}
  header.hero{{border-bottom:3px solid var(--accent);padding-bottom:18px;}}
  .tag{{font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);}}
  header.hero h1{{font-size:33px;font-weight:800;letter-spacing:-.02em;margin-top:6px;}}
  header.hero p{{font-size:14px;color:var(--mut);margin-top:8px;}}

  .toc{{display:flex;flex-wrap:wrap;gap:6px;margin-top:18px;}}
  .toc a{{font-size:12px;font-weight:600;color:var(--mut);text-decoration:none;border:1px solid var(--line);
        border-radius:999px;padding:4px 12px;background:#fff;}}
  .toc a:hover{{border-color:var(--accent-line);color:var(--accent);background:var(--accent-tint);}}

  main{{margin-top:6px;}}
  h2{{font-size:20px;font-weight:800;margin-top:34px;padding:12px 16px;background:var(--accent-tint);
     border:1px solid var(--accent-line);border-radius:12px;color:var(--ascentium-midnight);scroll-margin-top:72px;}}
  h3{{font-size:15px;font-weight:800;margin-top:22px;color:var(--accent-deep);letter-spacing:.01em;}}
  h4{{font-size:14px;font-weight:800;margin-top:18px;color:var(--ascentium-midnight);}}

  blockquote{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 18px;
             margin-top:10px;box-shadow:0 1px 2px rgba(15,21,20,.03);}}
  blockquote p{{margin:8px 0;font-size:14px;}}
  blockquote p:first-child{{margin-top:0;}}
  blockquote p:last-child{{margin-bottom:0;}}
  blockquote p.lang-en,blockquote p.lang-zh{{background:transparent;}}

  .lang-label{{display:inline-flex;align-items:center;gap:6px;margin-top:16px;font-size:10.5px;font-weight:800;
        letter-spacing:.12em;text-transform:uppercase;color:var(--accent-deep);background:var(--accent-tint);
        border:1px solid var(--accent-line);border-radius:999px;padding:3px 12px;}}
  .lang-label.zh{{color:var(--zh-fg);background:var(--zh-bg);border-color:var(--zh-line);}}

  .tag{{display:inline-block;font-size:10px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;
       border-radius:6px;padding:2px 8px;margin-right:8px;vertical-align:1px;}}
  p.lang-en .tag{{background:var(--accent-tint);color:var(--accent-deep);}}
  p.lang-zh .tag{{background:var(--zh-bg);color:var(--zh-fg);}}
  header.hero .tag{{background:none;padding:0;margin:0;}}

  .facilitator-note{{background:#FAFBFA;border:1px dashed var(--line);border-radius:12px;padding:12px 16px;
        margin-top:12px;font-size:13px;color:#2B3A38;}}
  .facilitator-note .fn-tag{{display:block;font-size:10px;font-weight:800;letter-spacing:.12em;
        text-transform:uppercase;color:var(--accent);margin-bottom:4px;}}

  ul,ol{{margin:10px 0 0 0;padding-left:22px;}}
  li{{margin:7px 0;font-size:14px;}}
  li>p{{margin:4px 0;}}
  p{{font-size:14px;}}
  hr{{border:none;border-top:1px dashed var(--line);margin:28px 0;}}
  strong{{color:var(--ascentium-midnight);}}
  code{{font-family:"SF Mono",Consolas,Menlo,monospace;font-size:12.5px;background:var(--accent-tint);
       color:var(--accent-deep);border-radius:5px;padding:1px 6px;}}

  footer{{margin-top:44px;border-top:1px dashed var(--line);padding-top:14px;font-size:11px;color:#9AA5A2;}}

  @media (max-width:760px){{
    .page{{padding:24px 18px 64px;}}
    header.hero h1{{font-size:26px;}}
  }}
</style>
</head>
<body>

<div class="topbar">
  <div class="in">
    <div class="logo">Ascentium<span>.</span></div>
    <a class="back" href="facilitator_guide.html">← Facilitator Guide</a>
  </div>
</div>

<div class="page">
  <header class="hero">
    <div class="tag">{kicker}</div>
    <h1>{title}</h1>
    <p>{sub}</p>
  </header>

  <nav class="toc">{toc}</nav>

  <main>
{content}
  </main>

  <footer>Ascentium Mini-Hackathon · 2026-10-13 深圳 · Facilitator Script（双语）· 人决策 + AI 执行</footer>
</div>

</body>
</html>
"""


def enhance(html):
    # facilitator-note paragraphs -> tinted dashed block
    html = re.sub(r'<p><strong>(Facilitator note[^<]*?)</strong>\s*',
                  r'<p class="facilitator-note"><span class="fn-tag">\1</span>', html)
    # standalone bold language labels -> chips above the block
    html = re.sub(r'<p><strong>(English[^<]*?)</strong></p>',
                  r'<div class="lang-label">\1</div>', html)
    html = re.sub(r'<p><strong>(\u4e2d\u6587[^<]*?)</strong></p>',
                  r'<div class="lang-label zh">\1</div>', html)
    # inline bold language labels -> chips inside the paragraph
    html = re.sub(r'<p><strong>(English[^<]*?)</strong>\s*',
                  r'<p class="lang-en"><span class="tag">\1</span> ', html)
    html = re.sub(r'<p><strong>(\u4e2d\u6587[^<]*?)</strong>\s*',
                  r'<p class="lang-zh"><span class="tag">\1</span> ', html)

    # tag each blockquote by its dominant language (for subtle framing)
    def bq(m):
        inner = m.group(1)
        cls = "zh" if CJK.search(inner) else "en"
        return '<blockquote class="%s">%s</blockquote>' % (cls, inner)

    html = re.sub(r'<blockquote>(.*?)</blockquote>', bq, html, flags=re.S)
    return html


def build(cfg):
    src = io.open(os.path.join(ROOT, cfg["md"]), encoding="utf-8").read()
    # drop the leading H1 (the hero carries the title)
    src = re.sub(r'^\s*#\s+.*?\n', '', src, count=1)

    html = markdown.markdown(
        src,
        extensions=["extra", "sane_lists", "nl2br", "toc"],
        output_format="html5",
    )
    html = enhance(html)

    # build a chip nav from the H2 sections
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html, flags=re.S)
    toc = "".join(
        '<a href="#%s">%s</a>' % (hid, re.sub(r'<[^>]+>', '', txt).strip())
        for hid, txt in heads
    )

    page = TEMPLATE.format(
        title=cfg["title"], kicker=cfg["kicker"], sub=cfg["sub"],
        toc=toc, content=html,
        accent=ACCENT, en_tint=EN_TINT, en_line=EN_LINE, en_deep=EN_DEEP,
        zh_bg=ZH_BG, zh_fg=ZH_FG, zh_line=ZH_LINE,
    )
    out = os.path.join(ROOT, cfg["out"])
    io.open(out, "w", encoding="utf-8").write(page)
    return out, len(page)


if __name__ == "__main__":
    for cfg in SCRIPTS:
        out, n = build(cfg)
        print("wrote %s (%d KB)" % (os.path.basename(out), n // 1024))
