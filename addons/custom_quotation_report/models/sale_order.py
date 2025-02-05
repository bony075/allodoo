from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    quotation_serial_no = fields.Char(string='Quotation Serial No.')
    revised_no = fields.Char(string='Revised No.')
