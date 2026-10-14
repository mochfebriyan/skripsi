# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api, _

class MstPeriodeSemt(models.Model):
    _name = 'mst_periodesemt'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Master Periode Semester'

    # ID otomatis: dibuat readonly, copy=False, dan default 'New'
    id_periode_semester = fields.Char(
        string='ID Periode Semester', 
        required=True, 
        copy=False, 
        readonly=True, 
        default=lambda self: _('New'), 
        tracking=True
    )
    tahun_semester = fields.Char('Tahun Semester', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    deadline = fields.Date('Deadline Pendaftaran', tracking=True)
    name = fields.Char(string="Nama Periode")
    deadline_date = fields.Date(string="Deadline Pendaftaran")
    poster_img = fields.Image(string="Poster Rekrutmen")
    link_pendaftaran = fields.Char(string="Link Portal Pendaftaran", default="/pendaftaran-asisten", readonly=True, help="Link otomatis ke portal pendaftaran mahasiswa")
    skep_file = fields.Binary(string="Dokumen SKEP Rektor (PDF)", attachment=True)
    skep_filename = fields.Char(string="Nama File SKEP")
    deadline_alokasi = fields.Datetime(string="Batas Waktu Alokasi Jadwal")

    _sql_constraints = [
        ('unique_id_periode_semester', 'unique(id_periode_semester)', 'ID Periode Semester harus unik!'),
    ]

    # Override metode create untuk men-generate ID saat record baru disimpan
    @api.model
    def create(self, vals):
        if vals.get('id_periode_semester', _('New')) == _('New'):
            # Menarik format sequence dari XML
            vals['id_periode_semester'] = self.env['ir.sequence'].next_by_code('mst.periodesemt.sequence') or _('New')
        return super(MstPeriodeSemt, self).create(vals)

    # =========================================================================
    # CRON: Update status asisten aktif harian
    # =========================================================================
    @api.model
    def _cron_update_status_asisten(self):
        # Cari periode aktif yang deadline alokasinya sudah lewat
        periode_aktif = self.search([
            ('active', '=', True),
            ('deadline_alokasi', '<', fields.Datetime.now()),
        ], limit=1)

        if not periode_aktif:
            return

        # Ambil semua ID op.student yang ada di asisten_ids pada jadwal manapun
        semua_jadwal = self.env['jadwal.praktikum'].search([])
        student_ids_aktif = set()
        for jadwal in semua_jadwal:
            for student in jadwal.asisten_ids:
                student_ids_aktif.add(student.id)

        # Cari semua op.student yang seleksinya lulus (passed)
        seleksi_lulus = self.env['asprak.selection'].search([
            ('status_seleksi', '=', 'passed')
        ])
        students_lulus = seleksi_lulus.mapped(
            'registrasi_calon_asisten_id.mahasiswa_id'
        )

        for student in students_lulus:
            if student.id in student_ids_aktif:
                student.is_active_assistant = True
            else:
                student.is_active_assistant = False