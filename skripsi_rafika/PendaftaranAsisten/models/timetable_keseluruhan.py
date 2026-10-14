# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api


class TimetableKeseluruhan(models.Model):
    _name = 'timetable.keseluruhan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Timetable Keseluruhan (Master Schedule)'
    _order = 'waktu_mulai asc'

    name = fields.Char(
        string='Nama Kegiatan',
        required=True,
        tracking=True,
        placeholder='Contoh: Praktikum Algoritma Kelas A',
    )

    dosen_id = fields.Many2one(
        comodel_name='mst_dosen',
        string='Dosen Pengampu',
        required=True,
        tracking=True,
    )

    kelas_id = fields.Many2one(
        comodel_name='mst_kodekelas',
        string='Kelas',
        required=True,
        tracking=True,
    )

    course_id = fields.Many2one(
        comodel_name='mst_coursesemt',
        string='Mata Kuliah',
        required=True,
        tracking=True,
    )

    jadwal_praktikum_id = fields.Many2one('jadwal.praktikum', string='Referensi Jadwal Induk')

    waktu_mulai = fields.Datetime(
        string='Waktu Mulai',
        required=True,
        tracking=True,
    )

    waktu_selesai = fields.Datetime(
        string='Waktu Selesai',
        required=True,
        tracking=True,
    )

    keterangan = fields.Text(
        string='Keterangan',
    )

    # ---------------------------------------------------------------------------
    # Computed display name  (depends: course_id, kelas_id)
    # ---------------------------------------------------------------------------
    @api.depends('course_id', 'kelas_id', 'name')
    def _compute_display_name(self):
        for rec in self:
            parts = []
            if rec.course_id:
                parts.append(rec.course_id.nama_matkul or rec.course_id.kode_matkul)
            if rec.kelas_id:
                parts.append(rec.kelas_id.nama_kelas or rec.kelas_id.kode_kelas)
            rec.display_name = ' - '.join(parts) if parts else (rec.name or '/')
