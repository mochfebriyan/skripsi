"""Use case diagram modul SDM & Kompetensi (Langkah 6), 4 halaman diagram + 1 halaman catatan.

Fungsi gambar dan gaya disalin dari contoh-tata-kelola/use_case.py versi `main` (gaya polos hitam-putih,
16 Nov 2026); yang diganti hanya data, prefiks ID (sdm-), dan kode UC-SDM-nn.
Seluruh isi hanya scope modul SDM: pengesahan dokumen SDM punya use case sendiri (UC-SDM-23–28).

Jalankan:
    python -I projek-fiklab/tools/drawio/sdm/use_case.py projek-fiklab/rancangan/use-case-sdm.drawio
    python -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/use-case-sdm.drawio sdm-
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]


def esc(s):
    return escape(s, {'"': "&quot;"})


FONT = "fontFamily=Times New Roman;"
BOUND = "rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fontStyle=1;fontSize=14;spacingTop=8;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
PKG = ("shape=folder;tabWidth=300;tabHeight=22;tabPosition=left;html=1;whiteSpace=wrap;verticalAlign=top;align=left;"
       "spacingLeft=8;spacingTop=2;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#000000;" + FONT)
ELL = "ellipse;whiteSpace=wrap;html=1;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
ACT = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT
ACT_ABS = ACT + "fontStyle=2;"   # aktor abstrak: nama miring (notasi UML)
ASSOC = "endArrow=none;html=1;strokeColor=#000000;"
GEN = "endArrow=block;endFill=0;endSize=14;html=1;strokeColor=#000000;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=16;fontStyle=1;align=left;verticalAlign=middle;"

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
    23: ("Ajukan Dokumen SDM", "", "W"),
    24: ("Terbitkan Dokumen SDM", "", "O"),
    25: ("Unggah Dokumen SDM Bertanda Tangan", "", "W"),
    26: ("Kembalikan Dokumen SDM", "", "W"),
    27: ("Sahkan Dokumen SDM", "", "W"),
    28: ("Cabut Dokumen SDM", "", "W"),
}
UC_X, UC_W, UC_H, STEP = 400, 290, 58, 70


class Page:
    def __init__(s, n, name):
        s.P, s.name, s.n, s.cells = f"sdm-uc{n}-", name, n, []
        s.maxx = s.maxy = 0

    def v(s, id, val, style, x, y, w, h):
        s.maxx, s.maxy = max(s.maxx, x + w), max(s.maxy, y + h + (40 if "umlActor" in style else 0))
        s.cells.append(f'<mxCell id="{s.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

    def e(s, id, a, b, style):
        s.cells.append(f'<mxCell id="{s.P}{id}" value="" style="{style}" edge="1" parent="1" source="{s.P}{a}" target="{s.P}{b}"><mxGeometry relative="1" as="geometry"/></mxCell>')

    def pkg(s, id, name, x, y, w, ucs):
        h = 40 + STEP * len(ucs)
        s.v(id, name, PKG, x, y, w, h)
        for i, n in enumerate(ucs):
            label, st, _lapis = UC[n]
            top = f"<font style='font-size:10px'>«{st}»</font><br>" if st else ""
            s.v(f"uc{n:02d}", f"{top}<b>UC-SDM-{n:02d}</b><br>{label}", ELL, UC_X, y + 34 + STEP * i, UC_W, UC_H)
        return y + h

    def actor(s, id, label, x, y, abstract=False):
        s.v(id, label, ACT_ABS if abstract else ACT, x, y, 30, 60)

    def links(s, d):
        for a, ns in d.items():
            for n in ns:
                s.e(f"a-{a}-{n:02d}", a, f"uc{n:02d}", ASSOC)

    def boundary(s, y_end):
        """Batas sistem digambar di bawah package (sel kedua setelah tidak ada judul)."""
        s.cells.insert(0, f'<mxCell id="{s.P}sys" value="{esc(SYS)}" style="{BOUND}" vertex="1" parent="1">'
                          f'<mxGeometry x="{BX}" y="20" width="{BW}" height="{y_end + 20 - 20}" as="geometry"/></mxCell>')
        s.maxy = max(s.maxy, y_end + 20)

    def xml(s, w=None, h=None):
        w, h = w or s.maxx + 40, h or s.maxy + 30
        return (f'<diagram id="sdm-uc{s.n}" name="{esc(s.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" '
                f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" math="0" shadow="0"><root>'
                '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(s.cells) + "</root></mxGraphModel></diagram>")


LEGEND = ("<b>Notasi</b> (Wazlawick 2024, §4.2–4.3)<br>"
          "• Nama aktor miring = <b>aktor abstrak</b>; panah segitiga kosong = generalisasi (turunan mewarisi use case induk)<br>"
          "• «CRUDL» = kelola data (buat, lihat, ubah, hapus, daftar) dengan satu pola; «report» = hanya membaca<br>"
          "• Tanpa «include»/«extend»: setiap use case satu sesi dan berdiri sendiri (§4.3.1, §4.5)<br>"
          "• Gaya polos hitam-putih (CLAUDE.md bagian 5); semua use case milik modul SDM")
SRC = ("Sumber: activity A1–A4 dan state machine S1–S4 (proses-bisnis-sdm.md), kebutuhan KF-SDM-01–43 (kebutuhan-sdm.md). "
       "Rincian: use-case-sdm.md · Draf 15 Nov 2026, direvisi 17 Nov 2026 (pengesahan dokumen SDM sebagai use case sendiri, gaya hitam-putih) · Zahir")
SYS = "Sistem LabFIK Compliance · Modul SDM & Kompetensi"
BX, BW, PX, PW = 310, 500, 340, 440
pages, notes = [], []

# ---------- halaman 1: kompetensi + pengesahan dokumen SDM + hierarki aktor
_n = []
p = Page(1, "UC TO-BE (1-4) - Kompetensi dan Pengesahan Dokumen SDM")
judul = "Use case TO-BE 1/4 · Kompetensi (dipakai PKG-04, 10, 14), pengesahan dokumen SDM, dan hierarki aktor"
y = p.pkg("p1", "Kompetensi (PKG-04, PKG-10, PKG-14)", PX, 60, PW, [3, 1, 2, 4])
y = p.pkg("p2", "Pengesahan Dokumen SDM", PX, y + 20, PW, [23, 24, 25, 26, 27, 28])
p.boundary(y)
p.actor("pnl", "Pengelola Lab", 180, 300, abstract=True)
p.actor("lab", "Laboran/PLP", 40, 440)
p.actor("kal", "KaLab", 180, 580)
p.links({"pnl": [3, 23, 24, 25], "kal": [1, 2, 4, 26, 27, 28]})
p.e("g-lab-pnl", "lab", "pnl", GEN)
p.e("g-kal-pnl", "kal", "pnl", GEN)
_n.append("<b>Cara baca</b><br>• <i>Pengelola Lab</i> = peran pencatat: KaLab atau Laboran/PLP. Semua use case <i>Pengelola Lab</i> "
          "juga bisa dilakukan KaLab dan Laboran.<br>"
          "• Kelola master Kompetensi dan syarat jabatan hanya oleh <b>KaLab</b>; bukti kompetensi dicatat keduanya.<br>"
          "• <b>Dokumen SDM</b> = Surat Tugas (UC-SDM-07, 08), Otorisasi (UC-SDM-13), Rencana Pelatihan (UC-SDM-17). Ketiganya "
          "diajukan, disahkan, dan dicabut lewat package Pengesahan Dokumen SDM. Kelengkapan tiap jenis diperiksa di UC-SDM-23; "
          "dokumen lama diganti di UC-SDM-27.<br>"
          "• UC-SDM-24 menerbitkan Surat Tugas dan Rencana Pelatihan sebagai PDF untuk ditandatangani (Pelengkap).")
_n.append("<b>Bukan aktor</b>: Dekan, Wadek, Koor Prodi (hanya menandatangani; dicatat sebagai pengesah atau penyetuju "
          "pengecualian), asisten praktikum, dan penilai monev (menerima PDF). Tidak ada aktor Penjadwal: status berlaku dihitung "
          "dari tanggal (kontrak Core K-3).")
notes.append((judul, _n)); pages.append(p)

# ---------- halaman 2: penugasan PKG-04
_n = []
p = Page(2, "UC TO-BE (2-4) - Penugasan Petugas (PKG-04)")
judul = "Use case TO-BE 2/4 · Penugasan Petugas sesuai Kompetensi (PKG-04)"
y = p.pkg("p1", "Penugasan Petugas (PKG-04)", PX, 60, PW, [6, 7, 9, 5, 8, 10])
p.boundary(y)
p.actor("pnl", "Pengelola Lab", 180, 160, abstract=True)
p.actor("kal", "KaLab", 180, 370)
p.links({"pnl": [6, 7, 9], "kal": [5, 8, 10]})
_n.append("<b>Cara baca</b><br>• Hierarki aktor di halaman 1/4: KaLab juga <i>Pengelola Lab</i>.<br>"
          "• UC-SDM-06 mencakup pengecualian syarat (alasan + penyetuju di luar sistem) dan pembuatan Personel asisten bila "
          "belum ada. Calon yang tidak lulus tidak dicatat.<br>"
          "• UC-SDM-07 dan 08 menghasilkan Surat Tugas bergaris (asisten → kelas, laboran → ruang); pengajuan dan pengesahannya "
          "lewat halaman 1/4.<br>"
          "• UC-SDM-10 menampilkan status S1–S4 setiap sesi terlaksana dan syarat yang gagal.")
_n.append("<b>[KONFIRMASI]</b> KB-3: Surat Tugas <b>ditolak</b> saat diajukan bila ada asisten tanpa seleksi lulus "
          "(dipakai sebagai default). K7: pengesah Surat Tugas.")
notes.append((judul, _n)); pages.append(p)

# ---------- halaman 3: otorisasi PKG-10
_n = []
p = Page(3, "UC TO-BE (3-4) - Otorisasi Personel (PKG-10)")
judul = "Use case TO-BE 3/4 · Otorisasi Personel untuk Tugas/Alat Berkewenangan Khusus (PKG-10)"
y = p.pkg("p1", "Otorisasi Personel (PKG-10)", PX, 60, PW, [12, 14, 15, 11, 13, 16])
p.boundary(y)
p.actor("pnl", "Pengelola Lab", 180, 160, abstract=True)
p.actor("kal", "KaLab", 180, 370)
p.links({"pnl": [12, 14, 15], "kal": [11, 13, 16]})
_n.append("<b>Cara baca</b><br>• UC-SDM-11 mencakup penetapan <b>pelaksana</b> tiap tugas/alat (penyebut PKG-10) dan cara "
          "pembatasan akses (Pelengkap).<br>"
          "• UC-SDM-12: asesmen <i>layak</i> langsung membuat Bukti Kompetensi.<br>"
          "• Evaluasi ulang dipecah dua karena ada jeda: pemicu dicatat saat terjadi (status <i>Terbuka</i>), keputusan diambil "
          "setelah personel dinilai ulang (S2).<br>"
          "• Keputusan diperpanjang/dibatasi/naik level diwujudkan dengan Otorisasi baru (UC-SDM-13); dicabut lewat "
          "UC-SDM-28 Cabut Dokumen SDM (halaman 1/4).")
_n.append("<b>[KONFIRMASI]</b> KP-1: keputusan <i>tetap berlaku</i> di UC-SDM-15 (default). KU-1: pemicu dan keputusan di hari "
          "berbeda. KB-1: penyebut = pelaksana yang ditetapkan KaLab.")
notes.append((judul, _n)); pages.append(p)

# ---------- halaman 4: pelatihan PKG-14 + status monev
_n = []
p = Page(4, "UC TO-BE (4-4) - Pelatihan PLP (PKG-14) dan Status Monev")
judul = "Use case TO-BE 4/4 · Pelatihan PLP/Laboran (PKG-14) dan Status Monev SDM"
y = p.pkg("p1", "Pelatihan PLP/Laboran (PKG-14)", PX, 60, PW, [18, 19, 17, 20, 21])
y = p.pkg("p2", "Status Monev (PKG-04, PKG-10, PKG-14)", PX, y + 20, PW, [22])
p.boundary(y)
p.actor("pnl", "Pengelola Lab", 180, 120, abstract=True)
p.actor("kal", "KaLab", 180, 380)
p.links({"pnl": [18, 19], "kal": [17, 20, 21, 22]})
_n.append("<b>Cara baca</b><br>• UC-SDM-17 mencakup kebutuhan kompetensi (diisi awal dari matriks) dan item pelatihan dalam "
          "satu draf rencana; pengesahannya lewat halaman 1/4.<br>"
          "• UC-SDM-19: evaluasi <i>efektif</i> langsung membuat Bukti Kompetensi, sehingga kebutuhan tahun berikutnya berkurang (K4).<br>"
          "• UC-SDM-22: persentase PKG-04 dan PKG-10, kriteria tertinggi K1–K4 PKG-14 yang lengkap secara data, daftar unit yang "
          "belum memenuhi, dan tautan bukti. Hasilnya diserahkan ke penilai sebagai PDF; skor akhir PKG-14 ditetapkan penilai.")
_n.append("<b>[KONFIRMASI]</b> KU-2: revisi Rencana Pelatihan setelah disahkan tidak dirancang; pelatihan pengganti masuk "
          "rencana tahun berikutnya. KU-3: laporan bukti memuat rekaman pendukung (orientasi, pembatasan akses).")
notes.append((judul, _n)); pages.append(p)

# ---------- halaman catatan (bahan kerja, tidak disisipkan ke naskah)
c = Page("-notes", "Catatan UC TO-BE (bahan kerja)")
c.P = "sdm-uc-notes-"
c.v("title", "Catatan use case diagram modul SDM (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 10, 1100, 36)
c.v("legend", LEGEND, NOTE, 40, 56, 1100, 100)
c.v("src", SRC, NOTE, 40, 166, 1100, 50)
y = 236
for i, (judul, items) in enumerate(notes):
    c.v(f"h{i}", f"<b>{judul}</b>", "text;html=1;fontSize=12;align=left;verticalAlign=top;whiteSpace=wrap;", 40, y, 1100, 24)
    y += 30
    for j, txt in enumerate(items):
        h = 40 + 18 * (len(txt) // 170 + txt.count("<br>"))
        c.v(f"n{i}-{j}", txt, NOTE, 40, y, 1100, h)
        y += h + 10
    y += 10
pages.append(c)

with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(pg.xml() for pg in pages) + "</mxfile>")
