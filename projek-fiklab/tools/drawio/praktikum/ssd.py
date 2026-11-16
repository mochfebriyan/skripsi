"""System sequence diagram modul Pelaksanaan Praktikum (langkah 8), 5 halaman.

Mesin gambar disalin dari contoh-tata-kelola/ssd.py; prefiks, lebar lajur, nama halaman, dan data diganti.
Pemakaian: python -X utf8 -I ssd.py projek-fiklab/rancangan/ssd-praktikum.drawio
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]


def esc(s):
    return escape(s, {'"': "&quot;"})


LIFE = ("shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=0;collapsible=0;"
        "recursiveResize=0;outlineConnect=0;fontSize=12;fontStyle=1;size={size};")
PART = {"actor": "participant=umlActor;verticalLabelPosition=top;verticalAlign=bottom;", "boundary": "participant=umlBoundary;", "control": "participant=umlControl;"}
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
    def __init__(self, n, uc, title, actors, pre, main, blocks, note=""):
        self.P = f"prk-ssd{n}-"
        self.n, self.uc, self.title, self.actors, self.pre, self.main, self.blocks = n, uc, title, actors, pre, main, blocks
        self.cells, self.note = [], note

    def v(self, id, val, style, x, y, w, h):
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def build(self):
        LY, HEAD = 150, 60
        lanes = [("a0", ":" + self.actors[0], "actor", 50, 60),
                 ("ui", ":Antarmuka", "boundary", 400, 130),
                 ("ct", ":Kontroler", "control", 900, 130)]
        if len(self.actors) > 1:
            lanes.append(("a1", ":" + self.actors[1], "actor", 1300, 60))
        self.cx = {k: x + w / 2 for k, _, _, x, w in lanes}
        right = max(self.cx.values()) + 90
        entries = list(self.main)
        total = 60 + sum(ROW[e[0]] for e in entries)
        for _, _, ents in self.blocks:
            total += 66 + sum(ROW[e[0]] for e in ents) + 16
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
            y += 50
            for e in ents:
                y = self.entry(e, y)
            h = y - top + 6
            kind = "opt"
            self.v(f"fr{i}", kind, FRAME, 20, top, right - 20, h)
            self.v(f"gd{i}", f"{stereo} {guard}", GUARD, 82, top, right - 110, 22)
            y += 6
        self.width = right + 380
        self.v("legend", LEGEND, NOTE, right + 30, LY, 330, 230)
        self.v("src", (self.note + "<br><br>" if self.note else "") + SRC, NOTE, right + 30, LY + 250, 330, 150)
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
            self.v(f"t{self.k}", text, TXT, self.cx["a0"] + 10, y - 12, 760, 22)
        elif kind == "ref":
            self.k += 1
            x0 = self.cx["a0"] - 30
            self.v(f"r{self.k}", "ref", FRAME.replace("width=54", "width=40"), x0, y - 18, self.cx["ct"] - x0 + 30, 38)
            self.v(f"rt{self.k}", text, "text;html=1;fontSize=11;align=center;verticalAlign=middle;", x0 + 40,
                   y - 14, self.cx["ct"] - x0 - 20, 30)
        return y + ROW[kind]

    def xml(self):
        self.build()
        return (f'<diagram id="prk-ssd{self.n}" name="{esc(f"SSD TO-BE ({self.n}-{len(D)}) - {self.uc} {self.title}")}">'
                f'<mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
                f'fold="1" page="1" pageScale="1" pageWidth="{self.width:.0f}" pageHeight="{self.height:.0f}" math="0" shadow="0">'
                '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")



SRC = ("Sumber: expanded-use-case-praktikum.md (alur lengkap, AB-PRK-01–34). Katalog operasi dan kamus DTO: ssd-praktikum.md. "
       "Draf 16 Nov 2026 · Herrens")
LOGIN = "pengguna sudah login dan <code>user_id</code> diketahui antarmuka. "
D = [
    SSD(1, "UC-PRK-03", "Impor Jadwal Kelas", ["Laboran"],
        LOGIN + "Periode, Ruang Lab, dan Personel dosen terdaftar. Berkas jadwal dari tim jadwal fakultas <b>[ASUMSI: impor berkas, tanpa API]</b>.",
        [("ev", "periode, berkas_jadwal, tanggal_pertemuan_pertama"),
         ("txt", "antarmuka membaca baris berkas menjadi dto_baris_jadwal* (fitur impor bawaan Odoo)"),
         ("q", "dto_pratinjau_impor = pratinjau_impor(periode, dto_baris_jadwal*, tanggal_pertemuan_pertama)"),
         ("ret", "dto_pratinjau_impor (16 tanggal per kelas, peringatan kapasitas)"),
         ("ev", "(konfirmasi impor)"),
         ("c", "impor_jadwal(periode, dto_baris_jadwal*, tanggal_pertemuan_pertama, user_id)"),
         ("q", "dto_ringkasan_jadwal = ringkasan_jadwal(periode)"),
         ("ret", "dto_ringkasan_jadwal (Sesi terjadwal, kelas lewat kapasitas)")],
        [("«variant» V1", "[tanpa berkas: satu kelas diisi manual] · langkah 1",
          [("ev", "dto_baris_jadwal (satu kelas: pola mingguan), tanggal_pertemuan_pertama"),
           ("txt", "operasi sama: pratinjau_impor() lalu impor_jadwal() dengan satu baris")]),
         ("«exception» E1", "[ruang bentrok, AB-PRK-01] · langkah 2",
          [("ret", "dto_konflik*, MSG bentrok"), ("txt", "kelas yang bentrok tidak dibangkitkan; laboran menyampaikan bentrok ke fakultas (di luar sistem)")]),
         ("«exception» E2", "[kelas terkunci: jadwal periode sudah diajukan/disahkan atau Sesi sudah berjurnal, AB-PRK-04] · langkah 2",
          [("ret", "kelas_terkunci*, MSG"), ("txt", "kelas itu dilewati; Sesi yang ada diubah lewat UC-PRK-14; kelas baru menunggu jadwal dicabut (UC-06 Tata Kelola) lalu disusun ulang")]),
         ("«exception» E3", "[baris tidak valid: ruang/dosen tidak dikenal, jam selesai ≤ jam mulai] · langkah 2",
          [("ret", "dto_baris_salah*, MSG"), ("txt", "kembali ke langkah 1")])],
        "<b>Catatan</b>: peringatan kapasitas (AB-PRK-03) tidak menggagalkan impor. Pertemuan 8 = UTS, 16 = UAS (AB-PRK-02)."),
    SSD(2, "UC-PRK-11", "Periksa Kesiapan Sesi", ["Laboran", "Dosen kelas"],
        LOGIN + "Ada Sesi terpublikasi hari itu (Penetapan Jadwal periode sudah disahkan).",
        [("ev", "(minta Sesi hari ini)"),
         ("q", "dto_sesi_ringkas* = daftar_sesi(filter = kesiapan_hari_ini, user_id)"), ("ret", "dto_sesi_ringkas*"),
         ("ev", "sesi terpilih"),
         ("q", "dto_form_kesiapan = form_kesiapan(sesi)"),
         ("ret", "dto_form_kesiapan (butir dari modul; info alat, O)"),
         ("ev", "dto_hasil_butir*"),
         ("q", "keputusan_boleh* = keputusan_tersedia(sesi, dto_hasil_butir*)"), ("ret", "keputusan_boleh*"),
         ("ev", "keputusan"),
         ("c", "catat_pemeriksaan(sesi, dto_hasil_butir*, keputusan, user_id)"),
         ("q", "dto_pemeriksaan = rincian_pemeriksaan(sesi)"),
         ("ret", "dto_pemeriksaan (waktu_periksa, keputusan, tepat_waktu)")],
        [("«variant» V1", "[substitusi bahan] · langkah 5",
          [("txt", "dto_hasil_butir bahan memuat bahan_pengganti dan alasan_substitusi; butir menunggu persetujuan"),
           ("ret", "pemberitahuan ‹sesi, bahan, bahan_pengganti› (O)", 1),
           ("ref", "UC-PRK-12 Setujui Substitusi Bahan (oleh Dosen kelas, sesi lain)")]),
         ("«exception» E1", "[Sesi sudah punya pemeriksaan, AB-PRK-13] · langkah 4",
          [("ret", "dto_pemeriksaan, MSG sudah diperiksa"), ("ev", "dto_koreksi"),
           ("c", "koreksi_rekaman(pemeriksaan, dto_koreksi, user_id)"), ("txt", "koreksi terlacak (AB-PRK-31); kembali ke langkah 8")]),
         ("«exception» E2", "[ada butir bermasalah ∧ keputusan = siap, AB-PRK-15] · langkah 7",
          [("ret", "butir_bermasalah*, MSG"), ("txt", "kembali ke langkah 7")]),
         ("«exception» E3", "[substitusi belum disetujui ∧ keputusan = siap, AB-PRK-16] · langkah 7",
          [("ret", "butir_menunggu*, MSG"), ("txt", "kembali ke langkah 7")]),
         ("«exception» E4", "[waktu periksa ≥ jam mulai Sesi, AB-PRK-13] · langkah 8",
          [("txt", "dto_pemeriksaan.tepat_waktu = salah; use case berhasil, tetapi Sesi tidak memenuhi PKG-16 S1")])],
        "<b>Catatan</b>: butir dihitung oleh query <code>form_kesiapan()</code> dan baru disimpan oleh <code>catat_pemeriksaan()</code> (CQS). "
        "Data Alat ruang hanya dibaca lewat <code>check_ketersediaan_sesi()</code> Core (KF-PRK-52, O): peringatan dan isian awal, hasil tetap dari laboran (I-13). "
        "Bila keputusan <i>tunda</i>, laboran melanjutkan UC-PRK-14 sebagai use case terpisah."),
    SSD(3, "UC-PRK-13", "Kirim Jurnal Sesi", ["Petugas Praktikum"],
        LOGIN + "Ada Sesi terpublikasi yang sudah berlangsung. Petugas Praktikum = asisten, dosen, atau laboran.",
        [("ev", "(minta Sesi belum berjurnal)"),
         ("q", "dto_sesi_ringkas* = daftar_sesi(filter = belum_berjurnal, user_id)"), ("ret", "dto_sesi_ringkas* (penanda terlewat)"),
         ("ev", "sesi terpilih"),
         ("q", "dto_konteks_jurnal = konteks_jurnal(sesi, user_id)"), ("ret", "dto_konteks_jurnal"),
         ("ev", "dto_jurnal"),
         ("c", "simpan_jurnal(sesi, dto_jurnal, user_id)"),
         ("q", "dto_rincian_jurnal = rincian_jurnal(sesi)"), ("ret", "dto_rincian_jurnal (penanda penugasan SDM, O)"),
         ("ev", "(kirim)"),
         ("c", "kirim_jurnal(sesi, user_id)"),
         ("q", "dto_status_sesi = status_sesi(sesi)"), ("ret", "dto_status_sesi (terlaksana, waktu_kirim)")],
        [("«variant» V1", "[simpan sebagai draf] · setelah langkah 6",
          [("txt", "use case berhasil setelah simpan_jurnal(); dilanjutkan kemudian dari langkah 5 dengan rincian_jurnal(sesi)")]),
         ("«exception» E1", "[Sesi tidak terjadwal, belum terpublikasi, belum berlangsung, atau sudah berjurnal, AB-PRK-17] · langkah 4",
          [("ret", "dto_status_sesi, MSG"), ("txt", "use case gagal")]),
         ("«exception» E2", "[jam selesai ≤ jam mulai, AB-PRK-18] · langkah 5",
          [("ret", "MSG jam tidak valid"), ("txt", "kembali ke langkah 5")]),
         ("«exception» E3", "[isian wajib belum lengkap, AB-PRK-19] · langkah 7",
          [("q", "dto_kelengkapan* = cek_kelengkapan_jurnal(sesi)"), ("ret", "dto_kelengkapan*, MSG"), ("txt", "kembali ke langkah 5")])],
        "<b>Catatan</b>: presensi petugas merujuk <code>hr.employee</code>; ketidaksesuaian dengan penugasan SDM hanya ditandai (AB-PRK-20, O)."),
    SSD(4, "UC-PRK-15", "Putuskan Perubahan Sesi", ["KaLab", "Pengaju"],
        LOGIN + "KaLab memegang wewenang <i>mengesahkan</i> untuk jenis <i>perubahan_sesi</i>; ada Perubahan Sesi berstatus Diajukan.",
        [("ev", "(minta perubahan diajukan)"),
         ("q", "dto_pengajuan_ringkas* = daftar_pengajuan(filter = perubahan_diajukan, user_id)"), ("ret", "dto_pengajuan_ringkas*"),
         ("ev", "perubahan terpilih"),
         ("q", "dto_rincian_pengajuan = rincian_pengajuan(perubahan)"), ("ret", "dto_rincian_pengajuan (Sesi asal, usulan pengganti)"),
         ("ev", "dto_pengganti (boleh mengubah usulan)"),
         ("q", "dto_konflik* = cek_bentrok(dto_pengganti, kecuali = sesi_asal)"), ("ret", "dto_konflik* (kosong)"),
         ("ev", "keputusan = disetujui"),
         ("c", "putuskan_pengajuan(perubahan, disetujui, —, —, dto_pengganti, user_id)"),
         ("q", "dto_rincian_pengajuan = rincian_pengajuan(perubahan)"),
         ("ret", "dto_rincian_pengajuan (Disetujui, Sesi pengganti)"),
         ("ret", "pemberitahuan ‹perubahan, keputusan› (O)", 1)],
        [("«variant» V1 / V2", "[jenis = daring / batal] · langkah 5",
          [("txt", "tanpa dto_pengganti dan tanpa cek_bentrok(); daring: Sesi asal tetap terjadwal, moda = daring; batal: Sesi asal batal")]),
         ("«variant» V3", "[ditolak] · langkah 5",
          [("ev", "keputusan = ditolak, alasan"), ("c", "putuskan_pengajuan(perubahan, ditolak, alasan, karena_bentrok, —, user_id)"),
           ("q", "dto_rincian_pengajuan = rincian_pengajuan(perubahan)"), ("ret", "dto_rincian_pengajuan (Ditolak)"),
           ("ret", "pemberitahuan ‹perubahan, alasan› (O)", 1)]),
         ("«exception» E1", "[waktu pengganti bentrok, AB-PRK-01] · langkah 4",
          [("ret", "dto_konflik*, MSG bentrok"), ("txt", "kembali ke pengiriman dto_pengganti")]),
         ("«exception» E2", "[Sesi asal tidak lagi terjadwal, AB-PRK-12] · langkah 4",
          [("ret", "dto_status_sesi, MSG"), ("txt", "use case gagal")]),
         ("«exception» E3", "[alasan penolakan kosong, AB-PRK-10] · V3",
          [("ret", "MSG alasan wajib"), ("txt", "kembali ke V3.1")])],
        "<b>Dipakai ulang</b>: <code>daftar_pengajuan()</code>, <code>rincian_pengajuan()</code>, dan <code>putuskan_pengajuan()</code> "
        "juga melayani UC-PRK-08 Putuskan Pemakaian Lab (pola S2 sama, tanpa dto_pengganti)."),
    SSD(5, "UC-PRK-23", "Catat Evaluasi Survei", ["KaLab"],
        LOGIN + "Survei kepuasan periode sudah Ditetapkan dan tanggal tutupnya terlewati.",
        [("ev", "(minta survei siap dievaluasi)"),
         ("q", "dto_survei_ringkas* = daftar_survei(filter = siap_dievaluasi, user_id)"), ("ret", "dto_survei_ringkas*"),
         ("ev", "survei terpilih"),
         ("q", "dto_rekap_survei = rekap_survei(survei)"),
         ("ret", "dto_rekap_survei (response rate, rerata per aspek)"),
         ("ev", "kesimpulan_aspek*, dto_rtl*"),
         ("c", "catat_evaluasi_survei(survei, kesimpulan_aspek*, dto_rtl*, user_id)"),
         ("q", "dto_status_survei = status_survei(survei)"),
         ("ret", "dto_status_survei (Dievaluasi, kriteria_tertinggi K1–K3)")],
        [("«exception» E1", "[survei belum ditutup atau sudah dievaluasi, AB-PRK-29] · langkah 4",
          [("ret", "dto_status_survei, MSG"), ("txt", "use case gagal")]),
         ("«exception» E2", "[baris RTL tidak lengkap: aspek, tindakan, PIC, tenggat, AB-PRK-29] · langkah 5",
          [("ret", "baris_rtl_kurang*, MSG"), ("txt", "kembali ke langkah 5")])],
        "<b>Catatan</b>: kriteria tertinggi dihitung <code>labfik.criteria.mixin</code> (AB-PRK-34); skor akhir ditetapkan penilai. "
        "K4 baru lengkap setelah UC-PRK-24 pada periode berikutnya."),
]

open(OUT, "w", encoding="utf-8").write('<mxfile host="app.diagrams.net">' + "".join(d.xml() for d in D) + "</mxfile>")
