from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'svl_agenciaviajes.cliente'
    _description = 'Clientes de la Agencia de Viajes'
    
    name = fields.Char(string="Nombre del Cliente", required=True)
    apellidos = fields.Char(string="Apellidos del Cliente", required=True)
    email = fields.Char(string="Correo Electrónico", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    
    viaje_ids = fields.One2many(
        'svl_agenciaviajes.viaje', 
        'cliente_id',               
        string="Viajes Contratados"
    )
    
    destino_ids = fields.Many2many(
    'svl_agenciaviajes.destino', 
    'rel_clientes_destinos',     
    'cliente_id',                
    'destino_id',                
    string='Destinos de Interés'
    )

    viaje_count = fields.Integer(string="Nº de Viajes", compute="_compute_viaje_count")

    @api.depends('viaje_ids')
    def _compute_viaje_count(self):
        for record in self:
            record.viaje_count = len(record.viaje_ids)