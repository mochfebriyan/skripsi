"""System sequence diagram modul SDM & Kompetensi (Langkah 8), satu halaman per SSD + halaman catatan.

Fungsi gambar dan gaya disalin dari contoh-tata-kelola/ssd.py versi `main` (polos hitam-putih);
yang diganti hanya data dan prefiks ID (sdm-). Garis putus-putus hanya untuk return (notasi UML).

Jalankan:
    python -I projek-fiklab/tools/drawio/sdm/ssd.py projek-fiklab/rancangan/ssd-sdm.drawio
    python -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/ssd-sdm.drawio sdm-
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
          "• Panah hitam kepala terbuka: <i>system event</i> (aktor → antarmuka)<br>"
          "• Panah putus-putus: <i>system return</i> (antarmuka → aktor)<br>"
          "• Panah kepala segitiga penuh: operasi sistem ke kontroler. "
          "<b>Command</b> <code>op(args)</code> mengubah data tanpa nilai balik; "
          "<b>query</b> <code>dto = op(args)</code> hanya membaca (CQS, §7.1)<br>"
          "• <code>dto_x</code> = data majemuk (lihat kamus DTO), <code>*</code> = koleksi, <i>terpilih</i> = pilihan dari daftar (§7.3)<br>"
          "• Stateless: <code>user_id</code> dikirim ke setiap operasi yang membutuhkannya (§7.5)<br>"
          "• <code>opt «exception»</code> / <code>opt «variant»</code>: alur alternatif; <code>ref</code>: use case lain (§7.6)<br>"
          "Sumber: expanded-use-case-sdm.md (alur lengkap, AB-SDM-01–28); katalog operasi dan kamus DTO di ssd-sdm.md · "
          "Draf 19 Nov 2026 · Zahir")


class SSD:
    def __init__(self, n, uc, title, actors, pre, main, blocks):
        self.P = f"sdm-ssd{n}-"
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
        self.cx = {k: x + w / 2 for k, _, _, x, w in lanes}
        right = max(self.cx.values()) + 90
        total = 60 + sum(ROW[e[0]] for e in self.main)
        for _, _, ents in self.blocks:
            total += 50 + sum(ROW[e[0]] for e in ents) + 16
        lh = HEAD + total + 30
        self.LY, self.lh = LY, lh
        for k, label, part, x, w in lanes:
            self.v(k, label, LIFE.format(size=HEAD) + PART[part], x, LY, w, lh)
        y = LY + HEAD + 40
        self.k = 0
        for e in self.main:
            y = self.entry(e, y)
        for i, (stereo, guard, ents) in enumerate(self.blocks):
            y += 16
            top = y
            y += 34
            for e in ents:
                y = self.entry(e, y)
            h = y - top + 6
            self.v(f"fr{i}", "opt", FRAME, 20, top, right - 20, h)
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
        if kind == "ev":
            self.msg("a0", "ui", text, EV, y)
        elif kind == "ret":
            self.msg("ui", "a0", text, RET, y)
        elif kind in ("q", "c"):
            self.msg("ui", "ct", text, CALL, y)
        elif kind == "txt":
            self.k += 1
            self.v(f"t{self.k}", text, TXT, self.cx["a0"] + 10, y - 12, 640, 22)
        elif kind == "ref":
            self.k += 1
            x0 = self.cx["a0"] - 30
            self.v(f"r{self.k}", "ref", FRAME.replace("width=54", "width=40"), x0, y - 18, self.cx["ct"] - x0 + 30, 38)
            self.v(f"rt{self.k}", text, "text;html=1;fontSize=11;align=center;verticalAlign=middle;" + FONT, x0 + 40,
                   y - 14, self.cx["ct"] - x0 - 20, 30)
        return y + ROW[kind]

    def xml(self):
        self.build()
        return (f'<diagram id="sdm-ssd{self.n}" name="{esc(name_of(self))}">'
                f'<mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
                f'fold="1" page="1" pageScale="1" pageWidth="{self.width:.0f}" pageHeight="{self.height:.0f}" math="0" shadow="0">'
                '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")


LOGIN = "pengguna sudah teridentifikasi dan <code>user_id</code> diketahui antarmuka. "
GAGAL = ("txt", "use case gagal")
D = [
    SSD(1, "UC-SDM-06", "Catat Hasil Seleksi Asisten", ["Pengelola Lab"],
        LOGIN + "Mata kuliah dan periode terdaftar. Seleksi sendiri dilakukan di luar sistem.",
        [("ev", "‹periode, mata_kuliah›"),
         ("q", "dto_seleksi_ringkas* = daftar_seleksi(periode, mata_kuliah)"),
         ("q", "dto_personel_ringkas* = daftar_personel(filter = asisten)"),
         ("ret", "dto_seleksi_ringkas*, dto_personel_ringkas*"),
         ("ev", "dto_seleksi (personel terpilih, keputusan = lulus)"),
         ("c", "catat_seleksi(dto_seleksi, user_id)"),
         ("q", "dto_seleksi_ringkas* = daftar_seleksi(periode, mata_kuliah)"),
         ("ret", "dto_seleksi_ringkas* (seleksi baru tercatat)")],
        [("«variant» V1", "[calon belum terdaftar sebagai Personel] · langkah 3",
          [("txt", "dto_seleksi memuat nama_calon; catat_seleksi() membuat Personel asisten (AB-SDM-15)")]),
         ("«variant» V2", "[lulus dengan pengecualian] · langkah 3",
          [("txt", "dto_seleksi memuat keputusan = lulus_pengecualian, alasan, penyetuju")]),
         ("«exception» E1", "[pengecualian tanpa alasan atau penyetuju, AB-SDM-15] · langkah 3",
          [("ret", "MSG data pengecualian wajib"), ("txt", "kembali ke langkah 3")]),
         ("«exception» E2", "[seleksi untuk personel, MK, dan periode itu sudah ada, AB-SDM-15] · langkah 3",
          [("ret", "dto_seleksi_ringkas (yang sudah ada)"), GAGAL])]),
    SSD(2, "UC-SDM-07", "Susun Surat Tugas", ["Pengelola Lab"],
        LOGIN + "Periode, kelas, dan ruang terdaftar di Core.",
        [("ev", "dto_surat_baru (nomor, periode)"),
         ("c", "buat_surat_tugas(dto_surat_baru, user_id)"),
         ("q", "dto_surat = rincian_surat_tugas(surat)"),
         ("q", "dto_personel_ringkas* = daftar_personel(filter = aktif)"),
         ("ret", "dto_surat (Draf, kelas dan kebutuhan, ruang), dto_personel_ringkas*"),
         ("ev", "dto_penugasan*"),
         ("c", "simpan_baris_penugasan(surat, dto_penugasan*, user_id)"),
         ("q", "dto_kelengkapan* = cek_kelengkapan(surat)"),
         ("ret", "dto_surat, dto_kelengkapan*")],
        [("«variant» V1", "[melanjutkan surat Draf] · menggantikan langkah 1–2",
          [("ev", "(cari draf)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = draf_saya, jenis = surat_tugas, user_id)"),
           ("ret", "dto_dokumen_ringkas*"), ("ev", "surat terpilih"), ("q", "dto_surat = rincian_surat_tugas(surat)"),
           ("ret", "dto_surat")]),
         ("«exception» E1", "[surat bukan Draf, AB-SDM-01] · langkah 3",
          [("q", "dto_status = status_dokumen(surat)"), ("ret", "dto_status"), GAGAL])]),
    SSD(3, "UC-SDM-12", "Catat Asesmen Keterampilan", ["Pengelola Lab"],
        LOGIN + "Tugas/alat dan personel terdaftar. Uji keterampilan dilakukan di luar sistem.",
        [("ev", "(minta tugas/alat)"),
         ("q", "dto_tugas_khusus_ringkas* = daftar_tugas_khusus(filter = aktif)"),
         ("ret", "dto_tugas_khusus_ringkas*"),
         ("ev", "tugas_khusus terpilih, dto_asesmen (kesimpulan = layak)"),
         ("c", "catat_asesmen(tugas_khusus, dto_asesmen, user_id)"),
         ("q", "dto_asesmen = rincian_asesmen(asesmen)"),
         ("ret", "dto_asesmen (+ bukti_kompetensi* demonstrasi, AB-SDM-17)")],
        [("«variant» V1", "[kesimpulan = belum_layak] · langkah 3",
          [("txt", "dto_asesmen.bukti_kompetensi* kosong; use case berhasil")])]),
    SSD(4, "UC-SDM-13", "Susun Otorisasi", ["KaLab"],
        LOGIN + "Tugas/alat terdaftar.",
        [("ev", "‹personel, tugas_khusus›"),
         ("c", "buat_otorisasi(personel, tugas_khusus, user_id)"),
         ("q", "dto_otorisasi = rincian_otorisasi(otorisasi)"),
         ("ret", "dto_otorisasi (Draf, masa berlaku awal, dasar*, calon_supervisor*)"),
         ("ev", "dto_otorisasi (dasar, lingkup, level, supervisor, berlaku)"),
         ("c", "ubah_otorisasi(otorisasi, dto_otorisasi, user_id)"),
         ("q", "dto_kelengkapan* = cek_kelengkapan(otorisasi)"),
         ("ret", "dto_otorisasi, dto_kelengkapan*")],
        [("«variant» V1", "[otorisasi baru dari keputusan evaluasi ulang] · menggantikan langkah 1",
          [("ev", "evaluasi terpilih"), ("c", "buat_otorisasi_dari_evaluasi(evaluasi, user_id)"),
           ("txt", "lanjut ke langkah 2; personel, tugas/alat, dan lingkup disalin dari otorisasi lama")]),
         ("«exception» E1", "[otorisasi bukan Draf, AB-SDM-01] · langkah 3",
          [("q", "dto_status = status_dokumen(otorisasi)"), ("ret", "dto_status"), GAGAL])]),
    SSD(5, "UC-SDM-15", "Putuskan Evaluasi Ulang Otorisasi", ["Pengelola Lab"],
        LOGIN + "Ada evaluasi ulang berstatus Terbuka (UC-SDM-14). Personel sudah dinilai ulang di luar sistem.",
        [("ev", "(minta evaluasi terbuka)"),
         ("q", "dto_evaluasi_ringkas* = daftar_evaluasi(filter = terbuka, user_id)"),
         ("ret", "dto_evaluasi_ringkas*"),
         ("ev", "evaluasi terpilih, dto_keputusan (keputusan = diperpanjang)"),
         ("c", "putuskan_evaluasi(evaluasi, dto_keputusan, user_id)"),
         ("q", "dto_evaluasi = rincian_evaluasi(evaluasi)"),
         ("ret", "dto_evaluasi (Diputuskan, tindak lanjut: susun otorisasi baru)")],
        [("«variant» V1", "[keputusan = dicabut] · langkah 3",
          [("txt", "dto_evaluasi.tindak_lanjut = cabut otorisasi"), ("ref", "UC-SDM-28 Cabut Dokumen SDM (dilakukan KaLab)")]),
         ("«variant» V2", "[keputusan = tetap_berlaku, KP-1] · langkah 3",
          [("txt", "dto_evaluasi.tindak_lanjut kosong; use case berhasil")]),
         ("«exception» E1", "[hasil atau penilai kosong, AB-SDM-19] · langkah 3",
          [("ret", "MSG data wajib"), ("txt", "kembali ke langkah 3")]),
         ("«exception» E2", "[evaluasi tidak lagi Terbuka, AB-SDM-19] · langkah 3",
          [("q", "dto_evaluasi = rincian_evaluasi(evaluasi)"), ("ret", "dto_evaluasi"), GAGAL])]),
    SSD(6, "UC-SDM-17", "Susun Rencana Pelatihan", ["KaLab"],
        LOGIN + "Periode tahunan terdaftar; kompetensi wajib jabatan dan bukti kompetensi sudah tercatat.",
        [("ev", "dto_rencana_baru (judul, periode)"),
         ("c", "buat_rencana_pelatihan(dto_rencana_baru, user_id)"),
         ("q", "dto_rencana = rincian_rencana_pelatihan(rencana)"),
         ("ret", "dto_rencana (Draf, kebutuhan* terisi awal, AB-SDM-20)"),
         ("ev", "dto_kebutuhan_pelatihan*"),
         ("c", "simpan_kebutuhan(rencana, dto_kebutuhan_pelatihan*, user_id)"),
         ("q", "dto_kompetensi_ringkas* = daftar_kompetensi(filter = aktif)"),
         ("ret", "dto_rencana, dto_kompetensi_ringkas*"),
         ("ev", "dto_item_pelatihan*"),
         ("c", "simpan_item_pelatihan(rencana, dto_item_pelatihan*, user_id)"),
         ("q", "dto_kelengkapan* = cek_kelengkapan(rencana)"),
         ("ret", "dto_rencana, dto_kelengkapan*")],
        [("«variant» V2", "[melanjutkan rencana Draf] · menggantikan langkah 1–2",
          [("ev", "(cari draf)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = draf_saya, jenis = rencana_pelatihan, user_id)"),
           ("ret", "dto_dokumen_ringkas*"), ("ev", "rencana terpilih"),
           ("q", "dto_rencana = rincian_rencana_pelatihan(rencana)"), ("ret", "dto_rencana")]),
         ("«exception» E1", "[rencana bukan Draf, AB-SDM-01] · langkah 3",
          [("q", "dto_status = status_dokumen(rencana)"), ("ret", "dto_status"), GAGAL])]),
    SSD(7, "UC-SDM-19", "Catat Evaluasi Efektivitas Pelatihan", ["Pengelola Lab"],
        LOGIN + "Ada realisasi pelatihan yang belum dievaluasi (UC-SDM-18).",
        [("ev", "(minta realisasi belum dievaluasi)"),
         ("q", "dto_realisasi_ringkas* = daftar_realisasi(filter = belum_dievaluasi, user_id)"),
         ("ret", "dto_realisasi_ringkas*"),
         ("ev", "realisasi terpilih, dto_evaluasi_pelatihan (kesimpulan = efektif)"),
         ("c", "catat_evaluasi_efektivitas(realisasi, dto_evaluasi_pelatihan, user_id)"),
         ("q", "dto_realisasi = rincian_realisasi(realisasi)"),
         ("ret", "dto_realisasi (+ evaluasi, bukti_kompetensi pelatihan, AB-SDM-23)")],
        [("«variant» V1", "[kesimpulan = perlu_pengembangan] · langkah 3",
          [("txt", "tidak ada bukti kompetensi baru; tindak lanjut tercatat; use case berhasil")]),
         ("«exception» E1", "[realisasi sudah punya evaluasi, AB-SDM-23] · langkah 3",
          [("q", "dto_realisasi = rincian_realisasi(realisasi)"), ("ret", "dto_realisasi (evaluasi yang ada)"), GAGAL])]),
    SSD(8, "UC-SDM-23", "Ajukan Dokumen SDM", ["Pengelola Lab"],
        LOGIN + "Ada dokumen SDM (Surat Tugas, Otorisasi, Rencana Pelatihan) berstatus Draf yang disusun aktor.",
        [("ev", "(minta draf saya)"),
         ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = draf_saya, user_id)"),
         ("ret", "dto_dokumen_ringkas*"),
         ("ev", "dokumen terpilih, (ajukan)"),
         ("c", "ajukan_dokumen(dokumen, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"),
         ("ret", "dto_status (Diajukan; rencana: kebutuhan dibekukan)")],
        [("«exception» E1", "[dokumen belum lengkap, AB-SDM-02/03/04 sesuai jenis] · langkah 3",
          [("q", "dto_kelengkapan* = cek_kelengkapan(dokumen)"), ("ret", "dto_kelengkapan*"),
           ("txt", "use case gagal; dokumen tetap Draf")]),
         ("«exception» E2", "[dokumen bukan Draf, AB-SDM-01] · langkah 3",
          [("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status"), GAGAL])]),
    SSD(9, "UC-SDM-27", "Sahkan Dokumen SDM", ["KaLab"],
        LOGIN + "Aktor adalah KaLab (AB-SDM-08). Ada dokumen SDM Diajukan yang sudah ditandatangani di luar sistem.",
        [("ev", "(minta dokumen diajukan)"),
         ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = diajukan, user_id)"),
         ("ret", "dto_dokumen_ringkas*"),
         ("ev", "dokumen terpilih"),
         ("q", "dto_rincian_dokumen = rincian_dokumen(dokumen, user_id)"),
         ("q", "dto_personel_ringkas* = daftar_pengesah_berwenang(dokumen)"),
         ("ret", "dto_rincian_dokumen, dto_personel_ringkas*"),
         ("ev", "‹pengesah terpilih, tanggal_sah›"),
         ("c", "sahkan_dokumen(dokumen, pengesah, tanggal_sah, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"),
         ("ret", "dto_status (Disahkan, dokumen_diganti)")],
        [("«exception» E1", "[berkas bertanda tangan belum ada, AB-SDM-06] · langkah 5",
          [("ret", "MSG berkas belum diunggah"), ("ref", "UC-SDM-25 Unggah Dokumen SDM Bertanda Tangan")]),
         ("«exception» E2", "[pengesah tidak berwenang, AB-SDM-07] · langkah 5",
          [("ret", "dto_personel_ringkas*, MSG pengesah tidak berwenang"), ("txt", "kembali ke langkah 5")]),
         ("«exception» E3", "[sudah ada Rencana Pelatihan Disahkan untuk periode itu, AB-SDM-12] · langkah 5",
          [("ret", "dto_dokumen_ringkas (rencana yang berlaku)"), GAGAL])]),
    SSD(10, "UC-SDM-22", "Lihat Status Monev SDM", ["KaLab"],
        LOGIN + "—",
        [("ev", "‹periode, tanggal_acuan›"),
         ("q", "dto_status_monev = status_monev(periode, tanggal_acuan)"),
         ("ret", "dto_status_monev"),
         ("txt", "PKG-04 dan PKG-10: persentase, skor, unit gagal (AB-SDM-26, 27); PKG-14: kriteria tertinggi (AB-SDM-28)"),
         ("ev", "unit terpilih"),
         ("q", "dto_unit_monev = rincian_unit_monev(unit, tanggal_acuan)"),
         ("ret", "dto_unit_monev (syarat per unit + tautan rekaman bukti)")],
        []),
]
N_SSD = len(D)


def name_of(d):
    return f"SSD TO-BE ({d.n}-{N_SSD}) - {d.uc} {d.title}"


def notes_page():
    P, cells, y = "sdm-ssd-notes-", [], 66

    def v(id, val, style, x, y, w, h):
        cells.append(f'<mxCell id="{P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                     f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    v("title", "Catatan system sequence diagram modul SDM (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 14, 1100, 36)
    v("legend", LEGEND, NOTE, 40, y, 1100, 150)
    y += 170
    for d in D:
        v(f"pre{d.n}", f"<b>SSD-{d.n} · {d.uc} {d.title}</b><br><b>Prakondisi</b>: {d.pre}", NOTE, 40, y, 1100, 50)
        y += 60
    return (f'<diagram id="sdm-ssd-notes" name="Catatan SSD TO-BE (bahan kerja)"><mxGraphModel dx="1600" dy="900" grid="1" '
            f'gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1180" '
            f'pageHeight="{y + 30}" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
            + "".join(cells) + "</root></mxGraphModel></diagram>")


with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(d.xml() for d in D) + notes_page() + "</mxfile>")
