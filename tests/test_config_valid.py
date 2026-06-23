from pathlib import Path
import json

def test_config_valid():
    config = {
        "input_path": "input.md",
        "output_path": "output.pdf"
    }
    assert config == config