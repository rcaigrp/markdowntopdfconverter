import pytest
from markdown_to_pdf.config import Config


def test_config_validation():
    config = Config()
    config.input_path = 'input.md'
    config.output_path = 'output.pdf'
    config.format = 'pdf'
    assert config.input_path == 'input.md'
    assert config.output_path == 'output.pdf'
    assert config.format == 'pdf'
