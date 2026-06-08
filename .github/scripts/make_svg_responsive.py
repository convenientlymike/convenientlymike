#!/usr/bin/env python3
"""Make a lowlighter/metrics SVG responsive by injecting a viewBox.

lowlighter/metrics emits a root `<svg width="W" height="H">` with NO viewBox.
When such an SVG is embedded via `<img>`, WebKit (iOS Safari + every in-app
browser on iOS, e.g. the Instagram/Facebook webviews) renders it at its fixed
intrinsic width and CLIPS the overflow instead of scaling it to the element's
CSS width — so the right edge of the card gets cut off on iPhone. Chromium
scales it regardless, which masks the bug on desktop.

Adding `viewBox="0 0 W H"` (while keeping width/height) gives the SVG a scalable
coordinate system, so `<img ... width="100%">` scales correctly in ALL engines.

Idempotent: if the root already has a viewBox, the file is left unchanged.
Only the FIRST <svg> (the root) is touched; nested <svg> icons are left alone.
"""
import re
import sys


def make_responsive(path: str) -> bool:
    with open(path, encoding="utf-8") as fh:
        svg = fh.read()

    m = re.search(r"<svg\b[^>]*>", svg)
    if not m:
        print(f"!! no <svg> root found in {path}", file=sys.stderr)
        return False

    root = m.group(0)
    if "viewBox" in root:
        print(f"== {path}: root already has a viewBox; no change")
        return False

    w = re.search(r'\bwidth="([\d.]+)"', root)
    h = re.search(r'\bheight="([\d.]+)"', root)
    if not (w and h):
        print(f"!! {path}: root <svg> lacks numeric width/height; cannot derive viewBox", file=sys.stderr)
        return False

    new_root = root[:-1] + f' viewBox="0 0 {w.group(1)} {h.group(1)}">'
    svg = svg[: m.start()] + new_root + svg[m.end():]

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"++ {path}: added viewBox=\"0 0 {w.group(1)} {h.group(1)}\"")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: make_svg_responsive.py <path-to-svg>", file=sys.stderr)
        sys.exit(2)
    make_responsive(sys.argv[1])
