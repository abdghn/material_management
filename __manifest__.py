# material_management/__manifest__.py
{
    'name': 'Material Management',
    'version': '1.0',
    'summary': 'Module to manage materials for sale',
    'author': 'Your Name',
    'depends': ['base', 'contacts', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/material_views.xml',
        'views/templates.xml',
        'data/data.xml',  # Jika ada data tambahan
    ],
    'assets': {
        'point_of_sale.assets': [
            'material_management/static/src/js/pos_customizations.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
