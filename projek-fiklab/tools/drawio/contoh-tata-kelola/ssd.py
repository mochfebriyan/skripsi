"""System sequence diagram modul Tata Kelola (langkah 8), satu halaman per SSD.

Gaya polos hitam-putih (sama dengan activity_state.py). Garis putus-putus hanya untuk return (notasi UML).
Halaman SSD hanya berisi diagram; judul, prakondisi, dan legenda dikumpulkan di halaman catatan terakhir.

Pemakaian: python3 -I ssd.py projek-fiklab/rancangan/ssd-tata-kelola.drawio
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]


def esc(s):
    return escape(s, {'"': "&quot;"})


FONT = "fontFamily=Times New Roman;"
LIFE = ("shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=0;collapsible=0;"
        "recursiveResize=0;outlineConnect=0;fontSize=12;fontStyle=1;fillColor=#FFFFFF;strokeColor=#000000;size={size};" + FONT)
PART = {"actor": "participant=umlActor;", "boundary": "participant=umlBoundary;", "control": "participant=umlControl;"}
EV = "html=1;endArrow=open;endSize=9;strokeColor=#000000;fontSize=11;verticalAlign=bottom;labelBackgroundColor=none;" + FONT
RET = "html=1;endArrow=open;endSize=9;dashed=1;strokeColor=#000000;fontSize=11;verticalAlign=bottom;labelBackgroundColor=none;" + FONT
CALL = "html=1;endArrow=block;endFill=1;endSize=9;strokeColor=#000000;fontSize=11;verticalAlign=bottom;labelBackgroundColor=none;" + FONT
FRAME = "shape=umlFrame;whiteSpace=wrap;html=1;pointerEvents=0;width=54;height=22;fontSize=11;fontStyle=1;fillColor=none;strokeColor=#000000;" + FONT
GUARD = "text;html=1;fontSize=11;align=left;verticalAlign=middle;fontStyle=2;" + FONT
TXT = "text;html=1;fontSize=11;align=left;verticalAlign=middle;fontStyle=2;" + FONT
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"

ROW = {"ev": 34, "ret": 34, "q": 34, "c": 34, "txt": 24, "ref": 48}
LEGEND = ("<b>Notasi</b> (Wazlawick 2024, Bab 7)<br>"
          "• Panah hitam penuh: <i>system event</i> (aktor → antarmuka)<br>"
          "• Panah hitam putus-putus: <i>system return</i> (antarmuka → aktor)<br>"
          "• Panah kepala segitiga penuh: operasi sistem ke kontroler. "
          "<b>Command</b> <code>op(args)</code> mengubah data tanpa nilai balik; "
          "<b>query</b> <code>dto = op(args)</code> hanya membaca (CQS, §7.1)<br>"
          "• <code>dto_x</code> = data majemuk (lihat kamus DTO), <code>*</code> = koleksi, <i>terpilih</i> = pilihan dari daftar (§7.3)<br>"
          "• Stateless: <code>user_id</code> dikirim ke setiap operasi yang membutuhkannya (§7.5)<br>"
          "• <code>opt «exception»</code> / <code>opt «variant»</code>: alur alternatif; <code>ref</code>: use case lain (§7.6)<br>"
          "Sumber: expanded-use-case-tata-kelola.md; kamus DTO di ssd-tata-kelola.md · Draf 14 Nov 2026 · Febriyan")


class SSD:
    def __init__(self, n, uc, title, actors, pre, main, blocks):
        self.P = f"tk-ssd{n}-"
        self.n, self.uc, self.title, self.actors, self.pre, self.main, self.blocks = n, uc, title, actors, pre, main, blocks
        self.cells = []

    def v(self, id, val, style, x, y, w, h):
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def build(self):
        LY, HEAD = 20, 60
        lanes = [("a0", ":" + self.actors[0], "actor", 40, 130),
                 ("ui", ":Antarmuka", "boundary", 360, 130),
                 ("ct", ":Kontroler", "control", 720, 130)]
        if len(self.actors) > 1:
            lanes.append(("a1", ":" + self.actors[1], "actor", 1080, 130))
        self.cx = {k: x + w / 2 for k, _, _, x, w in lanes}
        right = max(self.cx.values()) + 90
        entries = list(self.main)
        total = 60 + sum(ROW[e[0]] for e in entries)
        for _, _, ents in self.blocks:
            total += 50 + sum(ROW[e[0]] for e in ents) + 16
        lh = HEAD + total + 30
        self.LY, self.lh = LY, lh
        for k, label, part, x, w in lanes:
            self.v(k, label, LIFE.format(size=HEAD) + PART[part], x, LY, w, lh)
        y = LY + HEAD + 40
        self.k = 0
        for e in entries:
            y = self.entry(e, y)
        for i, (stereo, guard, ents) in enumerate(self.blocks):
            y += 16
            top = y
            y += 34
            for e in ents:
                y = self.entry(e, y)
            h = y - top + 6
            kind = "opt"
            self.v(f"fr{i}", kind, FRAME, 20, top, right - 20, h)
            self.v(f"gd{i}", f"{stereo} {guard}", GUARD, 82, top, right - 110, 22)
            y += 6
        self.width = right + 30
        self.height = LY + lh + 20

    def msg(self, src, dst, label, style, y):
        self.k += 1
        fy = (y - self.LY) / self.lh
        self.cells.append(
            f'<mxCell id="{self.P}m{self.k}" value="{esc(label)}" style="{style}exitX=0.5;exitY={fy:.4f};exitDx=0;exitDy=0;'
            f'entryX=0.5;entryY={fy:.4f};entryDx=0;entryDy=0;" edge="1" parent="1" source="{self.P}{src}" target="{self.P}{dst}">'
            f'<mxGeometry relative="1" as="geometry"/></mxCell>')

    def entry(self, e, y):
        kind, text = e[0], e[1]
        a = f"a{e[2]}" if len(e) > 2 else "a0"
        if kind == "ev":
            self.msg(a, "ui", text, EV, y)
        elif kind == "ret":
            self.msg("ui", a, text, RET, y)
        elif kind in ("q", "c"):
            self.msg("ui", "ct", text, CALL, y)
        elif kind == "txt":
            self.k += 1
            self.v(f"t{self.k}", text, TXT, self.cx["a0"] + 10, y - 12, 620, 22)
        elif kind == "ref":
            self.k += 1
            x0 = self.cx["a0"] - 30
            self.v(f"r{self.k}", "ref", FRAME.replace("width=54", "width=40"), x0, y - 18, self.cx["ct"] - x0 + 30, 38)
            self.v(f"rt{self.k}", text, "text;html=1;fontSize=11;align=center;verticalAlign=middle;" + FONT, x0 + 40,
                   y - 14, self.cx["ct"] - x0 - 20, 30)
        return y + ROW[kind]

    def xml(self):
        self.build()
        return (f'<diagram id="tk-ssd{self.n}" name="{esc(name_of(self))}">'
                f'<mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
                f'fold="1" page="1" pageScale="1" pageWidth="{self.width:.0f}" pageHeight="{self.height:.0f}" math="0" shadow="0">'
                '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")




N_SSD = 8
LOGIN = "pengguna sudah teridentifikasi dan <code>user_id</code> diketahui antarmuka. "
D = [
    SSD(1, "UC-01", "Ajukan Dokumen", ["Pengelola Lab"],
        LOGIN + "Ada dokumen Draf yang disusun aktor.",
        [("ev", "(minta draf saya)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = draf_saya, user_id)"), ("ret", "dto_dokumen_ringkas*"),
         ("ev", "dokumen terpilih, (ajukan)"), ("c", "ajukan_dokumen(dokumen, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status (Diajukan)")],
        [("«exception» E1", "[isi belum lengkap, AB-02] · langkah 3",
          [("q", "dto_kelengkapan* = cek_kelengkapan(dokumen)"), ("ret", "dto_kelengkapan*"), ("txt", "use case gagal; dokumen tetap Draf")]),
         ("«exception» E2", "[dokumen bukan Draf, AB-01] · langkah 3",
          [("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status"), ("txt", "use case gagal")]),
         ("«exception» E3", "[(O) ada versi lain dalam proses, AB-12] · langkah 3",
          [("ret", "versi_dalam_proses"), ("txt", "use case gagal")])]),
    SSD(2, "UC-03", "Unggah Dokumen Bertanda Tangan", ["Pengelola Lab"],
        LOGIN + "Ada dokumen Diajukan. Rencana dan SK sudah diterbitkan (UC-02) lalu ditandatangani di luar sistem.",
        [("ev", "(minta dokumen diajukan)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = diajukan, user_id)"), ("ret", "dto_dokumen_ringkas*"),
         ("ev", "dokumen terpilih, berkas_ttd"), ("c", "unggah_berkas_ttd(dokumen, berkas_ttd, user_id)"),
         ("q", "dto_rincian_dokumen = rincian_dokumen(dokumen, user_id)"), ("ret", "dto_rincian_dokumen (berkas terlampir)")],
        [("«variant» V1", "[berkas sudah pernah diunggah] · langkah 3",
          [("txt", "unggah_berkas_ttd() mengganti berkas; berkas lama tetap ada di riwayat (AB-09)")]),
         ("«exception» E1", "[dokumen bukan Diajukan, AB-03] · langkah 3",
          [("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status"), ("txt", "use case gagal")])]),
    SSD(3, "UC-05", "Sahkan Dokumen", ["KaLab"],
        LOGIN + "Aktor adalah KaLab (AB-06). Ada dokumen Diajukan.",
        [("ev", "(minta dokumen diajukan)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = diajukan, user_id)"), ("ret", "dto_dokumen_ringkas*"),
         ("ev", "dokumen terpilih"), ("q", "dto_rincian_dokumen = rincian_dokumen(dokumen, user_id)"),
         ("q", "dto_personel_ringkas* = daftar_pengesah_berwenang(dokumen)"), ("ret", "dto_rincian_dokumen, dto_personel_ringkas*"),
         ("ev", "‹pengesah terpilih, tanggal_sah›"), ("c", "sahkan_dokumen(dokumen, pengesah, tanggal_sah, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status (Disahkan, dokumen_diganti, tanggal_tinjau_berikutnya)")],
        [("«exception» E1", "[berkas bertanda tangan belum ada, AB-04] · langkah 5",
          [("ret", "MSG berkas belum diunggah"), ("ref", "UC-03 Unggah Dokumen Bertanda Tangan (SSD-2)")]),
         ("«exception» E2", "[pengesah tidak berwenang, AB-05] · langkah 5",
          [("ret", "dto_personel_ringkas*, MSG pengesah tidak berwenang"), ("txt", "kembali ke langkah 5")]),
         ("«exception» E3", "[(O) sudah ada rencana berlaku untuk jenis dan periode yang sama, AB-11] · langkah 5",
          [("ret", "rencana_berlaku"), ("txt", "use case gagal")])]),
    SSD(4, "UC-15", "Unggah Versi Dokumen", ["Laboran/PLP"],
        LOGIN + "Dokumen Induk terdaftar (UC-14).",
        [("ev", "(cari dokumen induk)"), ("q", "dto_dokumen_induk_ringkas* = daftar_dokumen_induk(filter, user_id)"), ("ret", "dto_dokumen_induk_ringkas*"),
         ("ev", "dokumen_induk terpilih"), ("q", "dto_info_versi = info_versi(dokumen_induk)"), ("ret", "dto_info_versi"),
         ("ev", "dto_versi_baru"), ("c", "buat_versi(dokumen_induk, dto_versi_baru, user_id)"),
         ("q", "dto_versi = rincian_versi(dokumen_induk, dto_versi_baru.revisi)"), ("ret", "dto_versi (Draf)")],
        [("«variant» V1", "[versi pertama] · langkah 5",
          [("txt", "dto_versi_baru hanya memuat berkas, revisi, tanggal_efektif")]),
         ("«exception» E1", "[nomor revisi sudah dipakai, AB-13] · langkah 5",
          [("ret", "dto_info_versi.riwayat_revisi*, MSG"), ("txt", "kembali ke langkah 5")]),
         ("«exception» E2", "[(O) ada versi dalam proses, AB-12] · langkah 5",
          [("ret", "dto_info_versi.versi_dalam_proses"), ("txt", "use case gagal")])]),
    SSD(5, "UC-18", "Tinjau Ulang Dokumen", ["Pengelola Lab"],
        LOGIN + "Ada versi Disahkan.",
        [("ev", "(minta versi berlaku)"), ("q", "dto_versi_berlaku* = daftar_versi_berlaku(filter, user_id)"), ("ret", "dto_versi_berlaku* (urut tanggal tinjau)"),
         ("ev", "versi terpilih, dto_tinjau (hasil = tetap_berlaku)"), ("c", "catat_tinjau_ulang(versi, dto_tinjau, user_id)"),
         ("q", "dto_status_tinjau = status_tinjau(versi)"), ("ret", "dto_status_tinjau (tanggal tinjau berikutnya baru)")],
        [("«variant» V1", "[hasil = perlu_revisi] · langkah 3",
          [("txt", "dto_status_tinjau: tanggal tinjau berikutnya tidak berubah"), ("ref", "UC-15 Unggah Versi Dokumen (SSD-4)")]),
         ("«exception» E1", "[versi bukan Disahkan, AB-15] · langkah 3",
          [("q", "dto_status = status_dokumen(versi)"), ("ret", "dto_status"), ("txt", "use case gagal")])]),
    SSD(6, "UC-23", "Susun Rencana", ["KaLab"],
        LOGIN + "KPI dan Personel terdaftar.",
        [("ev", "dto_rencana_baru (jenis = tahunan)"), ("c", "buat_rencana(dto_rencana_baru, user_id)"),
         ("q", "dto_rencana = rincian_rencana(rencana)"), ("q", "dto_kpi_ringkas* = daftar_kpi(filter = aktif)"),
         ("q", "dto_personel_ringkas* = daftar_personel(filter = aktif)"), ("ret", "dto_rencana (Draf), dto_kpi_ringkas*, dto_personel_ringkas*"),
         ("ev", "dto_item*"), ("c", "simpan_item_rencana(rencana, dto_item*, user_id)"),
         ("q", "dto_kelengkapan* = cek_kelengkapan(rencana)"), ("ret", "dto_rencana, dto_kelengkapan*")],
        [("«variant» V1", "[jenis = pengembangan] · setelah langkah 2",
          [("ev", "dto_gap*"), ("c", "simpan_temuan_gap(rencana, dto_gap*, user_id)"),
           ("q", "dto_rencana = rincian_rencana(rencana)"), ("ret", "dto_rencana (temuan per aspek)"),
           ("txt", "lanjut ke langkah 3; dto_item juga memuat gap*, nilai_risiko, nilai_manfaat, biaya; prioritas dihitung (O, AB-21)")]),
         ("«variant» V3", "[melanjutkan draf] · menggantikan langkah 1–2",
          [("ev", "(cari draf)"), ("q", "dto_rencana_ringkas* = daftar_rencana(filter = draf_saya, user_id)"), ("ret", "dto_rencana_ringkas*"),
           ("ev", "rencana terpilih"), ("q", "dto_rencana = rincian_rencana(rencana)"), ("ret", "dto_rencana")]),
         ("«exception» E1", "[rencana bukan Draf, AB-01] · langkah 3",
          [("ret", "dto_status"), ("txt", "use case gagal")])]),
    SSD(7, "UC-25", "Isi Realisasi Rencana", ["Pengelola Lab (PIC)"],
        LOGIN + "Ada rencana Disahkan dengan item milik aktor.",
        [("ev", "(minta item saya)"), ("q", "dto_item_pic* = daftar_item_pic(user_id)"), ("ret", "dto_item_pic*"),
         ("ev", "item terpilih, dto_realisasi"), ("c", "catat_realisasi(item, dto_realisasi, user_id)"),
         ("q", "dto_capaian = capaian_item(item)"), ("ret", "dto_capaian")],
        [("«variant» V2", "[sudah ada realisasi untuk item dan periode lapor itu] · langkah 3",
          [("q", "dto_capaian = capaian_item(item)"), ("ret", "realisasi yang ada"), ("ev", "dto_realisasi (dikoreksi)"),
           ("c", "koreksi_realisasi(realisasi, dto_realisasi, user_id)"), ("ret", "dto_capaian")]),
         ("«exception» E1", "[bukti kosong, AB-18] · langkah 3",
          [("ret", "MSG bukti wajib"), ("txt", "kembali ke langkah 3")]),
         ("«exception» E2", "[rencana bukan Disahkan, AB-18] · langkah 3",
          [("ret", "dto_status"), ("txt", "use case gagal")])]),
    SSD(8, "UC-28", "Lihat Status Monev", ["KaLab"],
        LOGIN + "—",
        [("ev", "tanggal_acuan"), ("q", "dto_status_monev = status_monev(tanggal_acuan)"), ("ret", "dto_status_monev"),
         ("txt", "PKG-02: persentase dan skor (AB-24); PKG-01, 03, 13: kriteria tertinggi dan tautan bukti (AB-25)")],
        []),
]


def name_of(d):
    return f"SSD TO-BE ({d.n}-{N_SSD}) - {d.uc} {d.title}"


def notes_page():
    """Halaman catatan (bahan kerja, tidak disisipkan ke naskah): judul, prakondisi, dan legenda setiap SSD."""
    P, cells, y = "tk-ssd-notes-", [], 66

    def v(id, val, style, x, y, w, h):
        cells.append(f'<mxCell id="{P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                     f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    v("title", "Catatan system sequence diagram (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 14, 1100, 36)
    v("legend", LEGEND, NOTE, 40, y, 1100, 150)
    y += 170
    for d in D:
        v(f"pre{d.n}", f"<b>SSD-{d.n} · {d.uc} {d.title}</b><br><b>Prakondisi</b>: {d.pre}", NOTE, 40, y, 1100, 50)
        y += 60
    return (f'<diagram id="tk-ssd-notes" name="Catatan SSD TO-BE (bahan kerja)"><mxGraphModel dx="1600" dy="900" grid="1" '
            f'gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1180" '
            f'pageHeight="{y + 30}" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
            + "".join(cells) + "</root></mxGraphModel></diagram>")


open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(d.xml() for d in D) + notes_page() + "</mxfile>")
