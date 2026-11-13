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


LEG = ("<b>Notasi</b> (Wazlawick 2024, §13.6; UML)<br>"
       "• Segitiga kosong ungu = generalisasi; di Odoo <code>_inherit = [mixin, …]</code>. Kelas ungu «AbstractModel» tidak punya tabel sendiri.<br>"
       "• Panah terbuka = asosiasi <b>berarah</b> (dapat dinavigasi dari pemilik field): Many2one atau Many2many. Label = nama field.<br>"
       "• Belah ketupat hitam = komposisi: One2many di induk + Many2one di anak (dua arah, anak ikut terhapus).<br>"
       "• Garis putus-putus = asosiasi turunan (field <code>compute</code>). Garis polos tanpa panah = dua arah (One2many + Many2one).<br>"
       "• <code>+</code> publik, <code>#</code> internal (diawali garis bawah di Odoo). «override» = method warisan yang diisi ulang. "
       "{abstract} = wajib diisi turunan. @model = method kelas (<code>@api.model</code>).<br>"
       "• Referensi ke model bawaan Odoo (res.users, ir.attachment, res.currency) ditulis sebagai atribut bertipe.")
SRC = ("Design class diagram (masuk proposal). Diturunkan dari conceptual model (CM-1–3) + katalog operasi SSD. "
       "Rincian: rancangan/design-class-tata-kelola.md · Draf 13 Nov 2026 · Febriyan")
pages = []

# =================================================================== DCD-1
p = Page(1, "DCD (1-3) Inheritance dan Pengesahan", "DCD 1/3 · Design class diagram: inheritance (mixin) dan mekanisme pengesahan")
p.cls("mt", "«Odoo»<br><b>mail.thread</b>", ["+ message_ids: mail.message [0..*]"], ["+ message_post()"], 500, 60, 240, "odoo")
p.cls("ma", "«Odoo»<br><b>mail.activity.mixin</b>", ["+ activity_ids: mail.activity [0..*]"], ["+ activity_schedule()"], 780, 60, 240, "odoo")
p.cls("ctl", am("labfik.controlled.mixin"), ["+ kode_dokumen: Char", "+ revisi: Integer", "+ unit_pemilik: Char", "+ tanggal_dibuat: Date"],
      [], 40, 260, 260, "mixin")
p.cls("apv", am("labfik.approval.mixin"), [
    "+ state: Selection {draf, diajukan, diperiksa,", "&nbsp;&nbsp;&nbsp;disahkan, diganti, dicabut, kedaluwarsa}",
    "+ penyusun_id: labfik.personel", "+ pengesah_id: labfik.personel", "+ pencatat_id: labfik.personel",
    "+ jabatan_pengesah_id: labfik.jabatan", "+ tanggal_ajukan: Datetime", "+ tanggal_sah: Date", "+ tanggal_berlaku: Date",
    "+ file_ttd: Binary", "+ tanggal_ttd: Date", "+ nama_penanda_tangan: Char", "+ log_ids: labfik.approval.log [0..*]"],
    ["+ action_ajukan()", "+ action_tarik(alasan)", "+ action_periksa(catatan)", "+ action_kembalikan(alasan)",
     "+ action_catat_pengembalian(alasan, nama, jabatan)", "+ action_lampirkan_ttd(berkas, tanggal_ttd, nama)",
     "+ action_sahkan(atas_nama=None)", "+ action_cabut(alasan)", "+ get_kelengkapan(): list",
     "# _cek_kelengkapan(): list {abstract}", "# _jenis_dokumen(): str {abstract}", "# _cek_wewenang(user, tindakan): bool",
     "# _catat_log(kejadian, **nilai)", "# _setelah_disahkan() {hook}"], 340, 260, 360, "mixin")
p.cls("prd", am("labfik.period.mixin"), ["+ periode_id: labfik.periode", "+ tanggal_mulai: Date", "+ tanggal_selesai: Date",
                                         "+ is_berlaku: Boolean {compute}"],
      ["# _compute_is_berlaku()", "@model # _cron_kedaluwarsakan()"], 740, 260, 280, "mixin")
p.cls("cri", am("labfik.criteria.mixin"), ["+ status_k1 … status_k4: Boolean {compute}", "+ kriteria_tertinggi: Integer {compute}"],
      ["# _compute_kriteria()", "# _cek_k1() … _cek_k4() {abstract}"], 1060, 260, 280, "mixin")
p.cls("evi", am("labfik.evidence.mixin"), ["+ tanggal: Date", "+ pelapor_id: labfik.personel", "+ bukti_ids: ir.attachment [0..*]",
                                           "+ keterangan: Text"], [], 1380, 260, 280, "mixin")
p.cls("log", "<b>labfik.approval.log</b><br><font style='font-size:10px'>Riwayat Pengesahan [T] (baru)</font>", [
    "+ res_model: Char", "+ res_id: Integer", "+ kejadian: Selection {ajukan, tarik, periksa,",
    "&nbsp;&nbsp;&nbsp;kembalikan, unggah_ttd, sahkan, cabut, kedaluwarsa}", "+ putaran: Integer (urutan pengajuan)",
    "+ waktu: Datetime", "+ pelaku_id: labfik.personel", "+ pencatat_id: labfik.personel",
    "+ jabatan_id: labfik.jabatan", "+ alasan: Text", "+ catatan: Text", "+ file_ttd: Binary", "+ tanggal_ttd: Date",
    "+ nama_penanda_tangan: Char"], [], 40, 520, 280, "new")
p.cls("pln", cm("labfik.plan", "Rencana", "controlled, approval, period, criteria"), ["<i>(atribut: DCD 3/3)</i>"],
      ["# _jenis_dokumen() «override»", "# _cek_kelengkapan() «override»", "# _cek_k1() … _cek_k4() «override»",
       "# _setelah_disahkan() «override»", "+ action_buat_revisi()", "+ action_terbitkan()"], 360, 960, 300)
p.cls("asg", cm("labfik.assignment", "SK Penetapan Pengelola", "controlled, approval, period, criteria"), ["<i>(atribut: DCD 2/3)</i>"],
      ["# _jenis_dokumen() «override»", "# _cek_kelengkapan() «override»", "# _cek_k1() … _cek_k4() «override»",
       "# _setelah_disahkan() «override»", "+ action_terbitkan()"], 700, 960, 300)
p.cls("ver", cm("labfik.document.version", "Versi Dokumen SOP/IK", "controlled, approval"), ["<i>(atribut: DCD 2/3)</i>"],
      ["# _jenis_dokumen() «override»", "# _cek_kelengkapan() «override»", "# _setelah_disahkan() «override»"], 1040, 960, 300)
ev = [("rea", "labfik.realisasi", "Realisasi"), ("mee", "labfik.meeting", "Rapat Koordinasi"), ("oev", "labfik.org.evaluation", "Evaluasi Struktur"),
      ("dis", "labfik.document.distribution", "Distribusi"), ("soc", "labfik.document.socialization", "Sosialisasi"),
      ("rev", "labfik.document.review", "Tinjau Ulang"), ("tin", "labfik.tinjauan", "Tinjauan Rencana")]
for i, (cid, name, label) in enumerate(ev):
    p.cls(cid, cm(name, label, "evidence"), ["<i>(atribut: DCD 2/3 atau 3/3)</i>"], [], 1380 + (i % 2) * 300, 520 + (i // 2) * 120, 280)
p.cls("ps", "<b>labfik.personel</b>", ["<i>(DCD 2/3) [KONFIRMASI]</i>"], [], 40, 860, 220, "stub")
p.cls("jb", "<b>labfik.jabatan</b>", ["<i>(DCD 2/3)</i>"], [], 40, 960, 220, "stub")
p.e("g-apv-mt", "apv", "mt", GEN, exit=(0.45, 0), entry=(0.5, 1))
p.e("g-apv-ma", "apv", "ma", GEN, exit=(0.75, 0), entry=(0.5, 1))
for c, parents in {"pln": ["ctl", "apv", "prd", "cri"], "asg": ["ctl", "apv", "prd", "cri"], "ver": ["ctl", "apv"]}.items():
    for par in parents:
        p.e(f"g-{c}-{par}", c, par, GEN)
for cid, _, _ in ev:
    p.e(f"g-{cid}-evi", cid, "evi", GEN)
p.e("c-apv-log", "apv", "log", COMP, "1", "log_ids 0..*", exit=(0, 0.85), entry=(1, 0.1))
p.e("n-log-ps", "log", "ps", NAV, "*", "pelaku_id, pencatat_id 0..1", exit=(0.3, 1), entry=(0.5, 0))
p.e("n-log-jb", "log", "jb", NAV, "*", "jabatan_id 0..1", exit=(0.8, 1), entry=(1, 0.3))
p.v("n1", LEG, NOTE, 40, 1180, 760, 140)
p.v("n2", "<b>Dari conceptual model ke desain</b> (§13.6: struktur boleh berubah)<br>"
    "• Generalisasi <i>DokumenTerkendali</i> (CM-1) → <code>controlled.mixin</code> + <code>approval.mixin</code>.<br>"
    "• Tujuh konsep riwayat (Pengajuan, Penarikan, Pemeriksaan, Pengembalian, BerkasTTD, Pengesahan, Pencabutan) → "
    "<b>satu</b> <code>labfik.approval.log</code> dengan field <code>kejadian</code> dan <code>putaran</code>. "
    "Field ringkas di mixin menyimpan keadaan terakhir untuk tampilan cepat.<br>"
    "• Peran asosiasi (penyusun, pengesah, pencatat, …) → field Many2one dengan nama yang sama.", NOTE, 820, 1180, 560, 140)
p.v("n3", "<b>Template Method</b>: <code>action_sahkan()</code> di mixin selalu menjalankan urutan tetap: cek wewenang (AB-02) → "
    "cek berkas TTD (AB-03) → cek pemeriksaan (AB-09) → ubah status → catat log → panggil <code>_setelah_disahkan()</code>. "
    "Model turunan hanya mengisi hook itu:<br>• Versi: versi lama → diganti, jadwal tinjau (AB-04, AB-08)<br>"
    "• SK: SK lama → diganti, penugasan berlaku<br>• Rencana: rencana sejenis periode sama → diganti (AB-14)", NOTE, 1400, 1180, 560, 140)
p.v("n4", SRC, NOTE, 40, 1340, 1300, 30)
pages.append((p, 2020, 1400))


# =================================================================== DCD-2 / DCD-3 helpers
def stack(page, columns, specs, top=110, gap=50):
    bottoms = {}
    for x, ids in columns:
        y = top
        for cid in ids:
            t, a, m, w, kind = specs[cid]
            y += page.cls(cid, t, a, m, x, y, w, kind) + gap
        bottoms[x] = y
    return bottoms


# =================================================================== DCD-2
p = Page(2, "DCD (2-3) Struktur dan Dokumen", "DCD 2/3 · Design class diagram: struktur organisasi (PKG-03) dan pengendalian dokumen (PKG-02)")
S = {}
S["per"] = (cm("labfik.personel", "Personel [M] [KONFIRMASI]"), ["+ name: Char", "+ jenis: Selection", "+ user_id: res.users [0..1]",
                                                                  "+ active: Boolean = True"], [], 260, "c")
S["asl"] = (cm("labfik.assignment.line", "Baris Penetapan"), ["+ tanggal_mulai: Date", "+ tanggal_selesai: Date"], [], 240, "c")
S["mee"] = (cm("labfik.meeting", "Rapat Koordinasi [T]", "evidence"), ["+ agenda: Text", "+ keputusan: Html", "+ notulen: Html"], [], 260, "c")
S["jab"] = (cm("labfik.jabatan", "Jabatan [M]"), ["+ kode: Char «unique»", "+ name: Char", "+ unit: Selection {lab_fik, prodi_if,",
                                                 "&nbsp;&nbsp;&nbsp;prodi_si, fakultas}", "+ is_eksternal: Boolean", "+ syarat_kompetensi: Text"],
            ["+ get_pemegang_aktif(tanggal): labfik.personel", "+ punya_wewenang(tindakan, jenis): bool",
             "@model + cari_pemegang_berwenang(tindakan, jenis)", "# _compute_pemegang_aktif()"], 320, "c")
S["asg"] = (cm("labfik.assignment", "SK Penetapan Pengelola [T]", "controlled, approval, period, criteria"),
            ["+ nomor_sk: Char «unique»", "+ name: Char", "+ menimbang: Html", "+ mengingat: Html", "+ diktum: Html", "+ tembusan: Text"],
            ["# _setelah_disahkan() «override»", "+ action_terbitkan()", "(+ override lain: DCD 1/3)"], 320, "c")
S["oev"] = (cm("labfik.org.evaluation", "Evaluasi Struktur [T]", "evidence"), ["+ temuan_beban_kerja: Text", "+ efektivitas_koordinasi: Text",
                                                                               "+ keputusan: Html"], [], 300, "c")
S["tug"] = (cm("labfik.jabatan.tugas", "Tugas"), ["+ urutan: Integer", "+ uraian: Text"], [], 220, "c")
S["wew"] = (cm("labfik.jabatan.wewenang", "Wewenang"), ["+ tindakan: Selection {menyusun,", "&nbsp;&nbsp;&nbsp;memeriksa, mengesahkan}",
                                                        "+ jenis_dokumen: Selection"], [], 240, "c")
S["rng"] = (cm("labfik.ruang", "Ruang Lab [M] «Core»"), ["+ kode: Char «unique»", "+ name: Char", "+ fungsi: Text", "+ kapasitas: Integer"], [], 220, "core")
S["doc"] = (cm("labfik.document", "Dokumen Induk [M]"), ["+ kode: Char «unique»", "+ name: Char", "+ jenis: Selection", "+ kategori: Selection",
                                                       "+ asal: Selection", "+ is_wajib: Boolean", "+ dasar_kebutuhan: Text",
                                                       "+ rekaman_dihasilkan: Text", "+ is_memenuhi: Boolean {compute}"],
            ["+ action_buat_versi(dto_versi_baru)", "+ get_info_versi(): dict", "@model + persentase_memenuhi(): float",
             "# _compute_versi_berlaku()", "# _compute_memenuhi()"], 320, "c")
S["rev"] = (cm("labfik.document.review", "Tinjau Ulang [T]", "evidence"), ["+ hasil: Selection {tetap_berlaku,", "&nbsp;&nbsp;&nbsp;perlu_revisi, tidak_diperlukan}"],
            ["# _perbarui_tanggal_tinjau()"], 280, "c")
S["ver"] = (cm("labfik.document.version", "Versi Dokumen [T]", "controlled, approval"),
            ["+ file: Binary", "+ tanggal_revisi: Date", "+ bagian_diubah: Char", "+ ringkasan_perubahan: Text", "+ alasan_revisi: Selection",
             "+ periode_tinjau_bulan: Integer", "+ tanggal_tinjau_berikutnya: Date {compute, store}",
             "+ status_kemutakhiran: Selection {compute}"],
            ["# _setelah_disahkan() «override»", "# _compute_tanggal_tinjau()", "# _compute_status_kemutakhiran()",
             "# _check_satu_versi_diproses() (AB-13)", "@model + daftar_jadwal_tinjau(user)", "@model # _cron_kirim_pengingat_tinjau()"], 340, "c")
S["dis"] = (cm("labfik.document.distribution", "Distribusi [T]", "evidence"), ["+ lokasi_lain: Char"], [], 260, "c")
S["soc"] = (cm("labfik.document.socialization", "Sosialisasi [T]", "evidence"), ["+ metode: Selection"], [], 260, "c")
cols = [(40, ["per", "asl", "mee"]), (360, ["jab", "asg", "oev"]), (740, ["tug", "wew", "rng"]), (1060, ["doc", "rev"]), (1460, ["ver", "dis", "soc"])]
b = stack(p, cols, S)
p.e("c-jt", "jab", "tug", COMP, "1", "tugas_ids 1..*")
p.e("c-jw", "jab", "wew", COMP, "1", "wewenang_ids *")
p.e("n-ja", "jab", "jab", NAV, None, "atasan_id 0..1")
p.e("n-jp", "jab", "jab", NAV, None, "pengganti_id 0..1")
p.e("n-jk", "jab", "jab", NAV, None, "koordinasi_ids *")
p.e("d-jper", "jab", "per", DER, None, "pemegang_aktif_ids * {compute}")
p.e("n-jd", "jab", "doc", NAV, None, "dasar_dokumen_id 0..1")
p.e("c-sl", "asg", "asl", COMP, "1", "line_ids 1..*")
p.e("n-lp", "asl", "per", NAV, "*", "personel_id 1")
p.e("n-lj", "asl", "jab", NAV, "*", "jabatan_id 1")
p.e("n-lr", "asl", "rng", NAV, "*", "ruang_ids *")
p.e("n-ad", "asg", "doc", NAV, "*", "dasar_hukum_ids *")
p.e("n-ar", "asg", "asg", NAV, None, "revisi_dari_id 0..1")
p.e("n-ma", "mee", "asg", NAV, "*", "assignment_id 1")
p.e("n-mp", "mee", "per", NAV, "*", "peserta_ids 1..*")
p.e("n-oa", "oev", "asg", NAV, "*", "assignment_id 1")
p.e("n-ob", "oev", "asg", NAV, "0..1", "assignment_baru_id 0..1")
p.e("n-oj", "oev", "jab", NAV, "*", "jabatan_direvisi_ids *")
p.e("c-dv", "doc", "ver", COMP, "1", "version_ids 1..*")
p.e("d-dv", "doc", "ver", DER, None, "versi_berlaku_id 0..1 {compute}")
p.e("n-dr", "doc", "rng", NAV, "*", "lokasi_penggunaan_ids *")
p.e("n-dd", "doc", "doc", NAV, None, "dokumen_terkait_ids *")
p.e("n-vv", "ver", "ver", NAV, None, "revisi_dari_id 0..1")
p.e("c-vd", "ver", "dis", COMP, "1", "distribution_ids *")
p.e("c-vs", "ver", "soc", COMP, "1", "socialization_ids *")
p.e("c-vr", "ver", "rev", COMP, "1", "review_ids *")
p.e("n-dsr", "dis", "rng", NAV, "*", "lokasi_id 0..1")
p.e("n-sp", "soc", "per", NAV, "*", "peserta_ids 1..*")
ny = max(b.values()) + 10
p.v("n1", LEG, NOTE, 40, ny, 760, 140)
p.v("n2", "<b>Field warisan tidak ditulis ulang</b>: lihat DCD 1/3 (mis. <code>state</code>, <code>pengesah_id</code>, <code>tanggal</code>, "
    "<code>pelapor_id</code>, <code>bukti_ids</code>).<br><b>Aturan bisnis sebagai constraint</b>: AB-04 satu versi berlaku "
    "(<code>_setelah_disahkan</code>), AB-13 satu versi diproses (<code>@api.constrains</code>), «unique» = <code>_sql_constraints</code>.<br>"
    "<b>[KONFIRMASI]</b> <code>labfik.personel</code> vs <code>hr.employee</code> vs model Rafika (kontrak kelompok).",
    NOTE, 820, ny, 560, 140)
p.v("n3", SRC, NOTE, 40, ny + 160, 1300, 30)
pages.append((p, 1860, ny + 220))

# =================================================================== DCD-3
p = Page(3, "DCD (3-3) Perencanaan", "DCD 3/3 · Design class diagram: perencanaan (PKG-01, PKG-13)")
S = {}
S["sas"] = (cm("labfik.plan.sasaran", "Sasaran Strategis"), ["+ kode: Char", "+ sasaran: Text", "+ target_akhir: Char"], [], 240, "c")
S["prg"] = (cm("labfik.plan.program", "Program Strategis"), ["+ kode: Char", "+ name: Char", "+ kegiatan_utama: Text", "+ luaran: Text",
                                                            "+ tahapan: Text"], [], 240, "c")
S["bas"] = (cm("labfik.plan.baseline", "Baseline"), ["+ data: Char", "+ nilai_awal: Char", "+ sumber: Char"], [], 240, "c")
S["pln"] = (cm("labfik.plan", "Rencana [T]", "controlled, approval, period, criteria"),
            ["+ name: Char", "+ jenis: Selection {strategis, tahunan,", "&nbsp;&nbsp;&nbsp;iku, pengembangan}",
             "+ ringkasan, latar_belakang, tujuan,", "&nbsp;&nbsp;&nbsp;ruang_lingkup, referensi, landasan,", "&nbsp;&nbsp;&nbsp;visi, misi, penutup: Html"],
            ["+ action_buat_revisi()", "+ action_terbitkan()", "+ get_status_item(): list", "+ get_status_gap(): dict",
             "# _setelah_disahkan() «override»", "(+ override lain: DCD 1/3)"], 320, "c")
S["gap"] = (cm("labfik.plan.gap", "Temuan Gap (PKG-13)"), ["+ aspek: Selection {tridharma,", "&nbsp;&nbsp;&nbsp;kompetensi, sarana, layanan}",
                                                         "+ kondisi_saat_ini: Text", "+ kebutuhan: Text", "+ sumber_data: Char",
                                                         "+ uraian_gap: Text", "+ lampiran_ids: ir.attachment [0..*]"], [], 280, "c")
S["lin"] = (cm("labfik.plan.line", "Item Rencana"), ["+ kegiatan: Text", "+ baseline: Float", "+ target: Float", "+ satuan: Char",
                                                    "+ jadwal_mulai: Date", "+ jadwal_selesai: Date", "+ bukti_diharapkan: Text",
                                                    "+ anggaran: Monetary", "+ currency_id: res.currency", "+ komponen_anggaran: Selection",
                                                    "+ nilai_risiko: Integer", "+ nilai_manfaat: Integer", "+ prioritas: Selection {compute}"],
            ["+ get_capaian(periode_lapor): dict", "@model + daftar_item_pic(user, periode_lapor)", "# _compute_prioritas()",
             "@model # _cron_kirim_pengingat_realisasi()"], 330, "c")
S["rea"] = (cm("labfik.realisasi", "Realisasi [T]", "evidence"), ["+ periode_lapor: Char", "+ capaian: Float", "+ anggaran_terpakai: Monetary",
                                                                 "+ status_capaian: Selection", "+ alasan_tidak_relevan: Text",
                                                                 "+ analisis_tindakan: Text", "+ tenggat: Date", "+ persen_capaian: Float {compute}"],
            ["# _check_alasan() (AB-10)", "# _check_bukti() (AB-12)", "# _check_pic() (AB-11)", "# _compute_persen_capaian()"], 300, "c")
S["kpi"] = (cm("labfik.kpi", "KPI [M]"), ["+ kode: Char «unique»", "+ name: Char", "+ sasaran_kerja: Char", "+ rumus: Text", "+ pembilang: Char",
                                         "+ penyebut: Char", "+ satuan: Char", "+ frekuensi: Selection", "+ sumber_bukti: Text", "+ acuan_iso: Char"], [], 260, "c")
S["sre"] = (cm("labfik.sasaran.renstra", "Sasaran Renstra [M]"), ["+ kode: Char «unique»", "+ uraian: Text", "+ tingkat: Selection"], [], 240, "c")
S["tin"] = (cm("labfik.tinjauan", "Tinjauan Rencana [T]", "evidence"), ["+ ringkasan: Html", "+ keputusan: Html"], [], 260, "c")
S["man"] = (cm("labfik.tinjauan.manfaat", "Ukuran Manfaat (PKG-13)"), ["+ indikator_manfaat: Char", "+ nilai_sebelum: Float",
                                                                     "+ nilai_sesudah: Float", "+ sumber: Char"], [], 250, "c")
S["prd"] = (cm("labfik.periode", "Periode [M] «Core»"), ["+ name: Char", "+ jenis: Selection", "+ tanggal_mulai: Date", "+ tanggal_selesai: Date"], [], 230, "core")
S["per"] = ("<b>labfik.personel</b>", ["<i>(DCD 2/3)</i>"], [], 200, "stub")
S["jab"] = ("<b>labfik.jabatan</b>", ["<i>(DCD 2/3)</i>"], [], 200, "stub")
cols = [(40, ["sas", "prg", "bas"]), (360, ["pln", "gap"]), (760, ["lin", "rea"]), (1170, ["kpi", "sre"]), (1500, ["tin", "man", "prd", "per", "jab"])]
b = stack(p, cols, S)
for c, lbl in [("sas", "sasaran_ids *"), ("prg", "program_ids *"), ("bas", "baseline_ids *"), ("gap", "gap_ids *"), ("lin", "line_ids *")]:
    p.e(f"c-p{c}", "pln", c, COMP, "1", lbl)
p.e("n-pp", "pln", "pln", NAV, None, "parent_id 0..1")
p.e("n-pr", "pln", "pln", NAV, None, "revisi_dari_id 0..1")
p.e("n-pprd", "pln", "prd", NAV, "*", "periode_id 1 (period.mixin)")
p.e("n-sk", "sas", "kpi", NAV, "*", "kpi_id 0..1")
p.e("n-bp", "bas", "per", NAV, "*", "pic_id 1")
p.e("n-lk", "lin", "kpi", NAV, "*", "kpi_id 0..1")
p.e("n-lp", "lin", "per", NAV, "*", "pic_id 1")
p.e("n-ls", "lin", "sas", NAV, "*", "sasaran_id 0..1")
p.e("n-lpg", "lin", "prg", NAV, "*", "program_id 0..1")
p.e("n-lsr", "lin", "sre", NAV, "*", "sasaran_renstra_ids *")
p.e("n-lg", "lin", "gap", NAV, "*", "gap_ids *")
p.e("b-lr", "lin", "rea", BI, "line_id 1", "realisasi_ids *")
p.e("n-rp", "rea", "per", NAV, "*", "pic_tindak_lanjut_id 0..1")
p.e("b-pt", "pln", "tin", BI, "plan_id 1", "tinjauan_ids *")
p.e("n-tb", "tin", "pln", NAV, "*", "rencana_berikut_id 0..1")
p.e("n-tp", "tin", "per", NAV, "*", "peserta_ids 1..*")
p.e("c-tm", "tin", "man", COMP, "1", "manfaat_ids *")
p.e("n-ml", "man", "lin", NAV, "*", "line_id 1")
p.e("n-kj", "kpi", "jab", NAV, "*", "jabatan_pic_id 1")
ny = max(b.values()) + 10
p.v("n1", LEG, NOTE, 40, ny, 760, 140)
p.v("n2", "<b>Field warisan tidak ditulis ulang</b>: lihat DCD 1/3. <code>periode_id</code> berasal dari <code>period.mixin</code>.<br>"
    "<b>Query dari SSD</b> (katalog operasi) menjadi method <code>get_*</code> / <code>daftar_*</code>; "
    "<b>command</b> menjadi <code>action_*</code>. Constraint AB-10–12 sebagai <code>@api.constrains</code> (<code>_check_*</code>).",
    NOTE, 820, ny, 560, 140)
p.v("n3", SRC, NOTE, 40, ny + 160, 1300, 30)
pages.append((p, 1800, ny + 220))

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + "".join(pg.xml(w, h) for pg, w, h in pages) + "</mxfile>")
