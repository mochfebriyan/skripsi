"""Validator struktur file .drawio (tanpa perlu membuka draw.io).

Pemakaian:
    python3 -I projek-fiklab/tools/drawio/validate.py <file.drawio> [prefiks_id]

Yang diperiksa per halaman (diagram):
  1. edge yang source/target-nya tidak ada (garis putus);
  2. ID ganda;
  3. ID yang tidak diawali prefiks modul (bila prefiks_id diberikan, mis. "sdm-");
  4. kotak yang saling bertumpuk: kelas (swimlane stackLayout), elips use case,
     catatan, dan state, di tingkat teratas (parent="1"). Lajur (swimlane tanpa
     stackLayout), bingkai, batas sistem, dan fragmen tidak dihitung.

Keluar dengan kode 1 bila ada masalah.
"""
import sys
import xml.dom.minidom as minidom


def boxes(cells):
    out = {}
    for c in cells:
        st = c.getAttribute("style")
        if c.getAttribute("vertex") != "1" or c.getAttribute("parent") != "1":
            continue
        is_class = "swimlane" in st and "stackLayout" in st
        is_other = any(k in st for k in ("ellipse;whiteSpace", "shape=note", "rounded=1;arcSize=30", "rounded=1;arcSize=40", "rhombus"))
        if not (is_class or is_other):
            continue
        g = c.getElementsByTagName("mxGeometry")[0]
        out[c.getAttribute("id")] = [float(g.getAttribute(k) or 0) for k in ("x", "y", "width", "height")]
    return out


def overlap(a, b):
    return not (a[0] + a[2] <= b[0] or b[0] + b[2] <= a[0] or a[1] + a[3] <= b[1] or b[1] + b[3] <= a[1])


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path, prefix = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)
    doc = minidom.parse(path)
    bad_total = 0
    for dg in doc.getElementsByTagName("diagram"):
        cells = dg.getElementsByTagName("mxCell")
        ids = [c.getAttribute("id") for c in cells]
        idset = set(ids)
        broken = [c.getAttribute("id") for c in cells if c.getAttribute("edge") == "1"
                  and (c.getAttribute("source") not in idset or c.getAttribute("target") not in idset)]
        dup = sorted({i for i in ids if ids.count(i) > 1})
        wrong = [i for i in ids if prefix and i not in ("0", "1") and not i.startswith(prefix)]
        b = boxes(cells)
        keys = list(b)
        ov = [(x, y) for i, x in enumerate(keys) for y in keys[i + 1:] if overlap(b[x], b[y])]
        n_edge = sum(1 for c in cells if c.getAttribute("edge") == "1")
        problems = len(broken) + len(dup) + len(wrong) + len(ov)
        bad_total += problems
        status = "OK" if problems == 0 else "MASALAH"
        print(f"[{status}] {dg.getAttribute('name')}: {len(cells)} sel, {n_edge} garis")
        for label, items in (("garis putus", broken), ("ID ganda", dup), ("ID tanpa prefiks", wrong[:10]), ("bertumpuk", ov[:10])):
            if items:
                print(f"    {label}: {items}")
    sys.exit(1 if bad_total else 0)


if __name__ == "__main__":
    main()
