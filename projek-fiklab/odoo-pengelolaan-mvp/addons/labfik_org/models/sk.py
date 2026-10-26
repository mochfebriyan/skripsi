# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

from .common import cek_kalab, is_internal, tgl_id

SK_STATE = [('draf', 'Draf'), ('berlaku', 'Berlaku'), ('dicabut', 'Dicabut')]
FIELD_BOLEH_SETELAH_BERLAKU = {'state', 'lampiran_versi_id', 'line_ids'}  # baris dicek di labfik.sk.line


class LabfikSk(models.Model):
    _name = 'labfik.sk'
    _description = 'SK penetapan pengelola laboratorium'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'labfik.lampiran.mixin']
    _order = 'tanggal desc, id desc'
    _lampiran_jenis = 'sk'
    _lampiran_prefix = 'SK'

    name = fields.Char('Nomor SK', required=True, tracking=True)
    perihal = fields.Char('Perihal', required=True, default='Penetapan Pengelola Laboratorium FIK')
    tanggal = fields.Date('Tanggal SK', required=True, default=fields.Date.context_today, tracking=True)
    pengesah_id = fields.Many2one('labfik.personel', 'Ditetapkan oleh', tracking=True,
                                  help='Pejabat penandatangan, misalnya Dekan.')
    tanggal_mulai = fields.Date('Berlaku mulai', required=True, tracking=True)
    tanggal_selesai = fields.Date('Berlaku sampai', tracking=True)
    state = fields.Selection(SK_STATE, string='Status', default='draf', required=True, tracking=True, copy=False)
    line_ids = fields.One2many('labfik.sk.line', 'sk_id', string='Personel dan jabatan', copy=True)
    jumlah_personel = fields.Integer('Jumlah penetapan', compute='_compute_jumlah')

    @api.depends('line_ids')
    def _compute_jumlah(self):
        for rec in self:
            rec.jumlah_personel = len(rec.line_ids)

    @api.constrains('tanggal_mulai', 'tanggal_selesai')
    def _check_tanggal(self):
        for rec in self:
            if rec.tanggal_selesai and rec.tanggal_selesai < rec.tanggal_mulai:
                raise ValidationError(_('Tanggal akhir berlaku SK harus setelah tanggal mulai.'))

    def _lampiran_terkunci(self):
        return self.state != 'draf'

    def _lampiran_judul(self):
        return _('SK %s', self.name)

    def _aktif_pada(self, tanggal):
        self.ensure_one()
        return (self.state == 'berlaku' and self.tanggal_mulai <= tanggal
                and (not self.tanggal_selesai or tanggal <= self.tanggal_selesai))

    def write(self, vals):
        if not is_internal(self.env) and any(r.state != 'draf' for r in self):
            terlarang = set(vals) - FIELD_BOLEH_SETELAH_BERLAKU
            terlarang = {f for f in terlarang if not f.startswith(('message_', 'activity_'))}
            if terlarang:
                raise UserError(_('SK yang sudah berlaku atau dicabut tidak dapat diubah. '
                                  'Buat SK baru untuk perubahan struktur.'))
        res = super().write(vals)
        if 'state' in vals or 'tanggal_selesai' in vals or 'tanggal_mulai' in vals:
            self.line_ids.personel_id._sync_akses()
        return res

    def unlink(self):
        if any(r.state != 'draf' for r in self):
            raise UserError(_('Hanya SK berstatus draf yang dapat dihapus.'))
        return super().unlink()

    def action_berlakukan(self):
        cek_kalab(self.env, _('memberlakukan SK'))
        for rec in self:
            if rec.state != 'draf':
                raise UserError(_('Hanya SK draf yang dapat diberlakukan.'))
            kurang = []
            if not rec.pengesah_id:
                kurang.append(_('pejabat yang menetapkan'))
            if not rec.lampiran_versi_id:
                kurang.append(_('file SK bertanda tangan'))
            if not rec.line_ids:
                kurang.append(_('minimal satu personel dan jabatan'))
            if kurang:
                raise UserError(_('SK %s belum dapat diberlakukan. Lengkapi: %s.', rec.name, ', '.join(kurang)))
            rec.with_context(labfik_internal=True).write({'state': 'berlaku'})
            rec._message_log(body=_('SK diberlakukan oleh %s.', self.env.user.name))
        return True

    def action_cabut(self):
        cek_kalab(self.env, _('mencabut SK'))
        for rec in self:
            if rec.state != 'berlaku':
                raise UserError(_('Hanya SK yang berlaku yang dapat dicabut.'))
            rec.with_context(labfik_internal=True).write({'state': 'dicabut'})
            rec._message_log(body=_('SK dicabut oleh %s.', self.env.user.name))
        return True

    def tgl_id(self, value):
        return tgl_id(value)

    def get_data_struktur(self):
        """Data untuk bagan organisasi dan matriks kewenangan: jabatan aktif + pemangku dari SK ini."""
        self.ensure_one()
        jabatan = self.env['labfik.jabatan'].search([])
        pemangku = {}
        for line in self.line_ids:
            if line.tanggal_selesai and line.tanggal_selesai < fields.Date.context_today(self):
                continue
            pemangku.setdefault(line.jabatan_id.id, []).append(line.personel_id.name)
        akar = jabatan.filtered(lambda j: not j.atasan_id or j.atasan_id not in jabatan)
        return {
            'jabatan': jabatan,
            'akar': akar,
            'pemangku': pemangku,
            'kewenangan': self.env['labfik.kewenangan'].search([]),
        }


class LabfikSkLine(models.Model):
    _name = 'labfik.sk.line'
    _description = 'Penetapan personel pada jabatan'
    _order = 'sk_id, jabatan_id, id'

    sk_id = fields.Many2one('labfik.sk', 'SK', required=True, ondelete='cascade', index=True)
    sk_state = fields.Selection(related='sk_id.state', string='Status SK')
    personel_id = fields.Many2one('labfik.personel', 'Personel', required=True, index=True,
                                  domain=[('active', '=', True)])
    jabatan_id = fields.Many2one('labfik.jabatan', 'Jabatan', required=True, index=True)
    tanggal_mulai = fields.Date('Mulai', help='Kosong = mengikuti tanggal mulai SK.')
    tanggal_selesai = fields.Date('Selesai', help='Kosong = mengikuti akhir berlaku SK.')
    tanggal_selesai_efektif = fields.Date('Selesai efektif', compute='_compute_efektif')
    is_aktif = fields.Boolean('Aktif hari ini', compute='_compute_is_aktif')
    catatan = fields.Char('Catatan')

    @api.depends('tanggal_selesai', 'sk_id.tanggal_selesai')
    def _compute_efektif(self):
        for rec in self:
            ends = [d for d in (rec.tanggal_selesai, rec.sk_id.tanggal_selesai) if d]
            rec.tanggal_selesai_efektif = min(ends) if ends else False

    def _compute_is_aktif(self):
        hari_ini = fields.Date.context_today(self)
        for rec in self:
            rec.is_aktif = rec._aktif_pada(hari_ini)

    def _aktif_pada(self, tanggal):
        self.ensure_one()
        if not self.sk_id._aktif_pada(tanggal):
            return False
        mulai = self.tanggal_mulai or self.sk_id.tanggal_mulai
        if mulai and tanggal < mulai:
            return False
        if self.tanggal_selesai and tanggal > self.tanggal_selesai:
            return False
        return True

    @api.constrains('tanggal_mulai', 'tanggal_selesai')
    def _check_tanggal(self):
        for rec in self:
            if rec.tanggal_mulai and rec.tanggal_selesai and rec.tanggal_selesai < rec.tanggal_mulai:
                raise ValidationError(_('Tanggal selesai jabatan harus setelah tanggal mulai.'))

    @api.model_create_multi
    def create(self, vals_list):
        if not is_internal(self.env):
            sks = self.env['labfik.sk'].browse([v.get('sk_id') for v in vals_list if v.get('sk_id')])
            if any(s.state != 'draf' for s in sks):
                raise UserError(_('Tidak dapat menambah penetapan pada SK yang sudah berlaku. Buat SK baru.'))
        # Aturan integritas: berlaku untuk semua pemanggil, termasuk sistem.
        personel = self.env['labfik.personel'].sudo().with_context(active_test=False).browse(
            [v.get('personel_id') for v in vals_list if v.get('personel_id')])
        if any(not p.active for p in personel):
            raise UserError(_('Personel nonaktif tidak dapat ditetapkan pada jabatan.'))
        records = super().create(vals_list)
        records.personel_id._sync_akses()
        return records

    def write(self, vals):
        if not is_internal(self.env) and any(r.sk_id.state != 'draf' for r in self):
            if set(vals) - {'tanggal_selesai', 'catatan'}:
                raise UserError(_('Pada SK yang sudah berlaku, penetapan hanya dapat diakhiri '
                                  '(isi tanggal selesai).'))
        personel_lama = self.personel_id
        res = super().write(vals)
        if 'tanggal_selesai' in vals:
            for rec in self.filtered(lambda r: r.sk_id.state != 'draf'):
                rec.sk_id._message_log(body=_('Penetapan %s sebagai %s diakhiri per %s.',
                                              rec.personel_id.name, rec.jabatan_id.name,
                                              rec.tanggal_selesai or '-'))
        (personel_lama | self.personel_id)._sync_akses()
        return res

    def action_akhiri(self):
        cek_kalab(self.env, _('mengakhiri penetapan jabatan'))
        hari_ini = fields.Date.context_today(self)
        for rec in self:
            if rec.sk_id.state != 'berlaku':
                raise UserError(_('Hanya penetapan pada SK yang berlaku yang dapat diakhiri.'))
            if rec.tanggal_selesai and rec.tanggal_selesai <= hari_ini:
                continue
            rec.write({'tanggal_selesai': max(hari_ini, rec.tanggal_mulai or rec.sk_id.tanggal_mulai)})
        return True

    def unlink(self):
        if not is_internal(self.env) and any(r.sk_id.state != 'draf' for r in self):
            raise UserError(_('Penetapan pada SK yang sudah berlaku tidak dapat dihapus; akhiri dengan tanggal selesai.'))
        personel = self.personel_id
        res = super().unlink()
        personel.exists()._sync_akses()
        return res
