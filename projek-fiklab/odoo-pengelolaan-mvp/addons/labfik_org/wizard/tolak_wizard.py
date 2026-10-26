# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError

MODEL_DIIZINKAN = ('labfik.dokumen.versi', 'labfik.rencana')


class LabfikTolakWizard(models.TransientModel):
    _name = 'labfik.tolak.wizard'
    _description = 'Tolak pengajuan'

    res_model = fields.Char(required=True)
    res_id = fields.Integer(required=True)
    alasan = fields.Text('Alasan penolakan', required=True)

    @api.model
    def buka(self, record):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Tolak pengajuan'),
            'res_model': self._name,
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_res_model': record._name, 'default_res_id': record.id},
        }

    def action_tolak(self):
        self.ensure_one()
        if self.res_model not in MODEL_DIIZINKAN:
            raise UserError(_('Model tidak didukung.'))
        self.env[self.res_model].browse(self.res_id)._tolak(self.alasan)
        return {'type': 'ir.actions.act_window_close'}
