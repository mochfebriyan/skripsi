# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api
# pyrefly: ignore [missing-import]
from odoo.exceptions import ValidationError

class CalonAsprakRegist(models.Model):
    _name = 'z.penyusup.regist' # diubah paksa
    _description = 'Pendaftaran Asisten Praktikum'

    student_id = fields.Many2one('op.student', string='Student', required=True)
    periode_id = fields.Many2one('mst_periodesemt', string='Periode', required=True)
    berkas_khs = fields.Binary(string='Berkas KHS', attachment=True, required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted')
    ], string='Status', default='draft')

    @api.constrains('berkas_khs')
    def _check_file_size(self):
        for record in self:
            if record.berkas_khs:
                file_size = len(record.berkas_khs) * 3 / 4
                if file_size > 2 * 1024 * 1024:
                    raise ValidationError("Ukuran file KHS tidak boleh melebihi 2MB.")

    @api.constrains('periode_id')
    def _check_periode_aktif(self):
        for record in self:
            if record.periode_id and hasattr(record.periode_id, 'active') and not record.periode_id.active:
                raise ValidationError("Periode rekrutmen ditutup atau tidak aktif.")