# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HR Payroll - Custom Currency',
    'version': '19.0.1.1.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Allow defining a custom currency on employee contracts for payroll',
    'description': """
HR Payroll - Custom Contract Currency
======================================

This module allows defining a custom currency per employee contract,
instead of always using the company's default currency.

Features:
- Editable currency field on the employee's Payroll tab
- Defaults to the company currency but can be overridden
- Payslip amounts computed in the contract currency
- Worked days amounts use the contract currency
- Accounting journal entries created in the contract currency
- Multi-currency support leverages Odoo's native exchange rate handling
    """,
    'depends': ['hr_payroll'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
