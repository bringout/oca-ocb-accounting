from odoo import api, SUPERUSER_ID


def _table_has_column(cr, table, column):
    cr.execute(
        """
        SELECT 1
          FROM information_schema.columns
         WHERE table_name = %s AND column_name = %s
        """,
        (table, column),
    )
    return bool(cr.fetchone())


def migrate(cr, version):
    if not version:
        return

    env = api.Environment(cr, SUPERUSER_ID, {})

    # Initialise new company lock fields using existing lock dates.
    companies = env['res.company'].with_context(active_test=False).search([])
    for company in companies:
        vals = {}
        if not company.sale_lock_date and company.period_lock_date:
            vals['sale_lock_date'] = company.period_lock_date
        if not company.purchase_lock_date and company.period_lock_date:
            vals['purchase_lock_date'] = company.period_lock_date
        if not company.hard_lock_date and company.fiscalyear_lock_date:
            vals['hard_lock_date'] = company.fiscalyear_lock_date
        if vals:
            company.sudo().write(vals)

    # If account_move_export is installed, migrate configuration defaults.
    if env.registry.get('account.move.export.config'):
        # Ensure new boolean fields are not left NULL and join_char has a value.
        cr.execute(
            """
            UPDATE account_move_export_config
               SET group_lines = COALESCE(group_lines, FALSE),
                   lock_tax = COALESCE(lock_tax, FALSE),
                   lock_sale = COALESCE(lock_sale, FALSE),
                   lock_purchase = COALESCE(lock_purchase, FALSE),
                   lock_fiscalyear = COALESCE(lock_fiscalyear, FALSE),
                   lock_hard = COALESCE(lock_hard, FALSE),
                   join_char = COALESCE(NULLIF(join_char, ''), '-')
            """
        )

        if _table_has_column(cr, 'account_move_export_config', 'lock'):
            cr.execute(
                """
                UPDATE account_move_export_config
                   SET lock_tax = lock_tax OR lock IN ('tax', 'period', 'fiscalyear'),
                       lock_sale = lock_sale OR lock IN ('period', 'fiscalyear'),
                       lock_purchase = lock_purchase OR lock IN ('period', 'fiscalyear'),
                       lock_fiscalyear = lock_fiscalyear OR lock = 'fiscalyear',
                       lock_hard = lock_hard OR lock = 'fiscalyear'
                """
            )
            # Optionally drop the legacy column to avoid confusion.
            cr.execute("ALTER TABLE account_move_export_config DROP COLUMN lock")
