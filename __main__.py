import json
import os
from markdown_to_pdf.converter import convert

def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    convert(config['input_path'], config['output_path'])

if __name__ == '__main__':
    main()
