# -*- coding: utf-8 -*-
{
    'name': "sge_agenciaviajes",

    'summary': "Gestiona una agencia de viajes",

    'description': """
Gestiona una agencia de viajes, permitiendo llevar el control de los clientes, viajes, reservas y pagos.
    """,

    'author': "Santos Valdivielso",
    'website': "https://github.com/Sant04K",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

    #Importante que el "menus.xml" esté antes que las vistas para que se creen los menús correctamente
        'views/sge_agenciaviajes_menus.xml',
        'views/sge_agenciaviajes_viaje.xml',
        'views/sge_agenciaviajes_destino.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

