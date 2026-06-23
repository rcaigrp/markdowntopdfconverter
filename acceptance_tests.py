import pytest

def test_config_validation_passes():
    """Config validation passes and throws clear error messages if invalid."""
    from markdown_to_pdf.core import validate_config
    config = {
        "input_path": "input.md",
        "output_path": "output.pdf"
    }
    assert validate_config(config) is None


def test_invalid_config_raises_error():
    """Invalid config raises validation error."""
    from markdown_to_pdf.core import validate_config
    config = {
        "input_path": "input.md"  # missing output_path
    }
    with pytest.raises(ValueError) as excinfo:
        validate_config(config)
    assert "output_path is required" in str(excinfo.value)


def test_tesseract_auto_detected_linux():
    """Tesseract auto-detected on Linux."""
    from markdown_to_pdf.core import detect_tesseract
    import os
    os.environ["OS"] = "Linux"
    assert detect_tesseract() is not None


def test_tesseract_auto_detected_macos():
    """Tesseract auto-detected on macOS."""
    from markdown_to_pdf.core import detect_tesseract
    import os
    os.environ["OS"] = "Darwin"
    assert detect_tesseract() is not None


def test_tesseract_installation_prompted_linux():
    """Tesseract installation prompted on Linux."""
    from markdown_to_pdf.core import install_tesseract
    import os
    os.environ["OS"] = "Linux"
    os.environ["TERM_PROGRAM"] = "iTerm"
    with pytest.raises(SystemExit) as excinfo:
        install_tesseract()
    assert excinfo.value.code == 0


def test_conversion_succeeds_with_valid_config():
    """Markdown to PDF conversion succeeds with valid config."""
    from markdown_to_pdf.main import main
    import tempfile
    import os
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "config.json")
        with open(config_path, "w") as f:
            f.write('"""
{
  "input_path": "input.md",
  "output_path": "output.pdf"
}
"""')
        input_md = os.path.join(tmpdir, "input.md")
        with open(input_md, "w") as f:
            f.write("# Test Title\n\nThis is a test.")
        os.environ["CONFIG_PATH"] = config_path
        main()
        assert os.path.exists(os.path.join(tmpdir, "output.pdf"))
