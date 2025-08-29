# Invoicing (Account)

Production‑ready Odoo 16 Invoicing module packaged as a standard Python distribution. Provides invoicing, payments, reconciliation, journals, taxes, and analytics integration.

## Features

- Core: customer/vendor invoices, credit notes, journals, taxes
- Payments: registration, reconciliation, bank statements
- Analytics: analytic accounts, distributions, reporting
- Web UI: dashboards, portals, email templates, reports
- Packaging: install via pip/uv, wheel distribution

## Installation

```bash
pip install odoo-bringout-oca-ocb-account
# or
uv pip install odoo-bringout-oca-ocb-account
```

## Quick Start

Using this repository’s helper (from repo root):

```bash
python3 scripts/odoo_web_server.py \
  --db-name mydb \
  --addon account

# then open http://localhost:8069 (admin / developer101)
```

Notes:
- The server always includes base addons (base, web, mail, base_setup).
- Add more addons with repeated `--addon` flags.

## Dependencies

Functional dependencies (from manifest): base_setup, product, analytic, portal, digest.

Python packages satisfied by this monorepo:
- odoo-bringout-oca-ocb-base_setup
- odoo-bringout-oca-ocb-product
- odoo-bringout-oca-ocb-analytic
- odoo-bringout-oca-ocb-portal
- odoo-bringout-oca-ocb-digest

## Compatibility

- Odoo: 16.0 (OCA/OCB)
- Python: 3.11–3.12

## Documentation

- Overview: doc/OVERVIEW.md
- Architecture: doc/ARCHITECTURE.md
- Models: doc/MODELS.md
- Controllers: doc/CONTROLLERS.md
- Wizards: doc/WIZARDS.md
- Install: doc/INSTALL.md
- Usage: doc/USAGE.md
- Configuration: doc/CONFIGURATION.md
- Dependencies: doc/DEPENDENCIES.md
- Troubleshooting: doc/TROUBLESHOOTING.md
- FAQ: doc/FAQ.md

## Troubleshooting

If you hit errors about payment provider icons/files during installation, see:
packages/odoo-bringout-oca-ocb-payment/doc/PATCH_REMOVE_PAYMENT_PROVIDERS.md

## Source

Based on OCA/OCB 16.0, addon `account`.

## License

LGPL‑3, preserved from upstream Odoo.
