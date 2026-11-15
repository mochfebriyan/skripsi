"""Activity + state machine modul SDM & Kompetensi (Langkah 5).

Fungsi gambar disalin dari contoh-tata-kelola/activity_state.py; yang diganti hanya data,
prefiks ID (sdm-), dan warna modul SDM (#EEFAF3 / #4E9A6B).

Jalankan:
    python -I projek-fiklab/tools/drawio/sdm/activity_state.py projek-fiklab/rancangan/activity-state-sdm.drawio
    python -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/activity-state-sdm.drawio sdm-
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]


def esc(s):
    return escape(s, {'"': "&quot;"})


ST = {
    "user": "rounded=1;arcSize=40;whiteSpace=wrap;html=1;fontSize=11;fillColor=#FFFFFF;strokeColor=#333333;",
    "service": "rounded=1;arcSize=40;whiteSpace=wrap;html=1;fontSize=11;fillColor=#EEEEEE;strokeColor=#333333;",
    "manual": "rounded=1;arcSize=40;whiteSpace=wrap;html=1;fontSize=11;fillColor=#FFF8E7;strokeColor=#333333;dashed=1;",
    "call": "rounded=1;arcSize=40;whiteSpace=wrap;html=1;fontSize=11;fillColor=#F5F0FF;strokeColor=#6C4A87;strokeWidth=2;",
    "dec": "rhombus;html=1;fillColor=#FFFFFF;strokeColor=#333333;",
    "merge": "rhombus;html=1;fillColor=#FFFFFF;strokeColor=#333333;",
    "start": "ellipse;html=1;fillColor=#000000;strokeColor=#000000;",
    "final": "ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;",
    "fork": "html=1;fillColor=#000000;strokeColor=none;",
    "time": "shape=collate;html=1;fillColor=#FFFFFF;strokeColor=#333333;labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=6;fontSize=11;",
}
SIZE = {"user": (200, 46), "service": (200, 46), "manual": (200, 46), "call": (200, 50), "dec": (34, 34),
        "merge": (34, 34), "start": (24, 24), "final": (28, 28), "time": (22, 28)}
STEREO = {"user": "«user»", "service": "«service»", "manual": "«manual»", "call": "«call behavior»"}
EDGE = ("endArrow=open;endSize=9;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;fontSize=10;"
        "labelBackgroundColor=#FFFFFF;strokeColor=#333333;")
# Warna modul SDM & Kompetensi (CLAUDE.md bagian 2)
LANE = ("swimlane;html=1;startSize=34;fillColor=#EEFAF3;strokeColor=#4E9A6B;fontStyle=1;fontSize=13;"
        "swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;")
LANE_EXT = ("swimlane;html=1;startSize=34;fillColor=#F2F2F2;strokeColor=#999999;dashed=1;fontStyle=1;fontSize=13;"
            "swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;")
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=18;fontStyle=1;align=left;verticalAlign=middle;"
SRC = "Sumber: kebutuhan-sdm.md (KF-SDM), brief-sdm.md, analisis PKG-04/10/14 · Draf 14 Nov 2026 · Zahir"


class Page:
    def __init__(self, pid, name, prefix):
        self.pid, self.name, self.P = pid, name, prefix
        self.cells, self.w, self.h = [], 1600, 1200

    def v(self, id, val, style, x, y, w, h):
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def e(self, id, s, t, val="", pts=None, style=EDGE, exit=None, entry=None):
        st = style
        if exit:
            st += f"exitX={exit[0]};exitY={exit[1]};exitDx=0;exitDy=0;"
        if entry:
            st += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        geo = '<mxGeometry relative="1" as="geometry">'
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
    ROWH, LANE_Y, HEAD = 74, 70, 34

    def __init__(self, pid, name, prefix, title, lanes):
        super().__init__(pid, name, prefix)
        self.lanes = {}
        x = 40
        for key, label, w, cols, *ext in lanes:
            self.lanes[key] = (x, w, cols, label, bool(ext and ext[0]))
            x += w
        self.total_w = x - 40
        self.v("title", title, TITLE, 40, 16, 1100, 40)
        self.nodes = {}

    def cy(self, row):
        return self.LANE_Y + self.HEAD + 34 + row * self.ROWH

    def cx(self, lane, col):
        lx, lw, cols, _, _ = self.lanes[lane]
        if cols == 1 or col is None:
            return lx + lw / 2
        return lx + lw * (col + 0.5) / cols

    def n(self, id, lane, row, kind, label="", col=None):
        cx, cy = self.cx(lane, col), self.cy(row)
        ww, hh = SIZE[kind]
        val = label
        if kind in STEREO:
            val = f"<font style='font-size:9px' color='#6C4A87'>{STEREO[kind]}</font><br>{label}"
        self.v(id, val, ST[kind], cx - ww / 2, cy - hh / 2, ww, hh)
        self.nodes[id] = (cx, cy, ww, hh)

    def lane_left(self, lane, off):
        return self.lanes[lane][0] + off

    def lane_right(self, lane, off):
        lx, lw, _, _, _ = self.lanes[lane]
        return lx + lw - off

    def finish(self, rows, notes):
        h = self.HEAD + 34 + rows * self.ROWH + 20
        lane_cells = []
        for key, (lx, lw, cols, label, ext) in self.lanes.items():
            lane_cells.append(f'<mxCell id="{self.P}lane-{key}" value="{esc(label)}" style="{LANE_EXT if ext else LANE}" '
                              f'vertex="1" parent="1"><mxGeometry x="{lx:.0f}" y="{self.LANE_Y}" width="{lw:.0f}" '
                              f'height="{h:.0f}" as="geometry"/></mxCell>')
        self.cells = lane_cells + self.cells  # lajur di belakang semua elemen
        nx = 40 + self.total_w + 40
        ny = self.LANE_Y
        for i, (txt, nh) in enumerate(notes):
            self.v(f"note{i}", txt, NOTE, nx, ny, 340, nh)
            ny += nh + 16
        self.w = nx + 380
        self.h = max(self.LANE_Y + h, ny) + 60


LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §3.2)<br>"
          "• Putih «user» = aktor memakai sistem<br>"
          "• Abu-abu «service» = dikerjakan sistem otomatis<br>"
          "• Krem putus-putus «manual» = di luar sistem<br>"
          "• Ungu «call behavior» = memanggil activity lain<br>"
          "• ◇ keputusan/gabungan; kondisi ditulis [guard] di panah<br>"
          "• ⧗ = menunggu kejadian/waktu tertentu<br>"
          "• Lajur abu-abu putus-putus = pihak di luar sistem")
CALL = ("<b>«call behavior» Sahkan dokumen (TK-A1)</b> = activity <i>A1 Pengesahan Dokumen</i> modul Tata Kelola "
        "(<code>labfik.approval.mixin</code> di Core): ajukan → periksa kelengkapan → terbitkan/cetak → tanda tangan di luar "
        "sistem → unggah PDF → sahkan (cek wewenang) → dokumen lama diganti. Tidak digambar ulang di modul SDM.")

pages = []

# ------------------------------------------------------------------ A1
a = Activity("sdm-act-a1", "Activity TO-BE (1-3) - Seleksi dan Penugasan Petugas", "sdm-act-a1-",
             "A1 · Seleksi Asisten dan Penugasan Petugas Praktikum (PKG-04), satu periode",
             [("k", "KaLab", 460, 2), ("l", "Laboran / PLP", 300, 1), ("s", "Sistem", 300, 1),
              ("x", "Penyetuju pengecualian (di luar sistem)", 260, 1, True)])
a.n("st", "k", 0, "start", col=0)
a.n("kb", "k", 1, "user", "Tetapkan kebutuhan petugas", col=0)
a.n("m0", "k", 2, "merge", col=0)
a.n("sc", "k", 3, "manual", "Seleksi calon asisten", col=0)
a.n("d1", "k", 4, "dec", col=0)
a.n("f0", "k", 4, "final", col=1)
a.n("sp", "x", 5, "manual", "Setujui pengecualian syarat")
a.n("m1", "l", 6, "merge")
a.n("ch", "l", 7, "user", "Catat hasil seleksi")
a.n("bp", "s", 8, "service", "Buat personel asisten")
a.n("d2", "l", 9, "dec")
a.n("su", "l", 10, "user", "Susun surat tugas")
a.n("a1", "l", 11, "call", "Sahkan dokumen (TK-A1)")
a.n("m2", "l", 12, "merge")
a.n("d3", "l", 13, "dec")
a.n("rv", "k", 13, "user", "Buat revisi surat tugas", col=1)
a.n("en", "l", 14, "final")
a.e("1", "st", "kb"); a.e("2", "kb", "m0"); a.e("3", "m0", "sc"); a.e("4", "sc", "d1")
a.e("5", "d1", "f0", "[tidak lulus]")
a.e("6", "d1", "sp", "[lulus dengan pengecualian]", [(a.cx("x", None), a.cy(4))], exit=(0.5, 1), entry=(0.5, 0))
a.e("7", "d1", "m1", "[lulus]", [(a.cx("k", 0), a.cy(6))], exit=(0.5, 1), entry=(0, 0.5))
a.e("8", "sp", "m1", "", [(a.cx("x", None), a.cy(6))], exit=(0.5, 1), entry=(1, 0.5))
a.e("9", "m1", "ch"); a.e("10", "ch", "bp", exit=(1, 0.5), entry=(0.5, 0))
a.e("11", "bp", "d2", "", [(a.cx("s", None), a.cy(9))], exit=(0.5, 1), entry=(1, 0.5))
a.e("12", "d2", "m0", "[masih ada calon]", [(a.lane_right("k", 30), a.cy(9)), (a.lane_right("k", 30), a.cy(2))],
    exit=(0, 0.5), entry=(1, 0.5))
a.e("13", "d2", "su", "[seleksi selesai]"); a.e("14", "su", "a1"); a.e("15", "a1", "m2"); a.e("16", "m2", "d3")
a.e("17", "d3", "rv", "[perlu pengganti]", exit=(0, 0.5), entry=(1, 0.5))
a.e("18", "rv", "m2", "", [(a.cx("k", 1), a.cy(12))], exit=(0.5, 0), entry=(0, 0.5))
a.e("19", "d3", "en", "[periode berakhir]")
a.finish(15, [
    (LEGEND, 150),
    (CALL, 100),
    ("<b>Kaitan ke PKG-04</b><br>"
     "S1 kebutuhan: <i>Tetapkan kebutuhan petugas</i> (KF-SDM-09)<br>"
     "S2 penugasan sah: <i>Susun surat tugas</i> + <i>Sahkan</i> (KF-SDM-10, 06, 11, 43)<br>"
     "S3 kompetensi: Bukti Kompetensi (CRUDL, KF-SDM-03), dicek sistem<br>"
     "S4 syarat internal: <i>Catat hasil seleksi</i> (KF-SDM-07, 08)<br>"
     "Status S1–S4 per sesi <b>dihitung saat dibaca</b> (KF-SDM-12), bukan tugas.", 130),
    ("<b>Surat tugas</b> berisi baris asisten → kelas dan laboran → ruang, dengan rentang berlaku. "
     "<i>Revisi surat tugas</i> (pengganti) = Pelengkap (KF-SDM-14).<br>"
     "Calon yang <b>tidak lulus</b> tidak dicatat; seleksinya sendiri di luar sistem (POB 2025).", 90),
    ("<b>[KONFIRMASI]</b> K7: siapa pengesah surat tugas. KB-3: surat tugas <b>ditolak</b> bila ada asisten tanpa "
     "seleksi lulus untuk MK kelasnya (default; alternatif: hanya peringatan). K2: penyetuju pengecualian (Koor Prodi/KaLab?).", 90),
    (SRC, 50),
])
pages.append(a)

# ------------------------------------------------------------------ A2
b = Activity("sdm-act-a2", "Activity TO-BE (2-3) - Otorisasi Personel", "sdm-act-a2-",
             "A2 · Otorisasi PLP/Laboran untuk Tugas/Alat Berkewenangan Khusus (PKG-10)",
             [("k", "KaLab", 300, 1), ("l", "Laboran / PLP (penilai, pencatat)", 460, 2), ("s", "Sistem", 300, 1)])
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
b.n("a1", "k", 10, "call", "Sahkan dokumen (TK-A1)")
b.n("go", "s", 11, "service", "Ganti otorisasi lama")
b.n("m2", "s", 12, "merge")
b.n("te", "s", 13, "time", "Muncul pemicu evaluasi ulang")
b.n("ce", "l", 14, "user", "Catat evaluasi ulang otorisasi", col=0)
b.n("d3", "l", 15, "dec", col=0)
b.n("cb", "k", 16, "user", "Cabut otorisasi")
b.n("en", "k", 17, "final")
b.e("1", "st", "tp")
b.e("2", "tp", "d1", "", [(b.cx("k", None), b.cy(2))], exit=(0.5, 1), entry=(0, 0.5))
b.e("3", "d1", "m0", "[belum ada bukti berlaku]")
b.e("4", "d1", "m1", "[bukti kompetensi berlaku ada]", [(b.lane_right("l", 8), b.cy(2)), (b.lane_right("l", 8), b.cy(8))],
    exit=(1, 0.5), entry=(1, 0.25))
b.e("5", "m0", "uj"); b.e("6", "uj", "ca"); b.e("7", "ca", "d2")
b.e("8", "d2", "pg", "[belum layak]")
b.e("9", "pg", "m0", "", [(b.cx("l", 1), b.cy(3))], exit=(0.5, 0), entry=(1, 0.5))
b.e("10", "d2", "bk", "[layak]", [(b.cx("l", 0), b.cy(7))], exit=(0.5, 1), entry=(0, 0.5))
b.e("11", "bk", "m1", "", [(b.cx("s", None), b.cy(8))], exit=(0.5, 1), entry=(1, 0.75))
b.e("12", "m1", "so"); b.e("13", "so", "a1")
b.e("14", "a1", "go", "", [(b.cx("k", None), b.cy(11))], exit=(0.5, 1), entry=(0, 0.5))
b.e("15", "go", "m2"); b.e("16", "m2", "te")
b.e("17", "te", "ce", "", [(b.cx("s", None), b.cy(14))], exit=(0.5, 1), entry=(1, 0.5))
b.e("18", "ce", "d3")
b.e("19", "d3", "m1", "[diperpanjang / dibatasi / naik level]", [(b.lane_left("l", 20), b.cy(15)), (b.lane_left("l", 20), b.cy(8))],
    exit=(0, 0.5), entry=(1, 0.5))
b.e("20", "d3", "m2", "[tetap berlaku]", [(b.cx("l", 1), b.cy(15)), (b.cx("l", 1), b.cy(12))], exit=(1, 0.5), entry=(0, 0.5))
b.e("21", "d3", "cb", "[dicabut]", [(b.cx("l", 0), b.cy(16))], exit=(0.5, 1), entry=(1, 0.5))
b.e("22", "cb", "en")
b.finish(18, [
    (LEGEND, 150),
    (CALL, 100),
    ("<b>Kaitan ke PKG-10</b><br>"
     "Penyebut: <i>Tetapkan pelaksana tugas/alat</i> (KF-SDM-18, 19)<br>"
     "S1 kompetensi: <i>Catat asesmen</i> / bukti yang ada (KF-SDM-20, 21)<br>"
     "S2 otorisasi berlaku: <i>Susun otorisasi</i> + <i>Sahkan</i> (KF-SDM-22, 23, 24)<br>"
     "S3 pemula disupervisi: guard kelengkapan saat diajukan (KF-SDM-23)<br>"
     "S4 evaluasi ulang: <i>Catat evaluasi ulang</i> (KF-SDM-25)<br>"
     "Status S1–S4 per pasangan dihitung saat dibaca (KF-SDM-26).", 140),
    ("<b>Temuan</b> (tabel status × transisi S2): keputusan <i>tetap berlaku</i> belum ada di KF-SDM-25 "
     "(mis. alat diganti tetapi kompetensi masih memadai).<br>"
     "⧗ pemicu dicatat manual; <b>tidak ada penjadwal</b> (kontrak Core K-3).", 90),
    ("<b>[KONFIRMASI]</b> KB-1 penyebut = pelaksana yang ditetapkan KaLab. Wawancara no. 16–18: alat mana yang wajib izin, "
     "cara uji, dan masa berlaku.", 70),
    (SRC, 50),
])
pages.append(b)

# ------------------------------------------------------------------ A3
c = Activity("sdm-act-a3", "Activity TO-BE (3-3) - Siklus Pelatihan PLP", "sdm-act-a3-",
             "A3 · Siklus Pelatihan PLP/Laboran (PKG-14), satu tahun",
             [("k", "KaLab", 300, 1), ("l", "Laboran / PLP (peserta, pencatat)", 460, 2), ("s", "Sistem", 300, 1)])
c.n("st", "k", 0, "start")
c.n("br", "k", 1, "user", "Buat rencana pelatihan")
c.n("ik", "s", 2, "service", "Isi kebutuhan dari matriks kompetensi")
c.n("lk", "k", 3, "user", "Lengkapi kebutuhan kompetensi")
c.n("si", "k", 4, "user", "Susun item pelatihan")
c.n("a1", "k", 5, "call", "Sahkan dokumen (TK-A1)")
c.n("m1", "l", 6, "merge", col=0)
c.n("te", "l", 7, "time", "Jadwal item pelatihan tiba", col=0)
c.n("d1", "l", 8, "dec", col=0)
c.n("tb", "k", 8, "user", "Tandai item batal")
c.n("ip", "l", 9, "manual", "Ikuti pelatihan", col=0)
c.n("cr", "l", 10, "user", "Catat realisasi pelatihan", col=0)
c.n("tk", "l", 11, "manual", "Terapkan keterampilan di pekerjaan", col=0)
c.n("t2", "l", 12, "time", "Waktu evaluasi pascapelatihan tiba", col=0)
c.n("ce", "l", 13, "user", "Catat evaluasi efektivitas", col=0)
c.n("d2", "l", 14, "dec", col=0)
c.n("bk", "s", 14, "service", "Buat bukti kompetensi")
c.n("m3", "l", 15, "merge", col=0)
c.n("d3", "l", 16, "dec", col=0)
c.n("en", "l", 17, "final", col=0)
c.e("1", "st", "br")
c.e("2", "br", "ik", "", [(c.cx("s", None), c.cy(1))], exit=(1, 0.5), entry=(0.5, 0))
c.e("3", "ik", "lk", "", [(c.cx("s", None), c.cy(3))], exit=(0.5, 1), entry=(1, 0.5))
c.e("4", "lk", "si"); c.e("5", "si", "a1")
c.e("6", "a1", "m1", "", [(c.cx("k", None), c.cy(6))], exit=(0.5, 1), entry=(0, 0.5))
c.e("7", "m1", "te"); c.e("8", "te", "d1")
c.e("9", "d1", "tb", "[batal]", exit=(0, 0.5), entry=(1, 0.5))
c.e("10", "d1", "ip", "[terlaksana]")
c.e("11", "tb", "m3", "", [(c.cx("k", None), c.cy(15))], exit=(0.5, 1), entry=(0, 0.5))
c.e("12", "ip", "cr"); c.e("13", "cr", "tk"); c.e("14", "tk", "t2"); c.e("15", "t2", "ce"); c.e("16", "ce", "d2")
c.e("17", "d2", "bk", "[efektif]")
c.e("18", "d2", "m3", "[perlu pengembangan]")
c.e("19", "bk", "m3", "", [(c.cx("s", None), c.cy(15))], exit=(0.5, 1), entry=(1, 0.5))
c.e("20", "m3", "d3")
c.e("21", "d3", "m1", "[masih ada item terjadwal]", [(c.cx("l", 1), c.cy(16)), (c.cx("l", 1), c.cy(6))],
    exit=(1, 0.5), entry=(1, 0.5))
c.e("22", "d3", "en", "[semua item selesai / batal]")
c.finish(18, [
    (LEGEND, 150),
    (CALL, 100),
    ("<b>Kaitan ke PKG-14</b><br>"
     "K1: <i>Buat rencana</i>, <i>Isi kebutuhan</i>, <i>Lengkapi kebutuhan</i>, <i>Sahkan</i> (KF-SDM-29, 30, 32)<br>"
     "K2: <i>Susun item pelatihan</i> (KF-SDM-31), dicek saat diajukan<br>"
     "K3: <i>Catat realisasi</i> + bukti penerapan (KF-SDM-33)<br>"
     "K4: <i>Catat evaluasi efektivitas</i>, <i>Buat bukti kompetensi</i> (KF-SDM-34, 35)<br>"
     "Kriteria tertinggi dihitung saat dibaca (KF-SDM-36).", 130),
    ("<b>Pembekuan kebutuhan</b> terjadi di dalam TK-A1 saat diajukan (<i>hook</i> <code>_sebelum_ajukan()</code>, KF-SDM-32).<br>"
     "<i>Tandai item batal</i> = Pelengkap (KF-SDM-37).<br>"
     "<b>Siklus berikutnya</b>: bukti kompetensi baru mengubah matriks, sehingga kebutuhan tahun depan (A3 berikutnya) ikut diperbarui.", 100),
    ("<b>[KONFIRMASI]</b> K10: pengesah rencana pelatihan (KaLab / Wadek Bidang Keuangan dan Umum). "
     "Wawancara no. 12: kapan dan oleh siapa efektivitas dinilai.", 70),
    (SRC, 50),
])
pages.append(c)

# ------------------------------------------------------------------ state machines
STATE = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#333333;"
STATE_T = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#EEEEEE;strokeColor=#333333;"
COMP = ("swimlane;rounded=1;arcSize=6;html=1;startSize=30;fontStyle=1;fontSize=13;fillColor=#EEFAF3;strokeColor=#4E9A6B;"
        "swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;")
TR = ("endArrow=open;endSize=9;html=1;rounded=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#333333;"
      "edgeStyle=orthogonalEdgeStyle;")
TRN = ("endArrow=open;endSize=9;html=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#9B2C44;"
       "edgeStyle=orthogonalEdgeStyle;rounded=1;")
SM_LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §3.3): <code>event [guard] / efek</code>. Abu-abu = status akhir. "
             "<font color='#9B2C44'><b>Garis merah</b></font> = transisi yang <b>baru ditemukan</b> lewat tabel status × "
             "transisi (proses-bisnis-sdm.md bagian 4). Kotak hijau = status komposit.")

# S1 Otorisasi
s1 = Page("sdm-stm-s1", "State Machine TO-BE (1-3) - Otorisasi", "sdm-stm-s1-")
s1.v("title", "S1 · State machine Otorisasi Personel (<code>approval.mixin.state</code> + masa berlaku sendiri), PKG-10",
     TITLE, 40, 16, 1500, 40)
s1.v("init", "", ST["start"], 50, 238, 24, 24)
s1.v("draf", "Draf", STATE, 130, 225, 150, 50)
s1.v("aju", "Diajukan", STATE, 470, 225, 150, 50)
s1.v("sah", "Disahkan", COMP, 800, 110, 420, 290)
s1.v("ini2", "", ST["start"], 830, 250, 24, 24)
s1.v("brl", "Berlaku", STATE, 900, 237, 130, 50)
s1.v("lwt", "Lewat masa berlaku", STATE, 1060, 330, 140, 50)
s1.v("gnt", "Diganti", STATE_T, 1330, 120, 150, 50)
s1.v("cbt", "Dicabut", STATE_T, 1330, 330, 150, 50)
s1.v("f0", "", ST["final"], 191, 400, 28, 28)
s1.v("f1", "", ST["final"], 1570, 131, 28, 28)
s1.v("f2", "", ST["final"], 1570, 341, 28, 28)
s1.e("t0", "init", "draf", "buat", style=TR)
s1.e("t1", "draf", "aju", "ajukan [kompetensi terbukti ∧ lingkup terisi<br>∧ supervisor berwenang bila terbimbing]<br>/ catat riwayat",
     style=TR, exit=(1, 0.3), entry=(0, 0.3))
s1.e("t2", "aju", "draf", "kembalikan / catat alasan", style=TR, exit=(0, 0.75), entry=(1, 0.75))
s1.e("t3", "aju", "sah", "sahkan [berkas TTD ada ∧ pengesah berwenang]<br>/ catat pengesah; otorisasi lama<br>pasangan sama → Diganti",
     style=TR, exit=(1, 0.5), entry=(0, 0.48))
s1.e("t4", "ini2", "brl", "/ tetapkan berlaku_mulai,<br>berlaku_sampai", style=TR)
s1.e("t5", "brl", "lwt", "when(hari ini &gt; berlaku_sampai)", [(965, 355)], style=TRN, exit=(0.5, 1), entry=(0, 0.5))
s1.e("t6", "sah", "gnt", "otorisasi baru pasangan sama disahkan<br>(perpanjang / batasi / naik level)", style=TR,
     exit=(1, 0.05), entry=(0, 0.5))
s1.e("t7", "sah", "cbt", "cabut [evaluasi ulang: dicabut]<br>/ catat alasan", style=TR, exit=(1, 0.76), entry=(0, 0.5))
s1.e("t8", "draf", "f0", "hapus [belum pernah diajukan]", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s1.e("tf1", "gnt", "f1", style=TR); s1.e("tf2", "cbt", "f2", style=TR)
s1.v("n1", SM_LEGEND, NOTE, 40, 470, 560, 80)
s1.v("n2", "<b>Berlaku / Lewat masa berlaku</b> adalah transisi stabil (§9.3.1): <b>tidak</b> disimpan di <code>state</code>, "
     "tetapi dihitung dari <code>berlaku_sampai</code> (<code>is_berlaku</code>). Tidak ada status <i>Kedaluwarsa</i> dan "
     "tidak ada penjadwal, karena Otorisasi tidak memakai <code>period.mixin</code> (kontrak Core K-3). "
     "PKG-10 S2 hanya terpenuhi di sub-status <b>Berlaku</b>.", NOTE, 620, 470, 520, 110)
s1.v("n3", "<b>Unggah berkas</b> (Diajukan → Diajukan) mengikuti S1 Tata Kelola dan tidak digambar ulang.<br>"
     "<b>[ASUMSI]</b> Diganti dan Dicabut adalah status akhir; otorisasi baru dibuat sebagai rekaman baru.", NOTE, 1160, 470, 420, 90)
s1.v("n4", SRC, NOTE, 40, 600, 560, 40)
s1.w, s1.h = 1660, 700
pages.append(s1)

# S2 Evaluasi Ulang Otorisasi
s2 = Page("sdm-stm-s2", "State Machine TO-BE (2-3) - Evaluasi Ulang Otorisasi", "sdm-stm-s2-")
s2.v("title", "S2 · State machine Evaluasi Ulang Otorisasi (PKG-10 S4)", TITLE, 40, 16, 1200, 40)
s2.v("init", "", ST["start"], 50, 188, 24, 24)
s2.v("trb", "Terbuka", STATE, 160, 175, 150, 50)
s2.v("ptn", "Diputuskan", STATE_T, 700, 175, 150, 50)
s2.v("f1", "", ST["final"], 960, 186, 28, 28)
s2.e("t0", "init", "trb", "catat pemicu", style=TR)
s2.e("t1", "trb", "ptn", "putuskan [keputusan ∈ {diperpanjang, dibatasi, naik level}]<br>/ susun otorisasi baru (A2)",
     style=TR, exit=(1, 0.2), entry=(0, 0.2))
s2.e("t2", "trb", "ptn", "putuskan [keputusan = dicabut] / cabut otorisasi", [(235, 300), (775, 300)],
     style=TR, exit=(0.5, 1), entry=(0.5, 1))
s2.e("t3", "trb", "ptn", "putuskan [keputusan = tetap berlaku]", [(235, 120), (775, 120)],
     style=TRN, exit=(0.5, 0), entry=(0.5, 0))
s2.e("tf", "ptn", "f1", style=TR)
s2.v("n1", SM_LEGEND, NOTE, 40, 360, 520, 80)
s2.v("n2", "<b>PKG-10 S4</b> gagal selama ada evaluasi ulang berstatus <b>Terbuka</b> pada pasangan itu (KF-SDM-26).<br>"
     "Status ini adalah field <code>status</code> milik <code>labfik.sdm.evaluasi.otorisasi</code> (transisi stabil, §9.3.1).",
     NOTE, 580, 360, 460, 80)
s2.v("n3", "<b>[ASUMSI]</b> Diputuskan adalah status akhir: keputusan yang berubah dicatat sebagai evaluasi ulang baru "
     "(rekaman bukti tidak dihapus, <code>evidence.mixin</code>).<br>" + SRC, NOTE, 40, 460, 520, 80)
s2.w, s2.h = 1100, 580
pages.append(s2)

# S3 Item Pelatihan
s3 = Page("sdm-stm-s3", "State Machine TO-BE (3-3) - Item Pelatihan", "sdm-stm-s3-")
s3.v("title", "S3 · State machine Item Pelatihan dalam Rencana Pelatihan (PKG-14 K3–K4)", TITLE, 40, 16, 1300, 40)
s3.v("init", "", ST["start"], 50, 238, 24, 24)
s3.v("rnc", "Direncanakan", STATE, 140, 225, 160, 50)
s3.v("tl", "Terlaksana", COMP, 560, 110, 440, 260)
s3.v("ini2", "", ST["start"], 590, 228, 24, 24)
s3.v("mnv", "Menunggu evaluasi", STATE, 660, 215, 140, 50)
s3.v("dev", "Dievaluasi", STATE, 840, 300, 130, 50)
s3.v("btl", "Batal", STATE_T, 140, 420, 160, 50)
s3.v("f0", "", ST["final"], 400, 120, 28, 28)
s3.v("f1", "", ST["final"], 206, 530, 28, 28)
s3.v("f2", "", ST["final"], 1080, 226, 28, 28)
s3.e("t0", "init", "rnc", "tambah item [rencana Draf]", style=TR)
s3.e("t1", "rnc", "tl", "catat realisasi [rencana Disahkan]<br>(peserta pertama)", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s3.e("t2", "rnc", "btl", "tandai batal [alasan diisi]", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s3.e("t3", "rnc", "f0", "hapus item [rencana masih Draf]", [(220, 134)], style=TRN, exit=(0.5, 0), entry=(0, 0.5))
s3.e("t4", "ini2", "mnv", "", style=TR)
s3.e("t5", "mnv", "dev", "when(setiap realisasi punya<br>evaluasi efektivitas)", [(730, 325)], style=TR,
     exit=(0.5, 1), entry=(0, 0.5))
s3.e("tf1", "btl", "f1", style=TR); s3.e("tf2", "tl", "f2", style=TR, exit=(1, 0.45), entry=(0, 0.5))
s3.v("n1", SM_LEGEND, NOTE, 40, 600, 540, 80)
s3.v("n2", "<b>Kaitan ke PKG-14</b>: K3 dihitung dari item <b>Terlaksana</b> yang setiap pesertanya punya realisasi dan bukti "
     "penerapan; item <b>Batal</b> tidak dihitung (KF-SDM-37, Pelengkap). K4 dihitung dari item <b>Dievaluasi</b>.<br>"
     "Sub-status Terlaksana dihitung dari data (transisi stabil, §9.3.1); hanya <i>rencana/terlaksana/batal</i> yang disimpan.",
     NOTE, 600, 420, 480, 110)
s3.v("n3", "<b>Status Rencana Pelatihan</b> mengikuti S1 Tata Kelola (draf → diajukan → disahkan → diganti/dicabut/kedaluwarsa); "
     "tidak digambar ulang. <b>[ASUMSI]</b> Batal adalah status akhir; item tidak bisa batal setelah ada realisasi.<br>" + SRC,
     NOTE, 600, 550, 480, 100)
s3.w, s3.h = 1160, 720
pages.append(s3)

with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(p.xml() for p in pages) + "</mxfile>")
