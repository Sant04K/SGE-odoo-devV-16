# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields, api

class Viaje(models.Model):
    _name = 'svl_agenciaviajes.viaje'
    _description = 'Gestion de Viajes'

    name = fields.Char(string='Nombre', help="Introducir nombre del viaje", required=True)
    
    precio_base = fields.Float(string='Precio Base', help="Introducir el precio base del viaje", required=True)
    
    precio_total = fields.Float(
        string='Precio Final', 
        compute='_compute_precio_total', 
        store=True
    )

    destino_id = fields.Many2one('svl_agenciaviajes.destino', string='Destino', required=True) 
    cliente_id = fields.Many2one('svl_agenciaviajes.cliente', string='Cliente', required=True)
    temporada_id = fields.Many2one('svl_agenciaviajes.temporada', string='Temporada Seleccionada', required=True)

    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_fin = fields.Date(string='Fecha Fin')
    
    state = fields.Selection([
        ('planificacion', 'Planificacion'),
        ('abierto', 'Abierto'),
        ('en_curso', 'En Curso'),
        ('finalizado', 'Finalizado'),
    ], string='Estado', compute="_compute_state", store=True, default='planificacion')

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
            if not record.fecha_inicio or not record.fecha_fin:
                record.state = 'planificacion'
                continue

            if today < record.fecha_inicio:
                record.state = 'abierto'
            elif record.fecha_inicio <= today <= record.fecha_fin:
                record.state = 'en_curso'
            else:
                record.state = 'finalizado'

    @api.depends('precio_base', 'temporada_id.state')
    def _compute_precio_total(self):
        for record in self:
            if record.precio_base and record.temporada_id:
                
                if record.temporada_id.state == "alta":  
                    record.precio_total = record.precio_base * 1.20
                elif record.temporada_id.state == "oportunidad":
                    record.precio_total = record.precio_base * 0.85
            else:
                record.precio_total = record.precio_base