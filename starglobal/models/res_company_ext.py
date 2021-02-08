from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare


class ResCompanyExt(models.Model):
       
    _inherit = "res.company"
    
    showroom_address = fields.Text( string='Branch Showroom Address', index=True)
    
class ResPartnersExt(models.Model):
       
    _inherit = "res.partner"
    
    fax = fields.Char(string='Fax', index=True)
    