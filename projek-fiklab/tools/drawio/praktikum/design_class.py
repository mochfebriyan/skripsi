"""Design class diagram modul Pelaksanaan Praktikum (langkah 10), 5 halaman.

Mesin gambar disalin dari contoh-tata-kelola/design_class.py (branch febriyan-skripsi); prefiks (prk-dcd), nama halaman,
penempatan label ujung garis (di luar kotak, menurut sisi keluar/masuk), titik belok, dan data diganti.
Pemakaian: python -X utf8 -I design_class.py projek-fiklab/rancangan/class-praktikum.drawio
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
LH = 15
NPAGE = 5


def esc(s):
    return escape(s, {'"': "&quot;"})


FILL = {"c": "fillColor=#FFFFFF;strokeColor=#333333;", "mixin": "fillColor=#E1D5E7;strokeColor=#9673A6;",
        "odoo": "fillColor=#F5F5F5;strokeColor=#666666;", "core": "fillColor=#F5F5F5;strokeColor=#666666;dashed=1;",
        "new": "fillColor=#FFFFFF;strokeColor=#9B2C44;strokeWidth=2;"}
TXT = ("text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
       "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;")
SEP = ("line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;"
       "rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;")
GEN = "endArrow=block;endFill=0;endSize=14;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#6C4A87;"
EXT = "endArrow=block;endFill=0;endSize=14;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#9B2C44;dashed=1;fontSize=10;"
COMP = ("endArrow=none;startArrow=diamondThin;startFill=1;startSize=16;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;"
        "strokeColor=#333333;fontSize=10;")
NAV = "endArrow=open;endFill=0;endSize=10;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#555555;fontSize=10;"
DER = "endArrow=open;endFill=0;endSize=10;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#555555;dashed=1;fontSize=10;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"


def height(title, attrs, methods):
    start = 10 + 15 * (title.count("<br>") + 1)
    return start + max(1, len(attrs)) * LH + 8 + ((8 + len(methods) * LH + 8) if methods else 0)


class Page:
    def __init__(self, n, isi, title):
        self.P, self.n, self.cells, self.geo = f"prk-dcd{n}-", n, [], {}
        self.name = f"DCD TO-BE ({n}-{NPAGE}) - {isi}"
        self.v("title", title, TITLE, 40, 6, 1700, 30)

    def v(self, id, val, style, x, y, w, h, parent="1"):
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

    def pt(self, id, fx, fy):
        x, y, w, h = self.geo[id]
        return (round(x + w * fx), round(y + h * fy))

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
                f'parent="{eid}"><mxGeometry x="{xpos}" relative="1" as="geometry"><mxPoint x="{dx}" y="{dy}" '
                f'as="offset"/></mxGeometry></mxCell>')

    def xml(self, w, h):
        return (f'<diagram id="prk-dcd{self.n}" name="{esc(self.name)}"><mxGraphModel dx="1600" dy="900" grid="1" '
                f'gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
                f'pageWidth="{w:.0f}" pageHeight="{h:.0f}" math="0" shadow="0"><root><mxCell id="0"/>'
                '<mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")


def f10(t, color=None):
    c = f" color='{color}'" if color else ""
    return f"<font style='font-size:10px'{c}>{t}</font>"


def am(name, label=None):
    return "«AbstractModel»<br>" + f"<b><i>{name}</i></b>" + (f"<br>{f10(label)}" if label else "")


def cm(name, label, inherit=None, stereo=None):
    t = (f"{stereo}<br>" if stereo else "") + f"<b>{name}</b><br>{f10(label)}"
    if inherit:
        t += "<br>" + f10(f"{{inherit: {inherit}}}", "#6C4A87")
    return t


def odoo(name, label, ext=None):
    t = f"«Odoo»<br><b>{name}</b><br>{f10(label)}"
    if ext:
        t += "<br>" + f10(ext, "#6C4A87")
    return t


def core(name, label, owner="«Core»"):
    return f"{owner}<br><b>{name}</b><br>{f10(label)}"


def stack(page, columns, specs, top=60, gap=50):
    bottoms = []
    for x, ids in columns:
        y = top
        for cid in ids:
            t, a, m, w, kind = specs[cid]
            y += page.cls(cid, t, a, m, x, y, w, kind) + gap
        bottoms.append(y)
    return max(bottoms)


LEG = ("<b>Notasi</b> (Wazlawick 2024, §13.6; CLAUDE.md bagian 5)<br>"
       "• Ungu «AbstractModel» (nama miring) = <i>mixin</i> tanpa tabel; segitiga kosong ungu = <code>_inherit = [mixin, …]</code>.<br>"
       "• «Odoo» abu-abu = model bawaan; «Core» / «SDM» abu-abu putus-putus = model addon lain yang dipakai. "
       "Tepi merah = model hasil desain tanpa padanan 1:1 di CM. Segitiga merah putus-putus = <code>_inherit</code> tanpa "
       "<code>_name</code> baru (perluasan model milik addon lain).<br>"
       "• Panah terbuka = Many2one/Many2many berarah, label = nama field + multiplisitas. Belah ketupat hitam = One2many + "
       "Many2one (anak ikut terhapus). Putus-putus = field/rujukan <code>compute</code> atau pemanggilan method.<br>"
       "• Atribut bertipe hanya untuk model bawaan Odoo (hr.employee, ir.attachment, survey.*). Field warisan mixin tidak ditulis ulang.<br>"
       "• <code>+</code> publik (<code>action_*</code>, <code>get_*</code>), <code>#</code> internal (<code>_…</code>), @model, "
       "@constrains, «override», {abstract}, {hook}. (O) = lapis Pelengkap.")
SRC = ("Design class diagram (masuk proposal Bab II 2.3). Diturunkan dari conceptual model CM-1–4, katalog operasi SSD, "
       "AB-PRK-01–34, kontrak Core 16 Nov 2026. Rincian: rancangan/design-class-praktikum.md · Draf 16 Nov 2026 · Herrens")
pages = []

APV = (am("labfik.approval.mixin", "Core · rincian: DCD Tata Kelola"),
       ["+ state: Selection {draf, diajukan, disahkan, …}", "+ berkas_ttd, pengesah_id, tanggal_sah"],
       ["+ action_ajukan(), action_sahkan(pengesah, tgl)", "# _jenis_dokumen(): str {abstract}",
        "# _cek_kelengkapan(): list {abstract}", "# _dokumen_diganti(): recordset {hook}"], 330, "mixin")
EVI = (am("labfik.evidence.mixin", "Core · rincian: DCD Tata Kelola"),
       ["+ tanggal: Date", "+ pelapor_id: hr.employee", "+ bukti_ids: ir.attachment [*]", "+ keterangan: Text [0..1]"],
       ["+ action_koreksi(nilai, alasan)", "+ unlink() «override» (ditolak, AB-PRK-31)", "# _boleh_dikoreksi(): bool {hook}"],
       320, "mixin")

# ===================================================================== DCD-1
p = Page(1, "Jadwal dan Sesi", "DCD 1/5 · Mata kuliah, kelas, sesi (labfik_core) dan penetapan jadwal, impor (labfik_praktikum) · PKG-15")
S = {
    "mk": (core("labfik.mata.kuliah", "Mata Kuliah [M]"),
           ["+ kode: Char «unique»", "+ name: Char", "+ prodi: Selection", "+ semester: Integer", "+ active: Boolean = True"],
           ["+ unlink() «override» (AB-PRK-31)"], 300, "core"),
    "kls": (core("labfik.kelas", "Kelas [M]"),
            ["+ name: Char", "+ jumlah_mahasiswa: Integer", "+ dosen_koordinator_id: hr.employee [0..1]",
             "+ dosen_ids: hr.employee [1..*]", "+ active: Boolean = True",
             "<i>_sql_constraints: unique(mata_kuliah_id,</i>", "<i>&nbsp;&nbsp;&nbsp;periode_id, name)</i>"],
            ["+ unlink() «override» (AB-PRK-31)"], 300, "core"),
    "per": (core("labfik.periode", "Periode [M]"), ["+ name: Char", "+ tanggal_mulai, tanggal_selesai: Date"], [], 300, "core"),
    "ses": (core("labfik.sesi", "Sesi Praktikum [T] · labfik_core"),
            ["+ pertemuan_ke: Integer", "+ jenis_pertemuan: Selection {praktikum, uts, uas}",
             "+ moda: Selection {luring, daring} = luring", "+ tanggal: Date", "+ jam_mulai: Float (widget jam)",
             "+ jam_selesai: Float (widget jam)", "+ state: Selection {terjadwal, terlaksana,", "&nbsp;&nbsp;&nbsp;batal} = terjadwal",
             "+ is_diganti: Boolean {compute}"],
            ["# _cek_jam() @constrains (AB-PRK-18)", "# _cek_pertemuan_unik() @constrains (AB-PRK-02)",
             "# _compute_is_diganti()"], 340, "core"),
    "rng": (core("labfik.ruang", "Ruang Lab [M]"), ["+ kode, name: Char", "+ kapasitas: Integer"], [], 240, "core"),
    "sesx": (cm("labfik.sesi", "Sesi diperluas [T]", stereo=f10("{_inherit: labfik.sesi} di labfik_praktikum", "#9B2C44")),
             ["+ is_terpublikasi: Boolean {compute, search}", "+ is_ditunda: Boolean {compute}",
              "+ is_terlewat: Boolean {compute, search}", "+ berasisten: Boolean {compute}",
              "+ melebihi_kapasitas: Boolean {compute}", "+ memenuhi_pkg15 … pkg18: Boolean {compute}"],
             ["@model + cari_bentrok(ruang, tanggal, jam_mulai,", "&nbsp;&nbsp;&nbsp;jam_selesai, kecuali): list (AB-PRK-01)",
              "+ get_petugas_ditugaskan(): hr.employee [*]", "+ get_modul_berlaku(): labfik.praktikum.modul",
              "+ get_cek_monev(pkg): list", "# _tandai_terlaksana()", "# _ganti(tanggal, jam, ruang): labfik.sesi",
              "+ unlink() «override» (AB-PRK-04)"], 380, "new"),
    "apv": APV,
    "jdw": (cm("labfik.praktikum.jadwal", "Penetapan Jadwal [T]", "approval"),
            ["+ jumlah_sesi: Integer {compute}", "+ tanggal_publikasi: Date {related: tanggal_sah}"],
            ["+ get_ringkasan(): dict", "# _jenis_dokumen() «override» → jadwal_praktikum",
             "# _cek_kelengkapan() «override» (AB-PRK-05)", "# _cek_satu_per_periode() @constrains"], 330, "c"),
    "imp": (cm("labfik.praktikum.impor.jadwal", "Impor Jadwal [wizard]", stereo="«TransientModel»"),
            ["+ tanggal_pertemuan_pertama: Date", "+ berkas: Binary [0..1]", "+ ringkasan: Text {compute}"],
            ["+ action_pratinjau()", "+ action_impor() (AB-PRK-01–04)", "# _baca_berkas(): baris_ids",
             "# _bangkitkan_sesi(kelas, baris)", "# _cek_terkunci(kelas): bool (AB-PRK-04)"], 330, "new"),
    "impb": (cm("labfik.praktikum.impor.jadwal.baris", "Baris Impor [wizard]", stereo="«TransientModel»"),
             ["+ kode_mk, nama_mk, prodi, nama_kelas: Char", "+ hari: Selection", "+ jam_mulai, jam_selesai: Float",
              "+ kode_ruang: Char", "+ dosen_id: hr.employee [0..1]", "+ jumlah_mahasiswa: Integer [0..1]",
              "+ status: Selection {siap, bentrok, terkunci, salah}", "+ pesan: Char"], [], 330, "new"),
}
bottom = stack(p, [(40, ["mk", "kls", "per"]), (420, ["ses", "rng"]), (840, ["sesx"]), (1300, ["apv", "jdw"]),
                   (1700, ["imp", "impb"])], S)
p.e("kls-mk", "kls", "mk", NAV, "*", "mata_kuliah_id 1", exit=(0.5, 0), entry=(0.5, 1))
p.e("kls-per", "kls", "per", NAV, "*", "periode_id 1", exit=(0.5, 1), entry=(0.5, 0))
p.e("ses-kls", "ses", "kls", NAV, "sesi_ids *", "kelas_id 1", exit=(0, 0.15), entry=(1, 0.3))
p.e("ses-rng", "ses", "rng", NAV, "*", "ruang_id 1", exit=(0.5, 1), entry=(0.5, 0))
x, y, w, h = p.geo["ses"]
p.e("ses-self", "ses", "ses", NAV, "pengganti 0..1", "sesi_asal_id 0..1",
    pts=[(x + w + 30, y + 30), (x + w + 30, y - 25), (x + w - 60, y - 25)], exit=(1, 0.1), entry=(0.82, 0))
p.e("sesx-ses", "sesx", "ses", EXT, None, "«_inherit»", exit=(0, 0.3), entry=(1, 0.5))
p.e("jdw-apv", "jdw", "apv", GEN, exit=(0.5, 0), entry=(0.5, 1))
xb = bottom - 20
p.e("jdw-per", "jdw", "per", NAV, "*", "periode_id 1 (unik)", pts=[(p.pt("jdw", 0.3, 1)[0], xb), (p.pt("per", 0.7, 1)[0], xb)],
    exit=(0.3, 1), entry=(0.7, 1))
p.e("imp-impb", "imp", "impb", COMP, "1", "baris_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.e("imp-per", "imp", "per", NAV, "*", "periode_id 1", pts=[(p.pt("imp", 0.97, 0)[0], 40), (1240, 40), (1240, xb + 15),
                                                             (p.pt("per", 0.35, 1)[0], xb + 15)], exit=(0.97, 0), entry=(0.35, 1))
ny = bottom + 30
p.v("n0", LEG, NOTE, 40, ny, 760, 170)
p.v("n1", "<b>Kunci</b><br>• <b>Core vs Praktikum.</b> Field yang tersimpan di <code>labfik.sesi</code> ada di <code>labfik_core</code> "
    "(kontrak C-9). Field hitung yang membutuhkan Penetapan Jadwal, Perubahan, Jurnal, dan penugasan SDM ditambahkan "
    "<code>labfik_praktikum</code> lewat <code>_inherit</code>, karena Core tidak bergantung ke modul fungsional. "
    "Hanya <code>is_diganti</code> yang dihitung di Core.<br>"
    "• <code>/sesi_asal</code> di CM menjadi field tersimpan <code>sesi_asal_id</code> (Core tidak bisa membaca Perubahan Sesi).<br>"
    "• <code>is_terpublikasi</code> = Penetapan Jadwal periode kelas berstatus disahkan; tidak memakai <i>hook</i> "
    "<code>_setelah_disahkan()</code>.<br>"
    "• Impor = <i>wizard</i>: <code>action_pratinjau()</code> mengisi status per baris tanpa membuat Sesi (query SSD); "
    "<code>action_impor()</code> membangkitkan 16 Sesi per kelas yang berstatus siap.", NOTE, 820, ny, 760, 170)
p.v("n2", SRC, NOTE, 40, ny + 190, 1540, 34)
pages.append((p, 2080, ny + 250))

# ===================================================================== DCD-2
p = Page(2, "Pengajuan", "DCD 2/5 · Pengajuan: pemakaian lab dan perubahan sesi (PKG-15, PKG-18) · labfik_praktikum")
S = {
    "mt": (odoo("mail.thread", "pelacakan perubahan dan chatter"), ["+ message_ids: mail.message [*]"], ["+ message_post()"], 300, "odoo"),
    "pgm": (am("labfik.praktikum.pengajuan.mixin", "Pengajuan, persetujuan sederhana (S2)"),
            ["+ state: Selection {diajukan, disetujui,", "&nbsp;&nbsp;&nbsp;ditolak, ditarik} = diajukan",
             "+ pengaju_id: hr.employee", "+ tanggal_ajukan: Datetime (readonly)",
             "+ pemutus_id: hr.employee [0..1] (readonly)", "+ tanggal_putus: Datetime [0..1] (readonly)",
             "+ alasan_tolak: Text [0..1]", "+ karena_bentrok: Boolean = False", "+ tanggal_tarik: Datetime [0..1] (O)"],
            ["+ action_putuskan(hasil, alasan, karena_bentrok,", "&nbsp;&nbsp;&nbsp;pengganti=None)",
             "+ action_tarik() (O, AB-PRK-11)", "+ get_ringkasan(): str {abstract}",
             "# _jenis_pengajuan(): str {abstract}", "# _cek_wewenang(pemutus) (AB-PRK-10)",
             "# _sebelum_disetujui(pengganti) {hook}", "# _efek_disetujui(pengganti) {hook}",
             "# _beri_tahu(pesan) (O, KF-PRK-49)", "+ unlink() «override» (ditolak)"], 400, "mixin"),
    "pml": (cm("labfik.praktikum.pemakaian", "Pemakaian Lab [T]", "pengajuan"),
            ["+ tanggal: Date", "+ jam_mulai, jam_selesai: Float", "+ keperluan: Text", "+ nama_pemohon: Char",
             "+ unit_pemohon: Char"],
            ["+ get_ringkasan() «override»", "# _jenis_pengajuan() «override» → pemakaian_lab",
             "# _sebelum_disetujui() «override» (AB-PRK-01)", "# _cek_jam_bentrok() @constrains (AB-PRK-01)"], 380, "c"),
    "pbs": (cm("labfik.praktikum.perubahan", "Perubahan Sesi [T]", "pengajuan"),
            ["+ jenis: Selection {pindah, daring, batal}", "+ alasan: Text", "+ usulan_tanggal: Date [0..1]",
             "+ usulan_jam_mulai, usulan_jam_selesai: Float [0..1]"],
            ["+ get_ringkasan() «override»", "# _jenis_pengajuan() «override» → perubahan_sesi",
             "# _sebelum_disetujui(pengganti) «override» (AB-PRK-01, 12)",
             "# _efek_disetujui(pengganti) «override»", "# _cek_usulan() @constrains (AB-PRK-12)"], 380, "c"),
    "ses": (core("labfik.sesi", "Sesi [T] · rincian: DCD-1"), ["<i>is_ditunda {compute} membaca perubahan_ids</i>"],
            ["@model + cari_bentrok(…): list", "# _ganti(tanggal, jam, ruang): labfik.sesi"], 320, "core"),
    "rng": (core("labfik.ruang", "Ruang Lab [M]"), ["+ kode, name: Char", "+ kapasitas: Integer"], [], 240, "core"),
    "job": (odoo("hr.job", "Jabatan [M]", "{_inherit: hr.job} di labfik_core"), ["<i>rincian: DCD Tata Kelola</i>"],
            ["+ punya_wewenang(tindakan, jenis): bool"], 300, "odoo"),
    "wwn": (core("labfik.jabatan.wewenang", "Wewenang Jabatan [M]"),
            ["+ tindakan: Selection {menyusun, mengesahkan}", "+ jenis_dokumen: Selection",
             "&nbsp;&nbsp;&nbsp;+ jadwal_praktikum, pemakaian_lab,", "&nbsp;&nbsp;&nbsp;perubahan_sesi, survei_kepuasan",
             "&nbsp;&nbsp;&nbsp;<i>(selection_add di labfik_praktikum)</i>"], [], 300, "core"),
}
bottom = stack(p, [(40, ["mt", "pgm"]), (520, ["pml", "pbs"]), (980, ["rng", "ses"]), (1380, ["job", "wwn"])], S)
p.e("pgm-mt", "pgm", "mt", GEN, exit=(0.5, 0), entry=(0.5, 1))
p.e("pml-pgm", "pml", "pgm", GEN, exit=(0, 0.3), entry=(1, 0.2))
p.e("pbs-pgm", "pbs", "pgm", GEN, exit=(0, 0.3), entry=(1, 0.75))
p.e("pml-rng", "pml", "rng", NAV, "*", "ruang_id 1", exit=(1, 0.15), entry=(0, 0.5))
p.e("pbs-ses", "pbs", "ses", NAV, "perubahan_ids *", "sesi_id 1", pts=[(940, p.pt("pbs", 1, 0.08)[1]), (940, p.pt("ses", 0, 0.3)[1])],
    exit=(1, 0.08), entry=(0, 0.3))
p.e("pbs-ses2", "pbs", "ses", NAV, "0..1", "sesi_pengganti_id 0..1 (readonly)", pts=[(960, p.pt("pbs", 1, 0.2)[1]),
                                                                                    (960, p.pt("ses", 0, 0.75)[1])],
    exit=(1, 0.2), entry=(0, 0.75))
p.e("pbs-rng", "pbs", "rng", NAV, "*", "usulan_ruang_id 0..1",
    pts=[(p.pt("pbs", 0.9, 1)[0], p.pt("pbs", 0.9, 1)[1] + 25), (1340, p.pt("pbs", 0.9, 1)[1] + 25), (1340, p.pt("rng", 1, 0.5)[1])],
    exit=(0.9, 1), entry=(1, 0.5))
p.e("job-wwn", "job", "wwn", COMP, "1", "wewenang_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.e("pgm-job", "pgm", "job", DER, None, "pemutus.job_id.punya_wewenang()",
    pts=[(p.pt("pgm", 1, 0.06)[0] + 40, p.pt("pgm", 1, 0.06)[1]), (p.pt("pgm", 1, 0.06)[0] + 40, 40),
         (p.pt("job", 0.5, 0)[0], 40)], exit=(1, 0.06), entry=(0.5, 0))
ny = bottom + 10
p.v("n0", LEG, NOTE, 40, ny, 760, 170)
p.v("n1", "<b>Template Method</b> <code>action_putuskan(hasil, alasan, karena_bentrok, pengganti)</code>, urutan tetap di mixin:<br>"
    "1. state harus <i>diajukan</i> · 2. <code>_cek_wewenang(pemutus)</code> → <code>pemutus.job_id.punya_wewenang('mengesahkan', "
    "self._jenis_pengajuan())</code> (AB-PRK-10) · 3. bila ditolak: alasan wajib (AB-PRK-10), tulis state, pemutus, tanggal, "
    "<code>karena_bentrok</code>, selesai · 4. bila disetujui: <code>_sebelum_disetujui(pengganti)</code> {hook} (cek bentrok, "
    "AB-PRK-01; Sesi masih terjadwal, AB-PRK-12) · 5. tulis state, pemutus, tanggal · 6. <code>_efek_disetujui(pengganti)</code> "
    "{hook} · 7. <code>_beri_tahu()</code> (O).<br>"
    "Efek Perubahan Sesi: <i>pindah</i> → <code>sesi._ganti(…)</code> membuat Sesi pengganti (sesi_asal_id) dan Sesi asal batal; "
    "<i>daring</i> → moda daring; <i>batal</i> → Sesi batal. Efek Pemakaian Lab: tidak ada (masuk jadwal terpadu lewat state).",
    NOTE, 820, ny, 800, 170)
p.v("n2", SRC, NOTE, 40, ny + 190, 1580, 34)
pages.append((p, 1740, ny + 250))

# ===================================================================== DCD-3
p = Page(3, "Versi Modul dan Kesiapan", "DCD 3/5 · Versi modul dan pemeriksaan kesiapan (PKG-15 C4, PKG-16, PKG-17) · labfik_praktikum")
S = {
    "ses": (core("labfik.sesi", "Sesi [T] · rincian: DCD-1"), ["<i>get_modul_berlaku()</i>"], [], 260, "core"),
    "evi": EVI,
    "ksp": (cm("labfik.praktikum.kesiapan", "Pemeriksaan Kesiapan [T]", "evidence"),
            ["+ waktu_periksa: Datetime", "+ keputusan: Selection {siap,", "&nbsp;&nbsp;&nbsp;siap_setelah_perbaikan, tunda}",
             "+ tepat_waktu: Boolean {compute, store}", "<i>pelapor_id (warisan) = pemeriksa</i>",
             "<i>_sql_constraints: unique(sesi_id)</i>"],
            ["@model + get_form(sesi): list", "@model + get_keputusan_tersedia(hasil_butir): list",
             "@model + catat(sesi, hasil_butir, keputusan)", "# _cek_keputusan() @constrains (AB-PRK-15, 16)",
             "# _compute_tepat_waktu() (AB-PRK-13)", "# _boleh_dikoreksi() «override»"], 340, "c"),
    "but": (cm("labfik.praktikum.kesiapan.butir", "Butir Pemeriksaan [T]"),
            ["+ kategori: Selection {stasiun_kerja, jaringan,", "&nbsp;&nbsp;&nbsp;listrik, proyektor_audio, software, bahan}",
             "+ hasil: Selection {baik, diperbaiki, bermasalah}", "+ keterangan: Text [0..1]",
             "+ jumlah_berfungsi: Integer [0..1] (stasiun kerja)", "+ jumlah_dibutuhkan: Float {compute}",
             "+ lisensi_sah: Boolean (software berbayar)", "+ jumlah_tersedia: Float [0..1] (bahan)",
             "+ kondisi_baik, berlabel: Boolean (bahan)", "+ tanggal_kedaluwarsa: Date [0..1] (bahan)",
             "+ alasan_substitusi: Text [0..1]", "+ penyetuju_id: hr.employee [0..1] (readonly)",
             "+ waktu_setuju: Datetime [0..1] (readonly)",
             "+ status_substitusi: Selection {tidak_ada,", "&nbsp;&nbsp;&nbsp;menunggu, disetujui} {compute}"],
            ["+ action_setujui_substitusi() (AB-PRK-16)", "# _cek_isian_kategori() @constrains",
             "# _cek_substitusi() @constrains (AB-PRK-16)", "# _compute_jumlah_dibutuhkan()"], 380, "c"),
    "mod": (cm("labfik.praktikum.modul", "Versi Modul [T]", "mail.thread"),
            ["+ nomor_versi: Char", "+ berkas: Binary [0..1]", "+ tautan_leads: Char [0..1]", "+ rubrik: Binary [0..1]",
             "+ tanggal_terbit: Date [0..1] (readonly)", "+ state: Selection {draf, berlaku, diganti} = draf",
             "+ penerbit_id: hr.employee",
             "<i>_sql_constraints: unique(mata_kuliah_id,</i>", "<i>&nbsp;&nbsp;&nbsp;periode_id, nomor_versi)</i>"],
            ["+ action_terbitkan() (AB-PRK-07, 08, 09)", "@model + get_berlaku(mata_kuliah, tanggal): modul",
             "# _cek_pengampu(employee): bool (AB-PRK-09)", "# _cek_isi() @constrains (AB-PRK-08)",
             "+ unlink() «override» (hanya draf)"], 360, "c"),
    "msw": (cm("labfik.praktikum.modul.software", "Kebutuhan Software [T]"),
            ["+ name: Char", "+ versi: Char", "+ berbayar: Boolean = False"], [], 280, "c"),
    "mbh": (cm("labfik.praktikum.modul.bahan", "Kebutuhan Bahan [T]"), ["+ jumlah_per_mahasiswa: Float"], [], 280, "c"),
    "mk": (core("labfik.mata.kuliah", "Mata Kuliah [M]"), ["<i>rincian: DCD-1</i>"], [], 240, "core"),
    "per": (core("labfik.periode", "Periode [M]"), ["<i>rincian: DCD-1</i>"], [], 240, "core"),
    "bhn": (core("labfik.bahan", "Bahan Praktikum [M] (C-13)"), ["+ kode, name, satuan: Char", "+ jenis: Selection"],
            [], 240, "core"),
}
bottom = stack(p, [(40, ["ses"]), (440, ["ksp", "but"]), (900, ["mod", "msw", "mbh"]), (1340, ["mk", "per", "bhn"])], S)
p.e("ksp-ses", "ksp", "ses", NAV, "0..1", "sesi_id 1", exit=(0, 0.1), entry=(1, 0.5))
p.e("ksp-but", "ksp", "but", COMP, "1", "butir_ids 1..*", exit=(0.5, 1), entry=(0.5, 0))
p.e("but-msw", "but", "msw", NAV, "*", "modul_software_id 0..1", exit=(1, 0.3), entry=(0, 0.5))
p.e("but-mbh", "but", "mbh", NAV, "*", "modul_bahan_id 0..1", exit=(1, 0.5), entry=(0, 0.5))
p.e("but-bhn", "but", "bhn", NAV, "*", "bahan_pengganti_id 0..1",
    pts=[(p.pt("but", 0.5, 1)[0], bottom - 20), (p.pt("bhn", 0.5, 1)[0], bottom - 20)], exit=(0.5, 1), entry=(0.5, 1))
p.e("mod-msw", "mod", "msw", COMP, "1", "software_ids *", exit=(0.3, 1), entry=(0.3, 0))
p.e("mod-mbh", "mod", "mbh", COMP, "1", "bahan_ids *",
    pts=[(p.pt("mod", 0.85, 1)[0], p.pt("mbh", 0.9, 0)[1] - 20), (p.pt("mbh", 0.9, 0)[0], p.pt("mbh", 0.9, 0)[1] - 20)],
    exit=(0.85, 1), entry=(0.9, 0))
p.e("mod-mk", "mod", "mk", NAV, "*", "mata_kuliah_id 1", exit=(1, 0.15), entry=(0, 0.5))
p.e("mod-per", "mod", "per", NAV, "*", "periode_id 1", exit=(1, 0.5), entry=(0, 0.5))
p.e("mbh-bhn", "mbh", "bhn", NAV, "*", "bahan_id 1", pts=[(1300, p.pt("mbh", 1, 0.5)[1]), (1300, p.pt("bhn", 0, 0.7)[1])],
    exit=(1, 0.5), entry=(0, 0.7))
ny = bottom + 10
p.v("n0", LEG, NOTE, 40, ny, 760, 170)
p.v("n1", "<b>Kunci</b><br>• <b>Butir: satu model, bukan empat subkelas.</b> Generalisasi CM (ButirUtilitas, StasiunKerja, "
    "Software, Bahan) diwujudkan dengan <code>kategori</code> + <code>_cek_isian_kategori()</code> (field wajib per kategori) "
    "dan tampilan per kategori. Subkelas Odoo (<code>_inherits</code>) akan membuat lima tabel untuk satu daftar butir.<br>"
    "• SubstitusiBahan dan PersetujuanSubstitusi (kejadian 0..1) menjadi field di butir; "
    "<code>action_setujui_substitusi()</code> hanya untuk dosen kelas Sesi itu (AB-PRK-16).<br>"
    "• <code>get_form(sesi)</code> membentuk butir dari <code>sesi.get_modul_berlaku()</code> + kategori tetap (AB-PRK-14), "
    "tanpa menyimpan. <code>/versi_berlaku</code> CM → <code>get_berlaku(mata_kuliah, tanggal)</code>.",
    NOTE, 820, ny, 760, 170)
p.v("n2", SRC, NOTE, 40, ny + 190, 1540, 34)
pages.append((p, 1640, ny + 250))

# ===================================================================== DCD-4
p = Page(4, "Jurnal, Penilaian, Pengaturan", "DCD 4/5 · Jurnal sesi (PKG-18), penilaian kelas (PKG-19), pengaturan · labfik_praktikum")
S = {
    "ses": (core("labfik.sesi", "Sesi [T] · rincian: DCD-1"), ["<i>get_petugas_ditugaskan()</i>"], [], 280, "core"),
    "pgs": (core("labfik.sdm.penugasan", "Baris Penugasan [T] · labfik_sdm", "«SDM»"),
            ["+ employee_id: hr.employee", "+ peran: Selection {asisten, laboran}", "+ kelas_id / ruang_id (sasaran)",
             "+ berlaku_mulai, berlaku_sampai: Date", "<i>surat_tugas_id.state = disahkan</i>"], [], 280, "core"),
    "kls": (core("labfik.kelas", "Kelas [M] · rincian: DCD-1"), ["<i>dosen_ids, dosen_koordinator_id</i>"], [], 280, "core"),
    "cfg": (odoo("res.config.settings", "Pengaturan Praktikum", "{_inherit} di labfik_praktikum"),
            ["+ prk_ambang_durasi: Float (%)", "+ prk_batas_hari_jurnal: Integer", "+ prk_sesi_daring_sah: Boolean",
             "+ prk_batas_lulus: Float = 60", "<i>config_parameter → ir.config_parameter</i>"], [], 280, "odoo"),
    "jur": (cm("labfik.praktikum.jurnal", "Jurnal Sesi [T]", "evidence"),
            ["+ jam_mulai_aktual, jam_selesai_aktual: Float", "+ topik: Text", "+ jumlah_hadir: Integer",
             "+ tautan_presensi: Char [0..1]", "+ kendala: Text [0..1]", "+ state: Selection {draf, terkirim} = draf",
             "+ waktu_kirim: Datetime [0..1] (readonly)", "+ pengirim_id: hr.employee [0..1] (readonly)",
             "+ terlambat: Boolean {compute, store} (O)", "+ durasi_memenuhi: Boolean {compute}",
             "<i>bukti_ids (warisan) = foto</i>", "<i>_sql_constraints: unique(sesi_id)</i>"],
            ["@model + get_konteks(sesi): dict", "+ action_kirim() (AB-PRK-17, 19)", "+ get_kekurangan(): list (AB-PRK-19)",
             "# _cek_jam() @constrains (AB-PRK-18)", "# _cek_sesi() @constrains (AB-PRK-17)",
             "# _boleh_dikoreksi() «override»"], 380, "c"),
    "pnl": (cm("labfik.praktikum.penilaian", "Penilaian Kelas [T]", "evidence"),
            ["+ tautan_leads: Char", "+ ada_rubrik: Boolean {compute}", "+ berbukti: Boolean {compute, store}",
             "+ berkas_nilai_ids: ir.attachment [*] (O, riwayat)", "<i>_sql_constraints: unique(kelas_id)</i>"],
            ["+ action_impor_nilai(berkas) (O, AB-PRK-24)", "+ get_status_praktikan(): list (O, AB-PRK-25)"], 380, "c"),
    "evi": EVI,
    "mod": (cm("labfik.praktikum.modul", "Versi Modul [T] · rincian: DCD-3"), ["<i>rubrik</i>"], [], 300, "c"),
    "ptg": (cm("labfik.praktikum.jurnal.petugas", "Presensi Petugas [T]"),
            ["+ employee_id: hr.employee", "+ peran: Selection {dosen, laboran, asisten}",
             "+ kehadiran: Selection {penuh, sebagian, tidak}", "+ sesuai_penugasan: Boolean {compute} (O)"], [], 320, "c"),
    "lgb": (cm("labfik.praktikum.jurnal.logbook", "Entri Log Book [T]"),
            ["+ waktu: Float (widget jam)", "+ uraian: Text", "<i>_order = 'waktu'</i>"], [], 300, "c"),
    "bn": (cm("labfik.praktikum.penilaian.baris", "Baris Nilai [T] (O)"),
           ["+ nim: Char", "+ jumlah_tugas_individual: Integer", "+ nilai_akhir: Float", "+ ada_umpan_balik: Boolean",
            "+ remedial: Boolean", "+ lengkap: Boolean {compute}", "<i>_sql_constraints: unique(penilaian_id, nim)</i>"],
           [], 320, "c"),
}
bottom = stack(p, [(40, ["ses", "pgs", "kls", "cfg"]), (440, ["jur", "pnl"]), (920, ["mod", "ptg", "lgb", "bn"])], S)
p.e("jur-ses", "jur", "ses", NAV, "0..1", "sesi_id 1", exit=(0, 0.06), entry=(1, 0.5))
p.e("ses-pgs", "ses", "pgs", DER, None, "get_petugas_ditugaskan()", exit=(0.5, 1), entry=(0.5, 0))
p.e("jur-mod", "jur", "mod", NAV, "*", "modul_id 1 (dipakai)", exit=(1, 0.08), entry=(0, 0.5))
p.e("jur-ptg", "jur", "ptg", COMP, "1", "petugas_ids 1..*", exit=(1, 0.4), entry=(0, 0.5))
p.e("jur-lgb", "jur", "lgb", COMP, "1", "logbook_ids 1..*", pts=[(890, p.pt("jur", 1, 0.8)[1]), (890, p.pt("lgb", 0, 0.5)[1])],
    exit=(1, 0.8), entry=(0, 0.5))
p.e("pnl-kls", "pnl", "kls", NAV, "0..1", "kelas_id 1", exit=(0, 0.3), entry=(1, 0.5))
p.e("pnl-bn", "pnl", "bn", COMP, "1", "baris_ids *", exit=(1, 0.7), entry=(0, 0.5))
ny = bottom + 10
p.v("n0", LEG, NOTE, 40, ny, 760, 170)
p.v("n1", "<b>Template Method</b> <code>action_kirim()</code>: 1. Sesi terjadwal, <code>is_terpublikasi</code>, tanggal ≤ hari ini, "
    "belum ada jurnal terkirim (AB-PRK-17) · 2. <code>get_kekurangan()</code> kosong: presensi dosen dan laboran, asisten bila "
    "<code>sesi.berasisten</code>, jumlah_hadir, modul_id, ≥ 1 log book (AB-PRK-19) · 3. tulis state = terkirim, waktu_kirim, "
    "pengirim_id · 4. <code>sesi._tandai_terlaksana()</code> (hanya Praktikum yang mengubah state Sesi).<br>"
    "• <code>sesuai_penugasan</code> membaca <code>sesi.get_petugas_ditugaskan()</code> (asisten lewat kelas, laboran lewat ruang, "
    "Surat Tugas disahkan dan berlaku pada tanggal sesi). Hanya penanda (AB-PRK-20).<br>"
    "• <code>terlambat</code>, <code>durasi_memenuhi</code>, <code>lengkap</code> membaca pengaturan dari "
    "<code>ir.config_parameter</code>. BerkasNilai CM → <code>berkas_nilai_ids</code> (riwayat lampiran).", NOTE, 820, ny, 760, 170)
p.v("n2", SRC, NOTE, 40, ny + 190, 1540, 34)
pages.append((p, 1640, ny + 250))

# ===================================================================== DCD-5
p = Page(5, "Survei dan Status Monev", "DCD 5/5 · Survei kepuasan (PKG-20) dan status monev praktikum · labfik_praktikum")
S = {
    "cri": (am("labfik.criteria.mixin", "Core · rincian: DCD Tata Kelola"), ["+ kriteria_tertinggi: Integer {compute}"],
            ["+ get_kriteria(tanggal_acuan): dict", "# _cek_k1(tanggal) … _cek_k4(tanggal) {abstract}"], 330, "mixin"),
    "per": (core("labfik.periode", "Periode [M]"), ["<i>rincian: DCD-1</i>"], [], 240, "core"),
    "srv": (odoo("survey.survey", "Survei Kepuasan [T]", "{_inherit: survey.survey, labfik.criteria.mixin} di labfik_praktikum"),
            ["+ jenis_responden: Selection {praktikan, dosen, asisten}", "+ populasi: Integer", "+ target_response_rate: Float (%)",
             "+ tanggal_buka, tanggal_tutup: Date", "+ status_lab: Selection {draf, ditetapkan,",
             "&nbsp;&nbsp;&nbsp;dievaluasi, siklus_selesai} {compute, store}", "+ status_buka: Selection {compute}",
             "+ penetap_id: hr.employee [0..1] (readonly)", "+ tanggal_tetap: Date [0..1] (readonly)",
             "+ response_rate: Float {compute}", "<i>bawaan dipakai: title, question_ids, answer_done_count,</i>",
             "<i>&nbsp;&nbsp;&nbsp;access_mode = public (anonim)</i>"],
            ["+ action_tetapkan() (AB-PRK-26)", "+ action_batalkan_penetapan() (O, AB-PRK-27)",
             "+ get_kekurangan_penetapan(): list (AB-PRK-26)", "+ get_rekap(): dict", "+ get_survei_berikutnya(): survey.survey",
             "# _cek_k1() … _cek_k4() «override» (AB-PRK-34)", "# _create_answer() «override» (AB-PRK-28)"], 440, "odoo"),
    "q": (odoo("survey.question", "Butir Survei", "{_inherit} di labfik_praktikum"),
          ["+ aspek: Selection {alat, bahan, layanan,", "&nbsp;&nbsp;&nbsp;keselamatan, akses, pengalaman_belajar}",
           "+ rerata: Float {compute}", "<i>bawaan: title, question_type, sequence</i>"], [], 340, "odoo"),
    "ui": (odoo("survey.user_input", "Respons (bawaan, tanpa perluasan)"), ["<i>state, create_date; tanpa partner (anonim)</i>"],
           [], 340, "odoo"),
    "uil": (odoo("survey.user_input.line", "Jawaban (bawaan)"), ["<i>value_numerical_box / value_text_box, …</i>"], [], 340, "odoo"),
    "evi": EVI,
    "evs": (cm("labfik.praktikum.evaluasi.survei", "Evaluasi Survei [T]", "evidence"),
            ["<i>_sql_constraints: unique(survey_id)</i>"],
            ["+ action_nilai_efektivitas(nilai) (AB-PRK-30)", "# _cek_setelah_tutup() @constrains (AB-PRK-29)"], 360, "c"),
    "ksa": (cm("labfik.praktikum.evaluasi.kesimpulan", "Kesimpulan Aspek [T]"), ["+ aspek: Selection", "+ kesimpulan: Text"],
            [], 300, "c"),
    "rtl": (cm("labfik.praktikum.evaluasi.rtl", "Rencana Tindak Lanjut [T]"),
            ["+ aspek: Selection", "+ prioritas: Selection {tinggi, sedang, rendah}", "+ tindakan: Text",
             "+ pic_id: hr.employee", "+ tenggat: Date", "+ rerata_sebelum, rerata_sesudah: Float {compute}",
             "+ efektif: Selection {ya, sebagian, tidak} [0..1]", "+ catatan_efektivitas: Text [0..1]",
             "+ penilai_id: hr.employee [0..1] (readonly)", "+ tanggal_nilai: Date [0..1] (readonly)",
             "+ status: Selection {terbuka, dinilai} {compute}"],
            ["# _cek_baris_lengkap() @constrains (AB-PRK-29)"], 360, "c"),
    "mon": (am("labfik.praktikum.monev", "Status Monev Praktikum [R] (layanan, tanpa tabel)"), ["<i>(tidak menyimpan data)</i>"],
            ["@model + get_status(periode, tanggal_acuan): dict", "@model + terbitkan_laporan_bukti(periode,",
             "&nbsp;&nbsp;&nbsp;tanggal_acuan): report", "@model # _persentase(pkg, periode): dict (AB-PRK-32)",
             "@model # _status_pkg19(periode): dict (AB-PRK-33)"], 380, "new"),
}
bottom = stack(p, [(40, ["cri", "per", "mon"]), (440, ["srv", "q"]), (960, ["ui"]), (1380, ["evs", "ksa", "rtl"])], S)
p.cls("uil", *S["uil"][:3], 960, p.geo["q"][1], S["uil"][3], S["uil"][4])
p.e("srv-cri", "srv", "cri", GEN, exit=(0, 0.08), entry=(1, 0.3))
p.e("srv-per", "srv", "per", NAV, "*", "periode_id 1", exit=(0, 0.35), entry=(1, 0.5))
p.e("srv-q", "srv", "q", COMP, "1", "question_ids * (bawaan)", exit=(0.5, 1), entry=(0.5, 0))
p.e("ui-srv", "ui", "srv", NAV, "*", "survey_id 1 (bawaan)", exit=(0, 0.5), entry=(1, 0.15))
p.e("ui-uil", "ui", "uil", COMP, "1", "user_input_line_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.e("uil-q", "uil", "q", NAV, "*", "question_id 1", exit=(0, 0.3), entry=(1, 0.3))
p.e("evs-srv", "evs", "srv", NAV, "0..1", "survey_id 1", pts=[(p.pt("evs", 0.3, 0)[0], 36), (p.pt("srv", 0.9, 0)[0], 36)],
    exit=(0.3, 0), entry=(0.9, 0))
p.e("evs-ksa", "evs", "ksa", COMP, "1", "kesimpulan_ids 1..*", exit=(0.5, 1), entry=(0.5, 0))
p.e("evs-rtl", "evs", "rtl", COMP, "1", "rtl_ids 1..*", pts=[(p.pt("evs", 1, 0.8)[0] + 30, p.pt("evs", 1, 0.8)[1]),
                                                           (p.pt("evs", 1, 0.8)[0] + 30, p.pt("rtl", 1, 0.1)[1])],
    exit=(1, 0.8), entry=(1, 0.1))
p.e("mon-srv", "mon", "srv", DER, None, "get_kriteria()", exit=(1, 0.3), entry=(0, 0.85))
ny = bottom + 10
p.v("n0", LEG, NOTE, 40, ny, 760, 170)
p.v("n1", "<b>Kunci</b><br>• Survei <b>memperluas</b> addon <code>survey</code> (LGPL-3), tidak membuat model survei sendiri: "
    "Respons dan Jawaban CM = <code>survey.user_input</code> dan <code>.line</code> bawaan; jumlah responden = "
    "<code>answer_done_count</code> bawaan. Anonim lewat <code>access_mode</code> publik (AB-PRK-28).<br>"
    "• PenetapanSurvei (kejadian) → <code>penetap_id</code>, <code>tanggal_tetap</code>; wewenang dicek "
    "<code>penetap.job_id.punya_wewenang('mengesahkan', 'survei_kepuasan')</code>. <code>status_lab</code> tersimpan supaya bisa "
    "dipakai filter; nilainya dihitung dari penetapan, evaluasi, dan RTL (§9.3.2 CM).<br>"
    "• <code>labfik.praktikum.monev.get_status()</code> mendelegasikan ke <code>sesi.get_cek_monev(pkg)</code>, "
    "<code>penilaian.berbukti</code>, dan <code>survey.get_kriteria()</code> (delegasi, §13.5).", NOTE, 820, ny, 760, 170)
p.v("n2", SRC, NOTE, 40, ny + 190, 1540, 34)
pages.append((p, 1800, ny + 250))

with open(OUT, "w", encoding="utf-8") as f:
    f.write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
