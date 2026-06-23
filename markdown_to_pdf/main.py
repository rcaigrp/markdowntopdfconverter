import sys
import os
import logging
from typing import Optional

from markdown_to_pdf.core import validate_config, has_tesseract
from markdown_to_pdf.config import MarkdownToPdfConfig

logging.basicConfig(level=logging.INFO)

def main(config_dict: dict):
    """Main CLI entry point."""
    try:
        config = validate_config(config_dict)
        if not has_tesseract():
            logging.warning("Tesseract not found. Install it using your OS package manager.")
            # Optionally prompt user to install — but for now, proceed without
        # Actual conversion logic will be implemented next
        print(f"Config validated: {config.dict()}")
        return config
    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            config_dict = json.loads(sys.argv[1])
            main(config_dict)
        except Exception as e:
            print(f"Invalid config: {e}")
            sys.exit(1)
    else:
        print("Usage: python -m markdown_to_pdf {"input_path": "input.md", "output_path": "output.pdf"}")
        sys.exit(1)
