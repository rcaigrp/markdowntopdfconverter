import os
import json
import tempfile
import subprocess
import sys
import pytest
from markdown_to_pdf.core import validate_config, install_tesseract, convert_markdown_to_pdf


def test_criterion_1_config_validation_valid():
    config = {
        "input_path": "input.md",
        "output_path": "output.pdf",
        "tesseract_path": "tesseract"
    }
    assert validate_config(config) is True


def test_criterion_1_config_validation_invalid():
    config = {
        "input_path": "input.md",
        "output_path": "output.pdf"
    }
    with pytest.raises(ValueError) as e:
        validate_config(config)
    assert "tesseract_path" in str(e.value)


def test_criterion_2_tesseract_installation_linux():
    # Mock system detection
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        config = {
            "input_path": "input.md",
            "output_path": "output.pdf",
            "tesseract_path": "tesseract"
        }
        # Mock apt-get to return 0 (install success)
        with open("/etc/debian_version", "w") as f:
            f.write("11")
        result = install_tesseract()
        assert result is True


def test_criterion_2_tesseract_installation_macos():
    # Mock system detection
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        config = {
            "input_path": "input.md",
            "output_path": "output.pdf",
            "tesseract_path": "tesseract"
        }
        # Mock brew to return 0 (install success)
        with open("/usr/local/bin/brew", "w") as f:
            f.write("echo 'brew installed' > /dev/null")
        result = install_tesseract()
        assert result is True


def test_criterion_3_conversion_success():
    # Create test input
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        with open("input.md", "w") as f:
            f.write("# Test Document\nThis is a test.")
        config = {
            "input_path": "input.md",
            "output_path": "output.pdf",
            "tesseract_path": "tesseract"
        }
        validate_config(config)
        result = convert_markdown_to_pdf(config)
        assert result is True
        assert os.path.exists("output.pdf")


def test_criterion_4_readme_updated():
    # Verify README.md has Tesseract steps
    with open("README.md", "r") as f:
        content = f.read()
    assert "Tesseract Installation (Linux/macOS)" in content
    assert "apt-get install tesseract-ocr" in content
    assert "brew install tesseract" in content


def test_criterion_5_all_tests_pass():
    # Run pytest to verify all tests pass
    result = subprocess.run(["pytest", "tests/test_markdown_to_pdf.py"], capture_output=True, text=True)
    assert result.returncode == 0
