# -*- coding: utf-8 -*-
from odoo import _, fields, models
from odoo.exceptions import UserError

from .common import tgl_id


class LabfikLampiranMixin(models.AbstractModel):
    """Lampiran bertanda tangan (SK, rencana kerja) yang disimpan SATU KALI di register dokumen
    (FR-A3, FR-B8). Rekaman pemilik hanya menautkan versi dokumennya."""
    _name = 'labfik.lampiran.mixin'
    _description = 'Lampiran yang tersimpan di register dokumen'

    _lampiran_jenis = 'lainnya'
    _lampiran_prefix = 'DOK'

    lampiran_versi_id = fields.Many2one('labfik.dokumen.versi', 'Versi di register dokumen',
                                        readonly=True, copy=False, ondelete='restrict')
    lampiran_file = fields.Binary('File bertanda tangan', compute='_compute_lampiran',
                                  inverse='_inverse_lampiran', attachment=False)
    lampiran_filename = fields.Char('Nama file', compute='_compute_lampiran', inverse='_inverse_lampiran')

    def get_nama_lab(self):
        return self.env['ir.config_parameter'].sudo().get_param('labfik.nama_lab') or 'Laboratorium'

    def get_tgl_cetak(self):
        return tgl_id(fields.Date.context_today(self))

    def _compute_lampiran(self):
        for rec in self:
            versi = rec.sudo().lampiran_versi_id
            rec.lampiran_file = versi.file
            rec.lampiran_filename = versi.file_name

    def _lampiran_terkunci(self):
        return False

    def _lampiran_kode(self):
        return '%s-%s' % (self._lampiran_prefix, self.id)

    def _lampiran_judul(self):
        return self.display_name

    def _inverse_lampiran(self):
        for rec in self:
            if not rec.lampiran_file:
                continue
            if rec._lampiran_terkunci():
                raise UserError(_('Lampiran "%s" sudah terkunci dan tidak dapat diganti.', rec.display_name))
            versi_lama = rec.sudo().lampiran_versi_id
            dokumen = versi_lama.dokumen_id
            if not dokumen:
                dokumen = self.env['labfik.dokumen'].sudo().create({
                    'kode': rec._lampiran_kode(),
                    'name': rec._lampiran_judul(),
                    'jenis': rec._lampiran_jenis,
                })
            versi = self.env['labfik.dokumen.versi'].sudo().with_context(labfik_internal=True).create({
                'dokumen_id': dokumen.id,
                'revisi': dokumen._revisi_berikut(),
                'file': rec.lampiran_file,
                'file_name': rec.lampiran_filename or '%s.pdf' % rec._lampiran_kode(),
                'ringkasan': _('Diunggah dari %s', rec.display_name),
            })
            versi._jadikan_berlaku()
            rec.with_context(labfik_internal=True).write({'lampiran_versi_id': versi.id})
