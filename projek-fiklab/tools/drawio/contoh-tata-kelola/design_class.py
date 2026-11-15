import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
LH = 15


def esc(s):
    return escape(s, {'"': "&quot;"})


FILL = {"c": "fillColor=#FFFFFF;strokeColor=#333333;", "mixin": "fillColor=#E1D5E7;strokeColor=#9673A6;",
        "odoo": "fillColor=#F5F5F5;strokeColor=#666666;", "core": "fillColor=#F5F5F5;strokeColor=#666666;dashed=1;",
        "stub": "fillColor=#FAFAFA;strokeColor=#999999;dashed=1;", "new": "fillColor=#FFFFFF;strokeColor=#9B2C44;strokeWidth=2;"}
TXT = ("text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
       "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;")
SEP = ("line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;"
       "rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;")
GEN = "endArrow=block;endFill=0;endSize=14;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#6C4A87;"
COMP = "endArrow=none;startArrow=diamondThin;startFill=1;startSize=16;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#333333;fontSize=10;"
NAV = "endArrow=open;endFill=0;endSize=10;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#555555;fontSize=10;"
DER = "endArrow=open;endFill=0;endSize=10;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#555555;dashed=1;fontSize=10;"
BI = "endArrow=none;html=1;edgeStyle=orthogonalEdgeStyle;rounded=0;strokeColor=#555555;fontSize=10;"
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
FRAME = ("rounded=1;arcSize=1;whiteSpace=wrap;html=1;verticalAlign=top;align=left;spacingLeft=10;spacingTop=6;"
         "fontSize=14;fontStyle=1;fillColor=#F5F0FF;strokeColor=#9673A6;")
TITLE = "text;html=1;fontSize=17;fontStyle=1;align=left;verticalAlign=middle;"


def height(title, attrs, methods):
    start = 10 + 15 * (title.count("<br>") + 1)
    return start + max(1, len(attrs)) * LH + 8 + ((8 + len(methods) * LH + 8) if methods else 0)


class Page:
    def __init__(self, n, name, title):
        self.P, self.n, self.name, self.cells, self.geo = f"tk-dcd{n}-", n, name, [], {}
        self.v("title", title, TITLE, 40, 10, 1700, 34)

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

    def e(self, id, s, t, style, src=None, tgt=None, mid=None, exit=None, entry=None):
        st = style
        if exit:
            st += f"exitX={exit[0]};exitY={exit[1]};exitDx=0;exitDy=0;"
        if entry:
            st += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        eid = f"{self.P}{id}"
        self.cells.append(f'<mxCell id="{eid}" value="{esc(mid or "")}" style="{st}labelBackgroundColor=#FFFFFF;" edge="1" '
                          f'parent="1" source="{self.P}{s}" target="{self.P}{t}"><mxGeometry relative="1" as="geometry"/></mxCell>')
        for k, (lbl, xpos, align) in enumerate([(src, -1, "left"), (tgt, 1, "right")]):
            if lbl:
                self.cells.append(
                    f'<mxCell id="{eid}-l{k}" value="{esc(lbl)}" style="edgeLabel;resizable=0;html=1;align={align};verticalAlign=bottom;'
                    f'fontSize=10;labelBackgroundColor=#FFFFFF;" connectable="0" vertex="1" parent="{eid}"><mxGeometry x="{xpos}" '
                    f'relative="1" as="geometry"><mxPoint x="{8 if xpos < 0 else -8}" y="-2" as="offset"/></mxGeometry></mxCell>')

    def xml(self, w, h):
        return (f'<diagram id="tk-dcd{self.n}" name="{esc(self.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" '
                f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w:.0f}" pageHeight="{h:.0f}" '
                'math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells) + "</root></mxGraphModel></diagram>")


def am(name):
    return f"«AbstractModel»<br><b><i>{name}</i></b>"


def cm(name, label, inherit=None):
    t = f"<b>{name}</b><br><font style='font-size:10px'>{label}</font>"
    if inherit:
        t += f"<br><font style='font-size:10px' color='#6C4A87'>{{inherit: {inherit}}}</font>"
    return t



def odoo(name, label, ext=False):
    t = f"«Odoo»<br><b>{name}</b><br><font style='font-size:10px'>{label}</font>"
    if ext:
        t += f"<br><font style='font-size:10px' color='#6C4A87'>{{_inherit: {name}}} di labfik_core</font>"
    return t


def core(name, label):
    return f"«Core»<br><b>{name}</b><br><font style='font-size:10px'>{label}</font>"


def stack(page, columns, specs, top=60, gap=46):
    bottoms = {}
    for x, ids in columns:
        y = top
        for cid in ids:
            t, a, m, w, kind = specs[cid]
            y += page.cls(cid, t, a, m, x, y, w, kind) + gap
        bottoms[x] = y
    return max(bottoms.values())


LEG = ("<b>Notasi</b> (Wazlawick 2024, §13.6; UML)<br>"
       "• Ungu «AbstractModel» (nama miring) = <i>mixin</i> tanpa tabel; segitiga kosong ungu = <code>_inherit = [mixin, …]</code>.<br>"
       "• «Odoo» abu-abu = model bawaan; bila diberi <code>{_inherit: …}</code>, model itu diperluas tanpa <code>_name</code> baru. "
       "«Core» abu-abu putus-putus = master bersama di labfik_core. Tepi merah = model hasil desain yang tidak ada padanannya 1:1 di CM.<br>"
       "• Panah terbuka = Many2one/Many2many berarah, label = nama field. Belah ketupat hitam = One2many + Many2one (anak ikut terhapus). "
       "Putus-putus = field <code>compute</code>.<br>"
       "• Atribut bertipe hanya untuk model bawaan Odoo (hr.employee, res.users, res.currency, ir.attachment). Field warisan mixin tidak ditulis ulang.<br>"
       "• <code>+</code> publik (<code>action_*</code>, <code>get_*</code>), <code>#</code> internal (<code>_…</code>), @model, «override», {abstract}, {hook}.")
SRC = ("Design class diagram (masuk proposal Bab II 2.3). Diturunkan dari conceptual model CM-1–4, katalog operasi SSD, dan AB-01–25. "
       "Rincian: design-class-tata-kelola.md · Draf 14 Nov 2026 · Febriyan")
pages = []

# =================================================================== DCD-1
p = Page(1, "DCD TO-BE (1-4) - Mixin dan Pengesahan", "DCD 1/4 · Mixin bersama (labfik_core) dan mekanisme pengesahan")
p.cls("mt", odoo("mail.thread", "pelacakan perubahan dan chatter"), ["+ message_ids: mail.message [*]"], ["+ message_post()"], 640, 50, 260, "odoo")
S = {}
S["apv"] = (am("labfik.approval.mixin"), [
    "+ state: Selection {draf, diajukan, disahkan,", "&nbsp;&nbsp;&nbsp;diganti, dicabut, kedaluwarsa} = draf",
    "+ penyusun_id: hr.employee", "+ tanggal_ajukan: Datetime (readonly)", "+ berkas_ttd: Binary [0..1]",
    "+ pengesah_id: hr.employee [0..1] (readonly)", "+ pencatat_id: res.users [0..1] (readonly)", "+ tanggal_sah: Date [0..1] (readonly)",
    "+ log_ids: labfik.approval.log [*] {compute}"],
    ["+ action_ajukan()", "+ action_unggah_ttd(berkas)", "+ action_kembalikan(alasan)", "+ action_sahkan(pengesah, tanggal_sah)",
     "+ action_cabut(alasan)", "+ action_terbitkan(): report", "+ get_kelengkapan(): list", "+ get_pengesah_berwenang(): hr.employee",
     "+ unlink() «override»", "# _jenis_dokumen(): str {abstract}", "# _cek_kelengkapan(): list {abstract}", "# _cek_wewenang(pengesah)",
     "# _sebelum_ajukan() {hook}", "# _sebelum_disahkan() {hook}", "# _dokumen_diganti(): recordset {hook}",
     "# _setelah_disahkan() {hook}", "# _ubah_status(status_baru, kejadian, alasan, berkas)"], 420, "mixin")
S["log"] = ("<b>labfik.approval.log</b><br><font style='font-size:10px'>Riwayat Pengesahan [T]</font>", [
    "+ res_model: Char", "+ res_id: Integer", "+ kejadian: Selection {diajukan, dikembalikan,",
    "&nbsp;&nbsp;&nbsp;berkas_diunggah, disahkan, diganti, dicabut, kedaluwarsa}", "+ waktu: Datetime",
    "+ pelaku_id: res.users [0..1]", "+ pengesah_id: hr.employee [0..1]", "+ alasan: Text [0..1]", "+ berkas: Binary [0..1]"],
    ["+ write() «override» (ditolak)", "+ unlink() «override» (ditolak)"], 320, "new")
S["prd"] = (am("labfik.period.mixin"), ["+ tanggal_mulai: Date {related}", "+ tanggal_selesai: Date {related}", "+ is_berlaku: Boolean {compute}"],
            ["+ berlaku_pada(tanggal): bool", "@model # _cron_kedaluwarsakan() (O)"], 300, "mixin")
S["per"] = (core("labfik.periode", "Periode [M]"), ["+ name: Char", "+ jenis: Selection", "+ tanggal_mulai: Date", "+ tanggal_selesai: Date"], [], 300, "core")
S["cri"] = (am("labfik.criteria.mixin"), ["+ kriteria_tertinggi: Integer {compute}"],
            ["+ get_kriteria(tanggal_acuan): dict", "# _compute_kriteria_tertinggi()", "# _cek_k1(tanggal) … _cek_k4(tanggal) {abstract}"], 320, "mixin")
S["evi"] = (am("labfik.evidence.mixin"), ["+ tanggal: Date", "+ pelapor_id: hr.employee", "+ bukti_ids: ir.attachment [*]", "+ keterangan: Text [0..1]"],
            ["+ action_koreksi(nilai, alasan)", "+ unlink() «override» (ditolak)", "# _boleh_dikoreksi(): bool {hook}"], 320, "mixin")
bottom = stack(p, [(40, ["apv"]), (500, ["log", "prd", "per"]), (860, ["cri", "evi"])], S, top=200)
p.e("g-apv-mt", "apv", "mt", GEN, exit=(0.6, 0), entry=(0, 0.5))
p.e("g-evi-mt", "evi", "mt", GEN, exit=(0.5, 0), entry=(1, 0.5))
p.e("c-apv-log", "apv", "log", DER, "1", "log_ids *", exit=(1, 0.1), entry=(0, 0.2))
p.e("n-prd-per", "prd", "per", NAV, "*", "periode_id 1", exit=(0.5, 1), entry=(0.5, 0))
# turunan
sub = [("ren", cm("labfik.renstra", "Renstra", "approval, period"), ["apv", "prd"]),
       ("pln", cm("labfik.plan", "Rencana", "approval, period, criteria"), ["apv", "prd", "cri"]),
       ("asg", cm("labfik.assignment", "SK Penetapan", "approval, period, criteria"), ["apv", "prd", "cri"]),
       ("ver", cm("labfik.document.version", "Versi SOP/IK", "approval"), ["apv"])]
for i, (cid, t, pars) in enumerate(sub):
    p.cls(cid, t, ["<i>(rincian: DCD 2–4)</i>"], [], 40 + i * 230, bottom + 40, 210)
    for par in pars:
        p.e(f"g-{cid}-{par}", cid, par, GEN, exit=(0.5, 0))
ev = [("mee", "labfik.meeting", "Rapat Koordinasi"), ("oev", "labfik.org.evaluation", "Evaluasi Struktur"),
      ("dis", "labfik.document.distribution", "Distribusi"), ("soc", "labfik.document.socialization", "Sosialisasi"),
      ("rev", "labfik.document.review", "Tinjau Ulang"), ("rea", "labfik.realisasi", "Realisasi"), ("tin", "labfik.tinjauan", "Tinjauan Rencana")]
for i, (cid, name, label) in enumerate(ev):
    p.cls(cid, cm(name, label, "evidence"), ["<i>(rincian: DCD 2–4)</i>"], [], 980 + (i % 2) * 250, 560 + (i // 2) * 110, 230)
    p.e(f"g-{cid}-evi", cid, "evi", GEN, exit=(0.5, 0), entry=(0.5, 1))
ny = max(bottom + 160, 560 + 4 * 110) + 20
p.v("n0", LEG, NOTE, 40, ny, 760, 150)
p.v("n1", "<b>Template Method</b> <code>action_sahkan(pengesah, tanggal_sah)</code> — urutan tetap di mixin, tidak di-<i>override</i>:<br>"
    "1. state harus <i>diajukan</i> · 2. berkas_ttd ada (AB-04) · 3. <code>_cek_wewenang(pengesah)</code> (AB-05) · "
    "4. <code>_sebelum_disahkan()</code> {hook} · 5. tulis pengesah, pencatat = pengguna, tanggal_sah, state = disahkan · "
    "6. <code>_dokumen_diganti()</code> {hook} → state = diganti + log (AB-08) · 7. log <i>disahkan</i> (AB-09) · "
    "8. <code>_setelah_disahkan()</code> {hook}.<br>Model turunan hanya mengisi <i>hook</i>. Hanya grup KaLab yang boleh memanggilnya (AB-06). "
    "<code>action_ajukan()</code> berpola sama: cek draf → <code>_cek_kelengkapan()</code> → <code>_sebelum_ajukan()</code> → ubah status.", NOTE, 820, ny, 640, 150)
p.v("n2", "<b>Dari CM ke desain</b> (§13.6)<br>• DokumenDisahkan → <code>approval.mixin</code>; Pengesahan (0..1) → field readonly di mixin; "
    "KejadianPengesahan → <code>approval.log</code> generik (res_model, res_id) untuk semua dokumen.<br>"
    "• RekamanBukti → <code>evidence.mixin</code>. Periode → <code>period.mixin</code>. /kriteria_tertinggi → <code>criteria.mixin</code>.<br>"
    "• <code>revisi_dari_id</code> ditulis di tiap model (Many2one ke model itu sendiri) karena mixin tidak bisa merujuk dirinya.<br>"
    "• <code>labfik.controlled.mixin</code> tidak dipakai (lihat dokumen).", NOTE, 1480, ny, 480, 150)
p.v("n3", SRC, NOTE, 40, ny + 170, 1420, 30)
pages.append((p, 2000, ny + 240))

# =================================================================== DCD-2
p = Page(2, "DCD TO-BE (2-4) - Struktur Organisasi", "DCD 2/4 · Struktur organisasi (PKG-03)")
S = {}
S["emp"] = (odoo("hr.employee", "Personel [M]", True), ["+ jenis_personel: Selection {dosen, laboran_plp,", "&nbsp;&nbsp;&nbsp;teknisi, asisten, petugas_k3}",
                                                         "+ unit: Selection", "<i>bawaan dipakai: name, job_id, user_id</i>"], ["+ unlink() «override» (AB-23)"], 300, "odoo")
S["asl"] = (cm("labfik.assignment.line", "Baris Penetapan [T]"), ["+ employee_id: hr.employee", "+ tanggal_mulai: Date", "+ tanggal_selesai: Date"], [], 300, "c")
S["job"] = (odoo("hr.job", "Jabatan [M]", True), ["+ unit: Selection {lab_fik, prodi_if, prodi_si, fakultas}", "+ is_eksternal: Boolean",
                                                 "+ syarat_kompetensi: Text [0..1]", "+ is_lengkap: Boolean {compute}"],
            ["+ punya_wewenang(tindakan, jenis): bool", "@model + cari_pemegang_berwenang(tindakan, jenis): hr.employee",
             "# _compute_is_lengkap()", "# _cek_atasan() @constrains (tanpa siklus)", "+ unlink() «override» (AB-23)"], 340, "odoo")
S["tgs"] = (cm("labfik.jabatan.tugas", "Tugas Jabatan [M]"), ["+ urutan: Integer", "+ uraian: Text"], [], 260, "c")
S["wwn"] = (cm("labfik.jabatan.wewenang", "Wewenang Jabatan [M]"), ["+ tindakan: Selection {menyusun, mengesahkan}", "+ jenis_dokumen: Selection",
                                                                  "<i>_sql_constraints: unique(jabatan_id, tindakan, jenis_dokumen)</i>"], [], 340, "c")
S["asg"] = (cm("labfik.assignment", "SK Penetapan Pengelola [T]", "approval, period, criteria"),
            ["+ nomor_sk: Char «unique»", "+ judul: Char", "+ menimbang: Html", "+ mengingat: Html"],
            ["# _jenis_dokumen() «override»", "# _cek_kelengkapan() «override»", "# _dokumen_diganti() «override»",
             "# _cek_k1() … _cek_k4() «override»"], 320, "c")
S["mee"] = (cm("labfik.meeting", "Rapat Koordinasi [T]", "evidence"), ["+ agenda: Text", "+ keputusan: Text", "+ notulen: Binary",
                                                                        "+ peserta_ids: hr.employee [*]"], [], 320, "c")
S["oev"] = (cm("labfik.org.evaluation", "Evaluasi Struktur [T]", "evidence"), ["+ temuan_beban_kerja: Text", "+ efektivitas_koordinasi: Text",
                                                                               "+ keputusan: Text", "+ struktur_diubah: Boolean"],
            ["+ action_tautkan_revisi(sk, jabatan)"], 320, "c")
S["rng"] = (core("labfik.ruang", "Ruang Lab [M]"), ["+ kode: Char", "+ name: Char", "+ kapasitas: Integer"], [], 220, "core")
bottom = stack(p, [(40, ["emp", "asl", "rng"]), (420, ["job", "tgs", "wwn"]), (840, ["asg", "mee", "oev"])], S)
p.e("n-emp-job", "emp", "job", NAV, "*", "job_id 0..1 (bawaan)", exit=(1, 0.3), entry=(0, 0.3))
p.e("n-job-atas", "job", "job", NAV, "bawahan *", "atasan_id 0..1", exit=(1, 0.15), entry=(1, 0.05))
p.e("n-job-ganti", "job", "job", NAV, "*", "pengganti_id 0..1", exit=(1, 0.45), entry=(1, 0.35))
p.e("c-job-tgs", "job", "tgs", COMP, "1", "tugas_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.e("c-job-wwn", "job", "wwn", COMP, "1", "wewenang_ids *", exit=(0.1, 1), entry=(0.1, 0))
p.e("c-asg-asl", "asg", "asl", COMP, "1", "baris_ids 1..*", exit=(0, 0.5), entry=(1, 0.3))
p.e("n-asl-job", "asl", "job", NAV, "*", "jabatan_id 1", exit=(1, 0.8), entry=(0, 0.8))
p.e("n-asl-rng", "asl", "rng", NAV, "*", "ruang_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.e("n-asg-self", "asg", "asg", NAV, "pengganti 0..1", "revisi_dari_id 0..1", exit=(1, 0.2), entry=(1, 0.1))
p.e("n-oev-asg", "oev", "asg", NAV, "*", "sk_id 1", exit=(1, 0.2), entry=(1, 0.6))
p.e("n-oev-asg2", "oev", "asg", NAV, "0..1", "sk_revisi_id 0..1", exit=(1, 0.5), entry=(1, 0.85))
p.e("n-oev-job", "oev", "job", NAV, "*", "jabatan_direvisi_ids *", exit=(0, 0.5), entry=(1, 0.8))
p.v("n0", LEG, NOTE, 40, bottom + 20, 760, 150)
p.v("n1", "<b>Kunci</b><br>• Personel dan Jabatan <b>memperluas</b> model bawaan <code>hr</code> (is-a), sedangkan Tugas dan Wewenang adalah "
    "<b>model anak baru</b> (has-a) (keputusan 14 Nov 2026).<br>"
    "• AB-05: <code>approval.mixin._cek_wewenang(pengesah)</code> memanggil <code>pengesah.job_id.punya_wewenang('mengesahkan', self._jenis_dokumen())</code> "
    "(delegasi, §13.5). Matriks kewenangan (UC-13) dibaca dari <code>wewenang_ids</code>.<br>"
    "• Pejabat fakultas = hr.employee tanpa <code>user_id</code>; jabatannya <code>is_eksternal</code>.", NOTE, 820, bottom + 20, 640, 150)
p.v("n2", SRC, NOTE, 40, bottom + 190, 1420, 30)
pages.append((p, 1560, bottom + 260))

# =================================================================== DCD-3
p = Page(3, "DCD TO-BE (3-4) - Pengendalian Dokumen", "DCD 3/4 · Pengendalian dokumen SOP/IK (PKG-02)")
S = {}
S["doc"] = (cm("labfik.document", "Dokumen Induk [M]", "mail.thread"), [
    "+ kode: Char «unique»", "+ judul: Char", "+ jenis: Selection {sop, ik, formulir, eksternal}", "+ kategori: Selection",
    "+ asal: Selection {lab, fakultas, universitas}", "+ is_wajib: Boolean", "+ dasar_kebutuhan: Text", "+ tanggal_ditetapkan_wajib: Date",
    "+ siklus_tinjau_bulan: Integer", "+ active: Boolean = True", "+ memenuhi: Boolean {compute}"],
    ["+ get_info_versi(): dict", "+ cek_monev(tanggal_tutup): dict (S1–S5)", "@model + hitung_persentase(tanggal_tutup): dict",
     "# _compute_versi_berlaku()", "+ unlink() «override» (AB-23)"], 360, "c")
S["rng"] = (core("labfik.ruang", "Ruang Lab [M]"), ["+ kode: Char", "+ name: Char", "+ kapasitas: Integer"], [], 220, "core")
S["ver"] = (cm("labfik.document.version", "Versi Dokumen SOP/IK [T]", "approval, mail.thread"), [
    "+ revisi: Char", "+ berkas: Binary", "+ tanggal_efektif: Date", "+ bagian_diubah: Text [0..1]", "+ ringkasan_perubahan: Text [0..1]",
    "+ alasan_revisi: Text [0..1]", "+ tanggal_tinjau_berikutnya: Date {compute, store}", "+ perlu_ditinjau: Boolean {compute, search}",
    "<i>_sql_constraints: unique(document_id, revisi)</i>"],
    ["+ baca_berkas(): Binary (O)", "# _jenis_dokumen() «override»", "# _cek_kelengkapan() «override»",
     "# _sebelum_ajukan() «override» (AB-12, O)", "# _dokumen_diganti() «override»", "# _compute_tanggal_tinjau()", "# _search_perlu_ditinjau()"], 380, "c")
S["dis"] = (cm("labfik.document.distribution", "Distribusi [T]", "evidence"), ["<i>(atribut dari evidence.mixin)</i>"],
            ["# _cek_versi_dan_lokasi() @constrains"], 300, "c")
S["soc"] = (cm("labfik.document.socialization", "Sosialisasi [T]", "evidence"), ["+ metode: Selection", "+ peserta_ids: hr.employee [*]",
                                                                                    "+ jumlah_peserta: Integer"],
            ["# _cek_versi_dan_peserta() @constrains"], 300, "c")
S["rev"] = (cm("labfik.document.review", "Tinjau Ulang [T]", "evidence"), ["+ hasil: Selection {tetap_berlaku, perlu_revisi}", "+ catatan: Text"],
            ["# _cek_versi() @constrains", "# _boleh_dikoreksi() «override» (False)"], 300, "c")
bottom = stack(p, [(40, ["doc", "rng"]), (480, ["ver"]), (940, ["dis", "soc", "rev"])], S)
p.e("c-doc-ver", "doc", "ver", COMP, "1", "versi_ids *", exit=(1, 0.15), entry=(0, 0.15))
p.e("d-doc-ver", "doc", "ver", DER, "0..1", "versi_berlaku_id 0..1 {compute}", exit=(1, 0.35), entry=(0, 0.4))
p.e("n-doc-rng", "doc", "rng", NAV, "*", "lokasi_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.e("n-dis-ver", "dis", "ver", NAV, "*", "version_id 1", exit=(0, 0.5), entry=(1, 0.15))
p.e("n-dis-rng", "dis", "rng", NAV, "*", "ruang_id 1", exit=(0.5, 1), entry=(1, 0.5))
p.e("n-soc-ver", "soc", "ver", NAV, "*", "version_id 1", exit=(0, 0.5), entry=(1, 0.45))
p.e("n-rev-ver", "rev", "ver", NAV, "*", "version_id 1", exit=(0, 0.5), entry=(1, 0.75))
p.v("n0", LEG, NOTE, 40, bottom + 20, 760, 150)
p.v("n1", "<b>Kunci</b><br>• AB-13 <code>_sql_constraints</code>; AB-12 (O) di hook <code>_sebelum_ajukan()</code>; "
    "AB-14 <code>_compute_tanggal_tinjau()</code> dari tanggal_sah / tinjau ulang terakhir + siklus.<br>"
    "• AB-15, AB-16 <code>@api.constrains</code> di Distribusi, Sosialisasi, Tinjau Ulang. AB-17 (O) <i>record rule</i> grup Pengguna Lab: "
    "<code>state = 'disahkan'</code>.<br>• AB-24 <code>cek_monev()</code> per dokumen + <code>hitung_persentase()</code>.", NOTE, 820, bottom + 20, 600, 150)
p.v("n2", SRC, NOTE, 40, bottom + 190, 1380, 30)
pages.append((p, 1500, bottom + 260))

# =================================================================== DCD-4
p = Page(4, "DCD TO-BE (4-4) - Rencana dan Status Monev", "DCD 4/4 · Renstra, rencana (PKG-01, PKG-13), dan status monev")
S = {}
S["ren"] = (cm("labfik.renstra", "Renstra [T]", "approval, period"), ["+ judul: Char", "+ berkas: Binary"],
            ["# _jenis_dokumen() «override»", "# _cek_kelengkapan() «override»", "# _dokumen_diganti() «override»"], 300, "c")
S["kpi"] = (cm("labfik.kpi", "KPI [M]"), ["+ kode: Char «unique»", "+ nama: Char", "+ definisi: Text", "+ rumus_pembilang: Text",
                                          "+ rumus_penyebut: Text", "+ satuan: Char", "+ frekuensi: Selection", "+ sumber_data: Text",
                                          "+ active: Boolean = True"], ["+ unlink() «override» (AB-23)"], 300, "c")
S["pln"] = (cm("labfik.plan", "Rencana [T]", "approval, period, criteria"), ["+ jenis: Selection {tahunan, pengembangan}", "+ judul: Char",
                                                                             "+ narasi: Html [0..1] (O)"],
            ["+ action_buat_revisi() (O)", "# _jenis_dokumen() «override»", "# _cek_kelengkapan() «override»",
             "# _sebelum_disahkan() «override» (AB-11, O)", "# _dokumen_diganti() «override»", "# _cek_k1() … _cek_k4() «override»"], 340, "c")
S["lin"] = (cm("labfik.plan.line", "Item Rencana [T]"), ["+ kegiatan: Text", "+ target: Float", "+ satuan: Char", "+ pic_id: hr.employee",
                                                          "+ jadwal_mulai: Date", "+ jadwal_selesai: Date", "+ anggaran: Monetary",
                                                          "+ currency_id: res.currency", "+ rujukan_renstra: Text",
                                                          "+ nilai_risiko: Selection {1, 2, 3}", "+ nilai_manfaat: Selection {1, 2, 3}",
                                                          "+ prioritas: Selection {compute} (O)"],
            ["+ get_capaian(): dict", "# _compute_prioritas() (O)"], 340, "c")
S["gap"] = (cm("labfik.plan.gap", "Temuan Gap [T]"), ["+ aspek: Selection {tridharma, kompetensi,", "&nbsp;&nbsp;&nbsp;sarana, layanan}",
                                                      "+ kondisi_saat_ini: Text", "+ kebutuhan: Text", "+ sumber_data: Text", "+ uraian_gap: Text",
                                                      "+ lampiran: Binary [0..1]", "+ tidak_ada_gap: Boolean", "+ alasan_tidak_ada_gap: Text [0..1]"], [], 300, "c")
S["rea"] = (cm("labfik.realisasi", "Realisasi [T]", "evidence"), ["+ periode_lapor: Char", "+ capaian: Float", "+ biaya_terpakai: Monetary",
                                                                   "+ status_capaian: Selection", "+ tindak_lanjut: Text",
                                                                   "<i>_sql_constraints: unique(line_id, periode_lapor)</i>"],
            ["# _cek_realisasi() @constrains (AB-18)"], 320, "c")
S["tin"] = (cm("labfik.tinjauan", "Tinjauan Rencana [T]", "evidence"), ["+ ringkasan_capaian: Text", "+ keputusan: Text",
                                                                         "+ peserta_ids: hr.employee [*]"],
            ["+ action_tautkan_rencana_berikutnya(rencana)", "# _cek_tinjauan() @constrains (AB-19, AB-20)"], 320, "c")
S["mnf"] = (cm("labfik.tinjauan.manfaat", "Ukuran Manfaat [T]"), ["+ indikator: Text", "+ nilai_sebelum: Float", "+ nilai_sesudah: Float",
                                                                  "+ sumber: Text"], [], 300, "c")
S["mon"] = ("«AbstractModel»<br><b>labfik.org.monev</b><br><font style='font-size:10px'>Status Monev [R] (layanan, tanpa tabel)</font>",
            ["<i>(tidak menyimpan data)</i>"],
            ["@model + get_status(tanggal_acuan): dict", "@model # _status_pkg02(tanggal)", "@model # _status_kriteria(model, tanggal)"], 320, "new")
bottom = stack(p, [(40, ["ren", "kpi"]), (400, ["pln", "lin"]), (800, ["gap", "rea"]), (1180, ["tin", "mnf", "mon"])], S)
p.e("n-pln-self", "pln", "pln", NAV, "pengganti 0..1", "revisi_dari_id 0..1", exit=(1, 0.1), entry=(1, 0.02))
p.e("n-ren-self", "ren", "ren", NAV, "", "revisi_dari_id 0..1", exit=(1, 0.2), entry=(1, 0.05))
p.e("c-pln-lin", "pln", "lin", COMP, "1", "line_ids 1..*", exit=(0.5, 1), entry=(0.5, 0))
p.e("c-pln-gap", "pln", "gap", COMP, "1", "gap_ids *", exit=(1, 0.4), entry=(0, 0.15))
p.e("n-lin-kpi", "lin", "kpi", NAV, "*", "kpi_id 0..1", exit=(0, 0.2), entry=(1, 0.3))
p.e("n-lin-gap", "lin", "gap", NAV, "*", "gap_ids *", exit=(1, 0.2), entry=(0, 0.7))
p.e("n-rea-lin", "rea", "lin", NAV, "realisasi_ids *", "line_id 1", exit=(0, 0.4), entry=(1, 0.7))
p.e("n-tin-pln", "tin", "pln", NAV, "*", "plan_id 1", exit=(0, 0.2), entry=(1, 0.5))
p.e("n-tin-pln2", "tin", "pln", NAV, "0..1", "rencana_berikut_id 0..1", exit=(0, 0.5), entry=(1, 0.8))
p.e("c-tin-mnf", "tin", "mnf", COMP, "1", "manfaat_ids *", exit=(0.5, 1), entry=(0.5, 0))
p.e("n-mnf-lin", "mnf", "lin", NAV, "*", "line_id 1", exit=(0, 0.5), entry=(1, 0.4))
p.v("n0", LEG, NOTE, 40, bottom + 20, 760, 150)
p.v("n1", "<b>Kunci</b><br>• Satu model <code>labfik.plan</code> untuk rencana tahunan dan pengembangan: <code>_jenis_dokumen()</code>, "
    "<code>_cek_kelengkapan()</code> (AB-02), dan <code>_cek_k1()–_cek_k4()</code> (AB-25) bercabang menurut <code>jenis</code>.<br>"
    "• <code>labfik.org.monev.get_status()</code> mendelegasikan perhitungan ke <code>labfik.document.hitung_persentase()</code> (AB-24) "
    "dan ke <code>get_kriteria()</code> di Rencana dan SK (AB-25). Tidak menyimpan data.<br>"
    "• Biaya rencana pengembangan = <code>anggaran</code>.", NOTE, 820, bottom + 20, 720, 150)
p.v("n2", SRC, NOTE, 40, bottom + 190, 1500, 30)
pages.append((p, 1600, bottom + 260))

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
