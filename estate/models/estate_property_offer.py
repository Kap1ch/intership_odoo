from datetime import timedelta

from odoo import fields, models, api
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers"

    price = fields.Float(required=True)
    status = fields.Selection([('accepted', 'Accepted'),
                               ('refused', 'Refused')], copy=False)

    validity_days = fields.Integer(default=7)
    deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline", store=True)
    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    @api.depends('create_date', 'validity_days')
    def _compute_deadline(self):
        for offer in self:
            if offer.deadline:
                offer.deadline = offer.create_date + timedelta(days=offer.validity_days)
            else:
                offer.deadline = fields.Date.today() + timedelta(days=offer.validity_days)

    def _inverse_deadline(self):
        for offer in self:
            if offer.deadline and offer.create_date:
                delta = offer.deadline - offer.create_date.date()
                offer.validity_days = delta.days

    # def action_accept_offer(self):
    #     for record in self:
    #         if record.status == 'accepted':
    #             raise UserError("This offer has already been accepted.")
    #         record.status = 'accepted'
    #         record.property_id.write({
    #             'selling_price': record.price,
    #             'buyer_id': record.partner_id.id,
    #             'state': 'offer_accepted'
    #         })
    #     return True
    #
    # def action_refuse_offer(self):
    #     for record in self:
    #         if record.status == 'accepted':
    #             raise UserError("Cannot refuse an accepted offer.")
    #         record.status = 'refused'
    #     return True
    def action_accept_offer(self):
        for record in self:
            property = record.property_id
            if property.state != 'offer_received':
                raise UserError('You can only accept an offer if it is in the "Offer Received" state.')
            record.status = 'accepted'
            property.write({
                'state': 'offer_accepted',
                'selling_price': record.price,
                'buyer_id': record.partner_id.id
            })

    def action_refuse_offer(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError('You cannot refuse an accepted offer.')
            record.status = 'refused'