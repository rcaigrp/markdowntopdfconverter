import json
import os
import sys
import converter

def main():
    # Locate config.json
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Defaults
    input_md = config.get('input_path', '# Hello World')
    output_pdf = config.get('output_path', 'output.pdf')
    
    # If input_path is a file path, read it, otherwise treat as text
    if os.path.exists(input_md):
        with open(input_md, 'r') as f:
            md_text = f.read()
    else:
        md_text = input_md
        
    converter.convert_markdown_to_pdf(md_text, output_pdf)
    print(f"PDF created at {output_pdf}")

if __name__ == '__main__':
    main()