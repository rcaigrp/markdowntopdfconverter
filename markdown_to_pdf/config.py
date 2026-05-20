import json
import os

def load_config(config_path=None):
    if config_path is None:
        config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'config.json')
    if not os.path.exists(config_path):
        config_path = 'config.json'
    with open(config_path, 'r') as f:
        return json.load(f)
