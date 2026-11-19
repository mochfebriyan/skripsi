"""Alur metode perancangan (Gambar 2.3 naskah Bab II), activity diagram 1 halaman + catatan.

Pemakaian: python3 -I metode.py projek-fiklab/rancangan/metode-perancangan-tata-kelola.drawio
"""
import sys
from xml.sax.saxutils import escape
OUT = sys.argv[1]
def esc(s): return escape(s, {'"': "&quot;"})
# Gaya polos hitam-putih, sama dengan activity_state.py.
FONT = "fontFamily=Times New Roman;"
ACT = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
OBJ = "rounded=0;whiteSpace=wrap;html=1;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
START = "ellipse;html=1;fillColor=#000000;strokeColor=#000000;"
FINAL = "ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;"
EDGE = ("endArrow=open;endSize=8;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;fontSize=11;"
        "labelBackgroundColor=#FFFFFF;strokeColor=#000000;" + FONT)
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=16;fontStyle=1;align=left;verticalAlign=middle;"


class Page:
    def __init__(s, pid, name):
        s.P, s.id, s.name, s.cells, s.maxx, s.maxy = f"tk-met{pid}-", f"tk-met{pid}", name, [], 0, 0

    def v(s, id, val, style, x, y, w, h):
        s.maxx, s.maxy = max(s.maxx, x + w), max(s.maxy, y + h)
        s.cells.append(f'<mxCell id="{s.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                       f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

    def e(s, id, a, b, exit=None, entry=None):
        st = EDGE
        if exit: st += f"exitX={exit[0]};exitY={exit[1]};exitDx=0;exitDy=0;"
        if entry: st += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        s.cells.append(f'<mxCell id="{s.P}{id}" value="" style="{st}" edge="1" parent="1" '
                       f'source="{s.P}{a}" target="{s.P}{b}"><mxGeometry relative="1" as="geometry"/></mxCell>')

    def xml(s):
        w, h = s.maxx + 30, s.maxy + 30
        return (f'<diagram id="{s.id}" name="{esc(s.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" '
                f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" math="0" shadow="0">'
                '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(s.cells) + "</root></mxGraphModel></diagram>")


def lbl(stereo, aksi, hasil):
    return (f"«{stereo}»<br>" if stereo else "") + f"<b>{aksi}</b><br>({hasil})"


W, H, GAP = 180, 66, 46
X = [80 + i * (W + GAP) for i in range(4)]   # kolom aksi
Y0, Y1, Y2 = 20, 120, 250                    # baris masukan, baris aksi 1, baris aksi 2

p = Page(1, "Metode TO-BE (1-1) - Alur Metode Perancangan")
p.v("in", "Instrumen Monev, ISO/IEC 17025,<br>dan dokumen lab", OBJ, X[0], Y0, W, 50)
p.v("start", "", START, 30, Y1 + H / 2 - 11, 22, 22)
# baris 1, kiri ke kanan
p.v("a1", lbl("", "Menyusun kebutuhan", "kebutuhan fungsional dan nonfungsional"), ACT, X[0], Y1, W, H)
p.v("a2", lbl("", "Memodelkan proses bisnis <i>to-be</i>", "<i>activity diagram</i>, <i>state machine diagram</i>"),
    ACT, X[1], Y1, W, H)
p.v("a3", lbl("", "Menurunkan <i>use case</i>", "<i>use case diagram</i>"), ACT, X[2], Y1, W, H)
p.v("a4", lbl("", "Memperluas <i>use case</i>", "alur, eksepsi, dan aturan bisnis"), ACT, X[3], Y1, W, H)
# baris 2, kanan ke kiri
p.v("a5", lbl("bahan kerja", "Menyusun <i>system sequence diagram</i>", "operasi sistem"), ACT, X[3], Y2, W, H)
p.v("a6", lbl("bahan kerja", "Menyusun <i>conceptual model</i>", "konsep dan asosiasi"), ACT, X[2], Y2, W, H)
p.v("a7", lbl("", "Menyusun <i>design class diagram</i>", "kelas Odoo, <i>method</i>, <i>inheritance</i>"),
    ACT, X[1], Y2, W, H)
p.v("final", "", FINAL, X[1] - GAP - 26 + 10, Y2 + H / 2 - 13, 26, 26)

p.e("f0", "start", "a1")
p.e("fin", "in", "a1", exit=(0.5, 1), entry=(0.5, 0))
p.e("f1", "a1", "a2")
p.e("f2", "a2", "a3")
p.e("f3", "a3", "a4")
p.e("f4", "a4", "a5", exit=(0.5, 1), entry=(0.5, 0))
p.e("f5", "a5", "a6")
p.e("f6", "a6", "a7")
p.e("f7", "a7", "final")

# halaman catatan (bahan kerja, tidak disisipkan ke naskah)
c = Page("-notes", "Catatan Metode TO-BE (bahan kerja)")
c.v("title", "Catatan alur metode perancangan (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 10, 900, 36)
c.v("legend", "<b>Notasi</b> (UML activity diagram)<br>"
    "• Kotak sudut bulat = aksi (tahap metode); teks dalam kurung = hasil tahap.<br>"
    "• Kotak sudut siku = object node (masukan).<br>"
    "• «bahan kerja» = hasil tahap tidak dimuat di subbab 2.3, hanya dipakai untuk menurunkan method dan kelas.",
    NOTE, 40, 56, 900, 80)
c.v("src", "<b>Sumber</b><br>• Wazlawick (2024), bab 3–4, 6–9, 13; CLAUDE.md bagian 4 (langkah 4–10). "
    "Draf 18 Nov 2026 · Febriyan<br>• Gambar 2.3 naskah Bab II (subbab 2.2.4).", NOTE, 40, 150, 900, 60)
c.v("konf", "<b>Isu terbuka</b><br>• Iterasi antar-tahap (kembali ke tahap sebelumnya saat menemukan transisi atau "
    "aturan baru) tidak digambar agar ringkas; dijelaskan di paragraf naskah bila perlu.",
    NOTE, 40, 224, 900, 60)

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + p.xml() + c.xml() + "</mxfile>")
