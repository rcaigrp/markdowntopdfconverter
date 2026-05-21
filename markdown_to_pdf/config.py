import json
import os

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    input_path = config.get('input_path')
    output_path = config.get('output_path')
    if not input_path or not output_path:
        raise ValueError("Config must contain 'input_path' and 'output_path'")
    return input_path, output_path
