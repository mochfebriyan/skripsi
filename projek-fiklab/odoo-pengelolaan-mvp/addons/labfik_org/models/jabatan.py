# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import is_html_empty


def _domain_grup_jabatan(model):
    kategori = model.env.ref('labfik_org.module_category_labfik', raise_if_not_found=False)
    admin = model.env.ref('labfik_org.group_labfik_admin', raise_if_not_found=False)
    domain = [('category_id', '=', kategori.id if kategori else False)]
    if admin:
        domain.append(('id', '!=', admin.id))
    return domain


class LabfikJabatan(models.Model):
    _name = 'labfik.jabatan'
    _description = 'Jabatan di struktur laboratorium'
    _inherit = ['mail.thread']
    _order = 'sequence, id'
    _parent_name = 'atasan_id'

    name = fields.Char('Jabatan', required=True, tracking=True)
    sequence = fields.Integer(default=10)
    uraian_tugas = fields.Html('Uraian tugas dan tanggung jawab')
    kewenangan_ids = fields.Many2many('labfik.kewenangan', 'labfik_jabatan_kewenangan_rel',
                                      'jabatan_id', 'kewenangan_id', string='Kewenangan')
    kewenangan_uraian = fields.Html('Uraian kewenangan tambahan')
    atasan_id = fields.Many2one('labfik.jabatan', 'Atasan (alur pelaporan)', tracking=True, ondelete='restrict')
    bawahan_ids = fields.One2many('labfik.jabatan', 'atasan_id', string='Bawahan')
    pengganti_id = fields.Many2one('labfik.jabatan', 'Jabatan pengganti', tracking=True, ondelete='restrict',
                                   help='Jabatan yang menjalankan tugas ini bila pemangkunya berhalangan.')
    is_puncak = fields.Boolean('Jabatan puncak', help='Jabatan tertinggi di struktur lab; tidak wajib punya atasan.')
    group_ids = fields.Many2many('res.groups', 'labfik_jabatan_group_rel', 'jabatan_id', 'group_id',
                                 string='Hak akses otomatis', domain=lambda self: _domain_grup_jabatan(self),
                                 help='Pemangku jabatan otomatis mendapat hak akses ini selama SK-nya berlaku.')
    pemangku_ids = fields.Many2many('labfik.personel', string='Pemangku saat ini', compute='_compute_pemangku')
    kekurangan = fields.Char('Kekurangan data', compute='_compute_kekurangan')
    active = fields.Boolean(default=True)

    def _compute_pemangku(self):
        hari_ini = fields.Date.context_today(self)
        pemangku = self._pemangku_pada(hari_ini)
        for rec in self:
            rec.pemangku_ids = pemangku.get(rec.id, self.env['labfik.personel'])

    def _compute_kekurangan(self):
        hari_ini = fields.Date.context_today(self)
        for rec in self:
            rec.kekurangan = ', '.join(rec._kekurangan(hari_ini))

    def _pemangku_pada(self, tanggal):
        """{jabatan_id: personel} untuk baris SK yang aktif pada tanggal tersebut."""
        hasil = {}
        lines = self.env['labfik.sk.line'].sudo().search([('jabatan_id', 'in', self.ids)])
        for line in lines:
            if line._aktif_pada(tanggal):
                hasil.setdefault(line.jabatan_id.id, self.env['labfik.personel'])
                hasil[line.jabatan_id.id] |= line.personel_id
        return hasil

    def _kekurangan(self, tanggal, cek_pemangku=True):
        """Daftar data yang belum lengkap untuk Pengelolaan 3 K2."""
        self.ensure_one()
        kurang = []
        if is_html_empty(self.uraian_tugas):
            kurang.append(_('uraian tugas'))
        if not self.kewenangan_ids and is_html_empty(self.kewenangan_uraian):
            kurang.append(_('kewenangan'))
        if not self.atasan_id and not self.is_puncak:
            kurang.append(_('atasan'))
        if not self.pengganti_id:
            kurang.append(_('pengganti'))
        if cek_pemangku and not self._pemangku_pada(tanggal).get(self.id):
            kurang.append(_('pemangku'))
        return kurang

    @api.constrains('atasan_id', 'pengganti_id')
    def _check_relasi(self):
        for rec in self:
            if rec.pengganti_id == rec:
                raise ValidationError(_('Jabatan "%s" tidak boleh menjadi penggantinya sendiri.', rec.name))
            if rec.atasan_id == rec:
                raise ValidationError(_('Jabatan "%s" tidak boleh menjadi atasannya sendiri.', rec.name))
        if not self._check_recursion():
            raise ValidationError(_('Struktur atasan membentuk lingkaran.'))

    @api.constrains('group_ids')
    def _check_group_ids(self):
        allowed = self.env['res.groups'].search(_domain_grup_jabatan(self))
        for rec in self:
            if rec.group_ids - allowed:
                raise ValidationError(_('Hak akses jabatan hanya boleh dipilih dari grup LabFIK (selain Admin LabFIK).'))

    def write(self, vals):
        res = super().write(vals)
        if 'group_ids' in vals or 'active' in vals:
            personel = self.env['labfik.sk.line'].sudo().search([('jabatan_id', 'in', self.ids)]).personel_id
            personel._sync_akses()
        return res
