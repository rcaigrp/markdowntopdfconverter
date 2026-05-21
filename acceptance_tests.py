import os
import json
import pytest
from unittest.mock import patch, MagicMock
from markdown_to_pdf.core import load_config, convert_md_to_html, convert_html_to_pdf


class TestMarkdownToPDF:
    def test_project_structure(self):
        base = '/workspace/projects/MarkdownToPDFConverter'
        assert os.path.isdir(f'{base}/markdown_to_pdf')
        assert os.path.isfile(f'{base}/markdown_to_pdf/__init__.py')
        assert os.path.isfile(f'{base}/markdown_to_pdf/__main__.py')
        assert os.path.isfile(f'{base}/markdown_to_pdf/core.py')

    def test_load_config(self):
        config = {"input": "test.md", "output": "test.pdf"}
        with open('/tmp/config.json', 'w') as f:
            json.dump(config, f)
        result = load_config('/tmp/config.json')
        assert result == config

    @patch('markdown_to_pdf.core.markdown')
    def test_convert_md_to_html(self, mock_md):
        mock_md.markdown.return_value = '<p>Hello</p>'
        result = convert_md_to_html('# Hello')
        assert result == '<p>Hello</p>'

    @patch('markdown_to_pdf.core.FPDF')
    def test_convert_html_to_pdf(self, mock_pdf_class):
        mock_pdf = MagicMock()
        mock_pdf_class.return_value = mock_pdf
        convert_html_to_pdf('<p>Test</p>', '/tmp/output.pdf')
        mock_pdf.add_page.assert_called_once()
        mock_pdf.html.assert_called_once()
        mock_pdf.output.assert_called_once_with(fname='/tmp/output.pdf')
