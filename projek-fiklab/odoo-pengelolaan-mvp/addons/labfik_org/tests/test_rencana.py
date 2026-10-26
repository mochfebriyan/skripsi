# -*- coding: utf-8 -*-
"""Pengelolaan 1: rencana kerja (TC-P1-01 … TC-P1-06)."""
from odoo.exceptions import UserError
from odoo.tests import tagged

from .common import LabfikCase


@tagged('post_install', '-at_install', 'labfik')
class TestRencana(LabfikCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.buat_kpi_renstra()

    def test_ajukan_ditolak_bila_item_tidak_lengkap(self):
        """US-13: rencana tidak bisa diajukan bila ada item tanpa KPI, target, PIC, jadwal, anggaran, atau Renstra."""
        rencana = self.buat_rencana(jumlah_item=1, sahkan=False)
        rencana.item_ids.write({'kpi_id': False, 'anggaran': 0, 'renstra_ids': [(5,)]})
        with self.assertRaises(UserError) as err:
            rencana.action_ajukan()
        pesan = str(err.exception)
        for kata in ('KPI', 'anggaran', 'keterkaitan Renstra'):
            self.assertIn(kata, pesan)
        # Tanpa anggaran diperbolehkan bila dinyatakan eksplisit; Renstra boleh berupa teks.
        rencana.item_ids.write({'kpi_id': self.kpi.id, 'tanpa_anggaran': True, 'renstra_teks': 'Renstra FIK'})
        rencana.action_ajukan()
        self.assertEqual(rencana.state, 'diajukan')

    def test_ajukan_tanpa_item_ditolak(self):
        rencana = self.env['labfik.rencana'].create({'name': 'Kosong', 'periode_id': self.periode.id})
        with self.assertRaises(UserError):
            rencana.action_ajukan()

    def test_sahkan_butuh_pdf_bertanda_tangan_dan_kalab(self):
        """US-14 / TC-P1-02: status disahkan butuh PDF di register; hanya KaLab."""
        rencana = self.buat_rencana(sahkan=False)
        rencana.with_user(self.u_kalab).action_ajukan()
        with self.assertRaises(UserError):
            rencana.with_user(self.u_kalab).action_sahkan()
        rencana.with_user(self.u_kalab).write({'lampiran_file': self.pdf, 'lampiran_filename': 'ttd.pdf'})
        self.assertEqual(rencana.lampiran_versi_id.dokumen_id.jenis, 'rencana')
        with self.assertRaises(UserError):
            rencana.with_user(self.u_laboran).action_sahkan()
        rencana.with_user(self.u_kalab).action_sahkan()
        self.assertEqual((rencana.state, rencana.tanggal_sah, rencana.disahkan_oleh_id),
                         ('disahkan', self.today, self.u_kalab))
        with self.assertRaises(UserError):
            rencana.with_user(self.u_kalab).write({'lampiran_file': self.pdf, 'lampiran_filename': 'lain.pdf'})

    def test_isi_terkunci_setelah_diajukan(self):
        rencana = self.buat_rencana(sahkan=False)
        rencana.action_ajukan()
        with self.assertRaises(UserError):
            rencana.item_ids[0].with_user(self.u_kalab).write({'target': '50%'})
        with self.assertRaises(UserError):
            rencana.with_user(self.u_kalab).write({'periode_id': self.periode.id, 'name': 'Ubah'})
        with self.assertRaises(UserError):
            self.env['labfik.rencana.item'].with_user(self.u_kalab).create(
                dict(self.item_vals(9), rencana_id=rencana.id))
        with self.assertRaises(UserError):
            rencana.with_user(self.u_kalab).write({'state': 'disahkan'})

    def test_tolak_rencana(self):
        rencana = self.buat_rencana(sahkan=False)
        rencana.action_ajukan()
        rencana.with_user(self.u_kalab)._tolak('Target item 2 belum terukur')
        self.assertEqual((rencana.state, rencana.alasan_tolak), ('draf', 'Target item 2 belum terukur'))
        rencana.item_ids[1].with_user(self.u_kalab).write({'target': '10 dari 10 SOP'})

    def test_revisi_mengganti_rencana_lama(self):
        """US-15 / FR-C6: revisi disahkan → rencana lama menjadi 'diganti'; realisasi ikut tersalin."""
        rencana = self.buat_rencana()
        self.realisasi(rencana.item_ids[0], self.ganjil)
        aksi = rencana.with_user(self.u_kalab).action_buat_revisi()
        revisi = self.env['labfik.rencana'].browse(aksi['res_id'])
        self.assertEqual((revisi.state, revisi.rencana_asal_id), ('draf', rencana))
        self.assertEqual(len(revisi.item_ids), 2)
        self.assertEqual(len(revisi.item_ids[0].realisasi_ids), 1)
        self.assertEqual(rencana.state, 'disahkan', 'versi lama tetap berlaku sampai revisi disahkan')
        with self.assertRaises(UserError):
            rencana.with_user(self.u_kalab).action_buat_revisi()
        revisi.item_ids[1].write({'target': 'baru'})
        revisi.action_ajukan()
        revisi.write({'lampiran_file': self.pdf, 'lampiran_filename': 'revisi.pdf'})
        revisi.with_user(self.u_kalab).action_sahkan()
        self.assertEqual((rencana.state, revisi.state), ('diganti', 'disahkan'))

    def test_realisasi_hanya_untuk_rencana_disahkan(self):
        """TC-P1-05: realisasi dilaporkan setelah rencana disahkan, pada semester periode rencana."""
        draf = self.buat_rencana(sahkan=False)
        with self.assertRaises(UserError):
            self.env['labfik.rencana.realisasi'].with_user(self.u_kalab).create(
                {'item_id': draf.item_ids[0].id, 'semester_id': self.ganjil.id, 'capaian': 'x'})
        rencana = self.buat_rencana()
        r = self.realisasi(rencana.item_ids[0], self.ganjil)
        self.assertTrue(r.berbukti)
        tanpa = self.realisasi(rencana.item_ids[1], self.ganjil, bukti=False)
        self.assertFalse(tanpa.berbukti)

    def test_tinjauan_hanya_rencana_disahkan_dan_tindak_lanjut_ke_rencana_lain(self):
        draf = self.buat_rencana(sahkan=False)
        with self.assertRaises(UserError):
            self.env['labfik.rencana.tinjauan'].with_user(self.u_kalab).create(
                {'rencana_id': draf.id, 'ringkasan': 'x'})
        rencana = self.buat_rencana()
        tinjauan = self.env['labfik.rencana.tinjauan'].create({'rencana_id': rencana.id, 'ringkasan': 'ok'})
        with self.assertRaises(Exception):
            self.env['labfik.rencana.tinjauan.keputusan'].create(
                {'tinjauan_id': tinjauan.id, 'uraian': 'x', 'item_berikut_id': rencana.item_ids[0].id})

    def test_cetak_rencana_dan_laporan_pelaksanaan(self):
        """TC-P1-01 … TC-P1-05 / NFR-10: dokumen tercetak dengan format baku dan tanggal Indonesia."""
        rencana = self.buat_rencana()
        self.realisasi(rencana.item_ids[0], self.ganjil)
        R = self.env['ir.actions.report']
        html, _t = R._render_qweb_html('labfik_org.report_rencana_kerja', rencana.ids)
        html = html.decode()
        for teks in ('RENCANA KERJA TAHUNAN', 'Matriks keterkaitan Renstra', 'Sasaran uji', 'No 1, No 2',
                     'T-KPI-01', 'Dekan Uji', '2.000.000', rencana.tgl_id(self.today)):
            self.assertIn(teks, html)
        self.assertNotIn('BELUM DISAHKAN', html)
        laporan, _t = R._render_qweb_html('labfik_org.report_laporan_pelaksanaan', rencana.ids)
        laporan = laporan.decode()
        self.assertIn('LAPORAN PELAKSANAAN', laporan)
        self.assertIn('belum ada realisasi', laporan)
        draf = self.buat_rencana(sahkan=False)
        html_draf, _t = R._render_qweb_html('labfik_org.report_rencana_kerja', draf.ids)
        self.assertIn('BELUM DISAHKAN', html_draf.decode())
