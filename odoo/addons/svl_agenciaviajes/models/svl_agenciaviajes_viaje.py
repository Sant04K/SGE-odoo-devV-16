# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields, api

class Viaje(models.Model):
    _name = 'svl_agenciaviajes.viaje'
    _description = 'Gestion de Viajes'

    name = fields.Char(string='Nombre', help="Introducir nombre del viaje", required=True)
    precio = fields.Float(string='Precio')
    
    destino_id = fields.Many2one('svl_agenciaviajes.destino', string='Destino') 
    cliente_id = fields.Many2one('svl_agenciaviajes.cliente', string='Cliente', required=True)

    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_fin = fields.Date(string='Fecha Fin')
    
    state = fields.Selection([
        ('planificacion', 'Planificacion'),
        ('abierto', 'Abierto'),
        ('en_curso', 'En Curso'),
        ('finalizado', 'Finalizado'),
    ], string='Estado', _compute="compute_state", store="True", default='planificacion')

    destino_id = fields.Many2one('svl_agenciaviajes.destino', string='Destino')

    duracion = fields.Integer(string='Duración (Días)', compute='_compute_duracion')

    @api.depends('fecha_inicio', 'fecha_fin')
    def _compute_duracion(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                diferencia = record.fecha_fin - record.fecha_inicio
                record.duracion = diferencia.days
            else:
                record.duracion = 0

    @api.depends('fecha_inicio', 'fecha_fin')
    def _compute_state(self):
        today = date.today() 
        for record in self:
            if not record.fecha_fin:
                record.state = 'planificacion'
                continue

            if today < record.fecha_inicio:
                record.state = 'abierto'
            elif record.fecha_inicio <= today <= record.fecha_fin:
                record.state = 'en_curso'
            elif today > record.fecha_fin:
                record.state = 'finalizado'