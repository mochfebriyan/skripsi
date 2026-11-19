"""Conceptual model modul SDM & Kompetensi (Langkah 9), 5 halaman (CM-1 dipecah menjadi 1a dan 1b) + halaman catatan.

Fungsi gambar dan gaya disalin dari contoh-tata-kelola/conceptual_model.py versi `main` (polos hitam-putih);
yang diganti hanya data dan prefiks ID (sdm-).

Jalankan:
    python -I projek-fiklab/tools/drawio/sdm/conceptual_model.py projek-fiklab/rancangan/conceptual-model-sdm.drawio
    python -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/conceptual-model-sdm.drawio sdm-
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
LH = 15


def esc(s):
    return escape(s, {'"': "&quot;"})


FONT = "fontFamily=Times New Roman;"
PLAIN = "fillColor=#FFFFFF;strokeColor=#000000;swimlaneFillColor=#FFFFFF;" + FONT
FILL = {k: PLAIN for k in ("c", "abs", "enum", "stub")}
TXT = ("text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
       "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;" + FONT)
ASSOC = "endArrow=none;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#000000;fontSize=10;" + FONT
COMP = "endArrow=none;startArrow=diamondThin;startFill=1;startSize=16;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#000000;fontSize=10;" + FONT
GEN = "endArrow=block;endFill=0;endSize=14;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#000000;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"


class Page:
    def __init__(self, n, name, title):
        self.P, self.n, self.name, self.cells = f"sdm-cm{n}-", n, name, []
        self.title, self.notes, self.maxx, self.maxy = title, [], 0, 0

    def v(self, id, val, style, x, y, w, h, parent="1"):
        if parent == "1":
            self.maxx, self.maxy = max(self.maxx, x + w), max(self.maxy, y + h)
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

    def stub(self, id, name, note, x, y, w=200):
        self.cls(id, name, [f"<i>{note}</i>"], x, y, w, "stub")

    def e(self, id, s, t, style, src=None, tgt=None, mid=None, pts=None, exit=None, entry=None):
        """Asosiasi. Label peran ditaruh di LUAR kotak, mengikuti sisi tempat garis keluar/masuk
        (exit/entry: x=0 kiri, x=1 kanan, y=0 atas, y=1 bawah)."""
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

        def side(pt):
            if pt is None:
                return "R"
            x, y = pt
            return "L" if x == 0 else "R" if x == 1 else "U" if y == 0 else "D"

        place = {"R": ("left", "bottom", 6, -2), "L": ("right", "bottom", -6, -2),
                 "D": ("left", "top", 4, 4), "U": ("left", "bottom", 4, -4)}
        for k, (lbl, xpos, pt) in enumerate([(src, -1, exit), (tgt, 1, entry)]):
            if lbl:
                al, va, dx, dy = place[side(pt)]
                self.cells.append(
                    f'<mxCell id="{eid}-l{k}" value="{esc(lbl)}" style="edgeLabel;resizable=0;html=1;align={al};verticalAlign={va};'
                    f'fontSize=10;labelBackgroundColor=#FFFFFF;{FONT}" connectable="0" vertex="1" parent="{eid}"><mxGeometry x="{xpos}" '
                    f'relative="1" as="geometry"><mxPoint x="{dx}" y="{dy}" as="offset"/></mxGeometry></mxCell>')

    def xml(self, w=None, h=None):
        w, h = w or self.maxx + 40, h or self.maxy + 40
        return (f'<diagram id="sdm-cm{self.n}" name="{esc(self.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" '
                f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" '
                'math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")


LEG = ("<b>Notasi</b> (Wazlawick 2024, Bab 8–9)<br>"
       "• Hanya konsep, atribut primitif, dan asosiasi: <b>tanpa method, tanpa detail Odoo</b>.<br>"
       "• Garis polos = asosiasi; label di ujung = <i>peran</i> dan multiplisitas. Belah ketupat hitam = komposisi (bagian–keseluruhan).<br>"
       "• Segitiga kosong = generalisasi. Nama miring = konsep abstrak. <code>{DokumenSDM}</code> / <code>{RekamanBukti}</code> di atas nama "
       "= turunan konsep itu (CM-3).<br>"
       "• <code>/nama</code> = atribut atau asosiasi turunan (dihitung). «unique» = tidak boleh kembar. <code>[0..1]</code> = boleh kosong.<br>"
       "• Kotak bertuliskan <i>rincian: CM-n</i> atau <i>master Core</i> = konsep yang dirinci di halaman lain atau milik Core.")
SRC = ("Bahan kerja. Sumber: kamus DTO (ssd-sdm.md), AB-SDM-01–28 (expanded-use-case-sdm.md). "
       "Rincian: conceptual-model-sdm.md · Draf 19 Nov 2026 · Zahir")
DS = "{DokumenSDM}"
RB = "{RekamanBukti}"
EN = "«enumeration»"
pages = []

# ======================================================== CM-1a Kompetensi
p = Page("1a", "CM TO-BE (1a-4) - Kompetensi", "CM-1a · Kompetensi, syarat jabatan, dan bukti kompetensi (PKG-04, 10, 14)")
p.stub("jab", "Jabatan", "master Core", 40, 40, 170)
p.cls("kom", "Kompetensi", ["+ nama: String «unique»", "+ jenis: JenisKompetensi", "+ kode_acuan: String [0..1]",
                            "+ keterangan: Text [0..1]"], 430, 30, 260)
p.e("jab-kom", "jab", "kom", ASSOC, src="*", tgt="kompetensi_wajib *", exit=(1, 0.5), entry=(0, 0.37))
p.cls("per", "Personel", ["<i>master Core</i>", "+ nama: String", "+ jenis: JenisPersonel"], 25, 230, 200)
p.e("per-jab", "per", "jab", ASSOC, src="pemegang *", tgt="jabatan 0..1", exit=(0.5, 0), entry=(0.5, 1))
p.cls("bk", "BuktiKompetensi", ["+ jenis_bukti: JenisBukti", "+ nomor_dokumen: String [0..1]", "+ penerbit: String [0..1]",
                                "+ berlaku_sampai: Date [0..1]", "+ /berlaku: Boolean (AB-SDM-13)"], 900, 30, 290, "c", RB)
p.e("bk-kom", "bk", "kom", ASSOC, src="*", tgt="kompetensi 1", exit=(0, 0.28), entry=(1, 0.37))
p.e("bk-per", "bk", "per", ASSOC, src="bukti *", tgt="pemilik 1", pts=[(1045, 290)], exit=(0.5, 1), entry=(1, 0.75))
p.e("per-kurang", "per", "kom", ASSOC, src="*", tgt="/kompetensi_kurang *", pts=[(560, 254)], exit=(1, 0.3), entry=(0.5, 1))
p.cls("e1", "JenisKompetensi", ["pendidikan", "keahlian", "sertifikasi", "pelatihan_fungsional"], 40, 380, 180, "enum", EN)
p.cls("e2", "JenisBukti", ["pendidikan", "pelatihan", "sertifikasi", "pengalaman", "demonstrasi"], 260, 380, 160, "enum", EN)
p.notes.append(("<b>Kunci</b><br>• <i>Specification class</i> (§11.3): Kompetensi = spesifikasi; BuktiKompetensi = <i>exemplar</i> milik "
    "satu Personel. Syarat jabatan merujuk spesifikasi.<br>"
    "• <i>/kompetensi_kurang</i> = kompetensi wajib jabatan yang tidak punya bukti berlaku (AB-SDM-13); dasar matriks, S3 PKG-04, "
    "dan kebutuhan pelatihan.<br>"
    "• Masa berlaku BuktiKompetensi = interval milik objeknya sendiri (<i>effectivity</i>, §11.12.1).", 100))
pages.append(p)

# ======================================================== CM-1b Seleksi dan penugasan
p = Page("1b", "CM TO-BE (1b-4) - Seleksi dan Penugasan", "CM-1b · Seleksi asisten, kebutuhan petugas, dan penugasan (PKG-04)")
p.cls("seb", "Seleksi", ["+ nilai_mk: String", "+ skor_wawancara: Real [0..1]", "+ skor_simulasi: Real [0..1]",
                         "+ skor_modul: Real [0..1]", "+ keputusan: KeputusanSeleksi",
                         "<i>{unique: asisten, mata_kuliah, periode}</i>"], 40, 40, 290, "c", RB)
p.stub("mk", "Mata Kuliah", "master Core", 470, 85, 170)
p.e("seb-mk", "seb", "mk", ASSOC, src="*", tgt="mata_kuliah 1", exit=(1, 0.5), entry=(0, 0.5))
p.stub("prd1", "Periode", "master Core", 20, 320, 170)
p.e("seb-prd", "seb", "prd1", ASSOC, src="*", tgt="periode 1", exit=(0.2, 1), entry=(0.46, 0))
p.cls("pgc", "Pengecualian", ["+ alasan: Text"], 330, 250, 220)
p.e("seb-pgc", "seb", "pgc", COMP, src="1", tgt="pengecualian 0..1", pts=[(440, 165)], exit=(1, 0.9), entry=(0.5, 0))
p.stub("perB", "Personel", "master Core", 200, 440, 170)
p.e("seb-per", "seb", "perB", ASSOC, src="seleksi *", tgt="asisten 1", exit=(0.6, 1), entry=(0.08, 0))
p.e("pgc-per", "pgc", "perB", ASSOC, src="*", tgt="penyetuju 1", pts=[(396, 465)], exit=(0.3, 1), entry=(1, 0.5))
p.stub("kls", "Kelas", "master Core", 780, 85, 170)
p.e("kls-mk", "kls", "mk", ASSOC, src="*", tgt="mata_kuliah 1", exit=(0, 0.5), entry=(1, 0.5))
p.cls("kbt", "KebutuhanPetugas", ["+ peran: PeranPetugas", "+ jumlah_minimal: Natural", "+ dasar_penetapan: Text",
                                  "<i>{unique: kelas, peran}</i>"], 600, 260, 290, "c", RB)
p.e("kbt-kls", "kbt", "kls", ASSOC, src="*", tgt="kelas 1", exit=(0.8, 0), entry=(0.3, 1))
p.cls("bp", "BarisPenugasan", ["+ peran: PeranPetugas", "+ berlaku_mulai: Date", "+ berlaku_sampai: Date",
                               "+ /berlaku: Boolean (AB-SDM-16)"], 1100, 60, 260)
p.e("bp-kls", "bp", "kls", ASSOC, src="*", tgt="kelas 0..1 (asisten)", exit=(0, 0.53), entry=(1, 0.5))
p.cls("st", "SuratTugas", ["+ nomor: String «unique»", "+ berkas_komitmen: Berkas [0..1]"], 1500, 60, 260, "c", DS)
p.e("st-bp", "st", "bp", COMP, src="1", tgt="baris 1..*", exit=(0, 0.5), entry=(1, 0.42))
p.stub("prd2", "Periode", "master Core", 1545, 240, 170)
p.e("st-prd", "st", "prd2", ASSOC, src="*", tgt="berlaku_pada 1", exit=(0.5, 1), entry=(0.5, 0))
p.stub("perC", "Personel", "master Core", 1000, 300, 170)
p.e("bp-per", "bp", "perC", ASSOC, src="*", tgt="petugas 1", exit=(0.15, 1), entry=(0.82, 0))
p.stub("rng", "Ruang", "master Core", 1200, 260, 170)
p.e("bp-rng", "bp", "rng", ASSOC, src="*", tgt="ruang 0..1 (laboran)", exit=(0.7, 1), entry=(0.48, 0))
p.stub("ses", "Sesi", "master Core (/terlaksana)", 1180, 440, 200)
p.e("ses-rng", "ses", "rng", ASSOC, src="*", tgt="ruang 1", exit=(0.5, 0), entry=(0.47, 1))
p.e("ses-kls", "ses", "kls", ASSOC, src="*", tgt="kelas 1", pts=[(940, 465)], exit=(0, 0.5), entry=(0.94, 1))
p.cls("ori", "Orientasi", ["+ jenis: JenisOrientasi"], 1500, 420, 220, "c", RB)
p.stub("perD", "Personel", "master Core", 1530, 600, 170)
p.e("ori-per", "ori", "perD", ASSOC, src="*", tgt="petugas 1", exit=(0.3, 1), entry=(0.21, 0))
p.e("ori-per2", "ori", "perD", ASSOC, src="*", tgt="pelaksana 1", exit=(0.8, 1), entry=(0.86, 0))
p.cls("e3", "PeranPetugas", ["asisten", "laboran"], 40, 600, 150, "enum", EN)
p.cls("e4", "KeputusanSeleksi", ["lulus", "lulus_pengecualian"], 220, 600, 170, "enum", EN)
p.cls("e5", "JenisOrientasi", ["orientasi", "supervisi"], 420, 600, 150, "enum", EN)
p.notes.append(("<b>Kunci</b><br>• Pengecualian adalah konsep kejadian (§9.3.2): baru ada bila keputusan <i>lulus_pengecualian</i> (AB-SDM-15).<br>"
    "• Masa berlaku BarisPenugasan = interval milik objeknya sendiri (<i>effectivity</i>, §11.12.1).<br>"
    "• Kotak Personel, Periode, dan Mata Kuliah digambar lebih dari sekali agar garis tidak bersilangan; semuanya konsep yang sama.", 100))
pages.append(p)

# ======================================================== CM-2 Otorisasi
p = Page(2, "CM TO-BE (2-4) - Otorisasi", "CM-2 · Tugas/alat berkewenangan khusus, asesmen, otorisasi, dan evaluasi ulang (PKG-10)")
p.stub("kom", "Kompetensi", "rincian: CM-1", 20, 60, 180)
p.cls("tk", "TugasKhusus", ["+ nama: String", "+ jenis: JenisTugasKhusus", "+ lokasi: String [0..1]",
                            "+ masa_berlaku_bulan: Natural", "+ cara_pembatasan: CaraPembatasan [0..1]",
                            "+ berkas_pembatasan: Berkas [0..1]"], 400, 30, 300)
p.e("tk-kom", "tk", "kom", ASSOC, src="*", tgt="kompetensi_disyaratkan 1..*", exit=(0, 0.4), entry=(1, 0.4))
p.cls("ase", "Asesmen", ["+ metode: MetodeAsesmen", "+ skor: Real [0..1]", "+ unsur_kritis_terpenuhi: Boolean",
                         "+ kesimpulan: KesimpulanAsesmen", "+ catatan_pengembangan: Text [0..1]"], 850, 30, 300, "c", RB)
p.e("ase-tk", "ase", "tk", ASSOC, src="*", tgt="tugas_khusus 1", exit=(0, 0.4), entry=(1, 0.4))
p.stub("perB", "Personel", "master Core", 1330, 40, 170)
p.e("ase-per", "ase", "perB", ASSOC, src="*", tgt="personel 1", exit=(1, 0.2), entry=(0, 0.3))
p.e("ase-per2", "ase", "perB", ASSOC, src="*", tgt="penilai 1", exit=(1, 0.4), entry=(0, 0.8))
p.stub("bk", "BuktiKompetensi", "rincian: CM-1", 990, 250, 200)
p.e("ase-bk", "ase", "bk", ASSOC, src="sumber 0..1", tgt="bukti_dihasilkan *", exit=(0.8, 1), entry=(0.5, 0))
p.cls("oto", "Otorisasi", ["+ lingkup: Text", "+ level: LevelOtorisasi", "+ berlaku_mulai: Date", "+ berlaku_sampai: Date",
                           "+ /berlaku: Boolean (AB-SDM-18)"], 400, 360, 300, "c", DS)
p.e("oto-tk", "oto", "tk", ASSOC, src="*", tgt="tugas_khusus 1", exit=(0.5, 0), entry=(0.5, 1))
p.stub("perA", "Personel", "master Core", 40, 395, 170)
p.e("oto-per", "oto", "perA", ASSOC, src="*", tgt="personel 1", exit=(0, 0.32), entry=(1, 0.1))
p.e("oto-sup", "oto", "perA", ASSOC, src="*", tgt="supervisor 0..1", exit=(0, 0.6), entry=(1, 0.8))
p.e("tk-per", "tk", "perA", ASSOC, src="*", tgt="pelaksana *", pts=[(125, 136)], exit=(0, 0.85), entry=(0.5, 0))
p.e("oto-ase", "oto", "ase", ASSOC, src="*", tgt="dasar_asesmen 0..1", pts=[(910, 385)], exit=(1, 0.2), entry=(0.2, 1))
p.e("oto-bk", "oto", "bk", ASSOC, src="*", tgt="dasar_bukti *", pts=[(1090, 429)], exit=(1, 0.55), entry=(0.5, 1))
p.cls("evu", "EvaluasiUlang", ["+ pemicu: JenisPemicu", "+ /status: StatusEvaluasi (terbuka bila belum ada keputusan)"],
      400, 580, 340, "c", RB)
p.e("evu-oto", "evu", "oto", ASSOC, src="evaluasi *", tgt="otorisasi 1", exit=(0.44, 0), entry=(0.5, 1))
p.cls("kpt", "KeputusanEvaluasi", ["+ keputusan: JenisKeputusan", "+ hasil: Text", "+ tanggal: Date"], 880, 580, 260)
p.e("evu-kpt", "evu", "kpt", COMP, src="1", tgt="keputusan 0..1", exit=(1, 0.5), entry=(0, 0.5))
p.e("kpt-oto", "kpt", "oto", ASSOC, src="0..1", tgt="otorisasi_baru 0..1", pts=[(958, 520), (650, 520)],
    exit=(0.3, 0), entry=(0.83, 1))
p.stub("perC", "Personel", "master Core", 1290, 595, 170)
p.e("kpt-per", "kpt", "perC", ASSOC, src="*", tgt="penilai 1", exit=(1, 0.5), entry=(0, 0.5))
p.cls("e1", "JenisTugasKhusus", ["tugas", "alat", "software"], 40, 740, 150, "enum", EN)
p.cls("e2", "CaraPembatasan", ["dikunci", "akun", "diawasi", "lainnya"], 210, 740, 150, "enum", EN)
p.cls("e3", "MetodeAsesmen", ["demonstrasi", "uji_praktik", "tinjauan_sertifikat"], 380, 740, 170, "enum", EN)
p.cls("e4", "KesimpulanAsesmen", ["layak", "belum_layak"], 570, 740, 160, "enum", EN)
p.cls("e5", "LevelOtorisasi", ["terbimbing", "mandiri"], 750, 740, 140, "enum", EN)
p.cls("e6", "JenisPemicu", ["masa_berlaku_habis", "alat_berubah", "insiden", "lama_tidak_aktif", "lainnya"], 910, 740, 170, "enum", EN)
p.cls("e7", "JenisKeputusan", ["diperpanjang", "dibatasi", "naik_level", "dicabut", "tetap_berlaku"], 1100, 740, 160, "enum", EN)
p.notes.append(("<b>Kunci</b><br>• Pasangan <i>pelaksana</i> × TugasKhusus = unit PKG-10 (penyebut, KB-1).<br>"
    "• KeputusanEvaluasi = konsep kejadian (§9.3.2): baru ada saat evaluasi diputuskan; <i>/status</i> EvaluasiUlang dihitung dari "
    "ada-tidaknya keputusan (S2).<br>"
    "• Otorisasi baru menggantikan yang lama lewat asosiasi <i>menggantikan</i> di DokumenSDM (CM-3), pola <i>superseding</i> (§11.9.2).<br>"
    "• Masa berlaku Otorisasi = interval sendiri, bukan Periode (K-3).", 120))
pages.append(p)

# ======================================================== CM-3 Pengesahan dan rekaman bukti
p = Page(3, "CM TO-BE (3-4) - Pengesahan dan Rekaman Bukti", "CM-3 · Dokumen SDM yang disahkan, riwayat pengesahan, dan rekaman bukti")
p.stub("st", "SuratTugas", "rincian: CM-1", 240, 30, 180)
p.stub("oto", "Otorisasi", "rincian: CM-2", 460, 30, 180)
p.stub("rp", "RencanaPelatihan", "rincian: CM-4", 680, 30, 180)
p.cls("ds", "DokumenSDM", ["+ status: StatusDokumen = draf", "+ /jenis_dokumen: JenisDokumenSDM",
                           "+ /tanggal_ajukan: Date", "+ /berkas_ttd: Berkas"], 400, 170, 340, "abs", "«abstract»")
for s in ["st", "oto", "rp"]:
    p.e(f"g-{s}", s, "ds", GEN, exit=(0.5, 1), entry=(0.5, 0))
p.e("rev", "ds", "ds", ASSOC, src="pengganti 0..1", tgt="digantikan 0..1", mid="menggantikan",
    pts=[(830, 203), (830, 130), (672, 130)], exit=(1, 0.3), entry=(0.8, 0))
p.stub("perA", "Personel", "master Core", 20, 190, 170)
p.e("ds-per", "ds", "perA", ASSOC, src="*", tgt="penyusun 1", exit=(0, 0.27), entry=(1, 0.2))
p.e("ds-pbw", "ds", "perA", ASSOC, src="*", tgt="/pengesah_berwenang *", exit=(0, 0.55), entry=(1, 0.8))
p.cls("pgs", "Pengesahan", ["+ tanggal_sah: Date"], 400, 390, 200)
p.e("ds-pgs", "ds", "pgs", ASSOC, src="1", tgt="pengesahan 0..1", exit=(0.25, 1), entry=(0.43, 0))
p.cls("kej", "KejadianPengesahan", ["+ jenis: JenisKejadian", "+ waktu: DateTime", "+ alasan: Text [0..1]",
                                    "+ berkas: Berkas [0..1]"], 640, 390, 240)
p.e("ds-kej", "ds", "kej", COMP, src="1", tgt="riwayat * {urut waktu}", exit=(0.8, 1), entry=(0.13, 0))
p.stub("perB", "Personel", "master Core", 400, 560, 170)
p.e("pgs-per1", "pgs", "perB", ASSOC, src="*", tgt="pengesah 1", exit=(0.3, 1), entry=(0.35, 0))
p.e("pgs-per2", "pgs", "perB", ASSOC, src="*", tgt="pencatat 1", exit=(0.7, 1), entry=(0.82, 0))
p.e("kej-per", "kej", "perB", ASSOC, src="*", tgt="pelaku 0..1", pts=[(760, 585)], exit=(0.5, 1), entry=(1, 0.5))
p.cls("e1", "StatusDokumen", ["draf", "diajukan", "disahkan", "diganti", "dicabut"], 1000, 30, 170, "enum", EN)
p.cls("e2", "JenisKejadian", ["diajukan", "dikembalikan", "berkas_diunggah", "disahkan", "diganti", "dicabut"],
      1000, 180, 170, "enum", EN)
p.cls("e3", "JenisDokumenSDM", ["penugasan_petugas", "otorisasi", "rencana_pelatihan"], 1000, 345, 190, "enum", EN)
p.cls("rb", "RekamanBukti", ["+ tanggal: Date", "+ bukti: Berkas [0..1]", "+ keterangan: Text [0..1]"],
      530, 700, 260, "abs", "«abstract»")
p.stub("perC", "Personel", "master Core", 940, 722, 170)
p.e("rb-per", "rb", "perC", ASSOC, src="*", tgt="pelapor 1", exit=(1, 0.5), entry=(0, 0.5))
subs = [("bk", "BuktiKompetensi", "CM-1"), ("kbt", "KebutuhanPetugas", "CM-1"), ("seb", "Seleksi", "CM-1"),
        ("ori", "Orientasi", "CM-1"), ("ase", "Asesmen", "CM-2"), ("evu", "EvaluasiUlang", "CM-2"),
        ("rls", "RealisasiPelatihan", "CM-4"), ("eve", "EvaluasiEfektivitas", "CM-4")]
for i, (sid, name, pg) in enumerate(subs):
    x = 20 + i * 162
    p.stub(sid, name, f"rincian: {pg}", x, 900, 150)
    p.e(f"g-{sid}", sid, "rb", GEN, pts=[(x + 75, 860), (660, 860)], exit=(0.5, 0), entry=(0.5, 1))
p.notes.append(("<b>Kunci</b><br>• Data yang muncul saat status berubah (pengesah, tanggal sah, alasan, berkas) disimpan sebagai konsep "
    "kejadian (Pengesahan, KejadianPengesahan), bukan atribut opsional (§9.3.2).<br>"
    "• <i>menggantikan</i> = pola <i>superseding</i> (§11.9.2): surat tugas yang direvisi, atau otorisasi lama untuk pasangan yang sama.<br>"
    "• <i>/pengesah_berwenang</i> = Personel yang jabatannya berwenang mengesahkan jenis dokumen itu (AB-SDM-07).<br>"
    "• Tidak ada status <i>kedaluwarsa</i> (K-3). RekamanBukti tidak dihapus, hanya dikoreksi (AB-SDM-24).", 130))
pages.append(p)

# ======================================================== CM-4 Pelatihan
p = Page(4, "CM TO-BE (4-4) - Pelatihan", "CM-4 · Rencana, realisasi, dan evaluasi efektivitas pelatihan PLP/laboran (PKG-14)")
p.cls("rp", "RencanaPelatihan", ["+ judul: String", "+ kebutuhan_dibekukan: Boolean", "+ /kriteria_tertinggi: 0..4 (AB-SDM-28)",
                                 "<i>{satu Disahkan per periode}</i>"], 420, 30, 300, "c", DS)
p.stub("prd", "Periode", "master Core", 40, 60, 170)
p.e("rp-prd", "rp", "prd", ASSOC, src="*", tgt="berlaku_pada 1", exit=(0, 0.5), entry=(1, 0.5))
p.cls("kbk", "KebutuhanKompetensi", ["+ tidak_ada_gap: Boolean", "+ sumber: SumberKebutuhan", "+ keterangan: Text [0..1]"],
      900, 45, 280)
p.e("rp-kbk", "rp", "kbk", COMP, src="1", tgt="kebutuhan 1..*", exit=(1, 0.5), entry=(0, 0.5))
p.stub("perA", "Personel", "master Core", 1320, 60, 170)
p.e("kbk-per", "kbk", "perA", ASSOC, src="*", tgt="personel 1", exit=(1, 0.5), entry=(0, 0.5))
p.stub("kom", "Kompetensi", "rincian: CM-1", 950, 240, 180)
p.e("kbk-kom", "kbk", "kom", ASSOC, src="*", tgt="kompetensi 0..1", exit=(0.5, 1), entry=(0.5, 0))
p.cls("itm", "ItemPelatihan", ["+ jenis: JenisPelatihan", "+ materi: Text", "+ penyelenggara: String", "+ anggaran: Money",
                               "+ jadwal_mulai: Date", "+ jadwal_selesai: Date", "+ kriteria_keberhasilan: Text",
                               "+ status: StatusItem = rencana", "+ /status_evaluasi: StatusEvaluasiItem"], 420, 240, 300)
p.e("rp-itm", "rp", "itm", COMP, src="1", tgt="item *", exit=(0.5, 1), entry=(0.5, 0))
p.e("itm-kom", "itm", "kom", ASSOC, src="*", tgt="kompetensi_sasaran 1", exit=(1, 0.15), entry=(0, 0.5))
p.stub("perB", "Personel", "master Core", 950, 340, 170)
p.e("itm-per", "itm", "perB", ASSOC, src="*", tgt="peserta 1..*", exit=(1, 0.75), entry=(0, 0.5))
p.cls("btl", "PembatalanItem", ["+ alasan: Text", "+ tanggal: Date"], 40, 300, 220)
p.e("itm-btl", "itm", "btl", COMP, src="1", tgt="pembatalan 0..1", exit=(0, 0.54), entry=(1, 0.5))
p.cls("rls", "RealisasiPelatihan", ["+ penyelenggara: String", "+ durasi_jam: Real", "+ sertifikat: Berkas [0..1]",
                                    "<i>{unique: item, peserta}</i>"], 420, 520, 300, "c", RB)
p.e("rls-itm", "rls", "itm", ASSOC, src="*", tgt="item 1", exit=(0.5, 0), entry=(0.5, 1))
p.stub("perD", "Personel", "master Core", 40, 550, 170)
p.e("rls-per", "rls", "perD", ASSOC, src="*", tgt="peserta 1", exit=(0, 0.5), entry=(1, 0.5))
p.cls("eve", "EvaluasiEfektivitas", ["+ metode: MetodeEvaluasi", "+ skor_sebelum: Real [0..1]", "+ skor_sesudah: Real [0..1]",
                                     "+ kesimpulan: KesimpulanEvaluasi", "+ peningkatan_layanan: Text [0..1]",
                                     "+ tindak_lanjut: Text [0..1]"], 900, 505, 300, "c", RB)
p.e("rls-eve", "rls", "eve", ASSOC, src="1", tgt="evaluasi 0..1", exit=(1, 0.5), entry=(0, 0.5))
p.stub("perC", "Personel", "master Core", 1340, 550, 170)
p.e("eve-per", "eve", "perC", ASSOC, src="*", tgt="penilai 1", exit=(1, 0.5), entry=(0, 0.5))
p.stub("bk", "BuktiKompetensi", "rincian: CM-1", 950, 750, 200)
p.e("eve-bk", "eve", "bk", ASSOC, src="sumber 0..1", tgt="bukti_dihasilkan 0..1", exit=(0.5, 1), entry=(0.5, 0))
p.cls("e1", "SumberKebutuhan", ["matriks", "tambahan"], 40, 870, 150, "enum", EN)
p.cls("e2", "JenisPelatihan", ["diklatfung", "bimtek", "sertifikasi", "internal"], 210, 870, 150, "enum", EN)
p.cls("e3", "StatusItem", ["rencana", "terlaksana", "batal"], 380, 870, 140, "enum", EN)
p.cls("e4", "StatusEvaluasiItem", ["menunggu_evaluasi", "dievaluasi"], 540, 870, 170, "enum", EN)
p.cls("e5", "MetodeEvaluasi", ["asesmen_ulang", "penilaian_kinerja"], 1180, 870, 170, "enum", EN)
p.cls("e6", "KesimpulanEvaluasi", ["efektif", "perlu_pengembangan"], 1370, 870, 170, "enum", EN)
p.notes.append(("<b>Kunci</b><br>• KebutuhanKompetensi terisi awal dari <i>/kompetensi_kurang</i> Personel (CM-1, AB-SDM-20) dan dibekukan "
    "saat rencana diajukan.<br>"
    "• PembatalanItem = konsep kejadian (§9.3.2), lapis Pelengkap (AB-SDM-22). <i>/status_evaluasi</i> dihitung dari ada-tidaknya "
    "evaluasi setiap realisasi (S3).<br>"
    "• EvaluasiEfektivitas <i>efektif</i> menghasilkan BuktiKompetensi baru, sehingga siklus kompetensi tertutup (K4).", 110))
pages.append(p)

# ======================================================== halaman catatan
c = Page("-notes", "Catatan CM TO-BE (bahan kerja)", "")
c.P = "sdm-cm-notes-"
c.v("title", "Catatan conceptual model modul SDM (bahan kerja)", TITLE, 40, 10, 1300, 34)
c.v("legend", LEG, NOTE, 40, 56, 1300, 110)
c.v("src", SRC, NOTE, 40, 176, 1300, 40)
y = 236
for i, pg in enumerate(pages):
    c.v(f"h{i}", f"<b>{pg.title}</b>", "text;html=1;fontSize=12;align=left;verticalAlign=top;whiteSpace=wrap;", 40, y, 1300, 24)
    y += 30
    for j, (txt, h) in enumerate(pg.notes):
        c.v(f"n{i}-{j}", txt, NOTE, 40, y, 1300, h)
        y += h + 10
    y += 10
pages.append(c)

with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(pg.xml() for pg in pages) + "</mxfile>")
