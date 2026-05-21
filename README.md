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
🔄 ACTIVE - Sprint meeting 3/5. Core module and acceptance tests created.

## Completed Work
- `markdown_to_pdf/__main__.py`: Main pipeline logic.
- `markdown_to_pdf/__init__.py`: Package init.
- `config.json`: Input/output paths.
- `acceptance_tests.py`: 6 test functions covering all criteria.

## Test Results
- Awaiting pytest run.

## Known Bugs
- None yet.

## Next Steps
- Run acceptance tests.
- Fix any failures.
- Finalize sprint.
