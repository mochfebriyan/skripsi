# 7. mst_role.py
# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields 

class MstRole(models.Model):
    _name = 'mst_role'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Master Role'

    id_master_role = fields.Char('Id Master Role', required=True, tracking=True)
    nama_role = fields.Char('Nama Role', required=True, tracking=True)

    _sql_constraints = [
        ('unique_id_master_role', 'unique(id_master_role)', 'Id Master Role harus unik!'),
    ]