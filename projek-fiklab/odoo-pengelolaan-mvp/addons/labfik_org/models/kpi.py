# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LabfikKpi(models.Model):
    _name = 'labfik.kpi'
    _description = 'Indikator kinerja (KPI) laboratorium'
    _order = 'kode'

    kode = fields.Char('Kode', required=True)
    name = fields.Char('Nama KPI', required=True)
    definisi = fields.Text('Definisi')
    pembilang = fields.Char('Pembilang')
    penyebut = fields.Char('Penyebut')
    satuan = fields.Char('Satuan', help='Contoh: %, jumlah, hari')
    sumber_data = fields.Char('Sumber data')
    active = fields.Boolean(default=True)

    _sql_constraints = [('kode_unique', 'unique(kode)', 'Kode KPI sudah dipakai.')]

    @api.depends('kode', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = '%s · %s' % (rec.kode, rec.name) if rec.kode else rec.name


class LabfikRenstraSasaran(models.Model):
    _name = 'labfik.renstra.sasaran'
    _description = 'Sasaran Renstra institusi'
    _order = 'tingkat, kode'

    tingkat = fields.Selection([('upnvj', 'UPNVJ'), ('upps', 'UPPS/FIK'), ('prodi', 'Program studi')],
                               string='Tingkat', required=True, default='upps')
    kode = fields.Char('Kode', required=True)
    name = fields.Char('Uraian sasaran', required=True)
    dokumen_sumber = fields.Char('Dokumen sumber', help='Judul, nomor, dan tahun dokumen Renstra')
    active = fields.Boolean(default=True)

    @api.depends('kode', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = '%s · %s' % (rec.kode, rec.name) if rec.kode else rec.name
