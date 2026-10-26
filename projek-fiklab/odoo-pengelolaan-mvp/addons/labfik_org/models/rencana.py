# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

from .common import cek_kalab, is_internal, personel_pengguna, tgl_id

RENCANA_STATE = [
    ('draf', 'Draf'),
    ('diajukan', 'Diajukan'),
    ('disahkan', 'Disahkan'),
    ('diganti', 'Diganti revisi'),
    ('selesai', 'Selesai'),
]
FIELD_TERKUNCI = {'name', 'jenis', 'periode_id', 'item_ids', 'narasi', 'pemilik_id'}
FIELD_STATUS = {'state', 'tanggal_sah', 'disahkan_oleh_id', 'alasan_tolak', 'rencana_asal_id'}


class LabfikRencana(models.Model):
    _name = 'labfik.rencana'
    _description = 'Rencana kerja laboratorium'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'labfik.lampiran.mixin']
    _order = 'tanggal_mulai_periode desc, id desc'
    _lampiran_jenis = 'rencana'
    _lampiran_prefix = 'RKT'

    name = fields.Char('Judul', required=True, tracking=True)
    jenis = fields.Selection([('tahunan', 'Rencana kerja tahunan'), ('strategis', 'Roadmap / rencana strategis')],
                             string='Jenis', required=True, default='tahunan', tracking=True)
    periode_id = fields.Many2one('labfik.periode', 'Periode', required=True, tracking=True)
    tanggal_mulai_periode = fields.Date(related='periode_id.tanggal_mulai', store=True)
    pemilik_id = fields.Many2one('labfik.personel', 'Pemilik rencana', tracking=True,
                                 default=lambda self: personel_pengguna(self.env))
    narasi = fields.Html('Latar belakang dan arah')
    state = fields.Selection(RENCANA_STATE, string='Status', default='draf', required=True, tracking=True,
                             copy=False, index=True)
    alasan_tolak = fields.Text('Alasan penolakan terakhir', readonly=True, copy=False)
    pengesah_id = fields.Many2one('labfik.personel', 'Ditandatangani oleh', tracking=True,
                                  help='Pejabat yang menandatangani dokumen rencana, misalnya Dekan.')
    disahkan_oleh_id = fields.Many2one('res.users', 'Disahkan di sistem oleh', readonly=True, copy=False)
    tanggal_sah = fields.Date('Tanggal sah', readonly=True, copy=False, tracking=True)
    item_ids = fields.One2many('labfik.rencana.item', 'rencana_id', string='Item rencana', copy=True)
    rencana_asal_id = fields.Many2one('labfik.rencana', 'Revisi dari', readonly=True, copy=False)
    revisi_ids = fields.One2many('labfik.rencana', 'rencana_asal_id', string='Revisi')
    tinjauan_ids = fields.One2many('labfik.rencana.tinjauan', 'rencana_id', string='Tinjauan')
    total_anggaran = fields.Float('Total anggaran (Rp)', compute='_compute_total', digits=(16, 0))
    jumlah_item = fields.Integer('Jumlah item', compute='_compute_total')

    @api.depends('item_ids.anggaran')
    def _compute_total(self):
        for rec in self:
            rec.total_anggaran = sum(rec.item_ids.mapped('anggaran'))
            rec.jumlah_item = len(rec.item_ids)

    def _lampiran_terkunci(self):
        return self.state not in ('draf', 'diajukan')

    def write(self, vals):
        if not is_internal(self.env):
            if FIELD_STATUS & set(vals):
                raise UserError(_('Status rencana hanya dapat diubah lewat tombol yang tersedia.'))
            if FIELD_TERKUNCI & set(vals) and any(r.state != 'draf' for r in self):
                raise UserError(_('Isi rencana terkunci setelah diajukan. Tolak terlebih dahulu, '
                                  'atau buat revisi bila sudah disahkan.'))
        return super().write(vals)

    def unlink(self):
        if not self.env.su and any(r.state != 'draf' for r in self):
            raise UserError(_('Hanya rencana berstatus draf yang dapat dihapus.'))
        return super().unlink()

    def copy(self, default=None):
        return super(LabfikRencana, self.with_context(labfik_internal=True)).copy(default)

    def _ubah(self, vals):
        return self.with_context(labfik_internal=True).write(vals)

    # ------------------------------------------------------------------ alur status
    def action_ajukan(self):
        for rec in self:
            if rec.state != 'draf':
                raise UserError(_('Hanya rencana draf yang dapat diajukan.'))
            if not rec.item_ids:
                raise UserError(_('Rencana belum memiliki item.'))
            kurang = []
            for i, item in enumerate(rec.item_ids, start=1):
                k = item._kekurangan()
                if k:
                    kurang.append(_('Item %s (%s): %s', i, item.sasaran or '-', ', '.join(k)))
            if kurang:
                raise UserError(_('Lengkapi item rencana sebelum diajukan:\n%s', '\n'.join(kurang)))
            rec._ubah({'state': 'diajukan', 'alasan_tolak': False})
            rec._message_log(body=_('Diajukan oleh %s.', self.env.user.name))
        return True

    def action_sahkan(self):
        cek_kalab(self.env, _('mengesahkan rencana kerja'))
        for rec in self:
            if rec.state != 'diajukan':
                raise UserError(_('Hanya rencana yang sudah diajukan yang dapat disahkan.'))
            if not rec.lampiran_versi_id:
                raise UserError(_('Unggah PDF rencana kerja yang sudah ditandatangani sebelum mengesahkan.'))
            rec._ubah({'state': 'disahkan', 'tanggal_sah': fields.Date.context_today(rec),
                       'disahkan_oleh_id': self.env.uid})
            asal = rec.rencana_asal_id
            if asal and asal.state == 'disahkan':
                asal._ubah({'state': 'diganti'})
                asal._message_log(body=_('Diganti oleh revisi "%s".', rec.name))
            rec._message_log(body=_('Disahkan oleh %s.', self.env.user.name))
        return True

    def action_tolak(self):
        cek_kalab(self.env, _('menolak rencana kerja'))
        self.ensure_one()
        return self.env['labfik.tolak.wizard'].buka(self)

    def _tolak(self, alasan):
        cek_kalab(self.env, _('menolak rencana kerja'))
        if not (alasan or '').strip():
            raise UserError(_('Alasan penolakan wajib diisi.'))
        for rec in self:
            if rec.state != 'diajukan':
                raise UserError(_('Hanya rencana yang diajukan yang dapat ditolak.'))
            rec._ubah({'state': 'draf', 'alasan_tolak': alasan})
            rec._message_log(body=_('Ditolak oleh %s. Alasan: %s', self.env.user.name, alasan))
        return True

    def action_buat_revisi(self):
        cek_kalab(self.env, _('merevisi rencana kerja'))
        self.ensure_one()
        if self.state != 'disahkan':
            raise UserError(_('Revisi hanya dapat dibuat dari rencana yang sudah disahkan.'))
        if self.revisi_ids.filtered(lambda r: r.state in ('draf', 'diajukan')):
            raise UserError(_('Masih ada revisi yang belum disahkan untuk rencana ini.'))
        baru = self.copy({'name': _('%s (revisi)', self.name), 'rencana_asal_id': self.id})
        self._message_log(body=_('Revisi "%s" dibuat oleh %s.', baru.name, self.env.user.name))
        return {
            'type': 'ir.actions.act_window', 'res_model': 'labfik.rencana', 'res_id': baru.id,
            'view_mode': 'form', 'target': 'current',
        }

    def action_selesai(self):
        cek_kalab(self.env, _('menutup rencana kerja'))
        for rec in self:
            if rec.state != 'disahkan':
                raise UserError(_('Hanya rencana yang disahkan yang dapat ditandai selesai.'))
            rec._ubah({'state': 'selesai'})
        return True

    def tgl_id(self, value):
        return tgl_id(value)

    def get_renstra_matriks(self):
        """Baris matriks keterkaitan Renstra: [{'sasaran', 'tingkat', 'item'}] untuk laporan cetak."""
        self.ensure_one()
        tingkat = dict(self.env['labfik.renstra.sasaran']._fields['tingkat'].selection)
        baris = {}
        for i, item in enumerate(self.item_ids, start=1):
            for s in item.renstra_ids:
                baris.setdefault(('m', s.id), {'sasaran': s.display_name, 'tingkat': tingkat.get(s.tingkat, ''),
                                               'nomor': []})['nomor'].append(i)
            if item.renstra_teks:
                baris.setdefault(('t', item.renstra_teks), {'sasaran': item.renstra_teks, 'tingkat': '',
                                                            'nomor': []})['nomor'].append(i)
        hasil = list(baris.values())
        for b in hasil:
            b['item'] = ', '.join('No %s' % n for n in b['nomor'])
        return hasil


class LabfikRencanaItem(models.Model):
    _name = 'labfik.rencana.item'
    _description = 'Item rencana kerja'
    _order = 'rencana_id, sequence, id'

    rencana_id = fields.Many2one('labfik.rencana', 'Rencana', required=True, ondelete='cascade', index=True)
    rencana_state = fields.Selection(related='rencana_id.state', string='Status rencana')
    sequence = fields.Integer(default=10)
    sasaran = fields.Char('Sasaran / kegiatan')
    renstra_ids = fields.Many2many('labfik.renstra.sasaran', 'labfik_item_renstra_rel', 'item_id', 'sasaran_id',
                                   string='Sasaran Renstra')
    renstra_teks = fields.Char('Keterkaitan Renstra (teks)', help='Diisi bila sasaran Renstra belum ada di master.')
    kpi_id = fields.Many2one('labfik.kpi', 'KPI')
    target = fields.Char('Target', help='Contoh: 90%, 10 dari 10 SOP')
    pic_id = fields.Many2one('labfik.personel', 'PIC')
    tanggal_mulai = fields.Date('Mulai')
    tanggal_selesai = fields.Date('Selesai')
    anggaran = fields.Float('Anggaran (Rp)', digits=(16, 0))
    tanpa_anggaran = fields.Boolean('Tanpa anggaran', help='Centang bila kegiatan memang tidak memerlukan biaya.')
    realisasi_ids = fields.One2many('labfik.rencana.realisasi', 'item_id', string='Realisasi', copy=True)
    is_lengkap = fields.Boolean('Lengkap', compute='_compute_is_lengkap')

    def _compute_is_lengkap(self):
        for rec in self:
            rec.is_lengkap = not rec._kekurangan()

    def _kekurangan(self):
        self.ensure_one()
        kurang = []
        if not self.sasaran:
            kurang.append(_('sasaran'))
        if not self.kpi_id:
            kurang.append(_('KPI'))
        if not self.target:
            kurang.append(_('target'))
        if not self.pic_id:
            kurang.append(_('PIC'))
        if not self.tanggal_mulai or not self.tanggal_selesai:
            kurang.append(_('jadwal'))
        if not self.tanpa_anggaran and self.anggaran <= 0:
            kurang.append(_('anggaran'))
        if not self.renstra_ids and not self.renstra_teks:
            kurang.append(_('keterkaitan Renstra'))
        return kurang

    @api.constrains('tanggal_mulai', 'tanggal_selesai')
    def _check_tanggal(self):
        for rec in self:
            if rec.tanggal_mulai and rec.tanggal_selesai and rec.tanggal_selesai < rec.tanggal_mulai:
                raise ValidationError(_('Tanggal selesai item harus setelah tanggal mulai.'))

    def _cek_draf(self, rencana):
        if not is_internal(self.env) and any(r.state != 'draf' for r in rencana):
            raise UserError(_('Item hanya dapat diubah selama rencana berstatus draf.'))

    @api.model_create_multi
    def create(self, vals_list):
        self._cek_draf(self.env['labfik.rencana'].browse([v.get('rencana_id') for v in vals_list if v.get('rencana_id')]))
        return super().create(vals_list)

    def write(self, vals):
        self._cek_draf(self.rencana_id)
        return super().write(vals)

    def unlink(self):
        self._cek_draf(self.rencana_id)
        return super().unlink()

    @api.depends('sasaran', 'rencana_id.name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = '%s › %s' % (rec.rencana_id.name or '', rec.sasaran or _('(tanpa sasaran)'))


class LabfikRencanaRealisasi(models.Model):
    _name = 'labfik.rencana.realisasi'
    _description = 'Realisasi item rencana kerja'
    _inherit = ['mail.thread']
    _order = 'tanggal desc, id desc'

    item_id = fields.Many2one('labfik.rencana.item', 'Item rencana', required=True, ondelete='cascade', index=True)
    rencana_id = fields.Many2one(related='item_id.rencana_id', store=True, string='Rencana')
    periode_id = fields.Many2one(related='item_id.rencana_id.periode_id', store=True, string='Periode')
    semester_id = fields.Many2one('labfik.periode.semester', 'Semester', required=True,
                                  domain="[('periode_id', '=', periode_id)]")
    tanggal = fields.Date('Tanggal lapor', required=True, default=fields.Date.context_today)
    capaian = fields.Char('Capaian', required=True, tracking=True)
    anggaran_terpakai = fields.Float('Anggaran terpakai (Rp)', digits=(16, 0))
    catatan = fields.Text('Catatan')
    bukti = fields.Binary('Bukti', attachment=True)
    bukti_name = fields.Char('Nama file bukti')
    berbukti = fields.Boolean('Berbukti', compute='_compute_berbukti', store=True)
    pelapor_id = fields.Many2one('labfik.personel', 'Pelapor', default=lambda self: personel_pengguna(self.env))

    @api.depends('bukti')
    def _compute_berbukti(self):
        for rec in self:
            rec.berbukti = bool(rec.bukti)

    @api.constrains('semester_id', 'item_id')
    def _check_semester(self):
        for rec in self:
            if rec.semester_id.periode_id != rec.item_id.rencana_id.periode_id:
                raise ValidationError(_('Semester realisasi harus berada pada periode rencana.'))

    @api.model_create_multi
    def create(self, vals_list):
        if not is_internal(self.env):
            items = self.env['labfik.rencana.item'].browse([v.get('item_id') for v in vals_list if v.get('item_id')])
            if any(i.rencana_id.state not in ('disahkan', 'selesai') for i in items):
                raise UserError(_('Realisasi hanya dapat dilaporkan untuk rencana yang sudah disahkan.'))
        return super().create(vals_list)


class LabfikRencanaTinjauan(models.Model):
    _name = 'labfik.rencana.tinjauan'
    _description = 'Tinjauan rencana kerja'
    _inherit = ['mail.thread']
    _order = 'tanggal desc, id desc'

    rencana_id = fields.Many2one('labfik.rencana', 'Rencana', required=True, ondelete='cascade', index=True,
                                 domain=[('state', 'in', ('disahkan', 'diganti', 'selesai'))])
    periode_id = fields.Many2one(related='rencana_id.periode_id', store=True)
    tanggal = fields.Date('Tanggal', required=True, default=fields.Date.context_today)
    peserta_ids = fields.Many2many('labfik.personel', 'labfik_tinjauan_peserta_rel', 'tinjauan_id', 'personel_id',
                                   string='Peserta')
    ringkasan = fields.Text('Ringkasan capaian', required=True)
    keputusan_ids = fields.One2many('labfik.rencana.tinjauan.keputusan', 'tinjauan_id', string='Keputusan')

    @api.model_create_multi
    def create(self, vals_list):
        if not is_internal(self.env):
            rencana = self.env['labfik.rencana'].browse([v.get('rencana_id') for v in vals_list if v.get('rencana_id')])
            if any(r.state not in ('disahkan', 'diganti', 'selesai') for r in rencana):
                raise UserError(_('Tinjauan hanya untuk rencana yang sudah disahkan.'))
        return super().create(vals_list)

    @api.depends('rencana_id.name', 'tanggal')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = _('Tinjauan %s (%s)', rec.rencana_id.name or '', tgl_id(rec.tanggal))


class LabfikRencanaTinjauanKeputusan(models.Model):
    _name = 'labfik.rencana.tinjauan.keputusan'
    _description = 'Keputusan tinjauan rencana kerja'
    _order = 'tinjauan_id, id'

    tinjauan_id = fields.Many2one('labfik.rencana.tinjauan', required=True, ondelete='cascade')
    uraian = fields.Text('Keputusan perbaikan', required=True)
    item_berikut_id = fields.Many2one('labfik.rencana.item', 'Ditindaklanjuti di item rencana berikutnya',
                                      help='Item pada rencana periode berikutnya yang menjalankan keputusan ini.')

    @api.constrains('item_berikut_id')
    def _check_item_berikut(self):
        for rec in self:
            if rec.item_berikut_id and rec.item_berikut_id.rencana_id == rec.tinjauan_id.rencana_id:
                raise ValidationError(_('Tindak lanjut harus ditautkan ke item pada rencana lain (periode berikutnya).'))
