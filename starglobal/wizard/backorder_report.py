'''
Created on Feb 4, 2021

@author: nang-pwint
'''
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class expense_report(models.Model):
    _name = 'backorder.report.template'    
    type = fields.Selection([
        ('customer', 'Customers'),
        ('vendor', 'Vendors'),
    ], string='Type', default='customer', track_visibility='onchange')
    
    is_cus = fields.Boolean(string="is_customer?", default=False)
    is_vendors = fields.Boolean(string="is_vendor?",  default=False)
    
    cus_id = fields.Many2one("res.partner",string="Customers")
    vendor_id = fields.Many2one("res.partner",string="Vendors")    
    sale_order = fields.Many2many("sale.order",string="Sales Order")
    purchase_order = fields.Many2many("purchase.order",string="Purchase Order")
    
    @api.onchange('cus_id','vendor_id','type')
    def _onchange_project(self):
        for data in self:
            if self.type == 'customer' and self.cus_id is not False:
                stock_picking_obj = self.env['stock.picking'].search([('partner_id', '=', data.cus_id.id),('backorder_id','!=',False),('state','!=','done')]).ids   
                for item in stock_picking_obj: 
                    sales_obj = self.env['sale.order'].search([('picking_ids', '=', item)])
                    for obj in sales_obj:
                        self.sale_order = [(4, obj.id)]
            if self.type == 'vendor' and self.vendor_id is not False:
                print (' purchase order')
                stock_picking_obj = self.env['stock.picking'].search([('partner_id', '=', data.vendor_id.id),('backorder_id','!=',False),('state','!=','done')]).ids   
                print('stock picking obj>',stock_picking_obj)
                for item in stock_picking_obj: 
                    purchase_obj = self.env['purchase.order'].search([('picking_ids', '=', item)])
                    for obj in purchase_obj:
                        self.purchase_order = [(4, obj.id)]
                    print('self.purchase_order>>',self.purchase_order)
    
    def _get_name(self):
        print ('reatch get name')
        return self.cus_id.name
    
    '''for expense advance print'''
    def _get_data_from_order_report(self, data):
        res = []
        total = 0
        backorder_data =self.env['backorder.report.template'].search([('id','=',self.id)]) 
        res.append({'data':[]})
        
        if self.type == 'customer' and self.cus_id is not False:
            for sales_order_data in backorder_data.sale_order:
                total = 0
                for delivery_order in sales_order_data.picking_ids:  
                    if delivery_order.backorder_id != False and delivery_order.state != 'done':
                        tmp_date = delivery_order.scheduled_date
                
                for order_line in sales_order_data.order_line:   
                    tmp_alloc= order_line.product_uom_qty - order_line.qty_delivered           
                    res[0]['data'].append({
                            'customer':sales_order_data.partner_id.name,
                            'sale_order': sales_order_data.name,
                            'order_date':sales_order_data.date_order.date(),
                            'order_code':order_line.product_id.default_code,
                            'qty_order':order_line.product_uom_qty,
                            'qty_ship':order_line.qty_delivered,
                            'qty_alloc':tmp_alloc,
                            'qty_pend': tmp_alloc,
                            'sales_price':order_line.price_unit,
                            'ship_date':sales_order_data.expected_date.date(),
                            'delivery_date':tmp_date.date(),
                            })
                    
        if self.type == 'vendor' and self.vendor_id is not False:
            print ('pruchase order')
            for sales_order_data in backorder_data.purchase_order:
                total = 0
                for delivery_order in sales_order_data.picking_ids:  
                    if delivery_order.backorder_id != False and delivery_order.state != 'done':
                        tmp_date = delivery_order.scheduled_date
                
                for order_line in sales_order_data.order_line:   
                    
                    tmp_alloc= order_line.product_uom_qty - order_line.qty_received
                    total += order_line.price_unit * tmp_alloc
                    res[0]['data'].append({
                            'customer':sales_order_data.partner_id.name,
                            'sale_order': sales_order_data.name,
                            'order_date':sales_order_data.date_order.date(),
                            'order_code':order_line.product_id.default_code,
                            'qty_order':order_line.product_uom_qty,
                            'qty_ship':order_line.qty_received,
                            'qty_alloc':tmp_alloc,
                            'qty_pend': tmp_alloc,
                            'sales_price':order_line.price_unit,
                            'ship_date':sales_order_data.date_approve.date(),
                            'delivery_date':tmp_date.date(),
                            })
            
        print('res>>>',res)
        return res
                   
    def _get_backorder_report_values(self, docids, data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
  
        order_report = self.env['ir.actions.report']._get_report_from_name('myanmar-star-global.action_report_backorder_template')
        return {
            'doc_ids': self.ids,
            'doc_model': order_report.model,
            'get_data_from_order_report': self._get_data_from_order_report(data['form']),
        }
    
    def print_backorder_report_template(self):
        self.ensure_one()
        [data] = self.read()    
        self.advance_Obj=self.env['backorder.report.template'].search([('id','=',self.id)]) 
        datas = {
            'ids': [],
            'model': 'backorder.report.template',
            'form': data,
        }
        return self.env.ref('myanmar-star-global.action_report_backorder_template').report_action(self,data=self._get_backorder_report_values(self,data=datas))
    
