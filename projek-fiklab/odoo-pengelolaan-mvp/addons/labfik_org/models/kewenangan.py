# -*- coding: utf-8 -*-
from odoo import fields, models


class LabfikKewenangan(models.Model):
    _name = 'labfik.kewenangan'
    _description = 'Kewenangan (kolom matriks kewenangan)'
    _order = 'sequence, id'

    name = fields.Char('Kewenangan', required=True)
    deskripsi = fields.Text('Deskripsi')
    sequence = fields.Integer(default=10)
    jabatan_ids = fields.Many2many('labfik.jabatan', 'labfik_jabatan_kewenangan_rel',
                                   'kewenangan_id', 'jabatan_id', string='Jabatan')
    active = fields.Boolean(default=True)
