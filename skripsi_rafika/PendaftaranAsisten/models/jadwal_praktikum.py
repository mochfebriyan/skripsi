# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api

class JadwalPraktikum(models.Model):
    _name = 'jadwal.praktikum'
    _description = 'Master Jadwal Praktikum'

    name = fields.Char(string="Nama Jadwal", compute="_compute_name", store=True)
    mata_kuliah_id = fields.Many2one('mst_coursesemt', string="Mata Kuliah", required=True, domain="[('butuh_asisten', '=', True)]")
    dosen_id = fields.Many2one('mst_dosen', string="Dosen", required=True) 
    kode_kelas_id = fields.Many2one('mst_kodekelas', string="Kelas / Ruangan", required=True)

    hari = fields.Selection([
        ('senin', 'Senin'), ('selasa', 'Selasa'), ('rabu', 'Rabu'),
        ('kamis', 'Kamis'), ('jumat', 'Jumat'), ('sabtu', 'Sabtu')
    ], string="Hari", required=True)

    def _get_waktu_selection(self):
        selection = []
        for hour in range(7, 19): 
            for minute in range(0, 60, 10):
                time_str = f"{hour:02d}:{minute:02d}"
                selection.append((time_str, time_str))
        return selection

    jam_mulai = fields.Selection(selection='_get_waktu_selection', string="Jam Mulai", required=True)
    jam_selesai = fields.Selection(selection='_get_waktu_selection', string="Jam Selesai", required=True)
    
    # =====================================================================
    # PERUBAHAN: Field diubah menjadi compute yang mengambil data dari planning
    # =====================================================================
    kuota_asisten = fields.Integer(
        string="Kuota Asisten", 
        compute="_compute_kuota_asisten", 
        store=True, 
        help="Terisi otomatis dari Perencanaan Kuota yang sudah disetujui Kalab."
    )
    asisten_ids = fields.Many2many('op.student', string="Asisten Terdaftar")
    pertemuan_ke = fields.Integer(string="Pertemuan Ke", default=0, help="Nomor pertemuan yang dialokasikan untuk jadwal ini (1-14).")

    @api.depends('mata_kuliah_id')
    def _compute_kuota_asisten(self):
        for record in self:
            if record.mata_kuliah_id:
                # Cari data perencanaan kuota yang sudah Final untuk matkul ini
                planning = self.env['assistant.planning'].search([
                    ('course_id', '=', record.mata_kuliah_id.id),
                    ('state', '=', 'final')
                ], limit=1)
                
                # Jika ketemu, ambil kuotanya. Jika belum ada/belum final, set 0.
                record.kuota_asisten = planning.assistant_quota if planning else 0
            else:
                record.kuota_asisten = 0

    @api.onchange('jam_mulai')
    def _onchange_jam_mulai(self):
        if self.jam_mulai:
            jam, menit = map(int, self.jam_mulai.split(':'))
            total_menit = (jam * 60) + menit + 100
            jam_baru = (total_menit // 60) % 24
            menit_baru = total_menit % 60
            self.jam_selesai = f"{jam_baru:02d}:{menit_baru:02d}"

    @api.depends('mata_kuliah_id', 'hari')
    def _compute_name(self):
        for record in self:
            if record.mata_kuliah_id:
                record.name = f"{record.mata_kuliah_id.display_name}"
            else:
                record.name = "Jadwal Baru"

    def action_klaim_jadwal(self, student_id):
        self.ensure_one()

        # REVISI 11: Validasi deadline alokasi jadwal
        periode_aktif = self.env['mst_periodesemt'].search([
            ('active', '=', True),
            ('deadline_alokasi', '!=', False),
        ], limit=1)
        if periode_aktif and fields.Datetime.now() > periode_aktif.deadline_alokasi:
            return {'status': 'error', 'pesan': 'Mohon maaf, masa alokasi jadwal telah ditutup.'}

        # PERBAIKAN: Validasi tambahan jika matkul belum disetujui kuotanya oleh Kalab
        if self.kuota_asisten <= 0:
            return {'status': 'error', 'pesan': 'Mohon maaf, kuota asisten untuk mata kuliah ini belum ditetapkan oleh Kepala Lab.'}
            
        if len(self.asisten_ids) >= self.kuota_asisten:
            return {'status': 'error', 'pesan': 'Mohon maaf, kuota asisten untuk kelas ini sudah penuh.'}

        jadwal_lain = self.env['jadwal.praktikum'].search([
            ('asisten_ids', 'in', [student_id.id]),
            ('hari', '=', self.hari),
            ('id', '!=', self.id)
        ])

        for j in jadwal_lain:
            if (self.jam_mulai < j.jam_selesai) and (self.jam_selesai > j.jam_mulai):
                pesan_error = f'Gagal! Jadwal ini bentrok dengan jadwal mengajar {j.mata_kuliah_id.name} milikmu.'
                return {'status': 'error', 'pesan': pesan_error}

        self.write({'asisten_ids': [(4, student_id.id)]})
        return {'status': 'success', 'pesan': 'Alokasi Jadwal Berhasil!'}