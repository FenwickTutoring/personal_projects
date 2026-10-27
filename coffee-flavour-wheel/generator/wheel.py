import math, sys, json, numpy as np
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from rdkit import Chem
from rdkit.Chem import AllChem, rdMolDescriptors

import os
HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.join(HERE, "fonts") + os.sep

# ---------------- DATA ----------------
# Molecule data: (category, [(chemical class, [(name, formula, descriptor, SMILES), ...]), ...]).
# Every entry is referenced in ../SOURCES.md; descriptors follow the cited coffee literature.
D = [
("Floral", [("Terpenoid", [("Linalool","C10H18O","floral, citrus","CC(C)=CCCC(C)(O)C=C")]),
            ("Norisoprenoid", [("β-Damascenone","C13H18O","rose, cooked apple","CC1=CC=CC(C)(C)C1C(=O)C=CC")])]),
("Fruity", [("Esters", [("Ethyl 2-methylbutanoate","C7H14O2","fruity, sweet","CCC(C)C(=O)OCC"),
                        ("Ethyl 3-methylbutanoate","C7H14O2","fruity, sweet","CC(C)CC(=O)OCC")]),
            ("Thiol", [("MMB formate","C6H12O2S","blackcurrant, catty","CC(C)(S)CCOC=O")]),
            ("Terpene", [("Limonene","C10H16","citrus; variety-dependent","CC1=CCC(CC1)C(C)=C")]),
            ("Aldehyde", [("Acetaldehyde","C2H4O","pungent, fruity","CC=O")])]),
("Sour / Fermented", [("Organic acids", [("Citric acid","C6H8O7","bright, clean sourness","OC(=O)CC(O)(CC(=O)O)C(=O)O"),
                                         ("Malic acid","C4H6O5","tart, sharp sourness","OC(=O)CC(O)C(=O)O"),
                                         ("Lactic acid","C3H6O3","soft, mild sourness","CC(O)C(=O)O"),
                                         ("Acetic acid","C2H4O2","vinegar, winey","CC(=O)O"),
                                         ("Quinic acid","C7H12O6","sour, slightly bitter","OC1CC(O)(CC(O)C1O)C(=O)O")]),
                      ("Mineral acid", [("Phosphoric acid","H3PO4","minor; experts can’t detect it","OP(=O)(O)O")]),
                      ("Fatty acids", [("Butanoic acid","C4H8O2","rancid butter","CCCC(=O)O"),
                                       ("3-Methylbutanoic acid","C5H10O2","sweaty, cheesy","CC(C)CC(=O)O")])]),
("Green / Vegetative", [("Methoxypyrazines", [("IBMP","C9H14N2O","bell pepper, peapod","COc1nccnc1CC(C)C"),
                                              ("IPMP","C8H12N2O","potato defect, earthy pea","COc1nccnc1C(C)C"),
                                              ("2-Methoxy-3,5-dimethylpyrazine","C7H10N2O","earthy, musty (raw bean)","COc1ncc(C)nc1C")]),
                        ("Lipid oxidation", [("Hexanal","C6H12O","green, grassy","CCCCCC=O")])]),
("Defects & Staling", [("Lipid oxidation", [("(E)-2-Nonenal","C9H16O","fatty, papery","CCCCCC/C=C/C=O")]),
                       ("Microbial", [("TCA","C7H5Cl3O","Rio defect: musty, iodine","COc1c(Cl)cc(Cl)cc1Cl"),
                                      ("Geosmin","C12H22O","earthy, mouldy","CC12CCCC(C)C1(O)CCCC2")])]),
("Bitter & Mouthfeel", [("Alkaloids", [("Caffeine","C8H10N4O2","pure bitter; ~10–15% of it","Cn1cnc2c1c(=O)n(C)c(=O)n2C"),
                                       ("Trigonelline","C7H7NO2","bitter; partly roasts to niacin","C[n+]1cccc(c1)C(=O)[O-]"),
                                       ("N-Methylpyridinium","C6H8N+","odourless dark-roast marker","C[n+]1ccccc1")]),
                        ("Chlorogenic acids", [("Chlorogenic acid","C16H18O9","astringent, mouthcoating","OC(=O)C1(O)CC(O)C(O)C(OC(=O)C=Cc2ccc(O)c(O)c2)C1"),
                                               ("Chlorogenic lactones","C16H16O8","coffee-typical bitter","O=C1OC2CC1(O)CC(OC(=O)C=Cc3ccc(O)c(O)c3)C2O")])]),
("Oil & Gas", [("Diterpene", [("Cafestol","C20H28O3","coffee oil; filters remove it","OCC1(O)CC23CCC4c5ccoc5CCC4(C)C2CCC1C3")]),
               ("Gas", [("Carbon dioxide","CO2","bloom, crema","O=C=O")])]),
("Roasted", [("Sulfur compounds", [("2-Furfurylthiol","C5H6OS","roasty, coffee-like","SCc1ccco1"),
                                   ("Methanethiol","CH4S","sulfurous; fresh-roast marker","CS"),
                                   ("Prenylthiol","C5H10S","skunky, foxy","CC(C)=CCS"),
                                   ("Methional","C4H8OS","cooked potato","CSCCC=O")]),
             ("Pyrazines", [("2-Ethyl-3,5-dimethylpyrazine","C8H12N2","earthy, roasty","CCc1nc(C)cnc1C"),
                            ("2,3-Diethyl-5-methylpyrazine","C9H14N2","earthy, roasty","CCc1ncc(C)nc1CC")]),
             ("Phenol", [("Guaiacol","C7H8O2","phenolic, smoky, spicy","COc1ccccc1O")])]),
("Spices", [("Phenols", [("4-Vinylguaiacol","C9H10O2","clove, spicy","COc1cc(C=C)ccc1O"),
                         ("4-Ethylguaiacol","C9H12O2","spicy, smoky; more in Robusta","CCc1ccc(O)c(OC)c1")])]),
("Nutty / Cocoa", [("Pyrazine", [("2,5-Dimethylpyrazine","C6H8N2","nutty, roasted peanut","Cc1cnc(C)cn1")]),
                   ("Strecker aldehydes", [("3-Methylbutanal","C5H10O","malty","CC(C)CC=O"),
                                           ("2-Methylbutanal","C5H10O","malty, cocoa-like","CCC(C)C=O")])]),
("Sweet", [("Diketones", [("Diacetyl","C4H6O2","buttery","CC(=O)C(C)=O"),
                          ("2,3-Pentanedione","C5H8O2","buttery, creamy","CCC(=O)C(C)=O")]),
           ("Furanones", [("Furaneol","C6H8O3","caramel-like","CC1OC(C)=C(O)C1=O"),
                          ("Sotolon","C6H8O3","seasoning, maple syrup","CC1OC(=O)C(O)=C1C"),
                          ("Abhexon","C7H10O3","seasoning, caramel","CCC1OC(=O)C(O)=C1C")]),
           ("Pyranone", [("Maltol","C6H6O3","caramel, sweet","Cc1occc(=O)c1O")]),
           ("Phenolic aldehyde", [("Vanillin","C8H8O3","vanilla","COc1cc(C=O)ccc1O")]),
           ("Strecker aldehyde", [("Phenylacetaldehyde","C8H8O","honey, floral","O=CCc1ccccc1")])]),
]
ITEMS = [it for _, gs in D for _, cs in gs for it in cs]
N = len(ITEMS)

def check():
    bad = []
    for cn, f, od, smi in ITEMS:
        m = Chem.MolFromSmiles(smi)
        ff = rdMolDescriptors.CalcMolFormula(m)
        if ff != f: bad.append((cn, f, ff))
    return bad

# ---------------- FONTS ----------------
def load_static(fam, w):
    """Load FD/<fam>-<w>.ttf if present, else instance it from the variable FD/<fam>.ttf."""
    p = f"{FD}{fam}-{w}.ttf"
    if os.path.exists(p): return TTFont(p)
    from fontTools.varLib import instancer
    vf = TTFont(f"{FD}{fam}.ttf")
    if "fvar" not in vf: return vf
    axes = {a.axisTag: a for a in vf["fvar"].axes}
    loc = {t: a.defaultValue for t, a in axes.items()}
    if "wght" in axes: loc["wght"] = max(axes["wght"].minValue, min(w, axes["wght"].maxValue))
    inst = instancer.instantiateVariableFont(vf, loc)
    inst.save(p)
    return TTFont(p)

class Font:
    cache = {}
    def __init__(self, fam, w):
        self.key = f"{fam}{w}"
        self.tt = load_static(fam, w)
        self.cmap = self.tt.getBestCmap(); self.gs = self.tt.getGlyphSet()
        self.upm = self.tt["head"].unitsPerEm; self.hmtx = self.tt["hmtx"]
        self.fb = None
    @classmethod
    def get(cls, fam, w):
        k = (fam, w)
        if k not in cls.cache:
            f = Font(fam, w)
            fbfam = os.environ.get("WHEEL_FALLBACK_FONT")
            if fbfam and fbfam != fam: f.fb = Font.get(fbfam, w)
            cls.cache[k] = f
        return cls.cache[k]

class SVG:
    def __init__(self, live=False):
        self.defs = {}; self.body = []; self.live = live
    def glyph(self, font, ch):
        f = font
        if ord(ch) not in f.cmap and f.fb: f = f.fb
        gn = f.cmap.get(ord(ch))
        if gn is None: return None, 0, f
        gid = f"{f.key}_{ord(ch)}"
        if gid not in self.defs:
            pen = SVGPathPen(f.gs); f.gs[gn].draw(pen)
            self.defs[gid] = pen.getCommands()
        return gid, f.hmtx[gn][0], f

    def runs(self, s, formula=False):
        out = []
        prev = ""
        for ch in s:
            if ch in "⁺⁻": out.append(("+" if ch == "⁺" else "−", "sup"))
            elif formula and ch.isdigit(): out.append((ch, "sub"))
            else: out.append((ch, "n"))
        return out

    def width(self, s, font, size, formula=False):
        w = 0
        for ch, k in self.runs(s, formula):
            gid, adv, f = self.glyph(font, ch)
            sz = size * (0.68 if k != "n" else 1)
            w += adv * sz / f.upm
        return w

    def text(self, s, x, y, size, font, fill, anchor="start", formula=False, track=0):
        """y is the vertical centre of x-height-ish (we place baseline at y+0.36*size)"""
        w = self.width(s, font, size, formula) + track * (len(s) - 1)
        if self.live:
            import html, re
            fam = re.sub(r"\d+$", "", font.key); wt = re.search(r"(\d+)$", font.key).group(1)
            t = s.translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")) if formula else s
            fam_css = {"JetBrainsMono": "JetBrains Mono", "IBMPlexSans": "IBM Plex Sans", "SpaceGrotesk": "Space Grotesk", "DMSans": "DM Sans", "InstrumentSans": "Instrument Sans"}.get(fam, fam)
            ls = f' letter-spacing="{track}"' if track else ""
            return (f'<text x="{x:.1f}" y="{y + 0.36*size:.1f}" font-family="{fam_css}, sans-serif" font-size="{size}" '
                    f'font-weight="{wt}" fill="{fill}" text-anchor="{anchor}"{ls}>{html.escape(t, quote=False)}</text>'), w
        if anchor == "middle": x -= w / 2
        elif anchor == "end": x -= w
        base = y + 0.36 * size
        parts = []
        for ch, k in self.runs(s, formula):
            gid, adv, f = self.glyph(font, ch)
            sz = size * (0.68 if k != "n" else 1)
            dy = 0.22 * size if k == "sub" else (-0.42 * size if k == "sup" else 0)
            if gid and self.defs[gid]:
                sc = sz / f.upm
                parts.append(f'<use href="#{gid}" transform="translate({x:.1f} {base+dy:.1f}) scale({sc:.5f} {-sc:.5f})"/>')
            x += adv * sz / f.upm + track
        return f'<g fill="{fill}">' + "".join(parts) + "</g>", w

# ---------------- COLOUR ----------------
def hx(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def mix(a, b, t):
    A, B = hx(a), hx(b); return "#%02x%02x%02x" % tuple(round(A[i] + (B[i]-A[i])*t) for i in range(3))
def lum(h):
    def c(v):
        v /= 255; return v/12.92 if v <= 0.03928 else ((v+0.055)/1.055)**2.4
    r, g, b = hx(h); return 0.2126*c(r) + 0.7152*c(g) + 0.0722*c(b)
def readable(h, target=4.6):
    t = 0.0
    c = h
    while (1.05/(lum(c)+0.05)) < target and t < 1:
        t += 0.05; c = mix(h, "#000000", t)
    return c
def on(h, dark="#111111"):
    L = lum(h); cw = 1.05/(L+0.05); cd = (L+0.05)/(lum(dark)+0.05)
    return "#ffffff" if cw >= cd else dark

# ---------------- BUILD ----------------
def build(v, live=False):
    svg = SVG(live)
    F = lambda w: Font.get(v["font"], w)
    FM = lambda w: Font.get(v.get("fmono", v["font"]), w)
    ink = v.get("ink", "#111111"); sub = v.get("sub", "#5b5b5b")
    pal = v["pal"]; mode = v["mode"]; bg = "#ffffff"
    hair = v.get("hair", "#e6e6e6")
    R0, R1, R2, R3 = v.get("radii", (96, 196, 316, 392))
    gapL = 12; RL = R3 + gapL
    step = 360 / N
    C = 2000  # temp centre; recentred later
    def P(r, a): a = math.radians(a); return (C + r*math.sin(a), C - r*math.cos(a))
    def pp(r, a): x, y = P(r, a); return f"{x:.1f} {y:.1f}"
    def sec(r0, r1, a0, a1, fill, stroke=None, sw=0):
        L = 1 if a1 - a0 > 180 else 0
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        return f'<path d="M{pp(r1,a0)}A{r1} {r1} 0 {L} 1 {pp(r1,a1)}L{pp(r0,a1)}A{r0} {r0} 0 {L} 0 {pp(r0,a0)}Z" fill="{fill}"{st}/>'
    S = []; T = []; mols = []; a = 0.0
    sw = v.get("gap", 2.0)
    for ci, (name, groups) in enumerate(D):
        col = pal[ci]
        catcol = col
        if mode == "solid":
            cfill, clfill, ffill = col, mix(col, "#ffffff", v.get("tint", 0.62)), col
        elif mode == "tint":
            cfill, clfill, ffill = mix(col, "#ffffff", 0.0), mix(col, "#ffffff", 0.55), mix(col, "#ffffff", 0.78)
        elif mode == "soft":
            cfill, clfill, ffill = mix(col, "#ffffff", 0.15), mix(col, "#ffffff", 0.6), mix(col, "#ffffff", 0.82)
        elif mode == "line":
            cfill = clfill = ffill = "#ffffff"
        elif mode == "band":   # only category ring coloured
            cfill, clfill, ffill = col, "#ffffff", "#ffffff"
        ca = a
        for cls, cs in groups:
            ga = a
            for cn, f, od, smi in cs:
                S.append(sec(R2, R3, a, a+step, ffill, *(("#ffffff", sw) if mode not in ("line",) else (hair, 1))))
                m = a + step/2
                if m < 180: rot = m - 90; s = 1; anc = "start"
                else: rot = m + 90; s = -1; anc = "end"
                fx = C + s*(R2+R3)/2; lx = C + s*RL
                fcol = on(ffill, ink) if mode not in ("line",) else v.get("fcol", sub)
                g1, _ = svg.text(f.replace("+", "⁺"), fx, C, v.get("fs", 12.5), FM(600), fcol, "middle", formula=True)
                ncol = v.get("ncol", ink)
                if v.get("ncat"): ncol = readable(col)
                g2, w2 = svg.text(cn, lx, C-7.5, 13.5, F(600), ncol, anc)
                g3, w3 = svg.text(od, lx, C+9, 11, F(400), sub, anc)
                T.append(f'<g transform="rotate({rot:.3f} {C} {C})">{g1}{g2}{g3}</g>')
                mols.append((m, smi, cn, ci, max(w2, w3)))
                a += step
            S.append(sec(R1, R2, ga, a, clfill, *(("#ffffff", sw) if mode != "line" else (hair, 1))))
            m = (ga+a)/2
            rot = m-90 if m < 180 else m+90; x = C + (1 if m < 180 else -1)*(R1+R2)/2
            ccol = on(clfill, ink) if mode != "line" else ink
            g, _ = svg.text(cls, x, C, 11.5, F(600), ccol, "middle")
            T.append(f'<g transform="rotate({rot:.3f} {C} {C})">{g}</g>')
        S.append(sec(R0, R1, ca, a, cfill, *(("#ffffff", sw) if mode != "line" else (hair, 1))))
        m = (ca+a)/2; r = (R0+R1)/2
        if 90 < m < 270: rot = m+180; y0 = r
        else: rot = m; y0 = -r
        ls = name.replace(" / ", " /|").replace(" & ", " &|").split("|")
        kcol = on(cfill, ink) if mode != "line" else catcol
        if v.get("kcolor") and mode == "line": kcol = v["kcolor"]
        kc = v.get("kcase", lambda z: z)
        wmax = max(svg.width(kc(l), F(700), 14.5) + v.get("ktrack", 0)*len(l) for l in ls)
        arcw = r * math.radians(a - ca)
        parts = []
        if wmax > arcw * 0.86:   # too narrow: set the label radially
            rot = m-90 if m < 180 else m+90; x = C + (1 if m < 180 else -1)*r
            if len(ls) > 1 and svg.width(kc(name), F(700), 14.5) < (R1-R0)*0.92 and False: ls = [name]
            for i, l in enumerate(ls):
                g, _ = svg.text(kc(l), x, C+(i-(len(ls)-1)/2)*16, 14 if len(ls) > 1 else 14.5, F(700), kcol, "middle", track=v.get("ktrack", 0))
                parts.append(g)
        else:
            for i, l in enumerate(ls):
                g, _ = svg.text(kc(l), C, C+y0+(i-(len(ls)-1)/2)*17, 14.5, F(700), kcol, "middle", track=v.get("ktrack", 0))
                parts.append(g)
        T.append(f'<g transform="rotate({rot:.3f} {C} {C})">' + "".join(parts) + "</g>")
        if mode == "line":   # coloured tick arc at outer edge of category ring
            S.append(sec(R1-5, R1, ca, a, catcol))
    # center
    cen = []
    cen.append(f'<circle cx="{C}" cy="{C}" r="{R0-6}" fill="{v.get("cfill", "#ffffff")}"/>')
    cc = v.get("ctext", ink)
    for txt, y, sz, w, fm in [("Roasted", -14, 20, 700, False), ("coffee", 10, 20, 700, False)]:
        g, _ = svg.text(txt, C, C+y, sz, F(w), cc, "middle"); cen.append(g)
    g, _ = svg.text("1000+ volatiles", C, C+36, 11, FM(500), sub if v.get("cfill", "#fff") == "#ffffff" else cc, "middle"); cen.append(g)

    # ---- structures
    out = []; maxr = R3 + 260
    scol_mode = v.get("scol", "mono"); smono = v.get("smono", ink)
    rays = v.get("rays", "fixed")
    maxlab = max(w for *_, w in mols)
    ws = sorted(w for *_, w in mols); RSfix = RL + ws[int(len(ws)*0.8)] + 18
    bw = v.get("bw", 1.4)
    for ang, smi, cn, ci, w in mols:
        RS = max(RSfix, RL + w + 16) if rays == "fixed" else RL + w + 16
        if scol_mode == "cat":
            sc_ = readable(pal[ci], 3.2)
        else: sc_ = smono
        m = Chem.MolFromSmiles(smi); Chem.Kekulize(m, clearAromaticFlags=True)
        AllChem.Compute2DCoords(m)
        xy = np.array([[m.GetConformer().GetAtomPosition(i).x, -m.GetConformer().GetAtomPosition(i).y] for i in range(m.GetNumAtoms())])
        if len(xy) > 1:
            c0 = xy.mean(0); _, _, vt = np.linalg.svd(xy-c0); ax = vt[0]
        else: c0 = xy[0]; ax = np.array([1.0, 0])
        rad = math.radians(ang); dirv = np.array([math.sin(rad), -math.cos(rad)]); tan = np.array([math.cos(rad), math.sin(rad)])
        perp = np.array([-ax[1], ax[0]])
        loc = np.stack([(xy-c0)@ax, (xy-c0)@perp], 1)
        L = max(np.ptp(loc[:, 0]), 0.01); Wd = max(np.ptp(loc[:, 1]), 0.01)
        arc = RS * math.radians(step) * 0.92
        sc = min(14, 118/L, max(arc, 40)/Wd)
        loc = loc*sc; loc[:, 0] -= loc[:, 0].min()
        pts = np.array([P(RS, ang)]) + loc[:, 0:1]*dirv + loc[:, 1:2]*tan + 10*dirv
        labels = {}
        for at in m.GetAtoms():
            sym = at.GetSymbol(); h = at.GetTotalNumHs(); ch = at.GetFormalCharge()
            if sym != "C" or smi == "O=C=O":
                t = sym + ("H" if h == 1 else (f"H{h}" if h > 1 else ""))
                if ch > 0: t += "⁺"
                if ch < 0: t += "⁻"
                labels[at.GetIdx()] = t
        for b in m.GetBonds():
            i, j = b.GetBeginAtomIdx(), b.GetEndAtomIdx()
            A, B = pts[i].copy(), pts[j].copy(); vv = B-A; d = np.linalg.norm(vv); vv /= d
            if i in labels: A = A + vv*(6.5 if len(labels[i]) < 3 else 11)
            if j in labels: B = B - vv*(6.5 if len(labels[j]) < 3 else 11)
            nrm = np.array([-vv[1], vv[0]])
            bt = b.GetBondTypeAsDouble()
            def line(p, q):
                out.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{sc_}" stroke-width="{bw}" stroke-linecap="round"/>')
            if bt == 2:
                if b.IsInRing():
                    rr = [r for r in m.GetRingInfo().AtomRings() if i in r and j in r][0]
                    cen_ = pts[list(rr)].mean(0); side = 1 if np.dot(cen_-(A+B)/2, nrm) > 0 else -1
                    line(A, B); off = nrm*side*3.5; sh = vv*2.6; line(A+off+sh, B+off-sh)
                else:
                    line(A+nrm*1.8, B+nrm*1.8); line(A-nrm*1.8, B-nrm*1.8)
            elif bt == 3:
                line(A, B); line(A+nrm*3, B+nrm*3); line(A-nrm*3, B-nrm*3)
            else: line(A, B)
            maxr = max(maxr, np.hypot(*(A-C)), np.hypot(*(B-C)))
        for i, t in labels.items():
            x, y = pts[i]
            g, w_ = svg.text(t, x, y, 11, F(700), sc_, "middle", formula=True)
            out.append(g); maxr = max(maxr, np.hypot(x-C, y-C)+12)
    R = int(maxr + 14)
    vb = f"{C-R} {C-R} {2*R} {2*R}"
    defs = "".join(f'<path id="{k}" d="{d}"/>' for k, d in svg.defs.items() if d)
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{2*R}" height="{2*R}">'
         f'<defs>{defs}</defs>' + "".join(S) + "".join(cen) + "".join(T) + "".join(out) + "</svg>")
    return s, 2*R

if __name__ == "__main__":
    bad = check()
    print("Formula check:", "all match" if all(b[0] == "Phosphoric acid" for b in bad) else bad)
