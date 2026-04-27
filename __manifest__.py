{
    'name': 'HR Hospital',
    'summary':'Hospital menagement system',
    'version': '19.0.1.0.0',
    'author': 'cuxoy',
    'website': 'https://www.odoo.com',
    'category': 'Services',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': []
    },

    'data': [
    'security/ir.model.access.csv',

    'data/disease_data.xml',

    'views/doctor_views.xml',
    'views/patient_views.xml',
    'views/disease_views.xml',
    'views/visit_views.xml',
    'views/hr_hospital_menu.xml',
],
    'demo': ['demo/demo_data.xml',
],
    'installable': True,
    'application': True,
    'auto_install': False,
}