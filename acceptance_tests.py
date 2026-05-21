import sys
import os
import pytest
import json
from unittest.mock import patch, MagicMock

sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')

@pytest.fixture
def setup_paths(tmp_path):
    config = {"input_path": str(tmp_path / "input.md"), "output_path": str(tmp_path / "output.pdf")}
    with open(config['input_path'], 'w') as f:
        f.write("# Hello\n\nWorld")
    return config

@patch('builtins.open')
@patch('markdown.markdown')
@patch('fpdf.FPDF')
def test_criterion_3_converts_md_to_html(mock_pdf_class, mock_markdown, mock_open, setup_paths):
    mock_open.return_value.__enter__ = lambda s: s
    mock_open.return_value.__exit__ = lambda s, *args: None
    mock_open.return_value.read.return_value = "# Hello\n\nWorld"
    mock_markdown.return_value = "<h1>Hello</h1><p>World</p>"
    
    from markdown_to_pdf.converter import convert_md_to_pdf
    convert_md_to_pdf(setup_paths['input_path'], setup_paths['output_path'])
    
    assert mock_markdown.called
    assert mock_pdf_class().html.called

@patch('builtins.open')
@patch('markdown.markdown')
@patch('fpdf.FPDF')
def test_criterion_4_converts_html_to_pdf(mock_pdf_class, mock_markdown, mock_open, setup_paths):
    mock_open.return_value.__enter__ = lambda s: s
    mock_open.return_value.__exit__ = lambda s, *args: None
    mock_open.return_value.read.return_value = "# Hello"
    mock_markdown.return_value = "<h1>Hello</h1>"
    
    from markdown_to_pdf.converter import convert_md_to_pdf
    pdf_instance = mock_pdf_class()
    convert_md_to_pdf(setup_paths['input_path'], setup_paths['output_path'])
    
    assert pdf_instance.html.called

@patch('builtins.open')
@patch('markdown.markdown')
@patch('fpdf.FPDF')
def test_criterion_5_saves_pdf(mock_pdf_class, mock_markdown, mock_open, setup_paths):
    mock_open.return_value.__enter__ = lambda s: s
    mock_open.return_value.__exit__ = lambda s, *args: None
    mock_open.return_value.read.return_value = "# Hello"
    mock_markdown.return_value = "<h1>Hello</h1>"
    
    from markdown_to_pdf.converter import convert_md_to_pdf
    pdf_instance = mock_pdf_class()
    convert_md_to_pdf(setup_paths['input_path'], setup_paths['output_path'])
    
    assert pdf_instance.output.called
    assert pdf_instance.output.call_args[0][0] == setup_paths['output_path']

@patch('builtins.open')
@patch('json.load')
def test_criterion_2_reads_config(mock_json_load, mock_open):
    config_path = '/workspace/projects/MarkdownToPDFConverter/config.json'
    assert os.path.exists(config_path)
    with open(config_path, 'r') as f:
        config = json.load(f)
    assert 'input_path' in config
    assert 'output_path' in config

def test_criterion_1_module_runs():
    from markdown_to_pdf import __main__
    assert hasattr(__main__, 'main')

def test_criterion_6_project_structure_valid():
    assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__init__.py')
    assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/converter.py')
    assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__main__.py')
    assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/config.json')
