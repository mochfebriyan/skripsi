# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, api
# pyrefly: ignore [missing-import]
from odoo.exceptions import AccessError

class ResUsers(models.Model):
    _inherit = 'res.users'

    def write(self, vals):
        if 'groups_id' in vals:
            pimpinan_group = self.env.ref('PendaftaranAsisten.group_lab_pimpinan', raise_if_not_found=False)
            
            if pimpinan_group:
                is_pimpinan_or_superuser = self.env.is_superuser() or self.env.user.has_group('PendaftaranAsisten.group_lab_pimpinan')
                
                if not is_pimpinan_or_superuser:
                    for command in vals.get('groups_id', []):
                        if command[0] == 4 and command[1] == pimpinan_group.id:
                            raise AccessError("Otoritas ditolak. Anda tidak memiliki izin untuk memodifikasi hierarki role tingkat Pimpinan.")
                        elif command[0] == 6 and pimpinan_group.id in command[2]:
                            for user in self:
                                if pimpinan_group not in user.groups_id:
                                    raise AccessError("Otoritas ditolak. Anda tidak memiliki izin untuk memodifikasi hierarki role tingkat Pimpinan.")
                                
        return super(ResUsers, self).write(vals)
