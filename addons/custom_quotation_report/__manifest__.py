{
    'name': 'Custom Quotation Report',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Customized Quotation Report for Odoo 17',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        'report/sale_quotation_template.xml',
        'report/sale_quotation_report.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}