# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api

class MstDosen(models.Model):
    _name = 'mst_dosen'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Master Dosen'

    id_dosen = fields.Char('ID Dosen', required=True, readonly=True, copy=False, default='New', tracking=True)
    kode_dosen = fields.Char('Kode Dosen', required=True, tracking=True)
    nama_dosen = fields.Char('Nama Dosen', required=True, tracking=True)

    # =====================================================================
    # TAMBAHAN REVISI 13: ASSOCIATE KE MODUL OPENEDUCAT
    # Menghubungkan tabel mst_dosen mandiri ini dengan master dosen bawaan
    # =====================================================================
    op_faculty_id = fields.Many2one(
        'op.faculty', 
        string='Relasi Dosen OpenEduCat',
        help='Relasi associate ke master data dosen OpenEduCat'
    )

    _sql_constraints = [
        ('unique_id_dosen', 'unique(id_dosen)', 'ID Dosen harus unik!'),
        ('unique_kode_dosen', 'unique(kode_dosen)', 'Kode Dosen harus unik!'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('id_dosen') or vals.get('id_dosen') == 'New':
                vals['id_dosen'] = self.env['ir.sequence'].next_by_code('mst.dosen.sequence') or 'New'
        return super().create(vals_list)

    @api.depends('kode_dosen', 'nama_dosen')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"[{record.kode_dosen}] {record.nama_dosen}" if record.kode_dosen else record.nama_dosen