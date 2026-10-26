# -*- coding: utf-8 -*-
{
    'name': 'LabFIK Organization Management',
    'summary': 'Struktur, SOP, dan rencana kerja laboratorium untuk Instrumen Monev '
               '(Pengelolaan 1, 2, 3)',
    'description': """
MVP LabFIK Compliance untuk indikator Instrumen Monev Laboratorium UPNVJ 2026.

* Pengelolaan 1: rencana kerja tahunan (form, cetak baku, realisasi, tinjauan)
* Pengelolaan 2: pengendalian SOP/IK (daftar wajib, versi, pengesahan, distribusi, sosialisasi)
* Pengelolaan 3: struktur organisasi (personel, jabatan, SK, hak akses, rapat, evaluasi)
* Status kepatuhan ketiga indikator beserta snapshot periode monev
""",
    'version': '17.0.1.0.0',
    'category': 'LabFIK',
    'author': 'Febriyan (LabFIK Compliance)',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'data/config_default.xml',
        'data/jabatan_standar.xml',
        'data/cron.xml',
        'wizard/tolak_wizard_views.xml',
        'views/periode_views.xml',
        'views/ruang_views.xml',
        'views/personel_views.xml',
        'views/jabatan_views.xml',
        'views/sk_views.xml',
        'views/rapat_views.xml',
        'views/dokumen_views.xml',
        'views/kpi_views.xml',
        'views/rencana_views.xml',
        'views/kepatuhan_views.xml',
        'views/checklist_views.xml',
        'views/res_config_settings_views.xml',
        'views/menu.xml',
        'report/report_actions.xml',
        'report/report_rencana.xml',
        'report/report_struktur.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
