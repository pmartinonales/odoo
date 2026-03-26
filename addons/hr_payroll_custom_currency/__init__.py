# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models


def _post_init_hook(env):
    """Populate contract_currency_id for existing hr.version records."""
    env.cr.execute("""
        UPDATE hr_version v
        SET contract_currency_id = c.currency_id
        FROM res_company c
        WHERE v.company_id = c.id
        AND v.contract_currency_id IS NULL
    """)
