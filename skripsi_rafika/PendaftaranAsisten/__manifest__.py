# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<https://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'OpenEduCat Assistant Management',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    'sequence': 50,
    'summary': 'Manage Student Assistants and Assistant Registrations',
    'complexity': 'easy',
    'author': 'OpenEduCat Inc',
    'website': 'https://www.openeducat.org',
    
    # WAJIB: Inherit ekosistem OpenEducat utama
    'depends': [
        'base',
        'mail',
        'website',
        'portal',
        'openeducat_core',
        'openeducat_admission',
        'openeducat_library',
        'openeducat_fees',
        'openeducat_attendance',
        'web_openeducat',
        'openeducat_timetable',
        'openeducat_classroom',
        'openeducat_facility',
    ],
    
    # File data XML untuk views, security, dan menus
    'data': [
        # Security HARUS diload pertama agar model dikenali sebelum views/actions
        'security/security_groups.xml',
        'security/op_assistant_security.xml',
        'security/lab_security_groups.xml', # <-- FILE DARI FOLDER BACKUP
        'security/ir.model.access.csv',
        

        # Views: Form, Tree, Search, Kanban
        'views/op_student_assistant_view.xml',
        'views/op_assistant_registration_view.xml',
        'views/op_assistant_document_view.xml',
        'views/student_view_inherit.xml',
        'views/mst_coursesemt_view.xml',
        'views/mst_rolepermission_view.xml',
        'views/mst_dosen_view.xml',
        'views/mst_kurikulum_view.xml',
        'wizard/wizard_publikasi_views.xml',
        'views/mst_periodesemt_view.xml',
        'views/mst_kodekelas_view.xml',
        'views/calon_asprak_view.xml',
        'views/asprak_selection_view.xml',
        'views/asprak_allocation_view.xml',
        'views/sarpras_checklist_view.xml',
        'views/jadwal_praktikum_views.xml',
        'views/timetable_keseluruhan_view.xml',
        'views/assistant_planning_view.xml',

        # --- FILE VIEWS DARI FOLDER BACKUP ---
        'views/announcement_view.xml',
        'views/master_ruangan_view.xml',
        'views/mst_role_view.xml',
        'views/op_facility_inherit_view.xml',
        'views/readiness_checklist_view.xml',
        'views/registrasi_seleksi_view.xml',
        'views/res_users_view.xml',
        'views/self_allocation_view.xml',
        'views/student_reference_view.xml',
        'views/website_form.xml',
        # -------------------------------------

        # Menus (diload SETELAH semua views & security)
        'views/assistant_menu.xml',
        'views/website_portal_templates.xml',
        'views/templates.xml',
        'views/website_status_seleksi.xml',
        'views/website_selection_result.xml',
        'views/website_alokasi_jadwal.xml',

        # Data dan Report (optional)
        'data/mst_dosen_sequence.xml',
        'data/mst_kodekelas_sequence.xml',
        'data/mst_coursesemt_sequence.xml',
        'data/assistant_sequence.xml',
        'data/calon_asprak_sequence.xml',
        'data/asprak_selection_sequence.xml',
        'data/asprak_allocation_sequence.xml',
        'data/cron_jobs.xml',
    ],
    
    'demo': [],
    
    'images': [
        'static/description/openeducat_assistant_banner.jpg',
    ],
    
    'assets': {
        'web.assets_frontend': [
            'PendaftaranAsisten/static/src/js/logout_confirmation.js',
        ],
        'web.assets_backend': [
            'PendaftaranAsisten/static/src/js/logout_confirmation.js',
        ],
    },
    
    'installable': True,
    'auto_install': False,
    'application': True,
}