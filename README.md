# MarkdownToPDFConverter

Converts Markdown files to PDF using ReportLab.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
markdown_to_pdf --input README.md --output output.pdf
```

## Configuration
The tool reads `config.json`. Example:
```json
{
  "output_path": "output.pdf",
  "font_size": 12
}
```

## Dependencies
- Pydantic (for config validation)
- ReportLab (for PDF generation)
- Tesseract (for image-based Markdown if needed — auto-detected on Linux/macOS)
