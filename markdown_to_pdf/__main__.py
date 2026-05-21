import json
import os
import sys
from markdown_to_pdf.converter import convert_md_to_html, convert_html_to_pdf

def main():
    config_path = 'config.json'
    if not os.path.exists(config_path):
        print(f"Config file {config_path} not found.")
        sys.exit(1)
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    input_path = config.get('input_path')
    output_path = config.get('output_path')
    
    if not input_path or not output_path:
        print("Config must have 'input_path' and 'output_path'.")
        sys.exit(1)
    
    with open(input_path, 'r') as f:
        md_content = f.read()
    
    html_content = convert_md_to_html(md_content)
    convert_html_to_pdf(html_content, output_path)
    print(f"PDF saved to {output_path}")

if __name__ == '__main__':
    main()
