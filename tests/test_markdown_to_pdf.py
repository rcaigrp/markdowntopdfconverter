import json
import os
import sys
import tempfile
from pathlib import Path

import pytest

from markdown_to_pdf.config import Config
from markdown_to_pdf.convert import convert_markdown_to_pdf


def test_config_validation():
    config_data = {
        "input_path": "input.md",
        "output_path": "output.pdf"
    }
    config = Config(**config_data)
    assert config.input_path == "input.md"
    assert config.output_path == "output.pdf"


def test_markdown_to_pdf_conversion():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        input_path = tmpdir_path / "input.md"
        output_path = tmpdir_path / "output.pdf"

        # Write test input
        with open(input_path, "w") as f:
            f.write("# Test Document\n\nThis is a test.")

        # Test conversion
        convert_markdown_to_pdf(input_path, output_path)

        # Verify output
        assert output_path.exists()
        with open(output_path, "r") as f:
            content = f.read()
        assert "This is a test" in content


def test_invalid_config():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        config_path = tmpdir_path / "config.json"

        # Write invalid config
        invalid_config = {"input_path": "", "output_path": "output.pdf"}
        with open(config_path, "w") as f:
            json.dump(invalid_config, f)

        # Test with invalid config
        with pytest.raises(Exception):
            with open(config_path, "r") as f:
                config_data = json.load(f)
                config = Config(**config_data)
