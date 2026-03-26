# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        compute='_compute_currency_id',
        store=True,
        readonly=True,
    )

    @api.depends('employee_id', 'employee_id.currency_id', 'company_id')
    def _compute_currency_id(self):
        for payslip in self:
            payslip.currency_id = (
                payslip.employee_id.currency_id
                or payslip.company_id.currency_id
            )

    def _get_account_move_values(self):
        res = super()._get_account_move_values()
        if self.currency_id:
            res['currency_id'] = self.currency_id.id
        return res

    def _get_moved_lines_vals(self):
        res = super()._get_moved_lines_vals()
        if self.currency_id and self.currency_id != self.company_id.currency_id:
            date = self.date_to or fields.Date.today()
            for line_vals in res:
                amount = line_vals.get('debit', 0) - line_vals.get('credit', 0)
                line_vals['amount_currency'] = self.company_id.currency_id._convert(
                    amount,
                    self.currency_id,
                    self.company_id,
                    date,
                )
                line_vals['currency_id'] = self.currency_id.id
        return res
