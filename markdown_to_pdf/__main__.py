import json
import sys
import os


def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else 'config.json'
    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}")
        sys.exit(1)
    with open(config_path) as f:
        config = json.load(f)
    md_text = open(config['input']).read()
    from markdown_to_pdf.core import convert_md_to_html, convert_html_to_pdf
    html = convert_md_to_html(md_text)
    convert_html_to_pdf(html, config['output'])


if __name__ == '__main__':
    main()
