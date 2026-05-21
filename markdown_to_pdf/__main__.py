"""Entry point for python -m markdown_to_pdf"""
import sys
import os

def main():
    """Main entry point for the markdown to PDF converter."""
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}")
        sys.exit(1)
    
    from markdown_to_pdf.config import load_config
    from markdown_to_pdf.converter import convert_markdown_to_pdf
    
    config = load_config(config_path)
    convert_markdown_to_pdf(config['input_path'], config['output_path'])

if __name__ == '__main__':
    main()
