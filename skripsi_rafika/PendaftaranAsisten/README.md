===========================================
OpenEduCat Assistant Management Module
===========================================

**Modul Custom Terintegrasi Penuh OpenEducat v17**

Fitur Utama:
============

1. **Student Assistant Master Data** (op.student.assistant)
   - Link ke model op.student untuk data personal terintegrasi
   - Tipe asisten: Teaching, Lab, Library, Admin, Research
   - Manajemen departemen & penawas (faculty supervisor)
   - Tracking jam kerja (hours_per_week)
   - Manajemen kompensasi (hourly, monthly, stipend, unpaid)
   - Status workflow: Draft → Submitted → Approved → Active → Completed

2. **Assistant Registration Form** (op.assistant.registration)
   - Form aplikasi untuk mendaftar menjadi asisten
   - Auto-generate registration number (AST/YYYY/#####)
   - Link ke student profile untuk auto-fill data
   - Motivasi, pengalaman kerja, dan kompetensi
   - Workflow approval dengan tracking reviewer
   - Auto-create op.student.assistant record saat approve

3. **Supporting Documents** (op.assistant.document)
   - Upload dokumen: KTP, sertifikat, kontrak, CV, transcript, recommendation letter
   - Tracking tanggal dokumen dan kadaluarsa
   - Link ke assistant record

4. **Student Model Enhancement**
   - Tambahan field: is_assistant, assistant_id, assistant_count
   - Smart link ke assistant records dengan computed fields
   - Akses quick-view dari student form ke assistant records

Struktur Keamanan:
==================

Groups (res.groups):
- openeducat_assistant.group_op_assistant_manager
  → Full access ke semua operasi asisten
  
- openeducat_assistant.group_op_assistant_user
  → Daftar sebagai asisten dengan akses terbatas
  
Inheritance dari OpenEducat groups:
- openeducat_core.group_op_back_office_admin
  → Full management capabilities
  
- openeducat_core.group_op_faculty
  → Read-only access untuk info asisten

Access Control (ir.model.access):
- CSV-based permission matrix dengan read/write/create/unlink untuk setiap group
- Record Rules untuk pembatasan domain-level access

Integrasi OpenEducat:
====================

✓ DEPENDS: openeducat_core, openeducat_admission, openeducat_library, openeducat_fees, openeducat_attendance
✓ Model Inheritance: _inherit = 'mail.thread', 'mail.activity.mixin'
✓ View Inheritance: inherit dari openeducat_core.view_op_student_form
✓ Security: menggunakan groups OpenEducat standard
✓ Menus: terintegrasi dengan menu struktur OpenEducat utama

Instalasi:
==========

1. Copy folder "openeducat_assistant" ke dalam openeducat_erp/
2. Buka Odoo dan tambahkan ke Apps (Update App List)
3. Search "Assistant Management" dan install
4. Sesuaikan user groups dengan kebutuhan

Developer Notes:
================

File Structure:
- __manifest__.py        → Metadata modul
- models/
  ├── assistant.py       → 3 model utama (Student Assistant, Registration, Document)
  ├── config_settings.py → Placeholder settings
  └── __init__.py        → Import models
- views/
  ├── op_student_assistant_view.xml      → Form, Tree, Kanban, Search
  ├── op_assistant_registration_view.xml → Registration forms
  ├── op_assistant_document_view.xml     → Document forms
  ├── student_view_inherit.xml           → Inherit openeducat_core views
  └── assistant_menu.xml                 → Menu structure
- security/
  ├── op_assistant_security.xml → Groups dan Record Rules
  └── ir.model.access.csv       → Permission matrix
- data/
  └── assistant_sequence.xml    → Auto-increment sequences
- static/
  └── description/              → Documentation images

Kustomisasi Lebih Lanjut:
=========================

1. Tambahkan Report/PDF: Buat di folder "report/"
2. Webhook Notifications: Edit models assistant.py untuk action_approve() +
3. Analytics Dashboard: Extend dengan Kanban/Reports
4. Multi-language: Buat i18n/
5. Attendance Tracking: Integrate dengan openeducat_attendance

Kompatibilitas:
===============

- Odoo 17.0+
- Python 3.8+
- OpenEducat v17

License: LGPL-3
Author: OpenEduCat Inc
