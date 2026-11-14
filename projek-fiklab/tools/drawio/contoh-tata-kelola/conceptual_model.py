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
       "• Segitiga kosong ungu = generalisasi. Nama miring = konsep abstrak. <code>{DokumenDisahkan}</code> di atas nama = turunan konsep itu (CM-1).<br>"
       "• <code>/nama</code> = atribut atau asosiasi turunan (dihitung). «unique» = nilai tidak boleh kembar. <code>[0..1]</code> = boleh kosong.<br>"
       "• Kotak abu-abu putus-putus = konsep yang dirinci di halaman lain.")
SRC = ("Bahan kerja (tidak masuk proposal). Sumber: kamus DTO (ssd-tata-kelola.md), AB-01–25. "
       "Rincian: conceptual-model-tata-kelola.md · Draf 14 Nov 2026 · Febriyan")
DD = "{DokumenDisahkan}"
RB = "{RekamanBukti}"
pages = []

# ======================================================== CM-1
p = Page(1, "CM TO-BE (1-4) - Pengesahan dan Rekaman Bukti", "CM-1 · Dokumen yang disahkan, riwayat pengesahan, dan rekaman bukti")
p.stub("ren", "Renstra", "rincian: CM-4", 40, 60, 180)
p.stub("rcn", "Rencana", "rincian: CM-4", 250, 60, 180)
p.stub("skp", "SK Penetapan", "rincian: CM-2", 460, 60, 180)
p.stub("ver", "Versi Dokumen", "rincian: CM-3", 670, 60, 180)
p.cls("dd", "DokumenDisahkan", ["+ status: StatusDokumen = draf", "+ /jenis_dokumen: JenisDokumen",
                                "+ /tanggal_ajukan: Date = waktu kejadian diajukan terakhir",
                                "+ /tanggal_sah: Date = pengesahan.tanggal_sah",
                                "+ /berkas_ttd: Berkas = berkas kejadian unggah terakhir"], 250, 200, 380, "abs", "«abstract»")
for s in ["ren", "rcn", "skp", "ver"]:
    p.e(f"g-{s}", s, "dd", GEN, exit=(0.5, 1), entry=(0.5, 0))
p.e("rev", "dd", "dd", ASSOC, src="pengganti 0..1", tgt="digantikan 0..1", mid="revisi_dari",
    pts=[(690, 250), (690, 170), (560, 170)], exit=(1, 0.4), entry=(0.82, 0))
p.cls("pgs", "Pengesahan", ["+ tanggal_sah: Date"], 250, 420, 220)
p.e("dd-pgs", "dd", "pgs", ASSOC, src="1", tgt="pengesahan 0..1", exit=(0.25, 1), entry=(0.5, 0))
p.cls("kej", "KejadianPengesahan", ["+ jenis: JenisKejadian", "+ waktu: DateTime", "+ alasan: Text [0..1]",
                                    "+ berkas: Berkas [0..1]"], 560, 420, 260)
p.e("dd-kej", "dd", "kej", COMP, src="1", tgt="riwayat * {urut waktu}", exit=(0.8, 1), entry=(0.5, 0))
p.stub("per", "Personel", "rincian: CM-2", 40, 420, 160)
p.e("pgs-per1", "pgs", "per", ASSOC, src="*", tgt="pengesah 1", exit=(0, 0.35), entry=(1, 0.35))
p.e("pgs-per2", "pgs", "per", ASSOC, src="*", tgt="pencatat 1", exit=(0, 0.8), entry=(1, 0.8))
p.e("kej-per", "kej", "per", ASSOC, src="*", tgt="pelaku 0..1", pts=[(690, 560), (120, 560)], exit=(0.5, 1), entry=(0.5, 1))
p.e("dd-per", "dd", "per", ASSOC, src="*", tgt="/pengesah_berwenang *", pts=[(90, 240)], exit=(0, 0.3), entry=(0.3, 0))
p.e("dd-pny", "dd", "per", ASSOC, src="*", tgt="penyusun 1", pts=[(150, 290)], exit=(0, 0.8), entry=(0.7, 0))
# rekaman bukti
p.cls("rb", "RekamanBukti", ["+ tanggal: Date", "+ bukti: Berkas [0..1]", "+ keterangan: Text [0..1]"], 1100, 200, 260, "abs", "«abstract»")
p.stub("per2", "Personel", "rincian: CM-2", 1440, 210, 160)
p.e("rb-per", "rb", "per2", ASSOC, src="*", tgt="pelapor 1", exit=(1, 0.5), entry=(0, 0.5))
subs = [("rpt", "Rapat Koordinasi", "CM-2", 960, 380), ("evs", "Evaluasi Struktur", "CM-2", 1140, 380),
        ("dst", "Distribusi", "CM-3", 1320, 380), ("sos", "Sosialisasi", "CM-3", 1500, 380),
        ("tju", "Tinjau Ulang", "CM-3", 1050, 470), ("rls", "Realisasi", "CM-4", 1230, 470),
        ("tjr", "Tinjauan Rencana", "CM-4", 1410, 470)]
for sid, name, pg, x, y in subs:
    p.stub(sid, name, f"rincian: {pg}", x, y, 160)
    p.e(f"g-{sid}", sid, "rb", GEN, exit=(0.5, 0), entry=(0.5, 1))
p.cls("e1", "StatusDokumen", ["draf", "diajukan", "disahkan", "diganti", "dicabut", "kedaluwarsa"], 40, 620, 180, "enum", "«enumeration»")
p.cls("e2", "JenisKejadian", ["diajukan", "dikembalikan", "berkas_diunggah", "disahkan", "diganti", "dicabut", "kedaluwarsa"], 250, 620, 180, "enum", "«enumeration»")
p.cls("e3", "JenisDokumen", ["sop_ik", "renstra", "rencana_tahunan", "rencana_pengembangan", "sk_penetapan"], 460, 620, 200, "enum", "«enumeration»")
p.v("n0", LEG, NOTE, 700, 620, 560, 120)
p.v("n1", "<b>Kunci</b><br>• Data yang muncul saat status berubah (pengesah, tanggal sah, alasan, berkas) disimpan sebagai "
    "<b>konsep kejadian</b> (Pengesahan, KejadianPengesahan), bukan atribut opsional (§9.3.2).<br>"
    "• <i>revisi_dari</i> = pola <i>superseding</i> (§11.9.2): dokumen lama tetap tersimpan sebagai Diganti.<br>"
    "• <i>/pengesah_berwenang</i> = Personel yang jabatannya punya Wewenang (mengesahkan, jenis_dokumen) (AB-05).<br>"
    "• RekamanBukti: tidak dihapus, hanya dikoreksi (AB-22).", NOTE, 1290, 620, 420, 150)
p.v("n2", SRC, NOTE, 700, 760, 560, 46)
pages.append((p, 1760, 840))

# ======================================================== CM-2
p = Page(2, "CM TO-BE (2-4) - Struktur Organisasi", "CM-2 · Struktur organisasi (PKG-03)")
p.cls("per", "Personel", ["+ nama: String", "+ jenis: JenisPersonel", "+ unit: Unit"], 40, 90, 240)
p.cls("jab", "Jabatan", ["+ nama: String", "+ unit: Unit", "+ is_eksternal: Boolean", "+ syarat_kompetensi: Text [0..1]",
                         "+ /lengkap: Boolean (tugas, wewenang, atasan, pengganti ada)"], 420, 90, 330)
p.e("per-jab", "per", "jab", ASSOC, src="pemegang *", tgt="jabatan 0..1", exit=(1, 0.4), entry=(0, 0.4))
p.e("jab-atas", "jab", "jab", ASSOC, src="bawahan *", tgt="atasan 0..1", pts=[(470, 60), (700, 60)], exit=(0.15, 0), entry=(0.85, 0))
p.e("jab-ganti", "jab", "jab", ASSOC, src="*", tgt="pengganti 0..1", pts=[(780, 140), (780, 250), (585, 250)], exit=(1, 0.3), entry=(0.5, 1))
p.cls("tgs", "Tugas", ["+ urutan: Natural", "+ uraian: Text"], 880, 60, 220)
p.cls("wwn", "Wewenang", ["+ tindakan: Tindakan", "+ jenis_dokumen: JenisDokumen"], 880, 190, 240)
p.e("jab-tgs", "jab", "tgs", COMP, src="1", tgt="tugas * {urut}", exit=(1, 0.15), entry=(0, 0.5))
p.e("jab-wwn", "jab", "wwn", COMP, src="1", tgt="wewenang *", pts=[(820, 175), (820, 225)], exit=(1, 0.6), entry=(0, 0.5))
p.cls("sk", "SK Penetapan", ["+ nomor_sk: String «unique»", "+ judul: String", "+ menimbang: Text", "+ mengingat: Text",
                             "+ /kriteria_tertinggi: 0..4 (AB-25)"], 420, 330, 330, "c", DD)
p.stub("prd", "Periode", "master Core", 880, 350, 180)
p.e("sk-prd", "sk", "prd", ASSOC, src="*", tgt="berlaku_pada 1", exit=(1, 0.4), entry=(0, 0.5))
p.cls("bp", "BarisPenetapan", ["+ tanggal_mulai: Date", "+ tanggal_selesai: Date"], 40, 330, 240)
p.e("sk-bp", "sk", "bp", COMP, src="1", tgt="baris 1..*", exit=(0, 0.5), entry=(1, 0.5))
p.e("bp-per", "bp", "per", ASSOC, src="*", tgt="personel 1", exit=(0.3, 0), entry=(0.3, 1))
p.e("bp-jab", "bp", "jab", ASSOC, src="*", tgt="jabatan 1", pts=[(250, 290), (500, 290)], exit=(0.8, 0), entry=(0.25, 1))
p.stub("rng", "Ruang", "master Core", 40, 500, 180)
p.e("bp-rng", "bp", "rng", ASSOC, src="*", tgt="ditugaskan_di *", exit=(0.4, 1), entry=(0.5, 0))
p.cls("rpt", "Rapat Koordinasi", ["+ agenda: Text", "+ keputusan: Text", "+ notulen: Berkas"], 300, 560, 260, "c", RB)
p.e("rpt-per", "rpt", "per", ASSOC, src="*", tgt="peserta *", pts=[(290, 620), (290, 470), (20, 470), (20, 130)], exit=(0, 0.6), entry=(0, 0.5))
p.cls("evs", "Evaluasi Struktur", ["+ temuan_beban_kerja: Text", "+ efektivitas_koordinasi: Text", "+ keputusan: Text",
                                   "+ struktur_diubah: Boolean"], 640, 560, 300, "c", RB)
p.e("evs-sk", "evs", "sk", ASSOC, src="*", tgt="dievaluasi 1", exit=(0.2, 0), entry=(0.75, 1))
p.e("evs-sk2", "evs", "sk", ASSOC, src="0..1", tgt="sk_revisi 0..1", pts=[(1000, 610), (1000, 450)], exit=(1, 0.3), entry=(1, 0.8))
p.e("evs-jab", "evs", "jab", ASSOC, src="*", tgt="jabatan_direvisi *", pts=[(1060, 680), (1060, 290), (700, 290)], exit=(1, 0.8), entry=(0.85, 1))
p.cls("e1", "JenisPersonel", ["dosen", "laboran_plp", "teknisi", "asisten", "petugas_k3"], 40, 760, 180, "enum", "«enumeration»")
p.cls("e2", "Unit", ["lab_fik", "prodi_informatika", "prodi_sistem_informasi", "fakultas"], 250, 760, 200, "enum", "«enumeration»")
p.cls("e3", "Tindakan", ["menyusun", "mengesahkan"], 480, 760, 160, "enum", "«enumeration»")
p.v("n0", LEG, NOTE, 680, 760, 560, 120)
p.v("n1", "<b>Kunci</b><br>• Jabatan memakai pola <i>organizational hierarchy</i> (§11.8): atasan sebagai asosiasi refleksif, bukan kelas per tingkat.<br>"
    "• Tugas dan Wewenang adalah <b>bagian</b> dari Jabatan (komposisi, <i>has-a</i>), bukan turunannya (keputusan 14 Nov 2026).<br>"
    "• Jabatan seseorang (asosiasi Personel–Jabatan) dipakai untuk cek wewenang pengesah (AB-05); "
    "BarisPenetapan mencatat penugasan resmi di SK.<br>• Pihak eksternal tidak dicatat sebagai Personel.", NOTE, 1260, 760, 440, 150)
p.v("n2", SRC, NOTE, 680, 900, 560, 46)
pages.append((p, 1760, 980))

# ======================================================== CM-3
p = Page(3, "CM TO-BE (3-4) - Pengendalian Dokumen", "CM-3 · Pengendalian dokumen SOP/IK (PKG-02)")
p.cls("di", "DokumenInduk", ["+ kode: String «unique»", "+ judul: String", "+ jenis: JenisDokumenInduk", "+ kategori: KategoriSOP",
                             "+ asal: AsalDokumen", "+ is_wajib: Boolean", "+ dasar_kebutuhan: Text [0..1]",
                             "+ tanggal_ditetapkan_wajib: Date [0..1]", "+ siklus_tinjau_bulan: Natural",
                             "+ /memenuhi: Boolean = S1 ∧ S2 ∧ S3 ∧ S4 ∧ S5 (AB-24)"], 40, 80, 360)
p.cls("ver", "Versi Dokumen", ["+ revisi: String", "+ berkas: Berkas", "+ tanggal_efektif: Date", "+ bagian_diubah: Text [0..1]",
                               "+ ringkasan_perubahan: Text [0..1]", "+ alasan_revisi: Text [0..1]",
                               "+ /tanggal_tinjau_berikutnya: Date (AB-14)", "+ /perlu_ditinjau: Boolean"], 560, 80, 340, "c", DD)
p.e("di-ver", "di", "ver", COMP, src="1", tgt="versi * {revisi «unique» per induk}", exit=(1, 0.25), entry=(0, 0.3))
p.e("di-verb", "di", "ver", ASSOC, src="0..1", tgt="/versi_berlaku 0..1", exit=(1, 0.6), entry=(0, 0.75))
p.stub("rng", "Ruang", "master Core", 40, 420, 180)
p.e("di-rng", "di", "rng", ASSOC, src="*", tgt="lokasi_penggunaan *", exit=(0.25, 1), entry=(0.5, 0))
p.cls("dst", "Distribusi", ["(atribut dari RekamanBukti)"], 300, 440, 220, "c", RB)
p.e("dst-ver", "dst", "ver", ASSOC, src="*", tgt="versi 1", pts=[(410, 380), (640, 380)], exit=(0.5, 0), entry=(0.25, 1))
p.e("dst-rng", "dst", "rng", ASSOC, src="*", tgt="lokasi 1", exit=(0, 0.6), entry=(1, 0.6))
p.cls("sos", "Sosialisasi", ["+ metode: MetodeSosialisasi", "+ jumlah_peserta: Natural"], 580, 440, 240, "c", RB)
p.e("sos-ver", "sos", "ver", ASSOC, src="*", tgt="versi 1", exit=(0.5, 0), entry=(0.55, 1))
p.stub("per", "Personel", "rincian: CM-2", 900, 460, 160)
p.e("sos-per", "sos", "per", ASSOC, src="*", tgt="peserta *", exit=(1, 0.5), entry=(0, 0.5))
p.cls("tju", "Tinjau Ulang", ["+ hasil: HasilTinjau", "+ catatan: Text"], 960, 220, 240, "c", RB)
p.e("tju-ver", "tju", "ver", ASSOC, src="*", tgt="versi 1", exit=(0, 0.5), entry=(1, 0.6))
p.cls("e1", "JenisDokumenInduk", ["sop", "ik", "formulir", "eksternal"], 40, 620, 180, "enum", "«enumeration»")
p.cls("e2", "KategoriSOP", ["tata_tertib", "praktikum", "operasional", "k3", "alat", "peminjaman", "kedaruratan", "limbah"], 240, 620, 170, "enum", "«enumeration»")
p.cls("e3", "AsalDokumen", ["lab", "fakultas", "universitas"], 430, 620, 160, "enum", "«enumeration»")
p.cls("e4", "MetodeSosialisasi", ["tatap_muka", "daring", "pengumuman"], 610, 620, 170, "enum", "«enumeration»")
p.cls("e5", "HasilTinjau", ["tetap_berlaku", "perlu_revisi"], 800, 620, 160, "enum", "«enumeration»")
p.v("n0", LEG, NOTE, 1000, 620, 560, 120)
p.v("n1", "<b>Kunci</b><br>• Kemutakhiran (S2) dihitung: <i>/tanggal_tinjau_berikutnya</i> dan <i>/perlu_ditinjau</i>, bukan status tersimpan (§9.3.1).<br>"
    "• Lokasi penggunaan = Ruang dari Core (keputusan 14 Nov 2026). S4 lolos bila setiap lokasi punya Distribusi untuk versi berlaku.<br>"
    "• Peserta sosialisasi: Personel yang tercatat + <i>jumlah_peserta</i>, karena mahasiswa bukan Personel <b>[ASUMSI]</b>.", NOTE, 1000, 760, 560, 110)
p.v("n2", SRC, NOTE, 1000, 890, 560, 46)
pages.append((p, 1620, 960))

# ======================================================== CM-4
p = Page(4, "CM TO-BE (4-4) - Rencana", "CM-4 · Renstra, rencana tahunan, dan rencana pengembangan (PKG-01, PKG-13)")
p.cls("rst", "Renstra", ["+ judul: String", "+ berkas: Berkas"], 40, 80, 220, "c", DD)
p.cls("rcn", "Rencana", ["+ jenis: JenisRencana", "+ judul: String", "+ narasi: Text [0..1]",
                         "+ /kriteria_tertinggi: 0..4 (AB-25)"], 360, 80, 300, "c", DD)
p.stub("prd", "Periode", "master Core", 40, 240, 180)
p.e("rst-prd", "rst", "prd", ASSOC, src="*", tgt="berlaku_pada 1", exit=(0.5, 1), entry=(0.5, 0))
p.e("rcn-prd", "rcn", "prd", ASSOC, src="*", tgt="berlaku_pada 1", pts=[(400, 265)], exit=(0.13, 1), entry=(1, 0.5))
p.cls("gap", "TemuanGap", ["+ aspek: AspekGap", "+ kondisi_saat_ini: Text", "+ kebutuhan: Text", "+ sumber_data: Text",
                           "+ uraian_gap: Text", "+ lampiran: Berkas [0..1]", "+ tidak_ada_gap: Boolean",
                           "+ alasan_tidak_ada_gap: Text [0..1]"], 780, 60, 290)
p.e("rcn-gap", "rcn", "gap", COMP, src="1", tgt="temuan_gap *", exit=(1, 0.3), entry=(0, 0.3))
p.cls("itm", "ItemRencana", ["+ kegiatan: Text", "+ target: Real", "+ satuan: String", "+ jadwal_mulai: Date",
                             "+ jadwal_selesai: Date", "+ anggaran: Money", "+ rujukan_renstra: Text",
                             "+ nilai_risiko: 1..3 [0..1] (pengembangan)", "+ nilai_manfaat: 1..3 [0..1] (pengembangan)",
                             "+ /prioritas: Prioritas (AB-21)"], 360, 320, 330)
p.e("rcn-itm", "rcn", "itm", COMP, src="1", tgt="item 1..*", exit=(0.5, 1), entry=(0.5, 0))
p.e("itm-gap", "itm", "gap", ASSOC, src="*", tgt="menjawab *", pts=[(925, 360)], exit=(1, 0.2), entry=(0.5, 1))
p.cls("kpi", "KPI", ["+ kode: String «unique»", "+ nama: String", "+ definisi: Text", "+ rumus_pembilang: Text",
                     "+ rumus_penyebut: Text", "+ satuan: String", "+ frekuensi: Frekuensi", "+ sumber_data: Text"], 40, 340, 240)
p.e("itm-kpi", "itm", "kpi", ASSOC, src="*", tgt="kpi 0..1", exit=(0, 0.3), entry=(1, 0.3))
p.stub("per", "Personel", "rincian: CM-2", 800, 420, 160)
p.e("itm-per", "itm", "per", ASSOC, src="*", tgt="pic 1", exit=(1, 0.55), entry=(0, 0.5))
p.cls("rls", "Realisasi", ["+ periode_lapor: String", "+ capaian: Real", "+ biaya_terpakai: Money",
                           "+ status_capaian: StatusCapaian", "+ tindak_lanjut: Text"], 360, 600, 300, "c", RB)
p.e("rls-itm", "rls", "itm", ASSOC, src="* {(item, periode_lapor) «unique»}", tgt="item 1", exit=(0.5, 0), entry=(0.5, 1))
p.cls("tjr", "Tinjauan Rencana", ["+ ringkasan_capaian: Text", "+ keputusan: Text"], 760, 600, 280, "c", RB)
p.e("tjr-rcn", "tjr", "rcn", ASSOC, src="*", tgt="ditinjau 1", pts=[(1100, 640), (1100, 30), (510, 30)], exit=(1, 0.3), entry=(0.5, 0))
p.e("tjr-rcn2", "tjr", "rcn", ASSOC, src="0..1", tgt="rencana_berikut 0..1", pts=[(1130, 680), (1130, 15), (620, 15)], exit=(1, 0.7), entry=(0.87, 0))
p.e("tjr-per", "tjr", "per", ASSOC, src="*", tgt="peserta *", exit=(0.4, 0), entry=(0.5, 1))
p.cls("um", "UkuranManfaat", ["+ indikator: Text", "+ nilai_sebelum: Real", "+ nilai_sesudah: Real", "+ sumber: Text"], 1180, 600, 240)
p.e("tjr-um", "tjr", "um", COMP, src="1", tgt="ukuran_manfaat *", exit=(1, 0.5), entry=(0, 0.3))
p.e("um-itm", "um", "itm", ASSOC, src="*", tgt="item 1", pts=[(1300, 560), (720, 560), (720, 480)], exit=(0.5, 0), entry=(1, 0.85))
p.cls("e1", "JenisRencana", ["tahunan", "pengembangan"], 40, 820, 160, "enum", "«enumeration»")
p.cls("e2", "AspekGap", ["tridharma", "kompetensi", "sarana", "layanan"], 220, 820, 160, "enum", "«enumeration»")
p.cls("e3", "StatusCapaian", ["tercapai", "perlu_perhatian", "tidak_tercapai", "belum_tersedia"], 400, 820, 180, "enum", "«enumeration»")
p.cls("e4", "Frekuensi", ["bulanan", "triwulan", "semester", "tahunan"], 600, 820, 160, "enum", "«enumeration»")
p.cls("e5", "Prioritas", ["tinggi", "sedang", "rendah"], 780, 820, 150, "enum", "«enumeration»")
p.v("n0", LEG, NOTE, 960, 820, 560, 120)
p.v("n1", "<b>Kunci</b><br>• Satu konsep Rencana untuk tahunan dan pengembangan, dibedakan <i>jenis</i> (brief, pola bersama). "
    "TemuanGap, nilai risiko/manfaat, dan UkuranManfaat hanya terisi untuk jenis pengembangan (AB-02, AB-20).<br>"
    "• Rujukan Renstra institusi berupa teks (keputusan 14 Nov 2026), jadi tidak ada asosiasi ke Renstra.<br>"
    "• Revisi rencana memakai <i>revisi_dari</i> di CM-1.", NOTE, 960, 960, 560, 110)
p.v("n2", SRC, NOTE, 40, 960, 880, 46)
pages.append((p, 1580, 1100))

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
