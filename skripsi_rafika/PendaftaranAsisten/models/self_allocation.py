# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api
# pyrefly: ignore [missing-import]
from odoo.exceptions import ValidationError

class AsprakSelfAllocation(models.Model):
    _name = 'asprak.self.allocation'
    _description = 'Self Service Alokasi Jadwal Asisten'

    def _default_asisten(self):
        return self.env['op.student'].search([('user_id', '=', self.env.uid)], limit=1)

    asisten_id = fields.Many2one('op.student', string='Asisten', required=True, default=_default_asisten)
    course_id = fields.Many2one('op.course', string='Mata Kuliah Praktikum', required=True)
    timetable_id = fields.Many2one('op.session', string='Jadwal Praktikum', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('locked', 'Locked')
    ], string='Status', default='draft')

    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id:
            return {'domain': {'timetable_id': [('course_id', '=', self.course_id.id)]}}
        else:
            return {'domain': {'timetable_id': []}}

    @api.constrains('timetable_id', 'asisten_id')
    def _check_validasi_alokasi(self):
        for record in self:
            if not record.timetable_id or not record.asisten_id:
                continue

            # 1. Validasi Kuota: Maksimal 2 asisten per kelas/slot yang SUDAH RESMI (Locked)
            allocated_count = self.search_count([
                ('timetable_id', '=', record.timetable_id.id),
                ('state', '=', 'locked'), # <-- TAMBAHAN INI BIAR AMAN
                ('id', '!=', record.id)
            ])
            if allocated_count >= 2:
                raise ValidationError("Mohon maaf, kuota asisten untuk kelas ini sudah penuh.")

            # 2. Validasi Bentrok: Contoh logika untuk mengecek bentrok dengan jadwal reguler
            # Contoh query mencari bentrok waktu (start_datetime dan end_datetime) pada op.session
            if record.timetable_id.start_datetime and record.timetable_id.end_datetime:
                bentrok = self.env['op.session'].search([
                    ('start_datetime', '<', record.timetable_id.end_datetime),
                    ('end_datetime', '>', record.timetable_id.start_datetime),
                    ('id', '!=', record.timetable_id.id),
                    # Asumsi filter tambahan untuk mengecek jadwal yang terkait dengan mahasiswa
                    # ('student_id', '=', record.asisten_id.id)
                ], limit=1)
                
                if bentrok:
                    raise ValidationError("Jadwal yang dipilih bentrok dengan jadwal reguler/KHS Anda.")

    def action_confirm(self):
        for record in self:
            record.state = 'locked'
