'''
Created on Jan 26, 2021

@author: isgm232
'''
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo import api, exceptions, fields, models, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_compare, float_is_zero
from collections import defaultdict
from odoo.tools.misc import formatLang, format_date, get_lang
from datetime import date, timedelta
from odoo.tools.misc import DEFAULT_SERVER_DATE_FORMAT, format_date
from docutils.nodes import Invisible
import time

class account_move_ext(models.Model):
    _inherit = 'stock.quant.package'
    
    packing_date = fields.Date('Packing Date')
    packing_remark = fields.Char()
    packing_vol_m3 = fields.Float()
    
    def action_view_picking_ext(self):
        domain = ['|', ('result_package_id', 'in', self.ids), ('package_id', 'in', self.ids)]
        pickings = self.env['stock.move.line'].search(domain).mapped('picking_id')
        return pickings

class stock_picking_ext(models.Model):
    _inherit = 'stock.move.line'
    
    total_kg_net = fields.Float('Net Weight')
    total_kg_gross = fields.Float('Gross Weight')
    dimension = fields.Float('Dimension')

    


    
    
    
    