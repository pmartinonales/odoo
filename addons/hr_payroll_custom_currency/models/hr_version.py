# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrVersion(models.Model):
    _inherit = 'hr.version'

    contract_currency_id = fields.Many2one(
        'res.currency',
        string="Contract Currency",
        default=lambda self: self.env.company.currency_id,
        required=True,
        tracking=True,
    )

    # Override currency_id to follow contract_currency_id
    # so all Monetary fields (wage, contract_wage) use the contract currency
    currency_id = fields.Many2one(
        related='contract_currency_id',
    )
