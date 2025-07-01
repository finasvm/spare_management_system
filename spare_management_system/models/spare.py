from odoo import models, fields


class Spare(models.Model):
    _name = 'spare.part'
    _description = 'Spare Parts'
    _rec_name='brand'

    brand = fields.Char(string='Brand', required=True)
    part_number = fields.Integer( string='CODE', required=True)
    part_name = fields.Char(string='Part Name')
    description = fields.Char(string='Description')
