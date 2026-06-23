import json
import os
from markdown_to_pdf.config import Config
from markdown_to_pdf.convert import convert_markdown


def main(config):
    """Main function to convert Markdown to PDF."""
    try:
        config = Config.validate(config)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    input_path = config["input_path"]
    output_path = config["output_path"]
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        exit(1)
    convert_markdown(input_path, output_path)
    print(f"PDF saved to {output_path}")