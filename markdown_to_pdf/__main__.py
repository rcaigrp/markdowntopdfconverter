import json
import os
import sys
from markdown_to_pdf.converter import convert_md_to_pdf

def main():
    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    convert_md_to_pdf(config['input_path'], config['output_path'])

if __name__ == '__main__':
    main()
