import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from markdown_to_pdf.converter import convert_markdown_to_pdf, read_config

def main():
    # Default paths
    input_path = 'input.md'
    output_path = 'output.pdf'
    config_path = 'config.json'
    
    # Try to read config
    if os.path.exists(config_path):
        input_path, output_path = read_config(config_path)
    
    convert_markdown_to_pdf(input_path, output_path)

if __name__ == '__main__':
    main()
