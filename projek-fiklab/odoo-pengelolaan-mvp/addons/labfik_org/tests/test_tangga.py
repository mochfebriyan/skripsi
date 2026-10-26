# -*- coding: utf-8 -*-
"""Tangga kriteria berurutan Pengelolaan 1 dan 3: dataset D-3 (TC-P1-06 … 09, TC-P3-06 … 09)."""
from dateutil.relativedelta import relativedelta

from odoo.tests import tagged

from .common import LabfikCase


def ringkas(hasil):
    return {k['kode']: (k['lengkap'], k['dihitung']) for k in hasil['kriteria']}


@tagged('post_install', '-at_install', 'labfik')
class TestTanggaP1(LabfikCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.buat_kpi_renstra()
        cls.K = cls.env['labfik.kepatuhan']

    def test_belum_ada_rencana(self):
        h = self.K.hitung_p1(self.periode, self.today)
        self.assertIsNone(h['tertinggi'])
        self.assertEqual(ringkas(h)['K1'], (False, True))

    def test_rencana_draf_atau_tanpa_pdf_tidak_memenuhi_k1(self):
        self.buat_rencana(sahkan=False)
        self.assertIsNone(self.K.hitung_p1(self.periode, self.today)['tertinggi'])

    def test_d3a_item_tanpa_pic(self):
        """D-3a: rencana disahkan, 1 dari 5 item tanpa PIC → kriteria tertinggi K1."""
        rencana = self.buat_rencana(jumlah_item=5)
        rencana.item_ids[2].with_context(labfik_internal=True).write({'pic_id': False})
        h = self.K.hitung_p1(self.periode, self.today)
        self.assertEqual(h['tertinggi'], 'K1')
        self.assertEqual(ringkas(h)['K2'], (False, True))
        self.assertIn('item 3: PIC', h['kriteria'][1]['keterangan'][0])

    def test_d3b_realisasi_ganjil_tanpa_tinjauan(self):
        """D-3b: item lengkap; realisasi semester Ganjil berbukti untuk 5 item; belum ada tinjauan → K3."""
        rencana = self.buat_rencana(jumlah_item=5)
        for item in rencana.item_ids:
            self.realisasi(item, self.ganjil)
        h = self.K.hitung_p1(self.periode, self.today)
        self.assertEqual(h['tertinggi'], 'K3')
        self.assertEqual(ringkas(h)['K4'], (False, True))

    def test_realisasi_tanpa_bukti_tidak_dihitung(self):
        rencana = self.buat_rencana(jumlah_item=2)
        self.realisasi(rencana.item_ids[0], self.ganjil)
        self.realisasi(rencana.item_ids[1], self.ganjil, bukti=False)
        self.assertEqual(self.K.hitung_p1(self.periode, self.today)['tertinggi'], 'K2')

    def test_k3_mengikuti_semester_berjalan(self):
        """Begitu Genap dimulai, setiap item juga butuh realisasi Genap."""
        rencana = self.buat_rencana(jumlah_item=1)
        self.realisasi(rencana.item_ids[0], self.ganjil)
        tgl_genap = self.genap.tanggal_mulai + relativedelta(days=1)
        self.assertEqual(self.K.hitung_p1(self.periode, tgl_genap)['tertinggi'], 'K2')
        self.realisasi(rencana.item_ids[0], self.genap, tanggal=self.genap.tanggal_mulai)
        self.assertEqual(self.K.hitung_p1(self.periode, tgl_genap)['tertinggi'], 'K3')

    def test_ambang_k3_dari_pengaturan(self):
        rencana = self.buat_rencana(jumlah_item=1)
        self.realisasi(rencana.item_ids[0], self.ganjil)
        self.env['ir.config_parameter'].sudo().set_param('labfik.p1_k3_min_realisasi', '2')
        self.assertEqual(self.K.hitung_p1(self.periode, self.today)['tertinggi'], 'K2')

    def test_k4_tinjauan_dan_tindak_lanjut(self):
        """K4: tinjauan ada DAN minimal satu keputusan tertaut ke item rencana periode berikutnya."""
        rencana = self.buat_rencana(jumlah_item=1)
        self.realisasi(rencana.item_ids[0], self.ganjil)
        tinjauan = self.env['labfik.rencana.tinjauan'].create({'rencana_id': rencana.id, 'ringkasan': 'Capaian'})
        keputusan = self.env['labfik.rencana.tinjauan.keputusan'].create(
            {'tinjauan_id': tinjauan.id, 'uraian': 'Tambah pelatihan'})
        self.assertEqual(self.K.hitung_p1(self.periode, self.today)['tertinggi'], 'K3')
        berikut = self.env['labfik.periode'].create({
            'name': 'UJI-BERIKUT', 'tanggal_mulai': self.periode.tanggal_selesai + relativedelta(days=1),
            'tanggal_selesai': self.periode.tanggal_selesai + relativedelta(years=1)})
        rencana_berikut = self.buat_rencana(jumlah_item=1, sahkan=False, periode=berikut)
        keputusan.item_berikut_id = rencana_berikut.item_ids[0]
        h = self.K.hitung_p1(self.periode, self.today)
        self.assertEqual(h['tertinggi'], 'K4')
        self.assertTrue(all(k['lengkap'] and k['dihitung'] for k in h['kriteria']))


@tagged('post_install', '-at_install', 'labfik')
class TestTanggaP3(LabfikCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.K = cls.env['labfik.kepatuhan']

    def rapat(self, tanggal):
        return self.env['labfik.rapat'].create({'name': 'Koordinasi', 'periode_id': self.periode.id,
                                                'tanggal': tanggal})

    def evaluasi(self):
        return self.env['labfik.evaluasi.struktur'].create({'periode_id': self.periode.id, 'tanggal': self.today,
                                                            'temuan': 'Beban laboran timpang',
                                                            'keputusan': 'Bagi ulang ruang'})

    def test_belum_ada_sk(self):
        self.assertIsNone(self.K.hitung_p3(self.periode, self.today)['tertinggi'])

    def test_d3c_jabatan_tanpa_pemangku_dan_tangga_berurutan(self):
        """D-3c: SK berlaku; Petugas K3 tanpa pemangku; ada evaluasi → tertinggi K1, K4 tidak dihitung."""
        self.lengkapi_jabatan()
        self.buat_sk([(self.p_kalab, self.j['kalab']), (self.p_laboran, self.j['laboran']),
                      (self.p_dosen, self.j['dosen']), (self.p_asisten, self.j['asisten'])])
        self.rapat(self.today)
        self.evaluasi()
        h = self.K.hitung_p3(self.periode, self.today)
        self.assertEqual(h['tertinggi'], 'K1')
        r = ringkas(h)
        self.assertEqual(r['K2'], (False, True))
        self.assertEqual(r['K4'], (True, False), 'data K4 ada, tetapi tidak dihitung karena K2 belum lengkap')
        self.assertIn('Petugas K3: pemangku', h['kriteria'][1]['keterangan'])

    def test_d3d_struktur_lengkap(self):
        """D-3d: Petugas K3 diisi; 1 rapat per semester berjalan; evaluasi ada → K4."""
        self.struktur_lengkap()
        h = self.K.hitung_p3(self.periode, self.today)
        self.assertEqual(h['tertinggi'], 'K2', 'belum ada rapat')
        self.rapat(self.today)
        self.assertEqual(self.K.hitung_p3(self.periode, self.today)['tertinggi'], 'K3')
        self.evaluasi()
        self.assertEqual(self.K.hitung_p3(self.periode, self.today)['tertinggi'], 'K4')

    def test_k2_butuh_uraian_kewenangan_pengganti(self):
        self.struktur_lengkap()
        self.j['dosen'].write({'uraian_tugas': False, 'kewenangan_ids': [(5,)], 'pengganti_id': False})
        h = self.K.hitung_p3(self.periode, self.today)
        self.assertEqual(h['tertinggi'], 'K1')
        teks = ' '.join(h['kriteria'][1]['keterangan'])
        for kata in ('uraian tugas', 'kewenangan', 'pengganti'):
            self.assertIn(kata, teks)

    def test_k3_butuh_rapat_setiap_semester_berjalan(self):
        self.struktur_lengkap()
        self.rapat(self.today)
        tgl_genap = self.genap.tanggal_mulai + relativedelta(days=2)
        self.assertEqual(self.K.hitung_p3(self.periode, tgl_genap)['tertinggi'], 'K2')
        self.rapat(self.genap.tanggal_mulai + relativedelta(days=1))
        self.assertEqual(self.K.hitung_p3(self.periode, tgl_genap)['tertinggi'], 'K3')

    def test_sk_tanpa_penetapan_aktif_tidak_memenuhi_k1(self):
        self.lengkapi_jabatan()
        sk = self.buat_sk([(self.p_kalab, self.j['kalab'])])
        sk.line_ids.write({'tanggal_selesai': self.today - relativedelta(days=1)})
        self.assertIsNone(self.K.hitung_p3(self.periode, self.today)['tertinggi'])

    def test_status_html_menampilkan_label_lengkap_secara_data(self):
        self.struktur_lengkap()
        self.env['labfik.kepatuhan'].siapkan_untuk_periode(self.periode)
        status = self.periode.kepatuhan_ids.filtered(lambda k: k.indikator == 'p3')
        self.assertEqual(status.kriteria_tertinggi, 'K2')
        self.assertIn('Lengkap secara data', status.detail_html)
        self.assertIn('Skor akhir ditetapkan penilai', status.ringkasan)
        self.assertEqual(status.skor_sistem, 0)
