#!/usr/bin/env python3
"""Build the poster deliverable: three standalone style pages + one tab page.

Reads (from --dir):
  • poster-page.html  · single-poster page (content filled; keeps {{POSTER_STYLE}}
                        / {{POSTER_STYLE_UPPER}} tokens)
  • poster-tabs.html  · tab shell (content filled) with injectable slots:
                        {{PAGE_STYLE}} · {{SYMBOLS}} · {{POSTER_STACK}} · {{POSTER_STYLE_DEFAULT}}

Writes (to --out, default = --dir):
  • poster-a.html · poster-b.html · poster-c.html   clean, croppable single posters
  • poster.html                                     tab page — posters inlined (content-driven
                                                    height, so it embeds/auto-fits cleanly)

The tab page reuses the page's own <style>, <symbol> art and article markup, so the three
designs stay in sync from one content pack.
"""
import argparse
import os
import re
import sys

STYLES = ("a", "b", "c")
RE_STYLE = re.compile(r"<style>.*?</style>", re.DOTALL)
RE_SYMBOLS = re.compile(r'<svg width="0" height="0".*?</svg>', re.DOTALL)
RE_ARTICLE = re.compile(r'<article class="poster p-\{\{POSTER_STYLE\}\}".*?</article>', re.DOTALL)
RE_REMAINING = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def read(path):
    if not os.path.isfile(path):
        sys.exit(f"error: not found: {path}")
    return open(path, encoding="utf-8").read()


def main():
    ap = argparse.ArgumentParser(description="Build poster style pages + tab page")
    ap.add_argument("--dir", default=os.getcwd(), help="dir holding the filled templates")
    ap.add_argument("--out", default=None, help="output dir (default: same as --dir)")
    ap.add_argument("--default", default="a", choices=STYLES, help="default tab style")
    args = ap.parse_args()
    out = args.out or args.dir
    os.makedirs(out, exist_ok=True)

    page = read(os.path.join(args.dir, "poster-page.html"))

    # ---- three standalone style pages ----
    for style in STYLES:
        html = (page
                .replace("{{POSTER_STYLE_UPPER}}", style.upper())
                .replace("{{POSTER_STYLE}}", style))
        path = os.path.join(out, f"poster-{style}.html")
        open(path, "w", encoding="utf-8").write(html)
        left = sorted(set(RE_REMAINING.findall(html)))
        print(f"wrote {path} ({len(html):,} bytes)" + (f" · UNFILLED {left}" if left else ""))

    # ---- tab page: inject style / symbols / inlined poster stack ----
    m_style = RE_STYLE.search(page)
    m_symbols = RE_SYMBOLS.search(page)
    m_article = RE_ARTICLE.search(page)
    if not (m_style and m_symbols and m_article):
        sys.exit("error: poster-page.html is missing <style>, the art <svg>, or the <article> block")

    article_tmpl = m_article.group(0)
    stack = "\n".join(
        article_tmpl.replace("{{POSTER_STYLE}}", s) for s in STYLES
    )

    tabs = (read(os.path.join(args.dir, "poster-tabs.html"))
            .replace("{{PAGE_STYLE}}", m_style.group(0))
            .replace("{{SYMBOLS}}", m_symbols.group(0))
            .replace("{{POSTER_STACK}}", stack)
            .replace("{{POSTER_STYLE_DEFAULT}}", args.default))
    path = os.path.join(out, "poster.html")
    open(path, "w", encoding="utf-8").write(tabs)
    left = sorted(set(RE_REMAINING.findall(tabs)))
    print(f"wrote {path} ({len(tabs):,} bytes)" + (f" · UNFILLED {left}" if left else ""))


if __name__ == "__main__":
    main()
