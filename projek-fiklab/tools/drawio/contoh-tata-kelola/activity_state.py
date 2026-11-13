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
LANE = ("swimlane;html=1;startSize=34;fillColor=#F5F0FF;strokeColor=#9673A6;fontStyle=1;fontSize=13;"
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

# ------------------------------------------------------------------ A1
a = Activity("tk-act-a1", "Activity TO-BE A1 - Pengesahan Dokumen", "tk-act-a1-",
             "A1 · Pengesahan Dokumen (dipakai bersama oleh A2, A3, A4)",
             [("p", "Penyusun (KaLab / Laboran)", 300, 1), ("s", "Sistem", 300, 1),
              ("m", "Pemeriksa (opsional)", 260, 1), ("g", "Pengesah (KaLab / Dekan)", 280, 1)])
a.n("st", "p", 0, "start")
a.n("m0", "p", 1, "merge")
a.n("aj", "p", 2, "user", "Ajukan dokumen")
a.n("kl", "s", 3, "service", "Periksa kelengkapan dokumen")
a.n("d1", "s", 4, "dec")
a.n("lk", "p", 4, "user", "Lengkapi dokumen")
a.n("cp", "s", 5, "service", "Catat pengajuan")
a.n("nt", "s", 6, "service", "Kirim notifikasi pengajuan")
a.n("d2", "s", 7, "dec")
a.n("pd", "m", 7, "user", "Periksa dokumen")
a.n("d3", "m", 8, "dec")
a.n("kb", "m", 9, "user", "Kembalikan dokumen")
a.n("mp", "p", 9, "merge")
a.n("m1", "s", 10, "merge")
a.n("pb", "p", 10, "user", "Perbaiki dokumen")
a.n("d4", "s", 11, "dec")
a.n("tr", "p", 12, "user", "Terbitkan dokumen resmi")
a.n("hp", "s", 13, "service", "Hasilkan PDF dokumen")
a.n("m2", "p", 14, "merge")
a.n("ct", "p", 15, "manual", "Cetak dokumen")
a.n("td", "g", 16, "manual", "Tinjau dokumen cetak")
a.n("d5", "g", 17, "dec")
a.n("cg", "p", 17, "user", "Catat pengembalian dokumen")
a.n("tt", "g", 18, "manual", "Tanda tangani dokumen")
a.n("m3", "p", 19, "merge")
a.n("ug", "p", 20, "user", "Unggah dokumen bertanda tangan")
a.n("sh", "g", 21, "user", "Sahkan dokumen")
a.n("vl", "s", 22, "service", "Validasi pengesahan")
a.n("d6", "s", 23, "dec")
a.n("us", "s", 24, "service", "Ubah status menjadi Disahkan")
a.n("jj", "s", 25, "service", "Catat jejak pengesahan")
a.n("en", "s", 26, "final")
a.e("1", "st", "m0"); a.e("2", "m0", "aj"); a.e("3", "aj", "kl"); a.e("4", "kl", "d1")
a.e("5", "d1", "lk", "[tidak lengkap]")
a.e("6", "lk", "m0", "", [(a.lane_left("p", 18), a.cy(4)), (a.lane_left("p", 18), a.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
a.e("7", "d1", "cp", "[lengkap]"); a.e("8", "cp", "nt"); a.e("9", "nt", "d2")
a.e("10", "d2", "pd", "[pemeriksaan aktif]")
a.e("11", "d2", "m1", "[pemeriksaan tidak aktif]")
a.e("12", "pd", "d3"); a.e("13", "d3", "kb", "[perlu perbaikan]")
a.e("14", "d3", "m1", "[layak]", exit=(0, 0.5), entry=(1, 0.5))
a.e("15", "kb", "mp", exit=(0, 0.5), entry=(1, 0.5))
a.e("16", "mp", "pb")
a.e("17", "pb", "m0", "", [(a.lane_left("p", 34), a.cy(10)), (a.lane_left("p", 34), a.cy(1) + 6)], exit=(0, 0.5), entry=(0, 0.75))
a.e("18", "m1", "d4")
a.e("19", "d4", "tr", "[rencana / SK]", exit=(0, 0.5), entry=(0.5, 0))
a.e("20", "tr", "hp", exit=(1, 0.5), entry=(0.5, 0))
a.e("21", "hp", "m2", exit=(0, 0.5), entry=(1, 0.5))
a.e("22", "d4", "m2", "[SOP / IK: berkas sudah diunggah]", [(a.lane_right("s", 30), a.cy(11)), (a.lane_right("s", 30), a.cy(14))], exit=(1, 0.5), entry=(1, 0.75))
a.e("23", "m2", "ct"); a.e("24", "ct", "td", exit=(1, 0.5), entry=(0, 0.5)); a.e("25", "td", "d5")
a.e("26", "d5", "cg", "[tidak disetujui]", exit=(0, 0.5), entry=(1, 0.5))
a.e("27", "cg", "mp", "", [(a.lane_left("p", 50), a.cy(17)), (a.lane_left("p", 50), a.cy(9))], exit=(0, 0.5), entry=(0, 0.5))
a.e("28", "d5", "tt", "[disetujui]"); a.e("29", "tt", "m3", exit=(0, 0.5), entry=(1, 0.5))
a.e("30", "m3", "ug"); a.e("31", "ug", "sh", exit=(1, 0.5), entry=(0, 0.5)); a.e("32", "sh", "vl", exit=(0, 0.5), entry=(1, 0.5))
a.e("33", "vl", "d6")
a.e("34", "d6", "m3", "[berkas bertanda tangan belum ada]", [(a.lane_left("s", 24), a.cy(23)), (a.lane_left("s", 24), a.cy(19))], exit=(0, 0.5), entry=(1, 0.5))
a.e("35", "d6", "us", "[valid]"); a.e("36", "us", "jj"); a.e("37", "jj", "en")
a.finish(27, [
    (LEGEND, 150),
    ("<b>Aturan bisnis</b><br>"
     "• <i>Periksa kelengkapan</i> = <code>_cek_kelengkapan()</code>, isinya berbeda per jenis dokumen (KF-24).<br>"
     "• <i>Sahkan dokumen</i> hanya tersedia bagi jabatan yang berwenang untuk jenis dokumen itu; "
     "<i>Validasi pengesahan</i> memastikan berkas bertanda tangan ada (KF-33).<br>"
     "• Tahap pemeriksaan aktif/tidak diatur per jenis dokumen (KF-32).<br>"
     "• Semua langkah tercatat di riwayat (KF-34).", 140),
    ("<b>[KONFIRMASI]</b> Bila Dekan/Pemeriksa tidak login, aksi di lajur mereka yang bertanda «user» "
     "dilakukan KaLab atas nama mereka; berkas bertanda tangan menjadi buktinya.", 80),
    ("<b>Tanpa tanda tangan digital</b> (brief, batasan 3). Pengesahan lintas hari: "
     "<i>Cetak → Tanda tangani → Unggah</i> adalah sesi terpisah, karena itu "
     "<i>Terbitkan dokumen resmi</i> dan <i>Sahkan dokumen</i> adalah aksi tersendiri.", 90),
    ("Status dokumen di sepanjang alur ini: lihat <b>S1</b>.<br>Draf 13 Nov 2026 · Febriyan", 50),
])
pages.append(a)

# ------------------------------------------------------------------ A2
b = Activity("tk-act-a2", "Activity TO-BE A2 - Siklus SOP-IK", "tk-act-a2-",
             "A2 · Siklus Dokumen SOP/IK (PKG-02)",
             [("l", "Laboran / PLP", 480, 2), ("k", "KaLab", 260, 1), ("s", "Sistem", 300, 1)])
b.n("st", "l", 0, "start")
b.n("d1", "l", 1, "dec")
b.n("di", "l", 2, "user", "Daftarkan dokumen induk", col=1)
b.n("m1", "l", 3, "merge")
b.n("sn", "l", 4, "manual", "Susun naskah dokumen")
b.n("uv", "l", 5, "user", "Unggah versi dokumen")
b.n("a1", "l", 6, "call", "Sahkan dokumen (A1)")
b.n("gv", "s", 7, "service", "Ganti status versi lama")
b.n("jt", "s", 8, "service", "Jadwalkan tinjau ulang")
b.n("fk", "l", 9, "fork")
b.n("cd", "l", 10, "user", "Catat distribusi dokumen", col=0)
b.n("cs", "l", 10, "user", "Catat sosialisasi dokumen", col=1)
b.n("jn", "l", 11, "fork")
b.n("m2", "s", 12, "merge")
b.n("te", "s", 13, "time", "Tanggal tinjau ulang tiba")
b.n("pn", "s", 14, "service", "Kirim pengingat tinjau ulang")
b.n("tu", "l", 15, "user", "Tinjau ulang dokumen")
b.n("d2", "l", 16, "dec")
b.n("pj", "s", 16, "service", "Perbarui jadwal tinjau")
b.n("cb", "k", 17, "user", "Cabut dokumen")
b.n("uc", "s", 18, "service", "Ubah status menjadi Dicabut")
b.n("en", "s", 19, "final")
b.e("1", "st", "d1")
b.e("2", "d1", "di", "[dokumen baru]", exit=(1, 0.5), entry=(0.5, 0))
b.e("3", "d1", "m1", "[revisi dokumen terdaftar]")
b.e("4", "di", "m1", exit=(0.5, 1), entry=(1, 0.5))
b.e("5", "m1", "sn"); b.e("6", "sn", "uv"); b.e("7", "uv", "a1")
b.e("8", "a1", "gv", exit=(1, 0.5), entry=(0.5, 0)); b.e("9", "gv", "jt")
b.e("10", "jt", "fk", exit=(0, 0.5), entry=(0.5, 0))
b.e("11", "fk", "cd", exit=(0.15, 1), entry=(0.5, 0)); b.e("12", "fk", "cs", exit=(0.85, 1), entry=(0.5, 0))
b.e("13", "cd", "jn", exit=(0.5, 1), entry=(0.15, 0)); b.e("14", "cs", "jn", exit=(0.5, 1), entry=(0.85, 0))
b.e("15", "jn", "m2", exit=(1, 0.5), entry=(0, 0.5))
b.e("16", "m2", "te"); b.e("17", "te", "pn")
b.e("18", "pn", "tu", exit=(0, 0.5), entry=(1, 0.5)); b.e("19", "tu", "d2")
b.e("20", "d2", "pj", "[tetap berlaku]", exit=(1, 0.5), entry=(0, 0.5))
b.e("21", "pj", "m2", "", [(b.lane_right("s", 24), b.cy(16)), (b.lane_right("s", 24), b.cy(12))], exit=(1, 0.5), entry=(1, 0.5))
b.e("22", "d2", "m1", "[perlu revisi]", [(b.lane_left("l", 24), b.cy(16)), (b.lane_left("l", 24), b.cy(3))], exit=(0, 0.5), entry=(0, 0.5))
b.e("23", "d2", "cb", "[tidak diperlukan lagi]", exit=(0.5, 1), entry=(0.5, 0))
b.e("24", "cb", "uc", exit=(1, 0.5), entry=(0.5, 0)); b.e("25", "uc", "en")
b.finish(20, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria PKG-02</b><br>"
     "S1 terdaftar: <i>Daftarkan dokumen induk</i><br>"
     "S2 disahkan: <i>Sahkan dokumen (A1)</i><br>"
     "S3 mutakhir: <i>Tinjau ulang</i> + jadwal (lihat <b>S2</b>)<br>"
     "S4 tersedia: <i>Catat distribusi</i><br>"
     "S5 disosialisasikan: <i>Catat sosialisasi</i>", 110),
    ("<b>Di luar sistem</b>: naskah SOP/IK tetap disusun di Word/Docs (keputusan 13 Nov 2026). "
     "Sistem hanya mengelola versi, pengesahan, distribusi, sosialisasi, dan tinjau ulang.", 80),
    ("Pengguna Lab hanya melihat versi berlaku (KF-16); tidak digambar karena bukan bagian alur ini.<br>"
     "<i>Cabut dokumen</i> hanya oleh jabatan berwenang.", 70),
    ("Draf 13 Nov 2026 · Febriyan", 30),
])
pages.append(b)

# ------------------------------------------------------------------ A3
c = Activity("tk-act-a3", "Activity TO-BE A3 - Siklus Rencana", "tk-act-a3-",
             "A3 · Siklus Rencana: strategis, RKT, IKU, pengembangan (PKG-01, PKG-13)",
             [("k", "KaLab", 460, 2), ("p", "PIC kegiatan (Laboran / KaLab)", 280, 1), ("s", "Sistem", 300, 1)])
c.n("st", "k", 0, "start")
c.n("m0", "k", 1, "merge")
c.n("d1", "k", 2, "dec")
c.n("ag", "k", 3, "user", "Susun analisis gap", col=1)
c.n("m1", "k", 4, "merge")
c.n("si", "k", 5, "user", "Susun item rencana")
c.n("a1", "k", 6, "call", "Sahkan dokumen (A1)")
c.n("m2", "s", 7, "merge")
c.n("te", "s", 8, "time", "Akhir periode lapor")
c.n("pr", "s", 9, "service", "Kirim pengingat realisasi")
c.n("ir", "p", 10, "user", "Isi realisasi item")
c.n("sk", "s", 11, "service", "Perbarui status kriteria")
c.n("d2", "s", 12, "dec")
c.n("br", "k", 12, "user", "Buat revisi rencana", col=0)
c.n("tk", "s", 13, "service", "Tandai rencana kedaluwarsa")
c.n("ct", "k", 14, "user", "Catat tinjauan rencana")
c.n("d3", "k", 15, "dec")
c.n("um", "k", 16, "user", "Ukur manfaat program", col=1)
c.n("m3", "k", 17, "merge")
c.n("tp", "k", 18, "user", "Tetapkan keputusan perbaikan")
c.n("s2", "s", 19, "service", "Perbarui status kriteria")
c.n("en", "s", 20, "final")
c.e("1", "st", "m0"); c.e("2", "m0", "d1")
c.e("3", "d1", "ag", "[jenis = pengembangan]", exit=(1, 0.5), entry=(0.5, 0))
c.e("4", "d1", "m1", "[strategis / tahunan / IKU]")
c.e("5", "ag", "m1", exit=(0.5, 1), entry=(1, 0.5))
c.e("6", "m1", "si"); c.e("7", "si", "a1")
c.e("8", "a1", "m2", exit=(1, 0.5), entry=(0.5, 0))
c.e("9", "m2", "te"); c.e("10", "te", "pr")
c.e("11", "pr", "ir", exit=(0, 0.5), entry=(0.5, 0)); c.e("12", "ir", "sk", exit=(0.5, 1), entry=(0, 0.5))
c.e("13", "sk", "d2")
c.e("14", "d2", "m2", "[periode masih berjalan]", [(c.lane_right("s", 24), c.cy(12)), (c.lane_right("s", 24), c.cy(7))], exit=(1, 0.5), entry=(1, 0.5))
c.e("15", "d2", "br", "[perlu revisi rencana]", exit=(0, 0.5), entry=(1, 0.5))
c.e("16", "br", "m0", "", [(c.lane_left("k", 24), c.cy(12)), (c.lane_left("k", 24), c.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
c.e("17", "d2", "tk", "[periode berakhir]")
c.e("18", "tk", "ct", exit=(0, 0.5), entry=(1, 0.5)); c.e("19", "ct", "d3")
c.e("20", "d3", "um", "[jenis = pengembangan]", exit=(1, 0.5), entry=(0.5, 0))
c.e("21", "d3", "m3", "[lainnya]")
c.e("22", "um", "m3", exit=(0.5, 1), entry=(1, 0.5))
c.e("23", "m3", "tp"); c.e("24", "tp", "s2", exit=(1, 0.5), entry=(0, 0.5)); c.e("25", "s2", "en")
c.finish(21, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria PKG-01 / PKG-13</b><br>"
     "K1 disahkan: <i>Sahkan dokumen (A1)</i><br>"
     "K2 lengkap: <i>Susun item rencana</i> (+ <i>analisis gap</i> untuk PKG-13), dicek saat diajukan<br>"
     "K3 dijalankan: <i>Isi realisasi item</i><br>"
     "K4 ditinjau: <i>Catat tinjauan</i>, <i>Tetapkan keputusan perbaikan</i> (+ <i>Ukur manfaat</i> untuk PKG-13)", 120),
    ("<b>Siklus berikutnya</b>: keputusan perbaikan ditautkan ke rencana periode berikutnya, "
     "yang dimulai lagi dari awal diagram ini (record rencana baru).", 70),
    ("<b>Temuan</b>: <i>Kirim pengingat realisasi</i> belum ada di daftar kebutuhan (kandidat KF baru, opsional).", 60),
    ("Draf 13 Nov 2026 · Febriyan", 30),
])
pages.append(c)

# ------------------------------------------------------------------ A4
d = Activity("tk-act-a4", "Activity TO-BE A4 - Siklus Struktur", "tk-act-a4-",
             "A4 · Siklus Struktur Organisasi (PKG-03), satu masa SK",
             [("k", "KaLab", 300, 1), ("s", "Sistem", 300, 1)])
d.n("st", "k", 0, "start")
d.n("lj", "k", 1, "user", "Lengkapi uraian jabatan")
d.n("ss", "k", 2, "user", "Susun SK penetapan pengelola")
d.n("a1", "k", 3, "call", "Sahkan dokumen (A1)<br>pengesah: Dekan")
d.n("bp", "s", 4, "service", "Berlakukan penugasan jabatan")
d.n("m1", "s", 5, "merge")
d.n("te", "s", 6, "time", "Jadwal rapat koordinasi")
d.n("rk", "k", 7, "user", "Catat rapat koordinasi")
d.n("d1", "k", 8, "dec")
d.n("ev", "k", 9, "user", "Catat evaluasi struktur")
d.n("sk", "s", 10, "service", "Perbarui status kriteria")
d.n("d2", "s", 11, "dec")
d.n("tt", "s", 12, "service", "Tutup masa SK")
d.n("en", "s", 13, "final")
d.e("1", "st", "lj"); d.e("2", "lj", "ss"); d.e("3", "ss", "a1")
d.e("4", "a1", "bp", exit=(1, 0.5), entry=(0.5, 0)); d.e("5", "bp", "m1"); d.e("6", "m1", "te")
d.e("7", "te", "rk", exit=(0, 0.5), entry=(0.5, 0)); d.e("8", "rk", "d1")
d.e("9", "d1", "m1", "[belum waktunya evaluasi]", [(d.lane_right("s", 40), d.cy(8)), (d.lane_right("s", 40), d.cy(5))], exit=(1, 0.5), entry=(1, 0.5))
d.e("10", "d1", "ev", "[waktunya evaluasi]")
d.e("11", "ev", "sk", exit=(1, 0.5), entry=(0, 0.5)); d.e("12", "sk", "d2")
d.e("13", "d2", "m1", "[struktur tetap, masa SK berjalan]", [(d.lane_right("s", 20), d.cy(11)), (d.lane_right("s", 20), d.cy(5) + 8)], exit=(1, 0.5), entry=(1, 0.75))
d.e("14", "d2", "tt", "[perlu perubahan atau masa SK berakhir]")
d.e("15", "tt", "en")
d.finish(14, [
    (LEGEND, 150),
    ("<b>Kaitan ke kriteria PKG-03</b><br>"
     "K1 disahkan: <i>Sahkan dokumen (A1)</i><br>"
     "K2 lengkap: <i>Lengkapi uraian jabatan</i> (tugas, wewenang, atasan, pengganti)<br>"
     "K3 dijalankan: <i>Catat rapat koordinasi</i><br>"
     "K4 dievaluasi: <i>Catat evaluasi struktur</i>", 110),
    ("<b>Siklus berikutnya</b>: setelah <i>Tutup masa SK</i>, SK baru disusun dari awal diagram ini; "
     "evaluasi ditautkan ke SK baru. SK lama berstatus Diganti atau Kedaluwarsa (lihat S1).", 80),
    ("<b>[KONFIRMASI]</b> Frekuensi rapat koordinasi dan evaluasi struktur belum diketahui (wawancara KaLab).", 60),
    ("Draf 13 Nov 2026 · Febriyan", 30),
])
pages.append(d)

# ------------------------------------------------------------------ state machines
STATE = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#333333;"
STATE_T = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#EEEEEE;strokeColor=#333333;"
TR = ("endArrow=open;endSize=9;html=1;rounded=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#333333;"
      "edgeStyle=orthogonalEdgeStyle;")
TRN = "endArrow=open;endSize=9;html=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#9B2C44;edgeStyle=orthogonalEdgeStyle;rounded=1;"

s1 = Page("tk-stm-s1", "State Machine S1 - Status Dokumen", "tk-stm-s1-")
s1.v("title", "S1 · State machine status dokumen terkendali (<code>approval.mixin.state</code>): Rencana, SK Penetapan, Versi SOP/IK",
     TITLE, 40, 16, 1500, 40)
s1.v("init", "", ST["start"], 50, 238, 24, 24)
s1.v("draf", "Draf", STATE, 130, 225, 150, 50)
s1.v("aju", "Diajukan", STATE, 520, 225, 150, 50)
s1.v("prk", "Diperiksa", STATE, 520, 470, 150, 50)
s1.v("sah", "Disahkan<br><font style='font-size:10px;font-weight:normal'>(versi berlaku)</font>", STATE, 960, 225, 160, 50)
s1.v("gnt", "Diganti", STATE_T, 1330, 100, 150, 50)
s1.v("cbt", "Dicabut", STATE_T, 1330, 225, 150, 50)
s1.v("kdl", "Kedaluwarsa", STATE_T, 1330, 350, 150, 50)
s1.v("f0", "", ST["final"], 191, 420, 28, 28)
s1.v("f1", "", ST["final"], 1580, 111, 28, 28)
s1.v("f2", "", ST["final"], 1580, 236, 28, 28)
s1.v("f3", "", ST["final"], 1580, 361, 28, 28)
s1.e("t0", "init", "draf", "buat", style=TR)
s1.e("t1", "draf", "aju", "ajukan [kelengkapan terpenuhi]<br>/ catat tanggal_ajukan, kirim notifikasi", style=TR, exit=(1, 0.3), entry=(0, 0.3))
s1.e("t2", "aju", "draf", "tarik kembali / catat alasan", [(595, 170), (205, 170)], style=TRN, exit=(0.5, 0), entry=(0.5, 0))
s1.e("t3", "aju", "draf", "kembalikan / catat alasan", style=TRN, exit=(0, 0.75), entry=(1, 0.75))
s1.e("t4", "aju", "prk", "periksa [pemeriksaan aktif]<br>/ catat pemeriksa", style=TR, exit=(0.5, 1), entry=(0.5, 0))
s1.e("t5", "prk", "draf", "kembalikan / catat alasan", [(205, 495)], style=TRN, exit=(0, 0.5), entry=(0.5, 1))
s1.e("t6", "aju", "sah", "sahkan [pemeriksaan tidak aktif<br>∧ berkas TTD ada ∧ jabatan berwenang]<br>/ catat pengesah, tanggal_sah", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s1.e("t7", "prk", "sah", "sahkan [berkas TTD ada ∧ jabatan berwenang]<br>/ catat pengesah, tanggal_sah", [(1040, 495)], style=TR, exit=(1, 0.5), entry=(0.5, 1))
s1.e("t8", "sah", "gnt", "revisi baru disahkan", [(1040, 125)], style=TR, exit=(0.5, 0), entry=(0, 0.5))
s1.e("t9", "sah", "cbt", "cabut [jabatan berwenang]<br>/ catat alasan", style=TRN, exit=(1, 0.5), entry=(0, 0.5))
s1.e("t10", "sah", "kdl", "when(tanggal_selesai &lt; hari ini)<br>[dokumen berperiode]", [(1080, 375)], style=TRN, exit=(0.75, 1), entry=(0, 0.5))
s1.e("t11", "draf", "f0", "hapus [belum pernah diajukan]", style=TRN, exit=(0.5, 1), entry=(0.5, 0))
for i, src in enumerate(["gnt", "cbt", "kdl"], 1):
    s1.e(f"tf{i}", src, f"f{i}", style=TR)
s1.v("n1", "<b>Notasi</b> (Wazlawick 2024, §3.3): <code>event [guard] / efek</code>. Abu-abu = status akhir. "
     "<font color='#9B2C44'><b>Garis merah</b></font> = transisi yang <b>baru ditemukan</b> lewat tabel status × transisi "
     "dan belum ada di analisis maupun class diagram sebelumnya.", NOTE, 40, 580, 560, 70)
s1.v("n2", "<b>Penyatuan status</b> dari tiga analisis yang berbeda:<br>"
     "• PKG-01: draf/diajukan/disahkan/kedaluwarsa<br>• PKG-02: draf/diajukan/<b>berlaku</b>/dicabut → berlaku = Disahkan<br>"
     "• PKG-13: draf/diajukan/disahkan/diganti/<b>selesai</b> → selesai = Kedaluwarsa<br>"
     "• Diperiksa: dari dokumen lab (Disusun/Diperiksa/Disahkan)", NOTE, 620, 580, 470, 110)
s1.v("n3", "<b>Berlaku untuk</b>: Rencana (semua jenis), SK Penetapan → semua transisi.<br>"
     "Versi SOP/IK → semua kecuali <i>Kedaluwarsa</i> (tidak berperiode; kemutakhirannya diatur jadwal tinjau ulang, lihat S2).", NOTE, 1110, 580, 420, 90)
s1.v("n4", "<b>[KONFIRMASI]</b> Apakah dokumen Dicabut/Kedaluwarsa boleh diaktifkan kembali? "
     "Untuk sekarang dianggap status akhir; dokumen baru dibuat sebagai revisi.", NOTE, 40, 670, 560, 60)
s1.w, s1.h = 1700, 780
pages.append(s1)

s2 = Page("tk-stm-s2", "State Machine S2 - Kemutakhiran Versi SOP-IK", "tk-stm-s2-")
s2.v("title", "S2 · State machine kemutakhiran versi SOP/IK yang sedang berlaku (rincian status Disahkan di S1)", TITLE, 40, 16, 1400, 40)
s2.v("pre", "Diajukan / Diperiksa", STATE, 40, 255, 160, 50)
s2.v("cmp", "Disahkan (versi berlaku)", "swimlane;rounded=1;arcSize=6;html=1;startSize=30;fontStyle=1;fontSize=13;"
     "fillColor=#F5F0FF;strokeColor=#333333;swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;", 290, 80, 860, 420)
s2.v("init", "", ST["start"], 330, 268, 24, 24)
s2.v("mut", "Mutakhir", STATE, 420, 255, 160, 50)
s2.v("ptn", "Perlu Ditinjau", STATE, 820, 160, 170, 50)
s2.v("mrv", "Menunggu Revisi", STATE, 820, 370, 170, 50)
s2.v("gnt", "Diganti", STATE_T, 1270, 160, 150, 50)
s2.v("cbt", "Dicabut", STATE_T, 1270, 370, 150, 50)
s2.e("t0", "pre", "cmp", "sahkan (S1)", style=TR, exit=(1, 0.5), entry=(0, 0.465))
s2.e("t1", "init", "mut", "/ hitung tanggal_tinjau_berikutnya", style=TR)
s2.e("t2", "mut", "ptn", "when(tanggal_tinjau_berikutnya terlewati)<br>/ kirim pengingat", [(500, 185)], style=TR, exit=(0.5, 0), entry=(0, 0.5))
s2.e("t3", "ptn", "mut", "tinjau [hasil = tetap berlaku]<br>/ perbarui tanggal_tinjau_berikutnya", [(905, 280)], style=TR, exit=(0.5, 1), entry=(1, 0.5))
s2.e("t4", "ptn", "mrv", "tinjau [hasil = perlu revisi]", [(960, 300)], style=TR, exit=(0.8, 1), entry=(0.8, 0))
s2.e("t5", "mut", "mrv", "tinjau [hasil = perlu revisi]", [(500, 395)], style=TR, exit=(0.5, 1), entry=(0, 0.5))
s2.e("t6", "mut", "mut", "tinjau [hasil = tetap berlaku]<br>/ perbarui tanggal_tinjau_berikutnya", [(440, 340), (380, 340), (380, 295)], style=TR, exit=(0.15, 1), entry=(0, 0.8))
s2.e("t7", "cmp", "gnt", "versi baru disahkan", style=TR, exit=(1, 0.2), entry=(0, 0.5))
s2.e("t8", "cmp", "cbt", "cabut [jabatan berwenang]", style=TR, exit=(1, 0.7), entry=(0, 0.5))
s2.v("n1", "<b>Kaitan ke PKG-02 S3 (mutakhir)</b>: versi dihitung <b>mutakhir</b> selama tidak berada di <i>Perlu Ditinjau</i>.<br>"
     "<b>[KONFIRMASI]</b> Apakah <i>Menunggu Revisi</i> masih dihitung mutakhir? Usulan penulis: ya sampai tenggat revisi, "
     "karena tinjauan sudah dilakukan.", NOTE, 40, 540, 560, 90)
s2.v("n2", "<b>Implementasi</b> (Wazlawick §9.3, <i>modal class</i>): sub-status ini <b>tidak</b> disimpan di field <code>state</code>. "
     "<i>Perlu Ditinjau</i> = <code>is_perlu_tinjau</code> {compute}; <i>Menunggu Revisi</i> = hasil tinjauan terakhir "
     "<code>perlu_revisi</code> dan belum ada versi baru yang disahkan.", NOTE, 620, 540, 520, 90)
s2.v("n3", "Draf 13 Nov 2026 · Febriyan", NOTE, 1160, 540, 220, 30)
s2.w, s2.h = 1500, 680
pages.append(s2)

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(p.xml() for p in pages) + "</mxfile>")
