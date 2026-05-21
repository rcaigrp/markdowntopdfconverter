import os
import json
import pytest
from unittest.mock import patch, mock_open, MagicMock
import sys

sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')

class TestMarkdownToPDF:
    def test_criterion_6_valid_structure(self):
        base = '/workspace/projects/MarkdownToPDFConverter'
        assert os.path.exists(f"{base}/markdown_to_pdf/__init__.py")
        assert os.path.exists(f"{base}/markdown_to_pdf/__main__.py")
        assert os.path.exists(f"{base}/markdown_to_pdf/converter.py")
        assert os.path.exists(f"{base}/config.json")

    def test_criterion_2_reads_config(self):
        with open('/workspace/projects/MarkdownToPDFConverter/config.json') as f:
            config = json.load(f)
        assert 'input' in config
        assert 'output' in config

    @patch('markdown_to_pdf.converter.markdown')
    def test_criterion_3_converts_md_to_html(self, mock_md):
        mock_md.markdown.return_value = "<p>Converted</p>"
        from markdown_to_pdf import converter
        result = converter.md_to_html("# Hello")
        assert "<p>Converted</p>" in result

    @patch('markdown_to_pdf.converter.html2text')
    @patch('markdown_to_pdf.converter.canvas')
    def test_criterion_4_converts_html_to_pdf(self, mock_canvas, mock_html2text):
        mock_html2text.HTML.return_value.process_text.return_value = "Hello World"
        mock_canvas.Canvas = MagicMock()
        
        from markdown_to_pdf import converter
        converter.html_to_pdf("<p>Test</p>", "test.pdf")
        
        mock_html2text.HTML.return_value.process_text.assert_called_once_with("<p>Test</p>")
        mock_canvas.Canvas.assert_called_once_with("test.pdf")
        mock_canvas.Canvas.return_value.drawString.assert_called_once_with(100, 750, "Hello World")
        mock_canvas.Canvas.return_value.save.assert_called_once()

    @patch('builtins.open', mock_open(read_data="# Test"))
    @patch('markdown_to_pdf.converter.markdown')
    @patch('markdown_to_pdf.converter.html2text')
    @patch('markdown_to_pdf.converter.canvas')
    def test_criterion_5_saves_pdf(self, mock_canvas, mock_h2t, mock_md):
        mock_md.markdown.return_value = "<p>Test</p>"
        mock_h2t.HTML.return_value.process_text.return_value = "Test Text"
        
        with patch('markdown_to_pdf.converter.read_config') as mock_rc:
            mock_rc.return_value = {'input': 'input.md', 'output': 'output.pdf'}
            
            from markdown_to_pdf import converter
            converter.convert('input.md', 'output.pdf', 'config.json')
            
            mock_canvas.Canvas.assert_called_once_with('output.pdf')
            mock_canvas.Canvas.return_value.drawString.assert_called_once_with(100, 750, 'Test Text')
            mock_canvas.Canvas.return_value.save.assert_called_once()
