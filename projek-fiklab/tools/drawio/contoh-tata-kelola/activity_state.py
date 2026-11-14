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
          "• Ungu «call behavior» = memanggil activity lain<br>"
          "• ◇ keputusan/gabungan; kondisi ditulis [guard] di panah<br>"
          "• ⧗ = menunggu waktu tertentu<br>"
          "• Bar hitam = fork/join: semua cabang dikerjakan, urutannya bebas; alur lanjut setelah semua cabang selesai")
SRC = "Sumber: kebutuhan-tata-kelola.md (KF-01–45), brief Tata Kelola (cakupan Inti + Pelengkap).<br>Draf 14 Nov 2026 · Febriyan"

pages = []

# ------------------------------------------------------------------ A1
a = Activity("tk-act-a1", "Activity TO-BE (1-4) - Pengesahan Dokumen", "tk-act-a1-",
             "A1 · Pengesahan Dokumen (dipanggil oleh A2, A3, A4)",
             [("p", "Penyusun (KaLab / Laboran)", 300, 1), ("s", "Sistem", 290, 1),
              ("k", "KaLab (pencatat pengesahan)", 270, 1), ("g", "Pejabat penanda tangan (di luar sistem)", 290, 1)])
a.n("st", "p", 0, "start")
a.n("m0", "p", 1, "merge")
a.n("aj", "p", 2, "user", "Ajukan dokumen")
a.n("kl", "s", 3, "service", "Periksa kelengkapan isi dokumen")
a.n("d1", "s", 4, "dec")
a.n("lk", "p", 4, "user", "Lengkapi isi dokumen")
a.n("cp", "s", 5, "service", "Ubah status menjadi Diajukan")
a.n("d2", "s", 6, "dec")
a.n("tr", "p", 7, "user", "Terbitkan dokumen PDF")
a.n("hp", "s", 8, "service", "Hasilkan PDF dari isi dokumen")
a.n("m2", "p", 9, "merge")
a.n("ct", "p", 10, "manual", "Cetak dokumen")
a.n("td", "g", 11, "manual", "Tinjau isi dokumen cetak")
a.n("d3", "g", 12, "dec")
a.n("kb", "k", 12, "user", "Kembalikan dokumen")
a.n("u1", "s", 13, "service", "Ubah status menjadi Draf")
a.n("pb", "p", 14, "user", "Perbaiki dokumen")
a.n("tt", "g", 15, "manual", "Tanda tangani dokumen")
a.n("m3", "p", 16, "merge")
a.n("ug", "p", 17, "user", "Unggah PDF bertanda tangan")
a.n("sh", "k", 18, "user", "Sahkan dokumen")
a.n("vl", "s", 19, "service", "Periksa berkas dan wewenang pengesah")
a.n("d4", "s", 20, "dec")
a.n("us", "s", 21, "service", "Ubah status menjadi Disahkan")
a.n("gv", "s", 22, "service", "Ganti status dokumen lama")
a.n("cr", "s", 23, "service", "Catat riwayat pengesahan")
a.n("en", "s", 24, "final")
cp_ = a.cx("p", None)
a.e("1", "st", "m0"); a.e("2", "m0", "aj")
a.e("3", "aj", "kl", exit=(1, 0.5), entry=(0.5, 0)); a.e("4", "kl", "d1")
a.e("5", "d1", "lk", "[belum lengkap]", exit=(0, 0.5), entry=(1, 0.5))
a.e("6", "lk", "m0", "", [(a.lane_left("p", 18), a.cy(4)), (a.lane_left("p", 18), a.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
a.e("7", "d1", "cp", "[lengkap]"); a.e("8", "cp", "d2")
a.e("9", "d2", "tr", "[rencana / SK]", exit=(0, 0.5), entry=(0.5, 0))
a.e("10", "tr", "hp", exit=(1, 0.5), entry=(0.5, 0))
a.e("11", "hp", "m2", "", [(cp_, a.cy(8))], exit=(0, 0.5), entry=(0.5, 0))
a.e("12", "d2", "m2", "[SOP / IK / Renstra:<br>berkas sudah ada]", [(a.lane_right("s", 30), a.cy(6)), (a.lane_right("s", 30), a.cy(9))], exit=(1, 0.5), entry=(1, 0.5))
a.e("13", "m2", "ct")
a.e("14", "ct", "td", exit=(1, 0.5), entry=(0, 0.5)); a.e("15", "td", "d3")
a.e("16", "d3", "kb", "[tidak disetujui]", exit=(0, 0.5), entry=(1, 0.5))
a.e("17", "kb", "u1", "", [(a.cx("s", None), a.cy(12))], exit=(0, 0.5), entry=(0.5, 0))
a.e("18", "u1", "pb", "", [(cp_, a.cy(13))], exit=(0, 0.5), entry=(0.5, 0))
a.e("19", "pb", "m0", "", [(a.lane_left("p", 34), a.cy(14)), (a.lane_left("p", 34), a.cy(1) + 6)], exit=(0, 0.5), entry=(0, 0.75))
a.e("20", "d3", "tt", "[disetujui]")
a.e("21", "tt", "m3", "", [(cp_, a.cy(15))], exit=(0, 0.5), entry=(0.5, 0))
a.e("22", "m3", "ug")
a.e("23", "ug", "sh", exit=(1, 0.5), entry=(0, 0.5))
a.e("24", "sh", "vl", exit=(0, 0.5), entry=(1, 0.5)); a.e("25", "vl", "d4")
a.e("26", "d4", "m3", "[berkas belum ada /<br>pengesah tidak berwenang]", [(a.lane_left("s", 24), a.cy(20)), (a.lane_left("s", 24), a.cy(16))], exit=(0, 0.5), entry=(1, 0.5))
a.e("27", "d4", "us", "[valid]"); a.e("28", "us", "gv"); a.e("29", "gv", "cr"); a.e("30", "cr", "en")
a.finish(25, [
    (LEGEND, 165),
    ("<b>Aturan</b><br>"
     "• <i>Periksa kelengkapan isi</i>: isinya berbeda per jenis dokumen (KF-01, KF-30).<br>"
     "• <i>Periksa berkas dan wewenang</i>: PDF bertanda tangan harus ada dan pengesah tercatat harus memegang "
     "jabatan yang berwenang untuk jenis dokumen itu (KF-05).<br>"
     "• <i>Ganti status dokumen lama</i>: versi/revisi sebelumnya menjadi Diganti (KF-08).<br>"
     "• Setiap kejadian (diajukan, dikembalikan, berkas diunggah, disahkan) dicatat sebagai riwayat (KF-07).", 170),
    ("<b>Pejabat penanda tangan bukan aktor sistem</b> (keputusan 14 Nov 2026). Bisa Dekan atau KaLab sendiri; "
     "bila KaLab, lajur KaLab dan lajur pejabat diperankan orang yang sama. "
     "Pemeriksaan isi menyatu dengan penandatanganan; tidak ada tahap <i>Diperiksa</i>.", 100),
    ("<b>Terbitkan dokumen PDF</b>: rencana tahunan (KF-35, Inti); rencana pengembangan (KF-41) dan SK (KF-26) "
     "di lapis Pelengkap. Bila belum dibangun, PDF disiapkan di luar sistem seperti SOP/IK.", 90),
    ("Status dokumen di sepanjang alur ini: lihat <b>S1</b>.<br>" + SRC, 60),
])
pages.append(a)

# ------------------------------------------------------------------ A2
b = Activity("tk-act-a2", "Activity TO-BE (2-4) - Siklus SOP-IK", "tk-act-a2-",
             "A2 · Siklus Dokumen SOP/IK (PKG-02)",
             [("l", "Laboran / PLP", 480, 2), ("k", "KaLab", 250, 1), ("s", "Sistem", 290, 1)])
b.n("st", "l", 0, "start")
b.n("d1", "l", 1, "dec")
b.n("di", "l", 2, "user", "Daftarkan dokumen induk", col=1)
b.n("m1", "l", 3, "merge")
b.n("sn", "l", 4, "manual", "Susun naskah SOP/IK")
b.n("uv", "l", 5, "user", "Unggah versi dokumen")
b.n("a1", "l", 6, "call", "Sahkan dokumen (A1)")
b.n("ht", "s", 7, "service", "Hitung tanggal tinjau berikutnya")
b.n("fk", "l", 8, "fork")
b.n("cd", "l", 9, "user", "Catat distribusi dokumen", col=0)
b.n("cs", "l", 9, "user", "Catat sosialisasi dokumen", col=1)
b.n("jn", "l", 10, "fork")
b.n("m2", "s", 11, "merge")
b.n("te", "s", 12, "time", "Tanggal tinjau terlewati")
b.n("tp", "s", 13, "service", "Tandai versi perlu ditinjau")
b.n("tu", "l", 14, "user", "Tinjau ulang dokumen")
b.n("d2", "l", 15, "dec")
b.n("pj", "s", 15, "service", "Perbarui tanggal tinjau berikutnya")
b.n("cb", "k", 16, "user", "Cabut dokumen")
b.n("uc", "s", 17, "service", "Ubah status menjadi Dicabut")
b.n("en", "s", 18, "final")
b.e("1", "st", "d1")
b.e("2", "d1", "di", "[dokumen baru]", exit=(1, 0.5), entry=(0.5, 0))
b.e("3", "d1", "m1", "[revisi dokumen terdaftar]")
b.e("4", "di", "m1", exit=(0.5, 1), entry=(1, 0.5))
b.e("5", "m1", "sn"); b.e("6", "sn", "uv"); b.e("7", "uv", "a1")
b.e("8", "a1", "ht", exit=(1, 0.5), entry=(0.5, 0))
b.e("9", "ht", "fk", exit=(0, 0.5), entry=(0.5, 0))
# titik keluar/masuk di bar = posisi tengah kotak tugas (bar 420 px mulai x=70; kotak di x=160 dan x=400)
FL, FR = round((160 - 70) / 420, 3), round((400 - 70) / 420, 3)
b.e("10", "fk", "cd", exit=(FL, 1), entry=(0.5, 0)); b.e("11", "fk", "cs", exit=(FR, 1), entry=(0.5, 0))
b.e("12", "cd", "jn", exit=(0.5, 1), entry=(FL, 0)); b.e("13", "cs", "jn", exit=(0.5, 1), entry=(FR, 0))
b.e("14", "jn", "m2", exit=(1, 0.5), entry=(0, 0.5))
b.e("15", "m2", "te"); b.e("16", "te", "tp")
b.e("17", "tp", "tu", exit=(0, 0.5), entry=(1, 0.5)); b.e("18", "tu", "d2")
b.e("19", "d2", "pj", "[tetap berlaku]", exit=(1, 0.5), entry=(0, 0.5))
b.e("20", "pj", "m2", "", [(b.lane_right("s", 24), b.cy(15)), (b.lane_right("s", 24), b.cy(11))], exit=(1, 0.5), entry=(1, 0.5))
b.e("21", "d2", "m1", "[perlu revisi]", [(b.lane_left("l", 24), b.cy(15)), (b.lane_left("l", 24), b.cy(3))], exit=(0, 0.5), entry=(0, 0.5))
b.e("22", "d2", "cb", "[tidak diperlukan lagi]", exit=(0.5, 1), entry=(0.5, 0))
b.e("23", "cb", "uc", exit=(1, 0.5), entry=(0.5, 0)); b.e("24", "uc", "en")
b.finish(19, [
    (LEGEND, 165),
    ("<b>Kaitan ke kriteria PKG-02</b><br>"
     "S1 terdaftar: <i>Daftarkan dokumen induk</i> (KF-10)<br>"
     "S2 disahkan: <i>Unggah versi</i> (KF-11) + <i>Sahkan dokumen (A1)</i><br>"
     "S3 mutakhir: <i>Tinjau ulang</i> (KF-14) + tanggal tinjau (KF-15, lihat <b>S2</b>)<br>"
     "S4 tersedia: <i>Catat distribusi</i> (KF-12)<br>"
     "S5 disosialisasikan: <i>Catat sosialisasi</i> (KF-13)", 120),
    ("<b>Di luar sistem</b>: naskah SOP/IK disusun di Word/Docs (keputusan 13 Nov 2026). "
     "Sistem mengelola versi, pengesahan, distribusi, sosialisasi, dan tinjau ulang.", 80),
    ("<b>Tanpa pengingat terjadwal</b>: <i>Tandai versi perlu ditinjau</i> adalah penanda yang dihitung dari tanggal "
     "(KF-15), bukan notifikasi. <i>Tinjau ulang</i> juga boleh dilakukan sebelum tanggalnya tiba.", 90),
    ("Pengguna Lab membaca versi berlaku (KF-17, Pelengkap); tidak digambar karena bukan bagian alur ini.<br>" + SRC, 80),
])
pages.append(b)

# ------------------------------------------------------------------ A3
c = Activity("tk-act-a3", "Activity TO-BE (3-4) - Siklus Rencana", "tk-act-a3-",
             "A3 · Siklus Rencana Tahunan dan Rencana Pengembangan (PKG-01, PKG-13)",
             [("k", "KaLab", 470, 2), ("p", "PIC item (Laboran / KaLab)", 270, 1), ("s", "Sistem", 270, 1)])
c.n("st", "k", 0, "start")
c.n("d1", "k", 1, "dec")
c.n("cg", "k", 2, "user", "Catat temuan gap", col=1)
c.n("m1", "k", 3, "merge")
c.n("si", "k", 4, "user", "Susun item rencana")
c.n("a1", "k", 5, "call", "Sahkan dokumen (A1)")
c.n("m2", "s", 6, "merge")
c.n("te", "s", 7, "time", "Akhir periode lapor")
c.n("ir", "p", 8, "user", "Isi realisasi item")
c.n("d2", "s", 9, "dec")
c.n("br", "k", 9, "user", "Buat revisi rencana", col=0)
c.n("ct", "k", 10, "user", "Catat tinjauan rencana")
c.n("d3", "k", 11, "dec")
c.n("um", "k", 12, "user", "Catat ukuran manfaat", col=1)
c.n("m3", "k", 13, "merge")
c.n("en", "k", 14, "final")
c.e("1", "st", "d1")
c.e("2", "d1", "cg", "[jenis = pengembangan]", exit=(1, 0.5), entry=(0.5, 0))
c.e("3", "d1", "m1", "[jenis = tahunan]")
c.e("4", "cg", "m1", exit=(0.5, 1), entry=(1, 0.5))
c.e("5", "m1", "si"); c.e("6", "si", "a1")
c.e("7", "a1", "m2", exit=(1, 0.5), entry=(0.5, 0))
c.e("8", "m2", "te")
c.e("9", "te", "ir", exit=(0, 0.5), entry=(0.5, 0))
c.e("10", "ir", "d2", exit=(1, 0.5), entry=(0.5, 0))
c.e("11", "d2", "m2", "[periode rencana berjalan]", [(c.lane_right("s", 24), c.cy(9)), (c.lane_right("s", 24), c.cy(6))], exit=(1, 0.5), entry=(1, 0.5))
c.e("12", "d2", "br", "[perlu revisi rencana]", [(c.cx("k", 1) + 80, c.cy(9))], exit=(0, 0.5), entry=(1, 0.5))
c.e("13", "br", "m1", "", [(c.lane_left("k", 24), c.cy(9)), (c.lane_left("k", 24), c.cy(3))], exit=(0, 0.5), entry=(0, 0.5))
c.e("14", "d2", "ct", "[periode rencana berakhir]", [(c.cx("s", None), c.cy(10))], exit=(0.5, 1), entry=(1, 0.5))
c.e("15", "ct", "d3")
c.e("16", "d3", "um", "[jenis = pengembangan]", exit=(1, 0.5), entry=(0.5, 0))
c.e("17", "d3", "m3", "[jenis = tahunan]")
c.e("18", "um", "m3", exit=(0.5, 1), entry=(1, 0.5))
c.e("19", "m3", "en")
c.finish(15, [
    (LEGEND, 165),
    ("<b>Kaitan ke kriteria PKG-01 / PKG-13</b><br>"
     "K1 disahkan: <i>Sahkan dokumen (A1)</i><br>"
     "K2 lengkap: <i>Susun item rencana</i> (+ <i>Catat temuan gap</i> untuk PKG-13), dicek saat diajukan (KF-30)<br>"
     "K3 dijalankan: <i>Isi realisasi item</i> (KF-31)<br>"
     "K4 ditinjau: <i>Catat tinjauan rencana</i> (KF-32) (+ <i>Catat ukuran manfaat</i> untuk PKG-13, KF-40)", 130),
    ("<b>Siklus berikutnya</b>: rencana periode berikutnya dimulai lagi dari awal diagram ini sebagai rekaman baru. "
     "Keputusan tinjauan ditautkan ke rencana itu (KF-32).", 80),
    ("<b>Pelengkap</b>: <i>Buat revisi rencana</i> (KF-37). Bila tidak dibangun, cabang [perlu revisi rencana] tidak ada.<br>"
     "<b>Renstra</b> tidak punya siklus: diunggah (KF-28) lalu <i>Sahkan dokumen (A1)</i>. Tidak digambar (§3.4).", 100),
    ("<b>[KONFIRMASI KaLab]</b> Periode lapor realisasi per triwulan atau per semester.<br>" + SRC, 80),
])
pages.append(c)

# ------------------------------------------------------------------ A4
d = Activity("tk-act-a4", "Activity TO-BE (4-4) - Siklus Struktur", "tk-act-a4-",
             "A4 · Siklus Struktur Organisasi (PKG-03), satu masa SK",
             [("k", "KaLab", 420, 1)])
d.n("st", "k", 0, "start")
d.n("m0", "k", 1, "merge")
d.n("lj", "k", 2, "user", "Lengkapi data jabatan")
d.n("ss", "k", 3, "user", "Susun SK penetapan pengelola")
d.n("a1", "k", 4, "call", "Sahkan dokumen (A1)")
d.n("m1", "k", 5, "merge")
d.n("rk", "k", 6, "user", "Catat rapat koordinasi")
d.n("d1", "k", 7, "dec")
d.n("ev", "k", 8, "user", "Catat evaluasi struktur")
d.n("d2", "k", 9, "dec")
d.n("en", "k", 10, "final")
d.e("1", "st", "m0"); d.e("2", "m0", "lj"); d.e("3", "lj", "ss"); d.e("4", "ss", "a1"); d.e("5", "a1", "m1")
d.e("6", "m1", "rk"); d.e("7", "rk", "d1")
d.e("8", "d1", "m1", "[belum waktunya evaluasi]", [(d.lane_right("k", 70), d.cy(7)), (d.lane_right("k", 70), d.cy(5))], exit=(1, 0.5), entry=(1, 0.5))
d.e("9", "d1", "ev", "[waktunya evaluasi]")
d.e("10", "ev", "d2")
d.e("11", "d2", "m1", "[struktur tetap ∧<br>masa SK berjalan]", [(d.lane_right("k", 30), d.cy(9)), (d.lane_right("k", 30), d.cy(5) + 8)], exit=(1, 0.5), entry=(1, 0.75))
d.e("12", "d2", "m0", "[struktur perlu diubah]", [(d.lane_left("k", 30), d.cy(9)), (d.lane_left("k", 30), d.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
d.e("13", "d2", "en", "[masa SK berakhir]")
d.finish(11, [
    (LEGEND, 165),
    ("<b>Kaitan ke kriteria PKG-03</b><br>"
     "K1 disahkan: <i>Susun SK</i> (KF-21) + <i>Sahkan dokumen (A1)</i><br>"
     "K2 lengkap: <i>Lengkapi data jabatan</i>: tugas, wewenang, atasan, pengganti (KF-20)<br>"
     "K3 dijalankan: <i>Catat rapat koordinasi</i> (KF-22)<br>"
     "K4 dievaluasi: <i>Catat evaluasi struktur</i> (KF-23)", 120),
    ("<b>Struktur diubah</b>: SK revisi disusun dan disahkan; SK lama menjadi Diganti (S1). "
     "Evaluasi ditautkan ke SK atau jabatan yang direvisi. <b>Masa SK berakhir</b>: SK baru dimulai dari awal diagram.", 90),
    ("Satu lajur saja: semua tugas sistem di alur ini sudah ada di A1. Status kriteria K1–K4 dihitung saat dibaca (KF-44), "
     "bukan tugas di alur.", 70),
    ("<b>[KONFIRMASI KaLab]</b> Frekuensi rapat koordinasi dan evaluasi struktur.<br>" + SRC, 70),
])
pages.append(d)

# ------------------------------------------------------------------ state machines
STATE = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#333333;"
STATE_T = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#EEEEEE;strokeColor=#333333;"
TR = ("endArrow=open;endSize=9;html=1;rounded=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#333333;"
      "edgeStyle=orthogonalEdgeStyle;")
TRN = "endArrow=open;endSize=9;html=1;fontSize=10;labelBackgroundColor=#FFFFFF;strokeColor=#9B2C44;edgeStyle=orthogonalEdgeStyle;rounded=1;"
TRO = TR + "dashed=1;"

s1 = Page("tk-stm-s1", "State Machine TO-BE (1-2) - Status Dokumen", "tk-stm-s1-")
s1.v("title", "S1 · Status dokumen yang disahkan (<code>labfik.approval.mixin</code>): Renstra, Rencana, SK Penetapan, Versi SOP/IK",
     TITLE, 40, 16, 1500, 40)
s1.v("init", "", ST["start"], 50, 238, 24, 24)
s1.v("draf", "Draf", STATE, 130, 225, 150, 50)
s1.v("aju", "Diajukan", STATE, 540, 225, 150, 50)
s1.v("sah", "Disahkan<br><font style='font-size:10px;font-weight:normal'>(berlaku)</font>", STATE, 980, 225, 160, 50)
s1.v("gnt", "Diganti", STATE_T, 1340, 100, 150, 50)
s1.v("cbt", "Dicabut", STATE_T, 1340, 225, 150, 50)
s1.v("kdl", "Kedaluwarsa", STATE_T, 1340, 350, 150, 50)
s1.v("f0", "", ST["final"], 191, 400, 28, 28)
s1.v("f1", "", ST["final"], 1580, 111, 28, 28)
s1.v("f2", "", ST["final"], 1580, 236, 28, 28)
s1.v("f3", "", ST["final"], 1580, 361, 28, 28)
s1.e("t0", "init", "draf", "buat", style=TR)
s1.e("t1", "draf", "aju", "ajukan [isi lengkap]<br>/ catat riwayat", style=TR, exit=(1, 0.3), entry=(0, 0.3))
s1.e("t2", "aju", "draf", "kembalikan / catat alasan", style=TRN, exit=(0, 0.75), entry=(1, 0.75))
s1.e("t3", "aju", "aju", "unggah berkas bertanda tangan<br>/ catat riwayat", [(575, 160), (655, 160)], style=TRN, exit=(0.25, 0), entry=(0.75, 0))
s1.e("t4", "aju", "sah", "sahkan [berkas ada ∧ pengesah berwenang]<br>/ catat pengesah, pencatat, tanggal sah;<br>dokumen lama → Diganti", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s1.e("t5", "sah", "gnt", "revisi / versi baru disahkan", [(1060, 125)], style=TR, exit=(0.5, 0), entry=(0, 0.5))
s1.e("t6", "sah", "cbt", "cabut / catat alasan", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s1.e("t7", "sah", "kdl", "when(periode berakhir)<br>[dokumen berperiode]", [(1100, 375)], style=TRO, exit=(0.75, 1), entry=(0, 0.5))
s1.e("t8", "draf", "f0", "hapus [belum pernah diajukan]", style=TRN, exit=(0.5, 1), entry=(0.5, 0))
for i, src in enumerate(["gnt", "cbt", "kdl"], 1):
    s1.e(f"tf{i}", src, f"f{i}", style=TR)
s1.v("n1", "<b>Notasi</b> (Wazlawick 2024, §3.3): <code>event [guard] / efek</code>. Abu-abu = status akhir. "
     "<font color='#9B2C44'><b>Garis merah</b></font> = transisi yang tidak ada di analisis PKG dan baru ditemukan "
     "lewat tabel status × transisi. <b>Garis putus-putus</b> = lapis Pelengkap (Penjadwal, KF-09).", NOTE, 40, 480, 560, 90)
s1.v("n2", "<b>Penyatuan status</b> dari analisis:<br>"
     "• PKG-01: draf/diajukan/disahkan/kedaluwarsa<br>"
     "• PKG-02: berlaku → <b>Disahkan</b><br>"
     "• PKG-13: selesai → <b>Kedaluwarsa</b><br>"
     "• Diperiksa dihapus (keputusan 14 Nov 2026)", NOTE, 620, 480, 400, 110)
s1.v("n3", "<b>Berlaku untuk</b>: Renstra, Rencana, SK Penetapan → semua transisi.<br>"
     "Versi SOP/IK → semua kecuali <i>Kedaluwarsa</i> (tidak berperiode; kemutakhirannya di <b>S2</b>).<br>"
     "Tanpa KF-09, status tetap Disahkan, tetapi K1 \"masih berlaku\" dihitung dari tanggal periode (KF-44).", NOTE, 1040, 480, 470, 110)
s1.v("n4", "<b>[ASUMSI]</b> Dicabut, Diganti, dan Kedaluwarsa adalah status akhir. Dokumen tidak diaktifkan kembali; "
     "yang dibuat adalah revisi atau dokumen periode baru.<br>Draf 14 Nov 2026 · Febriyan", NOTE, 40, 590, 560, 70)
s1.w, s1.h = 1700, 700
pages.append(s1)

s2 = Page("tk-stm-s2", "State Machine TO-BE (2-2) - Kemutakhiran Versi SOP-IK", "tk-stm-s2-")
s2.v("title", "S2 · Kemutakhiran versi SOP/IK yang sedang berlaku (rincian status Disahkan di S1)", TITLE, 40, 16, 1400, 40)
s2.v("pre", "Diajukan (S1)", STATE, 40, 235, 150, 50)
s2.v("cmp", "Disahkan (S1)", "swimlane;rounded=1;arcSize=6;html=1;startSize=30;fontStyle=1;fontSize=13;"
     "fillColor=#F5F0FF;strokeColor=#333333;swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;", 280, 80, 820, 360)
s2.v("init", "", ST["start"], 320, 248, 24, 24)
s2.v("mut", "Mutakhir", STATE, 420, 235, 160, 50)
s2.v("ptn", "Perlu Ditinjau", STATE, 840, 235, 170, 50)
s2.v("gnt", "Diganti", STATE_T, 1220, 140, 150, 50)
s2.v("cbt", "Dicabut", STATE_T, 1220, 330, 150, 50)
s2.e("t0", "pre", "cmp", "sahkan (S1)", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s2.e("t1", "init", "mut", "/ hitung tanggal tinjau", style=TR)
s2.e("t2", "mut", "ptn", "when(tanggal tinjau terlewati)", [(500, 170), (925, 170)], style=TR, exit=(0.5, 0), entry=(0.5, 0))
s2.e("t3", "ptn", "mut", "tinjau [hasil = tetap berlaku]<br>/ perbarui tanggal tinjau", style=TR, exit=(0, 0.5), entry=(1, 0.5))
s2.e("t4", "mut", "mut", "tinjau [hasil = tetap berlaku]<br>/ perbarui tanggal tinjau", [(460, 360), (380, 360), (380, 275)], style=TR, exit=(0.25, 1), entry=(0, 0.8))
s2.e("t5", "cmp", "gnt", "versi baru disahkan", style=TR, exit=(1, 0.2), entry=(0, 0.5))
s2.e("t6", "cmp", "cbt", "cabut", style=TR, exit=(1, 0.75), entry=(0, 0.5))
s2.v("n1", "<b>Kaitan ke PKG-02 S3 (mutakhir)</b>: versi berlaku memenuhi S3 selama berada di <i>Mutakhir</i>, "
     "yaitu tanggal tinjau berikutnya belum terlewati.<br>"
     "<b>[ASUMSI]</b> Tinjauan dengan hasil <i>perlu revisi</i> tidak mengubah sub-status dan tidak memperbarui tanggal tinjau. "
     "Tinjauan itu memicu penyusunan versi baru (A2).", NOTE, 40, 480, 560, 110)
s2.v("n2", "<b>Implementasi</b> (Wazlawick §9.3, <i>modal class</i>, transisi stabil): sub-status <b>tidak</b> disimpan sebagai "
     "field <code>state</code>. <i>Perlu Ditinjau</i> dihitung dari tanggal tinjau berikutnya &lt; hari ini (KF-15). "
     "Tanpa pengingat terjadwal.", NOTE, 620, 480, 500, 90)
s2.v("n3", "Draf 14 Nov 2026 · Febriyan", NOTE, 1140, 480, 220, 30)
s2.w, s2.h = 1450, 640
pages.append(s2)

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(p.xml() for p in pages) + "</mxfile>")
