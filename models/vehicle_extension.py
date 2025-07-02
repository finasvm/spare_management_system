from odoo import models, fields

class VehicleType(models.Model):
    _name = 'vehicle.type'
    _description = 'Vehicle Type'

    name = fields.Char(required=True)


class VehicleMake(models.Model):
    _name = 'vehicle.make'
    _description = 'Vehicle Make'

    name = fields.Char(required=True)
