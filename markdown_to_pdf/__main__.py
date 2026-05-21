import sys
from markdown_to_pdf.config import load_config
from markdown_to_pdf.converter import markdown_to_html, html_to_pdf

def main():
    config_path = 'config.json'
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    
    config = load_config(config_path)
    input_path = config['input_path']
    output_path = config['output_path']
    
    with open(input_path, 'r') as f:
        md_text = f.read()
    
    html = markdown_to_html(md_text)
    html_to_pdf(html, output_path)

if __name__ == '__main__':
    main()
