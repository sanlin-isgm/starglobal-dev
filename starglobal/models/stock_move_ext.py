from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
from datetime import date, timedelta


class StockMoveExt(models.Model):
       
    _inherit = 'stock.move'
    
    remarks = fields.Char('Remarks', store = True)
    
    
class StockPickingExt(models.Model):
    
    _inherit = 'stock.picking'
    
    ti_number = fields.Char('TI Ref No' , store = True)
    received_by = fields.Char('Received By',index = True)
    received_date = fields.Date('Received Date')
    delivered_by = fields.Char('Delivered By',index = True)
    delivered_date = fields.Date('Delivered Date')
