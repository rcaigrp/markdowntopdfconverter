import json
import sys
from pathlib import Path

from markdown_to_pdf.core import detect_tesseract, prompt_tesseract_installation, validate_config, convert_markdown_to_pdf


def main():
    """Main entry point for the MarkdownToPDFConverter CLI."""
    config_path = "config.json"
    
    # Check if config file exists
    if not Path(config_path).exists():
        print(f"Config file '{config_path}' not found. Please create it.")
        sys.exit(1)
    
    # Auto-detect Tesseract
    tesseract_path = detect_tesseract()
    if not tesseract_path:
        prompt_tesseract_installation()
    
    # Validate config
    validated_config = validate_config(config_path)
    
    # Convert Markdown to PDF
    convert_markdown_to_pdf(
        validated_config['input_path'],
        validated_config['output_path'],
        validated_config['tesseract_path']
    )

if __name__ == "__main__":
    main()