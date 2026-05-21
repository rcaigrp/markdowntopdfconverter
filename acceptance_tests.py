import os
import pytest
import json
import markdown
from unittest.mock import patch, MagicMock

class MockFPDF:
    def __init__(self):
        self.pages_added = 0
        self.last_html = None
        self.output_path = None
    def add_page(self):
        self.pages_added += 1
    def html(self, html_text, x=0, y=0):
        self.last_html = html_text
    def output(self, path):
        self.output_path = path

@pytest.fixture
def mock_fpdf_instance():
    instance = MockFPDF()
    with patch('fpdf2.FPDF', return_value=instance):
        yield instance

def test_criterion_1_module_runs():
    assert os.path.exists('markdown_to_pdf/__main__.py')
    assert os.path.exists('markdown_to_pdf/main.py')
    assert os.path.exists('markdown_to_pdf/__init__.py')

def test_criterion_2_reads_config():
    config_data = '{"input": "test.md", "output": "test.pdf"}'
    with patch('builtins.open', MagicMock(return_value=MagicMock(read=MagicMock(return_value=config_data)))):
        from markdown_to_pdf.main import load_config
        config = load_config('config.json')
        assert config['input'] == 'test.md'
        assert config['output'] == 'test.pdf'

def test_criterion_3_converts_md_to_html():
    md_text = "# Hello\n\nWorld"
    from markdown_to_pdf.main import md_to_html
    html = md_to_html(md_text)
    assert "<h1>Hello</h1>" in html
    assert "<p>World</p>" in html

def test_criterion_4_converts_html_to_pdf(mock_fpdf_instance):
    from markdown_to_pdf.main import html_to_pdf
    html_text = "<h1>Hello</h1>"
    html_to_pdf(html_text, "test.pdf")
    assert mock_fpdf_instance.output_path == "test.pdf"

def test_criterion_5_saves_pdf(mock_fpdf_instance):
    from markdown_to_pdf.main import html_to_pdf
    html_to_pdf("<h1>Test</h1>", "output.pdf")
    assert mock_fpdf_instance.output_path == "output.pdf"

def test_criterion_6_structure_valid():
    assert os.path.isdir('markdown_to_pdf')
    assert os.path.isfile('markdown_to_pdf/__init__.py')
    assert os.path.isfile('markdown_to_pdf/__main__.py')
    assert os.path.isfile('markdown_to_pdf/main.py')
