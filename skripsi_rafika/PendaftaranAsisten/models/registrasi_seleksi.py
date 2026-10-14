# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api
# pyrefly: ignore [missing-import]  
from odoo.exceptions import ValidationError

class CalonAsprakRegistSeleksi(models.Model):
    _inherit = 'registrasi.asprak'  # FIX: was 'calon.asprak.regist' (ghost model), correct target is 'registrasi.asprak'

    is_published = fields.Boolean(string='Published', default=False)
    skep_file = fields.Binary(string='File SKEP Rektor', attachment=True)
    skep_filename = fields.Char(string='Nama File SKEP')
    hasil_seleksi = fields.Selection([
        ('pending', 'Pending'),
        ('lolos', 'Lolos'),
        ('tidak_lolos', 'Tidak Lolos')
    ], string='Hasil Seleksi', default='pending')

    def action_finalize_and_publish(self):
        for record in self:
            if not record.skep_file:
                raise ValidationError("Dokumen SKEP Rektor wajib dilampirkan sebelum hasil dapat diumumkan.")
            record.is_published = True
            
            student = getattr(record, 'student_id', False) or getattr(record, 'mahasiswa_id', False)
            if record.hasil_seleksi == 'lolos' and student and student.user_id:
                try:
                    ta_group = self.env.ref('PendaftaranAsisten.group_teaching_assistant', raise_if_not_found=False)
                    if ta_group:
                        ta_group.sudo().write({'users': [(4, student.user_id.id)]})
                except Exception:
                    pass
