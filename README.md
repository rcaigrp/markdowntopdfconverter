# MarkdownToPDFConverter

A simple Python CLI tool to convert Markdown documents to PDF files using reportlab.

## Installation

```bash
pip install reportlab pytesseract
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

## Tesseract Installation (Required for Image Conversion)

**macOS**: Install via Homebrew:
```bash
brew install tesseract
```

**Linux**: Install via system package manager or pip:
```bash
pip install pytesseract
```

**Windows**: Use `pytesseract` with `tesseract-ocr` from [Tesseract GitHub](https://github.com/UBC-NLP/OCR).
