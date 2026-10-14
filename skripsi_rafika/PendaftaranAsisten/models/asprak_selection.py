# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api


class AsprakSelection(models.Model):
    _name = 'asprak.selection'
    _description = 'Asprak Selection'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    id_seleksi = fields.Char(
        'ID Seleksi',
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('asprak.selection') or 'SEL/0000'
    )
    tanggal_seleksi = fields.Date(
        'Tanggal Seleksi',
        default=fields.Date.today,
        required=True
    )
    registrasi_calon_asisten_id = fields.Many2one(
        'registrasi.asprak',
        'Registrasi Calon Asisten',
        required=True,
        tracking=True
    )
    dosen_penilai_id = fields.Many2one(
        'mst_dosen',
        'Dosen Penilai',
        tracking=True
    )
    total_nilai = fields.Float(
        'Total Nilai',
        compute='_compute_total_nilai',
        store=True
    )
    status_seleksi = fields.Selection([
        ('menunggu', 'Menunggu Penilaian'),
        ('review', 'Sedang Dinilai'),
        ('passed', 'Lulus'),
        ('failed', 'Gagal'),
    ], string='Status Seleksi', default='menunggu', tracking=True)

    line_ids = fields.One2many(
        'asprak.selection.line',
        'seleksi_id',
        string='Detail Penilaian'
    )

    @api.depends('line_ids.nilai_angka')
    def _compute_total_nilai(self):
        for record in self:
            record.total_nilai = sum(line.nilai_angka for line in record.line_ids)

    def action_mulai_penilaian(self):
        self.status_seleksi = 'review'

    def action_luluskan(self):
        self.status_seleksi = 'passed'

    def action_gagalkan(self):
        self.status_seleksi = 'failed'


class AsprakSelectionLine(models.Model):
    _name = 'asprak.selection.line'
    _description = 'Asprak Selection Line'

    seleksi_id = fields.Many2one(
        'asprak.selection',
        'Seleksi ID',
        required=True,
        ondelete='cascade'
    )
    kriteria_penilaian = fields.Selection([
        ('akademik', 'Akademik'),
        ('komunikasi', 'Komunikasi'),
        ('motivasi', 'Motivasi'),
        ('pengalaman', 'Pengalaman'),
    ], string='Kriteria Penilaian', required=True)
    nilai_angka = fields.Float('Nilai Angka')
    catatan_feedback = fields.Text('Catatan/Feedback')
