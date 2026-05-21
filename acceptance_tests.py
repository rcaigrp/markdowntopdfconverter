import unittest
from unittest.mock import patch, mock_open
import json
import os

class TestMarkdownToPDF(unittest.TestCase):
    @patch('fpdf.FPDF')
    def test_criterion_3_converts_md_to_html(self, mock_fpdf):
        from markdown_to_pdf.converter import md_to_html
        result = md_to_html("# Test\nHello")
        self.assertIn("Test", result)
        self.assertIn("Hello", result)

    @patch('fpdf.FPDF')
    def test_criterion_4_converts_html_to_pdf(self, mock_fpdf):
        from markdown_to_pdf.converter import html_to_pdf
        html_to_pdf("<h1>Hi</h1>", "test.pdf")
        mock_fpdf.return_value.add_page.assert_called_once()
        mock_fpdf.return_value.output.assert_called_once_with("test.pdf", "F")

    @patch('fpdf.FPDF')
    @patch('builtins.open', mock_open(read_data="# Test"))
    @patch('json.load', return_value={"input_path": "in.md", "output_path": "out.pdf"})
    def test_criterion_5_saves_pdf(self, mock_json, mock_open, mock_fpdf):
        from markdown_to_pdf.converter import convert_md_to_pdf
        convert_md_to_pdf("in.md", "out.pdf")
        mock_fpdf.return_value.output.assert_called_once_with("out.pdf", "F")

    def test_criterion_6_project_structure_valid(self):
        self.assertTrue(os.path.exists("/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/converter.py"))
        self.assertTrue(os.path.exists("/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__main__.py"))
