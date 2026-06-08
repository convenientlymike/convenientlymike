#!/usr/bin/env python3
"""Make a lowlighter/metrics SVG render correctly in WebKit (iOS Safari + every
iOS in-app browser, e.g. the Instagram/Facebook webviews).

lowlighter/metrics emits:
  * a root `<svg width="W" height="H">` with NO viewBox, and
  * a `<foreignObject x="0" y="0" width="100%" height="100%">` whose HTML body
    holds the actual card.

Two WebKit problems result, both of which clip the right edge of the card on
iPhone while Chromium renders it fine (which hides the bug on desktop):

  1. No viewBox  -> WebKit won't scale an SVG-in-<img> to the element's CSS
     width; it paints at the intrinsic width and clips.
  2. foreignObject width/height="100%" -> iOS Safari fails to resolve the
     percentage against the SVG viewport, so the inner HTML lays out at its
     natural (wider-than-W) width and overflows the canvas, clipping the right
     column + calendar labels. (macOS WebKit/Quick Look resolves it, so the
     same file looks fine there — a misleading signal.)

Fix: add `viewBox="0 0 W H"` to the root, and pin the root foreignObject to the
canvas size in explicit pixels. Both are idempotent.
"""
import re
import sys


def fix_svg(path: str) -> bool:
    with open(path, encoding="utf-8") as fh:
        svg = fh.read()
    original = svg

    m = re.search(r"<svg\b[^>]*>", svg)
    if not m:
        print(f"!! no <svg> root found in {path}", file=sys.stderr)
        return False
    root = m.group(0)

    w = re.search(r'\bwidth="([\d.]+)"', root)
    h = re.search(r'\bheight="([\d.]+)"', root)
    if not (w and h):
        print(f"!! {path}: root <svg> lacks numeric width/height", file=sys.stderr)
        return False
    W, H = w.group(1), h.group(1)

    # 1) viewBox on the root svg
    if "viewBox" not in root:
        new_root = root[:-1] + f' viewBox="0 0 {W} {H}">'
        svg = svg[: m.start()] + new_root + svg[m.end():]
        print(f"++ {path}: added viewBox=\"0 0 {W} {H}\"")

    # 2) pin the FIRST foreignObject to explicit px (iOS Safari can't resolve %)
    def pin_foreign_object(s: str) -> str:
        fm = re.search(r"<foreignObject\b[^>]*>", s)
        if not fm:
            return s
        tag = fm.group(0)
        new = tag
        new = re.sub(r'\bwidth="100%"', f'width="{W}"', new)
        new = re.sub(r'\bheight="100%"', f'height="{H}"', new)
        if new != tag:
            print(f"++ {path}: pinned foreignObject to {W}x{H} (was 100%)")
            return s[: fm.start()] + new + s[fm.end():]
        return s

    svg = pin_foreign_object(svg)

    if svg == original:
        print(f"== {path}: already responsive; no change")
        return False

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(svg)
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: make_svg_responsive.py <path-to-svg>", file=sys.stderr)
        sys.exit(2)
    fix_svg(sys.argv[1])
