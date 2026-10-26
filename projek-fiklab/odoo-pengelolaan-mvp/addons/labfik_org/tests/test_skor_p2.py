# -*- coding: utf-8 -*-
"""Pengelolaan 2: skor persentase, dataset skenario D-1 dan D-2 (TC-P2-08), status dan snapshot."""
from dateutil.relativedelta import relativedelta

from odoo.tests import tagged

from ..models.common import skor_dari_persen
from .common import LabfikCase


@tagged('post_install', '-at_install', 'labfik')
class TestSkorP2(LabfikCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.tgl = cls.today + relativedelta(days=30)   # tanggal penilaian

    def hitung(self):
        return self.env['labfik.kepatuhan'].hitung_p2(self.periode, self.tgl)

    def buat_d1(self):
        """D-1: 10 SOP wajib, 6 memenuhi, 4 gagal masing-masing di S2, S3, S4, S5."""
        dokumen = {}
        for n in range(1, 7):
            dokumen[n], _v = self.sop_memenuhi('SOP-%02d' % n, self.r301 | self.portal)
        # SOP-07: versi masih diajukan → S2
        dokumen[7] = self.buat_dokumen('SOP-07')
        self.v07 = self.buat_versi(dokumen[7], sampai='diajukan')
        # SOP-08: lewat tanggal tinjau → S3
        dokumen[8], v08 = self.sop_memenuhi('SOP-08')
        v08.write({'tanggal_tinjau': self.tgl - relativedelta(days=20)})
        # SOP-09: lokasi 301 dan 302, hanya terdistribusi ke 301 → S4
        dokumen[9] = self.buat_dokumen('SOP-09', self.r301 | self.r302)
        self.v09 = self.buat_versi(dokumen[9])
        self.env['labfik.dokumen.distribusi'].create({'versi_id': self.v09.id, 'ruang_id': self.r301.id})
        self.env['labfik.dokumen.sosialisasi'].create({'versi_id': self.v09.id})
        # SOP-10: belum disosialisasikan → S5
        dokumen[10] = self.buat_dokumen('SOP-10')
        self.v10 = self.buat_versi(dokumen[10])
        self.env['labfik.dokumen.distribusi'].create({'versi_id': self.v10.id, 'ruang_id': self.r301.id})
        self.jadikan_wajib(self.env['labfik.dokumen'].concat(*dokumen.values()))
        return dokumen

    def test_ambang_skor(self):
        """Ambang instrumen: 100 → 4, 90–<100 → 3, 70–<90 → 2, <70 → 1, N/A → 0."""
        for persen, skor in ((100, 4), (99.9, 3), (90, 3), (89.9, 2), (70, 2), (69.9, 1), (0, 1), (None, 0)):
            self.assertEqual(skor_dari_persen(persen), skor, persen)

    def test_d1_kondisi_campuran(self):
        """D-1 / US-18: 6/10 = 60% → skor 1, dengan cek yang gagal per SOP."""
        self.buat_d1()
        h = self.hitung()
        self.assertEqual((h['total'], h['memenuhi'], h['persen'], h['skor']), (10, 6, 60.0, 1))
        gagal = {b['kode']: b['gagal'] for b in h['baris'] if b['gagal']}
        self.assertEqual(gagal, {'SOP-07': ['S2'], 'SOP-08': ['S3'], 'SOP-09': ['S4'], 'SOP-10': ['S5']})

    def test_d2_setelah_perbaikan(self):
        """D-2: SOP-07 disahkan, SOP-09 didistribusikan ke 302, SOP-10 disosialisasikan → 9/10 = 90% → skor 3."""
        self.buat_d1()
        self.v07.with_user(self.u_kalab).action_sahkan()
        for r in self.v07.dokumen_id.ruang_ids:
            self.env['labfik.dokumen.distribusi'].create({'versi_id': self.v07.id, 'ruang_id': r.id})
        self.env['labfik.dokumen.sosialisasi'].create({'versi_id': self.v07.id})
        self.env['labfik.dokumen.distribusi'].create({'versi_id': self.v09.id, 'ruang_id': self.r302.id})
        self.env['labfik.dokumen.sosialisasi'].create({'versi_id': self.v10.id})
        h = self.hitung()
        self.assertEqual((h['memenuhi'], h['persen'], h['skor']), (9, 90.0, 3))

    def test_tanpa_sop_wajib_na(self):
        """Penyebut 0 → N/A, bukan 100%."""
        h = self.hitung()
        self.assertEqual((h['total'], h['persen'], h['skor']), (0, None, 0))

    def test_semua_memenuhi_skor_4(self):
        dok = self.env['labfik.dokumen'].concat(*[self.sop_memenuhi('ALL-%s' % n)[0] for n in range(3)])
        self.jadikan_wajib(dok)
        h = self.hitung()
        self.assertEqual((h['persen'], h['skor']), (100.0, 4))

    def test_tanpa_lokasi_penggunaan_gagal_s4(self):
        dok = self.buat_dokumen('NOLOK')
        dok.ruang_ids = [(5,)]
        versi = self.buat_versi(dok)
        self.env['labfik.dokumen.sosialisasi'].create({'versi_id': versi.id})
        self.jadikan_wajib(dok)
        self.assertEqual(self.hitung()['baris'][0]['gagal'], ['S4'])

    def test_versi_disahkan_setelah_tanggal_penilaian_tidak_dihitung(self):
        dok, _v = self.sop_memenuhi('LATE')
        self.jadikan_wajib(dok)
        h = self.env['labfik.kepatuhan'].hitung_p2(self.periode, self.today - relativedelta(days=1))
        self.assertEqual(h['baris'][0]['gagal'], ['S2'])

    def test_status_kepatuhan_dan_snapshot(self):
        """FR-D1 / FR-D3 / FR-D4: rekaman status menampilkan skor; snapshot membekukan hasil."""
        self.buat_d1()
        self.env['labfik.kepatuhan'].siapkan_untuk_periode(self.periode)
        status = self.env['labfik.kepatuhan'].search([('periode_id', '=', self.periode.id), ('indikator', '=', 'p2')])
        self.assertEqual(len(self.periode.kepatuhan_ids), 3)
        status.tanggal_penilaian = self.tgl
        self.assertEqual((status.skor_sistem, status.persen), (1, 60.0))
        self.assertIn('6 dari 10', status.ringkasan)
        self.assertIn('SOP-07', status.detail_html)
        status.with_user(self.u_kalab).action_snapshot()
        snap = status.snapshot_ids
        self.assertEqual((len(snap), snap.skor_sistem, snap.persen), (1, 1, 60.0))
        # Data berubah setelah snapshot → status berubah, snapshot tetap.
        self.v07.with_user(self.u_kalab).action_sahkan()
        for r in self.v07.dokumen_id.ruang_ids:
            self.env['labfik.dokumen.distribusi'].create({'versi_id': self.v07.id, 'ruang_id': r.id})
        self.env['labfik.dokumen.sosialisasi'].create({'versi_id': self.v07.id})
        status.invalidate_recordset()
        self.assertEqual(status.persen, 70.0)
        self.assertEqual(snap.persen, 60.0)
        with self.assertRaises(Exception):
            snap.with_user(self.u_kalab).write({'persen': 99})

    def test_snapshot_hanya_kalab_atau_penilai(self):
        self.env['labfik.kepatuhan'].siapkan_untuk_periode(self.periode)
        status = self.periode.kepatuhan_ids[:1]
        with self.assertRaises(Exception):
            status.with_user(self.u_laboran).action_snapshot()
        status.with_user(self.u_penilai).action_snapshot()
        self.assertEqual(len(status.snapshot_ids), 1)
