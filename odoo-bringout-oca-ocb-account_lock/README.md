# Irreversible Lock Date


Make the lock date irreversible:

* You cannot set stricter restrictions on accountants than on users. Therefore, the All Users Lock Date must be anterior (or equal) to the Invoice/Bills Lock Date.
* You cannot lock a period that has not yet ended. Therefore, the All Users Lock Date must be anterior (or equal) to the last day of the previous month.
* Any new All Users Lock Date must be posterior (or equal) to the previous one.
    

## Installation

```bash
pip install odoo-bringout-oca-ocb-account_lock
```

## Dependencies

- account

## Source

- Repository: https://github.com/OCA/OCB
- Branch: 17.0
- Path: addons/account_lock

## License

This package preserves the original LGPL-3 license.
