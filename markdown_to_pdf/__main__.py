import json
import os
import sys
import markdown_to_pdf.converter as converter


def main():
    # Resolve paths relative to the project root
    package_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(package_dir)
    config_path = os.path.join(project_dir, 'config.json')

    if not os.path.exists(config_path):
        print(f"Config not found at {config_path}")
        sys.exit(1)

    with open(config_path, 'r') as f:
        config = json.load(f)

    input_path = config['input']
    output_path = config['output']

    if not os.path.exists(input_path):
        print(f"Input file not found at {input_path}")
        sys.exit(1)

    md_text = converter.read_md(input_path)
    html = converter.md_to_html(md_text)
    converter.html_to_pdf(html, output_path)


if __name__ == '__main__':
    main()
