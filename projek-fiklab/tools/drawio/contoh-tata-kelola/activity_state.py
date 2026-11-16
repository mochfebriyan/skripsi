"""Activity diagram (A1-A4) dan state machine (S1-S2) modul Tata Kelola.

Gaya polos hitam-putih (keputusan Febriyan, 16 November 2026): tanpa warna isi dan tanpa garis
putus-putus. Jenis tugas dibedakan hanya lewat stereotype («user», «service», «manual»,
«call behavior» + simbol garpu). Halaman diagram tidak memuat catatan agar ringkas saat
disisipkan ke naskah; catatan kerja dikumpulkan di halaman terakhir.

Pemakaian: python3 activity_state.py <keluaran.drawio>
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
    """Baris boleh memuat beberapa node di lajur berbeda; panah antarlajur dalam satu baris mendatar."""
    LANE_Y, HEAD = 20, 30

    def __init__(self, pid, name, prefix, lanes, rows, small):
        super().__init__(pid, name, prefix)
        self.lanes, x = {}, 20
        for key, label, w, cols in lanes:
            self.lanes[key] = (x, w, cols, label)
            x += w
        self.total_w = x - 20
        self.rows = rows
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

    def n(self, id, lane, row, kind, label="", col=None, w=None):
        cx, cy = self.cx(lane, col), self.cy(row)
        if kind == "fork":
            ww, hh = (w or self.lanes[lane][1] - 40), 6
        else:
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
          "«manual» = di luar sistem; «call behavior» (simbol garpu) = memanggil activity lain; ◇ = keputusan/gabungan, "
          "kondisi ditulis [guard] di panah; ⧗ = menunggu waktu; bar hitam = fork/join. Gaya polos hitam-putih "
          "(keputusan Febriyan, 16 Nov 2026).")
SRC = "Sumber: kebutuhan-tata-kelola.md (KF-01–45), brief Tata Kelola (cakupan Inti + Pelengkap). Draf 14 Nov 2026, tata letak 16 Nov 2026 · Febriyan"

pages, notes = [], []

# ------------------------------------------------------------------ A1
a = Activity("tk-act-a1", "Activity TO-BE (1-4) - Pengesahan Dokumen", "tk-act-a1-",
             [("p", "Penyusun (KaLab / Laboran)", 260, 1), ("s", "Sistem", 220, 1),
              ("k", "KaLab (pencatat pengesahan)", 220, 1), ("g", "Pejabat penanda tangan (di luar sistem)", 220, 1)],
             rows=19, small={0, 1, 5, 7, 11, 14, 18})
a.n("st", "p", 0, "start")
a.n("m0", "p", 1, "merge")
a.n("aj", "p", 2, "user", "Ajukan dokumen")
a.n("kl", "s", 2, "service", "Periksa kelengkapan isi dokumen")
a.n("lk", "p", 3, "user", "Lengkapi isi dokumen")
a.n("d1", "s", 3, "dec")
a.n("cp", "s", 4, "service", "Ubah status menjadi Diajukan")
a.n("d2", "s", 5, "dec")
a.n("tr", "p", 6, "user", "Terbitkan dokumen PDF")
a.n("hp", "s", 6, "service", "Hasilkan PDF dari isi dokumen")
a.n("m2", "p", 7, "merge")
a.n("ct", "p", 8, "manual", "Cetak dokumen")
a.n("td", "g", 8, "manual", "Tinjau isi dokumen cetak")
a.n("kb", "k", 9, "user", "Kembalikan dokumen")
a.n("d3", "g", 9, "dec")
a.n("pb", "p", 10, "user", "Perbaiki dokumen")
a.n("u1", "s", 10, "service", "Ubah status menjadi Draf")
a.n("tt", "g", 10, "manual", "Tanda tangani dokumen")
a.n("m3", "p", 11, "merge")
a.n("ug", "p", 12, "user", "Unggah PDF bertanda tangan")
a.n("sh", "k", 12, "user", "Sahkan dokumen")
a.n("vl", "s", 13, "service", "Periksa berkas dan wewenang pengesah")
a.n("d4", "s", 14, "dec")
a.n("us", "s", 15, "service", "Ubah status menjadi Disahkan")
a.n("gv", "s", 16, "service", "Ganti status dokumen lama")
a.n("cr", "s", 17, "service", "Catat riwayat pengesahan")
a.n("en", "s", 18, "final")
cp_, cs_ = a.cx("p", None), a.cx("s", None)
a.e("1", "st", "m0"); a.e("2", "m0", "aj")
a.e("3", "aj", "kl", exit=(1, 0.5), entry=(0, 0.5)); a.e("4", "kl", "d1")
a.e("5", "d1", "lk", "[belum lengkap]", exit=(0, 0.5), entry=(1, 0.5))
a.e("6", "lk", "m0", "", [(a.lane_left("p", 12), a.cy(3)), (a.lane_left("p", 12), a.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
a.e("7", "d1", "cp", "[lengkap]"); a.e("8", "cp", "d2")
a.e("9", "d2", "tr", "[rencana / SK]", [(cp_, a.cy(5))], exit=(0, 0.5), entry=(0.5, 0))
a.e("10", "tr", "hp", exit=(1, 0.5), entry=(0, 0.5))
a.e("11", "hp", "m2", "", [(cs_, a.cy(7))], exit=(0.5, 1), entry=(1, 0.5))
a.e("12", "d2", "m2", "[SOP / IK / Renstra]", [(a.lane_right("s", 12), a.cy(5)), (a.lane_right("s", 12), a.cy(7.45)), (cp_, a.cy(7.45))],
    exit=(1, 0.5), entry=(0.5, 1))
a.e("13", "m2", "ct")
a.e("14", "ct", "td", exit=(1, 0.5), entry=(0, 0.5)); a.e("15", "td", "d3")
a.e("16", "d3", "kb", "[tidak disetujui]", exit=(0, 0.5), entry=(1, 0.5))
a.e("17", "kb", "u1", "", [(a.cx("k", None), a.cy(10))], exit=(0.5, 1), entry=(1, 0.5))
a.e("18", "u1", "pb", exit=(0, 0.5), entry=(1, 0.5))
a.e("19", "pb", "m0", "", [(a.lane_left("p", 24), a.cy(10)), (a.lane_left("p", 24), a.cy(1) + 6)], exit=(0, 0.5), entry=(0, 0.75))
a.e("20", "d3", "tt", "[disetujui]")
a.e("21", "tt", "m3", "", [(a.cx("g", None), a.cy(10.85)), (cp_, a.cy(10.85))], exit=(0.5, 1), entry=(0.5, 0))
a.e("22", "m3", "ug")
a.e("23", "ug", "sh", exit=(1, 0.5), entry=(0, 0.5))
a.e("24", "sh", "vl", "", [(a.cx("k", None), a.cy(13))], exit=(0.5, 1), entry=(1, 0.5))
a.e("25", "vl", "d4")
a.e("26", "d4", "m3", "[berkas belum ada /<br>pengesah tidak berwenang]", [(a.lane_left("s", 8), a.cy(14)), (a.lane_left("s", 8), a.cy(11))],
    exit=(0, 0.5), entry=(1, 0.5))
a.e("27", "d4", "us", "[valid]"); a.e("28", "us", "gv"); a.e("29", "gv", "cr"); a.e("30", "cr", "en")
a.finish()
pages.append(a)
notes.append(("A1 · Pengesahan Dokumen (dipanggil oleh A2, A3, A4)", [
    ("<b>Aturan</b><br>• <i>Periksa kelengkapan isi</i>: isinya berbeda per jenis dokumen (KF-01, KF-30).<br>"
     "• <i>Periksa berkas dan wewenang</i>: PDF bertanda tangan harus ada dan pengesah tercatat harus memegang "
     "jabatan yang berwenang untuk jenis dokumen itu (KF-05).<br>"
     "• <i>Ganti status dokumen lama</i>: versi/revisi sebelumnya menjadi Diganti (KF-08).<br>"
     "• Setiap kejadian (diajukan, dikembalikan, berkas diunggah, disahkan) dicatat sebagai riwayat (KF-07).", 150),
    ("<b>Pejabat penanda tangan bukan aktor sistem</b> (keputusan 14 Nov 2026). Bisa Dekan atau KaLab sendiri; "
     "bila KaLab, lajur KaLab dan lajur pejabat diperankan orang yang sama. "
     "Pemeriksaan isi menyatu dengan penandatanganan; tidak ada tahap <i>Diperiksa</i>.", 90),
    ("<b>Terbitkan dokumen PDF</b>: rencana tahunan (KF-35, Inti); rencana pengembangan (KF-41) dan SK (KF-26) "
     "di lapis Pelengkap. Bila belum dibangun, PDF disiapkan di luar sistem seperti SOP/IK.", 80),
    ("Status dokumen di sepanjang alur ini: lihat <b>S1</b>.", 40),
]))

# ------------------------------------------------------------------ A2
b = Activity("tk-act-a2", "Activity TO-BE (2-4) - Siklus SOP-IK", "tk-act-a2-",
             [("l", "Laboran / PLP", 470, 2), ("k", "KaLab", 220, 1), ("s", "Sistem", 220, 1)],
             rows=15, small={0, 1, 3, 7, 9, 10, 12, 14})
b.n("st", "l", 0, "start")
b.n("d1", "l", 1, "dec")
b.n("di", "l", 2, "user", "Daftarkan dokumen induk", col=1)
b.n("m1", "l", 3, "merge")
b.n("sn", "l", 4, "manual", "Susun naskah SOP/IK")
b.n("uv", "l", 5, "user", "Unggah versi dokumen")
b.n("a1", "l", 6, "call", "Sahkan dokumen (A1)")
b.n("ht", "s", 6, "service", "Hitung tanggal tinjau berikutnya")
b.n("fk", "l", 7, "fork")
b.n("cd", "l", 8, "user", "Catat distribusi dokumen", col=0)
b.n("cs", "l", 8, "user", "Catat sosialisasi dokumen", col=1)
b.n("jn", "l", 9, "fork")
b.n("m2", "s", 9, "merge")
b.n("te", "s", 10, "time", "Tanggal tinjau terlewati")
b.n("tu", "l", 11, "user", "Tinjau ulang dokumen")
b.n("tp", "s", 11, "service", "Tandai versi perlu ditinjau")
b.n("d2", "l", 12, "dec")
b.n("pj", "s", 12, "service", "Perbarui tanggal tinjau berikutnya")
b.n("cb", "k", 13, "user", "Cabut dokumen")
b.n("uc", "s", 13, "service", "Ubah status menjadi Dicabut")
b.n("en", "s", 14, "final")
b.e("1", "st", "d1")
b.e("2", "d1", "di", "[dokumen baru]", exit=(1, 0.5), entry=(0.5, 0))
b.e("3", "d1", "m1", "[revisi dokumen terdaftar]")
b.e("4", "di", "m1", exit=(0.5, 1), entry=(1, 0.5))
b.e("5", "m1", "sn"); b.e("6", "sn", "uv"); b.e("7", "uv", "a1")
b.e("8", "a1", "ht", exit=(1, 0.5), entry=(0, 0.5))
b.e("9", "ht", "fk", "", [(b.cx("s", None), b.cy(7))], exit=(0.5, 1), entry=(1, 0.5))
# titik keluar/masuk di bar fork/join = posisi tengah kotak kolom 0 dan 1 (bar selebar lajur dikurangi 40 px)
bx0, bw = b.lanes["l"][0] + 20, b.lanes["l"][1] - 40
FL, FR = round((b.cx("l", 0) - bx0) / bw, 3), round((b.cx("l", 1) - bx0) / bw, 3)
b.e("10", "fk", "cd", exit=(FL, 1), entry=(0.5, 0)); b.e("11", "fk", "cs", exit=(FR, 1), entry=(0.5, 0))
b.e("12", "cd", "jn", exit=(0.5, 1), entry=(FL, 0)); b.e("13", "cs", "jn", exit=(0.5, 1), entry=(FR, 0))
b.e("14", "jn", "m2", exit=(1, 0.5), entry=(0, 0.5))
b.e("15", "m2", "te"); b.e("16", "te", "tp")
b.e("17", "tp", "tu", exit=(0, 0.5), entry=(1, 0.5)); b.e("18", "tu", "d2")
b.e("19", "d2", "pj", "[tetap berlaku]", exit=(1, 0.5), entry=(0, 0.5))
b.e("20", "pj", "m2", "", [(b.lane_right("s", 10), b.cy(12)), (b.lane_right("s", 10), b.cy(9))], exit=(1, 0.5), entry=(1, 0.5))
b.e("21", "d2", "m1", "[perlu revisi]", [(b.lane_left("l", 8), b.cy(12)), (b.lane_left("l", 8), b.cy(3))], exit=(0, 0.5), entry=(0, 0.5))
b.e("22", "d2", "cb", "[tidak diperlukan lagi]", [(b.cx("l", None), b.cy(13))], exit=(0.5, 1), entry=(0, 0.5))
b.e("23", "cb", "uc", exit=(1, 0.5), entry=(0, 0.5)); b.e("24", "uc", "en")
b.finish()
pages.append(b)
notes.append(("A2 · Siklus Dokumen SOP/IK (PKG-02)", [
    ("<b>Kaitan ke kriteria PKG-02</b><br>S1 terdaftar: <i>Daftarkan dokumen induk</i> (KF-10)<br>"
     "S2 disahkan: <i>Unggah versi</i> (KF-11) + <i>Sahkan dokumen (A1)</i><br>"
     "S3 mutakhir: <i>Tinjau ulang</i> (KF-14) + tanggal tinjau (KF-15, lihat <b>S2</b>)<br>"
     "S4 tersedia: <i>Catat distribusi</i> (KF-12)<br>S5 disosialisasikan: <i>Catat sosialisasi</i> (KF-13)", 110),
    ("<b>Di luar sistem</b>: naskah SOP/IK disusun di Word/Docs (keputusan 13 Nov 2026). "
     "Sistem mengelola versi, pengesahan, distribusi, sosialisasi, dan tinjau ulang.", 70),
    ("<b>Tanpa pengingat terjadwal</b>: <i>Tandai versi perlu ditinjau</i> adalah penanda yang dihitung dari tanggal "
     "(KF-15), bukan notifikasi. <i>Tinjau ulang</i> juga boleh dilakukan sebelum tanggalnya tiba.", 80),
    ("Pengguna Lab membaca versi berlaku (KF-17, Pelengkap); tidak digambar karena bukan bagian alur ini.", 50),
]))

# ------------------------------------------------------------------ A3
c = Activity("tk-act-a3", "Activity TO-BE (3-4) - Siklus Rencana", "tk-act-a3-",
             [("k", "KaLab", 470, 2), ("p", "PIC item (Laboran / KaLab)", 220, 1), ("s", "Sistem", 220, 1)],
             rows=14, small={0, 1, 3, 6, 10, 12, 13})
c.n("st", "k", 0, "start")
c.n("d1", "k", 1, "dec")
c.n("cg", "k", 2, "user", "Catat temuan gap", col=1)
c.n("m1", "k", 3, "merge")
c.n("si", "k", 4, "user", "Susun item rencana")
c.n("a1", "k", 5, "call", "Sahkan dokumen (A1)")
c.n("m2", "s", 5, "merge")
c.n("te", "s", 6, "time", "Akhir periode lapor")
c.n("ir", "p", 7, "user", "Isi realisasi item")
c.n("br", "k", 8, "user", "Buat revisi rencana", col=0)
c.n("d2", "s", 8, "dec")
c.n("ct", "k", 9, "user", "Catat tinjauan rencana")
c.n("d3", "k", 10, "dec")
c.n("um", "k", 11, "user", "Catat ukuran manfaat", col=1)
c.n("m3", "k", 12, "merge")
c.n("en", "k", 13, "final")
c.e("1", "st", "d1")
c.e("2", "d1", "cg", "[jenis = pengembangan]", exit=(1, 0.5), entry=(0.5, 0))
c.e("3", "d1", "m1", "[jenis = tahunan]")
c.e("4", "cg", "m1", exit=(0.5, 1), entry=(1, 0.5))
c.e("5", "m1", "si"); c.e("6", "si", "a1")
c.e("7", "a1", "m2", exit=(1, 0.5), entry=(0, 0.5))
c.e("8", "m2", "te")
c.e("9", "te", "ir", "", [(c.cx("s", None), c.cy(6.5)), (c.cx("p", None), c.cy(6.5))], exit=(0.5, 1), entry=(0.5, 0))
c.e("10", "ir", "d2", "", [(c.cx("s", None), c.cy(7))], exit=(1, 0.5), entry=(0.5, 0))
c.e("11", "d2", "m2", "[periode rencana<br>berjalan]", [(c.lane_right("s", 10), c.cy(8)), (c.lane_right("s", 10), c.cy(5))], exit=(1, 0.5), entry=(1, 0.5))
c.e("12", "d2", "br", "[perlu revisi rencana]", exit=(0, 0.5), entry=(1, 0.5))
c.e("13", "br", "m1", "", [(c.lane_left("k", 14), c.cy(8)), (c.lane_left("k", 14), c.cy(3))], exit=(0, 0.5), entry=(0, 0.5))
c.e("14", "d2", "ct", "[periode rencana berakhir]", [(c.cx("s", None), c.cy(9))], exit=(0.5, 1), entry=(1, 0.5))
c.e("15", "ct", "d3")
c.e("16", "d3", "um", "[jenis = pengembangan]", exit=(1, 0.5), entry=(0.5, 0))
c.e("17", "d3", "m3", "[jenis = tahunan]")
c.e("18", "um", "m3", exit=(0.5, 1), entry=(1, 0.5))
c.e("19", "m3", "en")
c.finish()
pages.append(c)
notes.append(("A3 · Siklus Rencana Tahunan dan Rencana Pengembangan (PKG-01, PKG-13)", [
    ("<b>Kaitan ke kriteria PKG-01 / PKG-13</b><br>K1 disahkan: <i>Sahkan dokumen (A1)</i><br>"
     "K2 lengkap: <i>Susun item rencana</i> (+ <i>Catat temuan gap</i> untuk PKG-13), dicek saat diajukan (KF-30)<br>"
     "K3 dijalankan: <i>Isi realisasi item</i> (KF-31)<br>"
     "K4 ditinjau: <i>Catat tinjauan rencana</i> (KF-32) (+ <i>Catat ukuran manfaat</i> untuk PKG-13, KF-40)", 120),
    ("<b>Siklus berikutnya</b>: rencana periode berikutnya dimulai lagi dari awal diagram ini sebagai rekaman baru. "
     "Keputusan tinjauan ditautkan ke rencana itu (KF-32).", 70),
    ("<b>Pelengkap</b>: <i>Buat revisi rencana</i> (KF-37). Bila tidak dibangun, cabang [perlu revisi rencana] tidak ada. "
     "<b>Renstra</b> tidak punya siklus: diunggah (KF-28) lalu <i>Sahkan dokumen (A1)</i>. Tidak digambar (§3.4).", 90),
    ("<b>[KONFIRMASI KaLab]</b> Periode lapor realisasi per triwulan atau per semester.", 40),
]))

# ------------------------------------------------------------------ A4
d = Activity("tk-act-a4", "Activity TO-BE (4-4) - Siklus Struktur", "tk-act-a4-",
             [("k", "KaLab", 420, 1)], rows=11, small={0, 1, 5, 7, 9, 10})
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
d.e("11", "d2", "m1", "[struktur tetap ∧<br>masa SK berjalan]", [(d.lane_right("k", 24), d.cy(9)), (d.lane_right("k", 24), d.cy(5) + 6)], exit=(1, 0.5), entry=(1, 0.75))
d.e("12", "d2", "m0", "[struktur perlu diubah]", [(d.lane_left("k", 24), d.cy(9)), (d.lane_left("k", 24), d.cy(1))], exit=(0, 0.5), entry=(0, 0.5))
d.e("13", "d2", "en", "[masa SK berakhir]")
d.finish()
pages.append(d)
notes.append(("A4 · Siklus Struktur Organisasi (PKG-03), satu masa SK", [
    ("<b>Kaitan ke kriteria PKG-03</b><br>K1 disahkan: <i>Susun SK</i> (KF-21) + <i>Sahkan dokumen (A1)</i><br>"
     "K2 lengkap: <i>Lengkapi data jabatan</i>: tugas, wewenang, atasan, pengganti (KF-20)<br>"
     "K3 dijalankan: <i>Catat rapat koordinasi</i> (KF-22)<br>K4 dievaluasi: <i>Catat evaluasi struktur</i> (KF-23)", 110),
    ("<b>Struktur diubah</b>: SK revisi disusun dan disahkan; SK lama menjadi Diganti (S1). "
     "Evaluasi ditautkan ke SK atau jabatan yang direvisi. <b>Masa SK berakhir</b>: SK baru dimulai dari awal diagram.", 80),
    ("Satu lajur saja: semua tugas sistem di alur ini sudah ada di A1. Status kriteria K1–K4 dihitung saat dibaca (KF-44), "
     "bukan tugas di alur.", 60),
    ("<b>[KONFIRMASI KaLab]</b> Frekuensi rapat koordinasi dan evaluasi struktur.", 40),
]))

# ------------------------------------------------------------------ state machines
STATE = "rounded=1;arcSize=30;whiteSpace=wrap;html=1;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
TR = ("endArrow=open;endSize=8;html=1;rounded=1;fontSize=11;labelBackgroundColor=#FFFFFF;strokeColor=#000000;"
      "edgeStyle=orthogonalEdgeStyle;" + FONT)

s1 = Page("tk-stm-s1", "State Machine TO-BE (1-2) - Status Dokumen", "tk-stm-s1-")
s1.v("init", "", ST["start"], 30, 168, 22, 22)
s1.v("draf", "Draf", STATE, 100, 154, 140, 50)
s1.v("aju", "Diajukan", STATE, 470, 154, 140, 50)
s1.v("sah", "Disahkan", STATE, 880, 154, 140, 50)
s1.v("gnt", "Diganti", STATE, 1210, 40, 140, 50)
s1.v("cbt", "Dicabut", STATE, 1210, 154, 140, 50)
s1.v("kdl", "Kedaluwarsa", STATE, 1210, 268, 140, 50)
s1.v("f0", "", ST["final"], 157, 310, 26, 26)
s1.v("f1", "", ST["final"], 1400, 52, 26, 26)
s1.v("f2", "", ST["final"], 1400, 166, 26, 26)
s1.v("f3", "", ST["final"], 1400, 280, 26, 26)
s1.e("t0", "init", "draf", "buat", style=TR)
s1.e("t1", "draf", "aju", "ajukan [isi lengkap]<br>/ catat riwayat", style=TR, exit=(1, 0.3), entry=(0, 0.3))
s1.e("t2", "aju", "draf", "kembalikan / catat alasan *", style=TR, exit=(0, 0.75), entry=(1, 0.75))
s1.e("t3", "aju", "aju", "unggah berkas bertanda tangan / catat riwayat *", [(505, 110), (575, 110)], style=TR, exit=(0.25, 0), entry=(0.75, 0))
s1.e("t4", "aju", "sah", "sahkan [berkas ada ∧ pengesah berwenang]<br>/ catat pengesah, pencatat, tanggal sah;<br>dokumen lama → Diganti",
     style=TR, exit=(1, 0.5), entry=(0, 0.5))
s1.e("t5", "sah", "gnt", "revisi / versi baru disahkan", [(950, 65)], style=TR, exit=(0.5, 0), entry=(0, 0.5))
s1.e("t6", "sah", "cbt", "cabut / catat alasan", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s1.e("t7", "sah", "kdl", "when(periode berakhir)<br>[dokumen berperiode]", [(985, 293)], style=TR, exit=(0.75, 1), entry=(0, 0.5))
s1.e("t8", "draf", "f0", "hapus [belum pernah diajukan] *", style=TR, exit=(0.5, 1), entry=(0.5, 0))
for i, src in enumerate(["gnt", "cbt", "kdl"], 1):
    s1.e(f"tf{i}", src, f"f{i}", style=TR)
s1.v("ket", "* transisi yang ditemukan melalui tabel status × transisi", "text;html=1;fontSize=11;align=left;" + FONT,
     30, 350, 420, 24)
s1.w, s1.h = 1460, 390
pages.append(s1)
notes.append(("S1 · Status dokumen yang disahkan (labfik.approval.mixin): Renstra, Rencana, SK Penetapan, Versi SOP/IK", [
    ("<b>Notasi</b> (Wazlawick 2024, §3.3): <code>event [guard] / efek</code>. Tanda * = transisi yang tidak ada di "
     "analisis PKG dan baru ditemukan lewat tabel status × transisi. Transisi <i>when(periode berakhir)</i> = lapis "
     "Pelengkap (Penjadwal, KF-09).", 80),
    ("<b>Penyatuan status</b> dari analisis: PKG-01 draf/diajukan/disahkan/kedaluwarsa; PKG-02 berlaku → <b>Disahkan</b>; "
     "PKG-13 selesai → <b>Kedaluwarsa</b>; Diperiksa dihapus (keputusan 14 Nov 2026).", 70),
    ("<b>Berlaku untuk</b>: Renstra, Rencana, SK Penetapan → semua transisi. Versi SOP/IK → semua kecuali "
     "<i>Kedaluwarsa</i> (tidak berperiode; kemutakhirannya di <b>S2</b>). Tanpa KF-09, status tetap Disahkan, tetapi "
     "K1 \"masih berlaku\" dihitung dari tanggal periode (KF-44).", 80),
    ("<b>[ASUMSI]</b> Dicabut, Diganti, dan Kedaluwarsa adalah status akhir. Dokumen tidak diaktifkan kembali; "
     "yang dibuat adalah revisi atau dokumen periode baru.", 60),
]))

s2 = Page("tk-stm-s2", "State Machine TO-BE (2-2) - Kemutakhiran Versi SOP-IK", "tk-stm-s2-")
s2.v("pre", "Diajukan (S1)", STATE, 20, 175, 140, 50)
s2.v("cmp", "Disahkan (S1)", "swimlane;rounded=1;arcSize=6;html=1;startSize=30;fontStyle=1;fontSize=12;"
     "fillColor=#FFFFFF;strokeColor=#000000;swimlaneFillColor=#FFFFFF;collapsible=0;container=0;whiteSpace=wrap;" + FONT,
     240, 20, 760, 340)
s2.v("init", "", ST["start"], 280, 189, 22, 22)
s2.v("mut", "Mutakhir", STATE, 370, 175, 150, 50)
s2.v("ptn", "Perlu Ditinjau", STATE, 770, 175, 160, 50)
s2.v("gnt", "Diganti", STATE, 1080, 80, 140, 50)
s2.v("cbt", "Dicabut", STATE, 1080, 270, 140, 50)
s2.e("t0", "pre", "cmp", "sahkan (S1)", style=TR, exit=(1, 0.5), entry=(0, 0.5))
s2.e("t1", "init", "mut", "/ hitung tanggal tinjau", style=TR)
s2.e("t2", "mut", "ptn", "when(tanggal tinjau terlewati)", [(445, 110), (850, 110)], style=TR, exit=(0.5, 0), entry=(0.5, 0))
s2.e("t3", "ptn", "mut", "tinjau [hasil = tetap berlaku]<br>/ perbarui tanggal tinjau", style=TR, exit=(0, 0.5), entry=(1, 0.5))
s2.e("t4", "mut", "mut", "tinjau [hasil = tetap berlaku]<br>/ perbarui tanggal tinjau", [(407, 300), (330, 300), (330, 215)],
     style=TR, exit=(0.25, 1), entry=(0, 0.8))
s2.e("t5", "cmp", "gnt", "versi baru disahkan", style=TR, exit=(1, 0.2), entry=(0, 0.5))
s2.e("t6", "cmp", "cbt", "cabut", style=TR, exit=(1, 0.75), entry=(0, 0.5))
s2.w, s2.h = 1250, 390
pages.append(s2)
notes.append(("S2 · Kemutakhiran versi SOP/IK yang sedang berlaku (rincian status Disahkan di S1)", [
    ("<b>Kaitan ke PKG-02 S3 (mutakhir)</b>: versi berlaku memenuhi S3 selama berada di <i>Mutakhir</i>, "
     "yaitu tanggal tinjau berikutnya belum terlewati. <b>[ASUMSI]</b> Tinjauan dengan hasil <i>perlu revisi</i> tidak "
     "mengubah sub-status dan tidak memperbarui tanggal tinjau; tinjauan itu memicu penyusunan versi baru (A2).", 90),
    ("<b>Implementasi</b> (Wazlawick §9.3, <i>modal class</i>, transisi stabil): sub-status <b>tidak</b> disimpan sebagai "
     "field <code>state</code>. <i>Perlu Ditinjau</i> dihitung dari tanggal tinjau berikutnya &lt; hari ini (KF-15). "
     "Tanpa pengingat terjadwal.", 80),
]))

# ------------------------------------------------------------------ halaman catatan (bahan kerja, tidak masuk naskah)
cat = Page("tk-act-notes", "Catatan TO-BE (bahan kerja) - Activity dan State Machine", "tk-act-notes-")
cat.v("title", "Catatan diagram activity dan state machine (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 16, 1200, 36)
cat.v("legend", LEGEND, NOTE, 40, 60, 1220, 60)
cat.v("src", SRC, NOTE, 40, 132, 1220, 30)
col_w, x0, y0 = 400, 40, 180
for i, (head, items) in enumerate(notes):
    x = x0 + (i % 3) * (col_w + 20)
    y = y0 + (i // 3) * 470
    cat.v(f"h{i}", f"<b>{head}</b>", "text;html=1;fontSize=12;align=left;verticalAlign=top;whiteSpace=wrap;", x, y, col_w, 40)
    yy = y + 46
    for j, (txt, h) in enumerate(items):
        cat.v(f"n{i}-{j}", txt, NOTE, x, yy, col_w, h)
        yy += h + 10
cat.w, cat.h = 1300, y0 + 2 * 470 + 40
pages.append(cat)

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(p.xml() for p in pages) + "</mxfile>")
