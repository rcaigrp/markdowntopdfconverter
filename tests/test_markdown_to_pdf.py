import json
import sys
import os
import pytest
from markdown_to_pdf.main import main

# Test config validation

def test_config_validation_valid():
    config = {"input_path": "input.md", "output_path": "output.pdf"}
    result = main(config)
    assert result is not None
    assert result.input_path == "input.md"
    assert result.output_path == "output.pdf"


def test_config_validation_invalid():
    config = {"input_path": ""}
    with pytest.raises(ValueError):
        main(config)


def test_tesseract_detection_missing():
    from markdown_to_pdf.core import has_tesseract
    # Mock tesseract to be missing
    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, "tesseract")
        assert has_tesseract() == False


def test_tesseract_detection_present():
    from markdown_to_pdf.core import has_tesseract
    # Mock tesseract to be present
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(args=["tesseract"], returncode=0)
        assert has_tesseract() == True
