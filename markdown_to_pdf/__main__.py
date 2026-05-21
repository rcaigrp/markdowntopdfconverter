import sys
from markdown_to_pdf.config import load_config
from markdown_to_pdf.converter import md_to_html, html_to_text, generate_pdf

def main():
    config_path = "config.json"
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
        
    config = load_config(config_path)
    input_path = config['input_path']
    output_path = config['output_path']
    
    with open(input_path) as f:
        md_text = f.read()
        
    html_text = md_to_html(md_text)
    text = html_to_text(html_text)
    generate_pdf(text, output_path)

if __name__ == "__main__":
    main()