import sys
from xml.sax.saxutils import escape
OUT = sys.argv[1]
def esc(s): return escape(s, {'"': "&quot;"})
PF, PS = "#F5F0FF", "#9673A6"
BOUND = f"rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fontStyle=1;fontSize=15;spacingTop=8;fillColor=#FFFFFF;strokeColor={PS};strokeWidth=2;"
PKG = ("shape=folder;tabWidth=270;tabHeight=22;tabPosition=left;html=1;whiteSpace=wrap;verticalAlign=top;align=left;"
       f"spacingLeft=8;spacingTop=2;fontSize=12;fontStyle=1;fillColor={PF};strokeColor={PS};")
ELL = "ellipse;whiteSpace=wrap;html=1;fontSize=11;fillColor=#FFFFFF;strokeColor=#333333;"
ACT = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fontStyle=1;"
ACT_ABS = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fontStyle=3;fillColor=#F5F0FF;"
ACT_SYS = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fontStyle=1;fillColor=#EEEEEE;"
ASSOC = "endArrow=none;html=1;strokeColor=#555555;"
GEN = "endArrow=block;endFill=0;endSize=14;html=1;strokeColor=#333333;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
UC = {
 1: ("Kelola Personel", "CRUDL"), 2: ("Kelola Jabatan", "CRUDL"), 3: ("Susun SK Penetapan Pengelola", ""),
 4: ("Catat Rapat Koordinasi", ""), 5: ("Catat Evaluasi Struktur", ""), 6: ("Lihat Laporan Struktur Organisasi", "report"),
 7: ("Kelola Dokumen Induk", "CRUDL"), 8: ("Unggah Versi Dokumen", ""), 9: ("Catat Distribusi Dokumen", ""),
 10: ("Catat Sosialisasi Dokumen", ""), 11: ("Tinjau Ulang Dokumen", ""), 12: ("Baca Dokumen Berlaku", ""),
 13: ("Lihat Laporan Pengendalian Dokumen", "report"), 14: ("Kelola KPI", "CRUDL"), 15: ("Kelola Sasaran Renstra", "CRUDL"),
 16: ("Susun Rencana", ""), 18: ("Isi Realisasi Rencana", ""), 19: ("Catat Tinjauan Rencana", ""),
 20: ("Lihat Laporan Rencana", "report"), 21: ("Ajukan Dokumen", ""), 22: ("Tarik Pengajuan Dokumen", ""),
 23: ("Periksa Dokumen", ""), 24: ("Kembalikan Dokumen", ""), 25: ("Terbitkan Dokumen Resmi", ""),
 26: ("Unggah Dokumen Bertanda Tangan", ""), 27: ("Sahkan Dokumen", ""), 28: ("Cabut Dokumen", ""),
 29: ("Lihat Status Monev", "report"), 30: ("Atur Pengaturan Modul", ""),
 31: ("Kedaluwarsakan Dokumen Berperiode", ""), 32: ("Kirim Pengingat Jadwal", ""),
}

class Page:
    def __init__(s, n, name):
        s.P, s.name, s.n, s.cells = f"tk-uc{n}-", name, n, []
    def v(s, id, val, style, x, y, w, h):
        s.cells.append(f'<mxCell id="{s.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    def e(s, id, a, b, style):
        s.cells.append(f'<mxCell id="{s.P}{id}" value="" style="{style}" edge="1" parent="1" source="{s.P}{a}" target="{s.P}{b}"><mxGeometry relative="1" as="geometry"/></mxCell>')
    def pkg(s, id, name, x, y, w, ucs, uc_x):
        h = 40 + 70 * len(ucs)
        s.v(id, name, PKG, x, y, w, h)
        for i, n in enumerate(ucs):
            label, st = UC[n]
            top = f"<font style='font-size:9px' color='#6C4A87'>«{st}»</font><br>" if st else ""
            s.v(f"uc{n:02d}", f"{top}<b>UC-{n:02d}</b><br>{label}", ELL, uc_x, y + 34 + 70 * i, 240, 58)
        return y + h
    def actor(s, id, label, x, y, kind="h"):
        s.v(id, label, {"h": ACT, "a": ACT_ABS, "s": ACT_SYS}[kind], x, y, 30, 60)
    def links(s, d):
        for a, ns in d.items():
            for n in ns:
                s.e(f"a-{a}-{n:02d}", a, f"uc{n:02d}", ASSOC)
    def xml(s, w, h):
        return (f'<diagram id="tk-uc{s.n}" name="{esc(s.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" '
                f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" math="0" shadow="0"><root>'
                '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(s.cells) + "</root></mxGraphModel></diagram>")

SRC = ("Diturunkan dari activity A1–A4 dan state machine S1–S2 (rancangan/proses-bisnis-tata-kelola.md) "
       "dengan aturan Wazlawick 2024 §4.3–4.6, §4.8.2. Rincian: rancangan/use-case-tata-kelola.md · Draf 13 Nov 2026 · Febriyan")
pages = []

# ---------- page 1
p = Page(1, "UC TO-BE (1-3) - Pengesahan Dokumen")
p.v("sys", "Sistem LabFIK Compliance — Modul Tata Kelola &amp; Dokumen".replace("&amp;", "&"), BOUND, 360, 60, 760, 680)
p.pkg("p1", "Pengesahan Dokumen (dipakai semua dokumen)", 390, 100, 320, [21, 22, 25, 26, 23, 24, 27, 28], 430)
p.pkg("p2", "Otomatis (berbasis waktu)", 750, 260, 340, [31, 32], 800)
p.actor("pny", "Penyusun Dokumen", 225, 190, "a")
p.actor("pmr", "Pemeriksa", 225, 420, "h")
p.actor("pgs", "Pengesah Dokumen", 225, 580, "a")
p.actor("lab", "Laboran/PLP", 60, 140)
p.actor("kal", "KaLab", 60, 390)
p.actor("dek", "Dekan", 60, 640)
p.actor("jdw", "«system»<br>Penjadwal", 1200, 300, "s")
p.links({"pny": [21, 22, 25, 26], "pmr": [23, 24], "pgs": [24, 27, 28], "jdw": [31, 32]})
for c, par in [("lab", "pny"), ("kal", "pny"), ("kal", "pgs"), ("dek", "pgs")]:
    p.e(f"g-{c}-{par}", c, par, GEN)
p.v("n1", "<b>Cara baca</b><br>• Aktor miring (ungu) = <b>peran abstrak</b>. Panah segitiga kosong = generalisasi: KaLab dan Laboran berperan sebagai Penyusun; KaLab dan Dekan sebagai Pengesah, sesuai wewenang jabatan per jenis dokumen.<br>"
    "• «system» Penjadwal = pemicu berbasis waktu (Wazlawick §4.3.2).<br>"
    "• Use case di sini dipakai oleh dokumen dari UC-03 (SK), UC-08 (versi SOP/IK), dan UC-16 (rencana) di halaman 2/3 dan 3/3. "
    "Tidak memakai «include» karena pengajuan dan pengesahan terjadi di sesi dan hari yang berbeda (§4.5).", NOTE, 40, 770, 620, 120)
p.v("n2", "<b>Di luar sistem</b> (tugas «manual» di A1): cetak dokumen dan tanda tangan basah. Tanpa tanda tangan digital.<br>"
    "<b>[KONFIRMASI]</b> Bila Dekan tidak login, UC-27 dilakukan KaLab atas nama Dekan dengan berkas bertanda tangan sebagai bukti.", NOTE, 680, 770, 440, 100)
p.v("n3", SRC, NOTE, 40, 910, 1080, 46)
pages.append((p, 1320, 990))

# ---------- page 2
p = Page(2, "UC TO-BE (2-3) - Struktur dan Dokumen")
p.v("sys", "Sistem LabFIK Compliance — Modul Tata Kelola & Dokumen", BOUND, 300, 60, 860, 600)
p.pkg("p1", "Struktur Organisasi (PKG-03)", 330, 100, 360, [1, 2, 3, 4, 5, 6], 390)
p.pkg("p2", "Pengendalian Dokumen (PKG-02)", 760, 100, 370, [7, 8, 9, 10, 11, 13, 12], 825)
p.actor("adm", "Admin", 150, 110)
p.actor("kal", "KaLab", 150, 330)
p.actor("lab", "Laboran/PLP", 1250, 220)
p.actor("pnl", "Penilai Monev", 1250, 420)
p.actor("pgn", "Pengguna Lab<br>(dosen, asisten, mhs)", 1250, 560)
p.links({"adm": [1], "kal": [1, 2, 3, 4, 5, 6, 7, 11, 13], "lab": [7, 8, 9, 10, 11, 13], "pnl": [6, 13], "pgn": [12]})
p.v("n1", "<b>Cara baca</b><br>• «CRUDL» = kelola data (buat, lihat, ubah, hapus/arsipkan, daftar) dengan satu pola standar (Wazlawick §4.3, §6.7).<br>"
    "• «report» = use case kueri/laporan (hanya membaca).<br>"
    "• SK (UC-03) dan versi dokumen (UC-08) diajukan dan disahkan lewat halaman 1/3.<br>"
    "• Login tidak digambar karena bukan use case (§4.3.3).", NOTE, 40, 690, 620, 100)
p.v("n2", SRC, NOTE, 680, 690, 480, 80)
pages.append((p, 1400, 830))

# ---------- page 3
p = Page(3, "UC TO-BE (3-3) - Perencanaan dan Monev")
p.v("sys", "Sistem LabFIK Compliance — Modul Tata Kelola & Dokumen", BOUND, 300, 60, 860, 540)
p.pkg("p1", "Perencanaan (PKG-01, PKG-13)", 330, 100, 360, [14, 15, 16, 18, 19, 20], 390)
p.pkg("p2", "Status Monev &amp; Pengaturan".replace("&amp;", "&"), 760, 100, 370, [30, 29], 825)
p.actor("adm", "Admin", 150, 160)
p.actor("kal", "KaLab", 150, 330)
p.actor("lab", "Laboran/PLP", 1250, 290)
p.actor("pnl", "Penilai Monev", 1250, 150)
p.links({"adm": [15], "kal": [14, 15, 16, 18, 19, 20, 29, 30], "lab": [18], "pnl": [20, 29]})
p.v("n1", "<b>Cara baca</b><br>• UC-16 mencakup semua jenis rencana (strategis, RKT, IKU, pengembangan), analisis gap untuk rencana pengembangan, dan revisi dari rencana yang sudah disahkan.<br>"
    "• Rencana diajukan dan disahkan lewat halaman 1/3. Kedaluwarsa dan pengingat realisasi dipicu Penjadwal (halaman 1/3).<br>"
    "• Nomor UC-17 sengaja kosong (revisi rencana digabung ke UC-16).", NOTE, 40, 630, 620, 110)
p.v("n2", SRC, NOTE, 680, 630, 480, 80)
pages.append((p, 1400, 780))

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
