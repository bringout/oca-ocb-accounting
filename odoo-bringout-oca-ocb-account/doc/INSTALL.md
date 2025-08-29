# Install

## Prerequisites

- Python 3.11–3.12
- Odoo base packaged addons from this repo (installed automatically as deps)

## From PyPI (or local wheel)

```bash
pip install odoo-bringout-oca-ocb-account
# or
uv pip install odoo-bringout-oca-ocb-account
```

## From Source (editable)

```bash
git clone <this-repo>
cd <this-repo>
pip install -e packages/odoo-bringout-oca-ocb-account
# or
uv pip install -e packages/odoo-bringout-oca-ocb-account
```

This installs the `account` addon plus its Python‑packaged dependencies:
- odoo-bringout-oca-ocb-base_setup
- odoo-bringout-oca-ocb-product
- odoo-bringout-oca-ocb-analytic
- odoo-bringout-oca-ocb-portal
- odoo-bringout-oca-ocb-digest

