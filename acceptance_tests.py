import sys
import os
import unittest
from unittest.mock import patch, MagicMock
import json

sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')
import converter

class TestMarkdownToPDFConverter(unittest.TestCase):
    @patch('builtins.open', unittest.mock.mock_open(read_data=json.dumps({"input": "test.md", "output": "test.pdf"})))
    def test_read_config(self):
        config = converter.read_config("dummy.json")
        self.assertEqual(config, {"input": "test.md", "output": "test.pdf"})

    def test_md_to_html(self):
        md = "# Hello"
        html = converter.md_to_html(md)
        self.assertIn("<h1>", html)

    def test_html_to_text(self):
        html = "<h1>Hello</h1>"
        text = converter.html_to_text(html)
        self.assertIn("Hello", text)

    @patch('converter.FPDF')
    def test_text_to_pdf(self, mock_fpdf_class):
        mock_pdf = MagicMock()
        mock_fpdf_class.return_value = mock_pdf
        
        converter.text_to_pdf("Test text", "output.pdf")
        
        mock_fpdf_class.assert_called_once()
        mock_pdf.add_page.assert_called_once()
        mock_pdf.set_font.assert_called_once_with("Arial", size=12)
        mock_pdf.multi_cell.assert_called_once()
        mock_pdf.output.assert_called_once_with("output.pdf")
