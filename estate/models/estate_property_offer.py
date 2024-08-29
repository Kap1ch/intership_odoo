from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers"

    price = fields.Float(required=True)
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)