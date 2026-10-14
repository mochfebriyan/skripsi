# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api

class SarprasChecklist(models.Model):
    _name = 'sarpras.checklist'
    _description = 'Checklist Kesiapan Sarana & Prasarana'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'check_date desc, id desc'

    name = fields.Char(
        string='Nama Laporan',
        required=True,
        tracking=True,
        help='Contoh: Checklist Lab - 17 Mei 2026',
    )
    laboran_id = fields.Many2one(
        'res.users',
        string='Pencatat (Laboran)',
        default=lambda self: self.env.user,
        required=True,
        readonly=True,
        tracking=True,
    )
    
    # Field baru dengan nama kelas_id, nembak ke mst_kodekelas
    kelas_id = fields.Many2one(
        'mst_kodekelas',
        string='Ruangan Lab',
        required=True,
        tracking=True,
    )
    
    check_date = fields.Datetime(
        string='Waktu Pengecekan',
        default=fields.Datetime.now,
        required=True,
        readonly=True,
        tracking=True,
    )
    kondisi_fisik = fields.Selection(
        selection=[
            ('baik', 'Baik'),
            ('rusak', 'Rusak'),
        ],
        string='Kondisi Fisik',
        required=True,
        tracking=True,
    )
    catatan_kerusakan = fields.Text(
        string='Detail Kerusakan Fisik',
        tracking=True,
    )
    kesiapan_software = fields.Selection(
        selection=[
            ('tersedia', 'Tersedia'),
            ('perlu_bantuan', 'Perlu Bantuan Instalasi'),
        ],
        string='Kesiapan Software',
        required=True,
        tracking=True,
    )
    state = fields.Selection(
        selection=[
            ('ready', 'Siap'),
            ('issue', 'Ada Kendala'),
        ],
        string='Status Keseluruhan',
        compute='_compute_state',
        store=True,
        tracking=True,
        readonly=True,
    )

    @api.depends('kondisi_fisik', 'kesiapan_software')
    def _compute_state(self):
        for rec in self:
            if rec.kondisi_fisik == 'rusak' or rec.kesiapan_software == 'perlu_bantuan':
                rec.state = 'issue'
            else:
                rec.state = 'ready'