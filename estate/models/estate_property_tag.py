from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tags"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('check_unique_tag_name',
         'UNIQUE(name)',
         'Property tag name must be unique.')
    ]