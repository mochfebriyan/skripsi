"""Use case diagram modul SDM & Kompetensi (Langkah 6), 4 halaman.

Fungsi gambar disalin dari contoh-tata-kelola/use_case.py versi branch febriyan-skripsi (versi sweet spot,
14 Nov 2026); yang diganti hanya data, prefiks ID (sdm-), kode UC-SDM-nn, dan warna modul SDM (#EEFAF3 / #4E9A6B).
Tambahan: package rujukan (abu-abu putus-putus) untuk use case pengesahan milik modul Tata Kelola yang dipakai ulang.

Jalankan:
    python -I projek-fiklab/tools/drawio/sdm/use_case.py projek-fiklab/rancangan/use-case-sdm.drawio
    python -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/use-case-sdm.drawio sdm-
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]


def esc(s):
    return escape(s, {'"': "&quot;"})


# Warna modul SDM & Kompetensi (CLAUDE.md bagian 2)
PF, PS = "#EEFAF3", "#4E9A6B"
STEREO_COLOR = "#2F6B45"
BOUND = f"rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fontStyle=1;fontSize=15;spacingTop=8;fillColor=#FFFFFF;strokeColor={PS};strokeWidth=2;"
PKG = ("shape=folder;tabWidth=300;tabHeight=22;tabPosition=left;html=1;whiteSpace=wrap;verticalAlign=top;align=left;"
       f"spacingLeft=8;spacingTop=2;fontSize=12;fontStyle=1;fillColor={PF};strokeColor={PS};")
PKG_REF = ("shape=folder;tabWidth=300;tabHeight=22;tabPosition=left;html=1;whiteSpace=wrap;verticalAlign=top;align=left;"
           "spacingLeft=8;spacingTop=2;fontSize=12;fontStyle=1;fillColor=#F2F2F2;strokeColor=#999999;dashed=1;fontColor=#555555;")
ELL = "ellipse;whiteSpace=wrap;html=1;fontSize=11;fillColor=#FFFFFF;strokeColor=#333333;"
ELL_REF = "ellipse;whiteSpace=wrap;html=1;fontSize=11;fillColor=#F2F2F2;strokeColor=#999999;dashed=1;fontColor=#555555;"
ACT = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fontStyle=1;"
ACT_ABS = f"shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fontStyle=3;fillColor={PF};"
ACT_SYS = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fontStyle=1;fillColor=#EEEEEE;"
ASSOC = "endArrow=none;html=1;strokeColor=#555555;"
GEN = "endArrow=block;endFill=0;endSize=14;html=1;strokeColor=#333333;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=18;fontStyle=1;align=left;verticalAlign=middle;"

# nomor: (nama, stereotype, lapis); lapis W = Inti, O = Pelengkap. Lapis tidak dibedakan di diagram, hanya di dokumen
UC = {
    1: ("Kelola Kompetensi", "CRUDL", "W"),
    2: ("Kelola Syarat Kompetensi Jabatan", "CRUDL", "W"),
    3: ("Kelola Bukti Kompetensi", "CRUDL", "W"),
    4: ("Lihat Matriks Kompetensi", "report", "W"),
    5: ("Tetapkan Kebutuhan Petugas", "", "W"),
    6: ("Catat Hasil Seleksi Asisten", "", "W"),
    7: ("Susun Surat Tugas", "", "W"),
    8: ("Buat Revisi Surat Tugas", "", "O"),
    9: ("Catat Orientasi Petugas Baru", "", "O"),
    10: ("Lihat Daftar Petugas per Sesi", "report", "W"),
    11: ("Kelola Tugas/Alat Berkewenangan Khusus", "CRUDL", "W"),
    12: ("Catat Asesmen Keterampilan", "", "W"),
    13: ("Susun Otorisasi", "", "W"),
    14: ("Catat Pemicu Evaluasi Ulang", "", "W"),
    15: ("Putuskan Evaluasi Ulang Otorisasi", "", "W"),
    16: ("Lihat Daftar Operator Sah", "report", "W"),
    17: ("Susun Rencana Pelatihan", "", "W"),
    18: ("Catat Realisasi Pelatihan", "", "W"),
    19: ("Catat Evaluasi Efektivitas Pelatihan", "", "W"),
    20: ("Batalkan Item Pelatihan", "", "O"),
    21: ("Lihat Rekap Pelatihan Personel", "report", "O"),
    22: ("Lihat Status Monev SDM", "report", "W"),
}
# Use case milik modul Tata Kelola (branch febriyan-skripsi, use-case-tata-kelola.md) yang dipakai ulang
TK = {
    1: "Ajukan Dokumen", 2: "Terbitkan Dokumen Resmi", 3: "Unggah Dokumen Bertanda Tangan",
    4: "Kembalikan Dokumen", 5: "Sahkan Dokumen", 6: "Cabut Dokumen",
}

UC_X, UC_W, UC_H, STEP = 420, 290, 58, 70


class Page:
    def __init__(s, n, name):
        s.P, s.name, s.n, s.cells = f"sdm-uc{n}-", name, n, []

    def v(s, id, val, style, x, y, w, h):
        s.cells.append(f'<mxCell id="{s.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

    def e(s, id, a, b, style):
        s.cells.append(f'<mxCell id="{s.P}{id}" value="" style="{style}" edge="1" parent="1" source="{s.P}{a}" target="{s.P}{b}"><mxGeometry relative="1" as="geometry"/></mxCell>')

    def pkg(s, id, name, x, y, w, ucs):
        h = 40 + STEP * len(ucs)
        s.v(id, name, PKG, x, y, w, h)
        for i, n in enumerate(ucs):
            label, st, _lapis = UC[n]
            top = f"<font style='font-size:9px' color='{STEREO_COLOR}'>«{st}»</font><br>" if st else ""
            s.v(f"uc{n:02d}", f"{top}<b>UC-SDM-{n:02d}</b><br>{label}", ELL, UC_X, y + 34 + STEP * i, UC_W, UC_H)
        return y + h

    def pkg_ref(s, id, name, x, y, w, nums):
        h = 40 + STEP * len(nums)
        s.v(id, name, PKG_REF, x, y, w, h)
        for i, n in enumerate(nums):
            s.v(f"tk{n:02d}", f"<b>UC-{n:02d}</b> (Tata Kelola)<br>{TK[n]}", ELL_REF, UC_X, y + 34 + STEP * i, UC_W, UC_H)
        return y + h

    def actor(s, id, label, x, y, kind="h"):
        s.v(id, label, {"h": ACT, "a": ACT_ABS, "s": ACT_SYS}[kind], x, y, 30, 60)

    def links(s, d):
        for a, ns in d.items():
            for n in ns:
                key = n if isinstance(n, str) else f"uc{n:02d}"
                s.e(f"a-{a}-{key}", a, key, ASSOC)

    def xml(s, w, h):
        return (f'<diagram id="sdm-uc{s.n}" name="{esc(s.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" '
                f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" math="0" shadow="0"><root>'
                '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(s.cells) + "</root></mxGraphModel></diagram>")


LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §4.2–4.3)<br>"
          "• Aktor miring hijau = <b>aktor abstrak</b>; panah segitiga kosong = generalisasi (turunan mewarisi use case induk)<br>"
          "• «CRUDL» = kelola data (buat, lihat, ubah, hapus, daftar) dengan satu pola; «report» = hanya membaca<br>"
          "• Package dan elips <b>abu-abu putus-putus</b> = use case milik modul Tata Kelola yang dipakai ulang, tidak dirancang ulang<br>"
          "• Tanpa «include»/«extend»: setiap use case satu sesi dan berdiri sendiri (§4.3.1, §4.5)")
SRC = ("Sumber: activity A1–A3 dan state machine S1–S3 (proses-bisnis-sdm.md), kebutuhan KF-SDM-01–43 (kebutuhan-sdm.md), "
       "use case pengesahan UC-01–06 Tata Kelola (branch febriyan-skripsi). Rincian: use-case-sdm.md · Draf 15 Nov 2026 · Zahir")
SYS = "Sistem LabFIK Compliance · Modul SDM & Kompetensi"
BX, BW = 330, 500          # batas sistem
PX, PW = 360, 440          # package
NX, NW = 870, 460          # kolom catatan
pages = []

# ---------- halaman 1: kompetensi + pengesahan (rujukan) + hierarki aktor
p = Page(1, "UC TO-BE (1-4) - Kompetensi dan Pengesahan Dokumen SDM")
p.v("title", "Use case TO-BE 1/4 · Kompetensi (dipakai PKG-04, 10, 14), pengesahan dokumen SDM, dan hierarki aktor", TITLE, 40, 10, 1290, 36)
y = p.pkg("p1", "Kompetensi (PKG-04, PKG-10, PKG-14)", PX, 100, PW, [3, 1, 2, 4])
y = p.pkg_ref("p2", "Pengesahan Dokumen SDM · memakai UC Tata Kelola", PX, y + 20, PW, [1, 2, 3, 4, 5, 6])
p.v("sys", SYS, BOUND, BX, 60, BW, y + 20 - 60)
p.cells.insert(1, p.cells.pop())   # batas sistem digambar di bawah package
p.actor("pnl", "Pengelola Lab", 200, 330, "a")
p.actor("lab", "Laboran/PLP", 60, 470)
p.actor("kal", "KaLab", 200, 610)
p.links({"pnl": [3, "tk01", "tk02", "tk03"], "kal": [1, 2, 4, "tk04", "tk05", "tk06"]})
p.e("g-lab-pnl", "lab", "pnl", GEN)
p.e("g-kal-pnl", "kal", "pnl", GEN)
p.v("n0", LEGEND, NOTE, NX, 60, NW, 150)
p.v("n1", "<b>Cara baca</b><br>• <i>Pengelola Lab</i> = peran pencatat: KaLab atau Laboran/PLP. Semua use case <i>Pengelola Lab</i> "
    "juga bisa dilakukan KaLab dan Laboran.<br>"
    "• Kelola master Kompetensi dan syarat jabatan hanya oleh <b>KaLab</b>; bukti kompetensi dicatat keduanya.<br>"
    "• Surat Tugas (UC-SDM-07, 08), Otorisasi (UC-SDM-13), dan Rencana Pelatihan (UC-SDM-17) diajukan, disahkan, "
    "dan dicabut lewat use case Tata Kelola di package bawah. Kelengkapan tiap jenis dokumen SDM diperiksa saat <b>UC-01 Ajukan</b>; "
    "otorisasi lama diganti saat <b>UC-05 Sahkan</b>.<br>"
    "• UC-02 menerbitkan Surat Tugas dan Rencana Pelatihan sebagai PDF untuk ditandatangani (Pelengkap).", NOTE, NX, 230, NW, 230)
p.v("n2", "<b>Bukan aktor</b>: Dekan, Wadek, Koor Prodi (hanya menandatangani; dicatat sebagai pengesah atau penyetuju pengecualian), "
    "asisten praktikum, dan penilai monev (menerima PDF). Tidak ada aktor Penjadwal: status berlaku dihitung dari tanggal "
    "(kontrak Core K-3). Kedaluwarsa Rencana Pelatihan berperiode memakai UC-07 Tata Kelola (Pelengkap modul itu).", NOTE, NX, 480, NW, 130)
p.v("n3", "<b>[KONFIRMASI]</b> Nomor UC-01–06 dirujuk dari use-case-tata-kelola.md (Febriyan, 14 Nov 2026). "
    "Bila Tata Kelola menomori ulang, rujukan di halaman ini ikut diubah.", NOTE, NX, 630, NW, 70)
p.v("n4", SRC, NOTE, NX, 720, NW, 90)
pages.append((p, 1380, y + 70))

# ---------- halaman 2: penugasan PKG-04
p = Page(2, "UC TO-BE (2-4) - Penugasan Petugas (PKG-04)")
p.v("title", "Use case TO-BE 2/4 · Penugasan Petugas sesuai Kompetensi (PKG-04)", TITLE, 40, 10, 1290, 36)
y = p.pkg("p1", "Penugasan Petugas (PKG-04)", PX, 100, PW, [6, 7, 9, 5, 8, 10])
p.v("sys", SYS, BOUND, BX, 60, BW, y + 20 - 60)
p.cells.insert(1, p.cells.pop())
p.actor("pnl", "Pengelola Lab", 200, 200, "a")
p.actor("kal", "KaLab", 200, 410)
p.links({"pnl": [6, 7, 9], "kal": [5, 8, 10]})
p.v("n0", LEGEND, NOTE, NX, 60, NW, 150)
p.v("n1", "<b>Cara baca</b><br>• Hierarki aktor di halaman 1/4: KaLab juga <i>Pengelola Lab</i>.<br>"
    "• UC-SDM-06 mencakup pengecualian syarat (alasan + penyetuju di luar sistem) dan pembuatan Personel asisten "
    "bila belum ada. Calon yang tidak lulus tidak dicatat.<br>"
    "• UC-SDM-07 dan 08 menghasilkan Surat Tugas bergaris (asisten → kelas, laboran → ruang); "
    "pengajuan dan pengesahannya lewat halaman 1/4.<br>"
    "• UC-SDM-10 menampilkan status S1–S4 setiap sesi terlaksana dan syarat yang gagal.", NOTE, NX, 230, NW, 190)
p.v("n2", "<b>[KONFIRMASI]</b> KB-3: Surat Tugas <b>ditolak</b> saat diajukan bila ada asisten tanpa seleksi lulus "
    "(dipakai sebagai default). K7: pengesah Surat Tugas.", NOTE, NX, 440, NW, 60)
p.v("n3", SRC, NOTE, NX, 520, NW, 90)
pages.append((p, 1380, max(y, 610) + 60))

# ---------- halaman 3: otorisasi PKG-10
p = Page(3, "UC TO-BE (3-4) - Otorisasi Personel (PKG-10)")
p.v("title", "Use case TO-BE 3/4 · Otorisasi Personel untuk Tugas/Alat Berkewenangan Khusus (PKG-10)", TITLE, 40, 10, 1290, 36)
y = p.pkg("p1", "Otorisasi Personel (PKG-10)", PX, 100, PW, [12, 14, 15, 11, 13, 16])
p.v("sys", SYS, BOUND, BX, 60, BW, y + 20 - 60)
p.cells.insert(1, p.cells.pop())
p.actor("pnl", "Pengelola Lab", 200, 200, "a")
p.actor("kal", "KaLab", 200, 410)
p.links({"pnl": [12, 14, 15], "kal": [11, 13, 16]})
p.v("n0", LEGEND, NOTE, NX, 60, NW, 150)
p.v("n1", "<b>Cara baca</b><br>• UC-SDM-11 mencakup penetapan <b>pelaksana</b> tiap tugas/alat (penyebut PKG-10) "
    "dan cara pembatasan akses (Pelengkap).<br>"
    "• UC-SDM-12: asesmen <i>layak</i> langsung membuat Bukti Kompetensi.<br>"
    "• Evaluasi ulang dipecah dua karena ada jeda: pemicu dicatat saat terjadi (status <i>Terbuka</i>), "
    "keputusan diambil setelah personel dinilai ulang (S2).<br>"
    "• Keputusan diperpanjang/dibatasi/naik level diwujudkan dengan Otorisasi baru (UC-SDM-13); "
    "dicabut lewat UC-06 Cabut Dokumen (halaman 1/4).", NOTE, NX, 230, NW, 200)
p.v("n2", "<b>[KONFIRMASI]</b> KP-1: keputusan <i>tetap berlaku</i> di UC-SDM-15 (dipakai sebagai default). "
    "KB-1: penyebut = pelaksana yang ditetapkan KaLab.", NOTE, NX, 450, NW, 60)
p.v("n3", SRC, NOTE, NX, 530, NW, 90)
pages.append((p, 1380, max(y, 620) + 60))

# ---------- halaman 4: pelatihan PKG-14 + status monev
p = Page(4, "UC TO-BE (4-4) - Pelatihan PLP (PKG-14) dan Status Monev")
p.v("title", "Use case TO-BE 4/4 · Pelatihan PLP/Laboran (PKG-14) dan Status Monev SDM", TITLE, 40, 10, 1290, 36)
y = p.pkg("p1", "Pelatihan PLP/Laboran (PKG-14)", PX, 100, PW, [18, 19, 17, 20, 21])
y = p.pkg("p2", "Status Monev (PKG-04, PKG-10, PKG-14)", PX, y + 20, PW, [22])
p.v("sys", SYS, BOUND, BX, 60, BW, y + 20 - 60)
p.cells.insert(1, p.cells.pop())
p.actor("pnl", "Pengelola Lab", 200, 160, "a")
p.actor("kal", "KaLab", 200, 420)
p.links({"pnl": [18, 19], "kal": [17, 20, 21, 22]})
p.v("n0", LEGEND, NOTE, NX, 60, NW, 150)
p.v("n1", "<b>Cara baca</b><br>• UC-SDM-17 mencakup kebutuhan kompetensi (diisi awal dari matriks) dan item pelatihan "
    "dalam satu draf rencana; pengesahannya lewat halaman 1/4.<br>"
    "• UC-SDM-19: evaluasi <i>efektif</i> langsung membuat Bukti Kompetensi, sehingga kebutuhan tahun berikutnya berkurang (K4).<br>"
    "• UC-SDM-22: persentase PKG-04 dan PKG-10, kriteria tertinggi K1–K4 PKG-14 yang lengkap secara data, "
    "daftar unit yang belum memenuhi, dan tautan bukti. Hasilnya diserahkan ke penilai sebagai PDF; "
    "skor akhir PKG-14 ditetapkan penilai.", NOTE, NX, 230, NW, 200)
p.v("n2", "<b>[KONFIRMASI]</b> KU-2: revisi Rencana Pelatihan setelah disahkan tidak dirancang; pelatihan pengganti "
    "masuk rencana tahun berikutnya.", NOTE, NX, 450, NW, 60)
p.v("n3", SRC, NOTE, NX, 530, NW, 90)
pages.append((p, 1380, max(y, 620) + 60))

with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
