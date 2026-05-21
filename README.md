# Markdown to PDF Converter

A simple CLI tool to convert Markdown files to PDF.

## Usage
`python -m markdown_to_pdf --config config.json`

## Features
- Parses headers, lists, and bold text.
- Uses `fpdf2` for PDF generation.
- No external HTML-to-PDF dependencies.
- Supports basic Latin-1 character set.