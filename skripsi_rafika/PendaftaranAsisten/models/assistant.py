# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<https://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

# pyrefly: ignore [missing-import]
from odoo import models, fields, api, _ 
# pyrefly: ignore [missing-import]
from odoo.exceptions import ValidationError
from datetime import date, timedelta
# pyrefly: ignore [missing-import]


class OpStudentAssistant(models.Model):
    """
    Master data untuk Asisten Mahasiswa - Inherit dari op.student
    untuk memanfaatkan data personal yang sudah ada di OpenEducat
    """
    _name = 'op.student.assistant'
    _description = 'Student Assistant'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Link ke student - wajib ada untuk terintegrasi
    student_id = fields.Many2one(
        'op.student',
        'Student',
        required=True,
        ondelete='cascade',
        tracking=True,
        help='Mahasiswa yang akan menjadi asisten'
    )
    
    # Informasi Dasar Asisten
    name = fields.Char(
        'Assistant Name',
        compute='_compute_assistant_name',
        store=True,
        help='Nama asisten otomatis dari student'
    )
    
    employee_id = fields.Many2one(
        'hr.employee',
        'Employee',
        help='Link ke HR Employee jika ada'
    )
    
    assistant_type = fields.Selection([
        ('teaching', 'Teaching Assistant'),
        ('lab', 'Laboratory Assistant'),
        ('library', 'Library Assistant'),
        ('admin', 'Administrative Assistant'),
        ('research', 'Research Assistant'),
    ], string='Assistant Type', required=True, tracking=True)
    
    department_id = fields.Many2one(
        'op.department',
        'Department',
        required=True,
        tracking=True,
        help='Departemen tempat asisten bekerja'
    )
    
    faculty_id = fields.Many2one(
        'op.faculty',
        'Faculty Supervisor',
        required=True,
        tracking=True,
        help='Pembimbing/Dosen penyelia'
    )
    
    course_id = fields.Many2one(
        'op.course',
        'Course',
        help='Kursus terkait (jika applicable)'
    )

    classroom_id = fields.Many2one(
        'op.classroom',
        string='Assigned Laboratory',
        help='Laboratorium yang ditugaskan untuk asisten'
    )

    timetable_ids = fields.Many2many(
        'op.session',
        string='Assigned Schedule',
        help='Jadwal yang ditugaskan untuk asisten'
    )
    
    # Status dan Tanggal
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('completed', 'Completed'),
    ], string='Status', default='draft', tracking=True)
    
    start_date = fields.Date(
        'Start Date',
        required=True,
        tracking=True,
        help='Tanggal mulai menjadi asisten'
    )
    
    end_date = fields.Date(
        'End Date',
        tracking=True,
        help='Tanggal berakhir menjadi asisten'
    )
    
    # Kompensasi
    salary_type = fields.Selection([
        ('hourly', 'Hourly'),
        ('monthly', 'Monthly'),
        ('stipend', 'Stipend'),
        ('none', 'Unpaid'),
    ], string='Salary Type', default='none')
    
    hourly_rate = fields.Float(
        'Hourly Rate',
        help='Tarif per jam (jika hourly)'
    )
    
    monthly_salary = fields.Float(
        'Monthly Salary',
        help='Gaji bulanan (jika monthly)'
    )
    
    allocation_budget = fields.Float(
        'Allocation Budget',
        help='Total alokasi anggaran untuk asisten'
    )
    
    # Workload & Jam Kerja
    hours_per_week = fields.Float(
        'Hours Per Week',
        default=20.0,
        help='Jam kerja per minggu'
    )
    
    # Dokumen dan Informasi Tambahan
    notes = fields.Text('Notes', help='Catatan untuk asisten')
    
    active = fields.Boolean(default=True)
    
    # Link ke aplikasi/registrasi
    application_id = fields.Many2one(
        'op.assistant.registration',
        'Application',
        ondelete='set null',
        help='Referensi ke aplikasi pendaftaran'
    )
    
    _sql_constraints = [
        ('unique_student_assistant',
         'unique(student_id)',
         'Mahasiswa hanya bisa menjadi asisten sekali!')
    ]
    
    @api.depends('student_id', 'assistant_type')
    def _compute_assistant_name(self):
        """Generate nama asisten dari student dan tipe"""
        for record in self:
            if record.student_id:
                record.name = f"{record.student_id.name} - {dict(self._fields['assistant_type'].selection).get(record.assistant_type, '')}"
            else:
                record.name = _('New Assistant')
    
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Validasi tanggal"""
        for record in self:
            if record.end_date and record.start_date > record.end_date:
                raise ValidationError(_('Start Date harus sebelum End Date!'))
    
    @api.constrains('hours_per_week')
    def _check_hours(self):
        """Validasi jam kerja"""
        for record in self:
            if record.hours_per_week <= 0 or record.hours_per_week > 168:
                raise ValidationError(_('Hours per week harus antara 0-168!'))
    
    def action_submit(self):
        """Action untuk submit permohonan"""
        self.state = 'submitted'
    
    def action_approve(self):
        """Action untuk approve permohonan"""
        self.state = 'approved'
    
    def action_reject(self):
        """Action untuk reject permohonan"""
        self.state = 'rejected'


class OpAssistantRegistration(models.Model):
    """
    Form Registrasi/Aplikasi untuk menjadi Asisten Mahasiswa
    Terintegrasi dengan struktur OpenEducat untuk proses approval
    """
    _name = 'op.assistant.registration'
    _description = 'Assistant Registration'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'registration_date desc'
    
    # Nomor Registrasi (auto-generated)
    registration_number = fields.Char(
        'Registration Number',
        readonly=True,
        copy=False,
        help='Nomor registrasi unik'
    )
    
    # Tanggal
    registration_date = fields.Date(
        'Registration Date',
        default=fields.Date.today,
        readonly=True
    )
    
    # Identitas Pendaftar
    student_id = fields.Many2one(
        'op.student',
        'Student',
        required=True,
        ondelete='cascade',
        tracking=True,
        help='Mahasiswa yang mendaftar menjadi asisten'
    )
    
    email = fields.Char(
        'Email',
        compute='_compute_email',
        store=True,
        help='Email dari student'
    )
    
    phone = fields.Char(
        'Phone',
        compute='_compute_phone',
        store=True,
        help='Nomor kontak dari student'
    )
    
    # Preferensi Posisi
    preferred_assistants = fields.Selection([
        ('teaching', 'Teaching Assistant'),
        ('lab', 'Laboratory Assistant'),
        ('library', 'Library Assistant'),
        ('admin', 'Administrative Assistant'),
        ('research', 'Research Assistant'),
    ], string='Preferred Position', required=True, tracking=True)
    
    preferred_department_id = fields.Many2one(
        'op.department',
        'Preferred Department',
        required=True,
        tracking=True
    )
    
    preferred_faculty_id = fields.Many2one(
        'op.faculty',
        'Preferred Faculty Supervisor',
        help='Pilihan dosen penyelia (opsional)'
    )

    classroom_id = fields.Many2one(
        'op.classroom',
        string='Preferred Laboratory',
        help='Laboratorium pilihan untuk pendaftaran asisten'
    )

    timetable_ids = fields.Many2many(
        'op.session',
        string='Preferred Schedule',
        help='Jadwal pilihan untuk pendaftaran asisten'
    )
    
    # Academic Background (inherited info)
    course_id = fields.Many2one(
        'op.course',
        'Current Course',
        compute='_compute_course',
        store=True,
        help='Program studi mahasiswa saat ini'
    )
    
    batch_id = fields.Many2one(
        'op.batch',
        'Batch',
        compute='_compute_batch',
        store=True,
        help='Angkatan mahasiswa'
    )
    
    gpa = fields.Float(
        'GPA',
        help='IPK mahasiswa (opsional)'
    )
    
    # Dokumen & Pernyataan
    motivation_letter = fields.Text(
        'Motivation Letter',
        help='Surat motivasi untuk menjadi asisten'
    )
    
    work_experience = fields.Text(
        'Work Experience',
        help='Pengalaman kerja sebelumnya (jika ada)'
    )
    
    skills = fields.Text(
        'Skills & Competencies',
        help='Keahlian dan kompetensi yang dimiliki'
    )
    
    availability_hours = fields.Float(
        'Available Hours Per Week',
        default=20.0,
        help='Jam yang tersedia untuk bekerja per minggu'
    )
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('contract_pending', 'Contract Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    
    # Approval Trail
    submitted_by = fields.Many2one(
        'res.users',
        'Submitted By',
        readonly=True,
        help='User yang submit'
    )
    
    reviewed_by = fields.Many2one(
        'res.users',
        'Reviewed By',
        readonly=True,
        tracking=True,
        help='User yang review/approve'
    )
    
    review_date = fields.Date(
        'Review Date',
        readonly=True,
        tracking=True
    )
    
    rejection_reason = fields.Text(
        'Rejection Reason',
        help='Alasan penolakan (jika ada)'
    )
    
    notes = fields.Text('Notes')
    
    active = fields.Boolean(default=True)
    
    _sql_constraints = [
        ('unique_student_registration',
         'unique(student_id, registration_date)',
         'Mahasiswa hanya bisa mendaftar sekali per hari!')
    ]
    
    @api.model
    def create(self, vals):
        """Generate registration number saat create"""
        if not vals.get('registration_number'):
            vals['registration_number'] = self.env['ir.sequence'].next_by_code('op.assistant.registration') or 'AST/0000'
        return super().create(vals)
    
    @api.depends('student_id')
    def _compute_email(self):
        """Get email dari student"""
        for record in self:
            record.email = record.student_id.email if record.student_id else ''
    
    @api.depends('student_id')
    def _compute_phone(self):
        """Get phone dari student"""
        for record in self:
            record.phone = record.student_id.mobile if record.student_id else ''
    
    @api.depends('student_id')
    def _compute_course(self):
        """Get course dari student course details"""
        for record in self:
            course = None
            if record.student_id and record.student_id.course_detail_ids:
                course = record.student_id.course_detail_ids[0].course_id
            record.course_id = course
    
    @api.depends('student_id')
    def _compute_batch(self):
        """Get batch dari student course details"""
        for record in self:
            batch = None
            if record.student_id and record.student_id.course_detail_ids:
                batch = record.student_id.course_detail_ids[0].batch_id
            record.batch_id = batch
    
    def action_submit(self):
        """Submit aplikasi"""
        self.submitted_by = self.env.user.id
        self.state = 'submitted'
    
    def action_under_review(self):
        """Ubah status menjadi under review"""
        self.state = 'under_review'
    
    def action_approve(self):
        """Approve aplikasi dan create op.student.assistant"""
        self.reviewed_by = self.env.user.id
        self.review_date = fields.Date.today()
        self.state = 'approved'
        
        # Auto-create op.student.assistant record
        self._create_assistant_record()
    
    def action_reject(self):
        """Reject aplikasi"""
        self.reviewed_by = self.env.user.id
        self.review_date = fields.Date.today()
        self.state = 'rejected'
    
    def _create_assistant_record(self):
        """Helper untuk create op.student.assistant dari registration"""
        for record in self:
            assistant_vals = {
                'student_id': record.student_id.id,
                'assistant_type': record.preferred_assistants,
                'department_id': record.preferred_department_id.id,
                'faculty_id': record.preferred_faculty_id.id or False,
                'course_id': record.course_id.id or False,
                'classroom_id': record.classroom_id.id or False,
                'timetable_ids': [(6, 0, record.timetable_ids.ids)] if record.timetable_ids else False,
                'start_date': fields.Date.today(),
                'salary_type': 'none',
                'application_id': record.id,
                'state': 'approved',
            }
            self.env['op.student.assistant'].create(assistant_vals)


class OpAssistantDocument(models.Model):
    """
    Dokumen pendukung untuk asisten mahasiswa
    (KTP, sertifikat, kontrak, dll)
    """
    _name = 'op.assistant.document'
    _description = 'Assistant Document'
    _inherit = 'ir.attachment'
    
    assistant_id = fields.Many2one(
        'op.student.assistant',
        'Assistant',
        ondelete='cascade',
        tracking=True,
        help='Asisten yang memiliki dokumen ini'
    )
    
    document_type = fields.Selection([
        ('id_card', 'ID Card'),
        ('certificate', 'Certificate'),
        ('contract', 'Contract'),
        ('cv', 'CV/Resume'),
        ('transcript', 'Academic Transcript'),
        ('recommendation', 'Recommendation Letter'),
        ('health', 'Health Certificate'),
        ('other', 'Other'),
    ], string='Document Type', required=True)
    
    document_date = fields.Date(
        'Document Date',
        help='Tanggal dokumen'
    )
    
    expiry_date = fields.Date(
        'Expiry Date',
        help='Tanggal kadaluarsa (jika applicable)'
    )
    
    notes = fields.Text('Notes')


class OpStudentInherit(models.Model):
    """
    Inherit model op.student untuk menambah field terkait assistantship
    """
    _inherit = 'op.student'
    
    # Relasi ke assistant records
    is_assistant = fields.Boolean(
        'Is Assistant',
        compute='_compute_is_assistant',
        help='Flag jika mahasiswa adalah asisten'
    )
    
    assistant_id = fields.Many2one(
        'op.student.assistant',
        'Assistant Record',
        compute='_compute_assistant',
        help='Record asisten jika mahasiswa adalah asisten'
    )
    
    assistant_count = fields.Integer(
        'Assistant Records',
        compute='_compute_assistant_count'
    )

    allocation_status = fields.Selection([
        ('allocated', 'Teralokasi'),
        ('unallocated', 'Belum Teralokasi')
    ], string="Status Alokasi", compute="_compute_allocation_status", store=False)
    
    def _compute_is_assistant(self):
        """Check apakah student ini adalah asisten"""
        for record in self:
            record.is_assistant = self.env['op.student.assistant'].search_count(
                [('student_id', '=', record.id), ('state', 'in', ['approved', 'active'])]
            ) > 0
    
    def _compute_assistant(self):
        """Get assistant record pertama jika ada"""
        for record in self:
            assistant = self.env['op.student.assistant'].search(
                [('student_id', '=', record.id)],
                limit=1,
                order='start_date desc'
            )
            record.assistant_id = assistant.id if assistant else False
    
    def _compute_assistant_count(self):
        """Count berapa banyak record asisten"""
        for record in self:
            record.assistant_count = self.env['op.student.assistant'].search_count(
                [('student_id', '=', record.id)]
            )

    def _compute_allocation_status(self):
        """Check if this student is assigned to ANY jadwal.praktikum"""
        for record in self:
            jadwal_count = self.env['jadwal.praktikum'].search_count(
                [('asisten_ids', 'in', record.id)]
            )
            record.allocation_status = 'allocated' if jadwal_count > 0 else 'unallocated'

class OpFacility(models.Model):
    _inherit = 'op.facility'

    assistant_id = fields.Many2one(
        'op.student.assistant',
        string='Assigned Assistant',
        help='Asisten yang ditugaskan pada fasilitas ini'
    )

    registration_status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Registration Status', default='pending',
       help='Status pendaftaran asisten untuk fasilitas/praktikum')
