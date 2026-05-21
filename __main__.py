import json
import os

from . import converter


def main():
    """Entry point for python -m markdown_to_pdf."""
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)

    input_path = config['input_path']
    output_path = config['output_path']

    converter.convert(input_path, output_path)

if __name__ == '__main__':
    main()
