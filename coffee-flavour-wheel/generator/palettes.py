"""Colour presets for the wheel. Every preset uses the poster font (Manrope by default).

Category order for `pal` (11 colours, clockwise from the top):
    Floral, Fruity, Sour/Fermented, Green/Vegetative, Defects & Staling,
    Bitter, Body, Roasted, Spices, Nutty/Cocoa, Sweet

Keys:
    mode   "soft" (pale tints), "tint", "solid" (strong fills), "band" (only the inner ring coloured), "line" (outlines only)
    scol   "cat" colours each structure by its category; otherwise structures use `smono`
    rays   "hug" starts each structure right after its own label (sun shape); "fixed" lines them up on a ring
"""

PRESETS = {
"ink": dict(mode="solid", tint=0.86,
    pal=["#1a1a1a","#3d3d3d","#1a1a1a","#3d3d3d","#1a1a1a","#3d3d3d","#1a1a1a","#3d3d3d","#1a1a1a","#3d3d3d","#5a5a5a"]),
"crema": dict(mode="solid", tint=0.66, ink="#24170f", sub="#6e5a4b", smono="#24170f",
    pal=["#c9a98c","#a8714f","#d8bf9a","#7d6a4f","#9a8b7c","#4a3226","#6b4a36","#24170f","#8c4f2f","#5a3a28","#b8865a"]),
"nordic-ring": dict(mode="soft", scol="cat",
    pal=["#e8a6b8","#f19a7c","#f4cf6b","#8fc49a","#b8b2a7","#8b8fa8","#a98d7a","#6f6a66","#d08a5e","#a77a6a","#e9b872"]),
"nordic": dict(mode="soft", scol="cat", rays="hug",
    pal=["#e8a6b8","#f19a7c","#f4cf6b","#8fc49a","#b8b2a7","#8b8fa8","#a98d7a","#6f6a66","#d08a5e","#a77a6a","#e9b872"]),
"signal": dict(mode="line", kcolor="#ff4f1a", ncol="#111111", fcol="#ff4f1a", hair="#dedede",
    pal=["#ff4f1a"]*11, smono="#111111", kcase=str.upper, ktrack=0.6),
"lab": dict(mode="line", ink="#1a2fb0", sub="#5662a8", ncol="#1a2fb0", fcol="#1a2fb0", hair="#d6dbf3",
    pal=["#1a2fb0"]*11, kcolor="#1a2fb0", smono="#1a2fb0", bw=1.2),
"riso": dict(mode="solid", tint=0.7, scol="cat",
    pal=["#ff48b0","#ff6c2f","#ffd400","#00a95c","#9a9a9a","#3255a4","#765ba7","#1a1a1a","#e3363e","#a5554e","#ffb511"]),
"fenwick": dict(mode="solid", tint=0.6, ink="#1a1a1a", smono="#5d2137",
    pal=["#d4b5ae","#ba684e","#8999ab","#3d6b47","#c9bcb5","#a2b082","#6e4a3a","#1a1a1a","#8a4530","#5d2137","#d4a835"]),
"swiss": dict(mode="band", ink="#111111", smono="#111111", gap=1.5,
    pal=["#e30613","#111111","#e30613","#111111","#8a8a8a","#111111","#8a8a8a","#111111","#e30613","#111111","#e30613"]),
"origin": dict(mode="solid", tint=0.62, scol="cat", ink="#1f1a17",
    pal=["#d9a6a0","#c4603f","#e0b84f","#7f9467","#a99d8c","#5e5a54","#8a6650","#2f2a26","#a5532f","#6d4537","#cf9a52"]),
"electric": dict(mode="solid", tint=0.72, rays="hug",
    pal=["#ff7ad9","#ff5b3a","#ffe14d","#b6f03c","#c7c7c7","#7b61ff","#9d6b53","#111111","#ff9f1c","#2f5bff","#ffc21a"]),
"blueprint": dict(mode="tint", ink="#0b2545", sub="#4a5f7a", smono="#0b2545", rays="hug",
    pal=["#8da9c4","#13315c","#8da9c4","#13315c","#b7c4d3","#0b2545","#5b7899","#0b2545","#13315c","#5b7899","#8da9c4"]),
"tonal": dict(mode="soft", scol="cat", rays="hug", ncat=True,
    pal=["#b5838d","#c06c4c","#c9a23f","#6c8c5a","#8d8a84","#5d6d7e","#7a5c4f","#3a3633","#a0563a","#7d4b3e","#b98a3c"]),
}
