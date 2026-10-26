# -*- coding: utf-8 -*-
"""Umum: checklist mulai (FR-E1), periode (FR-E5), pengaturan (FR-E7), menu dan tampilan."""
from datetime import date

from odoo.exceptions import ValidationError
from odoo.tests import tagged

from .common import LabfikCase


@tagged('post_install', '-at_install', 'labfik')
class TestUmum(LabfikCase):

    def test_semester_dibuat_otomatis(self):
        """FR-E5: periode akademik 1 Sep–31 Agu → Ganjil s.d. 31 Jan, Genap mulai 1 Feb."""
        p = self.env['labfik.periode'].create({'name': '2030/2031', 'tanggal_mulai': date(2030, 9, 1),
                                               'tanggal_selesai': date(2031, 8, 31)})
        ganjil, genap = p.semester_ids.sorted('tanggal_mulai')
        self.assertEqual((ganjil.name, ganjil.tanggal_selesai), ('ganjil', date(2031, 1, 31)))
        self.assertEqual((genap.name, genap.tanggal_mulai), ('genap', date(2031, 2, 1)))
        self.assertEqual(genap.display_name, 'Genap 2030/2031')

    def test_semester_tumpang_tindih_ditolak(self):
        with self.assertRaises(ValidationError):
            self.ganjil.tanggal_selesai = self.genap.tanggal_mulai

    def test_checklist_mengikuti_data(self):
        """US-01 / FR-E1: setiap langkah checklist berubah menjadi selesai saat datanya ada."""
        cek = self.env['labfik.checklist.mulai'].create({})
        self.assertTrue(cek.langkah_periode)
        self.assertFalse(cek.langkah_jabatan, 'jabatan standar belum dilengkapi')
        self.assertTrue(cek.langkah_personel)
        self.assertFalse(cek.langkah_sk)
        self.assertFalse(cek.langkah_wajib)
        self.assertFalse(cek.langkah_rencana)
        self.struktur_lengkap()
        dok, _v = self.sop_memenuhi('CEK-1')
        self.jadikan_wajib(dok)
        self.buat_kpi_renstra()
        self.buat_rencana(jumlah_item=1)
        cek.invalidate_recordset()
        self.assertTrue(all([cek.langkah_periode, cek.langkah_jabatan, cek.langkah_personel,
                             cek.langkah_sk, cek.langkah_wajib, cek.langkah_rencana]))
        self.assertEqual(cek.progres, 100)
        for aksi in ('action_periode', 'action_jabatan', 'action_personel', 'action_sk', 'action_wajib',
                     'action_rencana'):
            self.assertEqual(getattr(cek, aksi)()['type'], 'ir.actions.act_window')

    def test_menu_checklist_membuka_rekaman_tersimpan(self):
        """Regresi: form checklist harus membuka rekaman tersimpan agar progres terhitung (bukan 0%)."""
        self.struktur_lengkap()
        aksi = self.env.ref('labfik_org.action_server_checklist').with_user(self.u_kalab).run()
        self.assertEqual(aksi['res_model'], 'labfik.checklist.mulai')
        self.assertTrue(aksi['res_id'])
        cek = self.env['labfik.checklist.mulai'].browse(aksi['res_id'])
        self.assertTrue(cek.langkah_sk)
        self.assertGreater(cek.progres, 0)

    def test_pengaturan_ambang(self):
        """FR-E7: ambang disimpan sebagai parameter dan dibaca mesin skor."""
        settings = self.env['res.config.settings'].create({'labfik_siklus_tinjau_bulan': 24,
                                                          'labfik_p3_k3_min_rapat': 2})
        settings.execute()
        ICP = self.env['ir.config_parameter'].sudo()
        self.assertEqual(ICP.get_param('labfik.siklus_tinjau_bulan'), '24')
        self.assertEqual(ICP.get_param('labfik.p3_k3_min_rapat'), '2')

    def test_buka_status_periode_menyiapkan_tiga_indikator(self):
        aksi = self.periode.action_buka_status()
        self.assertEqual(aksi['res_model'], 'labfik.kepatuhan')
        self.assertEqual(sorted(self.periode.kepatuhan_ids.mapped('indikator')), ['p1', 'p2', 'p3'])
        self.periode.action_buka_status()
        self.assertEqual(len(self.periode.kepatuhan_ids), 3, 'tidak membuat duplikat')

    def test_semua_tampilan_dapat_dimuat_per_peran(self):
        """Setiap tampilan dan menu dapat dimuat oleh peran yang berhak (menangkap galat field/view)."""
        model_peran = {
            self.u_pengguna: ['labfik.dokumen.versi', 'labfik.personel', 'labfik.jabatan', 'labfik.sk',
                              'labfik.rapat'],
            self.u_laboran: ['labfik.dokumen', 'labfik.dokumen.versi', 'labfik.rencana', 'labfik.rencana.realisasi',
                             'labfik.rencana.tinjauan', 'labfik.kepatuhan', 'labfik.evaluasi.struktur',
                             'labfik.dokumen.distribusi', 'labfik.dokumen.sosialisasi'],
            self.u_kalab: ['labfik.periode', 'labfik.ruang', 'labfik.kpi', 'labfik.renstra.sasaran',
                           'labfik.kewenangan', 'labfik.checklist.mulai', 'labfik.tolak.wizard', 'labfik.sk',
                           'labfik.personel', 'labfik.jabatan', 'labfik.rencana'],
            self.u_penilai: ['labfik.kepatuhan', 'labfik.dokumen.versi', 'labfik.rencana'],
        }
        for user, models in model_peran.items():
            for model in models:
                tipe = [(False, 'form')]
                if model not in ('labfik.checklist.mulai', 'labfik.tolak.wizard'):
                    tipe.append((False, 'tree'))
                hasil = self.env[model].with_user(user).get_views(tipe)
                self.assertTrue(hasil['views'], '%s / %s' % (user.login, model))
        menu = self.env['ir.ui.menu'].with_user(self.u_pengguna).load_menus(False)
        nama = {m['name'] for m in menu.values() if isinstance(m, dict) and m.get('name')}
        self.assertIn('Dokumen berlaku', nama)
        self.assertNotIn('Konfigurasi', nama)
        menu_kalab = self.env['ir.ui.menu'].with_user(self.u_kalab).load_menus(False)
        self.assertIn('Konfigurasi', {m['name'] for m in menu_kalab.values() if isinstance(m, dict) and m.get('name')})
