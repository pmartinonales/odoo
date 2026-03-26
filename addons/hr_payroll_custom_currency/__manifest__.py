# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HR Payroll - Custom Currency',
    'version': '19.0.3.0.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Allow defining a custom currency on employee contracts',
    'description': """
HR Payroll - Custom Contract Currency
======================================

Adds an editable Contract Currency field to the employee's Payroll tab.
Installable via zip import (data-only module).
    """,
    'depends': ['hr_payroll'],
    'data': [
        'data/ir_model_fields.xml',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
