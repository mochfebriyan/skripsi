# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


def _periode_default(model):
    return model.env['labfik.periode'].periode_pada(fields.Date.context_today(model))


class LabfikRapat(models.Model):
    _name = 'labfik.rapat'
    _description = 'Rapat koordinasi'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'tanggal desc, id desc'

    name = fields.Char('Agenda', required=True, tracking=True)
    periode_id = fields.Many2one('labfik.periode', 'Periode', required=True, default=lambda s: _periode_default(s))
    tanggal = fields.Date('Tanggal', required=True, default=fields.Date.context_today, tracking=True)
    semester_id = fields.Many2one('labfik.periode.semester', 'Semester', compute='_compute_semester', store=True)
    peserta_ids = fields.Many2many('labfik.personel', 'labfik_rapat_peserta_rel', 'rapat_id', 'personel_id',
                                   string='Peserta')
    keputusan = fields.Text('Keputusan')
    notulen = fields.Binary('Notulen', attachment=True)
    notulen_name = fields.Char('Nama file notulen')

    @api.depends('tanggal', 'periode_id.semester_ids')
    def _compute_semester(self):
        for rec in self:
            rec.semester_id = rec.periode_id.semester_pada(rec.tanggal) if rec.periode_id and rec.tanggal else False

    @api.constrains('tanggal', 'periode_id')
    def _check_tanggal(self):
        for rec in self:
            p = rec.periode_id
            if not (p.tanggal_mulai <= rec.tanggal <= p.tanggal_selesai):
                raise ValidationError(_('Tanggal rapat harus berada di dalam periode %s.', p.name))


class LabfikEvaluasiStruktur(models.Model):
    _name = 'labfik.evaluasi.struktur'
    _description = 'Evaluasi struktur dan beban kerja'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'tanggal desc, id desc'

    name = fields.Char('Judul', required=True, default='Evaluasi struktur dan beban kerja')
    periode_id = fields.Many2one('labfik.periode', 'Periode', required=True, default=lambda s: _periode_default(s))
    tanggal = fields.Date('Tanggal', required=True, default=fields.Date.context_today, tracking=True)
    peserta_ids = fields.Many2many('labfik.personel', 'labfik_evaluasi_peserta_rel', 'evaluasi_id', 'personel_id',
                                   string='Peserta')
    temuan = fields.Text('Temuan beban kerja dan koordinasi', required=True)
    keputusan = fields.Text('Keputusan perbaikan', required=True)
    sk_revisi_id = fields.Many2one('labfik.sk', 'SK hasil revisi')
    jabatan_revisi_ids = fields.Many2many('labfik.jabatan', 'labfik_evaluasi_jabatan_rel', 'evaluasi_id',
                                          'jabatan_id', string='Jabatan yang direvisi')

    @api.constrains('tanggal', 'periode_id')
    def _check_tanggal(self):
        for rec in self:
            p = rec.periode_id
            if not (p.tanggal_mulai <= rec.tanggal <= p.tanggal_selesai):
                raise ValidationError(_('Tanggal evaluasi harus berada di dalam periode %s.', p.name))
