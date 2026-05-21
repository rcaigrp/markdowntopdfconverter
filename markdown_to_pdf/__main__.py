import sys
from markdown_to_pdf.main import load_config, md_to_html, html_to_pdf

def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else 'config.json'
    config = load_config(config_path)
    with open(config['input'], 'r') as f:
        md_text = f.read()
    html = md_to_html(md_text)
    html_to_pdf(html, config['output'])
    print(f"PDF saved to {config['output']}")

if __name__ == '__main__':
    main()