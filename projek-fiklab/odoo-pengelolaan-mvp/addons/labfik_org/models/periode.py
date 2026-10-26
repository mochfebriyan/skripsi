# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

from .common import GROUP_ADMIN, cek_kalab, tgl_id

SEMESTER = [('ganjil', 'Ganjil'), ('genap', 'Genap')]


class LabfikPeriode(models.Model):
    _name = 'labfik.periode'
    _description = 'Periode (tahun akademik)'
    _inherit = ['mail.thread']
    _order = 'tanggal_mulai desc'

    name = fields.Char('Nama periode', required=True, tracking=True,
                       help='Contoh: 2026/2027')
    jenis = fields.Selection([('akademik', 'Tahun akademik'), ('anggaran', 'Tahun anggaran')],
                             string='Jenis', required=True, default='akademik', tracking=True)
    tanggal_mulai = fields.Date('Mulai', required=True, tracking=True)
    tanggal_selesai = fields.Date('Selesai', required=True, tracking=True)
    semester_ids = fields.One2many('labfik.periode.semester', 'periode_id', string='Semester')
    wajib_ids = fields.One2many('labfik.dokumen.wajib', 'periode_id', string='Daftar SOP wajib')
    wajib_terkunci = fields.Boolean('Daftar wajib terkunci', readonly=True, copy=False, tracking=True)
    tanggal_kunci = fields.Date('Dikunci pada', readonly=True, copy=False)
    kepatuhan_ids = fields.One2many('labfik.kepatuhan', 'periode_id', string='Status monev')
    jumlah_wajib = fields.Integer('Jumlah SOP wajib', compute='_compute_jumlah_wajib')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('name_unique', 'unique(name, jenis)', 'Nama periode sudah dipakai.'),
    ]

    @api.depends('wajib_ids')
    def _compute_jumlah_wajib(self):
        for rec in self:
            rec.jumlah_wajib = len(rec.wajib_ids)

    @api.constrains('tanggal_mulai', 'tanggal_selesai')
    def _check_tanggal(self):
        for rec in self:
            if rec.tanggal_selesai <= rec.tanggal_mulai:
                raise ValidationError(_('Tanggal selesai periode harus setelah tanggal mulai.'))

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records.filtered(lambda r: not r.semester_ids):
            rec._buat_semester_default()
        return records

    def _buat_semester_default(self):
        """Ganjil = 5 bulan pertama (sampai akhir bulan), Genap = sisanya."""
        self.ensure_one()
        akhir_ganjil = self.tanggal_mulai + relativedelta(months=4, day=31)
        if akhir_ganjil >= self.tanggal_selesai:
            akhir_ganjil = self.tanggal_mulai + (self.tanggal_selesai - self.tanggal_mulai) / 2
        self.env['labfik.periode.semester'].create([
            {'periode_id': self.id, 'name': 'ganjil',
             'tanggal_mulai': self.tanggal_mulai, 'tanggal_selesai': akhir_ganjil},
            {'periode_id': self.id, 'name': 'genap',
             'tanggal_mulai': akhir_ganjil + relativedelta(days=1), 'tanggal_selesai': self.tanggal_selesai},
        ])

    def semester_berjalan(self, tanggal):
        """Semester yang sudah dimulai pada tanggal penilaian, urut dari yang terlama."""
        self.ensure_one()
        return self.semester_ids.filtered(lambda s: s.tanggal_mulai <= tanggal).sorted('tanggal_mulai')

    def semester_pada(self, tanggal):
        self.ensure_one()
        return self.semester_ids.filtered(lambda s: s.tanggal_mulai <= tanggal <= s.tanggal_selesai)[:1]

    @api.model
    def periode_pada(self, tanggal):
        periode = self.search([('tanggal_mulai', '<=', tanggal), ('tanggal_selesai', '>=', tanggal)],
                              order='tanggal_mulai desc', limit=1)
        return periode or self.search([], order='tanggal_mulai desc', limit=1)

    def action_kunci_wajib(self):
        cek_kalab(self.env, _('mengunci daftar SOP wajib'))
        for rec in self:
            if not rec.wajib_ids:
                raise UserError(_('Daftar SOP wajib periode %s masih kosong.', rec.name))
            rec.write({'wajib_terkunci': True, 'tanggal_kunci': fields.Date.context_today(rec)})
            rec._message_log(body=_('Daftar SOP wajib dikunci (%s SOP).', len(rec.wajib_ids)))

    def action_buka_kunci_wajib(self):
        if not self.env.su and not self.env.user.has_group(GROUP_ADMIN):
            raise UserError(_('Hanya Admin LabFIK yang dapat membuka kunci daftar SOP wajib.'))
        for rec in self:
            rec.write({'wajib_terkunci': False, 'tanggal_kunci': False})
            rec._message_log(body=_('Kunci daftar SOP wajib dibuka oleh %s.', self.env.user.name))

    def action_buka_status(self):
        self.ensure_one()
        self.env['labfik.kepatuhan'].siapkan_untuk_periode(self)
        action = self.env['ir.actions.act_window']._for_xml_id('labfik_org.action_kepatuhan')
        action['domain'] = [('periode_id', '=', self.id)]
        action['context'] = {'default_periode_id': self.id}
        return action

    def tgl_id(self, value):
        return tgl_id(value)


class LabfikPeriodeSemester(models.Model):
    _name = 'labfik.periode.semester'
    _description = 'Semester'
    _order = 'tanggal_mulai'

    periode_id = fields.Many2one('labfik.periode', required=True, ondelete='cascade')
    name = fields.Selection(SEMESTER, string='Semester', required=True)
    tanggal_mulai = fields.Date('Mulai', required=True)
    tanggal_selesai = fields.Date('Selesai', required=True)

    _sql_constraints = [
        ('semester_unique', 'unique(periode_id, name)', 'Semester ini sudah ada pada periode tersebut.'),
    ]

    @api.depends('name', 'periode_id.name')
    def _compute_display_name(self):
        label = dict(SEMESTER)
        for rec in self:
            rec.display_name = '%s %s' % (label.get(rec.name, ''), rec.periode_id.name or '')

    @api.constrains('tanggal_mulai', 'tanggal_selesai', 'periode_id')
    def _check_tanggal(self):
        for rec in self:
            p = rec.periode_id
            if rec.tanggal_selesai < rec.tanggal_mulai:
                raise ValidationError(_('Tanggal selesai semester harus setelah tanggal mulai.'))
            if rec.tanggal_mulai < p.tanggal_mulai or rec.tanggal_selesai > p.tanggal_selesai:
                raise ValidationError(_('Semester harus berada di dalam rentang periode %s.', p.name))
            lain = p.semester_ids - rec
            if any(s.tanggal_mulai <= rec.tanggal_selesai and rec.tanggal_mulai <= s.tanggal_selesai for s in lain):
                raise ValidationError(_('Rentang semester tidak boleh tumpang tindih.'))
