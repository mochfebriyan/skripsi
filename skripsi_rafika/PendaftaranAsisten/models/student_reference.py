# e:\SKRIPSIAPP\openeducat_erp\PendaftaranAsisten\models\student_reference.py
# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields


class OpStudent(models.Model):
    _inherit = 'op.student'

    student_identifier = fields.Char('ID Student')
    nim = fields.Char('NIM')
    program_studi_id = fields.Many2one('op.course', 'Program Studi')
    is_active_assistant = fields.Boolean(string="Status Asisten Aktif", default=False)