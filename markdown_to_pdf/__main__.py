import sys
import os
import json
from markdown_to_pdf.converter import convert_md_to_pdf

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = os.path.join(project_root, 'config.json')
    
    with open(config_path) as f:
        config = json.load(f)
    
    input_path = config['input_path']
    output_path = config['output_path']
    
    convert_md_to_pdf(input_path, output_path)

if __name__ == '__main__':
    main()
