import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
LH = 15


def esc(s):
    return escape(s, {'"': "&quot;"})


FILL = {"c": "fillColor=#FFFFFF;strokeColor=#333333;", "abs": "fillColor=#F5F0FF;strokeColor=#6C4A87;",
        "enum": "fillColor=#F5F5F5;strokeColor=#666666;", "stub": "fillColor=#FAFAFA;strokeColor=#999999;dashed=1;"}
TXT = ("text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
       "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;")
ASSOC = "endArrow=none;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#444444;fontSize=10;"
COMP = "endArrow=none;startArrow=diamondThin;startFill=1;startSize=16;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#333333;fontSize=10;"
GEN = "endArrow=block;endFill=0;endSize=14;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#6C4A87;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"


class Page:
    def __init__(self, n, name, title):
        self.P, self.n, self.name, self.cells = f"tk-cm{n}-", n, name, []
        self.v("title", title, TITLE, 40, 10, 1500, 34)

    def v(self, id, val, style, x, y, w, h, parent="1"):
        par = "1" if parent == "1" else self.P + parent
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="{par}">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def cls(self, id, name, attrs, x, y, w=250, kind="c", stereo=None):
        title = (f"<font style='font-size:10px'>{stereo}</font><br>" if stereo else "") + \
                (f"<b><i>{name}</i></b>" if kind == "abs" else f"<b>{name}</b>")
        start = 12 + 15 * (title.count("<br>") + 1)
        ah = max(1, len(attrs)) * LH + 8
        self.v(id, title, "swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;"
               f"startSize={start};horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;"
               f"marginBottom=0;whiteSpace=wrap;html=1;fontSize=12;{FILL[kind]}", x, y, w, start + ah)
        self.v(id + "-a", "<br>".join(attrs) if attrs else " ", TXT, 0, start, w, ah, parent=id)

    def stub(self, id, name, note, x, y, w=220):
        self.cls(id, name, [f"<i>{note}</i>"], x, y, w, "stub")

    def e(self, id, s, t, style, src=None, tgt=None, mid=None, pts=None, exit=None, entry=None):
        st = style
        if exit:
            st += f"exitX={exit[0]};exitY={exit[1]};exitDx=0;exitDy=0;"
        if entry:
            st += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        eid = f"{self.P}{id}"
        geo = '<mxGeometry relative="1" as="geometry">'
        if pts:
            geo += '<Array as="points">' + "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts) + "</Array>"
        geo += "</mxGeometry>"
        self.cells.append(f'<mxCell id="{eid}" value="{esc(mid or "")}" style="{st}labelBackgroundColor=#FFFFFF;" edge="1" '
                          f'parent="1" source="{self.P}{s}" target="{self.P}{t}">{geo}</mxCell>')
        for k, (lbl, xpos, align) in enumerate([(src, -1, "left"), (tgt, 1, "right")]):
            if lbl:
                self.cells.append(
                    f'<mxCell id="{eid}-l{k}" value="{esc(lbl)}" style="edgeLabel;resizable=0;html=1;align={align};verticalAlign=bottom;'
                    f'fontSize=10;labelBackgroundColor=#FFFFFF;" connectable="0" vertex="1" parent="{eid}"><mxGeometry x="{xpos}" '
                    f'relative="1" as="geometry"><mxPoint x="{8 if xpos < 0 else -8}" y="-2" as="offset"/></mxGeometry></mxCell>')

    def xml(self, w, h):
        return (f'<diagram id="tk-cm{self.n}" name="{esc(self.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" '
                f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" '
                'math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")


LEG = ("<b>Notasi</b> (Wazlawick 2024, Bab 8–9)<br>"
       "• Hanya konsep, atribut primitif, dan asosiasi: <b>tanpa method, tanpa detail Odoo</b>.<br>"
       "• Garis polos = asosiasi; label di ujung = <i>peran</i> dan multiplisitas. Belah ketupat hitam = komposisi (bagian–keseluruhan).<br>"
       "• Segitiga kosong ungu = generalisasi. Nama miring = konsep abstrak.<br>"
       "• <code>/nama</code> = atribut/asosiasi turunan (dihitung). «unique» = nilai tidak boleh kembar. <code>[*]</code> = banyak nilai.<br>"
       "• Kotak abu-abu putus-putus = konsep yang dirinci di halaman lain.")
SRC = "Bahan kerja (tidak masuk proposal). Sumber: expanded use case, kamus DTO SSD. Rincian: rancangan/conceptual-model-tata-kelola.md · Draf 13 Nov 2026 · Febriyan"
pages = []

# ======================================================== CM-1
p = Page(1, "CM-1 Dokumen Terkendali dan Pengesahan", "CM-1 · Conceptual model: dokumen terkendali dan riwayat pengesahan")
p.stub("ren", "Rencana", "rincian: CM-3", 300, 60, 200)
p.stub("skp", "SK Penetapan", "rincian: CM-2", 560, 60, 200)
p.stub("ver", "Versi Dokumen", "rincian: CM-2", 820, 60, 200)
p.cls("dt", "DokumenTerkendali", ["+ revisi: Natural", "+ status: StatusDokumen = draf", "+ /tanggal_berlaku: Date",
                                  "+ /jenis: JenisDokumen"], 520, 230, 280, "abs", "«abstract»")
p.cls("pcb", "Pencabutan", ["+ tanggal: Date", "+ alasan: Text"], 1000, 240, 220)
p.cls("aju", "Pengajuan", ["+ tanggal_ajukan: Date", "+ /hasil: {menunggu, ditarik,", "&nbsp;&nbsp;&nbsp;dikembalikan, disahkan}"], 520, 470, 280)
p.cls("tar", "Penarikan", ["+ tanggal: Date", "+ alasan: Text"], 80, 420, 220)
p.cls("prk", "Pemeriksaan", ["+ tanggal: Date", "+ catatan: Text"], 80, 600, 220)
p.cls("kmb", "Pengembalian", ["+ tanggal: Date", "+ alasan: Text"], 80, 790, 220)
p.cls("sah", "Pengesahan", ["+ tanggal_sah: Date", "+ tanggal_berlaku: Date"], 1000, 470, 240)
p.cls("ttd", "BerkasTTD", ["+ berkas: Berkas", "+ tanggal_ttd: Date", "+ nama_penanda_tangan: String", "+ tanggal_unggah: Date"], 520, 720, 280)
p.cls("jab", "Jabatan", ["<i>rincian: CM-2</i>"], 1000, 760, 240, "stub")
p.cls("per", "Personel", ["+ nama: String", "+ jenis: JenisPersonel", "+ aktif: Boolean = true"], 520, 1030, 280)
p.cls("e1", "StatusDokumen", ["draf", "diajukan", "diperiksa", "disahkan", "diganti", "dicabut", "kedaluwarsa"], 1320, 60, 200, "enum", "«enumeration»")
p.cls("e2", "JenisDokumen", ["sop", "ik", "formulir", "rencana_strategis", "rkt", "iku", "rencana_pengembangan", "sk_pengelola"], 1320, 260, 200, "enum", "«enumeration»")
for s in ("ren", "skp", "ver"):
    p.e(f"g-{s}", s, "dt", GEN, exit=(0.5, 1), entry=(0.5, 0))
p.e("dt-self", "dt", "dt", ASSOC, "0..1 revisi_dari", "0..1 pengganti", pts=[(480, 270), (480, 200), (560, 200)], exit=(0, 0.3), entry=(0.15, 0))
p.e("dt-aju", "dt", "aju", COMP, "1", "{ordered} * pengajuan")
p.e("dt-pcb", "dt", "pcb", COMP, "1", "0..1")
p.e("aju-tar", "aju", "tar", COMP, "1", "0..1", exit=(0, 0.3), entry=(1, 0.5))
p.e("aju-prk", "aju", "prk", COMP, "1", "0..1", exit=(0, 0.6), entry=(1, 0.5))
p.e("aju-kmb", "aju", "kmb", COMP, "1", "0..1", exit=(0, 0.9), entry=(1, 0.5))
p.e("aju-ttd", "aju", "ttd", COMP, "1", "{ordered} * berkas")
p.e("aju-sah", "aju", "sah", COMP, "1", "0..1")
p.e("sah-ttd", "sah", "ttd", ASSOC, "*", "1 berkas_sah", exit=(0.5, 1), entry=(1, 0.3))
p.e("sah-jab", "sah", "jab", ASSOC, "*", "1 jabatan_pengesah", exit=(0.8, 1), entry=(0.8, 0))
p.e("aju-per", "aju", "per", ASSOC, "*", "1 penyusun", pts=[(470, 560), (470, 1060)], exit=(0, 0.7), entry=(0, 0.2))
p.e("prk-per", "prk", "per", ASSOC, "*", "1 pemeriksa", pts=[(60, 650), (60, 1080)], exit=(0, 0.5), entry=(0, 0.5))
p.e("kmb-per1", "kmb", "per", ASSOC, "*", "1 pemutus", pts=[(190, 1100)], exit=(0.5, 1), entry=(0, 0.8))
p.e("kmb-per2", "kmb", "per", ASSOC, "*", "0..1 pencatat", pts=[(280, 1040)], exit=(0.9, 1), entry=(0, 0.1))
p.e("ttd-per", "ttd", "per", ASSOC, "*", "1 pengunggah", exit=(0.5, 1), entry=(0.5, 0))
p.e("sah-per1", "sah", "per", ASSOC, "*", "1 pengesah", pts=[(1260, 520), (1260, 1100)], exit=(1, 0.4), entry=(1, 0.7))
p.e("sah-per2", "sah", "per", ASSOC, "*", "0..1 pencatat", pts=[(1290, 550), (1290, 1130)], exit=(1, 0.8), entry=(1, 0.95))
p.e("pcb-per", "pcb", "per", ASSOC, "*", "1 pencabut", pts=[(1320, 270), (1320, 1160), (660, 1160)], exit=(1, 0.5), entry=(0.5, 1))
p.e("jab-per", "jab", "per", ASSOC, "*", "* /pemegang_aktif", pts=[(1120, 1060)], exit=(0.5, 1), entry=(1, 0.3))
p.v("n1", LEG, NOTE, 40, 1220, 640, 110)
p.v("n2", "<b>Kenapa riwayat pengesahan menjadi konsep?</b> (Wazlawick §9.3.2) Dokumen <i>mendapat</i> data baru saat statusnya berubah "
    "(tanggal sah, pengesah, berkas TTD, alasan pengembalian). Daripada atribut opsional yang membuat kelas tidak kohesif, "
    "setiap kejadian dimodelkan sebagai konsep. Satu dokumen bisa diajukan, dikembalikan, dan diajukan lagi, jadi <b>Pengajuan</b> "
    "disimpan sebagai riwayat {ordered} (pola <i>history</i>, §11.12.2).<br>"
    "<b>revisi_dari / pengganti</b> = pola <i>superseding</i> (§11.9.2): dokumen baru menggantikan yang lama tanpa menghapusnya.",
    NOTE, 700, 1220, 640, 140)
p.v("n3", "<b>Invarian</b> (dari aturan bisnis):<br>"
    "• status = disahkan ⇒ pengajuan terakhir punya Pengesahan (AB-03)<br>"
    "• Pengesahan.jabatan_pengesah punya wewenang <i>mengesahkan</i> untuk /jenis (AB-02)<br>"
    "• Pengembalian, Penarikan, Pencabutan: alasan ≠ kosong (AB-05)<br>"
    "• pencatat terisi hanya bila dicatat atas nama orang lain [KONFIRMASI]", NOTE, 1360, 1220, 330, 140)
p.v("n4", SRC, NOTE, 40, 1380, 1300, 30)
pages.append((p, 1740, 1440))

# ======================================================== CM-2
p = Page(2, "CM-2 Struktur Organisasi dan Pengendalian Dokumen", "CM-2 · Conceptual model: struktur organisasi (PKG-03) dan pengendalian dokumen (PKG-02)")
p.cls("tug", "Tugas", ["+ urutan: Natural", "+ uraian: Text"], 60, 60, 220)
p.cls("wew", "Wewenang", ["+ tindakan: {menyusun, memeriksa,", "&nbsp;&nbsp;&nbsp;mengesahkan}", "+ jenis_dokumen: JenisDokumen"], 60, 220, 250)
p.cls("jab", "Jabatan", ["+ «unique» kode: String", "+ nama: String", "+ unit: {lab_fik, prodi_if,", "&nbsp;&nbsp;&nbsp;prodi_si, fakultas}",
                         "+ eksternal: Boolean = false", "+ syarat_kompetensi: Text"], 380, 80, 280)
p.stub("dt", "DokumenTerkendali", "abstrak, rincian: CM-1", 760, 330, 220)
p.cls("skp", "SKPenetapan", ["+ «unique» nomor_sk: String", "+ judul: String", "+ menimbang: Text", "+ mengingat: Text", "+ diktum: Text",
                             "+ tembusan: Text", "+ tanggal_mulai: Date", "+ tanggal_selesai: Date"], 380, 450, 280)
p.cls("pnt", "Penetapan", ["+ tanggal_mulai: Date", "+ tanggal_selesai: Date"], 60, 560, 230)
p.cls("rpt", "Rapat", ["+ tanggal: Date", "+ agenda: Text", "+ keputusan: Text", "+ notulen: Text", "+ bukti: Berkas [*]"], 60, 800, 230)
p.cls("evs", "EvaluasiStruktur", ["+ tanggal: Date", "+ temuan_beban_kerja: Text", "+ efektivitas_koordinasi: Text", "+ keputusan: Text"], 380, 820, 280)
p.cls("rng", "RuangLab", ["+ «unique» kode: String", "+ nama: String", "+ fungsi: Text", "+ kapasitas: Natural"], 760, 600, 220)
p.cls("din", "DokumenInduk", ["+ «unique» kode: String", "+ judul: String", "+ jenis: {sop, ik, formulir, eksternal}", "+ kategori: KategoriDokumen",
                              "+ asal: {lab, fakultas, universitas}", "+ wajib: Boolean", "+ dasar_kebutuhan: Text", "+ rekaman_dihasilkan: Text",
                              "+ /memenuhi: Boolean (S1–S5)"], 1100, 60, 320)
p.cls("ver", "VersiDokumen", ["+ berkas: Berkas", "+ tanggal_dibuat: Date", "+ bagian_diubah: String", "+ ringkasan_perubahan: Text",
                              "+ alasan_revisi: AlasanRevisi", "+ periode_tinjau_bulan: Natural", "+ /tanggal_tinjau_berikutnya: Date",
                              "+ /status_kemutakhiran: {mutakhir,", "&nbsp;&nbsp;&nbsp;perlu_ditinjau, menunggu_revisi}"], 1100, 450, 320)
p.cls("dis", "Distribusi", ["+ tanggal: Date", "+ lokasi_lain: String", "+ bukti: Berkas [*]"], 1500, 450, 230)
p.cls("sos", "Sosialisasi", ["+ tanggal: Date", "+ metode: {tatap_muka, daring,", "&nbsp;&nbsp;&nbsp;papan_informasi}", "+ bukti: Berkas [*]"], 1500, 650, 240)
p.cls("tnj", "TinjauUlang", ["+ tanggal: Date", "+ hasil: {tetap_berlaku, perlu_revisi,", "&nbsp;&nbsp;&nbsp;tidak_diperlukan}", "+ catatan: Text"], 1100, 860, 300)
p.cls("per", "Personel", ["+ nama: String", "+ jenis: JenisPersonel", "+ aktif: Boolean = true"], 700, 1120, 300)
p.e("j-tug", "jab", "tug", COMP, "1", "{ordered} 1..*", exit=(0, 0.2), entry=(1, 0.5))
p.e("j-wew", "jab", "wew", COMP, "1", "*", exit=(0, 0.6), entry=(1, 0.5))
p.e("j-atas", "jab", "jab", ASSOC, "* bawahan", "0..1 atasan", pts=[(700, 120), (700, 40), (520, 40)], exit=(1, 0.2), entry=(0.5, 0))
p.e("j-pgt", "jab", "jab", ASSOC, "*", "0..1 pengganti", pts=[(730, 160), (730, 20), (430, 20)], exit=(1, 0.5), entry=(0.18, 0))
p.e("j-koor", "jab", "jab", ASSOC, "*", "* koordinasi", pts=[(690, 230), (690, 300), (600, 300)], exit=(1, 0.85), entry=(0.8, 1))
p.e("j-din", "jab", "din", ASSOC, "*", "0..1 dasar", pts=[(1050, 100)], exit=(1, 0.1), entry=(0, 0.2))
p.e("g-skp", "skp", "dt", GEN, exit=(1, 0.2), entry=(0, 0.5))
p.e("g-ver", "ver", "dt", GEN, exit=(0, 0.2), entry=(1, 0.5))
p.e("s-pnt", "skp", "pnt", COMP, "1", "1..*", exit=(0, 0.5), entry=(1, 0.3))
p.e("pnt-jab", "pnt", "jab", ASSOC, "*", "1", pts=[(175, 420), (450, 420)], exit=(0.5, 0), entry=(0.25, 1))
p.e("pnt-per", "pnt", "per", ASSOC, "*", "1", pts=[(330, 700), (330, 1170)], exit=(1, 0.8), entry=(0, 0.5))
p.e("pnt-rng", "pnt", "rng", ASSOC, "*", "*", pts=[(175, 760), (720, 760), (720, 650)], exit=(0.5, 1), entry=(0, 0.3))
p.e("s-din", "skp", "din", ASSOC, "*", "* dasar_hukum", pts=[(1060, 470), (1060, 160)], exit=(1, 0.1), entry=(0, 0.45))
p.e("r-skp", "rpt", "skp", ASSOC, "*", "1", pts=[(320, 840), (320, 640)], exit=(1, 0.2), entry=(0, 0.85))
p.e("r-per", "rpt", "per", ASSOC, "*", "1..* peserta", pts=[(175, 1200)], exit=(0.5, 1), entry=(0, 0.85))
p.e("e-skp", "evs", "skp", ASSOC, "*", "1 dievaluasi", exit=(0.3, 0), entry=(0.3, 1))
p.e("e-skb", "evs", "skp", ASSOC, "0..1", "0..1 sk_baru", exit=(0.7, 0), entry=(0.7, 1))
p.e("e-jab", "evs", "jab", ASSOC, "*", "* jabatan_direvisi", pts=[(700, 860), (700, 330), (620, 330)], exit=(1, 0.2), entry=(0.85, 1))
p.e("jab-per", "jab", "per", ASSOC, "*", "* /pemegang_aktif", pts=[(740, 220), (740, 1060), (850, 1060)], exit=(1, 0.65), entry=(0.5, 0))
p.e("d-ver", "din", "ver", COMP, "1", "{ordered} 1..* versi")
p.e("d-verb", "din", "ver", ASSOC, "", "0..1 /versi_berlaku", pts=[(1440, 300), (1440, 520)], exit=(1, 0.8), entry=(1, 0.15))
p.e("d-rng", "din", "rng", ASSOC, "*", "* lokasi_penggunaan", pts=[(1080, 380), (870, 380)], exit=(0, 0.9), entry=(0.5, 0))
p.e("d-self", "din", "din", ASSOC, "*", "* terkait", pts=[(1460, 100), (1460, 20), (1260, 20)], exit=(1, 0.15), entry=(0.5, 0))
p.e("v-dis", "ver", "dis", ASSOC, "1", "*", exit=(1, 0.25), entry=(0, 0.5))
p.e("v-sos", "ver", "sos", ASSOC, "1", "*", exit=(1, 0.75), entry=(0, 0.5))
p.e("v-tnj", "ver", "tnj", ASSOC, "1", "{ordered} *")
p.e("dis-rng", "dis", "rng", ASSOC, "*", "0..1", pts=[(1615, 420), (1060, 420), (1060, 640)], exit=(0.5, 0), entry=(1, 0.3))
p.e("dis-per", "dis", "per", ASSOC, "*", "1 petugas", pts=[(1760, 500), (1760, 1150)], exit=(1, 0.5), entry=(1, 0.2))
p.e("sos-per", "sos", "per", ASSOC, "*", "1..* peserta", pts=[(1780, 700), (1780, 1190)], exit=(1, 0.5), entry=(1, 0.6))
p.e("tnj-per", "tnj", "per", ASSOC, "*", "1 peninjau", pts=[(1250, 1170)], exit=(0.5, 1), entry=(1, 0.9))
p.v("n1", LEG, NOTE, 40, 1260, 640, 110)
p.v("n2", "<b>Pola analisis</b> (Wazlawick Bab 11)<br>"
    "• <i>Organizational hierarchy</i> (§11.8): Jabatan–atasan; ditambah pengganti dan koordinasi.<br>"
    "• <i>Effectivity</i> (§11.12.1): Penetapan dan SKPenetapan berperiode; <code>/pemegang_aktif</code> = personel pada Penetapan "
    "dari SK berstatus disahkan yang periodenya mencakup hari ini (asosiasi turunan dengan filter, §8.4.4).<br>"
    "• <i>History</i> (§11.12.2): versi {ordered}, tinjau ulang {ordered}.<br>"
    "• <code>/versi_berlaku</code> = versi dengan status disahkan (AB-04: paling banyak satu).", NOTE, 700, 1260, 600, 130)
p.v("n3", "<b>Enumerasi lain</b>: JenisPersonel {dosen, laboran_plp, teknisi, asisten, petugas_k3, eksternal}; "
    "KategoriDokumen {tata_tertib, praktikum, operasi, k3, alat, peminjaman, kedaruratan, limbah}; "
    "AlasanRevisi {tinjauan_berkala, perubahan_alat, perubahan_metode, perubahan_fasilitas, perubahan_risiko, perubahan_lingkup}.<br>"
    "<b>[KONFIRMASI]</b> konsep Personel bersama kelompok.", NOTE, 1320, 1260, 440, 130)
p.v("n4", SRC, NOTE, 40, 1410, 1300, 30)
pages.append((p, 1820, 1470))

# ======================================================== CM-3
p = Page(3, "CM-3 Perencanaan", "CM-3 · Conceptual model: perencanaan (PKG-01, PKG-13)")
p.cls("sas", "SasaranStrategis", ["+ kode: String", "+ sasaran: Text", "+ target_akhir: String"], 80, 60, 240)
p.cls("prg", "Program", ["+ kode: String", "+ nama: String", "+ kegiatan_utama: Text", "+ luaran: Text", "+ tahapan: Text"], 80, 240, 240)
p.cls("bas", "Baseline", ["+ data: String", "+ nilai_awal: String", "+ sumber: String"], 80, 470, 240)
p.cls("gap", "TemuanGap", ["+ aspek: {tridharma, kompetensi,", "&nbsp;&nbsp;&nbsp;sarana, layanan}", "+ kondisi_saat_ini: Text", "+ kebutuhan: Text",
                           "+ sumber_data: String", "+ uraian_gap: Text", "+ lampiran: Berkas [*]"], 80, 660, 260)
p.stub("dt", "DokumenTerkendali", "abstrak, rincian: CM-1", 520, 60, 220)
p.cls("ren", "Rencana", ["+ nama: String", "+ jenis: {strategis, tahunan,", "&nbsp;&nbsp;&nbsp;iku, pengembangan}", "+ ringkasan, latar_belakang, tujuan,",
                         "&nbsp;&nbsp;&nbsp;ruang_lingkup, referensi, landasan,", "&nbsp;&nbsp;&nbsp;visi, misi, penutup: Text",
                         "+ /kriteria_tertinggi: Natural (0–4)"], 480, 260, 320)
p.cls("prd", "Periode", ["+ nama: String", "+ jenis: {tahun_anggaran, semester,", "&nbsp;&nbsp;&nbsp;multi_tahun}", "+ tanggal_mulai: Date",
                         "+ tanggal_selesai: Date"], 920, 60, 260)
p.cls("tin", "TinjauanRencana", ["+ tanggal: Date", "+ ringkasan: Text", "+ keputusan: Text"], 920, 300, 260)
p.cls("man", "UkuranManfaat", ["+ indikator_manfaat: String", "+ nilai_sebelum: Decimal", "+ nilai_sesudah: Decimal", "+ sumber: String"], 1280, 300, 250)
p.cls("itm", "ItemRencana", ["+ kegiatan: Text", "+ baseline: Decimal", "+ target: Decimal", "+ satuan: String", "+ jadwal_mulai: Date",
                             "+ jadwal_selesai: Date", "+ bukti_diharapkan: Text", "+ anggaran: Money", "+ komponen_anggaran: KomponenAnggaran",
                             "+ nilai_risiko: Natural (1–3)", "+ nilai_manfaat: Natural (1–3)", "+ /prioritas: {tinggi, sedang, rendah}"], 480, 640, 340)
p.cls("kpi", "KPI", ["+ «unique» kode: String", "+ nama: String", "+ sasaran_kerja: String", "+ rumus: Text", "+ pembilang: String",
                     "+ penyebut: String", "+ satuan: String", "+ frekuensi: Frekuensi", "+ sumber_bukti: Text", "+ acuan_iso: String"], 960, 640, 260)
p.cls("sre", "SasaranRenstra", ["+ «unique» kode: String", "+ uraian: Text", "+ tingkat: {upnvj, upps, prodi}"], 1300, 640, 240)
p.stub("jab", "Jabatan", "rincian: CM-2", 1300, 900, 200)
p.cls("rea", "Realisasi", ["+ periode_lapor: String", "+ capaian: Decimal", "+ anggaran_terpakai: Money", "+ status_capaian: StatusCapaian",
                           "+ alasan_tidak_relevan: Text", "+ analisis_tindakan: Text", "+ tenggat: Date", "+ bukti: Berkas [1..*]",
                           "+ /persen_capaian: Decimal"], 480, 1060, 320)
p.cls("per", "Personel", ["+ nama: String", "+ jenis: JenisPersonel", "+ aktif: Boolean = true"], 960, 1100, 280)
p.cls("e1", "StatusCapaian", ["tercapai", "perlu_perhatian", "tidak_tercapai", "belum_tersedia", "tidak_relevan"], 1300, 1060, 200, "enum", "«enumeration»")
p.e("g-ren", "ren", "dt", GEN, exit=(0.5, 0), entry=(0.5, 1))
p.e("r-sas", "ren", "sas", COMP, "1", "*", exit=(0, 0.1), entry=(1, 0.5))
p.e("r-prg", "ren", "prg", COMP, "1", "*", exit=(0, 0.35), entry=(1, 0.5))
p.e("r-bas", "ren", "bas", COMP, "1", "*", exit=(0, 0.65), entry=(1, 0.4))
p.e("r-gap", "ren", "gap", COMP, "1", "*", exit=(0, 0.95), entry=(1, 0.2))
p.e("r-itm", "ren", "itm", COMP, "1", "*")
p.e("r-prd", "ren", "prd", ASSOC, "*", "1", exit=(1, 0.1), entry=(0, 0.5))
p.e("r-self", "ren", "ren", ASSOC, "0..1 induk", "* turunan", pts=[(460, 300), (460, 230), (560, 230)], exit=(0, 0.15), entry=(0.25, 0))
p.e("r-tin", "ren", "tin", ASSOC, "1", "*", exit=(1, 0.5), entry=(0, 0.5))
p.e("t-ren", "tin", "ren", ASSOC, "*", "0..1 rencana_berikut", pts=[(1050, 520), (760, 520)], exit=(0.5, 1), entry=(0.875, 1))
p.e("t-man", "tin", "man", COMP, "1", "*", exit=(1, 0.5), entry=(0, 0.5))
p.e("m-itm", "man", "itm", ASSOC, "*", "1", pts=[(1405, 560), (870, 560), (870, 680)], exit=(0.5, 1), entry=(1, 0.1))
p.e("t-per", "tin", "per", ASSOC, "*", "1..* peserta", pts=[(1240, 340), (1240, 600), (1260, 600), (1260, 1130)], exit=(1, 0.2), entry=(1, 0.2))
p.e("s-kpi", "sas", "kpi", ASSOC, "*", "0..1", pts=[(360, 80), (360, 30), (1090, 30), (1090, 620), (1090, 640)], exit=(1, 0.2), entry=(0.5, 0))
p.e("b-per", "bas", "per", ASSOC, "*", "1 pic", pts=[(40, 510), (40, 1200)], exit=(0, 0.5), entry=(0, 0.8))
p.e("i-kpi", "itm", "kpi", ASSOC, "*", "0..1", exit=(1, 0.15), entry=(0, 0.15))
p.e("i-sre", "itm", "sre", ASSOC, "*", "* sasaran_renstra", pts=[(900, 760), (900, 940), (1420, 940)], exit=(1, 0.4), entry=(0.5, 1))
p.e("i-gap", "itm", "gap", ASSOC, "*", "* menjawab", exit=(0, 0.3), entry=(1, 0.75))
p.e("i-sas", "itm", "sas", ASSOC, "*", "0..1", pts=[(440, 680), (440, 120)], exit=(0, 0.1), entry=(1, 0.85))
p.e("i-prg", "itm", "prg", ASSOC, "*", "0..1", pts=[(420, 700), (420, 320)], exit=(0, 0.2), entry=(1, 0.8))
p.e("i-per", "itm", "per", ASSOC, "*", "1 pic", pts=[(880, 900), (880, 1130)], exit=(1, 0.7), entry=(0, 0.2))
p.e("i-rea", "itm", "rea", ASSOC, "1", "*")
p.e("rea-per1", "rea", "per", ASSOC, "*", "1 pelapor", exit=(1, 0.3), entry=(0, 0.6))
p.e("rea-per2", "rea", "per", ASSOC, "*", "0..1 pic_tindak_lanjut", pts=[(640, 1290), (1100, 1290)], exit=(0.5, 1), entry=(0.5, 1))
p.e("k-jab", "kpi", "jab", ASSOC, "*", "1 jabatan_pic", pts=[(1250, 860), (1250, 930)], exit=(1, 0.9), entry=(0, 0.4))
p.v("n1", LEG, NOTE, 40, 1330, 640, 110)
p.v("n2", "<b>Pola analisis</b> (Wazlawick Bab 11)<br>"
    "• <i>Specification class</i> (§11.3): KPI adalah definisi indikator; ItemRencana memberi target per periode.<br>"
    "• Satu konsep Rencana untuk semua jenis (dibedakan atribut <code>jenis</code>, transisi stabil §9.3.1). "
    "Atribut khusus pengembangan (<code>nilai_risiko</code>, <code>nilai_manfaat</code>, TemuanGap, UkuranManfaat) hanya terisi untuk jenis pengembangan.<br>"
    "• <code>/prioritas</code> = turunan dari nilai_risiko × nilai_manfaat [USULAN PENULIS].<br>"
    "• <code>/kriteria_tertinggi</code> = K1–K4 berurutan (PKG-01/13).", NOTE, 700, 1330, 620, 130)
p.v("n3", "<b>Enumerasi lain</b>: KomponenAnggaran {pemeliharaan, k3, perangkat_lunak, infrastruktur, pelatihan, riset_pkm, audit_mutu}; "
    "Frekuensi {bulanan, triwulanan, semesteran, tahunan}.<br>"
    "<b>Invarian</b>: status_capaian = tidak_relevan ⇒ alasan ≠ kosong (AB-10); bukti minimal 1 (AB-12).", NOTE, 1340, 1330, 400, 120)
p.v("n4", SRC, NOTE, 40, 1480, 1300, 30)
pages.append((p, 1800, 1540))

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
