# -*- coding: utf-8 -*-
"""Utilitas bersama: parameter ambang, konversi skor, dan format tanggal Indonesia."""
from babel.dates import format_date as babel_format_date

from odoo import _
from odoo.exceptions import UserError

PARAM_DEFAULTS = {
    'labfik.siklus_tinjau_bulan': 12,
    'labfik.pengingat_hari': 30,
    'labfik.p1_k3_min_realisasi': 1,
    'labfik.p3_k3_min_rapat': 1,
    'labfik.k4_min_per_tahun': 1,
}

GROUP_KALAB = 'labfik_org.group_labfik_kalab'
GROUP_PENILAI = 'labfik_org.group_labfik_penilai'
GROUP_ADMIN = 'labfik_org.group_labfik_admin'

# Konteks untuk transisi status yang dilakukan sistem sendiri (melewati kunci tulis).
CTX_INTERNAL = 'labfik_internal'


def get_param_int(env, key):
    value = env['ir.config_parameter'].sudo().get_param(key)
    try:
        number = int(value)
    except (TypeError, ValueError):
        return PARAM_DEFAULTS[key]
    return max(number, 0)


def skor_dari_persen(persen):
    """Ambang Instrumen Monev: 100% → 4, 90–<100% → 3, 70–<90% → 2, <70% → 1. None → 0 (N/A)."""
    if persen is None:
        return 0
    if persen >= 100:
        return 4
    if persen >= 90:
        return 3
    if persen >= 70:
        return 2
    return 1


def tgl_id(value):
    """Tanggal dalam format Indonesia, misalnya '1 Juni 2027', tanpa bergantung bahasa pengguna."""
    if not value:
        return ''
    return babel_format_date(value, 'd MMMM y', locale='id_ID')


def is_internal(env):
    return env.su or env.context.get(CTX_INTERNAL)


def cek_kalab(env, aksi):
    """Hanya Kepala Laboratorium (atau sistem) yang boleh melakukan aksi pengesahan."""
    if env.su:
        return
    if not env.user.has_group(GROUP_KALAB):
        raise UserError(_('Hanya Kepala Laboratorium yang dapat %s.', aksi))


def personel_pengguna(env):
    return env['labfik.personel'].sudo().search([('user_id', '=', env.uid)], limit=1)
