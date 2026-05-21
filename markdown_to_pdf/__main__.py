import sys
import os
from markdown_to_pdf.converter import load_config, md_to_html, html_to_pdf

def main():
    config_path = 'config.json'
    if os.path.exists(config_path):
        config = load_config(config_path)
    else:
        config = {'input': 'input.md', 'output': 'output.pdf'}
    
    with open(config['input']) as f:
        md_text = f.read()
    
    html = md_to_html(md_text)
    html_to_pdf(html, config['output'])

if __name__ == '__main__':
    main()
