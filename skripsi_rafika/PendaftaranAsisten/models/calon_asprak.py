# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api, _
# pyrefly: ignore [missing-import]
from odoo.exceptions import ValidationError

class CalonAsprakRegist(models.Model):
    _name = 'registrasi.asprak'
    _description = 'Calon Asprak Registration'
    _inherit = ['mail.thread']
    _rec_name = 'id_registrasi'

    id_registrasi = fields.Char(
        'ID Registrasi',
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('calon.asprak.regist') or 'REG/0000'
    )
    tanggal_pendaftaran = fields.Date(
        'Tanggal Pendaftaran',
        default=fields.Date.today,
        required=True
    )
    mahasiswa_id = fields.Many2one('op.student', string='Mahasiswa', required=True)
    periode_semester_id = fields.Many2one('mst_periodesemt', string='Periode', required=True)

    phone_number = fields.Char(string="Nomor HP/WhatsApp")
    berkas_khs = fields.Binary(string='Berkas KHS', attachment=True, required=False) # Ubah jadi False

    # 1. Tambahkan status lolos dan tidak_lolos di field state
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Menunggu Seleksi'),
        ('lolos', 'Lolos'),
        ('tidak_lolos', 'Tidak Lolos'),
        ('canceled', 'Dibatalkan'),
    ], string='Status Pendaftaran', default='draft')

    # 2. Tambahkan fungsi untuk tombol "Luluskan"
    def action_luluskan(self):
        for record in self:
            record.state = 'lolos'

            # Check if a selection record already exists for this registration
            existing_seleksi = self.env['asprak.selection'].search([
                ('registrasi_calon_asisten_id', '=', record.id)
            ], limit=1)

            # If it does not exist, automatically generate a new record in 'menunggu' state
            if not existing_seleksi:
                self.env['asprak.selection'].create({
                    'registrasi_calon_asisten_id': record.id,
                    'tanggal_seleksi': fields.Date.today(),
                    'status_seleksi': 'menunggu',
                })

    # 3. Tambahkan fungsi untuk tombol "Tolak"
    def action_tolak(self):
        for record in self:
            record.state = 'tidak_lolos'

    # ✅ One2many ke detail — pendaftar bisa pilih >1 mata kuliah
    detail_ids = fields.One2many(
        'calon.asprak.detail',
        'registrasi_id',
        string='Detail Registrasi'
    )

    @api.constrains('berkas_khs')
    def _check_file_size(self):
        for record in self:
            if record.berkas_khs:
                file_size = len(record.berkas_khs) * 3 / 4
                if file_size > 2 * 1024 * 1024:
                    raise ValidationError("Ukuran file KHS tidak boleh melebihi 2MB.")

    @api.constrains('periode_semester_id')
    def _check_periode_aktif(self):
        from datetime import date
        for record in self:
            if record.periode_semester_id:
                if hasattr(record.periode_semester_id, 'active') and not record.periode_semester_id.active:
                    raise ValidationError("Periode pendaftaran telah ditutup atau tidak aktif.")
                if hasattr(record.periode_semester_id, 'deadline') and record.periode_semester_id.deadline:
                    if record.periode_semester_id.deadline < date.today():
                        raise ValidationError("Periode pendaftaran telah ditutup.")

    @api.constrains('detail_ids')
    def _check_no_duplicate_matkul(self):
        """Cegah pendaftar pilih mata kuliah yang sama lebih dari sekali"""
        for record in self:
            matkul_ids = record.detail_ids.mapped('mata_kuliah_target_id').ids
            if len(matkul_ids) != len(set(matkul_ids)):
                raise ValidationError(_('Tidak boleh memilih mata kuliah yang sama lebih dari sekali!'))

    def action_submit_registration(self):
        for record in self:
            if not record.berkas_khs:
                raise ValidationError('Berkas KHS wajib diunggah sebelum mengirim pendaftaran!')
            if not record.detail_ids:
                raise ValidationError('Pilih minimal 1 mata kuliah target!')
            record.state = 'submitted'


class CalonAsprakDetail(models.Model):
    _name = 'calon.asprak.detail'
    _description = 'Calon Asprak Detail'

    registrasi_id = fields.Many2one(
        'registrasi.asprak',
        'Registrasi ID',
        required=True,
        ondelete='cascade'
    )

    # ✅ FIX: pakai 'mst_coursesemt' (underscore, sesuai _name di mst_coursesemt.py)
    mata_kuliah_target_id = fields.Many2one(
        'mst_coursesemt',
        string='Mata Kuliah Target',
        required=True,
        domain=[('is_praktikum_lab', '=', True)]  # ← opsional: filter hanya praktikum
    )
    nilai_mata_kuliah = fields.Float('Nilai Mata Kuliah')