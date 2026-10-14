# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LabReadinessChecklist(models.Model):
    _name = 'lab.readiness.checklist'
    _description = 'Checklist Kesiapan Ruangan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    facility_id = fields.Many2one('op.facility', string='Fasilitas/Ruangan', required=True, tracking=True)
    check_date = fields.Datetime(string='Tanggal Pemeriksaan', default=fields.Datetime.now, required=True, tracking=True)
    laboran_id = fields.Many2one('res.users', string='Laboran (Pemeriksa)', default=lambda self: self.env.user, required=True, tracking=True)
    physical_status = fields.Selection([
        ('baik', 'Baik'),
        ('rusak', 'Rusak')
    ], string='Status Fisik', required=True, tracking=True)
    software_status = fields.Selection([
        ('tersedia', 'Tersedia'),
        ('perlu_bantuan', 'Perlu Bantuan')
    ], string='Status Software', required=True, tracking=True)
    notes = fields.Text(string='Catatan Detail', tracking=True)

    @api.constrains('physical_status', 'notes')
    def _check_notes_on_rusak(self):
        for record in self:
            if record.physical_status == 'rusak' and not record.notes:
                raise ValidationError("Catatan detail wajib diisi apabila kondisi fisik Ruangan Rusak.")
