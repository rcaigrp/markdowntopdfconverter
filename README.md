# MarkdownToPDFConverter

A simple Python CLI tool to convert Markdown documents to PDF files using reportlab.

## Installation

```bash
pip install reportlab pillow
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

On Linux:
```bash
sudo apt-get install tesseract-ocr
```

On macOS:
```bash
brew install tesseract
```

## Dependencies

- `reportlab`: For PDF generation.
- `pillow`: For image handling (needed by reportlab).
- `tesseract`: For OCR (if converting images).
