# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LabfikRuang(models.Model):
    _name = 'labfik.ruang'
    _description = 'Ruang atau lokasi penggunaan dokumen'
    _order = 'kode'

    kode = fields.Char('Kode', required=True)
    name = fields.Char('Nama', required=True)
    lokasi = fields.Char('Lokasi', help='Gedung dan lantai')
    is_virtual = fields.Boolean('Lokasi daring', help='Contoh: Portal LabFIK')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('kode_unique', 'unique(kode)', 'Kode ruang sudah dipakai.'),
    ]

    @api.depends('kode', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = '%s · %s' % (rec.kode, rec.name) if rec.kode else rec.name
