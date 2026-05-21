import unittest
import os
import json
import sys
from unittest.mock import patch, mock_open

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestMarkdownToPDF(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data="# Hello"))
    @patch('markdown.markdown', return_value="<h1>Hello</h1>")
    @patch('fpdf.FPDF')
    def test_criterion_3_md_to_html(self, mock_pdf_class, mock_markdown):
        from markdown_to_pdf.converter import convert_md_to_pdf
        convert_md_to_pdf('input.md', 'output.pdf')
        mock_markdown.assert_called_once()

    @patch('fpdf.FPDF')
    @patch('builtins.open', mock_open(read_data="# Hello"))
    @patch('markdown.markdown', return_value="<h1>Hello</h1>")
    def test_criterion_5_saves_pdf(self, mock_pdf_class, mock_markdown):
        from markdown_to_pdf.converter import convert_md_to_pdf
        convert_md_to_pdf('input.md', 'output.pdf')
        mock_pdf_class.return_value.output.assert_called_once_with('output.pdf', dest='F')

    @patch('json.load', return_value={'input_path': 'test.md', 'output_path': 'test.pdf'})
    @patch('markdown_to_pdf.converter.convert_md_to_pdf')
    def test_criterion_2_reads_config(self, mock_convert, mock_load):
        from markdown_to_pdf import __main__
        __main__.main()
        mock_convert.assert_called_once_with('test.md', 'test.pdf')

    def test_criterion_1_module_runs(self):
        from markdown_to_pdf import __main__
        assert callable(__main__.main)

    def test_criterion_6_valid_structure(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        assert os.path.isdir(os.path.join(project_root, 'markdown_to_pdf'))
        assert os.path.exists(os.path.join(project_root, 'markdown_to_pdf', '__init__.py'))
        assert os.path.exists(os.path.join(project_root, 'markdown_to_pdf', '__main__.py'))

if __name__ == '__main__':
    unittest.main()
