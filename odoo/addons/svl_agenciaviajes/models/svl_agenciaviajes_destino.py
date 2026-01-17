#-*- coding: utf-8 -*-
from odoo import models, fields

class Destino(models.Model):
    
    # AQUÍ ES DONDE MANTIENES EL NOMBRE TÉCNICO DEL MODELO RECUERDA EL .DESTINO
    _name = 'svl_agenciaviajes.destino'
    _description = 'Destinos de Viajes'

    name = fields.Char(string='Continente', help="Introducir el continente del destino", required=True)
    pais = fields.Char(string='País', help="Introducir pais de destino", required=True)
    ciudad = fields.Char(string='Ciudad', help="Introducir la ciudad de destino", required=True)

    #Campo para almacenar una imagen del destino
    imagen = fields.Image(string='Imagen del Destino', max_width=800, max_height=600)