# -*- coding: utf-8 -*-
"""Data contoh FIKTIF untuk basis data demo. Semua nama, nomor SK, dan dokumen adalah rekaan.

Kondisi yang dibangun meniru lab yang baru mulai memakai sistem:
- struktur dan SK sudah berlaku (Pengelolaan 3 sampai K2; K3 tergantung rapat),
- 6 SOP wajib, 3 memenuhi (Pengelolaan 2 = 50%, skor 1),
- rencana kerja disahkan, realisasi baru sebagian (Pengelolaan 1 sampai K2).
"""
import base64
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


def pdf_contoh(judul):
    """PDF satu halaman yang valid, bertanda 'CONTOH FIKTIF'."""
    teks = ('CONTOH FIKTIF - %s' % judul).replace('(', '[').replace(')', ']')
    stream = 'BT /F1 14 Tf 60 780 Td (%s) Tj ET' % teks[:90]
    objek = [
        '<< /Type /Catalog /Pages 2 0 R >>',
        '<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R '
        '/Resources << /Font << /F1 5 0 R >> >> >>',
        '<< /Length %d >>\nstream\n%s\nendstream' % (len(stream), stream),
        '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
    ]
    out = '%PDF-1.4\n'
    offsets = []
    for i, isi in enumerate(objek, start=1):
        offsets.append(len(out.encode('latin-1')))
        out += '%d 0 obj\n%s\nendobj\n' % (i, isi)
    xref = len(out.encode('latin-1'))
    out += 'xref\n0 %d\n0000000000 65535 f \n' % (len(objek) + 1)
    out += ''.join('%010d 00000 n \n' % o for o in offsets)
    out += 'trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n' % (len(objek) + 1, xref)
    return base64.b64encode(out.encode('latin-1'))


class LabfikDemo(models.AbstractModel):
    _name = 'labfik.demo'
    _description = 'Pemuat data contoh LabFIK'

    @api.model
    def _muat_demo(self):
        env = self.env
        hari_ini = fields.Date.context_today(self)
        tahun = hari_ini.year if hari_ini.month >= 9 else hari_ini.year - 1
        lang = 'id_ID' if env['res.lang'].search_count([('code', '=', 'id_ID')]) else False

        periode = env['labfik.periode'].create({
            'name': '%s/%s' % (tahun, tahun + 1),
            'tanggal_mulai': date(tahun, 9, 1),
            'tanggal_selesai': date(tahun + 1, 8, 31),
        })

        # ---------------------------------------------------------- akun login contoh
        grup_user = env.ref('base.group_user')

        def akun(login, nama, grup_tambahan=None):
            vals = {'name': nama, 'login': login, 'password': login,
                    'groups_id': [(6, 0, [grup_user.id] + ([grup_tambahan.id] if grup_tambahan else []))]}
            if lang:
                vals.update(lang=lang, tz='Asia/Jakarta')
            return env['res.users'].with_context(no_reset_password=True).create(vals)

        u_kalab = akun('kalab', 'Sari Wulandari')
        u_laboran = akun('laboran', 'Dodi Pratama')
        u_asisten = akun('asisten', 'Rani Putri')
        u_penilai = akun('penilai', 'Gilang Ramadhan', env.ref('labfik_org.group_labfik_penilai'))

        # ---------------------------------------------------------- personel
        Personel = env['labfik.personel']
        p = {
            'dekan': Personel.create({'name': 'Dr. Rahmat Hidayat', 'jenis': 'eksternal', 'nomor_induk': 'CONTOH-0001'}),
            'kalab': Personel.create({'name': 'Sari Wulandari', 'jenis': 'dosen', 'nomor_induk': 'CONTOH-0002',
                                      'email': 'kalab@contoh.test', 'user_id': u_kalab.id}),
            'laboran': Personel.create({'name': 'Dodi Pratama', 'jenis': 'tendik', 'nomor_induk': 'CONTOH-0003',
                                        'user_id': u_laboran.id}),
            'laboran2': Personel.create({'name': 'Wati Lestari', 'jenis': 'tendik', 'nomor_induk': 'CONTOH-0004'}),
            'k3': Personel.create({'name': 'Joko Santoso', 'jenis': 'tendik', 'nomor_induk': 'CONTOH-0005'}),
            'dosen': Personel.create({'name': 'Andi Saputra', 'jenis': 'dosen', 'nomor_induk': 'CONTOH-0006'}),
            'asisten': Personel.create({'name': 'Rani Putri', 'jenis': 'mahasiswa', 'nomor_induk': 'CONTOH-0007',
                                        'user_id': u_asisten.id}),
            'asisten2': Personel.create({'name': 'Budi Setiawan', 'jenis': 'mahasiswa', 'nomor_induk': 'CONTOH-0008'}),
            'penilai': Personel.create({'name': 'Gilang Ramadhan', 'jenis': 'dosen', 'nomor_induk': 'CONTOH-0009',
                                        'user_id': u_penilai.id}),
        }

        # ---------------------------------------------------------- jabatan
        j = {k: env.ref('labfik_org.jabatan_%s' % k) for k in ('kalab', 'laboran', 'k3', 'dosen', 'asisten')}
        kw = lambda x: env.ref('labfik_org.kewenangan_%s' % x).id  # noqa: E731
        j['kalab'].write({
            'uraian_tugas': '<p>Mengendalikan layanan laboratorium, menetapkan prioritas, meninjau kinerja dan risiko.</p>',
            'kewenangan_ids': [(6, 0, [kw('sahkan_sop'), kw('sahkan_rencana'), kw('tetapkan_wajib'), kw('k3')])],
            'pengganti_id': j['laboran'].id,
        })
        j['laboran'].write({
            'uraian_tugas': '<p>Menyiapkan sesi, mengelola inventaris dan dokumen, mencatat penggunaan.</p>',
            'kewenangan_ids': [(6, 0, [kw('susun_sop'), kw('distribusi'), kw('realisasi')])],
            'pengganti_id': j['kalab'].id,
        })
        j['k3'].write({
            'uraian_tugas': '<p>Memeriksa sarana keselamatan dan memberi induksi K3.</p>',
            'kewenangan_ids': [(6, 0, [kw('k3'), kw('realisasi')])],
            'pengganti_id': j['laboran'].id,
        })
        j['dosen'].write({
            'uraian_tugas': '<p>Menetapkan modul dan asesmen praktikum, mendampingi sesi.</p>',
            'kewenangan_ids': [(6, 0, [kw('dampingi')])],
            'pengganti_id': j['kalab'].id,
        })
        j['asisten'].write({
            'uraian_tugas': '<p>Mendampingi praktikan sesuai modul dan melaporkan kendala.</p>',
            'kewenangan_ids': [(6, 0, [kw('dampingi')])],
            'pengganti_id': j['laboran'].id,
        })

        # ---------------------------------------------------------- SK penetapan
        sk = env['labfik.sk'].create({
            'name': 'CONTOH/045/FIK/%s' % tahun,
            'tanggal': periode.tanggal_mulai,
            'pengesah_id': p['dekan'].id,
            'tanggal_mulai': periode.tanggal_mulai,
            'tanggal_selesai': periode.tanggal_selesai,
            'line_ids': [(0, 0, {'personel_id': p[a].id, 'jabatan_id': j[b].id}) for a, b in (
                ('kalab', 'kalab'), ('laboran', 'laboran'), ('laboran2', 'laboran'), ('k3', 'k3'),
                ('dosen', 'dosen'), ('asisten', 'asisten'), ('asisten2', 'asisten'))],
        })
        sk.write({'lampiran_file': pdf_contoh('SK Penetapan Pengelola'), 'lampiran_filename': 'sk-pengelola.pdf'})
        sk.action_berlakukan()

        # ---------------------------------------------------------- ruang
        Ruang = env['labfik.ruang']
        ruang = {kode: Ruang.create({'kode': kode, 'name': nama, 'lokasi': 'Gedung FIK'}) for kode, nama in (
            ('FIKLAB-201', 'Lab 201'), ('FIKLAB-301', 'Lab 301'), ('FIKLAB-302', 'Lab 302'),
            ('FIKLAB-303', 'Lab 303'), ('FIKLAB-304', 'Lab 304'), ('FIKLAB-401', 'Lab 401 IoT'),
            ('FIKLAB-402', 'Lab 402'), ('FIKLAB-403', 'Lab 403'))}
        ruang['PORTAL'] = Ruang.create({'kode': 'PORTAL', 'name': 'Portal LabFIK', 'is_virtual': True})

        # ---------------------------------------------------------- SOP
        def sop(kode, judul, kategori, lokasi, sampai):
            dok = env['labfik.dokumen'].create({
                'kode': kode, 'name': judul, 'jenis': 'ik' if kode.startswith('IK') else 'sop',
                'kategori': kategori, 'pemilik_id': p['laboran'].id,
                'dasar_kebutuhan': 'Contoh fiktif: kegiatan rutin praktikum.',
                'ruang_ids': [(6, 0, [ruang[x].id for x in lokasi])],
            })
            versi = env['labfik.dokumen.versi'].with_user(u_laboran).create({
                'dokumen_id': dok.id, 'file': pdf_contoh(judul), 'file_name': '%s.pdf' % kode,
                'ringkasan': 'Terbitan pertama.',
            })
            versi.action_ajukan()
            if sampai == 'diajukan':
                return dok
            versi.with_user(u_kalab).action_sahkan()
            daftar_lokasi = lokasi if sampai != 'kurang_distribusi' else lokasi[:1]
            for x in daftar_lokasi:
                env['labfik.dokumen.distribusi'].create({'versi_id': versi.id, 'ruang_id': ruang[x].id,
                                                         'petugas_id': p['laboran'].id})
            if sampai != 'tanpa_sosialisasi':
                env['labfik.dokumen.sosialisasi'].create({
                    'versi_id': versi.id, 'metode': 'briefing',
                    'peserta_ids': [(6, 0, [p['asisten'].id, p['asisten2'].id, p['dosen'].id])],
                })
            return dok

        dokumen = [
            sop('SOP-TT-001', 'Tata tertib laboratorium', 'tata_tertib', ['FIKLAB-301', 'FIKLAB-302', 'PORTAL'], 'lengkap'),
            sop('SOP-PRA-001', 'Pelaksanaan praktikum', 'praktikum', ['FIKLAB-301', 'FIKLAB-302'], 'lengkap'),
            sop('SOP-PJM-001', 'Peminjaman ruang dan alat', 'peminjaman', ['PORTAL'], 'lengkap'),
            sop('SOP-K3-001', 'Keselamatan dan kedaruratan', 'k3', ['FIKLAB-301', 'FIKLAB-302'], 'kurang_distribusi'),
            sop('SOP-ALT-001', 'Penggunaan 3D printer', 'alat', ['FIKLAB-401'], 'diajukan'),
            sop('IK-LMB-001', 'Penanganan limbah elektronik', 'limbah', ['FIKLAB-401'], 'tanpa_sosialisasi'),
        ]
        env['labfik.dokumen.wajib'].create([{'periode_id': periode.id, 'dokumen_id': d.id} for d in dokumen])

        # ---------------------------------------------------------- KPI, Renstra, rencana kerja
        Kpi = env['labfik.kpi']
        kpi_sesi = Kpi.create({'kode': 'KPI-01', 'name': 'Keterlaksanaan sesi praktikum', 'satuan': '%',
                               'pembilang': 'Sesi terlaksana sesuai jadwal', 'penyebut': 'Sesi yang direncanakan',
                               'sumber_data': 'Jurnal sesi praktikum'})
        kpi_sop = Kpi.create({'kode': 'KPI-02', 'name': 'SOP wajib terkendali', 'satuan': '%',
                              'pembilang': 'SOP wajib yang memenuhi', 'penyebut': 'Seluruh SOP wajib',
                              'sumber_data': 'Status Pengelolaan 2'})
        kpi_k3 = Kpi.create({'kode': 'KPI-03', 'name': 'Pelatihan K3 asisten', 'satuan': 'kali',
                             'sumber_data': 'Daftar hadir pelatihan'})
        renstra = env['labfik.renstra.sasaran'].create({
            'tingkat': 'upps', 'kode': 'CONTOH-UPPS-01', 'name': 'Peningkatan mutu layanan laboratorium',
            'dokumen_sumber': 'Contoh fiktif; ganti dengan Renstra FIK yang berlaku'})

        rencana = env['labfik.rencana'].with_user(u_kalab).create({
            'name': 'Rencana Kerja LabFIK %s' % periode.name,
            'periode_id': periode.id,
            'pemilik_id': p['kalab'].id,
            'pengesah_id': p['dekan'].id,
            'narasi': '<p>Contoh fiktif: fokus tahun ini adalah menyusun dan mengendalikan SOP wajib '
                      'serta memastikan sesi praktikum tercatat.</p>',
            'item_ids': [
                (0, 0, {'sasaran': 'Seluruh SOP wajib disahkan dan disosialisasikan', 'kpi_id': kpi_sop.id,
                        'target': '100%', 'pic_id': p['laboran'].id, 'anggaran': 500000,
                        'renstra_ids': [(6, 0, [renstra.id])],
                        'tanggal_mulai': periode.tanggal_mulai, 'tanggal_selesai': periode.tanggal_selesai}),
                (0, 0, {'sasaran': 'Sesi praktikum terlaksana sesuai jadwal', 'kpi_id': kpi_sesi.id,
                        'target': '≥ 90%', 'pic_id': p['kalab'].id, 'tanpa_anggaran': True,
                        'renstra_ids': [(6, 0, [renstra.id])],
                        'tanggal_mulai': periode.tanggal_mulai, 'tanggal_selesai': periode.tanggal_selesai}),
                (0, 0, {'sasaran': 'Pelatihan K3 untuk asisten praktikum', 'kpi_id': kpi_k3.id,
                        'target': '1 kali per semester', 'pic_id': p['k3'].id, 'anggaran': 1500000,
                        'renstra_teks': 'Contoh fiktif: sasaran keselamatan kerja FIK',
                        'tanggal_mulai': periode.tanggal_mulai, 'tanggal_selesai': periode.tanggal_selesai}),
            ],
        })
        rencana.action_ajukan()
        rencana.write({'lampiran_file': pdf_contoh('Rencana Kerja Bertanda Tangan'),
                       'lampiran_filename': 'rencana-kerja-ttd.pdf'})
        rencana.action_sahkan()

        semester = periode.semester_pada(hari_ini) or periode.semester_ids[:1]
        for item, capaian in ((rencana.item_ids[0], '3 dari 6 SOP wajib memenuhi'),
                              (rencana.item_ids[1], '88% sesi terlaksana')):
            env['labfik.rencana.realisasi'].create({
                'item_id': item.id, 'semester_id': semester.id, 'capaian': capaian,
                'tanggal': min(hari_ini, semester.tanggal_selesai),
                'bukti': pdf_contoh('Bukti realisasi'), 'bukti_name': 'bukti-realisasi.pdf',
                'pelapor_id': item.pic_id.id,
            })

        # ---------------------------------------------------------- rapat koordinasi
        tanggal_rapat = max(periode.tanggal_mulai, hari_ini - relativedelta(days=7))
        env['labfik.rapat'].create({
            'name': 'Rapat koordinasi awal semester', 'periode_id': periode.id, 'tanggal': tanggal_rapat,
            'peserta_ids': [(6, 0, [p['kalab'].id, p['laboran'].id, p['laboran2'].id, p['k3'].id])],
            'keputusan': 'Contoh fiktif: pembagian penanggung jawab ruang dan target penyusunan SOP.',
        })

        env['labfik.kepatuhan'].siapkan_untuk_periode(periode)
        return True
