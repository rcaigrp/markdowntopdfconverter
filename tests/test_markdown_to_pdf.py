import sys
import os
import pytest
import responses
from unittest.mock import patch, MagicMock

sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')

from markdown_to_pdf.main import read_config, md_to_html, html_to_pdf, convert

class TestMarkdownToPDFConverter:
    @responses.activate
    def test_criterion_1_module_runs(self):
        import importlib.util
        spec = importlib.util.find_spec('markdown_to_pdf')
        assert spec is not None
        assert spec.origin == '/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__init__.py'

    @responses.activate
    def test_criterion_2_reads_config(self):
        config = read_config()
        assert 'input' in config
        assert 'output' in config

    @patch('markdown.markdown')
    def test_criterion_3_converts_md_to_html(self, mock_md):
        mock_md.return_value = "<h1>Hello World</h1>"
        md_text = "# Hello World"
        html = md_to_html(md_text)
        assert "<h1>Hello World</h1>" in html

    @responses.activate
    def test_criterion_4_converts_html_to_pdf(self):
        with patch('markdown_to_pdf.main.html2pdf') as mock_html2pdf:
            html_text = "<h1>Hello World</h1>"
            html_to_pdf(html_text, 'test_output.pdf')
            mock_html2pdf.assert_called_once_with(html=html_text, output='test_output.pdf')

    @patch('markdown.markdown')
    @patch('markdown_to_pdf.main.html2pdf')
    def test_criterion_5_saves_pdf(self, mock_html2pdf, mock_md):
        mock_md.return_value = "<h1>Hello</h1>"
        with patch('builtins.open', MagicMock()):
            convert('input.md', 'output.pdf')
            mock_html2pdf.assert_called_once_with(html="<h1>Hello</h1>", output='output.pdf')

    def test_criterion_6_project_structure_valid(self):
        assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__init__.py')
        assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/main.py')
        assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__main__.py')
        assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/config.json')
        assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/requirements.txt')
