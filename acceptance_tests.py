import pytest
from unittest.mock import patch, mock_open
import markdown_to_pdf.converter as converter
import markdown_to_pdf.config as config

@patch('markdown.markdown')
def test_md_to_html(mock_markdown):
    mock_markdown.return_value = "<h1>Test</h1>"
    result = converter.md_to_html("# Test")
    mock_markdown.assert_called_once_with("# Test")
    assert result == "<h1>Test</h1>"

@patch('fpdf.html2pdf')
def test_html_to_pdf(mock_html2pdf):
    converter.html_to_pdf("<h1>Test</h1>", "test.pdf")
    mock_html2pdf.assert_called_once_with("<h1>Test</h1>", "test.pdf")

@patch('builtins.open', mock_open(read_data='{"input_path": "in.md", "output_path": "out.pdf"}'))
def test_load_config():
    inp, out = config.load_config("config.json")
    assert inp == "in.md"
    assert out == "out.pdf"
