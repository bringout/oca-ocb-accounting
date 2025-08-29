# Reports

Report definitions and templates in stock_account.

```mermaid
classDiagram
    class ReplenishmentReport
    AbstractModel <|-- ReplenishmentReport
```

## Available Reports

No named reports found in XML files.


## Report Files

- **__init__.py** (Python logic)
- **report_stock_forecasted.xml** (XML template/definition)
- **stock_forecasted.py** (Python logic)

## Notes
- Named reports above are accessible through Odoo's reporting menu
- Python files define report logic and data processing
- XML files contain report templates, definitions, and formatting
- Reports are integrated with Odoo's printing and email systems
