"""Use case diagram modul Pelaksanaan Praktikum (langkah 6), 3 halaman.

Disalin dari pola contoh-tata-kelola/use_case.py; data dan prefiks diganti. Gaya polos hitam-putih (17 Nov 2026).
Pemakaian: python3 -I use_case.py projek-fiklab/rancangan/use-case-praktikum.drawio
"""
import sys
from xml.sax.saxutils import escape
OUT = sys.argv[1]
def esc(s): return escape(s, {'"': "&quot;"})
# Gaya polos hitam-putih (CLAUDE.md bagian 5, mengikuti contoh-tata-kelola/use_case.py): tanpa warna isi dan warna garis.
# Halaman diagram hanya berisi diagram; judul, legenda, dan catatan dikumpulkan di halaman catatan terakhir.
FONT = "fontFamily=Times New Roman;"
BOUND = "rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fontStyle=1;fontSize=14;spacingTop=8;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
PKG = ("shape=folder;tabWidth=270;tabHeight=22;tabPosition=left;html=1;whiteSpace=wrap;verticalAlign=top;align=left;"
       "spacingLeft=8;spacingTop=2;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#000000;" + FONT)
ELL = "ellipse;whiteSpace=wrap;html=1;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
ACT = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
ACT_ABS = ACT + "fontStyle=2;"   # aktor abstrak: nama miring (notasi UML)
ACT_ABS_SIDE = ACT_ABS.replace("verticalLabelPosition=bottom;verticalAlign=top;", "labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=4;")
FRAME = "rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;align=left;spacingLeft=8;spacingTop=4;fontSize=11;fillColor=none;strokeColor=#000000;wadah=1;" + FONT
ASSOC = "endArrow=none;html=1;strokeColor=#000000;"
GEN = "endArrow=block;endFill=0;endSize=14;html=1;strokeColor=#000000;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=16;fontStyle=1;align=left;verticalAlign=middle;"

# nomor: (nama, stereotype, lapis); lapis W = Inti, O = Pelengkap (hanya dicatat di dokumen)
UC = {
    1: ("Kelola Mata Kuliah", "CRUDL", "W"), 2: ("Kelola Kelas", "CRUDL", "W"),
    3: ("Impor Jadwal Kelas", "", "W"), 4: ("Susun Penetapan Jadwal", "", "W"),
    5: ("Terbitkan Versi Modul", "", "W"), 6: ("Baca Modul Berlaku", "", "W"),
    7: ("Ajukan Pemakaian Lab", "", "W"), 8: ("Putuskan Pemakaian Lab", "", "W"),
    9: ("Tarik Pengajuan", "", "O"), 10: ("Lihat Laporan Jadwal", "report", "W"),
    11: ("Periksa Kesiapan Sesi", "", "W"), 12: ("Setujui Substitusi Bahan", "", "W"),
    13: ("Kirim Jurnal Sesi", "", "W"), 14: ("Ajukan Perubahan Sesi", "", "W"),
    15: ("Putuskan Perubahan Sesi", "", "W"), 16: ("Lihat Laporan Pelaksanaan", "report", "O"),
    17: ("Catat Penilaian Kelas", "", "W"), 18: ("Impor Nilai Kelas", "", "O"),
    19: ("Susun Survei Kepuasan", "", "W"), 20: ("Tetapkan Survei Kepuasan", "", "W"),
    21: ("Batalkan Penetapan Survei", "", "O"), 22: ("Isi Survei Kepuasan", "", "W"),
    23: ("Catat Evaluasi Survei", "", "W"), 24: ("Nilai Efektivitas Tindak Lanjut", "", "W"),
    25: ("Lihat Laporan Survei", "report", "W"), 26: ("Lihat Status Monev Praktikum", "report", "W"),
    27: ("Terbitkan Laporan Bukti", "", "W"), 28: ("Kelola Pengaturan Praktikum", "CRUDL", "W"),
}


class Page:
    def __init__(s, n, name):
        s.P, s.name, s.n, s.cells = f"prk-uc{n}-", name, n, []
        s.ax, s.ux = {}, {}
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
            s.v(f"uc{n:02d}", f"{top}<b>UC-PRK-{n:02d}</b><br>{label}", ELL, uc_x, y + 34 + 70 * i, 250, 58)
            s.ux[n] = uc_x
        return y + h

    def actor(s, id, label, x, y, kind="h"):
        s.v(id, label, {"h": ACT, "a": ACT_ABS, "as": ACT_ABS_SIDE}[kind], x, y, 30, 60)
        s.ax[id] = x

    def links(s, d):
        for a, ns in d.items():
            for n in ns:
                side = "entryX=0;entryY=0.5;" if s.ax[a] < s.ux[n] else "entryX=1;entryY=0.5;"
                s.e(f"a-{a}-{n:02d}", a, f"uc{n:02d}", ASSOC + side)

    def xml(s, w=None, h=None):
        w, h = w or s.maxx + 40, h or s.maxy + 30
        return (f'<diagram id="prk-uc{s.n}" name="{esc(s.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" '
                f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" math="0" shadow="0"><root>'
                '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(s.cells) + "</root></mxGraphModel></diagram>")


LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §4.2–4.3)<br>"
          "• Aktor bernama miring = <b>aktor abstrak</b>; panah segitiga kosong = generalisasi (turunan mewarisi use case induk)<br>"
          "• «CRUDL» = kelola data (buat, lihat, ubah, hapus, daftar) dengan satu pola; «report» = hanya membaca<br>"
          "• Tanpa «include»/«extend»: setiap use case satu sesi dan berdiri sendiri (§4.3.1, §4.5)<br>"
          "• Tidak ada aktor «system» Penjadwal: status yang bergantung waktu dihitung, tidak dijadwalkan")
SRC = ("Diturunkan dari activity A1–A5 dan state machine S1–S3 (proses-bisnis-praktikum.md), kebutuhan KF-PRK-01–52. "
       "Rincian: use-case-praktikum.md · Draf 16 Nov 2026 · Herrens")
SYS = "Sistem LabFIK Compliance · Modul Pelaksanaan Praktikum"
pages, notes = [], []

# ---------- halaman 1: jadwal, modul, pemakaian lab (PKG-15)
_n = []
p = Page(1, "UC TO-BE (1-3) - Jadwal, Modul, dan Pemakaian Lab")
judul = "Use case TO-BE 1/3 · Jadwal, Modul, dan Pemakaian Lab (PKG-15)"
p.v("sys", SYS, BOUND, 380, 60, 880, 740)
p.pkg("p1", "Jadwal (PKG-15)", 410, 100, 380, [1, 2, 3, 4, 10], 470)
p.pkg("p2", "Pemakaian Lab (PKG-15)", 410, 520, 380, [7, 8, 9], 470)
p.pkg("p3", "Modul (PKG-15, dipakai 16, 17, 19)", 850, 100, 380, [5, 6], 910)
_n.append("<b>Pengesahan jadwal</b> memakai use case milik <b>Tata Kelola</b>, tidak dibuat ulang: "
    "<i>Ajukan Dokumen</i> (UC-01), <i>Terbitkan Dokumen Resmi</i> (UC-02), <i>Unggah Dokumen Bertanda Tangan</i> (UC-03), "
    "<i>Kembalikan Dokumen</i> (UC-04), <i>Sahkan Dokumen</i> (UC-05), dan <i>Cabut Dokumen</i> (UC-06) oleh KaLab, "
    "lewat <code>labfik.approval.mixin</code>. UC-PRK-04 menyiapkan dokumennya.")
p.actor("lab", "Laboran", 150, 180)
p.actor("kal", "KaLab", 150, 420)
p.actor("dos", "Dosen", 1330, 130)
p.actor("ptg", "Petugas Praktikum", 1330, 520, "a")
p.links({"lab": [1, 2, 3, 4, 7, 10], "kal": [8, 10], "dos": [5], "ptg": [6, 9, 10]})
_n.append("<b>Cara baca</b><br>• <i>Petugas Praktikum</i> = asisten, dosen, atau laboran yang bertugas di sesi (hierarki di halaman 2/3).<br>"
    "• UC-PRK-03: berkas jadwal dari tim jadwal fakultas (pola mingguan per kelas); sistem membangkitkan 16 sesi per kelas, "
    "memeriksa bentrok dan kapasitas <b>[ASUMSI: impor berkas, tanpa API]</b>.<br>"
    "• UC-PRK-10: jadwal terpadu (sesi + pemakaian disetujui) dan rekaman konflik.<br>"
    "• UC-PRK-07: pengguna lab tidak punya akun; laboran mencatat permintaannya. UC-PRK-09: menarik pengajuan sebelum diputuskan "
    "(laboran turunan Petugas Praktikum).")
_n.append("<b>Bukan aktor</b>: pengguna lab di luar praktikum (tanpa akun; dicatat laboran), tim jadwal fakultas (berkasnya diimpor laboran), Dekan, penilai monev (menerima PDF), pihak eksternal. "
    + SRC)
notes.append((judul, _n)); pages.append(p)

# ---------- halaman 2: pelaksanaan sesi (PKG-16, 17, 18)
_n = []
p = Page(2, "UC TO-BE (2-3) - Pelaksanaan Sesi")
judul = "Use case TO-BE 2/3 · Kesiapan (PKG-16, 17) dan Pelaksanaan Sesi (PKG-18), dengan hierarki aktor"
p.v("sys", SYS, BOUND, 380, 60, 880, 560)
p.pkg("p1", "Pelaksanaan Sesi (PKG-18)", 410, 100, 380, [13, 14, 15, 16], 470)
p.pkg("p2", "Kesiapan Alat, Software, Bahan (PKG-16, 17)", 850, 300, 380, [11, 12], 910)
p.actor("kal", "KaLab", 150, 330)
p.actor("ptg", "Petugas Praktikum", 1330, 140, "a")
p.actor("lab", "Laboran", 1330, 310)
p.actor("dos", "Dosen", 1330, 420)
p.links({"kal": [15, 16], "ptg": [13, 14], "lab": [11], "dos": [12]})
# hierarki aktor digambar terpisah agar panah generalisasi tidak menyilang garis asosiasi
p.v("hbox", "<b>Hierarki aktor</b> (§4.2): turunan mewarisi use case <i>Petugas Praktikum</i>", FRAME, 1290, 520, 330, 300)
p.actor("ptg2", "Petugas Praktikum", 1440, 580, "as")
p.actor("asi2", "Asisten", 1320, 720)
p.actor("dos2", "Dosen", 1440, 720)
p.actor("lab2", "Laboran", 1560, 720)
for c, ex in (("asi2", 0.1), ("dos2", 0.5), ("lab2", 0.9)):
    p.e(f"g-{c}-ptg2", c, "ptg2", GEN + f"exitX=0.5;exitY=0;entryX={ex};entryY=1;")
_n.append("<b>Cara baca</b><br>• UC-PRK-13 dalam satu sesi kerja: isi jurnal, presensi petugas (merujuk <code>hr.employee</code>), "
    "<i>log book</i>, lalu kirim; sistem memvalidasi, mengubah Sesi menjadi <i>terlaksana</i>, dan menandai petugas yang tidak sesuai penugasan SDM.<br>"
    "• Pengisi jurnal kelas tanpa asisten = dosen yang mengajar <b>[ASUMSI]</b>.<br>"
    "• UC-PRK-11 dilakukan sebelum jam mulai; keputusan <i>tunda</i> dilanjutkan dengan UC-PRK-14 (sesi lain, tidak di-«include»). "
    "Alat ruang (master Core) hanya dibaca sebagai peringatan dan isian awal (O).<br>"
    "• UC-PRK-15 membangkitkan sesi pengganti bila disetujui dengan pengganti.")
_n.append(SRC)
notes.append((judul, _n)); pages.append(p)

# ---------- halaman 3: penilaian, kepuasan, status monev (PKG-19, 20)
_n = []
p = Page(3, "UC TO-BE (3-3) - Penilaian, Kepuasan, dan Status Monev")
judul = "Use case TO-BE 3/3 · Penilaian (PKG-19), Kepuasan Pengguna (PKG-20), dan Status Monev"
p.v("sys", SYS, BOUND, 380, 60, 880, 620)
p.pkg("p1", "Penilaian Individual (PKG-19)", 410, 100, 380, [17, 18], 470)
p.pkg("p2", "Status Monev", 410, 310, 380, [26, 27, 28], 470)
p.pkg("p3", "Kepuasan Pengguna (PKG-20)", 850, 100, 380, [19, 20, 21, 23, 24, 25, 22], 910)
p.actor("dos", "Dosen", 150, 110)
p.actor("lab", "Laboran", 150, 230)
p.actor("kal", "KaLab", 150, 420)
p.actor("ka2", "KaLab", 1330, 220)
p.actor("res", "Responden<br>(praktikan, dosen, asisten)", 1330, 555)
p.links({"dos": [17, 18], "lab": [17, 18], "kal": [26, 27, 28], "ka2": [19, 20, 21, 23, 24, 25], "res": [22]})
_n.append("• KaLab digambar dua kali hanya agar garis tidak menyilang")
_n.append("<b>Cara baca</b><br>• UC-PRK-17: tautan penilaian LeADS per kelas (Inti); UC-PRK-18: impor ekspor Excel LeADS bila tersedia (Pelengkap).<br>"
    "• UC-PRK-22: lewat tautan addon <code>survey</code>, tanpa nama, tanpa login.<br>"
    "• UC-PRK-26: persentase PKG-15–19 dan kriteria tertinggi K1–K4 PKG-20; skor kriteria berurutan ditetapkan penilai.<br>"
    "• UC-PRK-27: laporan bukti per indikator per periode, diserahkan ke penilai.")
_n.append(SRC)
notes.append((judul, _n)); pages.append(p)

# ---------- halaman catatan (bahan kerja, tidak disisipkan ke naskah)
c = Page("-notes", "Catatan UC TO-BE (bahan kerja)")
c.P = "prk-uc-notes-"
c.v("title", "Catatan use case diagram (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 10, 1100, 36)
c.v("legend", LEGEND, NOTE, 40, 56, 1100, 110)
y = 186
for i, (judul, items) in enumerate(notes):
    c.v(f"h{i}", f"<b>{judul}</b>", "text;html=1;fontSize=12;align=left;verticalAlign=top;whiteSpace=wrap;", 40, y, 1100, 24)
    y += 30
    for j, txt in enumerate(items):
        h = 40 + 18 * (len(txt) // 170 + txt.count("<br>"))
        c.v(f"n{i}-{j}", txt, NOTE, 40, y, 1100, h)
        y += h + 10
    y += 10
pages.append(c)

open(OUT, "w", encoding="utf-8").write('<mxfile host="app.diagrams.net">' + "".join(pg.xml() for pg in pages) + "</mxfile>")
