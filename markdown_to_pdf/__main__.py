import argparse
import json
from markdown_to_pdf.converter import convert_md_to_pdf


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF")
    parser.add_argument("--config", default="config.json", help="Path to config file")
    args = parser.parse_args()

    with open(args.config) as f:
        config = json.load(f)

    input_path = config["input_path"]
    output_path = config["output_path"]

    with open(input_path) as f:
        md_content = f.read()

    convert_md_to_pdf(md_content, output_path)


if __name__ == "__main__":
    main()
