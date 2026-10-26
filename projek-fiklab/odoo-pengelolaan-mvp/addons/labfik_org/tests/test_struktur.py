# -*- coding: utf-8 -*-
"""Pengelolaan 3: struktur, jabatan, SK, laporan cetak (TC-P3-01 … TC-P3-07)."""
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError, ValidationError
from odoo.tests import tagged

from .common import LabfikCase


@tagged('post_install', '-at_install', 'labfik')
class TestStruktur(LabfikCase):

    def test_jabatan_standar_terpasang(self):
        """TC-P3-03 / FR-E2: lima jabatan standar beserta hak akses dan kewenangan standar terpasang."""
        nama = set(self.env['labfik.jabatan'].search([]).mapped('name'))
        self.assertTrue({'Kepala Laboratorium', 'Laboran/PLP', 'Petugas K3', 'Dosen Pengampu Praktikum',
                         'Asisten Praktikum'} <= nama)
        self.assertIn(self.env.ref('labfik_org.group_labfik_kalab'), self.j['kalab'].group_ids)
        self.assertTrue(self.j['kalab'].is_puncak)
        self.assertGreaterEqual(self.env['labfik.kewenangan'].search_count([]), 8)
        # Uraian tugas sengaja kosong: jabatan standar belum lengkap sampai diisi lab.
        self.assertIn('uraian tugas', self.j['laboran'].kekurangan)

    def test_pengganti_dan_atasan_tidak_boleh_diri_sendiri(self):
        """FR-A8: jabatan tidak boleh menjadi pengganti/atasannya sendiri."""
        with self.assertRaises(ValidationError):
            self.j['laboran'].pengganti_id = self.j['laboran']
        with self.assertRaises(ValidationError):
            self.j['laboran'].atasan_id = self.j['laboran']

    def test_atasan_melingkar_ditolak(self):
        """FR-A8: struktur atasan tidak boleh membentuk lingkaran."""
        with self.assertRaises(ValidationError):
            self.j['kalab'].atasan_id = self.j['asisten']  # asisten → laboran → kalab → asisten

    def test_grup_jabatan_hanya_grup_labfik(self):
        """Keamanan: jabatan tidak boleh memberi grup di luar LabFIK atau Admin LabFIK."""
        with self.assertRaises(ValidationError):
            self.j['laboran'].group_ids = [(4, self.env.ref('base.group_system').id)]
        with self.assertRaises(ValidationError):
            self.j['laboran'].group_ids = [(4, self.env.ref('labfik_org.group_labfik_admin').id)]

    def test_sk_tidak_bisa_berlaku_tanpa_data_wajib(self):
        """TC-P3-06: SK butuh pengesah, file bertanda tangan, dan minimal satu penetapan."""
        sk = self.buat_sk([], berlakukan=False)
        with self.assertRaises(UserError) as err:
            sk.action_berlakukan()
        self.assertIn('file SK bertanda tangan', str(err.exception))
        self.assertIn('minimal satu personel', str(err.exception))

    def test_lampiran_sk_tersimpan_sekali_di_register(self):
        """TC-P3-01 / FR-A3 / FR-B8: file SK disimpan di register dokumen, bukan di rekaman SK."""
        sk = self.buat_sk([(self.p_kalab, self.j['kalab'])])
        self.assertEqual(sk.state, 'berlaku')
        versi = sk.lampiran_versi_id
        self.assertEqual(versi.dokumen_id.jenis, 'sk')
        self.assertEqual(versi.state, 'berlaku')
        Att = self.env['ir.attachment'].sudo()
        self.assertEqual(Att.search_count([('res_model', '=', 'labfik.sk'), ('res_id', '=', sk.id)]), 0)
        self.assertEqual(Att.search_count([('res_model', '=', 'labfik.dokumen.versi'), ('res_id', '=', versi.id),
                                           ('res_field', '=', 'file')]), 1)
        self.assertTrue(sk.lampiran_file)

    def test_sk_berlaku_terkunci(self):
        """FR-A3: SK berlaku tidak dapat diubah; penetapan hanya dapat diakhiri."""
        sk = self.buat_sk([(self.p_kalab, self.j['kalab'])])
        kalab = self.u_kalab
        with self.assertRaises(UserError):
            sk.with_user(kalab).write({'name': 'SK-UBAH'})
        with self.assertRaises(UserError):
            sk.with_user(kalab).write({'lampiran_file': self.pdf, 'lampiran_filename': 'baru.pdf'})
        with self.assertRaises(UserError):
            self.env['labfik.sk.line'].with_user(kalab).create(
                {'sk_id': sk.id, 'personel_id': self.p_laboran.id, 'jabatan_id': self.j['laboran'].id})
        with self.assertRaises(UserError):
            sk.line_ids.with_user(kalab).write({'jabatan_id': self.j['laboran'].id})
        with self.assertRaises(UserError):
            sk.with_user(kalab).unlink()
        # Mengakhiri penetapan diperbolehkan, juga lewat form SK (perintah one2many).
        sk.with_user(kalab).write({'line_ids': [(1, sk.line_ids.id, {'tanggal_selesai': self.today})]})
        self.assertEqual(sk.line_ids.tanggal_selesai, self.today)

    def test_tombol_akhiri_penetapan(self):
        """Tombol 'Akhiri hari ini' pada baris SK berlaku; hanya KaLab."""
        sk = self.buat_sk([(self.p_kalab, self.j['kalab']), (self.p_laboran, self.j['laboran'])])
        baris = sk.line_ids.filtered(lambda l: l.personel_id == self.p_laboran)
        with self.assertRaises(UserError):
            baris.with_user(self.u_laboran).action_akhiri()
        baris.with_user(self.u_kalab).action_akhiri()
        self.assertEqual(baris.tanggal_selesai, self.today)
        self.assertFalse(self.j['laboran']._pemangku_pada(self.today + relativedelta(days=1)).get(self.j['laboran'].id))
        draf = self.buat_sk([(self.p_dosen, self.j['dosen'])], berlakukan=False, nama='SK-DRAF')
        with self.assertRaises(UserError):
            draf.line_ids.action_akhiri()

    def test_hanya_kalab_bisa_memberlakukan_sk(self):
        sk = self.buat_sk([(self.p_kalab, self.j['kalab'])], berlakukan=False)
        sk.write({'lampiran_file': self.pdf, 'lampiran_filename': 'sk.pdf'})
        with self.assertRaises(UserError):
            sk.with_user(self.u_laboran).action_berlakukan()
        sk.with_user(self.u_kalab).action_berlakukan()
        self.assertEqual(sk.state, 'berlaku')

    def test_pemangku_dan_riwayat(self):
        """Riwayat SK menjawab 'siapa pemangku jabatan pada tanggal X'."""
        self.buat_sk([(self.p_kalab, self.j['kalab'])], mulai=self.periode.tanggal_mulai,
                     selesai=self.today - relativedelta(days=1), nama='SK-LAMA')
        self.buat_sk([(self.p_laboran, self.j['kalab'])], mulai=self.today, nama='SK-BARU')
        kemarin = self.today - relativedelta(days=1)
        self.assertEqual(self.j['kalab']._pemangku_pada(kemarin)[self.j['kalab'].id], self.p_kalab)
        self.assertEqual(self.j['kalab']._pemangku_pada(self.today)[self.j['kalab'].id], self.p_laboran)
        self.assertEqual(self.j['kalab'].pemangku_ids, self.p_laboran)

    def test_personel_nonaktif_mengakhiri_jabatan(self):
        """PRD §8.4: personel dinonaktifkan → jabatan aktifnya diakhiri hari ini."""
        sk = self.buat_sk([(self.p_laboran, self.j['laboran'])])
        self.p_laboran.active = False
        self.assertEqual(sk.line_ids.tanggal_selesai, self.today)
        with self.assertRaises(UserError):
            self.buat_sk([(self.p_laboran, self.j['laboran'])], berlakukan=False, nama='SK-2')

    def test_laporan_bagan_dan_matriks(self):
        """TC-P3-02 / TC-P3-04: bagan organisasi dan matriks kewenangan tercetak dari data jabatan."""
        sk = self.struktur_lengkap()
        R = self.env['ir.actions.report']
        bagan, _t = R._render_qweb_html('labfik_org.report_bagan_organisasi', sk.ids)
        bagan = bagan.decode()
        for teks in ('BAGAN ORGANISASI', 'Kepala Laboratorium', 'KaLab Uji', 'Laboran Uji', 'pengganti'):
            self.assertIn(teks, bagan)
        matriks, _t = R._render_qweb_html('labfik_org.report_matriks_kewenangan', sk.ids)
        matriks = matriks.decode()
        for teks in ('MATRIKS KEWENANGAN', 'Mendampingi praktikum', '✓', 'Tugas Petugas K3'):
            self.assertIn(teks, matriks)

    def test_rapat_dan_evaluasi_dalam_periode(self):
        """TC-P3-05: rapat dan evaluasi wajib berada di dalam periode; semester terisi otomatis."""
        rapat = self.env['labfik.rapat'].create({'name': 'Rapat uji', 'periode_id': self.periode.id,
                                                 'tanggal': self.today, 'peserta_ids': [(6, 0, self.p_kalab.ids)]})
        self.assertEqual(rapat.semester_id, self.ganjil)
        with self.assertRaises(ValidationError):
            self.env['labfik.rapat'].create({'name': 'Di luar', 'periode_id': self.periode.id,
                                             'tanggal': self.periode.tanggal_selesai + relativedelta(days=1)})
        with self.assertRaises(ValidationError):
            self.env['labfik.evaluasi.struktur'].create({
                'periode_id': self.periode.id, 'tanggal': self.periode.tanggal_mulai - relativedelta(days=1),
                'temuan': 'x', 'keputusan': 'y'})

    def test_impor_personel_csv(self):
        """FR-E4: personel dapat diimpor massal (mekanisme impor Odoo memakai load())."""
        hasil = self.env['labfik.personel'].load(
            ['name', 'jenis', 'nomor_induk', 'email'],
            [['Impor Satu', 'dosen', 'IMP-1', 'satu@contoh.test'],
             ['Impor Dua', 'mahasiswa', 'IMP-2', ''],
             ['Impor Tiga', 'tendik', 'IMP-3', '']])
        self.assertFalse(hasil['messages'], hasil['messages'])
        self.assertEqual(len(hasil['ids']), 3)
        self.assertEqual(self.env['labfik.personel'].browse(hasil['ids'][1]).jenis, 'mahasiswa')

    def test_buat_akun_login_personel(self):
        self.p_dosen.email = 'dosen@contoh.test'
        self.p_dosen.action_buat_akun()
        self.assertEqual(self.p_dosen.user_id.login, 'dosen@contoh.test')
        with self.assertRaises(UserError):
            self.p_dosen.action_buat_akun()
