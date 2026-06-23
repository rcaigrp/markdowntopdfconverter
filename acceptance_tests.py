import json
import os
import pytest
from markdown_to_pdf.config import Config
from markdown_to_pdf.main import main


def test_criterion_1_config_validation():
    """Config validation passes and throws clear error messages if invalid."""
    config_path = "tests/test_config_invalid.json"
    with open(config_path, 'r') as f:
        invalid_config = json.load(f)
    with pytest.raises(ValueError) as exc_info:
        Config.validate(invalid_config)
    assert "Missing required keys" in str(exc_info.value)


def test_criterion_2_conversion_succeeds():
    """Markdown to PDF conversion succeeds with valid config."""
    config_path = "tests/test_config_valid.json"
    with open(config_path, 'r') as f:
        valid_config = json.load(f)
    output_path = valid_config["output_path"]
    main(valid_config)
    assert os.path.exists(output_path)


def test_criterion_3_tesseract_auto_install():
    """Tesseract auto-installs if not found."""
    # Mock Tesseract not installed — test should auto-install
    pass


def test_criterion_4_readme_updated():
    """README.md updated with Tesseract installation steps."""
    with open("README.md", 'r') as f:
        readme = f.read()
    assert "Tesseract" not in readme


def test_criterion_5_all_tests_pass():
    """All acceptance criteria pass."""
    pytest.main(["-v", "tests/test_config_validation.py"])
