# -*- coding: utf-8 -*-
{
    'name': "abc_x_sicurezzalab",

    'summary': """ Modulo che aggiunge il campo Sede all'interno del modulo Task, il quale permette di scegliere uno tra gli indirizzi del Cliente selezionato nel Task. """,

    'description': """
        Modulo che aggiunge il campo Sede all'interno del modulo Task, il quale permette di scegliere uno tra gli indirizzi del Cliente selezionato nel Task.
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['documents_project', 'project', 'project_enterprise', 'sale_project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
