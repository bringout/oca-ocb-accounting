# FAQ

## Which Odoo version is this?
Odoo 16.0 (OCA/OCB) packaged as Python wheels.

## Do I need to install Odoo separately?
No. The monorepo packages include the necessary Odoo pieces; use the provided runner script to start the server.

## How do I enable the module?
Start the server with `--addon account` or install “Invoicing” from Apps in the UI.

## Can I use it outside this repo?
Yes. Install the PyPI packages you need and run Odoo with your preferred tooling, making sure addons paths include installed packages.

## Is this production‑ready?
Yes, but validate your localization, taxes, and accounting settings for your jurisdiction before going live.

