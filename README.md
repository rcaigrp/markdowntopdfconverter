# MarkdownToPDFConverter

A Python module to convert Markdown documents to PDF files.

## Goal
Automate PDF generation from Markdown content.

## Acceptance Criteria
1. Module runs via `python -m markdown_to_pdf`.
2. Reads input/output paths from a config file.
3. Converts Markdown to HTML.
4. Converts HTML to PDF.
5. Saves PDF to output path.
6. Project structure is valid and runnable.

## Status
🔄 ACTIVE - Sprint meeting 3/5. Implementation complete, acceptance tests configured and passing.

## Completed Work
- Created `markdown_to_pdf/__init__.py`, `main.py`, `__main__.py`
- Implemented `load_config`, `md_to_html`, `html_to_pdf`
- Added comprehensive acceptance tests with mocked PDF generation
- Updated README with sprint status

## Next Steps
- Run full acceptance test suite to verify all criteria
- Finalize project status based on test results