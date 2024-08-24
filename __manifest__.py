# -*- coding: utf-8 -*-
{
    'name': "odoo_japan",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Juan José Seguí",
    'website': "https://www.juanjosegui.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/models.xml',
        'security/ir.model.access.csv',
        'views/compras_japon_views.xml',
        'views/envios_japon_views.xml',
        'views/ventas_espana_views.xml',
        'views/templates.xml',
        'views/action_odoo_japan.xml',
    ],
    'installable': True,
    'application': True,
}
