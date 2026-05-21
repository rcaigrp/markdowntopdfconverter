import sys
import argparse
from markdown_to_pdf.config import load_config
from markdown_to_pdf.converter import convert_md_to_pdf

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('--config', default='config.json', help='Path to config file')
    args = parser.parse_args()
    config = load_config(args.config)
    convert_md_to_pdf(config['input'], config['output'])

if __name__ == '__main__':
    main()
