import unittest
import json
import os
from unittest.mock import patch, mock_open
import sys

class TestMarkdownToPDF(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data='{"input": "input.md", "output": "output.pdf"}'))
    def test_load_config(self):
        from markdown_to_pdf.converter import load_config
        config = load_config()
        self.assertEqual(config['input'], 'input.md')
        self.assertEqual(config['output'], 'output.pdf')

    def test_md_to_html(self):
        from markdown_to_pdf.converter import md_to_html
        md_text = "# Hello\n- Item"
        html = md_to_html(md_text)
        self.assertIn('<h1>Hello</h1>', html)
        self.assertIn('<li>Item</li>', html)

    @patch('markdown_to_pdf.converter.PDF')
    def test_html_to_pdf(self, MockPDF):
        from markdown_to_pdf.converter import html_to_pdf
        html = "<h1>Hello</h1>"
        html_to_pdf(html, 'output.pdf')
        MockPDF.assert_called_once()
