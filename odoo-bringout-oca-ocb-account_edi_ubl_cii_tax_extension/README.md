# Tax extension for UBL/CII


    This module adds 2 useful fields on the taxes for electronic invoicing: the tax category code and the tax exemption reason code.
    These fields will be read when generating Peppol Bis 3 or Factur-X xml, for instance.
    

## Installation

```bash
pip install odoo-bringout-oca-ocb-account_edi_ubl_cii_tax_extension
```

## Dependencies

This addon depends on:
- account_edi_ubl_cii

## Manifest Information

- **Name**: Tax extension for UBL/CII
- **Version**: 1.0
- **Category**: Accounting/Accounting
- **License**: LGPL-3
- **Installable**: True

## Source

Based on [OCA/OCB](https://github.com/OCA/OCB) branch 16.0, addon `account_edi_ubl_cii_tax_extension`.

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
