import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestMarkdownToPDF(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    @patch('markdown.markdown')
    @patch('converter.FPDF')
    def test_complete_pipeline(self, mock_fpdf, mock_md, mock_json_load, mock_open_func):
        mock_json_load.return_value = {'input_path': 'input.md', 'output_path': 'output.pdf'}
        mock_md.return_value = '<h1>Test</h1>'
        mock_open_func.return_value.read.return_value = '# Test'
        
        mock_pdf = MagicMock()
        mock_fpdf.return_value = mock_pdf
        
        from markdown_to_pdf import __main__
        __main__.main()
        
        mock_json_load.assert_called()
        mock_md.assert_called_once_with('# Test')
        mock_pdf.output.assert_called_once_with(filename='output.pdf', dest='F')
