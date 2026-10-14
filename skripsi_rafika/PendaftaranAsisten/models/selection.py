# -*- coding: utf-8 -*-
from odoo import models, fields

class AsprakSelection(models.Model):
    _inherit = 'asprak.selection'

    skep_file = fields.Binary(string='File SKEP Rektor', attachment=True)
    skep_filename = fields.Char(string='Nama File SKEP')
    
    # Alias to fulfill QWeb requirement selection.state
    state = fields.Selection(related='status_seleksi', store=False)
