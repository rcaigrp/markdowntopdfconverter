import os
import sys
import json
import pytest
import unittest
from unittest.mock import patch, mock_open, MagicMock

# Add project path
sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')

from converter import load_config, read_markdown, markdown_to_html, html_to_pdf, convert_markdown_to_pdf

class TestProjectStructure(unittest.TestCase):
    def test_criterion_1_valid_structure(self):
        """Test that required files exist"""
        project_dir = '/workspace/projects/MarkdownToPDFConverter'
        assert os.path.exists(os.path.join(project_dir, '__main__.py'))
        assert os.path.exists(os.path.join(project_dir, 'converter.py'))
        assert os.path.exists(os.path.join(project_dir, 'config.json'))

class TestConfig(unittest.TestCase):
    def test_criterion_2_reads_config(self):
        """Test that config file is read correctly"""
        config = load_config()
        assert config['input_path'] == 'input.md'
        assert config['output_path'] == 'output.pdf'

class TestMarkdownConversion(unittest.TestCase):
    def test_criterion_3_converts_markdown_to_html(self):
        """Test markdown to HTML conversion"""
        md = "# Hello\\nWorld"
        html = markdown_to_html(md)
        assert "<html><body>" in html
        assert "</body></html>" in html
        assert "<h1>Hello</h1>" in html
        assert "<p>World</p>" in html

class TestHtmlPdfConversion(unittest.TestCase):
    @patch('converter.FPDF')
    def test_criterion_4_converts_html_to_pdf(self, MockFPDF):
        """Test HTML to PDF conversion"""
        mock_pdf = MockFPDF.return_value
        html = "<html><body><p>Test</p></body></html>"
        result = html_to_pdf(html, '/tmp/output.pdf')
        
        assert result is True
        mock_pdf.add_page.assert_called_once()
        mock_pdf.add_html.assert_called_once_with(html)
        mock_pdf.output.assert_called_once_with('/tmp/output.pdf')

class TestHtmlPdfConversionIntegration(unittest.TestCase):
    @patch('converter.FPDF')
    def test_criterion_5_saves_pdf(self, MockFPDF):
        """Test that PDF is saved to correct location"""
        mock_pdf = MockFPDF.return_value
        html = "<html><body><p>Test</p></body></html>"
        result = html_to_pdf(html, '/tmp/output.pdf')
        
        assert result is True
        mock_pdf.output.assert_called_once_with('/tmp/output.pdf')

class TestModuleExecution(unittest.TestCase):
    @patch('converter.FPDF')
    @patch('converter.read_markdown')
    @patch('converter.markdown_to_html')
    def test_criterion_6_full_conversion(self, mock_md_html, mock_md_read, MockFPDF):
        """Test full markdown to PDF conversion"""
        mock_md_read.return_value = "# Test\\nContent"
        mock_md_html.return_value = "<html><body><h1>Test</h1><p>Content</p></body></html>"
        
        mock_pdf = MockFPDF.return_value
        result = convert_markdown_to_pdf('test.md', 'output.pdf')
        
        assert result is True
        mock_pdf.output.assert_called_once_with('output.pdf')
