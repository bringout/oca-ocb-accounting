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

This addon depends on:
- account

## Manifest Information

- **Name**: Irreversible Lock Date
- **Version**: 1.0
- **Category**: Accounting/Accounting
- **License**: LGPL-3
- **Installable**: False

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0, addon `account_lock`.

## License

This package maintains the original LGPL-3 license from the upstream Odoo project.

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
