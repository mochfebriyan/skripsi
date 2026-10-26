# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class LabfikChecklistMulai(models.TransientModel):
    """Checklist mulai dari nol (FR-E1): menuntun urutan pengisian data awal."""
    _name = 'labfik.checklist.mulai'
    _description = 'Checklist mulai LabFIK'

    periode_id = fields.Many2one('labfik.periode', 'Periode aktif', compute='_compute_langkah')
    langkah_periode = fields.Boolean('1. Periode dan semester', compute='_compute_langkah')
    langkah_jabatan = fields.Boolean('2. Jabatan dilengkapi', compute='_compute_langkah')
    langkah_personel = fields.Boolean('3. Personel terdaftar', compute='_compute_langkah')
    langkah_sk = fields.Boolean('4. SK penetapan berlaku', compute='_compute_langkah')
    langkah_wajib = fields.Boolean('5. Daftar SOP wajib', compute='_compute_langkah')
    langkah_rencana = fields.Boolean('6. Rencana kerja disahkan', compute='_compute_langkah')
    ket_periode = fields.Char(compute='_compute_langkah')
    ket_jabatan = fields.Char(compute='_compute_langkah')
    ket_personel = fields.Char(compute='_compute_langkah')
    ket_sk = fields.Char(compute='_compute_langkah')
    ket_wajib = fields.Char(compute='_compute_langkah')
    ket_rencana = fields.Char(compute='_compute_langkah')
    progres = fields.Integer('Progres (%)', compute='_compute_langkah')

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = _('Mulai di sini')

    def _compute_langkah(self):
        hari_ini = fields.Date.context_today(self)
        env = self.env
        periode = env['labfik.periode'].periode_pada(hari_ini)
        jabatan = env['labfik.jabatan'].search([])
        jabatan_kurang = jabatan.filtered(lambda j: j._kekurangan(hari_ini, cek_pemangku=False))
        personel = env['labfik.personel'].search_count([])
        sk = env['labfik.sk'].search([('state', '=', 'berlaku')])
        wajib = periode.wajib_ids if periode else env['labfik.dokumen.wajib']
        rencana = env['labfik.rencana'].search([('periode_id', '=', periode.id), ('jenis', '=', 'tahunan')]) \
            if periode else env['labfik.rencana']
        rencana_sah = rencana.filtered(lambda r: r.state in ('disahkan', 'selesai'))
        for rec in self:
            rec.periode_id = periode
            rec.langkah_periode = bool(periode and periode.semester_ids)
            rec.ket_periode = periode.name if periode else _('Belum ada periode')
            rec.langkah_jabatan = bool(jabatan) and not jabatan_kurang
            rec.ket_jabatan = _('%s jabatan belum lengkap', len(jabatan_kurang)) if jabatan_kurang \
                else _('%s jabatan lengkap', len(jabatan))
            rec.langkah_personel = personel > 0
            rec.ket_personel = _('%s personel', personel)
            rec.langkah_sk = bool(sk)
            rec.ket_sk = ', '.join(sk.mapped('name')) or _('Belum ada SK berlaku')
            rec.langkah_wajib = bool(wajib)
            rec.ket_wajib = _('%s SOP wajib', len(wajib))
            rec.langkah_rencana = bool(rencana_sah)
            rec.ket_rencana = _('Disahkan') if rencana_sah else (
                _('Ada, belum disahkan') if rencana else _('Belum ada'))
            selesai = sum([rec.langkah_periode, rec.langkah_jabatan, rec.langkah_personel,
                           rec.langkah_sk, rec.langkah_wajib, rec.langkah_rencana])
            rec.progres = round(selesai * 100 / 6)

    @api.model
    def action_buka(self):
        """Dibuka dari menu lewat server action: rekaman disimpan dulu agar kolom terhitung terisi."""
        rec = self.create({})
        return {
            'type': 'ir.actions.act_window',
            'name': _('Mulai di sini'),
            'res_model': self._name,
            'res_id': rec.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def _buka(self, xmlid):
        return self.env['ir.actions.act_window']._for_xml_id(xmlid)

    def action_periode(self):
        return self._buka('labfik_org.action_periode')

    def action_jabatan(self):
        return self._buka('labfik_org.action_jabatan')

    def action_personel(self):
        return self._buka('labfik_org.action_personel')

    def action_sk(self):
        return self._buka('labfik_org.action_sk')

    def action_wajib(self):
        return self._buka('labfik_org.action_periode')

    def action_rencana(self):
        return self._buka('labfik_org.action_rencana')
