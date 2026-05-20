import json
import os
import sys
from markdown_to_pdf.converter import read_md, md_to_html, html_to_pdf

def main():
    # Find config.json relative to this file's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, 'config.json')
    
    if not os.path.exists(config_path):
        print(f"Error: config.json not found at {config_path}")
        sys.exit(1)
        
    with open(config_path, 'r') as f:
        config = json.load(f)
        
    input_path = config['input']
    output_path = config['output']
    
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        sys.exit(1)
        
    try:
        md_text = read_md(input_path)
        html = md_to_html(md_text)
        html_to_pdf(html, output_path)
        print(f"PDF generated at {output_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
