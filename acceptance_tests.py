import pytest
from unittest.mock import patch, MagicMock
import json
import os
import sys

def test_criterion_1_runs_via_main():
    import markdown_to_pdf.__main__ as main_module
    assert hasattr(main_module, 'main')

def test_criterion_2_reads_config():
    with patch('json.load', return_value={"input_path": "in.md", "output_path": "out.pdf"}):
        from markdown_to_pdf.config import load_config
        cfg = load_config("config.json")
        assert cfg == {"input_path": "in.md", "output_path": "out.pdf"}

def test_criterion_3_convert_md_to_html():
    from markdown_to_pdf.converter import markdown_to_html
    md = "# Test\n"
    html = markdown_to_html(md)
    assert "Test" in html

def test_criterion_4_convert_html_to_pdf():
    with patch('fpdf.FPDF') as MockPDF:
        from markdown_to_pdf.converter import html_to_pdf
        html_to_pdf("<h1>Test</h1>", "test.pdf")
        assert MockPDF.called

def test_criterion_5_saves_pdf():
    with patch('fpdf.FPDF') as MockPDF:
        from markdown_to_pdf.converter import html_to_pdf
        html_to_pdf("<h1>Test</h1>", "output.pdf")
        MockPDF.return_value.output.assert_called_once_with("output.pdf", "F")

def test_criterion_6_valid_structure():
    assert os.path.exists("markdown_to_pdf/__init__.py")
    assert os.path.exists("markdown_to_pdf/__main__.py")
    assert os.path.exists("markdown_to_pdf/config.py")
    assert os.path.exists("markdown_to_pdf/converter.py")
