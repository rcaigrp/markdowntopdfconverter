import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')

class TestMarkdownToPDFConverter(unittest.TestCase):
    @patch('markdown_to_pdf.converter.markdown')
    def test_convert_md_to_html(self, mock_markdown):
        from markdown_to_pdf.converter import convert_md_to_html
        mock_markdown.markdown.return_value = "<h1>Hello</h1>"
        result = convert_md_to_html("# Hello")
        self.assertEqual(result, "<h1>Hello</h1>")

    @patch('markdown_to_pdf.converter.FPDF')
    @patch('markdown_to_pdf.converter.HTMLMixin')
    def test_convert_html_to_pdf(self, mock_html_mixin, mock_fpdf):
        from unittest.mock import MagicMock
        from markdown_to_pdf.converter import convert_html_to_pdf
        
        mock_pdf = MagicMock()
        mock_fpdf.return_value = mock_pdf
        
        convert_html_to_pdf("<h1>Hello</h1>", "output.pdf")
        
        mock_pdf.add_page.assert_called()
        mock_pdf.write_html.assert_called_once()
        mock_pdf.output.assert_called_once_with("output.pdf")

    @patch('os.path.exists')
    @patch('builtins.open')
    @patch('json.load')
    @patch('markdown_to_pdf.converter.convert_md_to_html')
    @patch('markdown_to_pdf.converter.convert_html_to_pdf')
    def test_main_integration(self, mock_convert_pdf, mock_convert_html, mock_json_load, mock_open, mock_exists):
        from markdown_to_pdf import __main__
        
        mock_exists.return_value = True
        mock_open.return_value.__enter__ = lambda s: s
        mock_open.return_value.__exit = MagicMock()
        mock_open.return_value.read.return_value = "# Title"
        mock_json_load.return_value = {"input": "test.md", "output": "test.pdf"}
        
        __main__.main()
        
        mock_convert_html.assert_called_once()
        mock_convert_pdf.assert_called_once()
