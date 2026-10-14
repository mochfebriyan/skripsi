# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api
# pyrefly: ignore [missing-import]
from odoo.exceptions import ValidationError

class LabRecruitmentAnnouncement(models.Model):
    _name = 'lab.recruitment.announcement'
    _description = 'Pengumuman Rekrutmen Asisten'

    name = fields.Char(string='Judul Pengumuman', required=True)
    poster = fields.Image(string='Poster', max_width=1024, max_height=1024)
    content = fields.Html(string='Isi Pengumuman')
    date_deadline = fields.Datetime(string='Batas Waktu', required=True)
    periode_id = fields.Many2one('mst_periodesemt', string='Periode Semester', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('closed', 'Closed')
    ], string='Status', default='draft')

    @api.constrains('date_deadline')
    def _check_date_deadline(self):
        for record in self:
            if record.date_deadline and record.date_deadline < fields.Datetime.now():
                raise ValidationError("Batas waktu (Deadline) tidak boleh kurang dari waktu saat ini.")

    def action_publish(self):
        for record in self:
            if not record.poster and not record.content:
                raise ValidationError("Pengumuman harus memiliki konten atau poster sebelum dipublikasikan.")
            record.state = 'published'

    def action_unpublish(self):
        for record in self:
            record.state = 'closed'
