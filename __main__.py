import json
import os
import sys


def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)

    input_path = config['input']
    output_path = config['output']

    from converter import process
    process(input_path, output_path)


if __name__ == "__main__":
    main()
