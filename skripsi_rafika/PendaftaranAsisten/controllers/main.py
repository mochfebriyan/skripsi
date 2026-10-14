# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import http
# pyrefly: ignore [missing-import]
from odoo.http import request
# pyrefly: ignore [missing-import]
from odoo.addons.portal.controllers.portal import CustomerPortal
import base64
from datetime import date

class PendaftaranAsistenPortal(CustomerPortal):
    """Override /my untuk redirect mahasiswa ke halaman pendaftaran."""

    @http.route(['/my', '/my/home'], type='http', auth='user', website=True)
    def home(self, **kw):
        user = request.env.user
        if user.has_group('base.group_portal'):
            return request.redirect('/pendaftaran-asisten')
        return super(PendaftaranAsistenPortal, self).home(**kw)


class PendaftaranAsistenController(http.Controller):

    @http.route('/pendaftaran-asisten', type='http', auth='user', website=True, methods=['GET'])
    def pendaftaran_form(self, **kw):
        user = request.env.user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)

        # Mencari periode yang statusnya Active
        periode_aktif = request.env['mst_periodesemt'].sudo().search([('active', '=', True)], limit=1)
        master_courses = request.env['mst_coursesemt'].sudo().search([('is_praktikum_lab', '=', True)])

        # --- TAMBAHAN LOGIKA DEADLINE DI HALAMAN DEPAN ---
        is_closed = False
        if periode_aktif and periode_aktif.deadline_date:
            if date.today() > periode_aktif.deadline_date:
                is_closed = True
        # ------------------------------------------------

        pendaftaran = False
        if student:
            pendaftaran = request.env['registrasi.asprak'].sudo().search([
                ('mahasiswa_id', '=', student.id)
            ], limit=1)

        values = {
            'main_object': request.env['website'].get_current_website(),
            'periode': periode_aktif,
            'master_courses': master_courses,
            'pendaftaran': pendaftaran,
            'student': student,
            'is_closed': is_closed,  # <-- Kirim status tutup ke XML
            'error': {},
            'error_msg': kw.get('error', ''),
            'success': kw.get('success', ''),
            'data': kw,
        }
        return request.render('PendaftaranAsisten.website_pendaftaran_form', values)

    @http.route('/pendaftaran-asisten/submit', type='http', auth='user', website=True, methods=['POST'])
    def submit_pendaftaran(self, **post):
        user = request.env.user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)
        if not student:
            return request.redirect('/pendaftaran-asisten?error=student_not_found')

        periode_id_raw = post.get('periode_id', '')
        try:
            periode_id = int(periode_id_raw)
        except (ValueError, TypeError):
            # Fallback ke periode aktif jika ID tidak valid
            periode_aktif = request.env['mst_periodesemt'].sudo().search([('active', '=', True)], limit=1)
            periode_id = periode_aktif.id if periode_aktif else False

        # --- PERBAIKAN: Pengecekan Periode Aktif ---
        # Mencegah error 400 jika tidak ada periode aktif di database
        if not periode_id:
            pesan_error = "Pendaftaran gagal: Tidak ada Periode Semester yang aktif saat ini. Silakan hubungi Laboran."
            return request.redirect(f'/pendaftaran-asisten?error={pesan_error}')
        # -------------------------------------------

        # =========================================================
        # --- TAMBAHAN LOGIKA DEADLINE ---
        # =========================================================
        periode_obj = request.env['mst_periodesemt'].sudo().browse(periode_id)
        if periode_obj.deadline_date:
            if date.today() > periode_obj.deadline_date:
                pesan_error = "Pendaftaran Ditolak: Mohon maaf, periode rekrutmen sudah kedaluwarsa atau ditutup otomatis oleh sistem."
                return request.redirect(f'/pendaftaran-asisten?error={pesan_error}')
        # =========================================================

        berkas_khs = request.httprequest.files.get('berkas_khs')
        berkas_data = False
        if berkas_khs and hasattr(berkas_khs, 'read'):
            raw = berkas_khs.read()
            if raw:
                berkas_data = base64.b64encode(raw)

        data_simpan = {
            'mahasiswa_id': student.id,
            'periode_semester_id': periode_id,
        }

        if berkas_data:
            data_simpan['berkas_khs'] = berkas_data

        phone_number = post.get('phone_number')
        if phone_number:
            data_simpan['phone_number'] = phone_number

        course_ids_raw = request.httprequest.form.getlist('course_ids')
        if course_ids_raw:
            detail_lines = []
            for cid in course_ids_raw:
                detail_lines.append((0, 0, {'mata_kuliah_target_id': int(cid)}))
            data_simpan['detail_ids'] = detail_lines

        new_registrasi = request.env['registrasi.asprak'].sudo().create(data_simpan)
        new_registrasi.action_submit_registration()

        return request.redirect('/pendaftaran-asisten')

    @http.route('/pendaftaran-asisten/success', type='http', auth='public', website=True)
    def pendaftaran_success(self, **kw):
        return request.render('PendaftaranAsisten.website_form_success', {
            'main_object': request.env['website'].get_current_website(),
        })

    @http.route('/my/hasil-seleksi', type='http', auth='user', website=True)
    def hasil_seleksi(self, **kw):
        user = request.env.user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)
        if not student:
            return request.redirect('/my/home')

        pendaftaran = request.env['registrasi.asprak'].sudo().search([
            ('mahasiswa_id', '=', student.id)
        ], limit=1)

        selection = request.env['asprak.selection'].sudo().search([
            ('registrasi_calon_asisten_id', '=', pendaftaran.id)
        ], limit=1) if pendaftaran else False

        status_admin = pendaftaran.state if pendaftaran else 'draft'
        status_final = selection.status_seleksi if selection else 'draft'
        skep_file = pendaftaran.periode_semester_id.skep_file if pendaftaran and pendaftaran.periode_semester_id else False

        return request.render('PendaftaranAsisten.website_selection_result', {
            'main_object': request.env['website'].get_current_website(),
            'pendaftaran': pendaftaran,
            'selection': selection,
            'status_admin': status_admin,
            'status_final': status_final,
            'skep_file': skep_file,
        })

    @http.route('/status-seleksi', type='http', auth='user', website=True, methods=['GET'])
    def status_seleksi_view(self, **kw):
        user = request.env.user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)
        if not student:
            return request.redirect('/my/home')

        pendaftaran = request.env['registrasi.asprak'].sudo().search([('mahasiswa_id', '=', student.id)], limit=1)
        
        selection = request.env['asprak.selection'].sudo().search([
            ('registrasi_calon_asisten_id', '=', pendaftaran.id)
        ], limit=1) if pendaftaran else False

        status = False
        if selection:
            status = selection.status_seleksi if hasattr(selection, 'status_seleksi') else False
        elif pendaftaran:
            if hasattr(pendaftaran, 'hasil_seleksi'):
                status = pendaftaran.hasil_seleksi
                
        skep_file = pendaftaran.periode_semester_id.skep_file if pendaftaran and pendaftaran.periode_semester_id else False

        values = {
            'main_object': request.env['website'].get_current_website(),
            'pendaftaran': pendaftaran,
            'selection': selection,
            'status': status,
            'skep_file': skep_file,
        }
        return request.render('PendaftaranAsisten.website_status_seleksi', values)

    @http.route('/download/skep-rektor/<int:id>', type='http', auth='user', website=True, methods=['GET'])
    def download_skep_rektor_id(self, id, **kw):
        pendaftaran = request.env['registrasi.asprak'].sudo().browse(id)
        if pendaftaran.exists() and pendaftaran.periode_semester_id and pendaftaran.periode_semester_id.skep_file:
            filecontent = base64.b64decode(pendaftaran.periode_semester_id.skep_file)
            skep_filename = pendaftaran.periode_semester_id.skep_filename or 'SKEP_Rektor.pdf'
            headers = [
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'attachment; filename="{skep_filename}"'),
            ]
            return request.make_response(filecontent, headers)
        return request.redirect('/status-seleksi')

    @http.route('/my/alokasi-jadwal', type='http', auth='user', website=True)
    def portal_alokasi_jadwal(self, **kw):
        user = request.env.user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)
        if not student:
            return request.redirect('/my/home')

        jadwal_tersedia = request.env['jadwal.praktikum'].sudo().search([])

        return request.render('PendaftaranAsisten.website_alokasi_jadwal', {
            'jadwal_list': jadwal_tersedia,
            'student': student,
            'success_msg': kw.get('success'),
            'error_msg': kw.get('error'),
        })

    @http.route('/my/alokasi-jadwal/pilih-pertemuan/<int:jadwal_id>', type='http', auth='user', website=True)
    def pilih_pertemuan(self, jadwal_id, **kw):
        user = request.env.user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)
        if not student:
            return request.redirect('/my/home')
        jadwal = request.env['jadwal.praktikum'].sudo().browse(jadwal_id)
        if not jadwal.exists():
            return request.redirect('/my/alokasi-jadwal?error=Jadwal tidak ditemukan.')
        return request.render('PendaftaranAsisten.website_form_combo_box', {
            'jadwal': jadwal,
            'student': student,
        })

    @http.route('/my/alokasi-jadwal/submit', type='http', auth='user', website=True, methods=['POST'])
    def submit_alokasi_jadwal(self, **post):
        user = request.env.user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)
        if not student:
            return request.redirect('/my/home')
        try:
            jadwal_id = int(post.get('jadwal_id', 0))
        except (ValueError, TypeError):
            return request.redirect('/my/alokasi-jadwal?error=Data jadwal tidak valid.')
        try:
            pertemuan_ke = int(post.get('pertemuan_ke', 0))
        except (ValueError, TypeError):
            pertemuan_ke = 0
        jadwal = request.env['jadwal.praktikum'].sudo().browse(jadwal_id)
        if not jadwal.exists() or not jadwal_id:
            return request.redirect('/my/alokasi-jadwal?error=Jadwal tidak ditemukan.')
        if len(jadwal.asisten_ids) >= jadwal.kuota_asisten:
            return request.redirect('/my/alokasi-jadwal?error=Mohon maaf, kuota kelas ini sudah penuh.')
        
        jadwal_sebelumnya = request.env['jadwal.praktikum'].sudo().search([
            ('asisten_ids', 'in', student.id),
            ('hari', '=', jadwal.hari),
            ('id', '!=', jadwal.id),
        ])
        for j_lama in jadwal_sebelumnya:
            # String comparison for 'HH:MM' works correctly
            overlap = (str(jadwal.jam_mulai) < str(j_lama.jam_selesai)) and (str(jadwal.jam_selesai) > str(j_lama.jam_mulai))
            if overlap:
                jam_mulai_str = str(j_lama.jam_mulai)
                jam_selesai_str = str(j_lama.jam_selesai)
                nama_matkul = j_lama.mata_kuliah_id.nama_matkul if j_lama.mata_kuliah_id else 'Jadwal Praktikum Lain'
                error_pesan = 'Gagal! Jadwal ini bentrok dengan %s (%s - %s).' % (nama_matkul, jam_mulai_str, jam_selesai_str)
                return request.redirect('/my/alokasi-jadwal?error=%s' % error_pesan)
        
        try:
            jadwal.sudo().write({
                'asisten_ids': [(4, student.id)],
                'pertemuan_ke': pertemuan_ke,
            })
            return request.redirect('/my/alokasi-jadwal?success=Alokasi Jadwal Berhasil!')
        except Exception:
            return request.redirect('/my/alokasi-jadwal?error=Terjadi kesalahan sistem saat menyimpan data.')