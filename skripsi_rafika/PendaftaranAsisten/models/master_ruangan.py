    # 1. master_ruangan.py
# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields

class LabMasterRuangan(models.Model):
    _name = 'lab.master.ruangan'
    _description = 'Master Data Ruangan Laboratorium'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nama Ruangan', required=True, tracking=True)
    kode_ruangan = fields.Char(string='Kode Ruangan', required=True, tracking=True)
    kapasitas = fields.Integer(string='Kapasitas', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)

    _sql_constraints = [
        ('kode_ruangan_uniq', 'unique(kode_ruangan)', 'Kode Ruangan sudah digunakan! Kode harus unik.')
    ]