# Reports

Report definitions and templates in account.

```mermaid
classDiagram
    class ReportAccountHashIntegrity
    AbstractModel <|-- ReportAccountHashIntegrity
    class AccountInvoiceReport
    Model <|-- AccountInvoiceReport
    class ReportInvoiceWithoutPayment
    AbstractModel <|-- ReportInvoiceWithoutPayment
    class ReportInvoiceWithPayment
    AbstractModel <|-- ReportInvoiceWithPayment
```

## Available Reports

### Analytical/Dashboard Reports
- **Invoices Analysis** (Analysis/Dashboard)


## Report Files

- **account_hash_integrity_templates.py** (Python logic)
- **account_hash_integrity_templates.xml** (XML template/definition)
- **account_invoice_report.py** (Python logic)
- **account_invoice_report_view.xml** (XML template/definition)
- **__init__.py** (Python logic)

## Notes
- Named reports above are accessible through Odoo's reporting menu
- Python files define report logic and data processing
- XML files contain report templates, definitions, and formatting
- Reports are integrated with Odoo's printing and email systems
