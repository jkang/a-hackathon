#!/usr/bin/env python3
"""Assemble a unified proposal.html from a proposal shell + the sibling artifacts.

The proposal shell (`proposal.html`) contains `{{SRCDOC_<NAME>}}` placeholders.
This script reads each artifact file in the same directory and replaces the
matching placeholder with the artifact's full HTML, escaped for an `srcdoc`
attribute. `srcdoc` iframes inherit the parent's origin, so the proposal can
auto-size each embedded artifact even when opened from file:// (double-click).

Usage:
    python3 build-proposal.py [--dir DIR] [--in SHELL] [--out OUT]

Defaults: --dir = script's cwd, --in = proposal.html, --out = proposal.html (in place).
"""
import argparse
import html
import os
import sys

# placeholder name -> artifact filename
ARTIFACTS = {
    "SRCDOC_INSIGHT": "insight-brief.html",
    "SRCDOC_PLAN": "campaign-plan.html",
    "SRCDOC_POSTER": "poster.html",
    "SRCDOC_DECK": "pitch-deck.html",
    "SRCDOC_PROMPT": "prompt-pack.html",
}


def build(directory, shell_name, out_name):
    shell_path = os.path.join(directory, shell_name)
    if not os.path.isfile(shell_path):
        sys.exit(f"error: proposal shell not found: {shell_path}")
    shell = open(shell_path, encoding="utf-8").read()

    missing = []
    for token, filename in ARTIFACTS.items():
        placeholder = "{{" + token + "}}"
        if placeholder not in shell:
            continue
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            raw = open(path, encoding="utf-8").read()
            shell = shell.replace(placeholder, html.escape(raw, quote=True))
        else:
            missing.append(filename)
            shell = shell.replace(
                placeholder,
                html.escape(
                    f"<body style='font-family:sans-serif;padding:40px'>"
                    f"Artifact not found: {filename}</body>",
                    quote=True,
                ),
            )

    out_path = os.path.join(directory, out_name)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(shell)

    print(f"wrote {out_path} ({len(shell):,} bytes)")
    if missing:
        print("missing artifacts (left as notice): " + ", ".join(missing))


def main():
    ap = argparse.ArgumentParser(description="Inline artifacts into a proposal.html")
    ap.add_argument("--dir", default=os.getcwd(), help="directory holding the shell + artifacts")
    ap.add_argument("--in", dest="shell", default="proposal.html", help="proposal shell filename")
    ap.add_argument("--out", dest="out", default="proposal.html", help="output filename")
    args = ap.parse_args()
    build(args.dir, args.shell, args.out)


if __name__ == "__main__":
    main()
