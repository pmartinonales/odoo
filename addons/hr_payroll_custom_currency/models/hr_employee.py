# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # New editable field following the exact _inherits pattern
    # used by contract_type_id, structure_type_id, etc.
    contract_currency_id = fields.Many2one(
        readonly=False,
        related='version_id.contract_currency_id',
        inherited=True,
        groups="hr.group_hr_manager",
    )
