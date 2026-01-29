# -*- coding: utf-8 -*-
{
    'name': "svl_agenciaviajes",

    'summary': "Gestiona una agencia de viajes",

    'description': """
Gestiona una agencia de viajes, permitiendo llevar el control de los clientes, viajes y reservas.
    """,

    'author': "Santos Valdivielso",
    'website': "https://github.com/Sant04K",
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.3.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        

    #Importante que el "menus.xml" esté antes que las vistas para que se creen los menús correctamente
        'views/svl_agenciaviajes_viaje.xml',
        'views/svl_agenciaviajes_destino.xml',
        'views/svl_agenciaviajes_temporada.xml',
        'views/svl_agenciaviajes_cliente.xml',

    #Wizard
        'views/svl_agenciaviajes_wizard.xml',

    #Menu
        'views/svl_agenciaviajes_menu.xml',

    #Informes
        'reports/report_cliente.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

