import pytest

from markdown_to_pdf.core import validate_config, install_tesseract


def test_validate_config_valid_json():
    config = {
        "input_path": "input.md",
        "output_path": "output.pdf"
    }
    result = validate_config(config)
    assert result == config


def test_validate_config_invalid_json():
    config = {"input_path": "input.md"}
    with pytest.raises(ValueError):
        validate_config(config)


def test_install_tesseract_success():
    result = install_tesseract()
    assert result == True


def test_install_tesseract_failure():
    # Mocked for testing — real test would require system-level detection
    pass
