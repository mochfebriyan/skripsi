# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api

class MstKodeKelas(models.Model):
    _name = 'mst_kodekelas'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Master Kode Kelas'
    _rec_name = 'nama_kelas'

    id_kode_kelas = fields.Char('ID Kode Kelas', required=True, readonly=True, copy=False, default='New', tracking=True)
    kode_kelas = fields.Char('Kode Kelas', required=True, tracking=True)
    nama_kelas = fields.Char('Nama Kelas', required=True, tracking=True)

    # =====================================================================
    # TAMBAHAN REVISI 13: ASSOCIATE KE MODUL OPENEDUCAT
    # Menghubungkan tabel kelas mandiri ini dengan master batch/kelas bawaan
    # =====================================================================
    op_batch_id = fields.Many2one(
        'op.batch',
        string='Relasi Batch/Kelas OpenEduCat',
        help='Relasi associate ke master data batch/kelas OpenEduCat'
    )

    _sql_constraints = [
        ('unique_id_kode_kelas', 'unique(id_kode_kelas)', 'ID Kode Kelas harus unik!'),
        ('unique_kode_kelas', 'unique(kode_kelas)', 'Kode Kelas harus unik!'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('id_kode_kelas') or vals.get('id_kode_kelas') == 'New':
                vals['id_kode_kelas'] = self.env['ir.sequence'].next_by_code('mst.kodekelas.sequence') or 'New'
        return super().create(vals_list)

    def name_get(self):
        result = []
        for rec in self:
            label = f"[{rec.kode_kelas}] {rec.nama_kelas}" if rec.kode_kelas else rec.nama_kelas
            result.append((rec.id, label))
        return result