from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'svl_agenciaviajes.wizard'
    _description = 'Asistente para modificar el numero de telefono de clientes'

    new_num_telefono = fields.Char(string='Nuevo número', required=True)
    cliente_ids = fields.Many2many('svl_agenciaviajes.cliente', string='Clientes', required=True)

    @api.model
    def default_get(self, fields_list):
        res = super(Wizard, self).default_get(fields_list)
        active_ids = self.env.context.get('active_ids', [])
        res['cliente_ids'] = [(6, 0, active_ids)]
        return res
    
    def apply_changes(self):
        self.cliente_ids.write({'telefono': self.new_num_telefono})


    