#-*- coding: utf-8 -*-
from odoo import models, fields

class temporada(models.Model):
    _name = 'svl_agenciaviajes.temporada'
    _description = 'Temporada del viaje'

    _rec_name = 'state'
    
    state = fields.Selection([
        ('alta', 'Alta'),
        ('baja', 'Baja'),
        ('oportunidad', 'Oportunidad'),
    ], string='Estado', required=True)

    temporada_id = fields.Many2one('svl_agenciaviajes.temporada', string='Temporada')

