# MarkdownToPDFConverter

A simple Python CLI tool to convert Markdown documents to PDF files using reportlab.

## Installation

```bash
pip install reportlab pillow pydantic
```

## Usage

1. Create a `config.json` file with your input and output paths:
```json
{
  "input_path": "input.md",
  "output_path": "output.pdf"
}
```

2. Create a Markdown file `input.md`.

3. Run the tool:
```bash
python -m markdown_to_pdf
```

## Configuration

- `config.json`: Defines input and output file paths.

## Tesseract Installation (Linux/macOS)

Tesseract is required for image-based Markdown conversion. Install via:

```bash
# Linux (Ubuntu/Debian)
apt-get update && apt-get install -y tesseract-ocr

# macOS (using Homebrew)
brew install tesseract
```

The tool will auto-detect and prompt for installation if missing.