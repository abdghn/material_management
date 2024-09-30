# material_management/models/material.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material'
    _description = 'Material Registration'

    code = fields.Char('Material Code', required=True)
    name = fields.Char('Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string='Material Type', required=True)
    buy_price = fields.Float('Material Buy Price', required=True)
    supplier_id = fields.Many2one(
        'res.partner',
        string='Related Supplier',
        domain=[('supplier_rank', '>', 0)],
        required=True
    )

    @api.constrains('buy_price')
    def _check_buy_price(self):
        if any(record.buy_price < 100 for record in self):
            raise ValidationError('Material buy price must be at least 100.')
