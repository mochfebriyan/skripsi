# -*- coding: utf-8 -*-
"""Mesin status kepatuhan Pengelolaan 1, 2, 3 (PRD §8).

- Pengelolaan 2: persentase SOP wajib yang lolos S1–S5 → skor 1–4 (otomatis).
- Pengelolaan 1 dan 3: tangga kriteria berurutan K1–K4. Sistem hanya menilai
  "lengkap secara data"; skor akhir diisi Penilai (semi-otomatis).
"""
import json

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import html_escape

from .common import GROUP_KALAB, GROUP_PENILAI, get_param_int, skor_dari_persen, tgl_id

INDIKATOR = [
    ('p1', 'Pengelolaan 1 · Rencana kerja tahunan'),
    ('p2', 'Pengelolaan 2 · SOP dan instruksi kerja'),
    ('p3', 'Pengelolaan 3 · Struktur organisasi'),
]
CEK_P2 = {
    'S1': 'Terdaftar sebagai SOP wajib',
    'S2': 'Disahkan (ada versi berlaku)',
    'S3': 'Mutakhir (belum lewat tanggal tinjau)',
    'S4': 'Tersedia di semua lokasi penggunaan',
    'S5': 'Disosialisasikan',
}
LABEL_K = {
    'p1': {
        'K1': 'Rencana disahkan dan berlaku',
        'K2': 'Isi lengkap dan selaras Renstra',
        'K3': 'Dijalankan, realisasi tertelusur',
        'K4': 'Ditinjau, perbaikan masuk rencana berikutnya',
    },
    'p3': {
        'K1': 'Struktur dan pengangkatan disahkan (SK)',
        'K2': 'Tugas, wewenang, pelaporan, pengganti lengkap',
        'K3': 'Dijalankan (koordinasi rutin)',
        'K4': 'Beban kerja dan koordinasi dievaluasi',
    },
}


def _ref(model, rec_id, label):
    return {'model': model, 'id': rec_id, 'label': label}


def _tangga(indikator, hasil_per_k):
    """Kriteria berurutan: kriteria berikutnya hanya dihitung bila sebelumnya lengkap."""
    kriteria = []
    dihitung = True
    tertinggi = None
    for kode in ('K1', 'K2', 'K3', 'K4'):
        lengkap, keterangan, bukti = hasil_per_k[kode]
        kriteria.append({
            'kode': kode,
            'label': LABEL_K[indikator][kode],
            'lengkap': bool(lengkap),
            'dihitung': dihitung,
            'keterangan': keterangan,
            'bukti': bukti,
        })
        if dihitung and lengkap:
            tertinggi = kode
        dihitung = dihitung and bool(lengkap)
    return {'indikator': indikator, 'jenis': 'kriteria', 'kriteria': kriteria, 'tertinggi': tertinggi}


class LabfikKepatuhan(models.Model):
    _name = 'labfik.kepatuhan'
    _description = 'Status kepatuhan indikator monev'
    _inherit = ['mail.thread']
    _order = 'periode_id desc, indikator'

    periode_id = fields.Many2one('labfik.periode', 'Periode', required=True, ondelete='cascade')
    indikator = fields.Selection(INDIKATOR, string='Indikator', required=True)
    tanggal_penilaian = fields.Date('Tanggal penilaian', required=True, default=fields.Date.context_today,
                                    tracking=True)
    jenis_skor = fields.Selection([('persentase', 'Persentase (otomatis)'), ('kriteria', 'Kriteria berurutan')],
                                  compute='_compute_jenis_skor', string='Jenis skor')
    persen = fields.Float('Persentase', compute='_compute_hasil', digits=(5, 1))
    skor_sistem = fields.Integer('Skor sistem', compute='_compute_hasil',
                                 help='Pengelolaan 2: skor otomatis. 0 = N/A (tidak ada SOP wajib).')
    kriteria_tertinggi = fields.Char('Kriteria tertinggi lengkap', compute='_compute_hasil')
    ringkasan = fields.Char('Ringkasan', compute='_compute_hasil')
    detail_html = fields.Html('Rincian', compute='_compute_hasil', sanitize=False)
    skor_penilai = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                                    string='Skor penilai', tracking=True)
    catatan_penilai = fields.Text('Catatan penilai', tracking=True)
    snapshot_ids = fields.One2many('labfik.kepatuhan.snapshot', 'kepatuhan_id', string='Snapshot')

    _sql_constraints = [
        ('indikator_unique', 'unique(periode_id, indikator)', 'Status indikator ini sudah ada untuk periode tersebut.'),
    ]

    @api.depends('indikator')
    def _compute_jenis_skor(self):
        for rec in self:
            rec.jenis_skor = 'persentase' if rec.indikator == 'p2' else 'kriteria'

    def _compute_hasil(self):
        for rec in self:
            if not rec.periode_id or not rec.indikator:
                rec.persen = 0
                rec.skor_sistem = 0
                rec.kriteria_tertinggi = False
                rec.ringkasan = False
                rec.detail_html = False
                continue
            hasil = rec.hitung()
            rec.persen = hasil.get('persen') or 0
            rec.skor_sistem = hasil.get('skor', 0)
            rec.kriteria_tertinggi = hasil.get('tertinggi') or (False if hasil['jenis'] == 'persentase' else '–')
            rec.ringkasan = self._ringkasan(hasil)
            rec.detail_html = self._render_html(hasil)

    @api.depends('periode_id.name', 'indikator')
    def _compute_display_name(self):
        label = dict(INDIKATOR)
        for rec in self:
            rec.display_name = '%s · %s' % (label.get(rec.indikator, ''), rec.periode_id.name or '')

    def write(self, vals):
        if {'skor_penilai', 'catatan_penilai'} & set(vals) and not self.env.su \
                and not self.env.user.has_group(GROUP_PENILAI):
            raise UserError(_('Skor dan catatan penilai hanya dapat diisi oleh Penilai.'))
        return super().write(vals)

    @api.model
    def siapkan_untuk_periode(self, periode):
        ada = self.search([('periode_id', '=', periode.id)]).mapped('indikator')
        baru = [{'periode_id': periode.id, 'indikator': kode} for kode, _label in INDIKATOR if kode not in ada]
        if baru:
            self.sudo().create(baru)

    def hitung(self):
        self.ensure_one()
        fungsi = {'p1': self.hitung_p1, 'p2': self.hitung_p2, 'p3': self.hitung_p3}[self.indikator]
        return fungsi(self.periode_id, self.tanggal_penilaian)

    def action_snapshot(self):
        if not self.env.su and not (self.env.user.has_group(GROUP_KALAB) or self.env.user.has_group(GROUP_PENILAI)):
            raise UserError(_('Hanya Kepala Laboratorium atau Penilai yang dapat membuat snapshot.'))
        for rec in self:
            hasil = rec.hitung()
            self.env['labfik.kepatuhan.snapshot'].create({
                'kepatuhan_id': rec.id,
                'tanggal_penilaian': rec.tanggal_penilaian,
                'persen': hasil.get('persen') or 0,
                'skor_sistem': hasil.get('skor', 0),
                'kriteria_tertinggi': hasil.get('tertinggi') or False,
                'ringkasan': self._ringkasan(hasil),
                'hasil_json': json.dumps(hasil, default=str, ensure_ascii=False),
                'detail_html': self._render_html(hasil),
            })
            rec._message_log(body=_('Snapshot status per %s dibuat oleh %s.', tgl_id(rec.tanggal_penilaian),
                                    self.env.user.name))
        return True

    # ================================================================== Pengelolaan 2
    @api.model
    def hitung_p2(self, periode, tanggal):
        wajib = self.env['labfik.dokumen.wajib'].sudo().search([('periode_id', '=', periode.id)])
        baris = []
        for w in wajib:
            dok = w.dokumen_id
            versi = dok.versi_ids.filtered(lambda v: v.state == 'berlaku' and v.tanggal_sah and v.tanggal_sah <= tanggal)
            versi = versi.sorted('tanggal_sah', reverse=True)[:1]
            gagal, keterangan = [], []
            if not versi:
                gagal.append('S2')
                keterangan.append(_('belum ada versi yang disahkan'))
            else:
                if not versi.tanggal_tinjau or versi.tanggal_tinjau < tanggal:
                    gagal.append('S3')
                    keterangan.append(_('lewat tanggal tinjau %s', tgl_id(versi.tanggal_tinjau)))
                lokasi = dok.ruang_ids
                belum = lokasi - versi.distribusi_ids.filtered(lambda d: d.tanggal <= tanggal).ruang_id
                if not lokasi:
                    gagal.append('S4')
                    keterangan.append(_('lokasi penggunaan belum ditetapkan'))
                elif belum:
                    gagal.append('S4')
                    keterangan.append(_('belum didistribusikan ke %s', ', '.join(belum.mapped('display_name'))))
                if not versi.sosialisasi_ids.filtered(lambda s: s.tanggal <= tanggal):
                    gagal.append('S5')
                    keterangan.append(_('belum disosialisasikan'))
            baris.append({
                'dokumen_id': dok.id,
                'kode': dok.kode,
                'nama': dok.name,
                'versi_id': versi.id or False,
                'revisi': versi.revisi or False,
                'memenuhi': not gagal,
                'gagal': gagal,
                'keterangan': keterangan,
            })
        total = len(baris)
        memenuhi = len([b for b in baris if b['memenuhi']])
        persen = round(memenuhi * 100.0 / total, 1) if total else None
        return {
            'indikator': 'p2', 'jenis': 'persentase', 'tanggal': str(tanggal),
            'total': total, 'memenuhi': memenuhi, 'persen': persen,
            'skor': skor_dari_persen(persen), 'baris': baris,
        }

    # ================================================================== Pengelolaan 1
    @api.model
    def hitung_p1(self, periode, tanggal):
        Rencana = self.env['labfik.rencana'].sudo()
        rencana = Rencana.search([
            ('periode_id', '=', periode.id), ('jenis', '=', 'tahunan'),
            ('state', 'in', ('disahkan', 'selesai')), ('tanggal_sah', '<=', tanggal),
            ('lampiran_versi_id', '!=', False),
        ], order='tanggal_sah desc, id desc', limit=1)
        hasil = {}

        # K1
        if rencana:
            hasil['K1'] = (True, [_('"%s" disahkan %s', rencana.name, tgl_id(rencana.tanggal_sah))],
                           [_ref('labfik.rencana', rencana.id, rencana.name),
                            _ref('labfik.dokumen.versi', rencana.lampiran_versi_id.id, _('PDF bertanda tangan'))])
        else:
            hasil['K1'] = (False, [_('belum ada rencana kerja tahunan yang disahkan dengan PDF bertanda tangan')], [])

        # K2
        if rencana and rencana.item_ids:
            kurang = []
            for i, item in enumerate(rencana.item_ids, start=1):
                k = item._kekurangan()
                if k:
                    kurang.append(_('item %s: %s', i, ', '.join(k)))
            hasil['K2'] = (not kurang, kurang or [_('%s item lengkap', len(rencana.item_ids))],
                           [_ref('labfik.rencana', rencana.id, _('Item rencana'))])
        else:
            hasil['K2'] = (False, [_('belum ada item rencana')], [])

        # K3: setiap item punya realisasi berbukti pada setiap semester berjalan yang beririsan dengan jadwalnya
        minimal = get_param_int(self.env, 'labfik.p1_k3_min_realisasi')
        if rencana:
            semester = periode.semester_berjalan(tanggal)
            kurang, pasangan, bukti = [], 0, []
            for i, item in enumerate(rencana.item_ids, start=1):
                for sem in semester:
                    if item.tanggal_mulai and item.tanggal_mulai > sem.tanggal_selesai:
                        continue
                    if item.tanggal_selesai and item.tanggal_selesai < sem.tanggal_mulai:
                        continue
                    pasangan += 1
                    real = item.realisasi_ids.filtered(
                        lambda r: r.semester_id == sem and r.berbukti and r.tanggal <= tanggal)
                    if len(real) < minimal:
                        kurang.append(_('item %s belum punya realisasi berbukti di %s', i, sem.display_name))
                    bukti += [_ref('labfik.rencana.realisasi', r.id, _('Realisasi item %s', i)) for r in real]
            if not pasangan:
                hasil['K3'] = (False, [_('belum ada semester berjalan yang mencakup jadwal item')], [])
            else:
                hasil['K3'] = (not kurang, kurang or [_('%s pasangan item–semester berbukti', pasangan)], bukti)
        else:
            hasil['K3'] = (False, [_('belum ada rencana yang disahkan')], [])

        # K4
        minimal_k4 = get_param_int(self.env, 'labfik.k4_min_per_tahun')
        if rencana:
            tinjauan = rencana.tinjauan_ids.filtered(lambda t: t.tanggal <= tanggal)
            tertaut = tinjauan.keputusan_ids.filtered(lambda k: k.item_berikut_id)
            ket = []
            if len(tinjauan) < minimal_k4:
                ket.append(_('tinjauan baru %s dari minimal %s', len(tinjauan), minimal_k4))
            if not tertaut:
                ket.append(_('belum ada keputusan yang ditautkan ke rencana berikutnya'))
            hasil['K4'] = (not ket, ket or [_('%s tinjauan, %s keputusan ditindaklanjuti', len(tinjauan), len(tertaut))],
                           [_ref('labfik.rencana.tinjauan', t.id, t.display_name) for t in tinjauan])
        else:
            hasil['K4'] = (False, [_('belum ada rencana yang disahkan')], [])
        return _tangga('p1', hasil)

    # ================================================================== Pengelolaan 3
    @api.model
    def hitung_p3(self, periode, tanggal):
        sk_aktif = self.env['labfik.sk'].sudo().search([('state', '=', 'berlaku')]).filtered(
            lambda s: s._aktif_pada(tanggal) and s.lampiran_versi_id
            and any(l._aktif_pada(tanggal) for l in s.line_ids))
        hasil = {}

        # K1
        if sk_aktif:
            hasil['K1'] = (True, [_('SK %s berlaku', ', '.join(sk_aktif.mapped('name')))],
                           [_ref('labfik.sk', s.id, _('SK %s', s.name)) for s in sk_aktif])
        else:
            hasil['K1'] = (False, [_('belum ada SK berlaku dengan file bertanda tangan dan penetapan aktif')], [])

        # K2
        jabatan = self.env['labfik.jabatan'].sudo().search([])
        if jabatan:
            kurang = []
            for j in jabatan:
                k = j._kekurangan(tanggal)
                if k:
                    kurang.append(_('%s: %s', j.name, ', '.join(k)))
            hasil['K2'] = (not kurang, kurang or [_('%s jabatan lengkap', len(jabatan))],
                           [_ref('labfik.jabatan', j.id, j.name) for j in jabatan])
        else:
            hasil['K2'] = (False, [_('belum ada jabatan')], [])

        # K3: rapat koordinasi per semester berjalan
        minimal = get_param_int(self.env, 'labfik.p3_k3_min_rapat')
        semester = periode.semester_berjalan(tanggal)
        rapat = self.env['labfik.rapat'].sudo().search([('periode_id', '=', periode.id), ('tanggal', '<=', tanggal)])
        if not semester:
            hasil['K3'] = (False, [_('belum ada semester berjalan')], [])
        else:
            kurang = []
            for sem in semester:
                jumlah = len(rapat.filtered(lambda r: sem.tanggal_mulai <= r.tanggal <= sem.tanggal_selesai))
                if jumlah < minimal:
                    kurang.append(_('%s: %s rapat dari minimal %s', sem.display_name, jumlah, minimal))
            hasil['K3'] = (not kurang, kurang or [_('%s rapat koordinasi tercatat', len(rapat))],
                           [_ref('labfik.rapat', r.id, r.name) for r in rapat])

        # K4
        minimal_k4 = get_param_int(self.env, 'labfik.k4_min_per_tahun')
        evaluasi = self.env['labfik.evaluasi.struktur'].sudo().search(
            [('periode_id', '=', periode.id), ('tanggal', '<=', tanggal)])
        hasil['K4'] = (len(evaluasi) >= minimal_k4,
                       [_('%s evaluasi dari minimal %s', len(evaluasi), minimal_k4)],
                       [_ref('labfik.evaluasi.struktur', e.id, e.name) for e in evaluasi])
        return _tangga('p3', hasil)

    # ================================================================== tampilan
    @api.model
    def _ringkasan(self, hasil):
        if hasil['jenis'] == 'persentase':
            if hasil['persen'] is None:
                return _('N/A: belum ada SOP wajib pada periode ini')
            return _('%s dari %s SOP wajib memenuhi (%s%%) → skor %s',
                     hasil['memenuhi'], hasil['total'], hasil['persen'], hasil['skor'])
        if not hasil['tertinggi']:
            return _('Belum ada kriteria yang lengkap (K1 belum terpenuhi)')
        return _('Lengkap secara data sampai %s. Skor akhir ditetapkan penilai.', hasil['tertinggi'])

    @api.model
    def _link(self, ref):
        return '<a href="/web#model=%s&amp;id=%s&amp;view_type=form">%s</a>' % (
            ref['model'], ref['id'], html_escape(ref['label']))

    @api.model
    def _render_html(self, hasil):
        if hasil['jenis'] == 'persentase':
            rows = []
            for b in hasil['baris']:
                status = '<span class="badge text-bg-success">Memenuhi</span>' if b['memenuhi'] else \
                    '<span class="badge text-bg-danger">%s</span>' % html_escape(', '.join(b['gagal']))
                rows.append('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
                    self._link(_ref('labfik.dokumen', b['dokumen_id'], b['kode'])),
                    html_escape(b['nama']), status, html_escape('; '.join(b['keterangan']) or '–')))
            legenda = ''.join('<li><b>%s</b> %s</li>' % (k, html_escape(v)) for k, v in CEK_P2.items())
            return ('<p>%s</p><table class="table table-sm table-bordered"><thead><tr><th>Kode</th>'
                    '<th>Dokumen</th><th>Status</th><th>Keterangan</th></tr></thead><tbody>%s</tbody></table>'
                    '<ul class="small text-muted">%s</ul>') % (
                html_escape(self._ringkasan(hasil)), ''.join(rows) or
                '<tr><td colspan="4">Belum ada SOP wajib.</td></tr>', legenda)
        rows = []
        for k in hasil['kriteria']:
            if not k['dihitung']:
                status = '<span class="badge text-bg-secondary">Tidak dihitung</span>'
            elif k['lengkap']:
                status = '<span class="badge text-bg-success">Lengkap secara data</span>'
            else:
                status = '<span class="badge text-bg-danger">Belum</span>'
            bukti = ', '.join(self._link(b) for b in k['bukti'][:10]) or '–'
            rows.append('<tr><td><b>%s</b> %s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
                k['kode'], html_escape(k['label']), status,
                html_escape('; '.join(k['keterangan'])), bukti))
        return ('<p>%s</p><table class="table table-sm table-bordered"><thead><tr><th>Kriteria</th>'
                '<th>Status</th><th>Keterangan</th><th>Bukti</th></tr></thead><tbody>%s</tbody></table>'
                '<p class="small text-muted">"Lengkap secara data" berarti data dan bukti yang diminta sudah ada. '
                'Kualitas isi tetap dinilai penilai.</p>') % (html_escape(self._ringkasan(hasil)), ''.join(rows))


class LabfikKepatuhanSnapshot(models.Model):
    _name = 'labfik.kepatuhan.snapshot'
    _description = 'Snapshot status kepatuhan pada tanggal monev'
    _order = 'create_date desc, id desc'

    kepatuhan_id = fields.Many2one('labfik.kepatuhan', 'Status', required=True, ondelete='cascade')
    periode_id = fields.Many2one(related='kepatuhan_id.periode_id', store=True)
    indikator = fields.Selection(related='kepatuhan_id.indikator', store=True)
    tanggal_penilaian = fields.Date('Tanggal penilaian', required=True, readonly=True)
    persen = fields.Float('Persentase', readonly=True, digits=(5, 1))
    skor_sistem = fields.Integer('Skor sistem', readonly=True)
    kriteria_tertinggi = fields.Char('Kriteria tertinggi', readonly=True)
    ringkasan = fields.Char('Ringkasan', readonly=True)
    hasil_json = fields.Text('Data hasil (JSON)', readonly=True)
    detail_html = fields.Html('Rincian', readonly=True, sanitize=False)

    def write(self, vals):
        if not self.env.su:
            raise UserError(_('Snapshot tidak dapat diubah.'))
        return super().write(vals)
