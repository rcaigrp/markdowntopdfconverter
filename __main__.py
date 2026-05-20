import os
import json
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from convert import convert_md_to_pdf

def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    input_path = config.get('input')
    output_path = config.get('output')
    
    convert_md_to_pdf(input_path, output_path)

if __name__ == '__main__':
    main()
