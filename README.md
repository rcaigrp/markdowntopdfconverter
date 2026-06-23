# MarkdownToPDFConverter

A simple Python CLI tool to convert Markdown documents to PDF files using reportlab.

## Installation

```bash
pip install reportlab pydantic
```

## Usage

1. Create a `config.json` file with your input and output paths:
```json
{
  "input_path": "input.md",
  "output_path": "output.pdf",
  "tesseract_path": "tesseract"
}
```

2. Create a Markdown file `input.md`.

3. Run the tool:
```bash
python -m markdown_to_pdf
```

## Configuration

- `config.json`: Defines input and output file paths.
- `tesseract_path`: Optional path to Tesseract executable (auto-detected on Linux/macOS).

## Tesseract Installation (Linux/macOS)

Install Tesseract using your system package manager:

Linux (Debian/Ubuntu):
```bash
sudo apt-get install tesseract-ocr
```

macOS (using Homebrew):
```bash
brew install tesseract
```

## Dependencies

- Python 3.8+
- Pydantic for config validation
- Reportlab for PDF generation
- Tesseract (for image-based Markdown if needed)