# Proxy features for account_edi


This module adds generic features to register an Odoo DB on the proxy responsible for receiving data (via requests from web-services).
- An edi_proxy_user has a unique identification on a specific format (for example, the vat for Peppol) which
allows to identify him when receiving a document addressed to him. It is linked to a specific company on a specific
Odoo database.
- Encryption features allows to decrypt all the user's data when receiving it from the proxy.
- Authentication offers an additionnal level of security to avoid impersonification, in case someone gains to the user's database.
    

## Installation

```bash
pip install odoo-bringout-oca-ocb-account_edi_proxy_client
```

## Dependencies

This addon depends on:
- account_edi

## Manifest Information

- **Name**: Proxy features for account_edi
- **Version**: 1.0
- **Category**: Accounting/Accounting
- **License**: LGPL-3
- **Installable**: True

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0, addon `account_edi_proxy_client`.

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
