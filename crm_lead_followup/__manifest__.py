# -*- coding: utf-8 -*-
{
    'name': "crm_lead_follow_up",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mohamed Essam",
    'website': "https://www.linkedin.com/in/mohammed-essam-988199177/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'crm'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
