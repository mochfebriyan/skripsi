# 5. mst_kurikulum.py
# -*- coding: utf-8 -*-
from odoo import models, fields

class MstKurikulum(models.Model):
    _name = 'mst_kurikulum'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Master Kurikulum'

    id_course_kurikulum = fields.Char('ID Course Kurikulum', required=True, tracking=True)
    kode_mata_kuliah = fields.Char('Kode Mata Kuliah', required=True, tracking=True)
    nama_mata_kuliah = fields.Char('Nama Mata Kuliah', required=True, tracking=True)

    _sql_constraints = [
        ('unique_id_course_kurikulum', 'unique(id_course_kurikulum)', 'ID Course Kurikulum harus unik!'),
        ('unique_kode_mata_kuliah', 'unique(kode_mata_kuliah)', 'Kode Mata Kuliah harus unik!'),
    ]