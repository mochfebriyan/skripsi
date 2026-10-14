# -*- coding: utf-8 -*-
# pyrefly: ignore [missing-import]
from odoo import models, fields, api    
# pyrefly: ignore [missing-import]
from odoo.exceptions import ValidationError


class AssistantPlanning(models.Model):
    _name = 'assistant.planning'
    _description = 'Perencanaan Kuota Asisten Praktikum'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Nomor Perencanaan',
        readonly=True,
        default='New',
        copy=False,
        tracking=True,
    )

    # Associate method: Many2one ke tabel mst_coursesemt yang sudah ada
    course_id = fields.Many2one(
        comodel_name='mst_coursesemt',
        string='Mata Kuliah',
        required=True,
        tracking=True,
    )

    assistant_quota = fields.Integer(
        string='Kuota Asisten',
        required=True,
        default=1,
        tracking=True,
    )

    kaprodi_id = fields.Many2one(
        'res.users', 
        string='Kaprodi (Pengaju)', 
        default=lambda self: self.env.user, 
        readonly=True 
    )

    kalab_id = fields.Many2one(
        comodel_name='res.users',
        string='Diinput/Ditetapkan Oleh',
        readonly=True,
        tracking=True,
    )

    state = fields.Selection(
        selection=[
            ('draft', 'Pengajuan (Draft)'),
            ('final', 'Ditetapkan (Final)'),
        ],
        string='Status',
        default='draft',
        tracking=True,
    )

    # =========================================================================
    # OVERRIDE CREATE: Auto-generate sequence number
    # =========================================================================
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == 'New':
                vals['name'] = (
                    self.env['ir.sequence'].next_by_code('assistant.planning.seq') or 'New'
                )
        return super().create(vals_list)

    # =========================================================================
    # ACTION: Tetapkan ke status Final
    # =========================================================================
    def action_set_final(self):
        for rec in self:
            if rec.assistant_quota <= 0:
                raise ValidationError(
                    "Kuota Asisten harus lebih dari 0 sebelum dapat ditetapkan!"
                )
            rec.kalab_id = self.env.user.id
            rec.state = 'final'
