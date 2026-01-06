#-*- coding: utf-8 -*-
from odoo import models, fields


class Viaje(models.Model):
    _name = 'sge_agenciaviajes.viaje'
    _description = 'Gestion de Viajes'

    name = fields.Char(string='Nombre', help="Introducir nombre del viaje", required=True)
    precio = fields.Float(string='Precio')
    destino = fields.Char(string='Destino') 
    
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_fin = fields.Date(string='Fecha Fin')
    state = fields.Selection([
        ('planificacion', 'Planificacion'),
        ('abierto', 'Abierto'),
        ('en_curso', 'En Curso'),
        ('finalizado', 'Finalizado'),
    ], string='Estado', default='planificacion')