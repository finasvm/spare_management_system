from odoo import models, fields


class Spare(models.Model):
    _name = 'spare.part'
    _description = 'Spare Parts'
    _rec_name='brand'

    brand = fields.Char(string='Brand', required=True)
    part_number = fields.Integer( string='CODE', required=True)
    part_name = fields.Char(string='Part Name')
    description = fields.Char(string='Description')
    model_name=fields.Many2one("vehicle.info","Vehicle")
    unit_of_measure=fields.Integer("UOM")
    cost_price=fields.Integer("Cost Price")
    sale_price=fields.Integer("Sales Price")
    whole_sale_price=fields.Integer("Whole SalePrice")
    image=fields.Binary("Image")


