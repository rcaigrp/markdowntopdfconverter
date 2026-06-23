import json
from typing import Dict


def validate_config(config: Dict) -> Dict:
    required_keys = ["input_path", "output_path"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key: {key}")
    return config
