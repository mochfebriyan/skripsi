# -*- coding: utf-8 -*-
"""Pengelolaan 2: siklus hidup dokumen (TC-P2-01 … TC-P2-07)."""
from dateutil.relativedelta import relativedelta
from psycopg2 import IntegrityError

from odoo.exceptions import UserError
from odoo.tests import tagged
from odoo.tools import mute_logger

from .common import LabfikCase


@tagged('post_install', '-at_install', 'labfik')
class TestDokumen(LabfikCase):

    def test_alur_draf_ajukan_sahkan(self):
        """TC-P2-03 / TC-P2-04 / US-08 / US-09: draf → diajukan → berlaku, beserta tanggal tinjau."""
        dok = self.buat_dokumen('DOK-1')
        versi = self.buat_versi(dok, sampai='draf')
        self.assertEqual((versi.state, versi.revisi), ('draf', '1.0'))
        versi.with_user(self.u_laboran).action_ajukan()
        self.assertEqual(versi.state, 'diajukan')
        versi.with_user(self.u_kalab).action_sahkan()
        self.assertEqual(versi.state, 'berlaku')
        self.assertEqual(versi.tanggal_sah, self.today)
        self.assertEqual(versi.tanggal_tinjau, self.today + relativedelta(months=12))
        self.assertEqual(versi.disahkan_oleh_id, self.u_kalab)
        self.assertEqual(dok.versi_berlaku_id, versi)

    def test_ajukan_butuh_file(self):
        versi = self.env['labfik.dokumen.versi'].create({'dokumen_id': self.buat_dokumen('DOK-2').id})
        with self.assertRaises(UserError):
            versi.action_ajukan()

    def test_versi_baru_mencabut_versi_lama(self):
        """FR-B3: hanya satu versi berlaku; mengesahkan revisi mencabut versi lama."""
        dok = self.buat_dokumen('DOK-3')
        v1 = self.buat_versi(dok)
        v2 = self.buat_versi(dok)
        self.assertEqual(v2.revisi, '2.0')
        self.assertEqual((v1.state, v2.state), ('dicabut', 'berlaku'))
        self.assertEqual(dok.versi_berlaku_id, v2)
        self.assertEqual(len(dok.versi_ids.filtered(lambda v: v.state == 'berlaku')), 1)

    def test_tolak_butuh_alasan_dan_kembali_ke_draf(self):
        """US-09: tolak tanpa alasan ditolak sistem; dengan alasan → kembali ke draf."""
        versi = self.buat_versi(self.buat_dokumen('DOK-4'), sampai='diajukan')
        aksi = versi.with_user(self.u_kalab).action_tolak()
        self.assertEqual(aksi['res_model'], 'labfik.tolak.wizard')
        with self.assertRaises(UserError):
            versi.with_user(self.u_kalab)._tolak('   ')
        wizard = self.env['labfik.tolak.wizard'].with_user(self.u_kalab).with_context(aksi['context']).create(
            {'alasan': 'Langkah 3 belum jelas'})
        wizard.action_tolak()
        self.assertEqual(versi.state, 'draf')
        self.assertEqual(versi.alasan_tolak, 'Langkah 3 belum jelas')

    def test_file_terkunci_setelah_diajukan(self):
        """US-09 / NFR-02: file versi yang diajukan atau berlaku tidak dapat diganti."""
        versi = self.buat_versi(self.buat_dokumen('DOK-5'), sampai='diajukan')
        with self.assertRaises(UserError):
            versi.with_user(self.u_laboran).write({'file': self.pdf})
        versi.with_user(self.u_kalab).action_sahkan()
        with self.assertRaises(UserError):
            versi.with_user(self.u_kalab).write({'file': self.pdf})
        with self.assertRaises(UserError):
            versi.with_user(self.u_kalab).write({'revisi': '9.9'})
        # Ringkasan boleh dikoreksi; file tetap.
        versi.with_user(self.u_laboran).write({'ringkasan': 'koreksi ketik'})

    def test_status_hanya_lewat_tombol(self):
        """Laboran tidak dapat melompati alur dengan menulis status langsung."""
        dok = self.buat_dokumen('DOK-6')
        Versi = self.env['labfik.dokumen.versi'].with_user(self.u_laboran)
        versi = Versi.create({'dokumen_id': dok.id, 'file': self.pdf, 'state': 'berlaku',
                              'tanggal_sah': self.today})
        self.assertEqual(versi.state, 'draf', 'status dari create diabaikan')
        self.assertFalse(versi.tanggal_sah)
        with self.assertRaises(UserError):
            versi.write({'state': 'berlaku'})

    def test_hanya_versi_draf_yang_bisa_dihapus(self):
        dok = self.buat_dokumen('DOK-7')
        draf = self.buat_versi(dok, sampai='draf')
        berlaku = self.buat_versi(dok)
        with self.assertRaises(UserError):
            berlaku.with_user(self.u_kalab).unlink()
        draf.with_user(self.u_kalab).sudo().unlink()

    def test_tinjau_ulang_tanpa_perubahan(self):
        """TC-P2-05: tinjau ulang memperpanjang tanggal tinjau satu siklus; hanya KaLab."""
        versi = self.buat_versi(self.buat_dokumen('DOK-8'))
        versi.write({'tanggal_tinjau': self.today - relativedelta(days=1)})
        self.assertTrue(versi.perlu_ditinjau)
        with self.assertRaises(UserError):
            versi.with_user(self.u_laboran).action_tinjau_tanpa_perubahan()
        with self.assertRaises(UserError):
            versi.with_user(self.u_laboran).write({'tanggal_tinjau': self.today})
        versi.with_user(self.u_kalab).action_tinjau_tanpa_perubahan()
        self.assertEqual(versi.tanggal_tinjau, self.today + relativedelta(months=12))
        self.assertFalse(versi.perlu_ditinjau)

    def test_siklus_tinjau_mengikuti_pengaturan(self):
        self.env['ir.config_parameter'].sudo().set_param('labfik.siklus_tinjau_bulan', '6')
        versi = self.buat_versi(self.buat_dokumen('DOK-9'))
        self.assertEqual(versi.tanggal_tinjau, self.today + relativedelta(months=6))

    def test_distribusi_dan_sosialisasi_hanya_versi_berlaku(self):
        """TC-P2-06 / TC-P2-07."""
        dok = self.buat_dokumen('DOK-10', self.r301 | self.r302)
        diajukan = self.buat_versi(dok, sampai='diajukan')
        with self.assertRaises(UserError):
            self.env['labfik.dokumen.distribusi'].create({'versi_id': diajukan.id, 'ruang_id': self.r301.id})
        with self.assertRaises(UserError):
            self.env['labfik.dokumen.sosialisasi'].create({'versi_id': diajukan.id})
        diajukan.action_sahkan()
        self.env['labfik.dokumen.distribusi'].with_user(self.u_laboran).create(
            {'versi_id': diajukan.id, 'ruang_id': self.r301.id})
        self.assertEqual(diajukan.lokasi_belum_ids, self.r302)

    def test_halaman_dokumen_berlaku_per_ruang(self):
        """US-11: asisten mencari dokumen berlaku untuk ruang tempat ia bertugas."""
        self.sop_memenuhi('DOK-11', self.r301)
        self.sop_memenuhi('DOK-12', self.r302)
        hasil = self.env['labfik.dokumen.versi'].with_user(self.u_pengguna).search(
            [('state', '=', 'berlaku'), ('ruang_ids', 'in', self.r301.ids)])
        self.assertEqual(hasil.mapped('kode'), ['DOK-11'])

    def test_daftar_wajib_terkunci(self):
        """US-07 / FR-B9: setelah dikunci, daftar SOP wajib periode tidak dapat diubah."""
        d1, d2 = self.buat_dokumen('DOK-13'), self.buat_dokumen('DOK-14')
        self.jadikan_wajib(d1)
        with self.assertRaises(UserError):
            self.periode.with_user(self.u_laboran).action_kunci_wajib()
        self.periode.with_user(self.u_kalab).action_kunci_wajib()
        self.assertTrue(self.periode.wajib_terkunci)
        Wajib = self.env['labfik.dokumen.wajib'].with_user(self.u_kalab)
        with self.assertRaises(UserError):
            Wajib.create({'periode_id': self.periode.id, 'dokumen_id': d2.id})
        with self.assertRaises(UserError):
            self.periode.wajib_ids.with_user(self.u_kalab).unlink()
        with self.assertRaises(UserError):
            self.periode.with_user(self.u_kalab).action_buka_kunci_wajib()

    def test_kunci_daftar_wajib_kosong_ditolak(self):
        with self.assertRaises(UserError):
            self.periode.action_kunci_wajib()

    def test_pengingat_tinjau_membuat_aktivitas(self):
        """US-12 / FR-B7: pemilik dokumen mendapat aktivitas menjelang tanggal tinjau, tanpa duplikat."""
        self.p_laboran.user_id = self.u_laboran2
        dok = self.buat_dokumen('DOK-15')
        dok.pemilik_id = self.p_laboran
        versi = self.buat_versi(dok)
        versi.write({'tanggal_tinjau': self.today + relativedelta(days=10)})
        jauh = self.buat_versi(self.buat_dokumen('DOK-16'))
        jauh.dokumen_id.pemilik_id = self.p_laboran
        Versi = self.env['labfik.dokumen.versi']
        Versi._cron_pengingat_tinjau()
        Versi._cron_pengingat_tinjau()
        aktivitas = versi.activity_ids.filtered(lambda a: a.user_id == self.u_laboran2)
        self.assertEqual(len(aktivitas), 1)
        self.assertEqual(aktivitas.date_deadline, versi.tanggal_tinjau)
        self.assertFalse(jauh.activity_ids, 'tanggal tinjau masih jauh, belum perlu pengingat')

    @mute_logger('odoo.sql_db')
    def test_kode_dokumen_unik(self):
        self.buat_dokumen('DOK-17')
        with self.assertRaises(IntegrityError), self.cr.savepoint():
            self.buat_dokumen('DOK-17')
