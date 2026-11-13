import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]


def esc(s):
    return escape(s, {'"': "&quot;"})


LIFE = ("shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=0;collapsible=0;"
        "recursiveResize=0;outlineConnect=0;fontSize=12;fontStyle=1;size={size};")
PART = {"actor": "participant=umlActor;", "boundary": "participant=umlBoundary;", "control": "participant=umlControl;"}
EV = "html=1;endArrow=open;endSize=9;strokeColor=#333333;fontSize=11;verticalAlign=bottom;labelBackgroundColor=none;"
RET = "html=1;endArrow=open;endSize=9;dashed=1;strokeColor=#333333;fontSize=11;verticalAlign=bottom;labelBackgroundColor=none;"
CALL = "html=1;endArrow=block;endFill=1;endSize=9;strokeColor=#6C4A87;fontColor=#6C4A87;fontSize=11;verticalAlign=bottom;labelBackgroundColor=none;"
FRAME = "shape=umlFrame;whiteSpace=wrap;html=1;pointerEvents=0;width=54;height=22;fontSize=11;fontStyle=1;fillColor=none;"
GUARD = "text;html=1;fontSize=11;align=left;verticalAlign=middle;fontStyle=2;"
TXT = "text;html=1;fontSize=10;align=left;verticalAlign=middle;fontStyle=2;fontColor=#555555;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"

ROW = {"ev": 34, "ret": 34, "q": 34, "c": 34, "txt": 24, "ref": 48}
LEGEND = ("<b>Notasi</b> (Wazlawick 2024, Bab 7)<br>"
          "• Panah hitam penuh: <i>system event</i> (aktor → antarmuka)<br>"
          "• Panah hitam putus-putus: <i>system return</i> (antarmuka → aktor)<br>"
          "• Panah ungu, kepala segitiga: operasi sistem ke kontroler. "
          "<b>Command</b> <code>op(args)</code> mengubah data tanpa nilai balik; "
          "<b>query</b> <code>dto = op(args)</code> hanya membaca (CQS, §7.1)<br>"
          "• <code>dto_x</code> = data majemuk (lihat kamus DTO), <code>*</code> = koleksi, <i>terpilih</i> = pilihan dari daftar (§7.3)<br>"
          "• Stateless: <code>user_id</code> dikirim ke setiap operasi yang membutuhkannya (§7.5)<br>"
          "• <code>opt «exception»</code> / <code>opt «variant»</code>: alur alternatif; <code>ref</code>: use case lain (§7.6)")


class SSD:
    def __init__(self, n, uc, title, actors, pre, main, blocks):
        self.P = f"tk-ssd{n}-"
        self.n, self.uc, self.title, self.actors, self.pre, self.main, self.blocks = n, uc, title, actors, pre, main, blocks
        self.cells = []

    def v(self, id, val, style, x, y, w, h):
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def build(self):
        LY, HEAD = 120, 60
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
        self.v("title", f"SSD-{self.n} · {self.uc} {self.title}", TITLE, 40, 14, 1100, 32)
        self.v("pre", "<b>Prakondisi</b>: " + self.pre, NOTE, 40, 52, right - 40, 52)
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
        self.width = right + 380
        self.v("legend", LEGEND, NOTE, right + 30, LY, 330, 230)
        self.height = LY + lh + 40

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
            self.v(f"rt{self.k}", text, "text;html=1;fontSize=11;align=center;verticalAlign=middle;", x0 + 40,
                   y - 14, self.cx["ct"] - x0 - 20, 30)
        return y + ROW[kind]

    def xml(self):
        self.build()
        return (f'<diagram id="tk-ssd{self.n}" name="{esc("SSD-" + str(self.n) + " " + self.uc + " " + self.title)}">'
                f'<mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
                f'fold="1" page="1" pageScale="1" pageWidth="{self.width:.0f}" pageHeight="{self.height:.0f}" math="0" shadow="0">'
                '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")


LOGIN = "pengguna sudah login dan <code>user_id</code> diketahui antarmuka. "
D = [
    SSD(1, "UC-21", "Ajukan Dokumen", ["Penyusun", "Pemeriksa/Pengesah"],
        LOGIN + "Dokumen berstatus Draf.",
        [("ev", "(minta draf saya)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = draf_saya, user_id)"), ("ret", "dto_dokumen_ringkas*"),
         ("ev", "dokumen terpilih"), ("q", "dto_kelengkapan* = cek_kelengkapan(dokumen)"), ("ret", "dto_kelengkapan*"),
         ("ev", "(ajukan)"), ("c", "ajukan_dokumen(dokumen, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status"),
         ("ret", "pemberitahuan ‹dokumen, penyusun, tanggal_ajukan›", 1)],
        [("«exception» E1", "[kelengkapan belum terpenuhi, AB-01] · langkah 3",
          [("ret", "butir_belum_lengkap*, MSG kelengkapan"), ("txt", "use case gagal; dokumen tetap Draf")]),
         ("«exception» E2", "[tidak ada jabatan aktif yang berwenang, AB-02] · langkah 3",
          [("ret", "MSG belum ada pengesah berwenang"), ("txt", "use case gagal")])]),
    SSD(2, "UC-24", "Kembalikan Dokumen", ["Pemeriksa/Pengesah", "Penyusun"],
        LOGIN + "Dokumen berstatus Diajukan atau Diperiksa.",
        [("ev", "(minta dokumen menunggu)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = menunggu_tindakan_saya, user_id)"), ("ret", "dto_dokumen_ringkas*"),
         ("ev", "dokumen terpilih"), ("q", "dto_rincian_dokumen = rincian_dokumen(dokumen)"), ("ret", "dto_rincian_dokumen"),
         ("ev", "alasan"), ("c", "kembalikan_dokumen(dokumen, alasan, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status"),
         ("ret", "pemberitahuan ‹dokumen, alasan›", 1)],
        [("«variant» V1", "[penolakan di atas kertas, dicatat penyusun]",
          [("ev", "dokumen terpilih", 1), ("q", "dto_rincian_dokumen = rincian_dokumen(dokumen)"), ("ret", "dto_rincian_dokumen", 1),
           ("ev", "‹alasan, nama_pengesah, jabatan_pengesah›", 1),
           ("c", "catat_pengembalian(dokumen, alasan, nama_pengesah, jabatan_pengesah, user_id)"),
           ("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status", 1)]),
         ("«exception» E1", "[alasan kosong, AB-05] · langkah 3",
          [("ret", "MSG alasan wajib"), ("txt", "kembali ke pengiriman alasan")])]),
    SSD(3, "UC-26", "Unggah Dokumen Bertanda Tangan", ["Penyusun", "Pengesah"],
        LOGIN + "Dokumen Diajukan (pemeriksaan tidak aktif) atau Diperiksa; rencana/SK sudah diterbitkan (UC-25).",
        [("ev", "(minta dokumen menunggu tanda tangan)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = menunggu_ttd, user_id)"),
         ("ret", "dto_dokumen_ringkas*"), ("ev", "dokumen terpilih"),
         ("q", "dto_rincian_dokumen = rincian_dokumen(dokumen)"), ("ret", "dto_rincian_dokumen"),
         ("ev", "dto_ttd"), ("c", "lampirkan_berkas_ttd(dokumen, dto_ttd, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status (siap disahkan)"),
         ("ret", "pemberitahuan ‹dokumen siap disahkan›", 1)],
        [("«variant» V1", "[berkas sebelumnya sudah ada]",
          [("txt", "dto_rincian_dokumen memuat berkas sebelumnya; lampirkan_berkas_ttd() menggantinya, berkas lama tetap di riwayat")]),
         ("«exception» E1", "[berkas tidak terbaca] · langkah 3", [("ret", "MSG berkas tidak terbaca"), ("txt", "kembali ke pengiriman dto_ttd")]),
         ("«exception» E2", "[penanda tangan bukan pemegang jabatan berwenang, AB-02] · langkah 3",
          [("ret", "pengesah_berwenang*, MSG"), ("txt", "kembali ke pengiriman dto_ttd")])]),
    SSD(4, "UC-27", "Sahkan Dokumen", ["Pengesah", "Penyusun"],
        LOGIN + "Pengguna memegang jabatan aktif yang berwenang mengesahkan jenis dokumen itu; dokumen Diajukan atau Diperiksa.",
        [("ev", "(minta dokumen menunggu pengesahan)"), ("q", "dto_dokumen_ringkas* = daftar_dokumen(filter = menunggu_pengesahan_saya, user_id)"),
         ("ret", "dto_dokumen_ringkas*"), ("ev", "dokumen terpilih"),
         ("q", "dto_rincian_dokumen = rincian_dokumen(dokumen)"), ("ret", "dto_rincian_dokumen"),
         ("ev", "(sahkan)"), ("c", "sahkan_dokumen(dokumen, user_id)"),
         ("q", "dto_status = status_dokumen(dokumen)"), ("ret", "dto_status"),
         ("ret", "pemberitahuan ‹dokumen disahkan›", 1)],
        [("«variant» V1", "[pengesah tidak menyetujui] · langkah 5", [("ref", "UC-24 Kembalikan Dokumen (SSD-2)")]),
         ("«variant» V2", "[KaLab mengesahkan atas nama Dekan] [KONFIRMASI]",
          [("c", "sahkan_dokumen(dokumen, user_id, atas_nama)"), ("txt", "dto_status memuat Dekan sebagai pengesah dan KaLab sebagai pencatat")]),
         ("«exception» E1", "[berkas bertanda tangan belum ada, AB-03] · langkah 5",
          [("ret", "MSG berkas belum diunggah"), ("ref", "UC-26 Unggah Dokumen Bertanda Tangan (SSD-3)")]),
         ("«exception» E2", "[pemeriksaan wajib belum dilakukan, AB-09] · langkah 5",
          [("ret", "MSG dokumen harus diperiksa"), ("txt", "use case gagal")])]),
    SSD(5, "UC-08", "Unggah Versi Dokumen", ["Laboran"],
        LOGIN + "Dokumen induk sudah terdaftar (UC-07).",
        [("ev", "(cari dokumen induk)"), ("q", "dto_dokumen_induk* = daftar_dokumen_induk()"), ("ret", "dto_dokumen_induk*"),
         ("ev", "dokumen_induk terpilih"), ("q", "dto_info_versi = info_versi(dokumen_induk)"), ("ret", "dto_info_versi"),
         ("ev", "dto_versi_baru"), ("c", "buat_versi(dokumen_induk, dto_versi_baru, user_id)"),
         ("q", "dto_versi = rincian_versi(dokumen_induk, dto_versi_baru.revisi)"), ("ret", "dto_versi (Draf)")],
        [("«variant» V1", "[belum ada versi berlaku] · langkah 2–3",
          [("txt", "dto_info_versi tanpa versi berlaku; dto_versi_baru dikirim dengan revisi = 0 dan tanpa alasan revisi")]),
         ("«exception» E1", "[ada versi yang sedang diproses, AB-13] · langkah 2",
          [("ret", "versi_diproses, MSG"), ("txt", "use case gagal; lanjutkan versi yang sedang diproses")]),
         ("«exception» E2", "[revisi ≤ revisi berlaku] · langkah 3",
          [("ret", "revisi_berlaku, MSG"), ("txt", "kembali ke pengiriman dto_versi_baru")])]),
    SSD(6, "UC-11", "Tinjau Ulang Dokumen", ["Laboran/KaLab"],
        LOGIN + "Dokumen punya versi Disahkan.",
        [("ev", "(minta dokumen yang perlu ditinjau)"), ("q", "dto_jadwal_tinjau* = daftar_jadwal_tinjau(user_id)"),
         ("ret", "dto_jadwal_tinjau*"), ("ev", "dokumen terpilih"),
         ("q", "dto_rincian_tinjau = rincian_tinjau(dokumen)"), ("ret", "dto_rincian_tinjau"),
         ("ev", "dto_hasil_tinjau (hasil = tetap_berlaku)"), ("c", "catat_tinjau_ulang(dokumen, dto_hasil_tinjau, user_id)"),
         ("q", "dto_status_tinjau = status_tinjau(dokumen)"), ("ret", "dto_status_tinjau")],
        [("«variant» V1", "[hasil = perlu_revisi] · langkah 5",
          [("txt", "dto_status_tinjau = Menunggu Revisi"), ("ref", "UC-08 Unggah Versi Dokumen (SSD-5)")]),
         ("«variant» V2", "[hasil = tidak_diperlukan] · langkah 5",
          [("txt", "dto_status_tinjau = diusulkan dicabut, memuat jabatan yang berwenang mencabut"), ("ref", "UC-28 Cabut Dokumen")]),
         ("«exception» E1", "[catatan kosong ∧ hasil ≠ tetap_berlaku] · langkah 5",
          [("ret", "MSG catatan wajib"), ("txt", "kembali ke pengiriman dto_hasil_tinjau")])]),
    SSD(7, "UC-16", "Susun Rencana", ["KaLab"],
        LOGIN + "Periode yang akan direncanakan tersedia.",
        [("ev", "dto_rencana_baru"), ("c", "buat_rencana(dto_rencana_baru, user_id)"),
         ("q", "dto_rencana = rincian_rencana(dto_rencana_baru)"), ("ret", "dto_rencana (Draf, bagian wajib)"),
         ("ev", "dto_isi_rencana"), ("c", "ubah_isi_rencana(rencana, dto_isi_rencana, user_id)"),
         ("q", "dto_rencana = rincian_rencana(rencana)"), ("ret", "dto_rencana (bagian terisi / belum)"),
         ("ev", "dto_item*"), ("c", "simpan_item_rencana(rencana, dto_item*, user_id)"),
         ("q", "dto_status_item* = status_item_rencana(rencana)"), ("ret", "dto_status_item*, rekap_anggaran")],
        [("«variant» V1", "[jenis = pengembangan] · setelah langkah 2",
          [("ev", "dto_gap*"), ("c", "simpan_gap(rencana, dto_gap*, user_id)"), ("q", "dto_status_gap = status_gap(rencana)"),
           ("ret", "dto_status_gap"), ("txt", "dto_item juga memuat gap, nilai_risiko, nilai_manfaat; dto_status_item memuat prioritas")]),
         ("«variant» V2", "[revisi dari rencana Disahkan] · menggantikan langkah 1",
          [("ev", "(cari rencana disahkan)"), ("q", "dto_rencana_ringkas* = daftar_rencana(filter = disahkan, user_id)"),
           ("ret", "dto_rencana_ringkas*"), ("ev", "rencana terpilih"), ("c", "buat_revisi_rencana(rencana, user_id)"),
           ("q", "dto_rencana = rincian_rencana(rencana_revisi)"), ("ret", "dto_rencana (draf revisi)")]),
         ("«variant» V3", "[melanjutkan draf] · menggantikan langkah 1",
          [("ev", "(cari draf)"), ("q", "dto_rencana_ringkas* = daftar_rencana(filter = draf_saya, user_id)"), ("ret", "dto_rencana_ringkas*"),
           ("ev", "rencana terpilih"), ("q", "dto_rencana = rincian_rencana(rencana)"), ("ret", "dto_rencana")]),
         ("«exception» E1", "[periode di luar rencana induk] · langkah 1", [("ret", "periode_induk, MSG")]),
         ("«exception» E2", "[PIC bukan personel aktif] · langkah 5", [("ret", "item_bermasalah*, MSG")])]),
    SSD(8, "UC-18", "Isi Realisasi Rencana", ["PIC (Laboran/KaLab)"],
        LOGIN + "Rencana Disahkan dan masih berlaku (AB-10).",
        [("ev", "(minta item tanggung jawab saya)"), ("q", "dto_item_pic* = daftar_item_pic(user_id, periode_lapor)"),
         ("ret", "dto_item_pic*"), ("ev", "item terpilih"), ("q", "dto_rincian_item = rincian_item(item)"),
         ("ret", "dto_rincian_item"), ("ev", "dto_realisasi"), ("c", "catat_realisasi(item, dto_realisasi, user_id)"),
         ("q", "dto_capaian = capaian_item(item, dto_realisasi.periode_lapor)"), ("ret", "dto_capaian")],
        [("«exception» E1", "[status = tidak_relevan ∧ alasan kosong, AB-10] · langkah 5",
          [("ret", "MSG alasan wajib"), ("txt", "kembali ke pengiriman dto_realisasi")]),
         ("«exception» E2", "[bukti kosong, AB-12] · langkah 5", [("ret", "MSG bukti wajib"), ("txt", "kembali ke pengiriman dto_realisasi")]),
         ("«exception» E3", "[pengguna bukan PIC item dan bukan KaLab, AB-11] · langkah 3",
          [("ret", "pic_item, MSG"), ("txt", "use case gagal")])]),
]

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(d.xml() for d in D) + "</mxfile>")
