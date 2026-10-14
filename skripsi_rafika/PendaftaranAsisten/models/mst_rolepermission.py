# 8. mst_rolepermisson.py
# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields 

class MstRolePermission(models.Model):
    _name = 'mst_rolepermission'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Master Role Permission'

    id_master_role_permission = fields.Char('Id Master Role Permission', required=True, tracking=True)
    role_id = fields.Many2one('res.groups', 'Role', required=True, tracking=True)
    create_perm = fields.Boolean('Create', tracking=True)
    read_perm = fields.Boolean('Read', tracking=True)
    update_perm = fields.Boolean('Update', tracking=True)
    delete_perm = fields.Boolean('Delete', tracking=True)
    view_perm = fields.Boolean('View', tracking=True)

    _sql_constraints = [
        ('unique_id_master_role_permission', 'unique(id_master_role_permission)', 'Id Master Role Permission harus unik!'),
    ]