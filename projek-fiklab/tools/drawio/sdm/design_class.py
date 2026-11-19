"""Design class diagram modul SDM & Kompetensi (Langkah 10), 4 halaman + halaman catatan.

Fungsi gambar dan gaya disalin dari contoh-tata-kelola/design_class.py versi `main` (polos hitam-putih);
yang diganti hanya data dan prefiks ID (sdm-). Jenis kelas dibedakan lewat stereotype:
«AbstractModel» (nama miring) = mixin, «Odoo» = model bawaan, «Core» = master bersama labfik_core.

Jalankan:
    python -I projek-fiklab/tools/drawio/sdm/design_class.py projek-fiklab/rancangan/class-sdm.drawio
    python -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/class-sdm.drawio sdm-
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
LH = 15


def esc(s):
    return escape(s, {'"': "&quot;"})


FONT = "fontFamily=Times New Roman;"
PLAIN = "fillColor=#FFFFFF;strokeColor=#000000;swimlaneFillColor=#FFFFFF;" + FONT
FILL = {k: PLAIN for k in ("c", "mixin", "odoo", "core", "stub", "new")}
TXT = ("text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
       "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;" + FONT)
SEP = ("line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;"
       "rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;")
GEN = "endArrow=block;endFill=0;endSize=14;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#000000;"
COMP = "endArrow=none;startArrow=diamondThin;startFill=1;startSize=16;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#000000;fontSize=10;" + FONT
NAV = "endArrow=open;endFill=0;endSize=10;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#000000;fontSize=10;" + FONT
DER = "endArrow=open;endFill=0;endSize=10;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#000000;dashed=1;fontSize=10;" + FONT
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"


def height(title, attrs, methods):
    start = 10 + 15 * (title.count("<br>") + 1)
    return start + max(1, len(attrs)) * LH + 8 + ((8 + len(methods) * LH + 8) if methods else 0)


class Page:
    def __init__(self, n, name, title):
        self.P, self.n, self.name, self.cells, self.geo = f"sdm-dcd{n}-", n, name, [], {}
        self.title, self.notes, self.maxx, self.maxy = title, [], 0, 0

    def v(self, id, val, style, x, y, w, h, parent="1"):
        if parent == "1":
            self.maxx, self.maxy = max(self.maxx, x + w), max(self.maxy, y + h)
        par = "1" if parent == "1" else self.P + parent
        self.cells.append(f'<mxCell id="{self.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="{par}">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

    def cls(self, id, title, attrs, methods, x, y, w=280, kind="c"):
        start = 10 + 15 * (title.count("<br>") + 1)
        ah = max(1, len(attrs)) * LH + 8
        mh = len(methods) * LH + 8 if methods else 0
        h = height(title, attrs, methods)
        self.v(id, title, "swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;"
               f"startSize={start};horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;"
               f"marginBottom=0;whiteSpace=wrap;html=1;fontSize=12;{FILL[kind]}", x, y, w, h)
        self.v(id + "-a", "<br>".join(attrs) if attrs else " ", TXT, 0, start, w, ah, parent=id)
        if methods:
            self.v(id + "-s", "", SEP, 0, start + ah, w, 8, parent=id)
            self.v(id + "-m", "<br>".join(methods), TXT, 0, start + ah + 8, w, mh, parent=id)
        self.geo[id] = (x, y, w, h)
        return h

    def e(self, id, s, t, style, src=None, tgt=None, mid=None, exit=None, entry=None, pts=None):
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
        # Nama field + multiplisitas ujung tujuan ditulis di tengah garis (bukan di ujung), supaya label tidak
        # masuk ke dalam kotak saat garis menempel di sisi kotak. Multiplisitas sumber (src) tidak digambar.
        label = mid or tgt or ""
        self.cells.append(f'<mxCell id="{eid}" value="{esc(label)}" style="{st}labelBackgroundColor=#FFFFFF;" edge="1" '
                          f'parent="1" source="{self.P}{s}" target="{self.P}{t}">{geo}</mxCell>')

    def xml(self, w=None, h=None):
        w, h = w or self.maxx + 40, h or self.maxy + 40
        return (f'<diagram id="sdm-dcd{self.n}" name="{esc(self.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" '
                f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w:.0f}" pageHeight="{h:.0f}" '
                'math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")


def am(name):
    return f"«AbstractModel»<br><b><i>{name}</i></b>"


def cm(name, label, inherit=None):
    t = f"<b>{name}</b><br><font style='font-size:10px'>{label}</font>"
    if inherit:
        t += f"<br><font style='font-size:10px'>{{inherit: {inherit}}}</font>"
    return t


def odoo(name, label, ext=None):
    t = f"«Odoo»<br><b>{name}</b><br><font style='font-size:10px'>{label}</font>"
    if ext:
        t += f"<br><font style='font-size:10px'>{{_inherit: {name}}} di {ext}</font>"
    return t


def core(name, label):
    return f"«Core»<br><b>{name}</b><br><font style='font-size:10px'>{label}</font>"


RINCI = "<i>(rincian: kontrak Core)</i>"
LEG = ("<b>Notasi</b> (Wazlawick 2024, §13.6; UML)<br>"
       "• «AbstractModel» (nama miring) = <i>mixin</i> tanpa tabel; segitiga kosong = <code>_inherit = [mixin, …]</code>.<br>"
       "• «Odoo» = model bawaan; <code>{_inherit: …} di labfik_sdm</code> = diperluas modul ini tanpa <code>_name</code> baru. "
       "«Core» = master bersama labfik_core. Model tanpa stereotype = model baru modul SDM.<br>"
       "• Panah terbuka = Many2one/Many2many berarah, label = nama field. Belah ketupat hitam = One2many + Many2one (anak ikut terhapus). "
       "Putus-putus = asosiasi turunan {compute}.<br>"
       "• Field warisan mixin tidak ditulis ulang. <code>+</code> publik, <code>#</code> internal, @model, «override», {hook}.")
SRC = ("Design class diagram (masuk proposal Bab II 2.3). Diturunkan dari conceptual model CM-1–4, katalog operasi SSD, dan "
       "AB-SDM-01–28. Rincian: design-class-sdm.md · Draf 19 Nov 2026 · Zahir")
pages = []

# =================================================================== DCD-1 pewarisan
p = Page(1, "DCD TO-BE (1-4) - Pewarisan dari Core", "DCD 1/4 · Mixin Core yang dipakai, perluasan model Odoo, dan pewarisan model SDM")
p.cls("apv", am("labfik.approval.mixin"),
      ["+ state: Selection {draf, diajukan, disahkan, diganti, dicabut, …}", "+ penyusun_id: hr.employee", "+ berkas_ttd: Binary [0..1]",
       "+ pengesah_id: hr.employee [0..1]", "+ tanggal_sah: Date [0..1]", "+ log_ids: labfik.approval.log [*] {compute}"],
      ["+ action_ajukan()", "+ action_unggah_ttd(berkas)", "+ action_kembalikan(alasan)", "+ action_sahkan(pengesah, tanggal_sah)",
       "+ action_cabut(alasan)", "+ get_kelengkapan(): list", "# _jenis_dokumen(): str {abstract}", "# _cek_kelengkapan(): list {abstract}",
       "# _sebelum_ajukan() {hook}", "# _sebelum_disahkan() {hook}", "# _dokumen_diganti(): recordset {hook}"], 40, 40, 360, "mixin")
p.cls("prd", am("labfik.period.mixin"), ["+ periode_id: labfik.periode", "+ is_berlaku: Boolean {compute}"],
      ["+ berlaku_pada(tanggal): bool"], 440, 40, 260, "mixin")
p.cls("cri", am("labfik.criteria.mixin"), ["+ kriteria_tertinggi: Integer {compute}"],
      ["+ get_kriteria(tanggal_acuan): dict", "# _cek_k1(tanggal) … _cek_k4(tanggal) {abstract}"], 440, 200, 260, "mixin")
p.cls("evi", am("labfik.evidence.mixin"), ["+ tanggal: Date", "+ pelapor_id: hr.employee", "+ bukti_ids: ir.attachment [*]",
                                            "+ keterangan: Text [0..1]"],
      ["+ action_koreksi(nilai, alasan)", "+ unlink() «override» (ditolak)"], 1115, 40, 300, "mixin")
apv_subs = [("st", "labfik.sdm.surat.tugas", "Surat Tugas [T]", "approval", 40),
            ("oto", "labfik.sdm.otorisasi", "Otorisasi [T]", "approval", 260),
            ("rp", "labfik.sdm.rencana.pelatihan", "Rencana Pelatihan [T]", "approval, period, criteria", 480)]
for cid, name, label, inh, x in apv_subs:
    p.cls(cid, cm(name, label, inh), ["<i>(rincian: DCD 2–4)</i>"], [], x, 430, 200 if cid != "rp" else 240)
p.e("g-st", "st", "apv", GEN, exit=(0.5, 0), entry=(0.15, 1))
p.e("g-oto", "oto", "apv", GEN, exit=(0.5, 0), entry=(0.6, 1))
p.e("g-rp-apv", "rp", "apv", GEN, exit=(0.2, 0), entry=(0.95, 1))
p.e("g-rp-prd", "rp", "prd", GEN, exit=(0.85, 0), entry=(0.85, 1), pts=[(684, 400), (721, 400), (721, 170), (661, 170)])
p.e("g-rp-cri", "rp", "cri", GEN, exit=(0.55, 0), entry=(0.5, 1))
p.cls("emp", odoo("hr.employee", "Personel [M]", "labfik_sdm"), ["+ bukti_kompetensi_ids: labfik.sdm.bukti.kompetensi [*]"],
      ["+ punya_kompetensi(kompetensi, tanggal): bool", "+ kompetensi_kurang(tanggal): recordset", "+ memenuhi_syarat_jabatan(tanggal): bool"],
      40, 580, 330, "odoo")
p.cls("job", odoo("hr.job", "Jabatan [M]", "labfik_sdm"), ["+ syarat_kompetensi_ids: labfik.sdm.kompetensi [*]"], [], 400, 580, 320, "odoo")
p.cls("wwn", core("labfik.jabatan.wewenang", "Wewenang Jabatan [M]"),
      ["+ jenis_dokumen: Selection", "&nbsp;&nbsp;+= penugasan_petugas, otorisasi,", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rencana_pelatihan (selection_add)"],
      [], 400, 690, 320, "core")
ev = [("bk", "labfik.sdm.bukti.kompetensi", "Bukti Kompetensi"), ("kbt", "labfik.sdm.kebutuhan.petugas", "Kebutuhan Petugas"),
      ("seb", "labfik.sdm.seleksi", "Seleksi Asisten"), ("ori", "labfik.sdm.orientasi", "Orientasi Petugas (O)"),
      ("ase", "labfik.sdm.asesmen", "Asesmen Keterampilan"), ("evu", "labfik.sdm.evaluasi.otorisasi", "Evaluasi Ulang Otorisasi"),
      ("rls", "labfik.sdm.realisasi.pelatihan", "Realisasi Pelatihan"), ("eve", "labfik.sdm.evaluasi.pelatihan", "Evaluasi Efektivitas")]
for i, (cid, name, label) in enumerate(ev):
    x, y = 780 + (i % 4) * 250, 330 + (i // 4) * 120
    p.cls(cid, cm(name, label + " [T]", "evidence"), [], [], x, y, 220)
    if i < 4:   # baris atas: langsung naik
        p.e(f"g-{cid}", cid, "evi", GEN, exit=(0.5, 0), entry=(0.5, 1))
    else:       # baris bawah: lewat celah antarkolom supaya tidak menembus kotak baris atas
        p.e(f"g-{cid}", cid, "evi", GEN, exit=(0, 0.5), entry=(0.5, 1), pts=[(x - 15, y + 39), (x - 15, 290)])
p.notes.append(("<b>Pewarisan</b><br>• Tiga dokumen SDM mewarisi <code>approval.mixin</code>; Rencana Pelatihan juga <code>period.mixin</code> "
    "(satu rencana per tahun) dan <code>criteria.mixin</code> (K1–K4 PKG-14). Otorisasi <b>tidak</b> memakai period.mixin (K-3).<br>"
    "• Delapan rekaman bukti mewarisi <code>evidence.mixin</code>: tidak dihapus, hanya dikoreksi (AB-SDM-24).<br>"
    "• <code>hr.employee</code> dan <code>hr.job</code> diperluas dari labfik_sdm tanpa <code>_name</code> baru; jenis dokumen wewenang "
    "ditambah lewat <code>selection_add</code>. Core tidak diubah.<br>"
    "• Template Method <code>action_ajukan()</code> / <code>action_sahkan()</code> milik Core tidak di-<i>override</i>; model SDM hanya "
    "mengisi <i>hook</i> (DCD 2–4).", 130))
p.notes.append((SRC, 46))
pages.append(p)

# =================================================================== DCD-2 kompetensi dan penugasan
p = Page(2, "DCD TO-BE (2-4) - Kompetensi dan Penugasan", "DCD 2/4 · Kompetensi, seleksi, dan penugasan petugas (PKG-04)")
p.cls("kom", cm("labfik.sdm.kompetensi", "Kompetensi [M]"),
      ["+ name: Char «unique»", "+ jenis: Selection {pendidikan, keahlian,", "&nbsp;&nbsp;&nbsp;sertifikasi, pelatihan_fungsional}",
       "+ kode_acuan: Char [0..1]", "+ keterangan: Text [0..1]", "+ active: Boolean"],
      ["+ unlink() «override» (AB-SDM-25)"], 40, 40, 300)
p.cls("job", odoo("hr.job", "Jabatan [M]"), [RINCI], [], 40, 300, 220, "odoo")
p.cls("emp", odoo("hr.employee", "Personel [M]"), [RINCI, "+ (perluasan SDM: DCD 1)"], [], 400, 330, 220, "odoo")
p.cls("bk", cm("labfik.sdm.bukti.kompetensi", "Bukti Kompetensi [T]", "evidence"),
      ["+ employee_id: hr.employee", "+ jenis_bukti: Selection {pendidikan, pelatihan,", "&nbsp;&nbsp;&nbsp;sertifikasi, pengalaman, demonstrasi}",
       "+ nomor_dokumen: Char [0..1]", "+ penerbit: Char [0..1]", "+ berlaku_sampai: Date [0..1]", "+ is_berlaku: Boolean {compute}"],
      ["+ berlaku_pada(tanggal): bool (AB-SDM-13)", "# _compute_is_berlaku()"], 400, 40, 320)
p.e("n-job-kom", "job", "kom", NAV, "*", "syarat_kompetensi_ids *", exit=(0.5, 0), entry=(0.3, 1))
p.e("n-bk-kom", "bk", "kom", NAV, "*", "kompetensi_id 1", exit=(0, 0.3), entry=(1, 0.3))
p.e("n-emp-bk", "emp", "bk", COMP, "1", "bukti_kompetensi_ids *", exit=(0.5, 0), entry=(0.5, 1))
p.e("n-emp-job", "emp", "job", NAV, "*", "job_id 0..1", exit=(0, 0.5), entry=(1, 0.5))
p.cls("kbt", cm("labfik.sdm.kebutuhan.petugas", "Kebutuhan Petugas [T]", "evidence"),
      ["+ kelas_id: labfik.kelas", "+ peran: Selection {asisten, laboran}", "+ jumlah_minimal: Integer", "+ dasar_penetapan: Text",
       "<i>_sql_constraints: unique(kelas_id, peran)</i>"],
      ["# _cek_jumlah() @constrains (AB-SDM-14)"], 40, 470, 300)
p.cls("kls", core("labfik.kelas", "Kelas [M]"), [RINCI], [], 40, 800, 200, "core")
p.cls("mk", core("labfik.mata.kuliah", "Mata Kuliah [M]"), [RINCI], [], 300, 800, 200, "core")
p.e("n-kbt-kls", "kbt", "kls", NAV, "*", "kelas_id 1", exit=(0.3, 1), entry=(0.5, 0))
p.cls("seb", cm("labfik.sdm.seleksi", "Seleksi Asisten [T]", "evidence"),
      ["+ employee_id: hr.employee", "+ mata_kuliah_id: labfik.mata.kuliah", "+ periode_id: labfik.periode", "+ nilai_mk: Char",
       "+ skor_wawancara, skor_simulasi, skor_modul: Float", "+ penilai_id: hr.employee",
       "+ keputusan: Selection {lulus, lulus_pengecualian}", "+ alasan_pengecualian: Text [0..1]", "+ penyetuju_id: hr.employee [0..1]",
       "<i>_sql_constraints: unique(employee_id, mata_kuliah_id, periode_id)</i>"],
      ["@model + create(vals) «override»", "# _pastikan_personel(vals) (AB-SDM-15)", "# _cek_pengecualian() @constrains"], 400, 470, 360)
p.e("n-seb-emp", "seb", "emp", NAV, "*", "employee_id 1", exit=(0.4, 0), entry=(0.5, 1))
p.e("n-seb-mk", "seb", "mk", NAV, "*", "mata_kuliah_id 1", exit=(0.2, 1), entry=(0.8, 0))
p.cls("st", cm("labfik.sdm.surat.tugas", "Surat Tugas [T]", "approval"),
      ["+ name: Char «unique»", "+ periode_id: labfik.periode", "+ berkas_komitmen: Binary [0..1] (O)",
       "+ revisi_dari_id: labfik.sdm.surat.tugas [0..1] (O)"],
      ["+ action_buat_revisi() (O)", "# _jenis_dokumen() «override» = penugasan_petugas", "# _cek_kelengkapan() «override» (AB-SDM-02)",
       "# _dokumen_diganti() «override» = revisi_dari_id"], 820, 40, 360)
p.cls("bp", cm("labfik.sdm.penugasan", "Baris Penugasan [T]"),
      ["+ employee_id: hr.employee", "+ peran: Selection {asisten, laboran}", "+ kelas_id: labfik.kelas [0..1]",
       "+ ruang_id: labfik.ruang [0..1]", "+ berlaku_mulai, berlaku_sampai: Date", "+ is_sah: Boolean {compute}"],
      ["+ berlaku_pada(tanggal): bool (AB-SDM-16)", "# _cek_sasaran() @constrains"], 820, 330, 360)
p.e("c-st-bp", "st", "bp", COMP, "1", "penugasan_ids 1..*", exit=(0.5, 1), entry=(0.5, 0))
p.e("n-bp-emp", "bp", "emp", NAV, "*", "employee_id 1", exit=(0, 0.4), entry=(1, 0.5))
p.cls("rng", core("labfik.ruang", "Ruang [M]"), [RINCI], [], 1240, 380, 200, "core")
p.e("n-bp-rng", "bp", "rng", NAV, "*", "ruang_id 0..1", exit=(1, 0.4), entry=(0, 0.5))
p.e("n-bp-kls", "bp", "kls", NAV, "*", "kelas_id 0..1", exit=(0.2, 1), entry=(0.5, 1), pts=[(892, 905), (140, 905)])
p.cls("ori", cm("labfik.sdm.orientasi", "Orientasi Petugas [T] (O)", "evidence"),
      ["+ employee_id: hr.employee", "+ jenis: Selection {orientasi, supervisi}", "+ pelaksana_id: hr.employee"], [], 1240, 560, 300)
p.notes.append(("<b>Kunci</b><br>• Specification class: <code>kompetensi</code> = spesifikasi, <code>bukti.kompetensi</code> = exemplar milik Personel; "
    "syarat jabatan merujuk spesifikasi (<code>hr.job.syarat_kompetensi_ids</code>).<br>"
    "• Pengecualian seleksi (CM) dilebur menjadi field <code>alasan_pengecualian</code> dan <code>penyetuju_id</code> karena multiplisitasnya 0..1 (§13.6).<br>"
    "• Surat Tugas bergaris (K-6): disahkan sekali; baris sah bila suratnya disahkan dan tanggal di rentangnya.<br>"
    "• Orientasi tidak bertaut ke model lain di modul ini; dibaca laporan bukti (KU-3).", 120))
pages.append(p)

# =================================================================== DCD-3 otorisasi
p = Page(3, "DCD TO-BE (3-4) - Otorisasi", "DCD 3/4 · Tugas/alat berkewenangan khusus, asesmen, otorisasi, dan evaluasi ulang (PKG-10)")
p.cls("tk", cm("labfik.sdm.tugas.khusus", "Tugas/Alat Berkewenangan Khusus [M]"),
      ["+ name: Char", "+ jenis: Selection {tugas, alat, software}", "+ lokasi: Char [0..1]",
       "+ kompetensi_ids: labfik.sdm.kompetensi [1..*]", "+ masa_berlaku_bulan: Integer", "+ pelaksana_ids: hr.employee [*]",
       "+ cara_pembatasan: Selection [0..1] (O)", "+ berkas_pembatasan: Binary [0..1] (O)", "+ active: Boolean"],
      ["+ unlink() «override» (AB-SDM-25)"], 40, 40, 330)
p.cls("ase", cm("labfik.sdm.asesmen", "Asesmen Keterampilan [T]", "evidence"),
      ["+ employee_id: hr.employee", "+ tugas_khusus_id: labfik.sdm.tugas.khusus", "+ penilai_id: hr.employee",
       "+ metode: Selection {demonstrasi, uji_praktik, tinjauan_sertifikat}", "+ skor: Float [0..1]", "+ unsur_kritis_terpenuhi: Boolean",
       "+ kesimpulan: Selection {layak, belum_layak}", "+ catatan_pengembangan: Text [0..1]",
       "+ bukti_kompetensi_ids: labfik.sdm.bukti.kompetensi [*]"],
      ["@model + create(vals) «override»", "# _buat_bukti_kompetensi() (AB-SDM-17)"], 460, 40, 380)
p.e("n-ase-tk", "ase", "tk", NAV, "*", "tugas_khusus_id 1", exit=(0, 0.3), entry=(1, 0.3))
p.cls("bk", cm("labfik.sdm.bukti.kompetensi", "Bukti Kompetensi [T]", "evidence"), ["<i>(rincian: DCD 2)</i>"], [], 930, 60, 240)
p.e("c-ase-bk", "ase", "bk", COMP, "0..1 asesmen_id", "bukti_kompetensi_ids *", exit=(1, 0.3), entry=(0, 0.5))
p.cls("oto", cm("labfik.sdm.otorisasi", "Otorisasi [T]", "approval"),
      ["+ employee_id: hr.employee", "+ tugas_khusus_id: labfik.sdm.tugas.khusus", "+ asesmen_id: labfik.sdm.asesmen [0..1]",
       "+ bukti_kompetensi_ids: labfik.sdm.bukti.kompetensi [*]", "+ lingkup: Text", "+ level: Selection {terbimbing, mandiri}",
       "+ supervisor_id: hr.employee [0..1]", "+ berlaku_mulai, berlaku_sampai: Date", "+ is_berlaku: Boolean {compute}"],
      ["+ berlaku_pada(tanggal): bool (AB-SDM-18)", "@model + buat_dari_evaluasi(evaluasi)", "# _onchange_tugas_khusus(): isi berlaku_sampai",
       "# _jenis_dokumen() «override» = otorisasi", "# _cek_kelengkapan() «override» (AB-SDM-03)",
       "# _dokumen_diganti() «override» = otorisasi pasangan sama"], 460, 380, 380)
p.e("n-oto-tk", "oto", "tk", NAV, "*", "tugas_khusus_id 1", exit=(0, 0.25), entry=(0.5, 1))
p.e("n-oto-ase", "oto", "ase", NAV, "*", "asesmen_id 0..1", exit=(0.5, 0), entry=(0.5, 1))
p.e("n-oto-bk", "oto", "bk", NAV, "*", "bukti_kompetensi_ids *", exit=(1, 0.2), entry=(0.5, 1))
p.cls("evu", cm("labfik.sdm.evaluasi.otorisasi", "Evaluasi Ulang Otorisasi [T]", "evidence"),
      ["+ otorisasi_id: labfik.sdm.otorisasi", "+ pemicu: Selection {masa_berlaku_habis, alat_berubah,", "&nbsp;&nbsp;&nbsp;insiden, lama_tidak_aktif, lainnya}",
       "+ status: Selection {terbuka, diputuskan} {compute, store}", "+ keputusan: Selection {diperpanjang, dibatasi,",
       "&nbsp;&nbsp;&nbsp;naik_level, dicabut, tetap_berlaku} [0..1]", "+ hasil: Text [0..1]", "+ penilai_id: hr.employee [0..1]",
       "+ tanggal_keputusan: Date [0..1]", "+ otorisasi_baru_id: labfik.sdm.otorisasi [0..1]"],
      ["+ action_putuskan(keputusan, hasil, penilai, tanggal) (AB-SDM-19)", "# _compute_status()", "# _cek_otorisasi() @constrains"], 930, 380, 380)
p.e("n-evu-oto", "evu", "oto", NAV, "*", "otorisasi_id 1", exit=(0, 0.3), entry=(1, 0.6))
p.e("n-evu-oto2", "evu", "oto", NAV, "0..1", "otorisasi_baru_id 0..1", exit=(0, 0.75), entry=(1, 0.9))
p.cls("emp", odoo("hr.employee", "Personel [M]"), [RINCI], [], 40, 540, 220, "odoo")
p.e("n-oto-emp", "oto", "emp", NAV, "*", "employee_id, supervisor_id", exit=(0, 0.6), entry=(1, 0.5))
p.e("n-tk-emp", "tk", "emp", NAV, "*", "pelaksana_ids *", exit=(0.3, 1), entry=(0.4, 0))
p.notes.append(("<b>Kunci</b><br>• <code>tugas.khusus.pelaksana_ids</code> = penyebut PKG-10 (KB-1). Otorisasi berlaku dihitung dari interval "
    "sendiri (<code>is_berlaku</code>), bukan period.mixin (K-3).<br>"
    "• <code>_dokumen_diganti()</code> mengembalikan otorisasi Disahkan lain untuk pasangan (employee, tugas_khusus) yang sama, "
    "sehingga Template Method Core mengubahnya menjadi Diganti (AB-SDM-10).<br>"
    "• Keputusan evaluasi (konsep kejadian 0..1 di CM) dilebur menjadi field; <code>status</code> dihitung dari ada-tidaknya keputusan.", 120))
pages.append(p)

# =================================================================== DCD-4 pelatihan dan monev
p = Page(4, "DCD TO-BE (4-4) - Pelatihan dan Status Monev", "DCD 4/4 · Rencana, realisasi, evaluasi pelatihan (PKG-14) dan layanan status monev")
p.cls("rp", cm("labfik.sdm.rencana.pelatihan", "Rencana Pelatihan [T]", "approval, period, criteria"),
      ["+ name: Char", "+ kebutuhan_dibekukan: Boolean (readonly)", "+ kebutuhan_ids: labfik.sdm.kebutuhan.pelatihan [*]",
       "+ item_ids: labfik.sdm.item.pelatihan [*]"],
      ["+ action_isi_kebutuhan() (AB-SDM-20)", "# _jenis_dokumen() «override» = rencana_pelatihan",
       "# _cek_kelengkapan() «override» (AB-SDM-04)", "# _sebelum_ajukan() «override»: bekukan kebutuhan",
       "# _sebelum_disahkan() «override»: satu per periode (AB-SDM-12)", "# _cek_k1() … _cek_k4() «override» (AB-SDM-28)"],
      40, 40, 400)
p.cls("kbk", cm("labfik.sdm.kebutuhan.pelatihan", "Kebutuhan Kompetensi [T]"),
      ["+ rencana_id: labfik.sdm.rencana.pelatihan", "+ employee_id: hr.employee", "+ kompetensi_id: labfik.sdm.kompetensi [0..1]",
       "+ tidak_ada_gap: Boolean", "+ sumber: Selection {matriks, tambahan}", "+ keterangan: Text [0..1]"],
      ["# _cek_dibekukan() @constrains"], 540, 40, 360)
p.e("c-rp-kbk", "rp", "kbk", COMP, "1", "kebutuhan_ids 1..*", exit=(1, 0.3), entry=(0, 0.3))
p.cls("itm", cm("labfik.sdm.item.pelatihan", "Item Pelatihan [T]"),
      ["+ rencana_id: labfik.sdm.rencana.pelatihan", "+ kompetensi_id: labfik.sdm.kompetensi", "+ jenis: Selection {diklatfung, bimtek,",
       "&nbsp;&nbsp;&nbsp;sertifikasi, internal}", "+ materi: Text", "+ peserta_ids: hr.employee [1..*]", "+ penyelenggara: Char",
       "+ anggaran: Monetary + currency_id: res.currency", "+ jadwal_mulai, jadwal_selesai: Date", "+ kriteria_keberhasilan: Text",
       "+ status: Selection {rencana, terlaksana, batal}", "+ alasan_batal: Text [0..1] (O)",
       "+ status_evaluasi: Selection {compute}"],
      ["+ action_batalkan(alasan) (O, AB-SDM-22)", "# _compute_status_evaluasi()"], 40, 360, 400)
p.e("c-rp-itm", "rp", "itm", COMP, "1", "item_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.cls("rls", cm("labfik.sdm.realisasi.pelatihan", "Realisasi Pelatihan [T]", "evidence"),
      ["+ item_id: labfik.sdm.item.pelatihan", "+ employee_id: hr.employee", "+ penyelenggara: Char", "+ durasi_jam: Float",
       "+ berkas_sertifikat: Binary [0..1]", "<i>_sql_constraints: unique(item_id, employee_id)</i>"],
      ["@model + create(vals) «override»: item terlaksana", "# _cek_item() @constrains (AB-SDM-21)"], 540, 360, 360)
p.e("n-rls-itm", "rls", "itm", NAV, "*", "item_id 1", exit=(0, 0.4), entry=(1, 0.4))
p.cls("eve", cm("labfik.sdm.evaluasi.pelatihan", "Evaluasi Efektivitas [T]", "evidence"),
      ["+ realisasi_id: labfik.sdm.realisasi.pelatihan «unique»", "+ metode: Selection {asesmen_ulang, penilaian_kinerja}",
       "+ skor_sebelum, skor_sesudah: Float [0..1]", "+ penilai_id: hr.employee", "+ kesimpulan: Selection {efektif, perlu_pengembangan}",
       "+ peningkatan_layanan: Text [0..1]", "+ tindak_lanjut: Text [0..1]"],
      ["@model + create(vals) «override»", "# _buat_bukti_kompetensi() (AB-SDM-23)"], 540, 640, 360)
p.e("n-eve-rls", "eve", "rls", NAV, "0..1", "realisasi_id 1", exit=(0.5, 0), entry=(0.5, 1))
p.cls("bk", cm("labfik.sdm.bukti.kompetensi", "Bukti Kompetensi [T]", "evidence"), ["<i>(rincian: DCD 2)</i>"], [], 1000, 680, 240)
p.e("c-eve-bk", "eve", "bk", NAV, "0..1 evaluasi_pelatihan_id", "bukti_kompetensi 0..1", exit=(1, 0.5), entry=(0, 0.5))
p.cls("mon", am("labfik.sdm.monev"),
      ["<i>(layanan tanpa tabel; Status Monev SDM [R])</i>"],
      ["+ get_status(periode, tanggal_acuan): dict", "@model + status_sesi(periode): list (AB-SDM-26)",
       "@model + status_pasangan(tanggal): list (AB-SDM-27)", "@model # hitung_skor(persentase): int",
       "+ get_unit(unit, tanggal_acuan): dict", "+ action_laporan_bukti(): report"], 1000, 40, 360, "mixin")
p.e("d-mon-rp", "mon", "rp", DER, None, "get_kriteria() (AB-SDM-28)", exit=(0, 0.85), entry=(1, 0.15),
    pts=[(960, 160), (960, 20), (470, 20), (470, 62)])
p.cls("ses", core("labfik.sesi", "Sesi [T]"), [RINCI, "+ state = terlaksana"], [], 1000, 330, 220, "core")
p.e("d-mon-ses", "mon", "ses", DER, None, "membaca sesi terlaksana", exit=(0.3, 1), entry=(0.5, 0))
p.notes.append(("<b>Kunci</b><br>• Template Method Core: <code>_sebelum_ajukan()</code> membekukan kebutuhan (AB-SDM-04); "
    "<code>_sebelum_disahkan()</code> menolak rencana kedua untuk periode yang sama (AB-SDM-12).<br>"
    "• <code>criteria.mixin.get_kriteria()</code> memanggil <code>_cek_k1()–_cek_k4()</code> berurutan; berhenti di kriteria pertama yang gagal.<br>"
    "• <code>labfik.sdm.monev</code> mendelegasikan perhitungan: PKG-04 ke <code>penugasan.berlaku_pada()</code> dan "
    "<code>hr.employee.memenuhi_syarat_jabatan()</code>, PKG-10 ke <code>otorisasi.berlaku_pada()</code>, PKG-14 ke "
    "<code>get_kriteria()</code>. Tidak menyimpan data.<br>"
    "• PembatalanItem (CM) dilebur menjadi <code>alasan_batal</code> + status <i>batal</i>.", 140))
pages.append(p)

# =================================================================== halaman catatan
c = Page("-notes", "Catatan DCD TO-BE (bahan kerja)", "")
c.P = "sdm-dcd-notes-"
c.v("title", "Catatan design class diagram modul SDM (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 10, 1300, 34)
c.v("legend", LEG, NOTE, 40, 56, 1300, 110)
y = 186
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
