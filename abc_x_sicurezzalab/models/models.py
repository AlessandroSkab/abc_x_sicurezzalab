# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_x_sicurezzalab(models.Model):
     _name = 'abc_x_sicurezzalab.abc_x_sicurezzalab'
     _description = 'abc_x_sicurezzalab.abc_x_sicurezzalab'
    
class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"
    


    sede = fields.Many2one('res.partner', string="Sede", domain="['|',('id','=', partner_id), ('parent_id', '=', partner_id)]", change_default=True, index=True, tracking=1)