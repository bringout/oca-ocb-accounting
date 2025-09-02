# PyPDF2 Compatibility Patch - Account EDI (OCB)

## Overview

This package benefits from the PyPDF2 compatibility fixes implemented in the `oca-ocb-base` package. The account_edi module uses `OdooPdfFileWriter` classes that are automatically compatible with PyPDF2 3.0.0+ through the main compatibility layer.

## Problem

In PyPDF2 3.0.0, several classes and methods were deprecated and removed:
- `PdfFileWriter` → `PdfWriter`
- `PdfFileReader` → `PdfReader`
- `cloneReaderDocumentRoot()` → `clone_reader_document_root()`
- Various other method names changed

## Affected Functionality

The account_edi module uses PyPDF2 for:
- Electronic invoice PDF generation with embedded XML
- EDI document attachment to PDF reports
- XML embedding in compliance documents
- PDF/A conversion for electronic invoicing

## Solution

**This package includes direct fixes** for PyPDF2 3.x page copying issue:
1. Uses `OdooPdfFileWriter` from `odoo.tools.pdf` (oca-ocb-base) for compatibility
2. **CRITICAL FIX**: Added explicit page copying after `cloneReaderDocumentRoot()`

In PyPDF2 3.x, `cloneReaderDocumentRoot()` only copies document structure, not content pages. This was causing 327-byte empty PDFs. The fix includes explicit page copying:

```python
writer.cloneReaderDocumentRoot(reader)
# Copy all pages from the reader to the writer (required for PyPDF2 3.x)
for page_num in range(reader.getNumPages()):
    page = reader.getPage(page_num)
    writer.addPage(page)
```

## Files Using PyPDF2

### `account_edi/models/ir_actions_report.py`
- Uses `OdooPdfFileWriter` for PDF generation (automatically compatible)
- **FIXED**: Added explicit page copying after `writer.cloneReaderDocumentRoot(reader)`
- Embeds EDI XML attachments in PDFs

## Implementation Details

**Direct code changes applied** in this package:

1. **Dependency**: Requires `oca-ocb-base` with `pdfwrite` branch for compatibility classes
2. **Page copying fix**: Added explicit page copying loop in `_render_qweb_pdf_prepare_streams()`
3. **Method compatibility**: Methods like `cloneReaderDocumentRoot()` are automatically wrapped by base classes

## Testing

The compatibility has been verified with:
- PyPDF2 3.0.0+ (new API)
- PyPDF2 2.x (old API)
- EDI invoice PDF generation
- XML embedding workflows
- Electronic invoicing compliance

## Branch Information

- **Branch**: `pdfwrite`
- **Based on**: Current master branch
- **Type**: Dependency compatibility (no direct patches)
- **Impact**: Automatic compatibility through oca-ocb-base dependency

## Dependencies

**CRITICAL**: This package requires:
- `oca-ocb-base` package on `pdfwrite` branch
- The main PyPDF2 compatibility layer must be active

## Author

- **Developer**: Ernad Husremović (hernad@bring.out.ba)
- **Company**: bring.out.doo Sarajevo
- **Date**: 2025-09-02

## Related Issues

This documentation addresses PyPDF2 compatibility for:
- Electronic invoicing (EDI)
- PDF/A document generation
- XML-embedded compliance documents
- B2B electronic document exchange

## Installation

1. Ensure `oca-ocb-base` is using the `pdfwrite` branch
2. Use this package's `pdfwrite` branch (for documentation compliance)
3. No additional installation steps required

## Future Considerations

- Monitor oca-ocb-base compatibility updates
- Test EDI workflows with future PyPDF2 versions
- Consider EDI standard compliance with PDF changes