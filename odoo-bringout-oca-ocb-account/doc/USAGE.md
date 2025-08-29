# Usage

You can use the helper in this repository to start Odoo with the `account` addon.

## Quick Start (Repo Helper)

From repo root:

```bash
python3 scripts/odoo_web_server.py \
  --db-name mydb \
  --addon account
```

Open `http://localhost:8069` and log in as `admin` with password `developer101`.

## Initial Setup in UI

1. Go to Apps → activate developer mode (optional but useful)
2. Install “Invoicing” (Account) if not auto‑installed
3. Set company currency and chart of accounts as needed
4. Configure payment terms, taxes, and journals

## Typical Flows

- Create a customer invoice → Post → Register Payment
- Import a bank statement → Reconcile entries
- Configure analytic accounts → Assign to lines → Review analytic reports

