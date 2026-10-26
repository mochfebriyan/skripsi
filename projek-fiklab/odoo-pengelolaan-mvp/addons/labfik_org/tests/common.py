# -*- coding: utf-8 -*-
"""Kelas dasar test. Semua tanggal relatif terhadap hari ini agar test tetap valid kapan pun dijalankan.

Periode uji: mulai 60 hari lalu, 365 hari. Semester Ganjil = ~5 bulan pertama, Genap = sisanya.
"""
from dateutil.relativedelta import relativedelta

from odoo import fields
from odoo.tests.common import TransactionCase, new_test_user

from ..models.demo import pdf_contoh

G_PENGGUNA = 'base.group_user,labfik_org.group_labfik_pengguna'
G_LABORAN = 'base.group_user,labfik_org.group_labfik_laboran'
G_KALAB = 'base.group_user,labfik_org.group_labfik_kalab'
G_PENILAI = 'base.group_user,labfik_org.group_labfik_penilai'


class LabfikCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True, no_reset_password=True))
        cls.today = fields.Date.context_today(cls.env['labfik.periode'])
        cls.pdf = pdf_contoh('Uji')

        cls.periode = cls.env['labfik.periode'].create({
            'name': 'UJI-%s' % cls.today.year,
            'tanggal_mulai': cls.today - relativedelta(days=60),
            'tanggal_selesai': cls.today - relativedelta(days=60) + relativedelta(days=364),
        })
        cls.ganjil = cls.periode.semester_ids.filtered(lambda s: s.name == 'ganjil')
        cls.genap = cls.periode.semester_ids.filtered(lambda s: s.name == 'genap')

        Ruang = cls.env['labfik.ruang']
        cls.r301 = Ruang.create({'kode': 'T-301', 'name': 'Lab uji 301'})
        cls.r302 = Ruang.create({'kode': 'T-302', 'name': 'Lab uji 302'})
        cls.portal = Ruang.create({'kode': 'T-PORTAL', 'name': 'Portal uji', 'is_virtual': True})

        # Akun dengan grup tetap (tidak ditautkan ke personel, jadi tidak disentuh sinkronisasi).
        cls.u_kalab = new_test_user(cls.env, login='t_kalab', groups=G_KALAB)
        cls.u_laboran = new_test_user(cls.env, login='t_laboran', groups=G_LABORAN)
        cls.u_laboran2 = new_test_user(cls.env, login='t_laboran2', groups=G_LABORAN)
        cls.u_pengguna = new_test_user(cls.env, login='t_pengguna', groups=G_PENGGUNA)
        cls.u_penilai = new_test_user(cls.env, login='t_penilai', groups=G_PENILAI)

        Personel = cls.env['labfik.personel']
        cls.p_dekan = Personel.create({'name': 'Dekan Uji', 'jenis': 'eksternal'})
        cls.p_kalab = Personel.create({'name': 'KaLab Uji', 'jenis': 'dosen', 'nomor_induk': 'U-001'})
        cls.p_laboran = Personel.create({'name': 'Laboran Uji', 'jenis': 'tendik', 'nomor_induk': 'U-002'})
        cls.p_k3 = Personel.create({'name': 'Petugas K3 Uji', 'jenis': 'tendik'})
        cls.p_dosen = Personel.create({'name': 'Dosen Uji', 'jenis': 'dosen'})
        cls.p_asisten = Personel.create({'name': 'Asisten Uji', 'jenis': 'mahasiswa'})

        cls.j = {k: cls.env.ref('labfik_org.jabatan_%s' % k) for k in ('kalab', 'laboran', 'k3', 'dosen', 'asisten')}

    # ------------------------------------------------------------------ helper struktur
    @classmethod
    def lengkapi_jabatan(cls, kecuali=()):
        kw = cls.env.ref('labfik_org.kewenangan_dampingi')
        pengganti = {'kalab': 'laboran', 'laboran': 'kalab', 'k3': 'laboran', 'dosen': 'kalab', 'asisten': 'laboran'}
        for kode, jab in cls.j.items():
            if kode in kecuali:
                continue
            jab.write({'uraian_tugas': '<p>Tugas %s</p>' % jab.name, 'kewenangan_ids': [(6, 0, kw.ids)],
                       'pengganti_id': cls.j[pengganti[kode]].id})

    @classmethod
    def buat_sk(cls, baris, berlakukan=True, mulai=None, selesai=None, nama='SK-UJI'):
        sk = cls.env['labfik.sk'].create({
            'name': nama, 'pengesah_id': cls.p_dekan.id,
            'tanggal_mulai': mulai or cls.periode.tanggal_mulai,
            'tanggal_selesai': selesai or cls.periode.tanggal_selesai,
            'line_ids': [(0, 0, {'personel_id': p.id, 'jabatan_id': j.id}) for p, j in baris],
        })
        if berlakukan:
            sk.write({'lampiran_file': cls.pdf, 'lampiran_filename': 'sk.pdf'})
            sk.action_berlakukan()
        return sk

    @classmethod
    def struktur_lengkap(cls):
        cls.lengkapi_jabatan()
        return cls.buat_sk([(cls.p_kalab, cls.j['kalab']), (cls.p_laboran, cls.j['laboran']),
                            (cls.p_k3, cls.j['k3']), (cls.p_dosen, cls.j['dosen']),
                            (cls.p_asisten, cls.j['asisten'])])

    # ------------------------------------------------------------------ helper dokumen
    @classmethod
    def buat_dokumen(cls, kode, ruang=None, jenis='sop'):
        return cls.env['labfik.dokumen'].create({
            'kode': kode, 'name': 'Dokumen %s' % kode, 'jenis': jenis, 'kategori': 'praktikum',
            'ruang_ids': [(6, 0, (ruang or cls.r301).ids)],
        })

    @classmethod
    def buat_versi(cls, dokumen, sampai='berlaku'):
        """Alur nyata: laboran membuat dan mengajukan, KaLab mengesahkan."""
        versi = cls.env['labfik.dokumen.versi'].with_user(cls.u_laboran).create({
            'dokumen_id': dokumen.id, 'file': cls.pdf, 'file_name': '%s.pdf' % dokumen.kode,
        })
        if sampai == 'draf':
            return versi.with_env(cls.env)
        versi.action_ajukan()
        if sampai == 'diajukan':
            return versi.with_env(cls.env)
        versi.with_user(cls.u_kalab).action_sahkan()
        return versi.with_env(cls.env)

    @classmethod
    def sop_memenuhi(cls, kode, ruang=None):
        dok = cls.buat_dokumen(kode, ruang)
        versi = cls.buat_versi(dok)
        for r in dok.ruang_ids:
            cls.env['labfik.dokumen.distribusi'].create({'versi_id': versi.id, 'ruang_id': r.id})
        cls.env['labfik.dokumen.sosialisasi'].create({'versi_id': versi.id, 'peserta_ids': [(6, 0, cls.p_asisten.ids)]})
        return dok, versi

    @classmethod
    def jadikan_wajib(cls, dokumen):
        cls.env['labfik.dokumen.wajib'].create([{'periode_id': cls.periode.id, 'dokumen_id': d.id} for d in dokumen])

    # ------------------------------------------------------------------ helper rencana
    @classmethod
    def buat_kpi_renstra(cls):
        cls.kpi = cls.env['labfik.kpi'].create({'kode': 'T-KPI-01', 'name': 'KPI uji', 'satuan': '%'})
        cls.renstra = cls.env['labfik.renstra.sasaran'].create({'kode': 'T-R-01', 'name': 'Sasaran uji'})

    @classmethod
    def item_vals(cls, n=1, **kw):
        vals = {'sasaran': 'Sasaran %s' % n, 'kpi_id': cls.kpi.id, 'target': '100%', 'pic_id': cls.p_laboran.id,
                'tanggal_mulai': cls.periode.tanggal_mulai, 'tanggal_selesai': cls.periode.tanggal_selesai,
                'anggaran': 1000000, 'renstra_ids': [(6, 0, cls.renstra.ids)]}
        vals.update(kw)
        return vals

    @classmethod
    def buat_rencana(cls, jumlah_item=2, sahkan=True, periode=None, **item_kw):
        rencana = cls.env['labfik.rencana'].create({
            'name': 'Rencana uji', 'periode_id': (periode or cls.periode).id, 'pemilik_id': cls.p_kalab.id,
            'pengesah_id': cls.p_dekan.id,
            'item_ids': [(0, 0, cls.item_vals(n, **item_kw)) for n in range(1, jumlah_item + 1)],
        })
        if sahkan:
            rencana.action_ajukan()
            rencana.write({'lampiran_file': cls.pdf, 'lampiran_filename': 'rencana.pdf'})
            rencana.action_sahkan()
        return rencana

    @classmethod
    def realisasi(cls, item, semester, bukti=True, tanggal=None):
        vals = {'item_id': item.id, 'semester_id': semester.id, 'capaian': 'tercapai',
                'tanggal': tanggal or min(cls.today, semester.tanggal_selesai)}
        if bukti:
            vals.update(bukti=cls.pdf, bukti_name='bukti.pdf')
        return cls.env['labfik.rencana.realisasi'].create(vals)
