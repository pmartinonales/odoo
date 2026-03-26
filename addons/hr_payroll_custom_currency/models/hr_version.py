# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HrVersion(models.Model):
    _inherit = 'hr.version'

    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        compute='_compute_currency_id',
        store=True,
        readonly=False,
        precompute=True,
        tracking=True,
    )

    @api.depends('company_id')
    def _compute_currency_id(self):
        for version in self:
            if not version.currency_id:
                version.currency_id = version.company_id.currency_id
