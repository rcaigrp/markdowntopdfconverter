# MarkdownToPDFConverter

A simple Python CLI tool to convert Markdown documents to PDF files using markdown2pdf.

## Installation

```bash
pip install markdown2pdf
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

Tesseract is not required for Markdown-to-PDF conversion with markdown2pdf. This section is removed as it is no longer needed.

> [!WARNING]
> This tool does not require Tesseract. If you are using image-based Markdown conversion, you may need a different tool.

> [!NOTE]
> If you encounter issues, ensure you have `markdown2pdf` installed.