"""Katalog model Core (labfik_core): mixin, master, dan transaksi.

Pemakaian:
    python3 -I projek-fiklab/tools/drawio/core/model_core.py projek-fiklab/rancangan/model-core.drawio
    python3 -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/model-core.drawio core-

Sumber isi: projek-fiklab/rancangan/kontrak-core.md (15 November 2026; master aset dari kelompok Aset & Safety
digabung 16 November 2026).
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
        ("evi", "mixin", header("«AbstractModel»", "<i>labfik.evidence.mixin</i>", "Rekaman bukti kegiatan & hasil uji", "Tata Kelola",
                                "{tanpa _inherit}"),
         ["+ tanggal: Date", "+ pelapor_id: hr.employee", "+ bukti_ids: ir.attachment [*]", "+ keterangan: Text [0..1]"],
         ["+ action_koreksi(nilai, alasan)", "+ unlink() «override» (selalu ditolak)", "# _boleh_dikoreksi(): bool {hook}"]),
    ]),
    ("Baris 2 · Personel dan Jabatan: dua model bawaan Odoo diperluas, plus dua tabel anak Jabatan", [
        ("emp", "odoo", header("«Odoo» diperluas [M]", "hr.employee", "Personel", "Tata Kelola & Aset",
                               "{extend: _inherit = 'hr.employee', tanpa _name baru}"),
         ["+ jenis_personel: Selection {dosen, laboran_plp,", I + "teknisi, asisten, petugas_k3}", "+ unit: Selection",
          "+ aset_dikelola_ids: labfik.alat [*]", I + "(kebalikan alat.penanggung_jawab_id)",
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
          "+ jenis_dokumen: Selection {sop_ik, renstra,", I + "rencana_tahunan, rencana_pengembangan, sk_penetapan}",
          I + "modul lain menambah lewat selection_add,", I + "mis. Aset: baso, usulan_disposal, program_pemeliharaan",
          "<i>unique(jabatan_id, tindakan, jenis_dokumen)</i>"], []),
    ]),
    ("Baris 3 · Master bersama: ruang, periode, mata kuliah, kelas", [
        ("rng", "baru", header("«Core» model baru [M]", "labfik.ruang", "Ruang Lab", "Tata Kelola, Praktikum & Aset",
                               "{_name baru}"),
         ["+ kode: Char «unique»", "+ name: Char", "+ kapasitas: Integer (kursi mahasiswa)",
          "+ penanggung_jawab_id: hr.employee [0..1]", "+ alat_ids: labfik.alat [*]",
          "+ workstation_count: Integer {compute} (jumlah PC)"], []),
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
    ("Baris 4 · Master bersama domain aset dan fasilitas (usulan kelompok Aset & Safety, digabung 16 November 2026)", [
        ("alt", "baru", header("«Core» model baru [M]", "labfik.alat", "Peralatan Lab (inventaris per unit)", "Aset (PKG-07)",
                               "{_name baru}"),
         ["+ kode_operasional: Char «unique» (QR unit)", "+ kode_bmn: Char [0..1]", "+ nup: Integer [0..1]", "+ name: Char",
          "+ kategori_id: labfik.alat.kategori", "+ ruang_id: labfik.ruang",
          "+ lokasi_simpan_id: labfik.lokasi.simpan [0..1]", "+ serial_number: Char [0..1]",
          "+ kondisi: Selection {baik, rusak_ringan, rusak_berat}",
          "+ status: Selection {tersedia, dipinjam, perbaikan, afkir}", "+ penanggung_jawab_id: hr.employee",
          "+ is_perlu_kalibrasi: Boolean (awal dari kategori)", "+ tgl_terakhir_verifikasi: Date [0..1]"],
         ["+ action_set_tersedia()", "+ action_set_perbaikan()", "+ check_ketersediaan_sesi(sesi): bool {hook}"]),
        ("kat", "baru", header("«Core» model baru [M]", "labfik.alat.kategori", "Kategori Peralatan", "Aset (PKG-07/08)",
                               "{_name baru}"),
         ["+ kode: Char «unique»", "+ name: Char",
          "+ jenis: Selection {hardware_pc, instrumen_ukur,", I + "jaringan, mesin_lab, multimedia}",
          "+ rasio_per_mahasiswa: Float (standar PKG-08)", "+ interval_pemeliharaan_bulan: Integer",
          "+ butuh_kalibrasi_internal: Boolean"], []),
        ("lks", "baru", header("«Core» model baru [M]", "labfik.lokasi.simpan", "Sub-Lokasi Simpan (rak/meja)",
                               "Aset & Safety", "{_name baru; anak labfik.ruang}"),
         ["+ ruang_id: labfik.ruang (induk)", "+ kode: Char", "+ name: Char",
          "+ jenis: Selection {meja_workstation, rak_penyimpanan,", I + "lemari_alat, lemari_b3, laci}",
          "+ kapasitas_tampung: Integer", "+ keterangan: Text [0..1]", "<i>unique(ruang_id, kode)</i>"], []),
        ("bhn", "baru", header("«Core» model baru [M]", "labfik.bahan", "Bahan Praktikum (habis pakai)",
                               "Aset & Safety (PKG-07/11)", "{_name baru}"),
         ["+ kode: Char «unique»", "+ name: Char", "+ satuan: Char (pcs, roll, box, ml)",
          "+ jenis: Selection {elektronika, kabel_konektor,", I + "cairan_kimia, reagen, atki}",
          "+ stok_minimum: Float", "+ lokasi_simpan_id: labfik.lokasi.simpan", "+ is_berbahaya_b3: Boolean (dipakai Safety)",
          "<i>stok berjalan di addon Aset, bukan Core</i>"], []),
    ]),
    ("Baris 5 · Transaksi Core: riwayat pengesahan dan sesi praktikum", [
        ("log", "baru", header("«Core» model baru [T]", "labfik.approval.log", "Riwayat Pengesahan", "Tata Kelola",
                               "{_name baru; ditulis approval.mixin}"),
         ["+ res_model: Char", "+ res_id: Integer", "+ kejadian: Selection {diajukan, dikembalikan,",
          I + "berkas_diunggah, disahkan, diganti, dicabut, kedaluwarsa}", "+ waktu: Datetime",
          "+ pelaku_id: res.users [0..1]", "+ pengesah_id: hr.employee [0..1]", "+ alasan: Text [0..1]",
          "+ berkas: Binary [0..1]"],
         ["+ write() «override» (selalu ditolak)", "+ unlink() «override» (selalu ditolak)"]),
        ("ses", "baru", header("«Core» model baru [T]", "labfik.sesi", "Sesi Praktikum", "Praktikum",
                               "{_name baru; tidak mewarisi op.session}"),
         ["+ kelas_id: labfik.kelas", "+ pertemuan_ke: Integer", "+ jenis_pertemuan: Selection {praktikum, uts, uas}",
          "+ moda: Selection {luring, daring}", "+ tanggal: Date", "+ jam_mulai: Float", "+ jam_selesai: Float",
          "+ ruang_id: labfik.ruang", "+ state: Selection {terjadwal, terlaksana, batal}",
          "+ sesi_asal_id: labfik.sesi [0..1] (bila pengganti)",
          "+ is_terpublikasi, is_ditunda, is_diganti: Boolean {compute}", "<i>tipe field: [USULAN PENULIS]</i>"], []),
    ]),
]

SESI = ("<b>Aturan pakai bersama transaksi Core</b><br><br>"
        "<b>labfik.sesi</b> [USULAN PENULIS; KONFIRMASI kelompok]<br>"
        "• Dibangkitkan hanya oleh PKG-15 (Praktikum), atau sebagai sesi pengganti lewat Perubahan Sesi PKG-18.<br>"
        "• Satu Sesi asli per (kelas, pertemuan).<br>"
        "• Hanya modul Praktikum yang mengubah <code>state</code>.<br>"
        "• Modul lain <b>tidak menambah field</b> ke <code>labfik.sesi</code>; buat model sendiri yang merujuk "
        "<code>sesi_id</code> (mis. penugasan petugas di SDM).<br>"
        "• Sesi yang sudah punya jurnal atau penugasan tidak boleh dihapus.<br>"
        "• Status lain dihitung, tidak disimpan: terpublikasi = jadwal periode disahkan; ditunda = ada perubahan "
        "yang belum diputuskan; diganti = ada sesi yang merujuk sesi ini lewat <code>sesi_asal_id</code>.<br><br>"
        "<b>labfik.approval.log</b><br>"
        "• Tidak diisi langsung oleh modul: setiap baris dibuat <code>approval.mixin</code> saat status dokumen berubah.<br>"
        "• Satu tabel untuk semua dokumen yang disahkan (<code>res_model</code> + <code>res_id</code>); "
        "tidak bisa diubah atau dihapus.")

grid_w = 4 * W + 3 * GX
y = Y0
for r, (lbl, boxes) in enumerate(ROWS):
    v(f"row{r + 1}", lbl, ROWLBL, X0, y, grid_w, 24)
    y += 30
    h = max(size(a, m)[3] for _, _, _, a, m in boxes)
    if len(boxes) < 4:
        h = max(h, 330)  # beri ruang untuk catatan aturan pakai
    for c, (id, kind, title, attrs, methods) in enumerate(boxes):
        cls(id, title, attrs, methods, X0 + c * (W + GX), y, h, kind)
    if len(boxes) < 4:  # sisa kolom baris transaksi diisi catatan aturan pakai
        x = X0 + len(boxes) * (W + GX)
        v("sesi-aturan", SESI, NOTE, x, y, X0 + grid_w - x, h)
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
       "• [M] master, [T] transaksi. Model aset (Baris 4) master saja; transaksinya di addon Aset/Safety. Sesi adalah satu-satunya transaksi bisnis di Core; Riwayat Pengesahan adalah log teknis milik approval.mixin.")
USE = ("<b>Cara memakai Core</b><br>"
       "• Addon modul cukup <code>depends: ['labfik_core']</code>; <code>labfik_core</code> sendiri hanya <code>depends: ['hr', 'mail']</code>.<br>"
       "• Pakai, warisi, atau perluas dari addon modulmu; <b>jangan membuat versi sendiri</b> dan jangan mengubah Core. "
       "Butuh perubahan? Usulkan ke perancangnya (kolom \"dirancang\").<br>"
       "• Semua rujukan orang ke <code>hr.employee</code>. Asisten lab = <code>hr.employee</code> jenis <i>asisten</i>, jabatan "
       "<b>Asisten Praktikum</b>. Pihak eksternal tidak dicatat.<br>"
       "• Pengesahan: isi {abstract}/{hook}, jangan override <code>action_ajukan()</code>/<code>action_sahkan()</code>. "
       "Wewenang lewat <code>labfik.jabatan.wewenang</code> (tambah <code>jenis_dokumen</code> dengan <code>selection_add</code>).<br>"
       "• Tidak ada di Core: <code>labfik.controlled.mixin</code> (dihapus); Dokumen Induk, Versi, KPI (di <code>labfik_org</code>, "
       "pakai modul jembatan bila perlu).")
GRP = ("<b>Grup akses Core</b> (<code>res.groups</code>, data XML <code>labfik_core</code>; bukan model)<br><br>"
       "<code>base.group_user</code><br>"
       "&nbsp;└ <b>labfik_pengguna</b>: membaca dokumen yang sudah <i>disahkan</i><br>"
       "&nbsp;&nbsp;&nbsp;&nbsp;└ <b>labfik_laboran</b>: mencatat dokumen, realisasi, rekaman bukti<br>"
       "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ <b>labfik_kalab</b>: semua master; mengembalikan, mengesahkan, mencabut<br><br>"
       "• Grup lebih tinggi mewarisi hak grup di bawahnya (<code>implied_ids</code>).<br>"
       "• Grup ≠ jabatan. Siapa yang berwenang <b>mengesahkan sebagai pejabat</b> diatur "
       "<code>labfik.jabatan.wewenang</code>, bukan grup; karena itu Dekan tidak perlu akun.<br>"
       "• Aturan penempatan: grup masuk Core bila dirujuk kode Core atau dipakai lebih dari satu modul; "
       "selain itu di modul pemakainya. Contoh: <code>labfik_dosen</code>, <code>labfik_asisten</code> ada di "
       "<code>labfik_praktikum</code>, bukan Core.")
ASET = ("<b>Aturan pakai bersama domain aset</b> [KONFIRMASI kelompok Aset & Safety]<br>"
        "• Praktikum (PKG-15/18) mengecek ketersediaan PC/alat lewat <code>labfik.alat</code> di ruang terkait, tanpa tabel duplikat.<br>"
        "• Safety (PKG-11/17) memakai <code>labfik.alat</code> untuk inspeksi K3 berkala (APAR, kelistrikan) dan "
        "<code>labfik.lokasi.simpan</code> untuk lemari B3.<br>"
        "• Hanya addon Aset yang mengubah <code>status</code> alat; modul lain hanya membaca.<br>"
        "• <code>check_ketersediaan_sesi()</code> di Core hanya memeriksa <code>status</code> dan <code>ruang_id</code>; "
        "addon Aset meng-<i>override</i>-nya untuk menambah cek peminjaman.<br>"
        "• Kalibrasi internal oleh laboran; hasil uji dicatat lewat <code>evidence.mixin</code>.<br>"
        "• Berita acara (BASO, usulan afkir) disahkan lewat <code>approval.mixin</code>.")
SRC = ("<b>Sumber</b>: rancangan/kontrak-core.md (rangkuman branch febriyan-, herrens-, zahir-skripsi, ditambah usulan kelompok "
       "Aset & Safety) · 15 November 2026, diperbarui 16 November 2026 · disusun Febriyan<br>"
       "Model rancangan Tata Kelola sudah final (DCD). Mata Kuliah, Kelas, dan Sesi dari Praktikum: nama field ditetapkan, "
       "tipe field <b>[USULAN PENULIS]</b> sampai DCD Praktikum.<br>"
       "<b>[KONFIRMASI kelompok]</b> penempatan semua model ini di <code>labfik_core</code>. "
       "Tampilan belum dicek di draw.io; struktur lolos validate.py.")

nw = (grid_w - 3 * GX) / 4
nh = 360
for k, (id, txt) in enumerate([("leg", LEG), ("use", USE), ("grp", GRP), ("aset-aturan", ASET)]):
    v(id, txt, NOTE, X0 + k * (nw + GX), y, nw, nh)
y += nh + GY
v("src", SRC, NOTE, X0, y, grid_w, 80)
y += 80 + 40

v("frame", "MODEL CORE · labfik_core (mixin, master, master aset, dan transaksi)", FRAME, X0 - 30, 20, grid_w + 60, y - 20)
cells.insert(0, cells.pop())  # bingkai digambar paling belakang

page_w, page_h = grid_w + 2 * X0 + 20, y + 40
xml = ('<mxfile host="app.diagrams.net" type="device">'
       f'<diagram id="{P}1" name="Model Core (1-1) - Mixin, Master, Aset, dan Transaksi"><mxGraphModel dx="1600" dy="900" grid="1" '
       'gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
       f'pageWidth="{page_w:.0f}" pageHeight="{page_h:.0f}" math="0" shadow="0"><root><mxCell id="0"/>'
       '<mxCell id="1" parent="0"/>' + "".join(cells) + "</root></mxGraphModel></diagram></mxfile>")
with open(OUT, "w", encoding="utf-8") as f:
    f.write(xml)
print(f"{OUT}: {len(cells)} sel, halaman {page_w:.0f}×{page_h:.0f}")
