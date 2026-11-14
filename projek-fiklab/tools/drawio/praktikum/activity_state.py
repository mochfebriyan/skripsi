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
LANE = ("swimlane;html=1;startSize=34;fillColor=#EEF6FF;strokeColor=#6C8EBF;fontStyle=1;fontSize=13;"
        "swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;")
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=18;fontStyle=1;align=left;verticalAlign=middle;"


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
        for key, label, w, cols in lanes:
            self.lanes[key] = (x, w, cols, label)
            x += w
        self.total_w = x - 40
        self.v("title", title, TITLE, 40, 16, 1100, 40)
        self.nodes = {}

    def cy(self, row):
        return self.LANE_Y + self.HEAD + 34 + row * self.ROWH

    def cx(self, lane, col):
        lx, lw, cols, _ = self.lanes[lane]
        if cols == 1 or col is None:
            return lx + lw / 2
        return lx + lw * (col + 0.5) / cols

    def n(self, id, lane, row, kind, label="", col=None, w=None):
        cx, cy = self.cx(lane, col), self.cy(row)
        if kind == "fork":
            lw = self.lanes[lane][1]
            ww, hh = (w or lw - 60), 6
        else:
            ww, hh = SIZE[kind]
        val = label
        if kind in STEREO:
            val = f"<font style='font-size:9px' color='#6C4A87'>{STEREO[kind]}</font><br>{label}"
        self.v(id, val, ST[kind], cx - ww / 2, cy - hh / 2, ww, hh)
        self.nodes[id] = (cx, cy, ww, hh)

    def lane_left(self, lane, off):
        return self.lanes[lane][0] + off

    def lane_right(self, lane, off):
        lx, lw, _, _ = self.lanes[lane]
        return lx + lw - off

    def finish(self, rows, notes):
        h = self.HEAD + 34 + rows * self.ROWH + 20
        lane_cells = []
        for key, (lx, lw, cols, label) in self.lanes.items():
            lane_cells.append(f'<mxCell id="{self.P}lane-{key}" value="{esc(label)}" style="{LANE}" vertex="1" parent="1">'
                              f'<mxGeometry x="{lx:.0f}" y="{self.LANE_Y}" width="{lw:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')
        self.cells = lane_cells + self.cells  # lanes behind everything
        nx = 40 + self.total_w + 40
        ny = self.LANE_Y
        for i, (txt, nh) in enumerate(notes):
            self.v(f"note{i}", txt, NOTE, nx, ny, 320, nh)
            ny += nh + 16
        self.w = nx + 360
        self.h = max(self.LANE_Y + h, ny) + 60


LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §3.2)<br>"
          "• Putih «user» = aktor memakai sistem<br>"
          "• Abu-abu «service» = dikerjakan sistem otomatis<br>"
          "• Krem putus-putus «manual» = di luar sistem<br>"
          "• Ungu «call behavior» = memanggil diagram lain<br>"
          "• ◇ keputusan/gabungan; kondisi ditulis [guard] di panah<br>"
          "• ⧗ = menunggu waktu tertentu<br>"
          "• Bar hitam = jalur paralel (fork/join)")

pages = []
SRC = "Draf 14 Nov 2026 · Herrens · sumber: analisis PKG-15–20, studi dokumen (POB 2025), kebutuhan KF-PRK"

# ------------------------------------------------------------------ A1
a = Activity("prk-act-a1", "Activity TO-BE (1-5) - Persiapan Jadwal dan Modul", "prk-act-a1-",
             "A1 · Persiapan Jadwal dan Modul Periode (PKG-15)",
             [("f", "Tim Jadwal Fakultas", 260, 1), ("l", "Laboran", 280, 1), ("s", "Sistem", 300, 1),
              ("k", "KaLab", 280, 1), ("d", "Dosen", 260, 1)])
a.n("st", "f", 0, "start")
a.n("fk", "f", 1, "fork")
a.n("m0", "f", 2, "merge")
a.n("sj", "f", 3, "manual", "Susun jadwal kelas praktikum")
a.n("kb", "f", 4, "manual", "Kirim berkas jadwal kelas")
a.n("ij", "l", 5, "user", "Impor jadwal kelas")
a.n("bs", "s", 6, "service", "Bangkitkan sesi kelas")
a.n("pb", "s", 7, "service", "Periksa bentrok ruang")
a.n("d1", "s", 8, "dec")
a.n("sb", "l", 9, "manual", "Sampaikan bentrok ke fakultas")
a.n("pk", "s", 9, "service", "Periksa kapasitas ruang")
a.n("pj", "l", 10, "user", "Susun penetapan jadwal")
a.n("a1", "k", 11, "call", "Sahkan dokumen (A1 Tata Kelola)<br>penyetuju: KaLab")
a.n("tp", "s", 12, "service", "Catat tanggal publikasi")
a.n("ts", "s", 13, "service", "Tandai sesi terpublikasi")
a.n("tm", "d", 3, "user", "Terbitkan versi modul")
a.n("gm", "s", 4, "service", "Ganti versi modul lama")
a.n("jn", "s", 14, "fork")
a.n("en", "s", 15, "final")
a.e("1", "st", "fk"); a.e("2", "fk", "m0")
a.e("2b", "fk", "tm", "", [(a.cx("d", None), a.cy(1))], exit=(1, 0.5), entry=(0.5, 0))
a.e("3", "m0", "sj"); a.e("4", "sj", "kb")
a.e("5", "kb", "ij", "", [(a.cx("f", None), a.cy(5))], exit=(0.5, 1), entry=(0, 0.5))
a.e("6", "ij", "bs", "", [(a.cx("l", None), a.cy(6))], exit=(0.5, 1), entry=(0, 0.5))
a.e("7", "bs", "pb"); a.e("8", "pb", "d1")
a.e("9", "d1", "sb", "[bentrok]", [(a.cx("l", None), a.cy(8))], exit=(0, 0.5), entry=(0.5, 0))
a.e("10", "sb", "m0", "", [(a.lane_left("f", 18), a.cy(9)), (a.lane_left("f", 18), a.cy(2))], exit=(0, 0.5), entry=(0, 0.5))
a.e("11", "d1", "pk", "[tidak bentrok]")
a.e("12", "pk", "pj", "", [(a.cx("s", None), a.cy(10))], exit=(0.5, 1), entry=(1, 0.5))
a.e("13", "pj", "a1", "", [(a.cx("l", None), a.cy(11))], exit=(0.5, 1), entry=(0, 0.5))
a.e("14", "a1", "tp", "", [(a.cx("k", None), a.cy(12))], exit=(0.5, 1), entry=(1, 0.5))
a.e("15", "tp", "ts"); a.e("16", "ts", "jn")
a.e("17", "tm", "gm", "", [(a.cx("d", None), a.cy(4))], exit=(0.5, 1), entry=(1, 0.5))
a.e("18", "gm", "jn", "", [(a.lane_right("s", 16), a.cy(4)), (a.lane_right("s", 16), a.cy(14))], exit=(1, 0.5), entry=(1, 0.5))
a.e("19", "jn", "en")
a.finish(16, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria PKG-15</b><br>"
     "C1 jadwal sah: <i>Sahkan dokumen (A1 Tata Kelola)</i> + <i>Catat tanggal publikasi</i> (KF-PRK-06)<br>"
     "C2 tanpa bentrok: <i>Periksa bentrok ruang</i>; bentrok yang ditemukan menjadi rekaman konflik (KF-PRK-04, 11)<br>"
     "C3 kapasitas: <i>Periksa kapasitas ruang</i>, hanya peringatan (KF-PRK-05)<br>"
     "C4 modul berlaku: <i>Terbitkan versi modul</i> + <i>Ganti versi modul lama</i> (KF-PRK-12, 13)", 130),
    ("<b>Jadwal disusun tim jadwal fakultas</b> (di luar sistem); KaLab hanya menyetujui (keterangan Herrens, 14 Nov 2026). "
     "<b>[ASUMSI]</b> Jadwal masuk lewat <b>impor berkas</b> (Excel/CSV: kode MK, kelas, hari, jam, ruang, dosen), tanpa API. "
     "Jadwal berupa <b>pola mingguan tetap per kelas</b> selama satu semester (mis. Senin 13.00 untuk 16 pertemuan); satu baris per kelas. "
     "Pertemuan 8 (UTS) dan 16 (UAS) tetap di kelas pada jadwal yang sama (ujian atau presentasi proyek), jadi ikut dibangkitkan dengan jenis UTS/UAS. "
     "Jalan pengganti: laboran mengisi pola mingguan per kelas.", 140),
    ("<b>«call behavior»</b> memanggil activity <b>A1 Pengesahan Dokumen</b> milik modul Tata Kelola "
     "(<code>labfik.approval.mixin</code>): ajukan, unggah PDF bertanda tangan, sahkan. Tidak digambar ulang.", 80),
    ("<b>Tidak digambar</b> (§3.4, cukup dikelola): data Mata Kuliah dan Kelas («CRUDL»).", 50),
    ("<b>[KONFIRMASI]</b> Bentuk dan isi berkas jadwal dari fakultas, dan kapan dikirim (P2).", 50),
    (SRC, 50),
])
pages.append(a)

# ------------------------------------------------------------------ A2
b = Activity("prk-act-a2", "Activity TO-BE (2-5) - Pemakaian Lab", "prk-act-a2-",
             "A2 · Pemakaian Lab di Luar Praktikum (PKG-15)",
             [("p", "Pengguna Lab", 300, 1), ("s", "Sistem", 300, 1), ("k", "KaLab", 300, 1)])
b.n("st", "p", 0, "start")
b.n("m0", "p", 1, "merge")
b.n("aj", "p", 2, "user", "Ajukan pemakaian lab")
b.n("pb", "s", 3, "service", "Periksa bentrok ruang")
b.n("d1", "s", 4, "dec")
b.n("uw", "p", 4, "user", "Ubah waktu pemakaian")
b.n("nt", "s", 5, "service", "Kirim notifikasi pengajuan")
b.n("tj", "k", 6, "user", "Tinjau pengajuan pemakaian")
b.n("d2", "k", 7, "dec")
b.n("sp", "k", 8, "user", "Setujui pemakaian lab")
b.n("jt", "s", 9, "service", "Perbarui jadwal terpadu")
b.n("tl", "k", 10, "user", "Tolak pemakaian lab")
b.n("m1", "s", 11, "merge")
b.n("nk", "s", 12, "service", "Kirim notifikasi keputusan")
b.n("en", "s", 13, "final")
b.e("1", "st", "m0"); b.e("2", "m0", "aj")
b.e("3", "aj", "pb", "", [(b.cx("p", None), b.cy(3))], exit=(0.5, 1), entry=(0, 0.5))
b.e("4", "pb", "d1")
b.e("5", "d1", "uw", "[bentrok]", exit=(0, 0.5), entry=(1, 0.5))
b.e("6", "uw", "m0", "", [(b.lane_left("p", 18), b.cy(4)), (b.lane_left("p", 18), b.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
b.e("7", "d1", "nt", "[tidak bentrok]")
b.e("8", "nt", "tj", "", [(b.cx("s", None), b.cy(6))], exit=(0.5, 1), entry=(0, 0.5))
b.e("9", "tj", "d2"); b.e("10", "d2", "sp", "[disetujui]")
b.e("11", "sp", "jt", "", [(b.cx("k", None), b.cy(9))], exit=(0.5, 1), entry=(1, 0.5))
b.e("12", "d2", "tl", "[ditolak]", [(b.lane_right("k", 20), b.cy(7)), (b.lane_right("k", 20), b.cy(10))], exit=(1, 0.5), entry=(1, 0.5))
b.e("13", "jt", "m1")
b.e("14", "tl", "m1", "", [(b.cx("k", None), b.cy(11))], exit=(0.5, 1), entry=(1, 0.5))
b.e("15", "m1", "nk"); b.e("16", "nk", "en")
b.finish(14, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria PKG-15</b><br>"
     "Bukti 1 jadwal terpadu: <i>Perbarui jadwal terpadu</i> (KF-PRK-10)<br>"
     "Bukti 2 persetujuan pemakaian: <i>Setujui / Tolak pemakaian lab</i> (KF-PRK-09)<br>"
     "Bukti 5 rekaman konflik: bentrok yang ditemukan <i>Periksa bentrok ruang</i> dan penolakan beralasan bentrok (KF-PRK-11)", 110),
    ("<b>Penyetuju</b> = KaLab (keputusan Herrens, 14 Nov 2026). Status pengajuan mengikuti state machine S2.", 50),
    ("<b>[KONFIRMASI]</b> Jenis pemakaian di luar praktikum dan contoh kejadian bentrok (wawancara P3).", 50),
    (SRC, 50),
])
pages.append(b)

# ------------------------------------------------------------------ A3
c = Activity("prk-act-a3", "Activity TO-BE (3-5) - Pelaksanaan Sesi", "prk-act-a3-",
             "A3 · Pelaksanaan Satu Sesi Praktikum (PKG-16, 17, 18)",
             [("l", "Laboran", 300, 1), ("s", "Sistem", 280, 1), ("d", "Dosen", 260, 1),
              ("j", "Pengisi Jurnal (Asisten / Dosen / Laboran)", 320, 1)])
c.n("st", "l", 0, "start")
c.n("mp", "l", 1, "user", "Mulai pemeriksaan kesiapan")
c.n("bb", "s", 2, "service", "Buat butir pemeriksaan")
c.n("ih", "l", 3, "user", "Isi hasil butir pemeriksaan")
c.n("d1", "l", 4, "dec")
c.n("sb", "d", 5, "user", "Setujui substitusi bahan")
c.n("m1", "l", 6, "merge")
c.n("tk", "l", 7, "user", "Tetapkan keputusan kesiapan")
c.n("d2", "l", 8, "dec")
c.n("cp", "l", 9, "call", "Ajukan perubahan sesi (A4)")
c.n("f1", "l", 10, "final")
c.n("jm", "j", 9, "time", "Jam mulai sesi")
c.n("lp", "j", 10, "manual", "Laksanakan praktikum")
c.n("ij", "j", 11, "user", "Isi jurnal sesi")
c.n("pp", "j", 12, "user", "Catat presensi petugas")
c.n("lb", "j", 13, "user", "Catat entri log book")
c.n("m3", "j", 14, "merge")
c.n("kj", "j", 15, "user", "Kirim jurnal sesi")
c.n("vj", "s", 16, "service", "Validasi jurnal sesi")
c.n("d4", "s", 17, "dec")
c.n("pj", "j", 17, "user", "Perbaiki jurnal sesi")
c.n("us", "s", 18, "service", "Ubah status sesi menjadi Terlaksana")
c.n("en", "s", 19, "final")
c.e("1", "st", "mp")
c.e("2", "mp", "bb", "", [(c.cx("s", None), c.cy(1))], exit=(1, 0.5), entry=(0.5, 0))
c.e("3", "bb", "ih", "", [(c.cx("s", None), c.cy(3))], exit=(0.5, 1), entry=(1, 0.5))
c.e("4", "ih", "d1")
c.e("5", "d1", "sb", "[ada substitusi bahan]", [(c.cx("d", None), c.cy(4))], exit=(1, 0.5), entry=(0.5, 0))
c.e("6", "sb", "m1", "", [(c.cx("d", None), c.cy(6))], exit=(0.5, 1), entry=(1, 0.5))
c.e("7", "d1", "m1", "[tanpa substitusi]"); c.e("8", "m1", "tk"); c.e("9", "tk", "d2")
c.e("10", "d2", "cp", "[tunda]"); c.e("11", "cp", "f1")
c.e("12", "d2", "jm", "[siap]", [(c.cx("j", None), c.cy(8))], exit=(1, 0.5), entry=(0.5, 0))
c.e("13", "jm", "lp"); c.e("14", "lp", "ij"); c.e("15", "ij", "pp"); c.e("16", "pp", "lb"); c.e("17", "lb", "m3")
c.e("22", "m3", "kj")
c.e("23", "kj", "vj", "", [(c.cx("j", None), c.cy(16))], exit=(0.5, 1), entry=(1, 0.5))
c.e("24", "vj", "d4")
c.e("25", "d4", "pj", "[tidak valid]", exit=(1, 0.5), entry=(0, 0.5))
c.e("26", "pj", "m3", "", [(c.lane_right("j", 18), c.cy(17)), (c.lane_right("j", 18), c.cy(14))], exit=(1, 0.5), entry=(1, 0.5))
c.e("27", "d4", "us", "[valid]"); c.e("28", "us", "en")
c.finish(20, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria</b><br>"
     "PKG-16 S1–S4: <i>Mulai pemeriksaan</i> s.d. <i>Tetapkan keputusan kesiapan</i>, sebelum ⧗ jam mulai (KF-PRK-15–18)<br>"
     "PKG-17 B1–B3: butir bahan dari modul + <i>Setujui substitusi bahan</i> (KF-PRK-16, 19, 20)<br>"
     "PKG-18 C1–C5: <i>Isi jurnal</i> s.d. <i>Ubah status sesi</i> (KF-PRK-22–26)", 120),
    ("<b>Penilaian praktikan (PKG-19) tidak dicatat per sesi</b>: tugas punya tenggat sendiri dan tidak setiap sesi ada tugas. "
"Penilaian dilihat lewat tautan LeADS per kelas (KF-PRK-31); impor Excel bila tersedia (KF-PRK-50). Keputusan 14 Nov 2026.", 80),
    ("<b>Validasi jurnal</b> (KF-PRK-25): jam selesai &gt; jam mulai; satu jurnal terkirim per sesi; presensi dosen dan laboran terisi. "
     "Identitas sesi diambil dari Sesi, tidak diketik ulang.", 80),
    ("<b>Pengisi Jurnal</b> (aktor abstrak): asisten yang bertugas; untuk kelas tanpa asisten, dosen yang mengajar [ASUMSI].", 60),
    ("<b>[KONFIRMASI]</b> Pemeriksaan per sesi atau per ruang per hari (P8). Siapa pengisi jurnal kelas tanpa asisten (P10, P13).", 60),
    (SRC, 50),
])
pages.append(c)

# ------------------------------------------------------------------ A4
d = Activity("prk-act-a4", "Activity TO-BE (4-5) - Perubahan Sesi", "prk-act-a4-",
             "A4 · Perubahan Sesi (PKG-18)",
             [("p", "Pengaju (Dosen pengampu / Pengisi Jurnal / Laboran)", 320, 1), ("s", "Sistem", 300, 1), ("k", "KaLab", 460, 2)])
d.n("st", "p", 0, "start")
d.n("aj", "p", 1, "user", "Ajukan perubahan sesi")
d.n("nt", "s", 2, "service", "Kirim notifikasi pengajuan")
d.n("tj", "k", 3, "user", "Tinjau perubahan sesi")
d.n("d1", "k", 4, "dec")
d.n("tl", "k", 5, "user", "Tolak perubahan sesi", col=0)
d.n("sp", "k", 5, "user", "Setujui perubahan sesi", col=1)
d.n("d2", "s", 6, "dec")
d.n("m1", "s", 7, "merge")
d.n("pb", "s", 8, "service", "Periksa bentrok waktu pengganti")
d.n("d3", "s", 9, "dec")
d.n("tw", "k", 9, "user", "Tentukan waktu pengganti lain", col=1)
d.n("bp", "s", 10, "service", "Bangkitkan sesi pengganti")
d.n("m4", "s", 11, "merge")
d.n("ua", "s", 12, "service", "Ubah status sesi asal")
d.n("m2", "s", 13, "merge")
d.n("nk", "s", 14, "service", "Kirim notifikasi keputusan")
d.n("en", "s", 15, "final")
d.e("1", "st", "aj")
d.e("2", "aj", "nt", "", [(d.cx("p", None), d.cy(2))], exit=(0.5, 1), entry=(0, 0.5))
d.e("3", "nt", "tj", "", [(d.cx("s", None), d.cy(3))], exit=(0.5, 1), entry=(0, 0.5))
d.e("4", "tj", "d1")
d.e("5", "d1", "tl", "[ditolak]", [(d.cx("k", 0), d.cy(4))], exit=(0, 0.5), entry=(0.5, 0))
d.e("6", "d1", "sp", "[disetujui]", [(d.cx("k", 1), d.cy(4))], exit=(1, 0.5), entry=(0.5, 0))
d.e("7", "sp", "d2", "", [(d.cx("k", 1), d.cy(6))], exit=(0.5, 1), entry=(1, 0.5))
d.e("8", "d2", "m1", "[dengan pengganti]"); d.e("9", "m1", "pb"); d.e("10", "pb", "d3")
d.e("11", "d3", "tw", "[bentrok]", exit=(1, 0.5), entry=(0, 0.5))
d.e("12", "tw", "m1", "", [(d.cx("k", 1), d.cy(7))], exit=(0.5, 0), entry=(1, 0.5))
d.e("13", "d3", "bp", "[tidak bentrok]"); d.e("14", "bp", "m4")
d.e("15", "d2", "m4", "[tanpa pengganti: batal / daring]", [(d.lane_left("s", 24), d.cy(6)), (d.lane_left("s", 24), d.cy(11))], exit=(0, 0.5), entry=(0, 0.5))
d.e("16", "m4", "ua"); d.e("17", "ua", "m2")
d.e("18", "tl", "m2", "", [(d.cx("k", 0), d.cy(13))], exit=(0.5, 1), entry=(1, 0.5))
d.e("19", "m2", "nk"); d.e("20", "nk", "en")
d.finish(16, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria PKG-18</b><br>"
     "C2 (atau perubahan sah): <i>Setujui perubahan sesi</i> (KF-PRK-28)<br>"
     "Bukti 6 perubahan disetujui, bukti 7 penggantian sesi: <i>Bangkitkan sesi pengganti</i> (rujuk sesi asal)<br>"
     "Sesi tertunda dihitung memenuhi hanya bila pengganti terlaksana sebelum periode ditutup", 110),
    ("<b>Ubah status sesi asal</b>: dengan pengganti menjadi Diganti; batal menjadi Dibatalkan; daring: status tetap, moda menjadi daring (lihat S1).", 70),
    ("<b>Pengaju utama</b>: dosen pengampu (kelas jadi daring atau jadwal diubah; keterangan Herrens, 14 Nov 2026). Juga dipanggil dari A3 (keputusan tunda). Penyetuju = KaLab.", 60),
    ("<b>[KONFIRMASI]</b> Sesi daring dianggap sah? (pengaturan KaLab, KF-PRK-43; wawancara P12)", 50),
    (SRC, 50),
])
pages.append(d)

# ------------------------------------------------------------------ A5
e = Activity("prk-act-a5", "Activity TO-BE (5-5) - Survei Kepuasan", "prk-act-a5-",
             "A5 · Survei Kepuasan Pengguna per Periode (PKG-20)",
             [("k", "KaLab", 300, 1), ("s", "Sistem", 300, 1), ("r", "Responden", 280, 1)])
e.n("st", "k", 0, "start")
e.n("m0", "k", 1, "merge")
e.n("ss", "k", 2, "user", "Susun survei periode")
e.n("ts", "k", 3, "user", "Tetapkan survei")
e.n("pk", "s", 4, "service", "Periksa kelengkapan survei")
e.n("d1", "s", 5, "dec")
e.n("ls", "k", 5, "user", "Lengkapi survei")
e.n("tb", "s", 6, "time", "Tanggal buka survei")
e.n("is", "r", 7, "user", "Isi survei")
e.n("tt", "s", 8, "time", "Tanggal tutup survei")
e.n("hr", "s", 9, "service", "Hitung rekap per aspek")
e.n("ce", "k", 10, "user", "Catat evaluasi survei")
e.n("rt", "k", 11, "user", "Tetapkan rencana tindak lanjut")
e.n("k3", "s", 12, "service", "Perbarui status K1–K3")
e.n("np", "s", 13, "time", "Survei periode berikutnya dianalisis")
e.n("ne", "k", 14, "user", "Nilai efektivitas tindak lanjut")
e.n("k4", "s", 15, "service", "Perbarui status K4")
e.n("en", "s", 16, "final")
e.e("1", "st", "m0"); e.e("2", "m0", "ss"); e.e("3", "ss", "ts")
e.e("4", "ts", "pk", "", [(e.cx("k", None), e.cy(4))], exit=(0.5, 1), entry=(0, 0.5))
e.e("5", "pk", "d1")
e.e("6", "d1", "ls", "[tidak lengkap]", exit=(0, 0.5), entry=(1, 0.5))
e.e("7", "ls", "m0", "", [(e.lane_left("k", 18), e.cy(5)), (e.lane_left("k", 18), e.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
e.e("8", "d1", "tb", "[lengkap]")
e.e("9", "tb", "is", "", [(e.cx("r", None), e.cy(6))], exit=(1, 0.5), entry=(0.5, 0))
e.e("10", "is", "tt", "", [(e.cx("r", None), e.cy(8))], exit=(0.5, 1), entry=(1, 0.5))
e.e("11", "tt", "hr")
e.e("12", "hr", "ce", "", [(e.cx("s", None), e.cy(10))], exit=(0.5, 1), entry=(1, 0.5))
e.e("13", "ce", "rt")
e.e("14", "rt", "k3", "", [(e.cx("k", None), e.cy(12))], exit=(0.5, 1), entry=(0, 0.5))
e.e("15", "k3", "np")
e.e("16", "np", "ne", "", [(e.cx("s", None), e.cy(14))], exit=(0.5, 1), entry=(1, 0.5))
e.e("17", "ne", "k4", "", [(e.cx("k", None), e.cy(15))], exit=(0.5, 1), entry=(0, 0.5))
e.e("18", "k4", "en")
e.finish(17, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria PKG-20</b> (berurutan)<br>"
     "K1 ditetapkan: <i>Susun survei</i> + <i>Tetapkan survei</i> (KF-PRK-33, 34)<br>"
     "K2 enam aspek + target respons: <i>Periksa kelengkapan survei</i><br>"
     "K3 dilaksanakan dan dianalisis: <i>Isi survei</i>, <i>Hitung rekap</i>, <i>Catat evaluasi</i> (KF-PRK-35, 36, 38)<br>"
     "K4 perbaikan dan efektivitas: <i>Tetapkan RTL</i>, <i>Nilai efektivitas</i> (KF-PRK-36, 37)", 140),
    ("<b>Isi survei</b> dilakukan banyak responden secara anonim lewat tautan addon <code>survey</code>, selama survei dibuka.", 60),
    ("<b>⧗ Survei periode berikutnya dianalisis</b>: K4 baru bisa lengkap pada periode kedua.", 50),
    ("<b>[KONFIRMASI]</b> Waktu survei, responden, dan siapa yang menindaklanjuti (P16, P17).", 50),
    (SRC, 50),
])
pages.append(e)

# ------------------------------------------------------------------ state machines
STATE = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#333333;"
STATE_T = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#EEEEEE;strokeColor=#333333;"
TR = ("endArrow=open;endSize=9;html=1;rounded=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#333333;"
      "edgeStyle=orthogonalEdgeStyle;")
TRN = ("endArrow=open;endSize=9;html=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#9B2C44;"
       "edgeStyle=orthogonalEdgeStyle;rounded=1;")
STNOTE = ("<b>Notasi</b> (Wazlawick 2024, §3.3): <code>event [guard] / efek</code>. Abu-abu = status akhir. "
          "<font color='#9B2C44'><b>Garis merah</b></font> = transisi yang <b>baru ditemukan</b> lewat tabel status × transisi "
          "(proses-bisnis-praktikum.md bagian 3) dan belum ada di analisis maupun kebutuhan.")

# S1 Sesi
s1 = Page("prk-stm-s1", "State Machine TO-BE (1-3) - Sesi", "prk-stm-s1-")
s1.v("title", "S1 · State machine Sesi praktikum (<code>labfik.sesi.state</code>, Core; status diubah hanya oleh modul Praktikum)",
     TITLE, 40, 16, 1500, 40)
s1.v("init", "", ST["start"], 50, 238, 24, 24)
s1.v("ren", "Rencana", STATE, 130, 225, 150, 50)
s1.v("init2", "", ST["start"], 583, 70, 24, 24)
s1.v("pub", "Terpublikasi", STATE, 520, 225, 150, 50)
s1.v("lak", "Terlaksana", STATE_T, 1000, 225, 150, 50)
s1.v("tun", "Ditunda", STATE, 520, 470, 150, 50)
s1.v("gan", "Diganti", STATE_T, 1000, 470, 150, 50)
s1.v("bat", "Dibatalkan", STATE_T, 1000, 640, 150, 50)
s1.v("f0", "", ST["final"], 191, 420, 28, 28)
s1.v("f1", "", ST["final"], 1260, 236, 28, 28)
s1.v("f2", "", ST["final"], 1260, 481, 28, 28)
s1.v("f3", "", ST["final"], 1260, 651, 28, 28)
s1.e("t0", "init", "ren", "bangkitkan (A1)", style=TR)
s1.e("t0b", "init2", "pub", "bangkitkan pengganti (A4)", style=TR)
s1.e("t1", "ren", "pub", "jadwal periode disahkan (A1)<br>/ catat tanggal_publikasi", style=TR, exit=(1, 0.3), entry=(0, 0.3))
s1.e("t2", "pub", "ren", "jadwal periode dicabut<br>[belum ada jurnal]", style=TRN, exit=(0, 0.75), entry=(1, 0.75))
s1.e("t3", "pub", "lak", "kirim jurnal [jurnal valid]<br>/ catat waktu kirim", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s1.e("t4", "pub", "tun", "tetapkan keputusan tunda (A3)", style=TR, exit=(0.3, 1), entry=(0.3, 0))
s1.e("t5", "tun", "pub", "perubahan ditolak", style=TRN, exit=(0.7, 0), entry=(0.7, 1))
s1.e("t6", "pub", "gan", "perubahan disetujui [dengan pengganti]<br>/ bangkitkan sesi pengganti", [(860, 260), (860, 485)], style=TR, exit=(1, 0.7), entry=(0, 0.3))
s1.e("t7", "tun", "gan", "perubahan disetujui [dengan pengganti]<br>/ bangkitkan sesi pengganti", style=TR, exit=(1, 0.7), entry=(0, 0.7))
s1.e("t8", "tun", "bat", "perubahan disetujui [batal tanpa pengganti]", [(595, 665)], style=TR, exit=(0.5, 1), entry=(0, 0.5))
s1.e("t9", "pub", "pub", "perubahan disetujui [daring]<br>/ ubah moda", [(700, 215), (700, 190), (640, 190)], style=TR, exit=(1, 0.1), entry=(0.8, 0))
s1.e("t10", "ren", "f0", "hapus [belum terpublikasi]", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s1.e("t11", "pub", "bat", "perubahan disetujui [batal tanpa pengganti]", [(470, 250), (470, 705), (1075, 705)], style=TR, exit=(0, 0.5), entry=(0.5, 1))
for i, src in enumerate(["lak", "gan", "bat"], 1):
    s1.e(f"tf{i}", src, f"f{i}", style=TR)
s1.v("n1", STNOTE, NOTE, 40, 750, 560, 70)
s1.v("n2", "<b>Status turunan, bukan state</b> (Wazlawick §9.3.1): <i>Terlewat</i> = Terpublikasi, tanggal sudah lewat, "
     "belum ada jurnal, dihitung sebagai <code>is_terlewat</code> {compute}. Tidak dijadwalkan (prinsip hitung, bukan jadwalkan).", NOTE, 620, 750, 480, 80)
s1.v("n3", "<b>Kaitan</b>: Terlaksana = PKG-18 C1. Diganti/Dibatalkan hanya lewat Perubahan Sesi yang disetujui (C2). "
     "Sesi pengganti merujuk sesi asal (<code>sesi_asal_id</code>).", NOTE, 1120, 750, 400, 80)
s1.v("n4", "<b>[KONFIRMASI]</b> Jadwal dicabut setelah disahkan: sesi kembali ke Rencana? Tunda lalu perubahan ditolak: sesi kembali "
     "Terpublikasi untuk diperiksa ulang? " + SRC, NOTE, 40, 840, 760, 70)
s1.w, s1.h = 1600, 950
pages.append(s1)

# S2 Persetujuan sederhana
s2 = Page("prk-stm-s2", "State Machine TO-BE (2-3) - Pengajuan Pemakaian dan Perubahan", "prk-stm-s2-")
s2.v("title", "S2 · State machine pengajuan dengan persetujuan sederhana: Rencana Pemakaian Lab dan Perubahan Sesi", TITLE, 40, 16, 1400, 40)
s2.v("init", "", ST["start"], 50, 238, 24, 24)
s2.v("aju", "Diajukan", STATE, 160, 225, 150, 50)
s2.v("set", "Disetujui", STATE_T, 620, 110, 150, 50)
s2.v("tol", "Ditolak", STATE_T, 620, 240, 150, 50)
s2.v("tar", "Ditarik", STATE_T, 620, 370, 150, 50)
s2.v("f1", "", ST["final"], 880, 121, 28, 28)
s2.v("f2", "", ST["final"], 880, 251, 28, 28)
s2.v("f3", "", ST["final"], 880, 381, 28, 28)
s2.e("t0", "init", "aju", "ajukan [tidak bentrok]", style=TR)
s2.e("t1", "aju", "set", "setujui [jabatan berwenang: KaLab]<br>/ perbarui jadwal terpadu atau ubah Sesi (S1)", [(235, 135)], style=TR, exit=(0.5, 0), entry=(0, 0.5))
s2.e("t2", "aju", "tol", "tolak [alasan terisi] / catat alasan", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s2.e("t3", "aju", "tar", "tarik kembali [oleh pengaju]", [(235, 395)], style=TRN, exit=(0.5, 1), entry=(0, 0.5))
for i, src in enumerate(["set", "tol", "tar"], 1):
    s2.e(f"tf{i}", src, f"f{i}", style=TR)
s2.v("n1", STNOTE, NOTE, 40, 460, 560, 70)
s2.v("n2", "<b>Dipakai oleh</b> dua objek dengan pola sama: <code>labfik.praktikum.pemakaian</code> (A2) dan "
     "<code>labfik.praktikum.perubahan</code> (A4). Guard <i>tidak bentrok</i> hanya untuk pemakaian lab. Tanpa PDF bertanda tangan "
     "(kontrak Core b).", NOTE, 620, 460, 520, 90)
s2.v("n3", "<b>[KONFIRMASI]</b> Pemakaian yang sudah disetujui lalu batal dipakai: perlu status <i>Dibatalkan</i>? " + SRC, NOTE, 40, 560, 760, 60)
s2.w, s2.h = 1200, 660
pages.append(s2)

# S3 Survei
s3 = Page("prk-stm-s3", "State Machine TO-BE (3-3) - Survei Kepuasan", "prk-stm-s3-")
s3.v("title", "S3 · State machine Survei kepuasan per periode (perluasan <code>survey.survey</code>) dan kaitannya dengan K1–K4",
     TITLE, 40, 16, 1400, 40)
s3.v("init", "", ST["start"], 50, 238, 24, 24)
s3.v("dra", "Draf", STATE, 130, 225, 150, 50)
s3.v("tet", "Ditetapkan<br><font style='font-size:10px;font-weight:normal'>(K1–K2 lengkap)</font>", STATE, 470, 225, 160, 50)
s3.v("eva", "Dievaluasi<br><font style='font-size:10px;font-weight:normal'>(K3 lengkap)</font>", STATE, 830, 225, 160, 50)
s3.v("sel", "Siklus Selesai<br><font style='font-size:10px;font-weight:normal'>(K4 lengkap)</font>", STATE_T, 1190, 225, 160, 50)
s3.v("f1", "", ST["final"], 1256, 380, 28, 28)
s3.e("t0", "init", "dra", "buat", style=TR)
s3.e("t1", "dra", "tet", "tetapkan [enam aspek ∧ butir terbuka<br>∧ target respons ∧ jabatan berwenang]", style=TR, exit=(1, 0.3), entry=(0, 0.3))
s3.e("t2", "tet", "dra", "batalkan penetapan<br>[sebelum tanggal buka]", style=TRN, exit=(0, 0.75), entry=(1, 0.75))
s3.e("t3", "tet", "eva", "catat evaluasi + RTL<br>[tanggal tutup terlewati]", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s3.e("t4", "eva", "sel", "nilai efektivitas semua RTL<br>[survei periode berikutnya dievaluasi]", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s3.e("t5", "sel", "f1", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s3.v("n1", STNOTE, NOTE, 40, 440, 560, 70)
s3.v("n2", "<b>Status turunan</b> (§9.3.1): selama Ditetapkan, <i>Belum dibuka / Dibuka / Ditutup</i> dihitung dari tanggal buka–tutup, "
     "tidak disimpan. Kriteria K1–K4 dihitung <code>labfik.criteria.mixin</code>.", NOTE, 620, 440, 520, 80)
s3.v("n3", "<b>[KONFIRMASI]</b> Bolehkah penetapan dibatalkan setelah survei dibuka (mis. butir salah)? Asumsi: tidak; buat survei baru. "
     + SRC, NOTE, 40, 530, 760, 60)
s3.w, s3.h = 1450, 640
pages.append(s3)

open(OUT, "w", encoding="utf-8").write('<mxfile host="app.diagrams.net">' + "".join(p.xml() for p in pages) + "</mxfile>")
