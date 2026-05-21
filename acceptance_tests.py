import os
import pytest
from unittest.mock import patch, MagicMock
import sys

sys.path.insert(0, '/workspace')

class TestMarkdownToPDF:
    @patch('markdown.markdown')
    @patch('markdown_to_pdf.converter.PDF')
    def test_convert_creates_pdf(self, mock_pdf_class, mock_markdown):
        mock_markdown.return_value = "<h1>Test</h1><p>Content</p>"
        mock_pdf_instance = MagicMock()
        mock_pdf_class.return_value = mock_pdf_instance
        
        input_path = '/workspace/projects/MarkdownToPDFConverter/test_input.md'
        output_path = '/workspace/projects/MarkdownToPDFConverter/test_output.pdf'
        
        os.makedirs(os.path.dirname(input_path), exist_ok=True)
        with open(input_path, 'w') as f:
            f.write("# Test\nContent")
            
        from markdown_to_pdf.converter import convert
        convert(input_path, output_path)
        
        mock_markdown.assert_called_once_with("# Test\nContent")
        mock_pdf_instance.add_page.assert_called_once()
        mock_pdf_instance.set_font.assert_called_once_with("Courier", size=12)
        mock_pdf_instance.add_html.assert_called_once_with("<h1>Test</h1><p>Content</p>")
        mock_pdf_instance.output.assert_called_once_with(output_path)
