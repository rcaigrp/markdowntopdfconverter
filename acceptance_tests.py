import unittest
import os
from unittest.mock import patch, MagicMock
import markdown
from fpdf2 import FPDF


class TestMarkdownToPDFConverter(unittest.TestCase):
    @patch('markdown.markdown')
    def test_convert_md_to_html(self, mock_md):
        md_text = "# Hello\n- World"
        mock_md.return_value = "<h1>Hello</h1><ul><li>World</li></ul>"
        from markdown_to_pdf.core import convert_md_to_html
        result = convert_md_to_html(md_text)
        mock_md.assert_called_once_with(md_text)
        self.assertEqual(result, "<h1>Hello</h1><ul><li>World</li></ul>")

    @patch('fpdf2.FPDF')
    def test_convert_html_to_pdf(self, mock_pdf_class):
        mock_pdf_instance = MagicMock()
        mock_pdf_class.return_value = mock_pdf_instance
        html = "<h1>Hello</h1>"
        output_path = "/tmp/test.pdf"
        from markdown_to_pdf.core import convert_html_to_pdf
        convert_html_to_pdf(html, output_path)
        
        # Check that FPDF was instantiated
        mock_pdf_class.assert_called_once()
        pdf_instance = mock_pdf_class.return_value
        
        # Check methods called
        self.assertTrue(pdf_instance.add_page.called)
        self.assertTrue(pdf_instance.html.called_with(html, safe_mode='escape'))
        self.assertTrue(pdf_instance.output.called_with(output_path))


if __name__ == '__main__':
    unittest.main()
