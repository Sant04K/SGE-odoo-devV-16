#-*- coding: utf-8 -*-
from odoo import models, fields

class Destino(models.Model):
    
    _name = 'svl_agenciaviajes.destino'
    _description = 'Destinos de Viajes'

    name = fields.Char(string='Continente', help="Introducir el continente del destino", required=True)
    pais = fields.Char(string='País', help="Introducir pais de destino", required=True)
    ciudad = fields.Char(string='Ciudad', help="Introducir la ciudad de destino", required=True)

    imagen = fields.Image(string='Imagen del Destino', max_width=800, max_height=600)
    
    cliente_ids = fields.Many2many(
    'svl_agenciaviajes.cliente', 
    'rel_clientes_destinos',
    'destino_id', 
    'cliente_id', 
    string='Clientes Interesados'
    )