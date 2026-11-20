"""Model tipis untuk wireframe. Nama model dan field mengikuti design-class-tata-kelola.md;
aturan bisnis (AB) tidak diterapkan, tombol hanya mengubah status agar tampilan terisi."""
from odoo import api, fields, models

STATE = [
    ("draf", "Draf"),
    ("diajukan", "Diajukan"),
    ("disahkan", "Disahkan"),
    ("diganti", "Diganti"),
    ("dicabut", "Dicabut"),
    ("kedaluwarsa", "Kedaluwarsa"),
]


class HrJob(models.Model):
    _inherit = "hr.job"

    unit = fields.Selection([("lab_fik", "Lab FIK"), ("prodi_if", "Prodi IF"), ("prodi_si", "Prodi SI"),
                             ("fakultas", "Fakultas")], string="Unit")
    is_eksternal = fields.Boolean("Pejabat eksternal")
    atasan_id = fields.Many2one("hr.job", "Atasan")
    bawahan_ids = fields.One2many("hr.job", "atasan_id", "Bawahan")
    is_lengkap = fields.Boolean("Data jabatan lengkap", default=True)


class Periode(models.Model):
    _name = "labfik.periode"
    _description = "Periode"
    name = fields.Char("Nama", required=True)
    tanggal_mulai = fields.Date("Mulai")
    tanggal_selesai = fields.Date("Selesai")


class Kpi(models.Model):
    _name = "labfik.kpi"
    _description = "KPI"
    _rec_name = "nama"
    kode = fields.Char("Kode")
    nama = fields.Char("Nama KPI", required=True)
    satuan = fields.Char("Satuan")


class ApprovalLog(models.Model):
    _name = "labfik.approval.log"
    _description = "Riwayat Pengesahan"
    _order = "waktu desc"
    res_model = fields.Char("Model")
    res_id = fields.Integer("ID Rekaman")
    kejadian = fields.Selection([("diajukan", "Diajukan"), ("dikembalikan", "Dikembalikan"),
                                 ("berkas_diunggah", "Berkas diunggah"), ("disahkan", "Disahkan"),
                                 ("diganti", "Diganti"), ("dicabut", "Dicabut")], "Kejadian")
    waktu = fields.Datetime("Waktu")
    pelaku_id = fields.Many2one("hr.employee", "Pelaku")
    alasan = fields.Text("Alasan")


class ApprovalMixin(models.AbstractModel):
    _name = "labfik.approval.mixin"
    _description = "Mixin Pengesahan (tiruan)"

    state = fields.Selection(STATE, "Status", default="draf", tracking=True, group_expand="_expand_state")
    penyusun_id = fields.Many2one("hr.employee", "Penyusun")
    tanggal_ajukan = fields.Datetime("Tanggal diajukan", readonly=True)
    berkas_ttd = fields.Binary("Berkas bertanda tangan")
    berkas_ttd_nama = fields.Char()
    pengesah_id = fields.Many2one("hr.employee", "Pengesah", readonly=True)
    tanggal_sah = fields.Date("Tanggal sah", readonly=True)
    log_ids = fields.Many2many("labfik.approval.log", compute="_compute_log_ids", string="Riwayat")

    @api.model
    def _expand_state(self, states, domain, order):
        return ["draf", "diajukan", "disahkan"]

    def _compute_log_ids(self):
        Log = self.env["labfik.approval.log"]
        for rec in self:
            rec.log_ids = Log.search([("res_model", "=", rec._name), ("res_id", "=", rec.id)])

    def action_ajukan(self):
        self.write({"state": "diajukan", "tanggal_ajukan": fields.Datetime.now()})

    def action_terbitkan(self):
        return True

    def action_unggah_ttd(self):
        return True

    def action_kembalikan(self):
        self.write({"state": "draf"})

    def action_sahkan(self):
        self.write({"state": "disahkan", "tanggal_sah": fields.Date.today()})

    def action_cabut(self):
        self.write({"state": "dicabut"})


class Document(models.Model):
    _name = "labfik.document"
    _inherit = ["mail.thread"]
    _description = "Dokumen Induk"
    _rec_name = "judul"
    _order = "kode"

    kode = fields.Char("Kode", required=True)
    judul = fields.Char("Judul", required=True)
    jenis = fields.Selection([("sop", "SOP"), ("ik", "IK"), ("formulir", "Formulir"), ("eksternal", "Eksternal")], "Jenis")
    kategori = fields.Selection([("layanan", "Layanan"), ("praktikum", "Praktikum"), ("sarana", "Sarana"),
                                 ("k3", "K3")], "Kategori")
    asal = fields.Selection([("lab", "Lab"), ("fakultas", "Fakultas"), ("universitas", "Universitas")], "Asal")
    is_wajib = fields.Boolean("Wajib")
    dasar_kebutuhan = fields.Text("Dasar kebutuhan")
    siklus_tinjau_bulan = fields.Integer("Siklus tinjau (bulan)", default=12)
    active = fields.Boolean(default=True)
    versi_ids = fields.One2many("labfik.document.version", "document_id", "Versi")
    versi_berlaku_id = fields.Many2one("labfik.document.version", "Versi berlaku", compute="_compute_versi_berlaku")
    perlu_ditinjau = fields.Boolean("Perlu ditinjau", compute="_compute_versi_berlaku")
    memenuhi = fields.Boolean("Memenuhi syarat monev")

    @api.depends("versi_ids.state", "versi_ids.perlu_ditinjau")
    def _compute_versi_berlaku(self):
        for rec in self:
            rec.versi_berlaku_id = rec.versi_ids.filtered(lambda v: v.state == "disahkan")[:1]
            rec.perlu_ditinjau = rec.versi_berlaku_id.perlu_ditinjau


class DocumentVersion(models.Model):
    _name = "labfik.document.version"
    _inherit = ["labfik.approval.mixin", "mail.thread"]
    _description = "Versi Dokumen SOP/IK"
    _order = "document_id, revisi desc"

    document_id = fields.Many2one("labfik.document", "Dokumen Induk", required=True, ondelete="cascade")
    revisi = fields.Char("Revisi", required=True)
    berkas = fields.Binary("Berkas dokumen")
    berkas_nama = fields.Char()
    tanggal_efektif = fields.Date("Tanggal efektif")
    bagian_diubah = fields.Text("Bagian yang diubah")
    ringkasan_perubahan = fields.Text("Ringkasan perubahan")
    alasan_revisi = fields.Text("Alasan revisi")
    tanggal_tinjau_berikutnya = fields.Date("Tinjau berikutnya")
    perlu_ditinjau = fields.Boolean("Perlu ditinjau")
    jml_distribusi = fields.Integer("Distribusi")
    jml_sosialisasi = fields.Integer("Sosialisasi")
    jml_tinjau = fields.Integer("Tinjau Ulang")

    @api.depends("document_id.kode", "revisi")
    def _compute_display_name(self):
        for r in self:
            r.display_name = f"{r.document_id.kode} rev. {r.revisi}"

    def action_rekaman(self):
        return True


class Plan(models.Model):
    _name = "labfik.plan"
    _inherit = ["labfik.approval.mixin", "mail.thread"]
    _description = "Rencana"
    _rec_name = "judul"

    jenis = fields.Selection([("tahunan", "Rencana Kerja Tahunan"), ("pengembangan", "Rencana Pengembangan")],
                             "Jenis", required=True)
    judul = fields.Char("Judul", required=True)
    periode_id = fields.Many2one("labfik.periode", "Periode")
    narasi = fields.Html("Narasi")
    kriteria_tertinggi = fields.Integer("Kriteria tertinggi")
    line_ids = fields.One2many("labfik.plan.line", "plan_id", "Item Rencana")
    gap_ids = fields.One2many("labfik.plan.gap", "plan_id", "Temuan Gap")
    jml_tinjauan = fields.Integer("Tinjauan")

    def action_buat_revisi(self):
        return True

    def action_tinjauan(self):
        return True


class PlanLine(models.Model):
    _name = "labfik.plan.line"
    _description = "Item Rencana"
    _rec_name = "kegiatan"
    _order = "jadwal_mulai"

    plan_id = fields.Many2one("labfik.plan", "Rencana", required=True, ondelete="cascade")
    plan_state = fields.Selection(related="plan_id.state", string="Status rencana", store=True)
    kegiatan = fields.Char("Kegiatan", required=True)
    kpi_id = fields.Many2one("labfik.kpi", "KPI")
    target = fields.Float("Target")
    satuan = fields.Char("Satuan")
    pic_id = fields.Many2one("hr.employee", "PIC")
    jadwal_mulai = fields.Date("Mulai")
    jadwal_selesai = fields.Date("Selesai")
    currency_id = fields.Many2one("res.currency", default=lambda s: s.env.company.currency_id)
    anggaran = fields.Monetary("Anggaran")
    nilai_risiko = fields.Selection([("1", "1"), ("2", "2"), ("3", "3")], "Risiko")
    nilai_manfaat = fields.Selection([("1", "1"), ("2", "2"), ("3", "3")], "Manfaat")
    realisasi_ids = fields.One2many("labfik.realisasi", "line_id", "Realisasi")


class PlanGap(models.Model):
    _name = "labfik.plan.gap"
    _description = "Temuan Gap"
    _rec_name = "uraian_gap"

    plan_id = fields.Many2one("labfik.plan", "Rencana", required=True, ondelete="cascade")
    aspek = fields.Selection([("tridharma", "Tridharma"), ("kompetensi", "Kompetensi"), ("sarana", "Sarana"),
                              ("layanan", "Layanan")], "Aspek")
    kondisi_saat_ini = fields.Text("Kondisi saat ini")
    kebutuhan = fields.Text("Kebutuhan")
    uraian_gap = fields.Text("Uraian gap")


class Realisasi(models.Model):
    _name = "labfik.realisasi"
    _description = "Realisasi"
    _order = "line_id, periode_lapor"

    line_id = fields.Many2one("labfik.plan.line", "Item rencana", required=True, ondelete="cascade")
    periode_lapor = fields.Char("Periode lapor")
    tanggal = fields.Date("Tanggal")
    pelapor_id = fields.Many2one("hr.employee", "Pelapor")
    target = fields.Float(related="line_id.target", store=True, group_operator="max", string="Target")
    capaian = fields.Float("Capaian", group_operator="sum")
    currency_id = fields.Many2one(related="line_id.currency_id")
    biaya_terpakai = fields.Monetary("Biaya terpakai")
    status_capaian = fields.Selection([("tercapai", "Tercapai"), ("sebagian", "Sebagian"), ("belum", "Belum")],
                                      "Status capaian")
    tindak_lanjut = fields.Text("Tindak lanjut")


class OrgMonev(models.Model):
    """Di DCD ini AbstractModel layanan tanpa tabel; untuk wireframe hasil get_status() disimpan sebagai baris rekaan."""
    _name = "labfik.org.monev"
    _description = "Status Monev"
    _order = "urutan"

    urutan = fields.Integer()
    pkg = fields.Char("PKG")
    indikator = fields.Char("Indikator")
    jenis_skor = fields.Char("Jenis skor")
    status = fields.Char("Status")
    rincian = fields.Text("Rincian")
    sumber = fields.Char("Sumber data")
