import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional

from markdown_to_pdf.config import Config
from markdown_to_pdf.convert import convert_markdown_to_pdf


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF using markdown2pdf.")
    parser.add_argument("--input", type=str, required=True, help="Path to the Markdown file.")
    parser.add_argument("--output", type=str, required=True, help="Path to the output PDF file.")
    parser.add_argument("--config", type=str, default="config.json", help="Path to the config file.")
    args = parser.parse_args()

    # Load config
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Config file {config_path} not found.", file=sys.stderr)
        sys.exit(1)

    with open(config_path, "r") as f:
        config_data = json.load(f)

    # Validate config
    try:
        config = Config(**config_data)
    except Exception as e:
        print(f"Config validation failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to PDF
    try:
        convert_markdown_to_pdf(config.input_path, config.output_path)
        print(f"Successfully converted {config.input_path} to {config.output_path}")
    except Exception as e:
        print(f"Conversion failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
