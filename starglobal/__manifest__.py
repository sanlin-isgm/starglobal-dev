# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Myanmar Star Group Odoo13 Enterprise',
    'version': '1.0',
    'category': 'Myanmar Star Group',
    'sequence': 75,
    'summary': 'Myanmar Star Group Odoo13e',
    'description': """

You can manage:
---------------
    """,
    'website': '',
    'images': [
      
    ],
    
    'depends': [          
        'base_setup', 'crm', 'stock', 'account', 'sale_management', 'purchase', 'hr_expense', 'web', 'account_accountant'
    ],
    'data': [
            'security/ir.model.access.csv',
            'report/backorder_report.xml',
            'report/backorder_template.xml',
            'wizard/backorder_summary_view.xml',
            'report/delivery_report_template.xml',
            'views/sales_ext_view.xml',
            'views/res_company_ext_view.xml',
            'views/stock_ext_view.xml',
            'report/quotation_report_template.xml',
            'report/invoice_report_template.xml',
            'report/payment_receipt_report_template.xml',
            'report/packing_list_report_template.xml',
            'views/stock_quant_ext_views.xml',
            'views/payment_ext_view.xml',
            
           
    ],
    'demo': [],
    'test': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [
        ],
    'css': [
        ],
}
