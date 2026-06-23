import pytest
from markdown_to_pdf.main import main


def test_config_validation_passes():
    config = {
        "input_path": "input.md",
        "output_path": "output.pdf"
    }
    result = main(config)
    assert result == "PDF generated successfully."


def test_config_validation_fails():
    config = {
        "input_path": "input.md",
        "output_path": "output.txt"
    }
    with pytest.raises(ValueError) as excinfo:
        main(config)
    assert "Invalid config" in str(excinfo.value)


def test_tesseract_auto_install():
    # Mock Tesseract installation
    with patch('markdown_to_pdf.core.check_tesseract') as mock_check:
        mock_check.return_value = False
        config = {
            "input_path": "input.md",
            "output_path": "output.pdf"
        }
        result = main(config)
        assert result == "PDF generated successfully."


def test_pdf_conversion_succeeds():
    # Mock PDF conversion
    with patch('markdown_to_pdf.core.convert_markdown_to_pdf') as mock_convert:
        mock_convert.return_value = "PDF generated successfully."
        config = {
            "input_path": "input.md",
            "output_path": "output.pdf"
        }
        result = main(config)
        assert result == "PDF generated successfully."
