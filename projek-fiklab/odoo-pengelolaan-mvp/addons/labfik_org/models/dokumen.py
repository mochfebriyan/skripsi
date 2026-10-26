# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError

from .common import GROUP_KALAB, cek_kalab, get_param_int, is_internal, personel_pengguna, tgl_id

JENIS_DOKUMEN = [
    ('sop', 'SOP'),
    ('ik', 'Instruksi kerja'),
    ('formulir', 'Formulir'),
    ('sk', 'SK / keputusan'),
    ('rencana', 'Rencana kerja'),
    ('eksternal', 'Dokumen eksternal'),
    ('lainnya', 'Lainnya'),
]
KATEGORI_DOKUMEN = [
    ('tata_tertib', 'Tata tertib'),
    ('praktikum', 'Praktikum'),
    ('operasi', 'Operasi dan manajemen'),
    ('k3', 'K3'),
    ('alat', 'Alat'),
    ('peminjaman', 'Peminjaman'),
    ('kedaruratan', 'Kedaruratan'),
    ('limbah', 'Limbah'),
    ('lainnya', 'Lainnya'),
]
VERSI_STATE = [('draf', 'Draf'), ('diajukan', 'Diajukan'), ('berlaku', 'Berlaku'), ('dicabut', 'Dicabut')]
FIELD_FILE = {'file', 'file_name', 'revisi', 'dokumen_id'}
FIELD_STATUS = {'state', 'tanggal_sah', 'pengesah_id', 'disahkan_oleh_id', 'alasan_tolak'}


class LabfikDokumen(models.Model):
    _name = 'labfik.dokumen'
    _description = 'Daftar induk dokumen'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'kode'

    kode = fields.Char('Kode dokumen', required=True, tracking=True, help='Contoh: SOP-PRA-001')
    name = fields.Char('Judul', required=True, tracking=True)
    jenis = fields.Selection(JENIS_DOKUMEN, string='Jenis', required=True, default='sop', tracking=True)
    kategori = fields.Selection(KATEGORI_DOKUMEN, string='Kategori', tracking=True)
    dasar_kebutuhan = fields.Text('Dasar kebutuhan', help='Kegiatan atau risiko yang membuat dokumen ini diperlukan.')
    ruang_ids = fields.Many2many('labfik.ruang', 'labfik_dokumen_ruang_rel', 'dokumen_id', 'ruang_id',
                                 string='Lokasi penggunaan')
    pemilik_id = fields.Many2one('labfik.personel', 'Pemilik dokumen', tracking=True)
    versi_ids = fields.One2many('labfik.dokumen.versi', 'dokumen_id', string='Versi')
    versi_berlaku_id = fields.Many2one('labfik.dokumen.versi', 'Versi berlaku',
                                       compute='_compute_versi_berlaku', store=True)
    revisi_berlaku = fields.Char(related='versi_berlaku_id.revisi', string='Revisi berlaku')
    tanggal_tinjau = fields.Date(related='versi_berlaku_id.tanggal_tinjau', string='Tinjau ulang')
    wajib_ids = fields.One2many('labfik.dokumen.wajib', 'dokumen_id', string='Wajib pada periode')
    jumlah_versi = fields.Integer(compute='_compute_versi_berlaku', store=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('kode_unique', 'unique(kode)', 'Kode dokumen sudah dipakai.'),
    ]

    @api.depends('versi_ids.state')
    def _compute_versi_berlaku(self):
        for rec in self:
            berlaku = rec.versi_ids.filtered(lambda v: v.state == 'berlaku')
            rec.versi_berlaku_id = berlaku[:1]
            rec.jumlah_versi = len(rec.versi_ids)

    @api.depends('kode', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = '[%s] %s' % (rec.kode, rec.name) if rec.kode else rec.name

    def _revisi_berikut(self):
        self.ensure_one()
        return '%s.0' % (len(self.sudo().with_context(active_test=False).versi_ids) + 1)

    def action_versi_baru(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'labfik.dokumen.versi',
            'view_mode': 'form',
            'target': 'current',
            'context': {'default_dokumen_id': self.id, 'default_revisi': self._revisi_berikut()},
        }


class LabfikDokumenVersi(models.Model):
    _name = 'labfik.dokumen.versi'
    _description = 'Versi dokumen'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'dokumen_id, id desc'

    dokumen_id = fields.Many2one('labfik.dokumen', 'Dokumen', required=True, ondelete='restrict',
                                 index=True, tracking=True)
    kode = fields.Char(related='dokumen_id.kode', store=True, string='Kode')
    judul = fields.Char(related='dokumen_id.name', store=True, string='Judul')
    jenis = fields.Selection(related='dokumen_id.jenis', store=True, string='Jenis')
    kategori = fields.Selection(related='dokumen_id.kategori', store=True, string='Kategori')
    ruang_ids = fields.Many2many(related='dokumen_id.ruang_ids', string='Lokasi penggunaan')
    revisi = fields.Char('Revisi', required=True, tracking=True, default=lambda self: self._default_revisi())
    file = fields.Binary('File dokumen', attachment=True)
    file_name = fields.Char('Nama file')
    ringkasan = fields.Text('Ringkasan perubahan')
    state = fields.Selection(VERSI_STATE, string='Status', default='draf', required=True, tracking=True,
                             copy=False, index=True)
    alasan_tolak = fields.Text('Alasan penolakan terakhir', readonly=True, copy=False, tracking=True)
    pengesah_id = fields.Many2one('labfik.personel', 'Disahkan oleh (personel)', readonly=True, copy=False)
    disahkan_oleh_id = fields.Many2one('res.users', 'Disahkan oleh (akun)', readonly=True, copy=False)
    tanggal_sah = fields.Date('Tanggal sah', readonly=True, copy=False, tracking=True)
    tanggal_tinjau = fields.Date('Tinjau ulang berikutnya', copy=False, tracking=True)
    perlu_ditinjau = fields.Boolean('Lewat tanggal tinjau', compute='_compute_perlu_ditinjau')
    distribusi_ids = fields.One2many('labfik.dokumen.distribusi', 'versi_id', string='Distribusi')
    sosialisasi_ids = fields.One2many('labfik.dokumen.sosialisasi', 'versi_id', string='Sosialisasi')
    lokasi_belum_ids = fields.Many2many('labfik.ruang', string='Belum didistribusikan ke',
                                        compute='_compute_lokasi_belum')

    _sql_constraints = [
        ('revisi_unique', 'unique(dokumen_id, revisi)', 'Nomor revisi ini sudah ada untuk dokumen tersebut.'),
    ]

    @api.model
    def _default_revisi(self):
        dokumen_id = self.env.context.get('default_dokumen_id')
        if dokumen_id:
            return self.env['labfik.dokumen'].browse(dokumen_id)._revisi_berikut()
        return False

    @api.onchange('dokumen_id')
    def _onchange_dokumen_id(self):
        if self.dokumen_id and not self.revisi:
            self.revisi = self.dokumen_id._revisi_berikut()

    @api.depends('kode', 'judul', 'revisi')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = '[%s] %s · rev %s' % (rec.kode or '', rec.judul or '', rec.revisi or '')

    def _compute_perlu_ditinjau(self):
        hari_ini = fields.Date.context_today(self)
        for rec in self:
            rec.perlu_ditinjau = bool(rec.state == 'berlaku' and rec.tanggal_tinjau and rec.tanggal_tinjau < hari_ini)

    @api.depends('distribusi_ids.ruang_id', 'dokumen_id.ruang_ids')
    def _compute_lokasi_belum(self):
        for rec in self:
            rec.lokasi_belum_ids = rec.dokumen_id.ruang_ids - rec.distribusi_ids.ruang_id

    # ------------------------------------------------------------------ CRUD dan kunci
    @api.model_create_multi
    def create(self, vals_list):
        if not is_internal(self.env):
            for vals in vals_list:
                vals.pop('state', None)
                for f in ('tanggal_sah', 'pengesah_id', 'disahkan_oleh_id', 'alasan_tolak'):
                    vals.pop(f, None)
        for vals in vals_list:
            if vals.get('dokumen_id') and not vals.get('revisi'):
                vals['revisi'] = self.env['labfik.dokumen'].browse(vals['dokumen_id'])._revisi_berikut()
        return super().create(vals_list)

    def write(self, vals):
        if not is_internal(self.env):
            if FIELD_FILE & set(vals) and any(r.state != 'draf' for r in self):
                raise UserError(_('File dan nomor revisi terkunci setelah diajukan. '
                                  'Untuk perubahan, buat versi baru.'))
            if FIELD_STATUS & set(vals):
                raise UserError(_('Status dokumen hanya dapat diubah lewat tombol Ajukan, Sahkan, Tolak, atau Cabut.'))
            if 'tanggal_tinjau' in vals and not self.env.user.has_group(GROUP_KALAB):
                raise UserError(_('Hanya Kepala Laboratorium yang dapat mengubah tanggal tinjau ulang.'))
        return super().write(vals)

    def unlink(self):
        if not self.env.su and any(r.state != 'draf' for r in self):
            raise UserError(_('Hanya versi berstatus draf yang dapat dihapus.'))
        return super().unlink()

    # ------------------------------------------------------------------ alur status
    def _ubah(self, vals):
        return self.with_context(labfik_internal=True).write(vals)

    def action_ajukan(self):
        for rec in self:
            if rec.state != 'draf':
                raise UserError(_('Hanya versi draf yang dapat diajukan.'))
            if not rec.file:
                raise UserError(_('Unggah file dokumen sebelum mengajukan.'))
            rec._ubah({'state': 'diajukan'})
            rec._message_log(body=_('Diajukan untuk disahkan oleh %s.', self.env.user.name))
        return True

    def action_sahkan(self):
        cek_kalab(self.env, _('mengesahkan dokumen'))
        for rec in self:
            if rec.state != 'diajukan':
                raise UserError(_('Hanya versi yang sudah diajukan yang dapat disahkan.'))
        self._jadikan_berlaku()
        for rec in self:
            rec._message_log(body=_('Disahkan oleh %s; berlaku mulai %s.', self.env.user.name, tgl_id(rec.tanggal_sah)))
        return True

    def action_tolak(self):
        cek_kalab(self.env, _('menolak dokumen'))
        self.ensure_one()
        return self.env['labfik.tolak.wizard'].buka(self)

    def _tolak(self, alasan):
        cek_kalab(self.env, _('menolak dokumen'))
        if not (alasan or '').strip():
            raise UserError(_('Alasan penolakan wajib diisi.'))
        for rec in self:
            if rec.state != 'diajukan':
                raise UserError(_('Hanya versi yang diajukan yang dapat ditolak.'))
            rec._ubah({'state': 'draf', 'alasan_tolak': alasan})
            rec._message_log(body=_('Ditolak oleh %s. Alasan: %s', self.env.user.name, alasan))
        return True

    def action_cabut(self):
        cek_kalab(self.env, _('mencabut dokumen'))
        for rec in self:
            if rec.state != 'berlaku':
                raise UserError(_('Hanya versi berlaku yang dapat dicabut.'))
            rec._ubah({'state': 'dicabut'})
            rec._message_log(body=_('Dicabut oleh %s.', self.env.user.name))
        return True

    def action_tinjau_tanpa_perubahan(self):
        """Tinjau ulang: isi masih sesuai, tanggal tinjau berikutnya diperpanjang satu siklus."""
        cek_kalab(self.env, _('mencatat tinjau ulang'))
        siklus = get_param_int(self.env, 'labfik.siklus_tinjau_bulan')
        hari_ini = fields.Date.context_today(self)
        for rec in self:
            if rec.state != 'berlaku':
                raise UserError(_('Tinjau ulang hanya untuk versi berlaku.'))
            rec._ubah({'tanggal_tinjau': hari_ini + relativedelta(months=siklus)})
            rec._message_log(body=_('Ditinjau ulang oleh %s: isi masih sesuai. Tinjau berikutnya %s.',
                                    self.env.user.name, tgl_id(rec.tanggal_tinjau)))
        return True

    def _jadikan_berlaku(self, tanggal=None):
        """Satu versi berlaku per dokumen: versi lain yang berlaku otomatis dicabut (FR-B3)."""
        tanggal = tanggal or fields.Date.context_today(self)
        siklus = get_param_int(self.env, 'labfik.siklus_tinjau_bulan')
        pengesah = personel_pengguna(self.env)
        for rec in self:
            lama = self.sudo().search([('dokumen_id', '=', rec.dokumen_id.id),
                                       ('state', '=', 'berlaku'), ('id', '!=', rec.id)])
            if lama:
                lama.with_context(labfik_internal=True).write({'state': 'dicabut'})
                for v in lama:
                    v._message_log(body=_('Otomatis dicabut karena revisi %s disahkan.', rec.revisi))
            rec.sudo()._ubah({
                'state': 'berlaku',
                'tanggal_sah': tanggal,
                'tanggal_tinjau': tanggal + relativedelta(months=siklus),
                'disahkan_oleh_id': self.env.uid,
                'pengesah_id': pengesah.id or False,
                'alasan_tolak': False,
            })

    @api.model
    def _cron_pengingat_tinjau(self):
        """Aktivitas untuk pemilik dokumen menjelang tanggal tinjau ulang (FR-B7)."""
        hari = get_param_int(self.env, 'labfik.pengingat_hari')
        batas = fields.Date.context_today(self) + relativedelta(days=hari)
        tipe = self.env.ref('mail.mail_activity_data_todo', raise_if_not_found=False)
        versi = self.search([('state', '=', 'berlaku'), ('tanggal_tinjau', '!=', False),
                             ('tanggal_tinjau', '<=', batas)])
        ringkasan = _('Tinjau ulang dokumen')
        for rec in versi:
            user = rec.dokumen_id.pemilik_id.user_id
            if not user:
                continue
            sudah = rec.activity_ids.filtered(lambda a: a.user_id == user and a.summary == ringkasan)
            if sudah:
                continue
            rec.activity_schedule(
                activity_type_id=tipe.id if tipe else False,
                summary=ringkasan,
                note=_('Versi %s perlu ditinjau ulang sebelum %s.', rec.revisi, tgl_id(rec.tanggal_tinjau)),
                date_deadline=rec.tanggal_tinjau,
                user_id=user.id,
            )


class LabfikDokumenWajib(models.Model):
    _name = 'labfik.dokumen.wajib'
    _description = 'SOP wajib pada periode monev'
    _order = 'periode_id desc, dokumen_id'

    periode_id = fields.Many2one('labfik.periode', 'Periode', required=True, ondelete='cascade', index=True)
    dokumen_id = fields.Many2one('labfik.dokumen', 'Dokumen', required=True, ondelete='restrict',
                                 domain=[('jenis', 'in', ('sop', 'ik'))])
    kode = fields.Char(related='dokumen_id.kode')
    versi_berlaku_id = fields.Many2one(related='dokumen_id.versi_berlaku_id')
    catatan = fields.Char('Catatan')

    _sql_constraints = [
        ('wajib_unique', 'unique(periode_id, dokumen_id)', 'Dokumen ini sudah ada di daftar wajib periode tersebut.'),
    ]

    def _cek_kunci(self, periode):
        if not self.env.su and any(p.wajib_terkunci for p in periode):
            raise UserError(_('Daftar SOP wajib periode ini sudah dikunci.'))

    @api.model_create_multi
    def create(self, vals_list):
        self._cek_kunci(self.env['labfik.periode'].browse([v.get('periode_id') for v in vals_list if v.get('periode_id')]))
        return super().create(vals_list)

    def write(self, vals):
        self._cek_kunci(self.periode_id)
        if vals.get('periode_id'):
            self._cek_kunci(self.env['labfik.periode'].browse(vals['periode_id']))
        return super().write(vals)

    def unlink(self):
        self._cek_kunci(self.periode_id)
        return super().unlink()


class LabfikDokumenDistribusi(models.Model):
    _name = 'labfik.dokumen.distribusi'
    _description = 'Distribusi versi dokumen ke lokasi penggunaan'
    _order = 'tanggal desc, id desc'

    versi_id = fields.Many2one('labfik.dokumen.versi', 'Versi', required=True, ondelete='cascade',
                               domain=[('state', '=', 'berlaku')], index=True)
    dokumen_id = fields.Many2one(related='versi_id.dokumen_id', store=True)
    ruang_id = fields.Many2one('labfik.ruang', 'Lokasi', required=True)
    tanggal = fields.Date('Tanggal', required=True, default=fields.Date.context_today)
    petugas_id = fields.Many2one('labfik.personel', 'Petugas', default=lambda self: personel_pengguna(self.env))
    catatan = fields.Char('Catatan')

    _sql_constraints = [
        ('distribusi_unique', 'unique(versi_id, ruang_id)', 'Versi ini sudah tercatat didistribusikan ke lokasi tersebut.'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        versi = self.env['labfik.dokumen.versi'].browse([v.get('versi_id') for v in vals_list if v.get('versi_id')])
        if any(v.state != 'berlaku' for v in versi):
            raise UserError(_('Distribusi hanya dapat dicatat untuk versi yang berlaku.'))
        return super().create(vals_list)


class LabfikDokumenSosialisasi(models.Model):
    _name = 'labfik.dokumen.sosialisasi'
    _description = 'Sosialisasi versi dokumen'
    _order = 'tanggal desc, id desc'

    versi_id = fields.Many2one('labfik.dokumen.versi', 'Versi', required=True, ondelete='cascade',
                               domain=[('state', '=', 'berlaku')], index=True)
    dokumen_id = fields.Many2one(related='versi_id.dokumen_id', store=True)
    tanggal = fields.Date('Tanggal', required=True, default=fields.Date.context_today)
    metode = fields.Selection([('briefing', 'Briefing'), ('rapat', 'Rapat'), ('daring', 'Daring/pesan'),
                               ('lainnya', 'Lainnya')], string='Metode', required=True, default='briefing')
    peserta_ids = fields.Many2many('labfik.personel', 'labfik_sosialisasi_peserta_rel', 'sosialisasi_id',
                                   'personel_id', string='Peserta')
    jumlah_peserta = fields.Integer(compute='_compute_jumlah_peserta')
    bukti = fields.Binary('Bukti (daftar hadir/foto)', attachment=True)
    bukti_name = fields.Char('Nama file bukti')
    catatan = fields.Text('Catatan')

    @api.depends('peserta_ids')
    def _compute_jumlah_peserta(self):
        for rec in self:
            rec.jumlah_peserta = len(rec.peserta_ids)

    @api.model_create_multi
    def create(self, vals_list):
        versi = self.env['labfik.dokumen.versi'].browse([v.get('versi_id') for v in vals_list if v.get('versi_id')])
        if any(v.state != 'berlaku' for v in versi):
            raise UserError(_('Sosialisasi hanya dapat dicatat untuk versi yang berlaku.'))
        return super().create(vals_list)
