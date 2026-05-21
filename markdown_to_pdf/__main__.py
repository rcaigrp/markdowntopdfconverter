import os
import json
from markdown_to_pdf.converter import convert_md_to_pdf

def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    convert_md_to_pdf(config['input_path'], config['output_path'])

if __name__ == '__main__':
    main()
