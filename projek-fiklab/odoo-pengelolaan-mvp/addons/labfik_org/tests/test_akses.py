# -*- coding: utf-8 -*-
"""Hak akses (TC-AKS, PRD Lampiran B dan D-4)."""
from dateutil.relativedelta import relativedelta

from odoo.exceptions import AccessError, UserError
from odoo.tests import tagged, new_test_user

from .common import LabfikCase


@tagged('post_install', '-at_install', 'labfik')
class TestAkses(LabfikCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.g_kalab = cls.env.ref('labfik_org.group_labfik_kalab')
        cls.g_laboran = cls.env.ref('labfik_org.group_labfik_laboran')
        cls.g_pengguna = cls.env.ref('labfik_org.group_labfik_pengguna')
        cls.g_penilai = cls.env.ref('labfik_org.group_labfik_penilai')
        cls.g_admin = cls.env.ref('labfik_org.group_labfik_admin')
        cls.u_a = new_test_user(cls.env, login='t_akses_a', groups='base.group_user')
        cls.u_b = new_test_user(cls.env, login='t_akses_b', groups='base.group_user')
        cls.p_a = cls.env['labfik.personel'].create({'name': 'Personel A', 'user_id': cls.u_a.id})
        cls.p_b = cls.env['labfik.personel'].create({'name': 'Personel B', 'user_id': cls.u_b.id})

    def grup(self, user):
        user.invalidate_recordset(['groups_id'])
        return user.groups_id

    # ---------------------------------------------------------------- sinkronisasi jabatan → grup
    def test_sk_berlaku_memberi_grup_jabatan(self):
        """US-04: SK disahkan → pemangku masuk grup jabatannya (beserta grup turunan)."""
        self.assertNotIn(self.g_kalab, self.grup(self.u_a))
        sk = self.buat_sk([(self.p_a, self.j['kalab'])], berlakukan=False)
        self.assertNotIn(self.g_kalab, self.grup(self.u_a), 'SK draf belum memberi akses')
        sk.write({'lampiran_file': self.pdf, 'lampiran_filename': 'sk.pdf'})
        sk.action_berlakukan()
        g = self.grup(self.u_a)
        self.assertIn(self.g_kalab, g)
        self.assertIn(self.g_laboran, g)
        self.assertIn(self.g_pengguna, g)
        self.assertTrue(self.u_a.has_group('labfik_org.group_labfik_kalab'))

    def test_periode_jabatan_berakhir_mencabut_grup(self):
        """US-04 / D-4: periode jabatan berakhir → grup dicabut setelah sinkronisasi."""
        sk = self.buat_sk([(self.p_a, self.j['kalab'])])
        self.assertIn(self.g_kalab, self.grup(self.u_a))
        sk.line_ids.write({'tanggal_selesai': self.today - relativedelta(days=1)})
        g = self.grup(self.u_a)
        self.assertNotIn(self.g_kalab, g)
        self.assertNotIn(self.g_laboran, g)
        self.assertNotIn(self.g_pengguna, g)

    def test_cron_mencabut_grup_saat_sk_kedaluwarsa(self):
        """Cron harian menyamakan grup ketika masa berlaku SK lewat tanpa ada perubahan data."""
        sk = self.buat_sk([(self.p_a, self.j['laboran'])])
        self.assertIn(self.g_laboran, self.grup(self.u_a))
        # Simulasikan SK yang sudah kedaluwarsa (langsung di basis data, tanpa memicu sinkronisasi).
        self.env.cr.execute('UPDATE labfik_sk SET tanggal_selesai = %s WHERE id = %s',
                            (self.today - relativedelta(days=1), sk.id))
        sk.invalidate_recordset()
        self.assertIn(self.g_laboran, self.grup(self.u_a))
        self.env['labfik.personel']._cron_sinkron_akses()
        self.assertNotIn(self.g_laboran, self.grup(self.u_a))

    def test_cron_memulihkan_grup_yang_dihapus_manual(self):
        self.buat_sk([(self.p_a, self.j['laboran'])])
        self.u_a.write({'groups_id': [(3, self.g_laboran.id)]})
        self.assertNotIn(self.g_laboran, self.grup(self.u_a))
        self.env['labfik.personel']._cron_sinkron_akses()
        self.assertIn(self.g_laboran, self.grup(self.u_a))

    def test_dua_jabatan_mendapat_gabungan_grup(self):
        """D-4: personel B memegang Laboran dan Petugas K3 → gabungan grup keduanya."""
        self.buat_sk([(self.p_b, self.j['laboran']), (self.p_b, self.j['k3'])])
        g = self.grup(self.u_b)
        self.assertIn(self.g_laboran, g)
        self.assertIn(self.g_pengguna, g)
        self.assertNotIn(self.g_kalab, g)

    def test_cabut_sk_mencabut_grup(self):
        sk = self.buat_sk([(self.p_a, self.j['kalab'])])
        sk.with_user(self.u_kalab).action_cabut()
        self.assertEqual(sk.state, 'dicabut')
        self.assertNotIn(self.g_kalab, self.grup(self.u_a))

    def test_grup_manual_tidak_disentuh(self):
        """PRD §8.4: grup di luar pemetaan jabatan (Penilai, Admin LabFIK) tetap utuh."""
        self.u_a.write({'groups_id': [(4, self.g_penilai.id)]})
        self.u_b.write({'groups_id': [(4, self.g_admin.id)]})
        sk = self.buat_sk([(self.p_a, self.j['asisten']), (self.p_b, self.j['asisten'])])
        sk.action_cabut()
        ga, gb = self.grup(self.u_a), self.grup(self.u_b)
        self.assertIn(self.g_penilai, ga)
        self.assertIn(self.g_pengguna, ga, 'tetap ada karena diwarisi dari Penilai')
        self.assertIn(self.g_admin, gb)
        self.assertIn(self.g_kalab, gb, 'tetap ada karena diwarisi dari Admin LabFIK')

    def test_akun_dilepas_dari_personel_dicabut_grupnya(self):
        self.buat_sk([(self.p_a, self.j['laboran'])])
        self.assertIn(self.g_laboran, self.grup(self.u_a))
        self.p_a.user_id = False
        self.assertNotIn(self.g_laboran, self.grup(self.u_a))

    def test_pemetaan_grup_jabatan_berubah(self):
        self.buat_sk([(self.p_a, self.j['k3'])])
        self.assertNotIn(self.g_laboran, self.grup(self.u_a))
        self.j['k3'].group_ids = [(6, 0, self.g_laboran.ids)]
        self.assertIn(self.g_laboran, self.grup(self.u_a))

    # ---------------------------------------------------------------- hak akses per peran
    def test_laboran_tidak_bisa_mengesahkan(self):
        """D-4: laboran mencoba mengesahkan SOP → ditolak."""
        versi = self.buat_versi(self.buat_dokumen('AKS-1'), sampai='diajukan')
        with self.assertRaises(UserError):
            versi.with_user(self.u_laboran).action_sahkan()
        with self.assertRaises(UserError):
            versi.with_user(self.u_laboran)._tolak('alasan')
        rencana = self.env['labfik.rencana'].create({'name': 'R', 'periode_id': self.periode.id})
        with self.assertRaises(UserError):
            rencana.with_user(self.u_laboran).action_sahkan()

    def test_tombol_sahkan_tersembunyi_untuk_laboran(self):
        """D-4: tombol Sahkan/Tolak tidak dikirim ke tampilan pengguna tanpa grup KaLab."""
        Versi = self.env['labfik.dokumen.versi']
        arch_laboran = Versi.with_user(self.u_laboran).get_views([(False, 'form')])['views']['form']['arch']
        arch_kalab = Versi.with_user(self.u_kalab).get_views([(False, 'form')])['views']['form']['arch']
        self.assertNotIn('action_sahkan', arch_laboran)
        self.assertNotIn('action_tolak', arch_laboran)
        self.assertIn('action_ajukan', arch_laboran)
        self.assertIn('action_sahkan', arch_kalab)

    def test_pengguna_hanya_melihat_versi_berlaku(self):
        """Lampiran B: pengguna lab hanya membaca versi berlaku."""
        dok = self.buat_dokumen('AKS-2')
        berlaku = self.buat_versi(dok)
        draf = self.buat_versi(dok, sampai='draf')
        terlihat = self.env['labfik.dokumen.versi'].with_user(self.u_pengguna).search([('dokumen_id', '=', dok.id)])
        self.assertEqual(terlihat, berlaku)
        with self.assertRaises(AccessError):
            draf.with_user(self.u_pengguna).read(['revisi'])
        semua = self.env['labfik.dokumen.versi'].with_user(self.u_penilai).search([('dokumen_id', '=', dok.id)])
        self.assertEqual(len(semua), 2, 'penilai membaca semua versi')

    def test_pengguna_tidak_melihat_pdf_sk_dan_rencana_di_register(self):
        """Privasi: register juga menyimpan PDF SK dan rencana kerja; pengguna lab hanya melihat SOP/IK/formulir."""
        sk = self.buat_sk([(self.p_kalab, self.j['kalab'])])
        self.buat_kpi_renstra()
        rencana = self.buat_rencana(jumlah_item=1)
        sop, _v = self.sop_memenuhi('AKS-SOP')
        Versi = self.env['labfik.dokumen.versi']
        terlihat = Versi.with_user(self.u_pengguna).search([])
        self.assertIn(sop.versi_berlaku_id, terlihat)
        self.assertNotIn(sk.lampiran_versi_id, terlihat)
        self.assertNotIn(rencana.lampiran_versi_id, terlihat)
        self.assertIn(rencana.lampiran_versi_id, Versi.with_user(self.u_laboran).search([]))

    def test_pengguna_tidak_bisa_mengubah_dokumen(self):
        dok = self.buat_dokumen('AKS-3')
        with self.assertRaises(AccessError):
            dok.with_user(self.u_pengguna).write({'name': 'ubah'})
        with self.assertRaises(AccessError):
            self.env['labfik.rencana'].with_user(self.u_pengguna).search([])

    def test_nomor_induk_tersembunyi_selain_kalab(self):
        """NFR-03: NIP/NIM hanya terlihat KaLab dan Admin."""
        with self.assertRaises(AccessError):
            self.p_kalab.with_user(self.u_laboran).read(['nomor_induk'])
        data = self.p_kalab.with_user(self.u_kalab).read(['nomor_induk'])
        self.assertEqual(data[0]['nomor_induk'], 'U-001')

    def test_laboran_hanya_mengubah_realisasi_item_yang_ia_pic(self):
        self.buat_kpi_renstra()
        # Akun laboran ditautkan ke personel yang memang menjabat Laboran (agar sinkronisasi mempertahankan grupnya).
        self.buat_sk([(self.p_laboran, self.j['laboran'])])
        self.p_laboran.user_id = self.u_laboran
        self.assertTrue(self.u_laboran.has_group('labfik_org.group_labfik_laboran'))
        rencana = self.buat_rencana(jumlah_item=2)
        item_milik, item_lain = rencana.item_ids
        item_lain.with_context(labfik_internal=True).write({'pic_id': self.p_kalab.id})
        Real = self.env['labfik.rencana.realisasi'].with_user(self.u_laboran)
        Real.create({'item_id': item_milik.id, 'semester_id': self.ganjil.id, 'capaian': 'ok'})
        with self.assertRaises(AccessError):
            Real.create({'item_id': item_lain.id, 'semester_id': self.ganjil.id, 'capaian': 'ok'})
        lain = self.realisasi(item_lain, self.ganjil)
        self.assertEqual(Real.search([('item_id', '=', item_lain.id)]), lain.with_user(self.u_laboran),
                         'laboran tetap dapat membaca realisasi item lain')

    def test_hanya_penilai_mengisi_skor_akhir(self):
        self.env['labfik.kepatuhan'].siapkan_untuk_periode(self.periode)
        status = self.env['labfik.kepatuhan'].search([('periode_id', '=', self.periode.id), ('indikator', '=', 'p1')])
        with self.assertRaises(UserError):
            status.with_user(self.u_kalab).write({'skor_penilai': '3'})
        status.with_user(self.u_penilai).write({'skor_penilai': '3', 'catatan_penilai': 'cukup'})
        self.assertEqual(status.skor_penilai, '3')
