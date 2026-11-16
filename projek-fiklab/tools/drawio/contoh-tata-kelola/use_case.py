"""Use case diagram modul Tata Kelola & Dokumen (langkah 6), 3 halaman.

Pemakaian: python3 -I use_case.py projek-fiklab/rancangan/use-case-tata-kelola.drawio
"""
import sys
from xml.sax.saxutils import escape
OUT = sys.argv[1]
def esc(s): return escape(s, {'"': "&quot;"})
# Gaya polos hitam-putih (sama dengan activity_state.py): tanpa warna isi, tanpa garis putus-putus.
# Halaman diagram hanya berisi diagram; judul, legenda, dan catatan dikumpulkan di halaman catatan terakhir.
FONT = "fontFamily=Times New Roman;"
BOUND = "rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fontStyle=1;fontSize=14;spacingTop=8;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
PKG = ("shape=folder;tabWidth=270;tabHeight=22;tabPosition=left;html=1;whiteSpace=wrap;verticalAlign=top;align=left;"
       "spacingLeft=8;spacingTop=2;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#000000;" + FONT)
ELL = "ellipse;whiteSpace=wrap;html=1;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
ACT = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
ACT_ABS = ACT + "fontStyle=2;"   # aktor abstrak: nama miring (notasi UML)
ACT_SYS = ACT
ASSOC = "endArrow=none;html=1;strokeColor=#000000;"
GEN = "endArrow=block;endFill=0;endSize=14;html=1;strokeColor=#000000;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=16;fontStyle=1;align=left;verticalAlign=middle;"

# nomor: (nama, stereotype, lapis); lapis W = Inti, O = Pelengkap. Lapis tidak dibedakan di diagram, hanya di dokumen
UC = {
    1: ("Ajukan Dokumen", "", "W"), 2: ("Terbitkan Dokumen Resmi", "", "W"),
    3: ("Unggah Dokumen Bertanda Tangan", "", "W"), 4: ("Kembalikan Dokumen", "", "W"),
    5: ("Sahkan Dokumen", "", "W"), 6: ("Cabut Dokumen", "", "W"),
    7: ("Kedaluwarsakan Dokumen Berperiode", "", "O"),
    8: ("Kelola Personel", "CRUDL", "W"), 9: ("Kelola Jabatan", "CRUDL", "W"),
    10: ("Susun SK Penetapan Pengelola", "", "W"), 11: ("Catat Rapat Koordinasi", "", "W"),
    12: ("Catat Evaluasi Struktur", "", "W"), 13: ("Lihat Laporan Struktur Organisasi", "report", "W"),
    14: ("Kelola Dokumen Induk", "CRUDL", "W"), 15: ("Unggah Versi Dokumen", "", "W"),
    16: ("Catat Distribusi Dokumen", "", "W"), 17: ("Catat Sosialisasi Dokumen", "", "W"),
    18: ("Tinjau Ulang Dokumen", "", "W"), 19: ("Baca Dokumen Berlaku", "", "O"),
    20: ("Lihat Laporan Pengendalian Dokumen", "report", "W"),
    21: ("Kelola KPI", "CRUDL", "W"), 22: ("Kelola Renstra", "CRUDL", "W"),
    23: ("Susun Rencana", "", "W"), 24: ("Buat Revisi Rencana", "", "O"),
    25: ("Isi Realisasi Rencana", "", "W"), 26: ("Catat Tinjauan Rencana", "", "W"),
    27: ("Lihat Laporan Rencana", "report", "W"), 28: ("Lihat Status Monev", "report", "W"),
}


class Page:
    def __init__(s, n, name):
        s.P, s.name, s.n, s.cells = f"tk-uc{n}-", name, n, []
        s.maxx = s.maxy = 0

    def v(s, id, val, style, x, y, w, h):
        s.maxx, s.maxy = max(s.maxx, x + w), max(s.maxy, y + h + (40 if "umlActor" in style else 0))
        s.cells.append(f'<mxCell id="{s.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

    def e(s, id, a, b, style):
        s.cells.append(f'<mxCell id="{s.P}{id}" value="" style="{style}" edge="1" parent="1" source="{s.P}{a}" target="{s.P}{b}"><mxGeometry relative="1" as="geometry"/></mxCell>')

    def pkg(s, id, name, x, y, w, ucs, uc_x):
        h = 40 + 70 * len(ucs)
        s.v(id, name, PKG, x, y, w, h)
        for i, n in enumerate(ucs):
            label, st, lapis = UC[n]
            top = f"<font style='font-size:10px'>«{st}»</font><br>" if st else ""
            s.v(f"uc{n:02d}", f"{top}<b>UC-{n:02d}</b><br>{label}", ELL, uc_x, y + 34 + 70 * i, 250, 58)
        return y + h

    def actor(s, id, label, x, y, kind="h"):
        s.v(id, label, {"h": ACT, "a": ACT_ABS, "s": ACT_SYS}[kind], x, y, 30, 60)

    def links(s, d):
        for a, ns in d.items():
            for n in ns:
                s.e(f"a-{a}-{n:02d}", a, f"uc{n:02d}", ASSOC)

    def xml(s, w=None, h=None):
        w, h = w or s.maxx + 40, h or s.maxy + 30
        return (f'<diagram id="tk-uc{s.n}" name="{esc(s.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" '
                f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" math="0" shadow="0"><root>'
                '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(s.cells) + "</root></mxGraphModel></diagram>")


LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §4.2–4.3)<br>"
          "• Nama aktor miring = <b>aktor abstrak</b>; panah segitiga kosong = generalisasi (turunan mewarisi use case induk)<br>"
          "• Aktor «system» = pemicu berbasis waktu<br>"
          "• «CRUDL» = kelola data (buat, lihat, ubah, hapus, daftar) dengan satu pola; «report» = hanya membaca<br>"
          "• Tanpa «include»/«extend»: setiap use case satu sesi dan berdiri sendiri (§4.3.1, §4.5)")
SRC = ("Diturunkan dari activity A1–A4 dan state machine S1–S2 (proses-bisnis-tata-kelola.md), "
       "kebutuhan KF-01–45. Rincian: use-case-tata-kelola.md · Draf 14 Nov 2026 · Febriyan")
SYS = "Sistem LabFIK Compliance · Modul Tata Kelola & Dokumen"
pages, notes = [], []

# ---------- halaman 1: pengesahan
_n = []
p = Page(1, "UC TO-BE (1-3) - Pengesahan Dokumen")
judul = "Use case TO-BE 1/3 · Pengesahan Dokumen (dipakai semua dokumen) dan hierarki aktor"
p.v("sys", SYS, BOUND, 400, 60, 760, 560)
p.pkg("p1", "Pengesahan Dokumen", 430, 100, 340, [1, 2, 3, 4, 5, 6], 475)
p.pkg("p2", "Otomatis (berbasis waktu)", 800, 100, 330, [7], 840)
p.actor("pgn", "Pengguna Lab<br>(dosen, asisten)", 90, 90)
p.actor("pnl", "Pengelola Lab", 260, 200, "a")
p.actor("lab", "Laboran/PLP", 90, 400)
p.actor("kal", "KaLab", 260, 420)
p.actor("jdw", "«system»<br>Penjadwal", 1240, 150, "s")
p.links({"pnl": [1, 2, 3], "kal": [4, 5, 6], "jdw": [7]})
p.e("g-pnl-pgn", "pnl", "pgn", GEN)
p.e("g-lab-pnl", "lab", "pnl", GEN)
p.e("g-kal-pnl", "kal", "pnl", GEN)
_n.append("<b>Cara baca</b><br>• <i>Pengelola Lab</i> = peran penyusun dokumen: KaLab (rencana, SK, Renstra) atau Laboran (SOP/IK). "
    "Pengelola Lab juga <i>Pengguna Lab</i>, jadi bisa membaca dokumen berlaku (UC-19).<br>"
    "• Kembalikan, sahkan, dan cabut hanya oleh <b>KaLab</b>, sebagai pencatat pengesahan.<br>"
    "• Dokumen yang memakai use case ini dibuat di UC-10 (SK), UC-15 (versi SOP/IK), UC-22 (Renstra), dan UC-23 (rencana).")
_n.append("<b>Bukan aktor</b>: Dekan dan pejabat penanda tangan (tanda tangan di kertas, dicatat sebagai pengesah), "
    "penilai monev (menerima PDF), dan pihak eksternal. Keputusan 14 Nov 2026.<br>" + SRC)
notes.append((judul, _n)); pages.append(p)

# ---------- halaman 2: struktur + dokumen
_n = []
p = Page(2, "UC TO-BE (2-3) - Struktur dan Pengendalian Dokumen")
judul = "Use case TO-BE 2/3 · Struktur Organisasi (PKG-03) dan Pengendalian Dokumen SOP/IK (PKG-02)"
p.v("sys", SYS, BOUND, 300, 60, 880, 610)
p.pkg("p1", "Struktur Organisasi (PKG-03)", 330, 100, 370, [8, 9, 10, 11, 12, 13], 390)
p.pkg("p2", "Pengendalian Dokumen (PKG-02)", 780, 100, 370, [14, 15, 16, 17, 18, 20, 19], 840)
p.actor("kal", "KaLab", 150, 330)
p.actor("pnl", "Pengelola Lab", 1270, 130, "a")
p.actor("lab", "Laboran/PLP", 1270, 330)
p.actor("pgn", "Pengguna Lab<br>(dosen, asisten)", 1270, 540)
p.links({"kal": [8, 9, 10, 11, 12, 13], "pnl": [14, 18, 20], "lab": [15, 16, 17], "pgn": [19]})
p.e("g-lab-pnl", "lab", "pnl", GEN)
_n.append("<b>Cara baca</b><br>• KaLab juga turunan <i>Pengelola Lab</i> dan <i>Pengguna Lab</i> (halaman 1/3), "
    "jadi KaLab juga bisa melakukan UC-14, 18, dan 19.<br>"
    "• SK (UC-10) dan versi dokumen (UC-15) diajukan dan disahkan lewat halaman 1/3.<br>"
    "• UC-13 memuat bagan organisasi, uraian tugas, dan matriks kewenangan. UC-20 memuat daftar induk, riwayat revisi, "
    "serta rekaman distribusi, sosialisasi, dan tinjau ulang.")
_n.append(SRC)
notes.append((judul, _n)); pages.append(p)

# ---------- halaman 3: perencanaan + monev
_n = []
p = Page(3, "UC TO-BE (3-3) - Perencanaan dan Status Monev")
judul = "Use case TO-BE 3/3 · Perencanaan (PKG-01, PKG-13) dan Status Monev"
p.v("sys", SYS, BOUND, 300, 60, 880, 610)
p.pkg("p1", "Perencanaan (PKG-01, PKG-13)", 330, 100, 370, [21, 22, 23, 24, 25, 26, 27], 390)
p.pkg("p2", "Status Monev", 780, 100, 370, [28], 840)
p.actor("kal", "KaLab", 150, 300)
p.actor("pnl", "Pengelola Lab<br>(PIC item)", 1270, 420, "a")
p.links({"kal": [21, 22, 23, 24, 26, 27, 28], "pnl": [25]})
_n.append("<b>Cara baca</b><br>• UC-23 mencakup rencana tahunan dan rencana pengembangan (temuan gap + item program).<br>"
    "• Renstra (UC-22) dan rencana (UC-23) diajukan dan disahkan lewat halaman 1/3.<br>"
    "• UC-25 dilakukan PIC item: Laboran atau KaLab.<br>"
    "• UC-26 mencakup ukuran manfaat untuk rencana pengembangan.<br>"
    "• UC-28: persentase PKG-02 dan kriteria tertinggi K1–K4 dengan tautan bukti; hasilnya diserahkan ke penilai sebagai PDF.")
_n.append(SRC)
notes.append((judul, _n)); pages.append(p)

# ---------- halaman catatan (bahan kerja, tidak disisipkan ke naskah)
c = Page("-notes", "Catatan UC TO-BE (bahan kerja)")
c.P = "tk-uc-notes-"
c.v("title", "Catatan use case diagram (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 10, 1100, 36)
c.v("legend", LEGEND, NOTE, 40, 56, 1100, 100)
y = 176
for i, (judul, items) in enumerate(notes):
    c.v(f"h{i}", f"<b>{judul}</b>", "text;html=1;fontSize=12;align=left;verticalAlign=top;whiteSpace=wrap;", 40, y, 1100, 24)
    y += 30
    for j, txt in enumerate(items):
        h = 40 + 18 * (len(txt) // 170 + txt.count("<br>"))
        c.v(f"n{i}-{j}", txt, NOTE, 40, y, 1100, h)
        y += h + 10
    y += 10
pages.append(c)

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(pg.xml() for pg in pages) + "</mxfile>")
