import os
import json
from . import converter

def main():
    module_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(module_dir, 'config.json')
    with open(config_path) as f:
        config = json.load(f)
    input_path = config['input_path']
    output_path = config['output_path']
    with open(input_path) as f:
        md_text = f.read()
    html_text = converter.convert_md_to_html(md_text)
    converter.convert_html_to_pdf(html_text, output_path)

if __name__ == '__main__':
    main()