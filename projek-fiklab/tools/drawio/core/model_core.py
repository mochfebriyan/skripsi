"""Katalog model Core (labfik_core): mixin dan master bersama.

Pemakaian:
    python3 -I projek-fiklab/tools/drawio/core/model_core.py projek-fiklab/rancangan/model-core.drawio
    python3 -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/model-core.drawio core-

Sumber isi: projek-fiklab/rancangan/kontrak-core.md (15 November 2026).
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
P = "core-mdl-"
LH = 15
W = 370          # lebar kotak
GX = 30          # jarak antar-kolom
GY = 40          # jarak antar-baris
X0 = 60          # kiri kotak pertama
Y0 = 120         # atas baris pertama


def esc(s):
    return escape(s, {'"': "&quot;"})


FILL = {
    "mixin": "fillColor=#E1D5E7;strokeColor=#9673A6;",
    "odoo": "fillColor=#F5F5F5;strokeColor=#666666;",
    "baru": "fillColor=#FFFFFF;strokeColor=#666666;",
}
TXT = ("text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
       "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;")
SEP = ("line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;"
       "rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;")
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
FRAME = ("rounded=1;arcSize=1;whiteSpace=wrap;html=1;verticalAlign=top;align=center;spacingTop=10;"
         "fontSize=22;fontStyle=1;fillColor=#F2F2F2;strokeColor=#666666;strokeWidth=2;")
ROWLBL = "text;html=1;fontSize=12;fontStyle=3;align=left;verticalAlign=middle;fontColor=#555555;"

cells = []


def v(id, val, style, x, y, w, h, parent=None):
    par = P + parent if parent else "1"
    cells.append(f'<mxCell id="{P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="{par}">'
                 f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')


def header(stereo, name, label, asal, inherit):
    t = (f"<font style='font-size:10px'>{stereo}</font><br><b>{name}</b><br>"
         f"<font style='font-size:10px'>{label} · dirancang {asal}</font>")
    t += f"<br><font style='font-size:10px' color='#6C4A87'><b>{inherit}</b></font>"
    return t


def size(attrs, methods):
    start = 10 + 15 * 4
    ah = max(1, len(attrs)) * LH + 8
    mh = (len(methods) * LH + 8) if methods else 0
    return start, ah, mh, start + ah + (8 + mh if methods else 0)


def cls(id, title, attrs, methods, x, y, h, kind):
    start, ah, mh, _ = size(attrs, methods)
    v(id, title, "swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;"
      f"startSize={start};horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;"
      f"marginBottom=0;whiteSpace=wrap;html=1;fontSize=12;{FILL[kind]}", x, y, W, h)
    v(id + "-a", "<br>".join(attrs), TXT, 0, start, W, ah, parent=id)
    if methods:
        v(id + "-s", "", SEP, 0, start + ah, W, 8, parent=id)
        v(id + "-m", "<br>".join(methods), TXT, 0, start + ah + 8, W, h - start - ah - 8, parent=id)


I = "&nbsp;&nbsp;&nbsp;"
ROWS = [
    ("Baris 1 · AbstractModel (mixin): perilaku bersama, tanpa tabel sendiri. Dipakai lewat _inherit = ['labfik.…mixin']", [
        ("apv", "mixin", header("«AbstractModel»", "<i>labfik.approval.mixin</i>", "Siklus pengesahan", "Tata Kelola",
                                "{_inherit: mail.thread}"),
         ["+ state: Selection {draf, diajukan, disahkan,", I + "diganti, dicabut, kedaluwarsa} = draf",
          "+ penyusun_id: hr.employee", "+ tanggal_ajukan: Datetime (readonly)", "+ berkas_ttd: Binary [0..1]",
          "+ pengesah_id: hr.employee [0..1] (readonly)", "+ pencatat_id: res.users [0..1] (readonly)",
          "+ tanggal_sah: Date [0..1] (readonly)", "+ log_ids: labfik.approval.log [*] {compute}"],
         ["+ action_ajukan()", "+ action_unggah_ttd(berkas)", "+ action_kembalikan(alasan)",
          "+ action_sahkan(pengesah, tanggal_sah)", "+ action_cabut(alasan)", "+ unlink() «override»",
          "# _jenis_dokumen(): str {abstract}", "# _cek_kelengkapan(): list {abstract}", "# _cek_wewenang(pengesah)",
          "# _sebelum_ajukan() {hook}", "# _sebelum_disahkan() {hook}", "# _dokumen_diganti(): recordset {hook}",
          "# _setelah_disahkan() {hook}"]),
        ("prd", "mixin", header("«AbstractModel»", "<i>labfik.period.mixin</i>", "Masa berlaku per periode", "Tata Kelola",
                                "{tanpa _inherit}"),
         ["+ periode_id: labfik.periode", "+ tanggal_mulai: Date {related}", "+ tanggal_selesai: Date {related}",
          "+ is_berlaku: Boolean {compute}"],
         ["+ berlaku_pada(tanggal): bool", "@model # _cron_kedaluwarsakan() (Pelengkap)"]),
        ("cri", "mixin", header("«AbstractModel»", "<i>labfik.criteria.mixin</i>", "Kriteria berurutan K1–K4", "Tata Kelola",
                                "{tanpa _inherit}"),
         ["+ kriteria_tertinggi: Integer {compute}"],
         ["+ get_kriteria(tanggal_acuan): dict", "# _compute_kriteria_tertinggi()",
          "# _cek_k1(tanggal) … _cek_k4(tanggal) {abstract}"]),
        ("evi", "mixin", header("«AbstractModel»", "<i>labfik.evidence.mixin</i>", "Rekaman bukti kegiatan", "Tata Kelola",
                                "{tanpa _inherit}"),
         ["+ tanggal: Date", "+ pelapor_id: hr.employee", "+ bukti_ids: ir.attachment [*]", "+ keterangan: Text [0..1]"],
         ["+ action_koreksi(nilai, alasan)", "+ unlink() «override» (selalu ditolak)", "# _boleh_dikoreksi(): bool {hook}"]),
    ]),
    ("Baris 2 · Personel dan Jabatan: dua model bawaan Odoo diperluas, plus dua tabel anak Jabatan", [
        ("emp", "odoo", header("«Odoo» diperluas [M]", "hr.employee", "Personel", "Tata Kelola",
                               "{extend: _inherit = 'hr.employee', tanpa _name baru}"),
         ["+ jenis_personel: Selection {dosen, laboran_plp,", I + "teknisi, asisten, petugas_k3}", "+ unit: Selection",
          "<i>bawaan dipakai: name, job_id, user_id [0..1]</i>"],
         ["+ unlink() «override» (ditolak bila dirujuk)"]),
        ("job", "odoo", header("«Odoo» diperluas [M]", "hr.job", "Jabatan", "Tata Kelola",
                               "{extend: _inherit = 'hr.job', tanpa _name baru}"),
         ["+ unit: Selection {lab_fik, prodi_if, prodi_si, fakultas}", "+ is_eksternal: Boolean",
          "+ atasan_id: hr.job [0..1]", "+ pengganti_id: hr.job [0..1]", "+ syarat_kompetensi: Text [0..1]",
          "+ tugas_ids: labfik.jabatan.tugas [*]", "+ wewenang_ids: labfik.jabatan.wewenang [*]",
          "+ is_lengkap: Boolean {compute}", "<i>bawaan dipakai: name</i>"],
         ["+ punya_wewenang(tindakan, jenis): bool", "@model + cari_pemegang_berwenang(tindakan, jenis)", I + ": hr.employee",
          "# _cek_atasan() @constrains (tanpa siklus)", "+ unlink() «override»"]),
        ("tgs", "baru", header("«Core» model baru [M]", "labfik.jabatan.tugas", "Tugas Jabatan", "Tata Kelola",
                               "{_name baru; anak hr.job}"),
         ["+ jabatan_id: hr.job", "+ urutan: Integer", "+ uraian: Text"], []),
        ("wwn", "baru", header("«Core» model baru [M]", "labfik.jabatan.wewenang", "Wewenang Jabatan", "Tata Kelola",
                               "{_name baru; anak hr.job}"),
         ["+ jabatan_id: hr.job", "+ tindakan: Selection {menyusun, mengesahkan}",
          "+ jenis_dokumen: Selection", I + "(modul lain menambah lewat selection_add)",
          "<i>unique(jabatan_id, tindakan, jenis_dokumen)</i>"], []),
    ]),
    ("Baris 3 · Master bersama: ruang, periode, mata kuliah, kelas", [
        ("rng", "baru", header("«Core» model baru [M]", "labfik.ruang", "Ruang Lab", "Tata Kelola", "{_name baru}"),
         ["+ kode: Char", "+ name: Char", "+ kapasitas: Integer"], []),
        ("per", "baru", header("«Core» model baru [M]", "labfik.periode", "Periode", "Tata Kelola", "{_name baru}"),
         ["+ name: Char", "+ jenis: Selection {semester, tahun_anggaran}", "+ tanggal_mulai: Date",
          "+ tanggal_selesai: Date"], []),
        ("mk", "baru", header("«Core» model baru [M]", "labfik.mata.kuliah", "Mata Kuliah", "Praktikum", "{_name baru}"),
         ["+ kode: Char «unique»", "+ name: Char", "+ prodi: Selection", "+ semester: Integer",
          "<i>tipe field: [USULAN PENULIS]</i>"], []),
        ("kls", "baru", header("«Core» model baru [M]", "labfik.kelas", "Kelas", "Praktikum", "{_name baru}"),
         ["+ mata_kuliah_id: labfik.mata.kuliah", "+ periode_id: labfik.periode", "+ name: Char",
          "+ jumlah_mahasiswa: Integer", "+ dosen_koordinator_id: hr.employee", "+ dosen_ids: hr.employee [*]",
          "<i>unique(mata_kuliah_id, periode_id, name)</i>", "<i>tipe field: [USULAN PENULIS]</i>"], []),
    ]),
]

grid_w = 4 * W + 3 * GX
y = Y0
for r, (lbl, boxes) in enumerate(ROWS):
    v(f"row{r + 1}", lbl, ROWLBL, X0, y, grid_w, 24)
    y += 30
    h = max(size(a, m)[3] for _, _, _, a, m in boxes)
    for c, (id, kind, title, attrs, methods) in enumerate(boxes):
        cls(id, title, attrs, methods, X0 + c * (W + GX), y, h, kind)
    y += h + GY

LEG = ("<b>Notasi</b> (UML class diagram, Wazlawick 2024 §13.6)<br>"
       "• Ungu, nama miring «AbstractModel» = mixin; tidak punya tabel sendiri. Model lain memakainya dengan "
       "<code>_inherit = ['labfik.approval.mixin', …]</code> dan mewarisi field serta method-nya.<br>"
       "• Abu-abu «Odoo» diperluas = model bawaan Odoo yang ditambah field dengan <code>_inherit</code> tanpa <code>_name</code>; "
       "nama model tetap <code>hr.employee</code> / <code>hr.job</code>.<br>"
       "• Putih «Core» model baru = model dengan <code>_name</code> sendiri di <code>labfik_core</code>.<br>"
       "• Relasi ditulis sebagai field: <code>nama_id: model</code> = Many2one; <code>[*]</code> = One2many/Many2many; "
       "<code>[0..1]</code> = boleh kosong.<br>"
       "• <code>+</code> publik, <code>#</code> internal. {abstract} = wajib diisi model turunan; {hook} = boleh diisi; "
       "«override» = mengganti method bawaan; {compute}/{related} = dihitung, tidak diisi pengguna.<br>"
       "• [M] master. Sesi dan Riwayat Pengesahan adalah transaksi [T] Core dan tidak digambar di halaman ini.")
USE = ("<b>Cara memakai Core</b><br>"
       "• Addon modul cukup <code>depends: ['labfik_core']</code>; <code>labfik_core</code> sendiri hanya <code>depends: ['hr', 'mail']</code>.<br>"
       "• Pakai, warisi, atau perluas dari addon modulmu; <b>jangan membuat versi sendiri</b> dan jangan mengubah Core. "
       "Butuh perubahan? Usulkan ke perancangnya (kolom \"dirancang\").<br>"
       "• Semua rujukan orang ke <code>hr.employee</code>. Asisten lab = <code>hr.employee</code> jenis <i>asisten</i>, jabatan "
       "<b>Asisten Praktikum</b>. Pihak eksternal tidak dicatat.<br>"
       "• Pengesahan: isi {abstract}/{hook}, jangan override <code>action_ajukan()</code>/<code>action_sahkan()</code>. "
       "Wewenang lewat <code>labfik.jabatan.wewenang</code> (tambah <code>jenis_dokumen</code> dengan <code>selection_add</code>).<br>"
       "• Tidak ada di Core: <code>labfik.controlled.mixin</code> (dihapus); Dokumen Induk, Versi, KPI (di <code>labfik_org</code>, "
       "pakai modul jembatan bila perlu).<br>"
       "• Grup akses Core: <code>labfik_pengguna</code> ⊂ <code>labfik_laboran</code> ⊂ <code>labfik_kalab</code>.")
SRC = ("<b>Sumber</b>: rancangan/kontrak-core.md (rangkuman branch febriyan-, herrens-, zahir-skripsi) · "
       "15 November 2026 · disusun Febriyan<br>"
       "Model rancangan Tata Kelola sudah final (DCD). Mata Kuliah dan Kelas dari Praktikum: nama field ditetapkan, "
       "tipe field <b>[USULAN PENULIS]</b> sampai DCD Praktikum.<br>"
       "<b>[KONFIRMASI kelompok]</b> penempatan semua model ini di <code>labfik_core</code>. "
       "Tampilan belum dicek di draw.io; struktur lolos validate.py.")

nw = (grid_w - 2 * GX) / 3
nh = 250
for k, (id, txt) in enumerate([("leg", LEG), ("use", USE), ("src", SRC)]):
    v(id, txt, NOTE, X0 + k * (nw + GX), y, nw, nh)
y += nh + 40

v("frame", "MODEL CORE · labfik_core (master dan mixin)", FRAME, X0 - 30, 20, grid_w + 60, y - 20)
cells.insert(0, cells.pop())  # bingkai digambar paling belakang

page_w, page_h = grid_w + 2 * X0 + 20, y + 40
xml = ('<mxfile host="app.diagrams.net" type="device">'
       f'<diagram id="{P}1" name="Model Core (1-1) - Master dan Mixin"><mxGraphModel dx="1600" dy="900" grid="1" '
       'gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
       f'pageWidth="{page_w:.0f}" pageHeight="{page_h:.0f}" math="0" shadow="0"><root><mxCell id="0"/>'
       '<mxCell id="1" parent="0"/>' + "".join(cells) + "</root></mxGraphModel></diagram></mxfile>")
with open(OUT, "w", encoding="utf-8") as f:
    f.write(xml)
print(f"{OUT}: {len(cells)} sel, halaman {page_w:.0f}×{page_h:.0f}")
