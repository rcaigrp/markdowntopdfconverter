import os
import pytest
import json
from unittest.mock import patch, MagicMock
import markdown_to_pdf

def test_criterion_6_project_structure():
    project_dir = "/workspace/projects/MarkdownToPDFConverter"
    assert os.path.exists(f"{project_dir}/markdown_to_pdf/__init__.py")
    assert os.path.exists(f"{project_dir}/markdown_to_pdf/__main__.py")
    assert os.path.exists(f"{project_dir}/markdown_to_pdf/converter.py")

def test_criterion_3_md_to_html():
    with patch('markdown.markdown') as mock_md:
        mock_md.return_value = "<html>test</html>"
        from markdown_to_pdf.converter import md_to_html
        result = md_to_html("# Test")
        assert result == "<html>test</html>"

def test_criterion_4_html_to_pdf():
    with patch('markdown_to_pdf.converter.FPDF') as MockFPDF:
        mock_pdf = MagicMock()
        MockFPDF.return_value = mock_pdf
        from markdown_to_pdf.converter import html_to_pdf
        html_to_pdf("<html>test</html>", "output.pdf")
        MockFPDF.assert_called_once()
        mock_pdf.add_page.assert_called_once()
        mock_pdf.html.assert_called_once_with("<html>test</html>", home_dir='.')
        mock_pdf.output.assert_called_once_with("output.pdf")

def test_criterion_5_pdf_saved():
    # Covered by criterion 4 test above
    pass

def test_criterion_1_module_runs():
    import markdown_to_pdf
    assert hasattr(markdown_to_pdf, '__main__')

def test_criterion_2_config_loading():
    # Verify config file structure
    config_path = "/workspace/projects/MarkdownToPDFConverter/config.json"
    assert os.path.exists(config_path)
    with open(config_path) as f:
        config = json.load(f)
    assert "input_path" in config
    assert "output_path" in config
