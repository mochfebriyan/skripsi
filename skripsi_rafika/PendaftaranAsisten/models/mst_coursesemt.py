# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api

class MstCourseSemt(models.Model):
    _name = 'mst_coursesemt'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Master Course Semester'

    course_identifier = fields.Char('ID Course', readonly=True,
                                    copy=False, default='New', tracking=True)
    kode_matkul = fields.Char('Kode Matkul', required=True, tracking=True)
    nama_matkul = fields.Char('Nama Matkul', required=True, tracking=True)
    jumlah_sks = fields.Integer('Jumlah SKS', tracking=True)
    is_praktikum_lab = fields.Boolean('Is Praktikum Lab?', tracking=True)
    semester = fields.Selection(
        selection=[
            ('1', 'Semester 1'),
            ('2', 'Semester 2'),
            ('3', 'Semester 3'),
            ('4', 'Semester 4'),
            ('5', 'Semester 5'),
            ('6', 'Semester 6'),
            ('7', 'Semester 7'),
            ('8', 'Semester 8'),
        ],
        string='Semester',
        required=True,
        tracking=True,
    )
    butuh_asisten = fields.Boolean(string='Butuh Asisten?', default=True, tracking=True)

    # =====================================================================
    # TAMBAHAN REVISI 13: ASSOCIATE KE MODUL OPENEDUCAT
    # Menghubungkan tabel matkul mandiri ini dengan master subject bawaan
    # =====================================================================
    op_subject_id = fields.Many2one(
        'op.subject',
        string='Relasi Subject OpenEduCat',
        help='Relasi associate ke master data mata kuliah (subject) OpenEduCat'
    )

    _sql_constraints = [
        ('unique_course_identifier', 'unique(course_identifier)', 'ID Course harus unik!'),
        ('unique_kode_matkul', 'unique(kode_matkul)', 'Kode Matkul harus unik!'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('course_identifier') or vals['course_identifier'] == 'New':
                vals['course_identifier'] = self.env['ir.sequence'].next_by_code('mst.coursesemt.sequence') or 'New'
        return super().create(vals_list)

    @api.depends('kode_matkul', 'nama_matkul')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.kode_matkul}] {rec.nama_matkul}" if rec.kode_matkul else rec.nama_matkul