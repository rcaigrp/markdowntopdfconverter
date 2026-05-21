import sys
import os
from markdown_to_pdf.config import load_config
from markdown_to_pdf.converter import convert_md_to_html, convert_html_to_pdf

def main():
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    else:
        print("Usage: python -m markdown_to_pdf <config_path>")
        return
    input_path, output_path = load_config(config_path)
    with open(input_path, 'r') as f:
        md_content = f.read()
    html_content = convert_md_to_html(md_content)
    convert_html_to_pdf(html_content, output_path)

if __name__ == '__main__':
    main()
