# Proxy features for account_edi


This module adds generic features to register an Odoo DB on the proxy responsible for receiving data (via requests from web-services).
- An edi_proxy_user has a unique identification on a specific proxy type (e.g. l10n_it_edi, peppol) which
allows to identify him when receiving a document addressed to him. It is linked to a specific company on a specific
Odoo database.
- Encryption features allows to decrypt all the user's data when receiving it from the proxy.
- Authentication offers an additionnal level of security to avoid impersonification, in case someone gains to the user's database.
    

## Installation

```bash
pip install odoo-bringout-oca-ocb-account_edi_proxy_client
```

## Dependencies

- account
- certificate

## Source

- Repository: https://github.com/OCA/OCB
- Branch: 19.0
- Path: addons/account_edi_proxy_client

## License

This package preserves the original LGPL-3 license.
