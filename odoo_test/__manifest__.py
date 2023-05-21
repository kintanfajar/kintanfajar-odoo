# -*- coding: utf-8 -*-
{
    'name': "Modul Odoo Test",

    'summary': """
        Materials""",

    'description': """
        Untuk regitrasi material
    """,

    'author': "Kintan Fajarwati",
    'website': "http://www.yourcompany.com",
    'category': 'Custom',
    'version': '0.1',

    'depends': ['base','website'],

    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/templates.xml',
    ],
}