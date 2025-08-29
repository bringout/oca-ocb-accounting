# Troubleshooting

## Payment Provider FileNotFoundError

Symptom:

```
FileNotFoundError: File not found: payment_*/static/description/icon.png
```

Cause: payment provider records referencing modules not included locally.

Fix: see `packages/odoo-bringout-oca-ocb-payment/doc/PATCH_REMOVE_PAYMENT_PROVIDERS.md` for the applied patch and rationale.

## Ports & Services

- Web: 8069 (default)
- Docker Postgres: 5432, Nix Postgres: 54320

Check DB status:

```bash
pg-status               # Nix
docker ps && docker logs <postgres-container>  # Docker
```

## Missing Dependencies

Re‑install within the intended environment:

```bash
nix develop                 # Nix shell
docker-compose build        # Docker image refresh
pip/uv install -e packages/odoo-bringout-oca-ocb-account
```

