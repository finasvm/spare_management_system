from odoo import models, fields


class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _rec_name="name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char("Vehicle Name",requied="true")
    type=fields.Char("Vehicle Type")
    make=fields.Char("Make")
    model=fields.Char("Model")
    year=fields.Date("Year")

