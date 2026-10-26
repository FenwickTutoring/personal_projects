"""
Build the "Coffee, molecularly." poster.

    pip install -r requirements.txt
    python make_poster.py            # Nordic palette (default)
    python make_poster.py riso       # any preset name from palettes.py

Outputs (written to the folder above this one):
    index.html                 editable poster, real text, opens in any browser, print to any size
    coffee-flavour-wheel.svg   print-shop file, text converted to outlines (no fonts needed)
    coffee-flavour-wheel.pdf   vector PDF, 50 x 50 cm (scales to any size without losing quality)
    preview.png                small preview image

To change the molecules, descriptors or categories, edit the D list in wheel.py.
To change the corner text, edit POSTER below.
"""
import os, re, sys, html
import cairosvg
from wheel import build, SVG, Font
from palettes import PRESETS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SIZE = 1800          # poster is square, in px units
WHEEL = (80, 80, 1640)   # x, y, width of the wheel inside the poster
FONT = "Manrope"

# Corner text. Each entry: (x, y_first_baseline_centre, size, weight, colour, anchor, line_height, [lines])
POSTER = [
    (64, 92, 50, 800, "#1c1c1c", "start", 50, ["Coffee,", "molecularly."]),
    (64, 196, 14, 500, "#777777", "start", 20, ["56 key odorants & tastants"]),
    (1736, 74, 14, 400, "#444444", "end", 21.7, ["Read from the centre: the sensory",
                                                  "category a taster names, the chemical",
                                                  "class behind it, the formula, the",
                                                  "compound and its skeletal structure."]),
    (64, 1712, 12.5, 400, "#777777", "start", 19.4, ["Learn the chemical names of the coffee",
                                                      "flavours so you can sound fancy"]),
    (1736, 1730, 14, 700, "#1c1c1c", "end", 20, ["fenwicktutoring.com"]),
]


def nest(wheel_svg):
    """Turn the wheel's root <svg> into a nested <svg> placed inside the poster."""
    x, y, w = WHEEL
    vb = re.search(r'viewBox="([^"]+)"', wheel_svg).group(1)
    body = wheel_svg[wheel_svg.index(">") + 1: wheel_svg.rindex("</svg>")]
    return f'<svg x="{x}" y="{y}" width="{w}" height="{w}" viewBox="{vb}">{body}</svg>'


def corner_text(live, existing_ids=""):
    svg = SVG(live)
    parts = []
    for x, y, size, weight, col, anchor, lh, lines in POSTER:
        for i, line in enumerate(lines):
            g, _ = svg.text(line, x, y + i * lh, size, Font.get(FONT, weight), col, anchor)
            parts.append(g)
    defs = "".join(f'<path id="{k}" d="{d}"/>' for k, d in svg.defs.items() if d and f'id="{k}"' not in existing_ids)
    return defs, "".join(parts)


def poster_svg(v, live):
    wheel, _ = build(v, live=live)
    wheel = nest(wheel)
    defs, text = corner_text(live, wheel)
    defs = f"<defs>{defs}</defs>" if defs else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" width="{SIZE}" height="{SIZE}">'
            f'{defs}<rect width="{SIZE}" height="{SIZE}" fill="#ffffff"/>{wheel}{text}</svg>')


HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coffee, molecularly. A flavour chemistry wheel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<!--
  Coffee, molecularly. A flavour chemistry wheel.
  To print: open in a browser > Print > choose any paper size, set margins to None,
  enable "Background graphics", or Save as PDF. Everything is vector, so it stays sharp at any size.
  To edit: every label is a plain <text> element below. Search for the word you want to change.
  To regenerate with different molecules or colours, see generator/README in the repository.
  Licence: CC BY 4.0. Credit "James Fenwick, fenwicktutoring.com".
-->
<style>
  html, body { margin: 0; height: 100%; background: #ffffff; }
  body { display: flex; align-items: center; justify-content: center; }
  svg { display: block; width: min(100vw, 100vh); height: auto; }
  @page { margin: 0; }
  @media print { html, body { height: auto; } svg { width: 100%; height: auto; } }
</style>
</head>
<body>
__SVG__
</body>
</html>
"""


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "nordic"
    v = dict(PRESETS[name]); v["font"] = FONT
    live = poster_svg(v, live=True)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(HTML.replace("__SVG__", live))
    outlined = poster_svg(v, live=False)
    open(os.path.join(ROOT, "coffee-flavour-wheel.svg"), "w", encoding="utf-8").write(outlined)
    # 50 cm square at 72 pt/inch: 500 mm = 1417.32 pt
    cairosvg.svg2pdf(bytestring=outlined.encode(), write_to=os.path.join(ROOT, "coffee-flavour-wheel.pdf"),
                     output_width=1417.32, output_height=1417.32)
    cairosvg.svg2png(bytestring=outlined.encode(), write_to=os.path.join(ROOT, "preview.png"), output_width=1200)
    print("Wrote index.html, coffee-flavour-wheel.svg, coffee-flavour-wheel.pdf, preview.png")


if __name__ == "__main__":
    main()
