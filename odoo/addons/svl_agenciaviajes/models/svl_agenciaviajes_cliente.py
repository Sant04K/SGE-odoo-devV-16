from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'svl_agenciaviajes.cliente'
    
    name = fields.Char(string="Nombre del Cliente", required=True)
    
    viaje_ids = fields.One2many(
        'svl_agenciaviajes.viaje', 
        'cliente_id',               
        string="Viajes Contratados"
    )
    
    viaje_count = fields.Integer(string="Nº de Viajes", compute="_compute_viaje_count")

    @api.depends('viaje_ids')
    def _compute_viaje_count(self):
        for record in self:
            record.viaje_count = len(record.viaje_ids)