# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    currency_id = fields.Many2one(
        'res.currency',
        related='version_id.currency_id',
        readonly=False,
        groups="hr.group_hr_user",
    )
