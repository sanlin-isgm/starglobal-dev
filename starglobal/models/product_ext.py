'''
Created on Jan 27, 2021

@author: isgm232
'''
from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare


class ProductExt(models.Model):
       
    _inherit = 'product.product'
    
    nt_weight = fields.Float('Net Weight')
    gr_weight = fields.Float('GR Weight')
    dimension = fields.Float('Dimension')
