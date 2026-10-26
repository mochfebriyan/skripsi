# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError

JENIS_PERSONEL = [
    ('dosen', 'Dosen'),
    ('tendik', 'Tenaga kependidikan'),
    ('mahasiswa', 'Mahasiswa'),
    ('eksternal', 'Pejabat/pihak luar lab'),
]


class LabfikPersonel(models.Model):
    """Orang yang berperan di lab. Rancangan field mengacu master Rafika
    (mst_dosen, op.student.assistant, res.users) agar mudah dipetakan saat integrasi."""
    _name = 'labfik.personel'
    _description = 'Personel laboratorium'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char('Nama', required=True, tracking=True)
    jenis = fields.Selection(JENIS_PERSONEL, string='Jenis', required=True, default='tendik', tracking=True)
    nomor_induk = fields.Char('NIP/NIDN/NIM', tracking=True, groups='labfik_org.group_labfik_kalab')
    email = fields.Char('Email')
    user_id = fields.Many2one('res.users', 'Akun login', tracking=True, ondelete='set null',
                              domain=[('share', '=', False)])
    sk_line_ids = fields.One2many('labfik.sk.line', 'personel_id', string='Riwayat jabatan')
    jabatan_aktif_ids = fields.Many2many('labfik.jabatan', string='Jabatan aktif', compute='_compute_jabatan_aktif')
    active = fields.Boolean(default=True, tracking=True)

    _sql_constraints = [
        ('nomor_induk_unique', 'unique(nomor_induk)', 'NIP/NIDN/NIM sudah terdaftar pada personel lain.'),
        ('user_unique', 'unique(user_id)', 'Akun login ini sudah ditautkan ke personel lain.'),
    ]

    def _compute_jabatan_aktif(self):
        hari_ini = fields.Date.context_today(self)
        for rec in self:
            rec.jabatan_aktif_ids = rec._jabatan_pada(hari_ini)

    def _jabatan_pada(self, tanggal):
        self.ensure_one()
        lines = self.sudo().sk_line_ids.filtered(lambda l: l._aktif_pada(tanggal))
        return lines.jabatan_id

    # ------------------------------------------------------------------ hak akses
    @api.model
    def _grup_dikelola(self):
        """Grup yang diatur otomatis: grup semua jabatan beserta grup turunannya di kategori LabFIK."""
        jabatan = self.env['labfik.jabatan'].sudo().with_context(active_test=False).search([])
        grup = jabatan.group_ids
        kategori = self.env.ref('labfik_org.module_category_labfik')
        return (grup | grup.trans_implied_ids).filtered(lambda g: g.category_id == kategori)

    def _sync_akses(self, tanggal=None):
        """Menyamakan grup akun login dengan jabatan aktif (FR-A4).
        Grup di luar grup yang dikelola tidak disentuh."""
        tanggal = tanggal or fields.Date.context_today(self)
        dikelola = self._grup_dikelola()
        for rec in self.sudo().with_context(active_test=False):
            user = rec.user_id
            if not user:
                continue
            jabatan = rec._jabatan_pada(tanggal) if rec.active else self.env['labfik.jabatan']
            jabatan = jabatan.filtered('active')
            seharusnya = jabatan.group_ids | jabatan.group_ids.trans_implied_ids
            # Grup yang diwarisi dari grup non-kelola (misalnya Admin LabFIK) tetap dipertahankan.
            lain = user.groups_id - dikelola
            seharusnya |= lain.trans_implied_ids
            sekarang = user.groups_id & dikelola
            tambah = (seharusnya & dikelola) - sekarang
            cabut = sekarang - seharusnya
            if not tambah and not cabut:
                continue
            perintah = [(4, g.id) for g in tambah] + [(3, g.id) for g in cabut]
            user.sudo().write({'groups_id': perintah})
            pesan = []
            if tambah:
                pesan.append(_('ditambah: %s', ', '.join(tambah.mapped('name'))))
            if cabut:
                pesan.append(_('dicabut: %s', ', '.join(cabut.mapped('name'))))
            rec._message_log(body=_('Hak akses %s diperbarui (%s).', user.login, '; '.join(pesan)))

    def _cabut_akses_user(self, users):
        dikelola = self._grup_dikelola()
        for user in users.sudo():
            sisa = user.groups_id - dikelola
            seharusnya = sisa.trans_implied_ids & dikelola
            cabut = (user.groups_id & dikelola) - seharusnya
            if cabut:
                user.write({'groups_id': [(3, g.id) for g in cabut]})

    @api.model
    def _cron_sinkron_akses(self):
        self.with_context(active_test=False).search([('user_id', '!=', False)])._sync_akses()

    # ------------------------------------------------------------------ CRUD
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.filtered('user_id')._sync_akses()
        return records

    def write(self, vals):
        user_lama = self.mapped('user_id')
        if 'active' in vals and not vals['active']:
            self._akhiri_jabatan()
        res = super().write(vals)
        if 'user_id' in vals:
            terlepas = user_lama - self.mapped('user_id')
            self._cabut_akses_user(terlepas)
        if {'user_id', 'active'} & set(vals):
            self._sync_akses()
        return res

    def unlink(self):
        self._cabut_akses_user(self.mapped('user_id'))
        return super().unlink()

    def _akhiri_jabatan(self):
        """Personel dinonaktifkan: baris jabatan yang masih aktif diakhiri hari ini (PRD §8.4)."""
        hari_ini = fields.Date.context_today(self)
        for rec in self.sudo():
            aktif = rec.sk_line_ids.filtered(
                lambda l: not l.tanggal_selesai_efektif or l.tanggal_selesai_efektif > hari_ini)
            if aktif:
                aktif.with_context(labfik_internal=True).write({'tanggal_selesai': hari_ini})
                rec._message_log(body=_('Personel dinonaktifkan; %s jabatan diakhiri per %s.',
                                        len(aktif), hari_ini))

    def action_buat_akun(self):
        self.ensure_one()
        if self.user_id:
            raise UserError(_('Personel ini sudah punya akun login.'))
        login = self.email or self.sudo().nomor_induk
        if not login:
            raise UserError(_('Isi email atau NIP/NIM terlebih dahulu sebagai login.'))
        user = self.env['res.users'].sudo().with_context(no_reset_password=True).create({
            'name': self.name,
            'login': login,
            'email': self.email,
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
        })
        self.user_id = user
        self._message_log(body=_('Akun login "%s" dibuat. Atur kata sandinya lewat menu Pengaturan › Pengguna.', login))
        return True
