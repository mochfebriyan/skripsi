# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    labfik_nama_lab = fields.Char('Nama laboratorium', config_parameter='labfik.nama_lab')
    labfik_siklus_tinjau_bulan = fields.Integer('Siklus tinjau ulang SOP (bulan)',
                                                config_parameter='labfik.siklus_tinjau_bulan', default=12)
    labfik_pengingat_hari = fields.Integer('Pengingat sebelum tinjau ulang (hari)',
                                           config_parameter='labfik.pengingat_hari', default=30)
    labfik_p1_k3_min_realisasi = fields.Integer('P1 K3: minimal realisasi per item per semester',
                                                config_parameter='labfik.p1_k3_min_realisasi', default=1)
    labfik_p3_k3_min_rapat = fields.Integer('P3 K3: minimal rapat koordinasi per semester',
                                            config_parameter='labfik.p3_k3_min_rapat', default=1)
    labfik_k4_min_per_tahun = fields.Integer('K4: minimal tinjauan/evaluasi per periode',
                                             config_parameter='labfik.k4_min_per_tahun', default=1)
