from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
from datetime import date, timedelta
from num2words import num2words

class PaymentExt(models.Model):
       
    _inherit = 'account.payment'
    
    remark = fields.Char('Remark', index = True)
    acknowledge = fields.Text( string='Acknowledgement', index = True)
    paid_by = fields.Char('Paid By', required = True , index = True)
    paid_date = fields.Date('Paid Date')
    collected_by = fields.Char('Collected By', required = True , index = True)
    collected_date = fields.Date('Collected Date')
    
    
    def get_kyat_explanation(self,amount):
        new_amount=num2words(amount,lang='en')
        return new_amount
    
    def get_invoice(self):        
        invoices = self.env['account.move'].search([('id', '=', self.reconciled_invoice_ids.ids)]) 
        
        return invoices
    
    def get_pi(self):     
        result_list = []   
        invoices = self.env['account.move'].search([('id', '=', self.reconciled_invoice_ids.ids)]) 
        print(invoices)
        for inv in invoices:
            pi_list = inv.invoice_origin
            result_list.append(pi_list)
            pi_concat_list = str(result_list).replace("'", "")[1:-1]
        return pi_concat_list
    
    
    
    