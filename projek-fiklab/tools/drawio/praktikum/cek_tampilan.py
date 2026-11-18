"""Cek kasar tampilan .drawio: garis yang menembus kotak selain sumber/tujuannya.
Garis dihitung sebagai polyline: titik keluar sumber -> titik belok -> titik masuk tujuan.
Garis ortogonal tanpa titik belok didekati dengan siku (horizontal dulu, lalu vertikal, dan sebaliknya;
dilaporkan hanya bila KEDUA kemungkinan menembus kotak)."""
import sys, re
import xml.dom.minidom as minidom


def style_val(st, k):
    m = re.search(r'(?:^|;)' + k + r'=([^;]+)', st)
    return float(m.group(1)) if m else None


def seg_hits(p, q, r, pad=4):
    x0, y0, w, h = r
    x0 += pad; y0 += pad; x1 = x0 + w - 2 * pad; y1 = y0 + h - 2 * pad
    if x1 <= x0 or y1 <= y0:
        return False
    (ax, ay), (bx, by) = p, q
    # Liang-Barsky
    dx, dy = bx - ax, by - ay
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, ax - x0), (dx, x1 - ax), (-dy, ay - y0), (dy, y1 - ay)):
        if pp == 0:
            if qq < 0:
                return False
        else:
            t = qq / pp
            if pp < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
            if t0 > t1:
                return False
    return True


def main(path):
    doc = minidom.parse(path)
    total = 0
    for dg in doc.getElementsByTagName("diagram"):
        cells = dg.getElementsByTagName("mxCell")
        box, label = {}, {}
        for c in cells:
            if c.getAttribute("vertex") != "1":
                continue
            st = c.getAttribute("style")
            if any(k in st for k in ("swimlane", "shape=folder", "verticalAlign=top;fontStyle=1;fontSize=15",
                                     "verticalAlign=top;fontStyle=1;fontSize=14", "text;html=1", "wadah=1",
                                     "shape=umlFrame", "shape=umlLifeline")):
                # lajur, paket, batas sistem (gaya lama fontSize=15, gaya polos fontSize=14), judul, wadah,
                # fragmen opt/ref, dan lifeline SSD (pesan memang melintasinya): boleh dilewati
                continue
            g = c.getElementsByTagName("mxGeometry")[0]
            box[c.getAttribute("id")] = tuple(float(g.getAttribute(k) or 0) for k in ("x", "y", "width", "height"))
            label[c.getAttribute("id")] = re.sub("<[^>]+>", " ", c.getAttribute("value"))[:40]
        hits = []
        for c in cells:
            if c.getAttribute("edge") != "1":
                continue
            s, t, st = c.getAttribute("source"), c.getAttribute("target"), c.getAttribute("style")
            if s not in box or t not in box:
                continue
            S, T = box[s], box[t]
            ex, ey = style_val(st, "exitX"), style_val(st, "exitY")
            nx, ny = style_val(st, "entryX"), style_val(st, "entryY")
            p0 = (S[0] + S[2] * (ex if ex is not None else 0.5), S[1] + S[3] * (ey if ey is not None else 0.5))
            p1 = (T[0] + T[2] * (nx if nx is not None else 0.5), T[1] + T[3] * (ny if ny is not None else 0.5))
            pts = [(float(m.getAttribute("x")), float(m.getAttribute("y"))) for m in c.getElementsByTagName("mxPoint")]
            ortho = "orthogonalEdgeStyle" in st
            variants = []
            if pts or not ortho:
                variants.append([p0] + pts + [p1])
            else:
                variants.append([p0, (p1[0], p0[1]), p1])
                variants.append([p0, (p0[0], p1[1]), p1])
            bad_all = None
            for poly in variants:
                bad = set()
                for a, b in zip(poly, poly[1:]):
                    for k, r in box.items():
                        if k in (s, t):
                            continue
                        if seg_hits(a, b, r):
                            bad.add(k)
                bad_all = bad if bad_all is None else (bad_all & bad)
            for k in sorted(bad_all or []):
                hits.append((c.getAttribute("id"), label.get(s, s)[:22], label.get(t, t)[:22], label[k][:30]))
        total += len(hits)
        print(f"[{'OK' if not hits else 'CEK'}] {dg.getAttribute('name')}: {len(hits)} garis menembus kotak lain")
        for h in hits:
            print("     ", h)
    return total


if __name__ == "__main__":
    n = sum(main(p) for p in sys.argv[1:])
    sys.exit(1 if n else 0)
