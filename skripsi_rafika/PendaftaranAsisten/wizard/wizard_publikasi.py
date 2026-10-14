# pyrefly: ignore [missing-import]
from odoo import models, fields, api

class WizardPublikasiHasil(models.TransientModel):
    _name = 'wizard.publikasi.hasil'
    _description = 'Wizard Publikasi Hasil Seleksi'

    # Relasi ke form Master Periode (dipanggil dari mst_periodesemt)
    periode_id = fields.Many2one('mst_periodesemt', string="Periode", default=lambda self: self.env.context.get('active_id'))

    def action_konfirmasi_publikasi(self):
        # 1. Cari pendaftaran yang lolos
        pendaftaran_lolos = self.env['registrasi.asprak'].search([
            ('periode_semester_id', '=', self.periode_id.id),
            ('state', '=', 'lolos')
        ])

        # 2. Ambil XML ID dari grup role yang dibutuhkan
        ta_group = self.env.ref('PendaftaranAsisten.group_asisten_praktikum', raise_if_not_found=False)
        portal_group = self.env.ref('base.group_portal', raise_if_not_found=False)
        internal_group = self.env.ref('base.group_user', raise_if_not_found=False)

        if ta_group and portal_group and internal_group:
            for reg in pendaftaran_lolos:
                user = reg.mahasiswa_id.user_id
                if user:
                    # KUNCI PERBAIKAN:
                    # Odoo melarang 1 akun punya 2 tipe user (Portal & Internal) bersamaan.
                    # Maka kita harus cabut grup Portal (3), lalu pasang grup Internal & TA (4).
                    # sudo() memastikan Laboran bisa mengeksekusi ini tanpa terhalang hak akses.
                    user.sudo().write({
                        'groups_id': [
                            (3, portal_group.id),    # Cabut akses Portal
                            (4, internal_group.id),  # Berikan akses Internal User (Syarat Odoo)
                            (4, ta_group.id)         # Berikan Role Teaching Assistant
                        ]
                    })

        # Close the wizard
        return {'type': 'ir.actions.act_window_close'}