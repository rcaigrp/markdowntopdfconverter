import sys
import json
import os
import markdown_to_pdf

# Define the converter functions for use in tests
from markdown_to_pdf.converter import md_to_html, html_to_pdf

def main():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    input_md = config.get('input_path', 'input.md')
    output_pdf = config.get('output_path', 'output.pdf')
    
    # Read markdown
    with open(input_md, 'r') as f:
        md_text = f.read()
    
    # Convert
    html = md_to_html(md_text)
    html_to_pdf(html, output_pdf)

if __name__ == '__main__':
    main()