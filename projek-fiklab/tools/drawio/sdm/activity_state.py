"""Activity diagram (A1-A4) dan state machine (S1-S4) modul SDM & Kompetensi (Langkah 5).

Fungsi gambar dan gaya disalin dari contoh-tata-kelola/activity_state.py versi `main`
(gaya polos hitam-putih, 16 Nov 2026); yang diganti hanya data dan prefiks ID (sdm-).
Halaman diagram hanya berisi diagram; judul, legenda, sumber, dan [KONFIRMASI] ada di
halaman catatan terakhir.

Seluruh isi hanya scope modul SDM: pengesahan dokumen SDM digambar sendiri sebagai A4 dan S4,
tidak memanggil activity atau use case modul lain.

Jalankan:
    python -I projek-fiklab/tools/drawio/sdm/activity_state.py projek-fiklab/rancangan/activity-state-sdm.drawio
    python -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/activity-state-sdm.drawio sdm-
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]


def esc(s):
    return escape(s, {'"': "&quot;"})


FONT = "fontFamily=Times New Roman;"
TASK = "rounded=1;arcSize=40;whiteSpace=wrap;html=1;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
ST = {
    "user": TASK, "service": TASK, "manual": TASK, "call": TASK,
    "dec": "rhombus;html=1;fillColor=#FFFFFF;strokeColor=#000000;",
    "merge": "rhombus;html=1;fillColor=#FFFFFF;strokeColor=#000000;",
    "start": "ellipse;html=1;fillColor=#000000;strokeColor=#000000;",
    "final": "ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;",
    "fork": "html=1;fillColor=#000000;strokeColor=none;",
    "time": ("shape=collate;html=1;fillColor=#FFFFFF;strokeColor=#000000;labelPosition=right;verticalLabelPosition=middle;"
             "align=left;verticalAlign=middle;spacingLeft=6;fontSize=12;" + FONT),
}
SIZE = {"user": (180, 44), "service": (180, 44), "manual": (180, 44), "call": (180, 44), "dec": (30, 30),
        "merge": (30, 30), "start": (22, 22), "final": (26, 26), "time": (20, 26)}
STEREO = {"user": "«user»", "service": "«service»", "manual": "«manual»", "call": "«call behavior»"}
EDGE = ("endArrow=open;endSize=8;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;fontSize=11;"
        "labelBackgroundColor=#FFFFFF;strokeColor=#000000;" + FONT)
LANE = ("swimlane;html=1;startSize=30;fillColor=#FFFFFF;strokeColor=#000000;fontStyle=1;fontSize=12;"
        "swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;" + FONT)
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=16;fontStyle=1;align=left;verticalAlign=middle;"
TASK_H, SMALL_H = 62, 42  # tinggi baris tugas dan baris kecil (keputusan, gabungan, awal, akhir)


class Page:
    def __init__(self, pid, name, prefix):
        self.pid, self.name, self.P = pid, name, prefix
        self.cells, self.w, self.h = [], 1600, 1200

    def v(self, id, val, style, x, y, w, h):
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def e(self, id, s, t, val="", pts=None, style=EDGE, exit=None, entry=None, lx=None):
        st = style
        if exit:
            st += f"exitX={exit[0]};exitY={exit[1]};exitDx=0;exitDy=0;"
        if entry:
            st += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        geo = f'<mxGeometry{" x=\"%s\"" % lx if lx is not None else ""} relative="1" as="geometry">'
        if pts:
            geo += '<Array as="points">' + "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in pts) + "</Array>"
        geo += "</mxGeometry>"
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{st}" edge="1" parent="1" '
                          f'source="{self.P}{s}" target="{self.P}{t}">{geo}</mxCell>')

    def xml(self):
        return (f'<diagram id="{self.pid}" name="{esc(self.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" '
                f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.w:.0f}" '
                f'pageHeight="{self.h:.0f}" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
                + "".join(self.cells) + "</root></mxGraphModel></diagram>")


class Activity(Page):
    """Baris boleh memuat beberapa node di lajur berbeda; panah antarlajur dalam satu baris mendatar."""
    LANE_Y, HEAD = 20, 30

    def __init__(self, pid, name, prefix, lanes, rows, small):
        super().__init__(pid, name, prefix)
        self.lanes, x = {}, 20
        for key, label, w, cols in lanes:
            self.lanes[key] = (x, w, cols, label)
            x += w
        self.total_w = x - 20
        self.top, y = {}, self.LANE_Y + self.HEAD + 10
        for r in range(rows):
            h = SMALL_H if r in small else TASK_H
            self.top[r] = (y, h)
            y += h
        self.body_h = y - self.LANE_Y + 10

    def cy(self, row):
        y, h = self.top[int(row)]
        return y + h / 2 + (row - int(row)) * h

    def cx(self, lane, col):
        lx, lw, cols, _ = self.lanes[lane]
        if cols == 1 or col is None:
            return lx + lw / 2
        return lx + lw * (col + 0.5) / cols

    def n(self, id, lane, row, kind, label="", col=None):
        cx, cy = self.cx(lane, col), self.cy(row)
        ww, hh = SIZE[kind]
        val = label
        if kind in STEREO:
            mark = " &#8916;" if kind == "call" else ""
            val = f"<font style='font-size:10px'>{STEREO[kind]}</font><br>{label}{mark}"
        self.v(id, val, ST[kind], cx - ww / 2, cy - hh / 2, ww, hh)

    def lane_left(self, lane, off):
        return self.lanes[lane][0] + off

    def lane_right(self, lane, off):
        lx, lw, _, _ = self.lanes[lane]
        return lx + lw - off

    def finish(self):
        lane_cells = []
        for key, (lx, lw, cols, label) in self.lanes.items():
            lane_cells.append(f'<mxCell id="{self.P}lane-{key}" value="{esc(label)}" style="{LANE}" vertex="1" parent="1">'
                              f'<mxGeometry x="{lx:.0f}" y="{self.LANE_Y}" width="{lw:.0f}" height="{self.body_h:.0f}" as="geometry"/></mxCell>')
        self.cells = lane_cells + self.cells  # lajur di belakang semua node
        self.w = self.total_w + 40
        self.h = self.LANE_Y + self.body_h + 20


LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §3.2): «user» = aktor memakai sistem; «service» = dikerjakan sistem otomatis; "
          "«manual» = di luar sistem; «call behavior» (simbol garpu) = memanggil activity lain di modul ini; ◇ = keputusan/"
          "gabungan, kondisi ditulis [guard] di panah; ⧗ = menunggu kejadian atau waktu. Gaya polos hitam-putih (CLAUDE.md bagian 5).")
SRC = ("Sumber: kebutuhan-sdm.md (KF-SDM-01–43), brief-sdm.md (cakupan Inti + Pelengkap), kontrak-core-sdm.md, analisis PKG-04/10/14. "
       "Draf 14 Nov 2026, direvisi 17 Nov 2026 (pengesahan dokumen SDM digambar sendiri, gaya hitam-putih) · Zahir")
CALL = "Sahkan dokumen SDM (A4)"

pages, notes = [], []

# ------------------------------------------------------------------ A1
a = Activity("sdm-act-a1", "Activity TO-BE (1-4) - Seleksi dan Penugasan Petugas", "sdm-act-a1-",
             [("k", "KaLab", 460, 2), ("l", "Laboran / PLP", 220, 1), ("s", "Sistem", 220, 1),
              ("x", "Penyetuju pengecualian (di luar sistem)", 220, 1)],
             rows=14, small={0, 2, 4, 6, 8, 11, 13})
a.n("st", "k", 0, "start", col=1)
a.n("kb", "k", 1, "user", "Tetapkan kebutuhan petugas", col=1)
a.n("m0", "k", 2, "merge", col=1)
a.n("sc", "k", 3, "manual", "Seleksi calon asisten", col=1)
a.n("d1", "k", 4, "dec", col=1)
a.n("f0", "k", 4, "final", col=0)
a.n("sp", "x", 5, "manual", "Setujui pengecualian syarat")
a.n("m1", "l", 6, "merge")
a.n("ch", "l", 7, "user", "Catat hasil seleksi")
a.n("bp", "s", 7, "service", "Buat personel asisten")
a.n("d2", "l", 8, "dec")
a.n("su", "l", 9, "user", "Susun surat tugas")
a.n("a4", "l", 10, "call", CALL)
a.n("m2", "l", 11, "merge")
a.n("d3", "l", 12, "dec")
a.n("rv", "k", 12, "user", "Buat revisi surat tugas", col=0)
a.n("en", "l", 13, "final")
a.e("1", "st", "kb"); a.e("2", "kb", "m0"); a.e("3", "m0", "sc"); a.e("4", "sc", "d1")
a.e("5", "d1", "f0", "[tidak lulus]", exit=(0, 0.5), entry=(1, 0.5))
a.e("6", "d1", "sp", "[lulus dengan pengecualian]", [(a.cx("x", None), a.cy(4))], exit=(1, 0.5), entry=(0.5, 0))
a.e("7", "d1", "m1", "[lulus]", [(a.cx("k", 1), a.cy(6))], exit=(0.5, 1), entry=(0, 0.5))
a.e("8", "sp", "m1", "", [(a.cx("x", None), a.cy(6))], exit=(0.5, 1), entry=(1, 0.5))
a.e("9", "m1", "ch"); a.e("10", "ch", "bp", exit=(1, 0.5), entry=(0, 0.5))
a.e("11", "bp", "d2", "", [(a.cx("s", None), a.cy(8))], exit=(0.5, 1), entry=(1, 0.5))
a.e("12", "d2", "m0", "[masih ada calon]", [(a.lane_left("l", 12), a.cy(8)), (a.lane_left("l", 12), a.cy(2))],
    exit=(0, 0.5), entry=(1, 0.5))
a.e("13", "d2", "su", "[seleksi selesai]"); a.e("14", "su", "a4"); a.e("15", "a4", "m2"); a.e("16", "m2", "d3")
a.e("17", "d3", "rv", "[perlu pengganti]", exit=(0, 0.5), entry=(1, 0.5))
a.e("18", "rv", "m2", "", [(a.cx("k", 0), a.cy(11))], exit=(0.5, 0), entry=(0, 0.5))
a.e("19", "d3", "en", "[periode berakhir]")
a.finish()
pages.append(a)
notes.append(("A1 · Seleksi Asisten dan Penugasan Petugas Praktikum (PKG-04), satu periode", [
    ("<b>Kaitan ke PKG-04</b><br>S1 kebutuhan: <i>Tetapkan kebutuhan petugas</i> (KF-SDM-09)<br>"
     "S2 penugasan sah: <i>Susun surat tugas</i> + <i>Sahkan dokumen SDM (A4)</i> (KF-SDM-10, 06, 11, 43)<br>"
     "S3 kompetensi: Bukti Kompetensi (CRUDL, KF-SDM-03), dicek sistem<br>"
     "S4 syarat internal: <i>Catat hasil seleksi</i> (KF-SDM-07, 08)<br>"
     "Status S1–S4 per sesi <b>dihitung saat dibaca</b> (KF-SDM-12), bukan tugas.", 120),
    ("<b>Surat tugas</b> berisi baris asisten → kelas dan laboran → ruang, dengan rentang berlaku. "
     "<i>Buat revisi surat tugas</i> (pengganti) = Pelengkap (KF-SDM-14). Calon yang <b>tidak lulus</b> tidak dicatat; "
     "seleksinya sendiri di luar sistem (POB 2025).", 80),
    ("<b>[KONFIRMASI]</b> K7: pengesah surat tugas. KB-3: surat tugas <b>ditolak</b> saat diajukan bila ada asisten tanpa "
     "seleksi lulus (default). K2: penyetuju pengecualian (Koor Prodi atau KaLab).", 70),
]))

# ------------------------------------------------------------------ A2
b = Activity("sdm-act-a2", "Activity TO-BE (2-4) - Otorisasi Personel", "sdm-act-a2-",
             [("k", "KaLab", 220, 1), ("l", "Laboran / PLP (penilai, pencatat)", 440, 2), ("s", "Sistem", 220, 1)],
             rows=17, small={0, 2, 3, 8, 11, 12, 14, 16})
b.n("st", "k", 0, "start")
b.n("tp", "k", 1, "user", "Tetapkan pelaksana tugas/alat")
b.n("d1", "l", 2, "dec", col=0)
b.n("m0", "l", 3, "merge", col=0)
b.n("uj", "l", 4, "manual", "Uji keterampilan personel", col=0)
b.n("ca", "l", 5, "user", "Catat asesmen keterampilan", col=0)
b.n("d2", "l", 6, "dec", col=0)
b.n("pg", "l", 6, "manual", "Ikuti pengembangan kompetensi", col=1)
b.n("bk", "s", 7, "service", "Buat bukti kompetensi")
b.n("m1", "k", 8, "merge")
b.n("so", "k", 9, "user", "Susun otorisasi")
b.n("a4", "k", 10, "call", CALL)
b.n("m2", "s", 11, "merge")
b.n("te", "s", 12, "time", "Muncul pemicu")
b.n("ce", "l", 13, "user", "Catat evaluasi ulang otorisasi", col=0)
b.n("d3", "l", 14, "dec", col=0)
b.n("cb", "k", 15, "user", "Cabut otorisasi")
b.n("en", "k", 16, "final")
b.e("1", "st", "tp")
b.e("2", "tp", "d1", "", [(b.cx("k", None), b.cy(2))], exit=(0.5, 1), entry=(0, 0.5))
b.e("3", "d1", "m0", "[belum ada bukti berlaku]")
b.e("4", "d1", "m1", "[bukti kompetensi berlaku ada]", [(b.lane_right("l", 10), b.cy(2)), (b.lane_right("l", 10), b.cy(8) - 6)],
    exit=(1, 0.5), entry=(1, 0.3), lx=-0.75)
b.e("5", "m0", "uj"); b.e("6", "uj", "ca"); b.e("7", "ca", "d2")
b.e("8", "d2", "pg", "[belum layak]", exit=(1, 0.5), entry=(0, 0.5))
b.e("9", "pg", "m0", "", [(b.cx("l", 1), b.cy(3))], exit=(0.5, 0), entry=(1, 0.5))
b.e("10", "d2", "bk", "[layak]", [(b.cx("l", 0), b.cy(7))], exit=(0.5, 1), entry=(0, 0.5))
b.e("11", "bk", "m1", "", [(b.cx("s", None), b.cy(8) + 6)], exit=(0.5, 1), entry=(1, 0.7))
b.e("12", "m1", "so"); b.e("13", "so", "a4")
b.e("14", "a4", "m2", "", [(b.cx("k", None), b.cy(11) - 6)], exit=(0.5, 1), entry=(0, 0.3))
b.e("15", "m2", "te")
b.e("16", "te", "ce", "", [(b.cx("s", None), b.cy(13))], exit=(0.5, 1), entry=(1, 0.5))
b.e("17", "ce", "d3")
b.e("18", "d3", "m1", "[diperpanjang / dibatasi / naik level]", [(b.lane_left("k", 12), b.cy(14)), (b.lane_left("k", 12), b.cy(8))],
    exit=(0, 0.5), entry=(0, 0.5), lx=-0.6)
b.e("19", "d3", "m2", "[tetap berlaku]", [(b.cx("l", 1), b.cy(14)), (b.cx("l", 1), b.cy(11) + 6)], exit=(1, 0.5), entry=(0, 0.7))
b.e("20", "d3", "cb", "[dicabut]", [(b.cx("l", 0), b.cy(15))], exit=(0.5, 1), entry=(1, 0.5))
b.e("21", "cb", "en")
b.finish()
pages.append(b)
notes.append(("A2 · Otorisasi PLP/Laboran untuk Tugas/Alat Berkewenangan Khusus (PKG-10)", [
    ("<b>Kaitan ke PKG-10</b><br>Penyebut: <i>Tetapkan pelaksana tugas/alat</i> (KF-SDM-18, 19)<br>"
     "S1 kompetensi: <i>Catat asesmen</i> / bukti yang ada (KF-SDM-20, 21)<br>"
     "S2 otorisasi berlaku: <i>Susun otorisasi</i> + <i>Sahkan dokumen SDM (A4)</i> (KF-SDM-22, 23, 24)<br>"
     "S3 pemula disupervisi: kelengkapan saat diajukan (KF-SDM-23)<br>"
     "S4 evaluasi ulang: <i>Catat evaluasi ulang</i> (KF-SDM-25)<br>"
     "Status S1–S4 per pasangan dihitung saat dibaca (KF-SDM-26).", 130),
    ("<b>Otorisasi lama diganti</b> di dalam A4 (<i>Ganti status dokumen lama</i>): otorisasi berlaku untuk pasangan "
     "personel × tugas/alat yang sama menjadi Diganti (KF-SDM-24).<br>"
     "⧗ Pemicu (masa berlaku habis, alat berubah, insiden, lama tidak aktif) dicatat manual; <b>tidak ada penjadwal</b> "
     "(kontrak Core K-3).", 90),
    ("<b>Temuan</b> (tabel status × transisi S2): keputusan <i>tetap berlaku</i> belum ada di KF-SDM-25. "
     "<b>[KONFIRMASI]</b> KP-1 (keputusan <i>tetap berlaku</i>); KU-1 (pemicu dan keputusan di hari berbeda; use case sudah dipecah dua); "
     "KB-1 (penyebut = pelaksana yang ditetapkan KaLab).", 80),
]))

# ------------------------------------------------------------------ A3
c = Activity("sdm-act-a3", "Activity TO-BE (3-4) - Siklus Pelatihan PLP", "sdm-act-a3-",
             [("k", "KaLab", 220, 1), ("l", "Laboran / PLP (peserta, pencatat)", 440, 2), ("s", "Sistem", 220, 1)],
             rows=17, small={0, 5, 6, 11, 14, 15, 16})
c.n("st", "k", 0, "start")
c.n("br", "k", 1, "user", "Buat rencana pelatihan")
c.n("ik", "s", 1, "service", "Isi kebutuhan dari matriks kompetensi")
c.n("lk", "k", 2, "user", "Lengkapi kebutuhan kompetensi")
c.n("si", "k", 3, "user", "Susun item pelatihan")
c.n("a4", "k", 4, "call", CALL)
c.n("m1", "l", 5, "merge", col=0)
c.n("te", "l", 6, "time", "Jadwal item tiba", col=0)
c.n("d1", "l", 7, "dec", col=0)
c.n("tb", "k", 7, "user", "Tandai item batal")
c.n("ip", "l", 8, "manual", "Ikuti pelatihan", col=0)
c.n("cr", "l", 9, "user", "Catat realisasi pelatihan", col=0)
c.n("tk", "l", 10, "manual", "Terapkan keterampilan di pekerjaan", col=0)
c.n("t2", "l", 11, "time", "Waktu evaluasi tiba", col=0)
c.n("ce", "l", 12, "user", "Catat evaluasi efektivitas", col=0)
c.n("d2", "l", 13, "dec", col=0)
c.n("bk", "s", 13, "service", "Buat bukti kompetensi")
c.n("m3", "l", 14, "merge", col=0)
c.n("d3", "l", 15, "dec", col=0)
c.n("en", "l", 16, "final", col=0)
c.e("1", "st", "br")
c.e("2", "br", "ik", exit=(1, 0.5), entry=(0, 0.5))
c.e("3", "ik", "lk", "", [(c.cx("s", None), c.cy(2))], exit=(0.5, 1), entry=(1, 0.5))
c.e("4", "lk", "si"); c.e("5", "si", "a4")
c.e("6", "a4", "m1", "", [(c.cx("k", None), c.cy(5))], exit=(0.5, 1), entry=(0, 0.5))
c.e("7", "m1", "te"); c.e("8", "te", "d1")
c.e("9", "d1", "tb", "[batal]", exit=(0, 0.5), entry=(1, 0.5))
c.e("10", "d1", "ip", "[terlaksana]")
c.e("11", "tb", "m3", "", [(c.cx("k", None), c.cy(14))], exit=(0.5, 1), entry=(0, 0.5))
c.e("12", "ip", "cr"); c.e("13", "cr", "tk"); c.e("14", "tk", "t2"); c.e("15", "t2", "ce"); c.e("16", "ce", "d2")
c.e("17", "d2", "bk", "[efektif]", exit=(1, 0.5), entry=(0, 0.5))
c.e("18", "d2", "m3", "[perlu pengembangan]")
c.e("19", "bk", "m3", "", [(c.cx("s", None), c.cy(14))], exit=(0.5, 1), entry=(1, 0.5))
c.e("20", "m3", "d3")
c.e("21", "d3", "m1", "[masih ada item terjadwal]", [(c.lane_right("l", 20), c.cy(15)), (c.lane_right("l", 20), c.cy(5))],
    exit=(1, 0.5), entry=(1, 0.5))
c.e("22", "d3", "en", "[semua item selesai / batal]")
c.finish()
pages.append(c)
notes.append(("A3 · Siklus Pelatihan PLP/Laboran (PKG-14), satu tahun", [
    ("<b>Kaitan ke PKG-14</b><br>K1: <i>Buat rencana</i>, <i>Isi kebutuhan</i>, <i>Lengkapi kebutuhan</i>, "
     "<i>Sahkan dokumen SDM (A4)</i> (KF-SDM-29, 30, 32)<br>K2: <i>Susun item pelatihan</i> (KF-SDM-31), dicek saat diajukan<br>"
     "K3: <i>Catat realisasi</i> + bukti penerapan (KF-SDM-33)<br>"
     "K4: <i>Catat evaluasi efektivitas</i>, <i>Buat bukti kompetensi</i> (KF-SDM-34, 35)<br>"
     "Kriteria tertinggi dihitung saat dibaca (KF-SDM-36).", 120),
    ("<b>Pembekuan kebutuhan</b> terjadi di A4 saat rencana diajukan (KF-SDM-32). <i>Tandai item batal</i> = Pelengkap "
     "(KF-SDM-37). <b>Siklus berikutnya</b>: bukti kompetensi baru mengubah matriks, sehingga kebutuhan tahun depan ikut "
     "diperbarui (K4).", 80),
    ("<b>[KONFIRMASI]</b> K10: pengesah rencana pelatihan (KaLab / Wadek Bidang Keuangan dan Umum). "
     "Wawancara no. 12: kapan dan oleh siapa efektivitas dinilai. KU-2: revisi rencana setelah disahkan tidak dirancang.", 70),
]))

# ------------------------------------------------------------------ A4
d = Activity("sdm-act-a4", "Activity TO-BE (4-4) - Pengesahan Dokumen SDM", "sdm-act-a4-",
             [("p", "Penyusun (KaLab / Laboran)", 240, 1), ("s", "Sistem", 220, 1),
              ("k", "KaLab (pencatat pengesahan)", 220, 1), ("g", "Pejabat penanda tangan (di luar sistem)", 220, 1)],
             rows=19, small={0, 1, 5, 7, 11, 14, 18})
d.n("st", "p", 0, "start")
d.n("m0", "p", 1, "merge")
d.n("aj", "p", 2, "user", "Ajukan dokumen SDM")
d.n("kl", "s", 2, "service", "Periksa kelengkapan dokumen")
d.n("lk", "p", 3, "user", "Lengkapi isi dokumen")
d.n("d1", "s", 3, "dec")
d.n("cp", "s", 4, "service", "Ubah status menjadi Diajukan")
d.n("d2", "s", 5, "dec")
d.n("tr", "p", 6, "user", "Terbitkan dokumen PDF")
d.n("hp", "s", 6, "service", "Hasilkan PDF dari isi dokumen")
d.n("m2", "p", 7, "merge")
d.n("ct", "p", 8, "manual", "Cetak dokumen")
d.n("td", "g", 8, "manual", "Tinjau isi dokumen cetak")
d.n("kb", "k", 9, "user", "Kembalikan dokumen")
d.n("d3", "g", 9, "dec")
d.n("pb", "p", 10, "user", "Perbaiki dokumen")
d.n("u1", "s", 10, "service", "Ubah status menjadi Draf")
d.n("tt", "g", 10, "manual", "Tanda tangani dokumen")
d.n("m3", "p", 11, "merge")
d.n("ug", "p", 12, "user", "Unggah PDF bertanda tangan")
d.n("sh", "k", 12, "user", "Sahkan dokumen")
d.n("vl", "s", 13, "service", "Periksa berkas dan wewenang pengesah")
d.n("d4", "s", 14, "dec")
d.n("us", "s", 15, "service", "Ubah status menjadi Disahkan")
d.n("gv", "s", 16, "service", "Ganti status dokumen lama")
d.n("cr", "s", 17, "service", "Catat riwayat pengesahan")
d.n("en", "s", 18, "final")
cp_, cs_ = d.cx("p", None), d.cx("s", None)
d.e("1", "st", "m0"); d.e("2", "m0", "aj")
d.e("3", "aj", "kl", exit=(1, 0.5), entry=(0, 0.5)); d.e("4", "kl", "d1")
d.e("5", "d1", "lk", "[belum lengkap]", exit=(0, 0.5), entry=(1, 0.5))
d.e("6", "lk", "m0", "", [(d.lane_left("p", 12), d.cy(3)), (d.lane_left("p", 12), d.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
d.e("7", "d1", "cp", "[lengkap]"); d.e("8", "cp", "d2")
d.e("9", "d2", "tr", "[surat tugas / rencana pelatihan]", [(cp_, d.cy(5))], exit=(0, 0.5), entry=(0.5, 0))
d.e("10", "tr", "hp", exit=(1, 0.5), entry=(0, 0.5))
d.e("11", "hp", "m2", "", [(cs_, d.cy(6.85)), (cp_, d.cy(6.85))], exit=(0.5, 1), entry=(0.5, 0))
d.e("12", "d2", "m2", "[otorisasi]", [(d.lane_right("s", 12), d.cy(5)), (d.lane_right("s", 12), d.cy(7))],
    exit=(1, 0.5), entry=(0.5, 1))
d.e("13", "m2", "ct")
d.e("14", "ct", "td", exit=(1, 0.5), entry=(0, 0.5)); d.e("15", "td", "d3")
d.e("16", "d3", "kb", "[tidak disetujui]", exit=(0, 0.5), entry=(1, 0.5))
d.e("17", "kb", "u1", "", [(d.cx("k", None), d.cy(10))], exit=(0.5, 1), entry=(1, 0.5))
d.e("18", "u1", "pb", exit=(0, 0.5), entry=(1, 0.5))
d.e("19", "pb", "m0", "", [(d.lane_left("p", 24), d.cy(10)), (d.lane_left("p", 24), d.cy(1) + 6)], exit=(0, 0.5), entry=(0, 0.75))
d.e("20", "d3", "tt", "[disetujui]")
d.e("21", "tt", "m3", "", [(d.cx("g", None), d.cy(10.85)), (cp_, d.cy(10.85))], exit=(0.5, 1), entry=(0.5, 0))
d.e("22", "m3", "ug")
d.e("23", "ug", "sh", exit=(1, 0.5), entry=(0, 0.5))
d.e("24", "sh", "vl", "", [(d.cx("k", None), d.cy(13))], exit=(0.5, 1), entry=(1, 0.5))
d.e("25", "vl", "d4")
d.e("26", "d4", "m3", "[tidak valid]", [(d.lane_left("s", 8), d.cy(14)), (d.lane_left("s", 8), d.cy(11))],
    exit=(0, 0.5), entry=(1, 0.5))
d.e("27", "d4", "us", "[valid]"); d.e("28", "us", "gv"); d.e("29", "gv", "cr"); d.e("30", "cr", "en")
d.finish()
pages.append(d)
notes.append(("A4 · Pengesahan Dokumen SDM: Surat Tugas, Otorisasi, Rencana Pelatihan (dipanggil A1, A2, A3)", [
    ("<b>Periksa kelengkapan dokumen</b>, isinya per jenis: Surat Tugas = ≥1 baris lengkap dan setiap asisten punya seleksi "
     "lulus (KF-SDM-11); Otorisasi = kompetensi terbukti, lingkup terisi, supervisor berwenang bila terbimbing (KF-SDM-23); "
     "Rencana Pelatihan = semua PLP/teknisi tercantum dan item lengkap, lalu <b>kebutuhan dibekukan</b> (KF-SDM-32).", 100),
    ("<b>Periksa berkas dan wewenang</b>: PDF bertanda tangan harus ada dan pengesah tercatat harus memegang jabatan yang "
     "berwenang untuk jenis dokumen itu (KF-SDM-43). <b>Ganti status dokumen lama</b>: surat tugas yang direvisi, atau "
     "otorisasi berlaku untuk pasangan yang sama, menjadi Diganti (KF-SDM-14, 24). Setiap kejadian dicatat sebagai riwayat (KF-SDM-06).", 100),
    ("<b>Terbitkan dokumen PDF</b> hanya untuk Surat Tugas dan Rencana Pelatihan, lapis Pelengkap (KF-SDM-17, 39). "
     "Otorisasi disiapkan di luar sistem. <b>Pejabat penanda tangan bukan aktor</b>: KaLab, Wadek, atau Koor Prodi; "
     "bila KaLab sendiri, lajur KaLab dan lajur pejabat diperankan orang yang sama. Mekanisme teknis: "
     "<code>labfik.approval.mixin</code> (Core).", 100),
    ("Status dokumen di alur ini: <b>S1</b> (Otorisasi) dan <b>S4</b> (Surat Tugas, Rencana Pelatihan). "
     "Pencabutan dokumen yang berlaku: A2 <i>Cabut otorisasi</i>, S1, S4.", 50),
]))

# ------------------------------------------------------------------ state machines
STATE = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
COMP = ("swimlane;rounded=1;arcSize=6;html=1;startSize=30;fontStyle=1;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;"
        "swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;" + FONT)
TR = ("endArrow=open;endSize=8;html=1;rounded=1;fontSize=11;labelBackgroundColor=#FFFFFF;strokeColor=#000000;"
      "edgeStyle=orthogonalEdgeStyle;" + FONT)
KET = "text;html=1;fontSize=11;align=left;" + FONT
STAR = "* transisi yang ditemukan melalui tabel status × transisi (proses-bisnis-sdm.md bagian 4)"
SM_NOTE = ("<b>Notasi</b> (Wazlawick 2024, §3.3): <code>event [guard] / efek</code>. Status akhir = status yang berpanah ke ◉. "
           "Tanda * = transisi yang baru ditemukan lewat tabel status × transisi. Kotak bertajuk = status komposit.")

# S1 Otorisasi
s1 = Page("sdm-stm-s1", "State Machine TO-BE (1-4) - Otorisasi", "sdm-stm-s1-")
s1.v("init", "", ST["start"], 30, 228, 22, 22)
s1.v("draf", "Draf", STATE, 100, 214, 140, 50)
s1.v("aju", "Diajukan", STATE, 440, 214, 140, 50)
s1.v("sah", "Disahkan", COMP, 880, 100, 400, 280)
s1.v("ini2", "", ST["start"], 910, 240, 22, 22)
s1.v("brl", "Berlaku", STATE, 980, 226, 120, 50)
s1.v("lwt", "Lewat masa berlaku", STATE, 1120, 316, 140, 50)
s1.v("gnt", "Diganti", STATE, 1500, 110, 140, 50)
s1.v("cbt", "Dicabut", STATE, 1500, 320, 140, 50)
s1.v("f0", "", ST["final"], 157, 380, 26, 26)
s1.v("f1", "", ST["final"], 1690, 122, 26, 26)
s1.v("f2", "", ST["final"], 1690, 332, 26, 26)
s1.e("t0", "init", "draf", "buat", style=TR)
s1.e("t1", "draf", "aju", "ajukan [kompetensi terbukti ∧ lingkup terisi<br>∧ supervisor berwenang bila terbimbing]<br>/ catat riwayat",
     style=TR, exit=(1, 0.3), entry=(0, 0.3))
s1.e("t2", "aju", "draf", "kembalikan / catat alasan", style=TR, exit=(0, 0.75), entry=(1, 0.75))
s1.e("t2b", "aju", "aju", "unggah berkas bertanda tangan / catat riwayat", [(475, 170), (545, 170)], style=TR,
     exit=(0.25, 0), entry=(0.75, 0))
s1.e("t3", "aju", "sah", "sahkan [berkas ada ∧ pengesah berwenang]<br>/ catat pengesah; otorisasi lama<br>pasangan sama → Diganti",
     style=TR, exit=(1, 0.5), entry=(0, 0.48))
s1.e("t4", "ini2", "brl", "", style=TR)
s1.e("t5", "brl", "lwt", "when(hari ini &gt; berlaku_sampai) *", [(1040, 341)], style=TR, exit=(0.5, 1), entry=(0, 0.5))
s1.e("t6", "sah", "gnt", "otorisasi baru pasangan sama disahkan", style=TR, exit=(1, 0.2), entry=(0, 0.5))
s1.e("t7", "sah", "cbt", "cabut [evaluasi ulang: dicabut]<br>/ catat alasan", style=TR, exit=(1, 0.79), entry=(0, 0.5))
s1.e("t8", "draf", "f0", "hapus [belum pernah diajukan]", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s1.e("tf1", "gnt", "f1", style=TR); s1.e("tf2", "cbt", "f2", style=TR)
s1.v("ket", STAR, KET, 30, 420, 600, 24)
s1.w, s1.h = 1760, 460
pages.append(s1)
notes.append(("S1 · Otorisasi Personel (labfik.sdm.otorisasi): approval.mixin + masa berlaku sendiri", [
    (SM_NOTE, 60),
    ("<b>Berlaku / Lewat masa berlaku</b> adalah transisi stabil (§9.3.1): tidak disimpan di <code>state</code>, tetapi "
     "dihitung dari <code>berlaku_sampai</code> (<code>is_berlaku</code>). Tidak ada status <i>Kedaluwarsa</i> dan tidak ada "
     "penjadwal, karena Otorisasi tidak memakai <code>period.mixin</code> (kontrak Core K-3). PKG-10 S2 hanya terpenuhi di "
     "sub-status <b>Berlaku</b>.", 100),
    ("<b>Temuan</b>: otorisasi yang <code>berlaku_sampai</code>-nya sudah lewat sebelum disahkan langsung masuk <i>Lewat masa "
     "berlaku</i>; kandidat aturan bisnis <code>berlaku_sampai ≥ hari ini</code> saat diajukan (langkah 7). "
     "<b>[ASUMSI]</b> Diganti dan Dicabut adalah status akhir; perubahan lingkup, level, atau masa berlaku dibuat sebagai "
     "otorisasi baru (<i>superseding</i>, §11.9.2).", 90),
]))

# S2 Evaluasi Ulang Otorisasi
s2 = Page("sdm-stm-s2", "State Machine TO-BE (2-4) - Evaluasi Ulang Otorisasi", "sdm-stm-s2-")
s2.v("init", "", ST["start"], 30, 158, 22, 22)
s2.v("trb", "Terbuka", STATE, 130, 144, 140, 50)
s2.v("ptn", "Diputuskan", STATE, 680, 144, 140, 50)
s2.v("f1", "", ST["final"], 900, 156, 26, 26)
s2.e("t0", "init", "trb", "catat pemicu", style=TR)
s2.e("t1", "trb", "ptn", "putuskan [keputusan ∈ {diperpanjang, dibatasi, naik level}]<br>/ susun otorisasi baru (A2)",
     style=TR, exit=(1, 0.3), entry=(0, 0.3))
s2.e("t2", "trb", "ptn", "putuskan [keputusan = dicabut] / cabut otorisasi", [(200, 260), (750, 260)],
     style=TR, exit=(0.5, 1), entry=(0.5, 1))
s2.e("t3", "trb", "ptn", "putuskan [keputusan = tetap berlaku] *", [(200, 80), (750, 80)],
     style=TR, exit=(0.5, 0), entry=(0.5, 0))
s2.e("tf", "ptn", "f1", style=TR)
s2.v("ket", STAR, KET, 30, 300, 600, 24)
s2.w, s2.h = 980, 340
pages.append(s2)
notes.append(("S2 · Evaluasi Ulang Otorisasi (labfik.sdm.evaluasi.otorisasi), PKG-10 S4", [
    ("<b>PKG-10 S4</b> gagal selama ada evaluasi ulang berstatus <b>Terbuka</b> pada pasangan itu (KF-SDM-26). "
     "Status ini field <code>status</code> milik model evaluasi ulang.", 60),
    ("<b>Temuan</b>: keputusan <i>tetap berlaku</i> tidak ada di analisis PKG-10 dan KF-SDM-25. Tanpa keputusan itu, "
     "pemicu yang tidak butuh perubahan (mis. alat diganti, kompetensi tetap memadai) membuat evaluasi terbuka selamanya "
     "<b>[KONFIRMASI KP-1]</b>. <b>[ASUMSI]</b> Keputusan yang berubah dicatat sebagai evaluasi ulang baru (rekaman bukti tidak dihapus).", 90),
]))

# S3 Item Pelatihan
s3 = Page("sdm-stm-s3", "State Machine TO-BE (3-4) - Item Pelatihan", "sdm-stm-s3-")
s3.v("init", "", ST["start"], 30, 218, 22, 22)
s3.v("rnc", "Direncanakan", STATE, 110, 204, 150, 50)
s3.v("tl", "Terlaksana", COMP, 520, 90, 420, 250)
s3.v("ini2", "", ST["start"], 550, 208, 22, 22)
s3.v("mnv", "Menunggu evaluasi", STATE, 620, 194, 140, 50)
s3.v("dev", "Dievaluasi", STATE, 790, 280, 120, 50)
s3.v("btl", "Batal", STATE, 110, 390, 150, 50)
s3.v("f0", "", ST["final"], 360, 100, 26, 26)
s3.v("f1", "", ST["final"], 172, 490, 26, 26)
s3.v("f2", "", ST["final"], 1010, 202, 26, 26)
s3.e("t0", "init", "rnc", "tambah item [rencana Draf]", style=TR)
s3.e("t1", "rnc", "tl", "catat realisasi [rencana Disahkan]<br>(peserta pertama)", style=TR, exit=(1, 0.5), entry=(0, 0.53))
s3.e("t2", "rnc", "btl", "tandai batal [alasan diisi]", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s3.e("t3", "rnc", "f0", "hapus item [rencana masih Draf] *", [(185, 113)], style=TR, exit=(0.5, 0), entry=(0, 0.5))
s3.e("t4", "ini2", "mnv", "", style=TR)
s3.e("t5", "mnv", "dev", "when(setiap realisasi punya<br>evaluasi efektivitas)", [(690, 305)], style=TR,
     exit=(0.5, 1), entry=(0, 0.5))
s3.e("tf1", "btl", "f1", style=TR); s3.e("tf2", "tl", "f2", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s3.v("ket", STAR, KET, 30, 540, 600, 24)
s3.w, s3.h = 1080, 580
pages.append(s3)
notes.append(("S3 · Item Pelatihan dalam Rencana Pelatihan (labfik.sdm.item.pelatihan), PKG-14 K3–K4", [
    ("<b>Kaitan ke PKG-14</b>: K3 dihitung dari item <b>Terlaksana</b> yang setiap pesertanya punya realisasi dan bukti "
     "penerapan; item <b>Batal</b> tidak dihitung (KF-SDM-37, Pelengkap). K4 dihitung dari item <b>Dievaluasi</b>. "
     "Sub-status Terlaksana dihitung dari data (§9.3.1); yang disimpan hanya <i>rencana / terlaksana / batal</i>.", 100),
    ("<b>[ASUMSI]</b> Batal adalah status akhir; item tidak bisa batal setelah ada realisasi. Pelatihan pengganti masuk "
     "rencana tahun berikutnya; revisi rencana setelah disahkan tidak dirancang <b>[KONFIRMASI KU-2]</b>.", 70),
]))

# S4 Surat Tugas dan Rencana Pelatihan
s4 = Page("sdm-stm-s4", "State Machine TO-BE (4-4) - Surat Tugas dan Rencana Pelatihan", "sdm-stm-s4-")
s4.v("init", "", ST["start"], 30, 168, 22, 22)
s4.v("draf", "Draf", STATE, 100, 154, 140, 50)
s4.v("aju", "Diajukan", STATE, 470, 154, 140, 50)
s4.v("sah", "Disahkan", STATE, 880, 154, 140, 50)
s4.v("gnt", "Diganti", STATE, 1210, 54, 140, 50)
s4.v("cbt", "Dicabut", STATE, 1210, 254, 140, 50)
s4.v("f0", "", ST["final"], 157, 300, 26, 26)
s4.v("f1", "", ST["final"], 1400, 66, 26, 26)
s4.v("f2", "", ST["final"], 1400, 266, 26, 26)
s4.e("t0", "init", "draf", "buat", style=TR)
s4.e("t1", "draf", "aju", "ajukan [kelengkapan per jenis]<br>/ catat riwayat; rencana: bekukan kebutuhan", style=TR,
     exit=(1, 0.3), entry=(0, 0.3))
s4.e("t2", "aju", "draf", "kembalikan / catat alasan", style=TR, exit=(0, 0.75), entry=(1, 0.75))
s4.e("t3", "aju", "aju", "unggah berkas bertanda tangan / catat riwayat", [(505, 110), (575, 110)], style=TR,
     exit=(0.25, 0), entry=(0.75, 0))
s4.e("t4", "aju", "sah", "sahkan [berkas ada ∧ pengesah berwenang]<br>/ catat pengesah, pencatat, tanggal sah",
     style=TR, exit=(1, 0.5), entry=(0, 0.5))
s4.e("t5", "sah", "gnt", "revisi surat tugas disahkan<br>[surat tugas]", [(950, 79)], style=TR, exit=(0.5, 0), entry=(0, 0.5))
s4.e("t6", "sah", "cbt", "cabut / catat alasan", [(950, 279)], style=TR, exit=(0.5, 1), entry=(0, 0.5))
s4.e("t7", "draf", "f0", "hapus [belum pernah diajukan]", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s4.e("tf1", "gnt", "f1", style=TR); s4.e("tf2", "cbt", "f2", style=TR)
s4.w, s4.h = 1460, 360
pages.append(s4)
notes.append(("S4 · Surat Tugas dan Rencana Pelatihan (labfik.sdm.surat.tugas, labfik.sdm.rencana.pelatihan): approval.mixin", [
    ("<b>Kelengkapan per jenis</b>: lihat catatan A4. Pada Rencana Pelatihan, pengajuan sekaligus membekukan daftar kebutuhan "
     "(KF-SDM-32). <b>Diganti</b> hanya untuk Surat Tugas yang direvisi (Pelengkap, KF-SDM-14); revisi Rencana Pelatihan tidak "
     "dirancang (KU-2).", 80),
    ("<b>Tanpa status Kedaluwarsa</b>: modul SDM tidak memakai penjadwal (kontrak Core K-3). Rencana Pelatihan yang periodenya "
     "sudah lewat tetap <i>Disahkan</i>; \"masih berlaku\" untuk K1 dihitung dari periode (<code>period.mixin.is_berlaku</code>). "
     "<b>[ASUMSI]</b> Diganti dan Dicabut adalah status akhir.", 90),
]))

# ------------------------------------------------------------------ halaman catatan (bahan kerja, tidak masuk naskah)
cat = Page("sdm-act-notes", "Catatan TO-BE (bahan kerja) - Activity dan State Machine", "sdm-act-notes-")
cat.v("title", "Catatan diagram activity dan state machine modul SDM (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 16, 1240, 36)
cat.v("legend", LEGEND, NOTE, 40, 60, 1260, 60)
cat.v("src", SRC, NOTE, 40, 132, 1260, 40)
col_w, x0, y0, row_h = 400, 40, 190, 540
for i, (head, items) in enumerate(notes):
    x = x0 + (i % 3) * (col_w + 30)
    y = y0 + (i // 3) * row_h
    cat.v(f"h{i}", f"<b>{head}</b>", "text;html=1;fontSize=12;align=left;verticalAlign=top;whiteSpace=wrap;", x, y, col_w, 40)
    yy = y + 46
    for j, (txt, h) in enumerate(items):
        cat.v(f"n{i}-{j}", txt, NOTE, x, yy, col_w, h)
        yy += h + 10
cat.w, cat.h = 1340, y0 + ((len(notes) + 2) // 3) * row_h + 40
pages.append(cat)

with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(p.xml() for p in pages) + "</mxfile>")
