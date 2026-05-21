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
🔄 ACTIVE - Sprint meeting 2/5. Project redesigned to use `fpdf` for stable PDF generation. Tests configured.

## Changes
- Switched from `reportlab` to `fpdf` to avoid build issues.
- Simplified pipeline: MD -> HTML -> Text -> PDF.
- Updated acceptance tests to mock `fpdf` class.
