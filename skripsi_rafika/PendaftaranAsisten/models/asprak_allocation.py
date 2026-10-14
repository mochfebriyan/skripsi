# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api
# pyrefly: ignore [missing-import]
from odoo.exceptions import ValidationError


class AsprakAllocation(models.Model):
    _name = 'asprak.allocation'
    _description = 'Asprak Allocation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id_alokasi = fields.Char(
        'ID Alokasi',
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('asprak.allocation') or 'ALO/0000'
    )
    tanggal_penetapan = fields.Date(
        'Tanggal Penetapan',
        default=fields.Date.today,
        required=True
    )
    periode_semester_id = fields.Many2one(
        'mst_periodesemt',
        'Periode Semester',
        required=True,
        tracking=True
    )
    penanggung_jawab_lab_id = fields.Many2one(
        'res.users',
        'Penanggung Jawab Lab',
        required=True,
        tracking=True
    )
    status_alokasi = fields.Selection([
        ('draft', 'Draft'),
        ('allocated', 'Teralokasi'),
        ('done', 'Selesai/Disahkan'),
    ], string='Status Alokasi', default='draft', tracking=True)

    line_ids = fields.One2many(
        'asprak.allocation.line',
        'alokasi_id',
        string='Detail Alokasi'
    )

    def action_konfirmasi_plotting(self):
        self.status_alokasi = 'allocated'

    def action_sahkan_jadwal(self):
        self.status_alokasi = 'done'


class AsprakAllocationLine(models.Model):
    _name = 'asprak.allocation.line'
    _description = 'Asprak Allocation Line'

    alokasi_id = fields.Many2one(
        'asprak.allocation',
        'Alokasi ID',
        required=True,
        ondelete='cascade'
    )
    asisten_terpilih_id = fields.Many2one(
        'asprak.selection',
        'Asisten Terpilih',
        required=True,
        domain="[('status_seleksi', '=', 'passed')]"
    )
    mata_kuliah_id = fields.Many2one(
        'op.course',
        'Mata Kuliah',
        required=True
    )
    kelas_id = fields.Many2one(
        'op.batch',
        'Kelas',
        required=True
    )
    ruang_lab_id = fields.Many2one(
        'op.facility',
        'Ruang Lab',
        required=True
    )
    jadwal_waktu_id = fields.Many2one(
        'op.session',
        'Jadwal/Waktu',
        required=True
    )

    @api.constrains('jadwal_waktu_id', 'asisten_terpilih_id')
    def _check_validasi_skenario_usecase_5(self):
        for record in self:
            if not record.jadwal_waktu_id or not record.asisten_terpilih_id:
                continue

            # Skenario A2: Validasi Kuota Penuh (Maksimal 2 asisten per kelas/jadwal)
            alokasi_sama = self.search_count([
                ('jadwal_waktu_id', '=', record.jadwal_waktu_id.id),
                ('id', '!=', record.id),
                ('alokasi_id.status_alokasi', '!=', 'draft')
            ])
            if alokasi_sama >= 2:
                raise ValidationError("Mohon maaf, kuota asisten untuk kelas ini sudah penuh.")

            # Skenario A1: Validasi Jadwal Bentrok
            if record.jadwal_waktu_id.start_datetime and record.jadwal_waktu_id.end_datetime:
                bentrok = self.search([
                    ('asisten_terpilih_id', '=', record.asisten_terpilih_id.id),
                    ('id', '!=', record.id),
                    ('jadwal_waktu_id.start_datetime', '<', record.jadwal_waktu_id.end_datetime),
                    ('jadwal_waktu_id.end_datetime', '>', record.jadwal_waktu_id.start_datetime),
                    ('alokasi_id.status_alokasi', '!=', 'draft')
                ], limit=1)
                if bentrok:
                    raise ValidationError("Peringatan: Jadwal praktikum ini bentrok dengan jadwal KHS/praktikum mahasiswa yang bersangkutan.")