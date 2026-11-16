"""Conceptual model modul Pelaksanaan Praktikum (langkah 9), 4 halaman.

Mesin gambar disalin dari contoh-tata-kelola/conceptual_model.py; prefiks (prk-cm), warna modul,
nama halaman, stereotype, dan data diganti.
Pemakaian: python -X utf8 -I conceptual_model.py projek-fiklab/rancangan/conceptual-model-praktikum.drawio
Catatan: tulis '<' dan '>' di nama tipe sebagai &lt; &gt; (label memakai HTML).
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
LH = 15


def esc(s):
    return escape(s, {'"': "&quot;"})


FILL = {"c": "fillColor=#FFFFFF;strokeColor=#333333;",
        "abs": "fillColor=#EEF6FF;strokeColor=#6C8EBF;",
        "enum": "fillColor=#F5F5F5;strokeColor=#666666;",
        "prim": "fillColor=#F5F5F5;strokeColor=#666666;",
        "stub": "fillColor=#FAFAFA;strokeColor=#999999;dashed=1;"}
TXT = ("text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
       "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;")
ASSOC = "endArrow=none;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#444444;fontSize=10;"
DER = "endArrow=open;endSize=10;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#444444;fontSize=10;"
COMP = ("endArrow=none;startArrow=diamondThin;startFill=1;startSize=16;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;"
        "strokeColor=#333333;fontSize=10;")
GEN = "endArrow=block;endFill=0;endSize=14;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#6C8EBF;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"
NPAGE = 4


class Page:
    def __init__(self, n, name, title):
        self.P, self.n, self.name, self.cells = f"prk-cm{n}-", n, name, []
        self.v("title", title, TITLE, 40, 4, 1500, 30)

    def v(self, id, val, style, x, y, w, h, parent="1"):
        par = "1" if parent == "1" else self.P + parent
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="{par}">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def cls(self, id, name, attrs, x, y, w=250, kind="c", stereo=None):
        if kind == "abs" and stereo is None:
            stereo = "«abstract»"
        title = (f"<font style='font-size:10px'>{stereo}</font><br>" if stereo else "") + \
                (f"<b><i>{name}</i></b>" if kind == "abs" else f"<b>{name}</b>")
        start = 12 + 15 * (title.count("<br>") + 1)
        ah = max(1, len(attrs)) * LH + 8
        self.v(id, title, "swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;"
               f"startSize={start};horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;"
               f"marginBottom=0;whiteSpace=wrap;html=1;fontSize=12;{FILL[kind]}", x, y, w, start + ah)
        self.v(id + "-a", "<br>".join(attrs) if attrs else " ", TXT, 0, start, w, ah, parent=id)

    def stub(self, id, name, lines, x, y, w=230):
        self.cls(id, name, [f"<i>{t}</i>" for t in lines], x, y, w, "stub")

    def enum(self, id, name, vals, x, y, w=200):
        self.cls(id, name, vals, x, y, w, "enum", "«enumeration»")

    def e(self, id, s, t, style, src=None, tgt=None, pts=None, exit=None, entry=None):
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
        self.cells.append(f'<mxCell id="{eid}" value="" style="{st}labelBackgroundColor=#FFFFFF;" edge="1" '
                          f'parent="1" source="{self.P}{s}" target="{self.P}{t}">{geo}</mxCell>')
        # Label ujung diletakkan di luar kotak, bergantung sisi tempat garis keluar/masuk.
        for k, (lbl, xpos, port) in enumerate([(src, -1, exit), (tgt, 1, entry)]):
            if not lbl:
                continue
            side = None if port is None else ("l" if port[0] == 0 else "r" if port[0] == 1 else
                                              "t" if port[1] == 0 else "b" if port[1] == 1 else None)
            align, valign, dx, dy = {"l": ("right", "bottom", -8, -2), "r": ("left", "bottom", 8, -2),
                                     "t": ("left", "bottom", 8, -2), "b": ("left", "top", 8, 2)}.get(
                side, ("left", "bottom", 8, -2) if xpos < 0 else ("right", "bottom", -8, -2))
            self.cells.append(
                f'<mxCell id="{eid}-l{k}" value="{esc(lbl)}" style="edgeLabel;resizable=0;html=1;align={align};'
                f'verticalAlign={valign};fontSize=10;labelBackgroundColor=#FFFFFF;" connectable="0" vertex="1" '
                f'parent="{eid}"><mxGeometry x="{xpos}" relative="1" as="geometry"><mxPoint x="{dx}" '
                f'y="{dy}" as="offset"/></mxGeometry></mxCell>')

    def xml(self, w, h):
        return (f'<diagram id="prk-cm{self.n}" name="{esc(self.name)}"><mxGraphModel dx="1600" dy="900" grid="1" '
                f'gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
                f'pageWidth="{w}" pageHeight="{h}" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
                + "".join(self.cells) + "</root></mxGraphModel></diagram>")


def pname(n, isi):
    return f"CM TO-BE ({n}-{NPAGE}) - {isi}"


LEG = ("<b>Notasi</b> (Wazlawick 2024, Bab 8–11)<br>"
       "• Hanya konsep, atribut primitif, dan asosiasi: <b>tanpa method, tanpa detail Odoo</b>, tanpa atribut <code>*_id</code>.<br>"
       "• Garis polos = asosiasi; label di ujung = <i>peran</i> + multiplisitas. Belah ketupat hitam = komposisi (bagian–keseluruhan).<br>"
       "• Segitiga kosong biru = generalisasi; nama miring «abstract» = konsep abstrak.<br>"
       "• <code>/nama</code> = atribut/asosiasi turunan (dihitung, hanya dibaca); panah terbuka = asosiasi turunan satu arah.<br>"
       "• Kotak abu-abu putus-putus = konsep yang dirinci di halaman/dokumen lain. (O) = lapis Pelengkap.<br>"
       "• Tipe primitif: Date, DateTime, Jam, Natural, Real, Persen, Boolean, String, Text, URL, Berkas, Interval&lt;T&gt; (CM-1).")
SRC = ("Bahan kerja (tidak masuk proposal). Sumber: kamus DTO dan katalog operasi ssd-praktikum.md; AB-PRK-01–34 "
       "expanded-use-case-praktikum.md; kontrak-core.md (16 Nov 2026). Rincian: rancangan/conceptual-model-praktikum.md · "
       "Draf 16 Nov 2026 · Herrens")
pages = []

# ============================================================ CM-1
p = Page(1, pname(1, "Jadwal, Sesi, dan Pengajuan"),
         "CM-1 · Conceptual model: jadwal, sesi, dan pengajuan (PKG-15, PKG-18 perubahan sesi)")
p.cls("mk", "MataKuliah", ["«unique» kode: String", "nama: String", "prodi: String", "semester: Natural"], 40, 60, 240)
p.cls("kls", "Kelas", ["nama: String", "jumlah_mahasiswa: Natural"], 40, 250, 240)
p.stub("per", "Periode", ["master Core: nama, tanggal mulai–selesai"], 400, 60, 240)
p.stub("psl", "Personel", ["master Core (orang internal FIK)"], 300, 980, 240)
p.cls("ses", "Sesi", ["pertemuan_ke: Natural (1–16)", "jenis_pertemuan: JenisPertemuan", "moda: Moda = luring",
                      "tanggal: Date", "jam: Interval&lt;Jam&gt;", "status: StatusSesi = terjadwal",
                      "/is_terpublikasi: Boolean", "/is_ditunda: Boolean", "/is_diganti: Boolean", "/is_terlewat: Boolean",
                      "/berasisten: Boolean", "/melebihi_kapasitas: Boolean", "/memenuhi_pkg15 … pkg18: Boolean"],
      400, 230, 300)
p.stub("rng", "Ruang", ["master Core: kode, nama, kapasitas"], 400, 800, 240)
p.stub("dd", "DokumenDisahkan", ["abstrak; status, pengesahan, riwayat:", "CM-1 Tata Kelola"], 820, 50, 260)
p.cls("pj", "PenetapanJadwal", ["/tanggal_publikasi: Date", "/jumlah_sesi: Natural"], 820, 230, 260)
p.cls("aju", "Pengajuan", ["tanggal_ajukan: Date", "/status: StatusPengajuan"], 1200, 470, 260, "abs")
p.cls("kep", "KeputusanPengajuan", ["tanggal_putus: Date", "hasil: HasilKeputusan", "alasan: Text [0..1]", "karena_bentrok: Boolean = false"], 1560, 380, 240)
p.cls("tar", "Penarikan (O)", ["tanggal: Date"], 1560, 560, 240)
p.cls("pml", "PemakaianLab", ["keperluan: Text", "nama_pemohon: String", "unit_pemohon: String", "tanggal: Date",
                              "jam: Interval&lt;Jam&gt;"], 820, 650, 260)
p.cls("pbs", "PerubahanSesi", ["jenis: JenisPerubahan", "alasan: Text"], 1200, 650, 260)
p.cls("usl", "UsulanPengganti", ["tanggal: Date", "jam: Interval&lt;Jam&gt;"], 1200, 820, 260)
ey = 1090
p.enum("e1", "StatusSesi", ["terjadwal", "terlaksana", "batal"], 40, ey, 180)
p.enum("e2", "JenisPertemuan", ["praktikum", "uts", "uas"], 240, ey, 180)
p.enum("e3", "Moda", ["luring", "daring"], 440, ey, 160)
p.enum("e4", "StatusPengajuan", ["diajukan", "disetujui", "ditolak", "ditarik (O)"], 620, ey, 180)
p.enum("e5", "HasilKeputusan", ["disetujui", "ditolak"], 820, ey, 180)
p.enum("e6", "JenisPerubahan", ["pindah", "daring", "batal"], 1020, ey, 180)
p.cls("e7", "Interval&lt;T&gt;", ["awal: T", "akhir: T", "{awal &lt; akhir}"], 1220, ey, 200, "prim", "«primitive»")

p.e("mk-kls", "mk", "kls", ASSOC, "1 mata_kuliah", "* kelas", exit=(0.5, 1), entry=(0.5, 0))
p.e("kls-per", "kls", "per", ASSOC, "*", "1", pts=[(330, 256)], exit=(1, 0.1), entry=(0, 0.5))
p.e("kls-psl1", "kls", "psl", ASSOC, "*", "0..1 dosen_koordinator", pts=[(24, 270), (24, 1005)], exit=(0, 0.3), entry=(0, 0.5))
p.e("kls-psl2", "kls", "psl", ASSOC, "*", "1..* dosen", pts=[(10, 300), (10, 960), (324, 960)], exit=(0, 0.75), entry=(0.1, 0))
p.e("kls-ses", "kls", "ses", ASSOC, "1 kelas", "* sesi", exit=(1, 0.5), entry=(0, 0.22))
p.e("ses-rng", "ses", "rng", ASSOC, "*", "1 ruang", exit=(0.4, 1), entry=(0.5, 0))
p.e("ses-asal", "ses", "ses", DER, None, "0..1 /sesi_asal", pts=[(370, 425), (370, 490), (460, 490)],
    exit=(0, 0.85), entry=(0.2, 1))
p.e("pj-dd", "pj", "dd", GEN, exit=(0.5, 0), entry=(0.5, 1))
p.e("pj-per", "pj", "per", ASSOC, "0..1", "1", pts=[(760, 249), (760, 85)], exit=(0, 0.3), entry=(1, 0.5))
p.e("pml-aju", "pml", "aju", GEN, pts=[(950, 575), (1278, 575)], exit=(0.5, 0), entry=(0.3, 1))
p.e("pbs-aju", "pbs", "aju", GEN, exit=(0.5, 0), entry=(0.7, 1))
p.e("aju-kep", "aju", "kep", COMP, "1", "0..1 keputusan", exit=(1, 0.3), entry=(0, 0.5))
p.e("aju-tar", "aju", "tar", COMP, "1", "0..1 penarikan", exit=(1, 0.8), entry=(0, 0.5))
p.e("aju-psl", "aju", "psl", ASSOC, "*", "1 pengaju", pts=[(1150, 534), (1150, 940), (420, 940)], exit=(0, 0.8), entry=(0.5, 0))
p.e("kep-psl", "kep", "psl", ASSOC, "*", "1 pemutus", pts=[(1840, 420), (1840, 1015)], exit=(1, 0.5), entry=(1, 0.7))
p.e("kep-ses", "kep", "ses", ASSOC, "0..1", "0..1 sesi_pengganti", pts=[(1680, 330)], exit=(0.5, 0), entry=(1, 0.43))
p.e("pml-rng", "pml", "rng", ASSOC, "*", "1 ruang", pts=[(760, 705), (760, 815)], exit=(0, 0.5), entry=(1, 0.3))
p.e("pbs-ses", "pbs", "ses", ASSOC, "*", "1 sesi", pts=[(1239, 625), (720, 625), (720, 391)], exit=(0.15, 0), entry=(1, 0.7))
p.e("pbs-usl", "pbs", "usl", COMP, "1", "0..1 usulan", exit=(0.5, 1), entry=(0.5, 0))
p.e("usl-rng", "usl", "rng", ASSOC, "*", "1 ruang", pts=[(1100, 852), (1100, 840)], exit=(0, 0.5), entry=(1, 0.8))

ny = 1230
p.v("n1", LEG, NOTE, 40, ny, 640, 125)
p.v("n2", "<b>Atribut dan asosiasi turunan</b><br>"
    "• <code>/is_terpublikasi</code> = PenetapanJadwal periode kelasnya berstatus disahkan (AB-PRK-06); "
    "<code>/tanggal_publikasi</code> = tanggal sah.<br>"
    "• <code>/is_ditunda</code> = ada PerubahanSesi atas sesi ini dengan /status = diajukan.<br>"
    "• <code>/sesi_asal</code> = PerubahanSesi yang keputusannya menghasilkan sesi ini → sesinya. "
    "<code>/is_diganti</code> = ada sesi lain yang /sesi_asal-nya sesi ini (pola <i>superseding</i>, §11.9.2).<br>"
    "• <code>/is_terlewat</code> = status terjadwal ∧ tanggal &lt; hari ini ∧ tanpa jurnal terkirim (§9.3.1).<br>"
    "• <code>/melebihi_kapasitas</code> = kelas.jumlah_mahasiswa &gt; ruang.kapasitas (AB-PRK-03). "
    "<code>/berasisten</code>: CM-3. <code>/memenuhi_pkg15…18</code> = cek C/S/B per sesi (AB-PRK-32).<br>"
    "• <code>/status</code> Pengajuan = ditarik bila ada Penarikan; hasil Keputusan bila ada; selain itu diajukan "
    "(kejadian sebagai konsep, §9.3.2).", NOTE, 700, ny, 620, 160)
p.v("n3", "<b>Invarian</b><br>"
    "• Kelas unik per (mata kuliah, periode, nama).<br>"
    "• Satu sesi asli per (kelas, pertemuan_ke); pertemuan 8 = uts, 16 = uas (AB-PRK-02).<br>"
    "• Dua Sesi terjadwal, atau Sesi dan PemakaianLab disetujui, di ruang sama tidak beririsan waktu (AB-PRK-01).<br>"
    "• Paling banyak satu PenetapanJadwal yang tidak dicabut per Periode (AB-PRK-05).<br>"
    "• Hasil ditolak ⇒ alasan terisi (AB-PRK-10). Keputusan dan Penarikan tidak keduanya ada.<br>"
    "• UsulanPengganti ada ⇔ jenis = pindah; sesi_pengganti ada ⇔ disetujui ∧ pindah (AB-PRK-12).",
    NOTE, 1340, ny, 500, 160)
p.v("n4", "<b>Pengaju</b> PemakaianLab = laboran yang mencatat; pemohon (tanpa akun) hanya nama dan unit. "
    "<b>Rekaman konflik</b> (PKG-15 bukti 5, KF-PRK-11) bukan konsep: laporan dari Keputusan ditolak karena_bentrok dan PerubahanSesi disetujui. "
    "Jam = jam dalam hari.", NOTE, 40, 1370, 640, 64)
p.v("n5", SRC, NOTE, 700, 1405, 1140, 42)
pages.append((p, 1880, 1470))

# ============================================================ CM-2
p = Page(2, pname(2, "Versi Modul dan Kesiapan Sesi"),
         "CM-2 · Conceptual model: versi modul dan kesiapan sesi (PKG-15 C4, PKG-16, PKG-17)")
p.stub("ses", "Sesi", ["rincian: CM-1"], 40, 60, 180)
p.stub("rb", "RekamanBukti", ["abstrak: tanggal, bukti [*], keterangan;", "peran pelapor. CM-1 Tata Kelola"], 40, 170, 240)
p.cls("pk", "PemeriksaanKesiapan", ["waktu_periksa: DateTime", "keputusan: KeputusanKesiapan", "/tepat_waktu: Boolean",
                                     "/jumlah_pc_tersedia: Natural (O)"], 340, 60, 280)
p.cls("bp", "ButirPemeriksaan", ["hasil: HasilButir", "keterangan: Text [0..1]"], 340, 230, 280, "abs")
p.cls("bu", "ButirUtilitas", ["kategori: KategoriUtilitas"], 40, 420, 190)
p.cls("bsk", "ButirStasiunKerja", ["jumlah_berfungsi: Natural", "/jumlah_dibutuhkan: Natural"], 250, 420, 200)
p.cls("bbh", "ButirBahan", ["jumlah_tersedia: Real", "kondisi_baik: Boolean", "berlabel: Boolean",
                            "tanggal_kedaluwarsa: Date [0..1]", "/jumlah_dibutuhkan: Real"], 470, 420, 230)
p.cls("bsw", "ButirSoftware", ["lisensi_sah: Boolean [0..1]"], 720, 420, 190)
p.cls("sub", "SubstitusiBahan", ["alasan: Text", "/status_persetujuan: {menunggu,", "&nbsp;&nbsp;&nbsp;disetujui}"],
      470, 580, 230)
p.cls("pst", "PersetujuanSubstitusi", ["waktu: DateTime"], 470, 740, 230)
p.cls("vm", "VersiModul", ["nomor_versi: String", "berkas: Berkas [0..1]", "tautan_leads: URL [0..1]",
                           "rubrik: Berkas [0..1]", "tanggal_terbit: Date", "status: StatusVersiModul = draf"], 720, 60, 280)
p.cls("ksw", "KebutuhanSoftware", ["nama: String", "versi: String", "berbayar: Boolean = false"], 720, 250, 220)
p.cls("kbh", "KebutuhanBahan", ["jumlah_per_mahasiswa: Real"], 1100, 420, 220)
p.stub("mk", "MataKuliah", ["rincian: CM-1"], 1180, 50, 200)
p.stub("per", "Periode", ["master Core"], 1180, 170, 200)
p.stub("psl", "Personel", ["master Core"], 1400, 300, 220)
p.stub("bhn", "Bahan", ["master Core (C-13): kode, nama,", "satuan, jenis [KONFIRMASI kelompok]"], 1400, 420, 240)
p.stub("alt", "Alat", ["master Core (C-10), diisi kelompok", "Aset; hanya dibaca (O, KF-PRK-52)"], 40, 285, 240)
p.enum("e1", "StatusVersiModul", ["draf", "berlaku", "diganti"], 40, 580, 190)
p.enum("e2", "KeputusanKesiapan", ["siap", "siap_setelah_perbaikan", "tunda"], 250, 580, 200)
p.enum("e3", "HasilButir", ["baik", "diperbaiki", "bermasalah"], 40, 720, 190)
p.enum("e4", "KategoriUtilitas", ["jaringan", "listrik", "proyektor_audio"], 250, 720, 200)

p.e("ses-pk", "ses", "pk", ASSOC, "1", "0..1 pemeriksaan", exit=(1, 0.5), entry=(0, 0.3))
p.e("pk-rb", "pk", "rb", GEN, exit=(0, 0.85), entry=(1, 0.3))
p.e("ses-alt", "ses", "alt", DER, None, "* /alat_tidak_tersedia", pts=[(20, 86), (20, 262), (64, 262)],
    exit=(0, 0.5), entry=(0.1, 0))
p.e("pk-bp", "pk", "bp", COMP, "1", "1..* butir", exit=(0.5, 1), entry=(0.5, 0))
p.e("bu-bp", "bu", "bp", GEN, pts=[(135, 380), (382, 380)], exit=(0.5, 0), entry=(0.15, 1))
p.e("bsk-bp", "bsk", "bp", GEN, pts=[(350, 380), (452, 380)], exit=(0.5, 0), entry=(0.4, 1))
p.e("bbh-bp", "bbh", "bp", GEN, pts=[(585, 380), (522, 380)], exit=(0.5, 0), entry=(0.65, 1))
p.e("bsw-bp", "bsw", "bp", GEN, pts=[(777, 380), (592, 380)], exit=(0.3, 0), entry=(0.9, 1))
p.e("bsw-ksw", "bsw", "ksw", ASSOC, "*", "1 kebutuhan", exit=(0.5, 0), entry=(0.42, 1))
p.e("bbh-kbh", "bbh", "kbh", ASSOC, "*", "1 kebutuhan", pts=[(1060, 513), (1060, 445)], exit=(1, 0.85), entry=(0, 0.5))
p.e("bbh-sub", "bbh", "sub", COMP, "1", "0..1 substitusi", exit=(0.5, 1), entry=(0.5, 0))
p.e("sub-pst", "sub", "pst", COMP, "1", "0..1 persetujuan", exit=(0.5, 1), entry=(0.5, 0))
p.e("sub-bhn", "sub", "bhn", ASSOC, "*", "1 bahan_pengganti", pts=[(1520, 612)], exit=(1, 0.5), entry=(0.5, 1))
p.e("pst-psl", "pst", "psl", ASSOC, "*", "1 penyetuju", pts=[(1660, 765), (1660, 325)], exit=(1, 0.5), entry=(1, 0.5))
p.e("vm-mk", "vm", "mk", ASSOC, "{ordered} * versi", "1 mata_kuliah", exit=(1, 0.15), entry=(0, 0.3))
p.e("mk-vmb", "mk", "vm", DER, None, "0..1 /versi_berlaku [periode]", exit=(0, 0.92), entry=(1, 0.45))
p.e("vm-per", "vm", "per", ASSOC, "*", "1", exit=(1, 0.85), entry=(0, 0.5))
p.e("vm-psl", "vm", "psl", ASSOC, "*", "1 penerbit", pts=[(958, 30), (1510, 30)], exit=(0.85, 0), entry=(0.5, 0))
p.e("vm-ksw", "vm", "ksw", COMP, "1", "* software", exit=(0.3, 1), entry=(0.38, 0))
p.e("vm-kbh", "vm", "kbh", COMP, "1", "* bahan", pts=[(888, 220), (1210, 220)], exit=(0.6, 1), entry=(0.5, 0))
p.e("kbh-bhn", "kbh", "bhn", ASSOC, "*", "1 bahan", exit=(1, 0.5), entry=(0, 0.4))

ny = 880
p.v("n1", LEG, NOTE, 40, ny, 640, 125)
p.v("n2", "<b>Keputusan pemodelan</b><br>"
    "• <b>Generalisasi butir</b> (§9.2.1): tiap jenis butir punya atribut sendiri, dan butir tidak berganti jenis. "
    "Tanpa subkelas, atribut seperti <code>lisensi_sah</code> atau <code>berlabel</code> menjadi opsional bergantung kategori (§11.2).<br>"
    "• <b>SubstitusiBahan</b> dan <b>PersetujuanSubstitusi</b> = kejadian (§9.3.2); <code>/status_persetujuan</code> "
    "= disetujui bila ada persetujuan.<br>"
    "• <b>KebutuhanBahan → Bahan</b> = <i>specification class</i> (§11.3): nama dan satuan diambil dari master Bahan Core.<br>"
    "• <code>/versi_berlaku [periode]</code> = versi berstatus berlaku untuk periode itu; diganti oleh versi baru "
    "(<i>superseding</i>, §11.9.2; AB-PRK-07).", NOTE, 700, ny, 560, 150)
p.v("n3", "<b>Turunan dan invarian</b><br>"
    "• <code>/tepat_waktu</code> = waktu_periksa &lt; sesi.tanggal + sesi.jam.awal (AB-PRK-13, PKG-16 S1).<br>"
    "• ButirStasiunKerja <code>/jumlah_dibutuhkan</code> = sesi.kelas.jumlah_mahasiswa; ButirBahan = "
    "kebutuhan.jumlah_per_mahasiswa × jumlah mahasiswa.<br>"
    "• Butir software dan bahan dibentuk dari /versi_berlaku pada tanggal sesi (AB-PRK-14).<br>"
    "• keputusan = siap ⇒ tidak ada butir bermasalah dan semua substitusi disetujui (AB-PRK-15, 16).<br>"
    "• VersiModul: berkas atau tautan_leads terisi; nomor_versi unik per (MK, periode) (AB-PRK-08).<br>"
    "• penyetuju = dosen kelas sesi itu; penerbit = dosen pengampu MK (AB-PRK-09, 16).<br>"
    "• (O) Sesi <code>/alat_tidak_tersedia</code> = alat di ruang sesi yang tidak tersedia untuk sesi itu menurut master Alat Core; "
    "<code>/jumlah_pc_tersedia</code> = jumlah PC di ruang sesi yang tersedia. Hanya peringatan dan isian awal "
    "<code>jumlah_berfungsi</code>; hasil butir tetap dari laboran, status alat tidak diubah (AB-PRK-14, KF-PRK-52).",
    NOTE, 1280, ny, 420, 260)
p.v("n4", SRC, NOTE, 40, 1085, 1220, 42)
pages.append((p, 1720, 1170))

# ============================================================ CM-3
p = Page(3, pname(3, "Pelaksanaan Sesi dan Penilaian"),
         "CM-3 · Conceptual model: pelaksanaan sesi (PKG-18) dan penilaian individual (PKG-19)")
p.stub("ses", "Sesi", ["rincian: CM-1"], 40, 60, 240)
p.stub("pgs", "BarisPenugasan", ["modul SDM (PKG-04), baris Surat Tugas:", "peran, rentang berlaku;",
                                 "asisten → kelas, laboran → ruang"], 40, 170, 240)
p.stub("psl", "Personel", ["master Core"], 40, 420, 240)
p.cls("jur", "JurnalSesi", ["jam_aktual: Interval&lt;Jam&gt;", "topik: Text", "jumlah_hadir: Natural",
                            "tautan_presensi_simpel: URL [0..1]", "kendala: Text [0..1]", "/status: {draf, terkirim}",
                            "/durasi_memenuhi: Boolean"], 400, 50, 300)
p.stub("rb", "RekamanBukti", ["abstrak: tanggal, bukti [*], keterangan;", "peran pelapor. CM-1 Tata Kelola"], 800, 50, 260)
p.stub("vm", "VersiModul", ["rincian: CM-2"], 800, 180, 260)
p.cls("krm", "PengirimanJurnal", ["waktu_kirim: DateTime", "/terlambat: Boolean (O)"], 340, 290, 220)
p.cls("pre", "PresensiPetugas", ["peran: PeranPetugas", "kehadiran: Kehadiran", "/sesuai_penugasan: Boolean (O)"],
      580, 290, 250)
p.cls("log", "EntriLogBook", ["waktu: Jam", "uraian: Text"], 850, 290, 200)
p.stub("kls", "Kelas", ["rincian: CM-1"], 40, 600, 240)
p.cls("pnk", "PenilaianKelas", ["tautan_leads: URL", "/ada_rubrik: Boolean", "/berbukti: Boolean"], 400, 590, 300)
p.cls("bn", "BarisNilai (O)", ["nim: String", "jumlah_tugas_individual: Natural", "nilai_akhir: Real",
                                "ada_umpan_balik: Boolean", "remedial: Boolean", "/lengkap: Boolean (P1–P4)"],
      400, 760, 300)
p.cls("bk", "BerkasNilai (O)", ["waktu_impor: DateTime", "berkas: Berkas"], 800, 760, 240)
p.cls("pgt", "PengaturanPraktikum", ["ambang_durasi: Persen", "batas_hari_jurnal: Natural", "sesi_daring_sah: Boolean",
                                     "batas_lulus: Real = 60"], 1160, 290, 260, "c", "«singleton»")
p.enum("e1", "PeranPetugas", ["dosen", "laboran", "asisten"], 1160, 460, 190)
p.enum("e2", "Kehadiran", ["penuh", "sebagian", "tidak"], 1370, 460, 190)

p.e("ses-jur", "ses", "jur", ASSOC, "1", "0..1 jurnal", exit=(1, 0.5), entry=(0, 0.25))
p.e("jur-rb", "jur", "rb", GEN, exit=(1, 0.12), entry=(0, 0.35))
p.e("jur-vm", "jur", "vm", ASSOC, "*", "1 versi_modul_dipakai", exit=(1, 0.8), entry=(0, 0.5))
p.e("jur-krm", "jur", "krm", COMP, "1", "0..1 pengiriman", exit=(0.1, 1), entry=(0.4, 0))
p.e("jur-pre", "jur", "pre", COMP, "1", "1..* presensi", exit=(0.6, 1), entry=(0.25, 0))
p.e("jur-log", "jur", "log", COMP, "1", "{ordered} 1..* log_book", pts=[(670, 250), (910, 250)], exit=(0.9, 1), entry=(0.3, 0))
p.e("krm-psl", "krm", "psl", ASSOC, "*", "1 pengirim", pts=[(310, 322), (310, 435)], exit=(0, 0.5), entry=(1, 0.3))
p.e("pre-psl", "pre", "psl", ASSOC, "*", "1 petugas", pts=[(655, 470)], exit=(0.3, 1), entry=(1, 0.9))
p.e("ses-ptg", "ses", "psl", DER, None, "* /petugas_ditugaskan", pts=[(290, 108), (290, 400), (250, 400)],
    exit=(1, 0.75), entry=(0.875, 0))
p.e("pgs-psl", "pgs", "psl", ASSOC, "*", "1 petugas", exit=(0.5, 1), entry=(0.5, 0))
p.e("pgs-kls", "pgs", "kls", ASSOC, "*", "0..1 kelas_sasaran", pts=[(20, 210), (20, 570), (88, 570)],
    exit=(0, 0.5), entry=(0.2, 0))
p.e("kls-pnk", "kls", "pnk", ASSOC, "1", "0..1 penilaian", exit=(1, 0.5), entry=(0, 0.4))
p.e("pnk-rb", "pnk", "rb", GEN, pts=[(1100, 610), (1100, 87)], exit=(1, 0.2), entry=(1, 0.45))
p.e("pnk-bn", "pnk", "bn", COMP, "1", "* baris", exit=(0.5, 1), entry=(0.5, 0))
p.e("pnk-bk", "pnk", "bk", COMP, "1", "{ordered} * berkas", pts=[(920, 654)], exit=(1, 0.8), entry=(0.5, 0))

ny = 920
p.v("n1", LEG, NOTE, 40, ny, 640, 125)
p.v("n2", "<b>Keputusan pemodelan</b><br>"
    "• <b>PengirimanJurnal</b> = kejadian (§9.3.2): jurnal draf belum punya waktu kirim dan pengirim. "
    "<code>/status</code> = terkirim bila ada pengiriman.<br>"
    "• Foto kegiatan = <code>bukti</code> warisan RekamanBukti. Presensi petugas merujuk Personel (kontrak Core I-8).<br>"
    "• <b>BerkasNilai {ordered}</b> = riwayat impor (pola <i>history</i>, §11.12.2): baris nilai diganti saat impor "
    "ulang, berkas lama tetap ada (AB-PRK-24). NIM tanpa nama.<br>"
    "• <b>PengaturanPraktikum</b> = variabel sistem satu rekaman (§8.2.2), dibaca oleh atribut turunan; tidak berasosiasi.",
    NOTE, 700, ny, 560, 150)
p.v("n3", "<b>Turunan dan invarian</b><br>"
    "• <code>/petugas_ditugaskan</code> (Sesi) = personel pada BarisPenugasan dari Surat Tugas disahkan yang berlaku "
    "pada sesi.tanggal: asisten lewat sesi.kelas, laboran lewat sesi.ruang (SDM KF-SDM-10, 12).<br>"
    "• <code>/berasisten</code> (Sesi) = ada asisten di /petugas_ditugaskan. Dosen dibaca dari Kelas.dosen.<br>"
    "• <code>/durasi_memenuhi</code> = durasi jam_aktual ≥ ambang_durasi × durasi sesi.jam (AB-PRK-22).<br>"
    "• <code>/terlambat</code> = waktu_kirim &gt; sesi.tanggal + batas_hari_jurnal (AB-PRK-21).<br>"
    "• <code>/sesuai_penugasan</code> = petugas ∈ sesi./petugas_ditugaskan (AB-PRK-20).<br>"
    "• Pengiriman hanya bila presensi dosen dan laboran (+ asisten bila berasisten), jumlah_hadir, versi modul, "
    "≥ 1 log book (AB-PRK-19).<br>"
    "• <code>/ada_rubrik</code> = /versi_berlaku MK kelas punya rubrik; <code>/berbukti</code> = tautan_leads ∧ "
    "/ada_rubrik (AB-PRK-33).<br>"
    "• <code>/lengkap</code> = P1–P4 dengan batas_lulus (AB-PRK-25). nim unik per penilaian.",
    NOTE, 1280, ny, 440, 260)
p.v("n4", SRC, NOTE, 40, 1150, 1220, 42)
pages.append((p, 1760, 1240))

# ============================================================ CM-4
p = Page(4, pname(4, "Survei Kepuasan Pengguna"),
         "CM-4 · Conceptual model: survei kepuasan pengguna (PKG-20)")
p.stub("per", "Periode", ["master Core"], 40, 60, 220)
p.cls("pts", "PenetapanSurvei", ["tanggal: Date"], 40, 180, 220)
p.stub("psl", "Personel", ["master Core"], 80, 860, 220)
p.cls("srv", "Survei", ["judul: String", "jenis_responden: JenisResponden", "populasi: Natural",
                        "target_response_rate: Persen", "masa_buka: Interval&lt;Date&gt;", "/status: StatusSurvei",
                        "/status_buka: {belum_dibuka, dibuka,", "&nbsp;&nbsp;&nbsp;ditutup}", "/jumlah_responden: Natural",
                        "/response_rate: Persen", "/kriteria_tertinggi: Natural (0–4)"], 400, 60, 320)
p.cls("bs", "ButirSurvei", ["urutan: Natural", "pertanyaan: Text", "jenis: JenisButir", "aspek: AspekLayanan",
                            "/rerata: Real"], 40, 330, 280)
p.cls("rsp", "Respons", ["waktu: DateTime"], 420, 380, 240)
p.cls("jwb", "Jawaban", [], 420, 500, 240, "abs")
p.cls("jsk", "JawabanSkala", ["nilai: Natural (1–5)"], 300, 640, 200)
p.cls("jtb", "JawabanTerbuka", ["teks: Text"], 540, 640, 200)
p.cls("ev", "EvaluasiSurvei", [], 860, 120, 240)
p.stub("rb", "RekamanBukti", ["abstrak: tanggal, bukti [*], keterangan;", "peran pelapor. CM-1 Tata Kelola"], 1200, 30, 260)
p.cls("ksa", "KesimpulanAspek", ["aspek: AspekLayanan", "kesimpulan: Text"], 1200, 160, 240)
p.cls("rtl", "RencanaTindakLanjut", ["aspek: AspekLayanan", "prioritas: Prioritas", "tindakan: Text", "tenggat: Date",
                                     "/rerata_sebelum: Real", "/rerata_sesudah: Real"], 860, 300, 300)
p.cls("pe", "PenilaianEfektivitas", ["tanggal: Date", "efektif: TingkatEfektivitas", "catatan: Text [0..1]"],
      1000, 520, 260)
p.enum("e1", "AspekLayanan", ["alat", "bahan", "layanan", "keselamatan", "akses", "pengalaman_belajar"], 1310, 280, 200)
p.enum("e2", "StatusSurvei", ["draf", "ditetapkan", "dievaluasi", "siklus_selesai"], 1310, 440, 200)
p.enum("e3", "JenisButir", ["skala", "terbuka"], 1310, 570, 200)
p.enum("e4", "Prioritas", ["tinggi", "sedang", "rendah"], 1310, 670, 200)
p.enum("e5", "TingkatEfektivitas", ["ya", "sebagian", "tidak"], 1540, 280, 200)
p.enum("e6", "JenisResponden", ["praktikan", "dosen", "asisten"], 1540, 400, 200)

p.e("srv-per", "srv", "per", ASSOC, "*", "1", exit=(0, 0.13), entry=(1, 0.5))
p.e("srv-pts", "srv", "pts", COMP, "1", "0..1 penetapan", exit=(0, 0.66), entry=(1, 0.5))
p.e("pts-psl", "pts", "psl", ASSOC, "*", "1 penetap", pts=[(20, 205), (20, 885)], exit=(0, 0.5), entry=(0, 0.5))
p.e("srv-next", "srv", "srv", DER, None, "0..1 /survei_berikutnya", pts=[(624, 30), (704, 30)], exit=(0.7, 0), entry=(0.95, 0))
p.e("srv-bs", "srv", "bs", COMP, "1", "{ordered} 1..* butir", pts=[(432, 290), (180, 290)], exit=(0.1, 1), entry=(0.5, 0))
p.e("srv-rsp", "srv", "rsp", ASSOC, "1", "* respons", exit=(0.4, 1), entry=(0.45, 0))
p.e("rsp-jwb", "rsp", "jwb", COMP, "1", "1..* jawaban", exit=(0.5, 1), entry=(0.5, 0))
p.e("jsk-jwb", "jsk", "jwb", GEN, exit=(0.5, 0), entry=(0.3, 1))
p.e("jtb-jwb", "jtb", "jwb", GEN, exit=(0.5, 0), entry=(0.7, 1))
p.e("jwb-bs", "jwb", "bs", ASSOC, "*", "1 butir", pts=[(180, 532)], exit=(0, 0.5), entry=(0.5, 1))
p.e("srv-ev", "srv", "ev", ASSOC, "1", "0..1 evaluasi", exit=(1, 0.42), entry=(0, 0.5))
p.e("ev-rb", "ev", "rb", GEN, pts=[(1150, 130), (1150, 62)], exit=(1, 0.25), entry=(0, 0.5))
p.e("ev-ksa", "ev", "ksa", COMP, "1", "1..* kesimpulan", pts=[(1170, 147), (1170, 192)], exit=(1, 0.75), entry=(0, 0.5))
p.e("ev-rtl", "ev", "rtl", COMP, "1", "1..* rtl", exit=(0.5, 1), entry=(0.4, 0))
p.e("rtl-pe", "rtl", "pe", COMP, "1", "0..1 penilaian", exit=(0.7, 1), entry=(0.27, 0))
p.e("rtl-psl", "rtl", "psl", ASSOC, "*", "1 pic", pts=[(920, 880)], exit=(0.2, 1), entry=(1, 0.4))
p.e("pe-psl", "pe", "psl", ASSOC, "*", "1 penilai", pts=[(1130, 902)], exit=(0.5, 1), entry=(1, 0.85))

ny = 950
p.v("n1", LEG, NOTE, 40, ny, 640, 125)
p.v("n2", "<b>Keputusan pemodelan</b><br>"
    "• <b>Respons tanpa asosiasi ke Personel</b>: anonim (AB-PRK-28, KNF-PRK-04).<br>"
    "• <b>Jawaban</b> abstrak menggeneralisasi asosiasi ke ButirSurvei; skala dan terbuka punya atribut berbeda (§9.2.1).<br>"
    "• <b>PenetapanSurvei</b>, <b>EvaluasiSurvei</b>, <b>PenilaianEfektivitas</b> = kejadian (§9.3.2). "
    "<code>/status</code> Survei = siklus_selesai bila setiap RTL dinilai; dievaluasi bila ada evaluasi; ditetapkan bila "
    "ada penetapan; selain itu draf. Pembatalan penetapan (O) menghapus PenetapanSurvei.<br>"
    "• <code>/status_buka</code> dari masa_buka dan hari ini (§9.3.1).", NOTE, 700, ny, 560, 150)
p.v("n3", "<b>Turunan dan invarian</b><br>"
    "• <code>/response_rate</code> = /jumlah_responden ÷ populasi; <code>/rerata</code> = rerata JawabanSkala butir itu.<br>"
    "• <code>/survei_berikutnya</code> = survei periode sesudahnya dengan jenis_responden sama.<br>"
    "• RTL <code>/rerata_sebelum</code>/<code>/rerata_sesudah</code> = rerata aspek RTL di survei ini / survei berikutnya (AB-PRK-30).<br>"
    "• Penetapan: tiap aspek ≥ 1 butir skala, ≥ 1 butir terbuka, populasi &gt; 0, target terisi, "
    "penetapan.tanggal &lt; masa_buka.awal, penetap berwenang (AB-PRK-26).<br>"
    "• Respons hanya dalam masa_buka (AB-PRK-28). Evaluasi setelah masa_buka.akhir (AB-PRK-29).<br>"
    "• <code>/kriteria_tertinggi</code> = K1–K4 berurutan (AB-PRK-34).", NOTE, 1280, ny, 460, 200)
p.v("n4", SRC, NOTE, 40, 1165, 1220, 42)
pages.append((p, 1780, 1230))

with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
