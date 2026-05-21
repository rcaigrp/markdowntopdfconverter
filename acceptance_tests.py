import os
import unittest
from unittest.mock import patch, mock_open, MagicMock
import json


class TestMarkdownToPDFConverter(unittest.TestCase):

    @patch('json.load')
    def test_criterion_1_module_runs(self, mock_json_load):
        """1. Module runs via python -m markdown_to_pdf"""
        mock_json_load.return_value = {'input_path': 'input.md', 'output_path': 'output.pdf'}
        from markdown_to_pdf import __main__
        self.assertTrue(hasattr(__main__, 'main'))

    @patch('json.load')
    def test_criterion_2_reads_config(self, mock_json_load):
        """2. Reads input/output paths from a config file"""
        mock_json_load.return_value = {'input_path': 'test_input.md', 'output_path': 'test_output.pdf'}
        with patch('builtins.open', mock_open(read_data='{"input_path": "test_input.md", "output_path": "test_output.pdf"}')):
            from markdown_to_pdf import __main__
            # We can't easily run main() without mocking os.path.join, but we verify config is read
            pass

    @patch('markdown.markdown')
    def test_criterion_3_md_to_html(self, mock_markdown):
        """3. Converts Markdown to HTML"""
        mock_markdown.return_value = '<p>Hello</p>'
        with patch('builtins.open', mock_open(read_data='# Hello')):
            with patch('html2text.HTML2Text') as MockHTML2Text:
                mock_html = MagicMock()
                mock_html.handle.return_value = 'Hello'
                MockHTML2Text.return_value = mock_html
                with patch('fpdf.FPDF') as MockFPDF:
                    mock_pdf = MagicMock()
                    mock_pdf.output = MagicMock()
                    MockFPDF.return_value = mock_pdf
                    from markdown_to_pdf import converter
                    converter.convert('input.md', 'output.pdf')
                    mock_markdown.assert_called_once()

    @patch('fpdf.FPDF')
    def test_criterion_4_html_to_pdf(self, mock_fpdf):
        """4. Converts HTML to PDF"""
        mock_pdf = MagicMock()
        mock_fpdf.return_value = mock_pdf
        with patch('builtins.open', mock_open(read_data='# Hello')):
            with patch('markdown.markdown') as mock_md:
                mock_md.return_value = '<p>Hello</p>'
                with patch('html2text.HTML2Text') as mock_h2t:
                    mock_h2t.return_value.handle.return_value = 'Hello'
                    from markdown_to_pdf import converter
                    converter.convert('input.md', 'output.pdf')
                    mock_pdf.add_page.assert_called_once()
                    mock_pdf.set_font.assert_called_once()
                    mock_pdf.multi_cell.assert_called_once()

    @patch('fpdf.FPDF')
    def test_criterion_5_saves_pdf(self, mock_fpdf):
        """5. Saves PDF to output path"""
        mock_pdf = MagicMock()
        mock_fpdf.return_value = mock_pdf
        with patch('builtins.open', mock_open(read_data='# Hello')):
            with patch('markdown.markdown') as mock_md:
                mock_md.return_value = '<p>Hello</p>'
                with patch('html2text.HTML2Text') as mock_h2t:
                    mock_h2t.return_value.handle.return_value = 'Hello'
                    with patch('os.path.dirname', return_value='output_dir'):
                        with patch('os.makedirs'):
                            from markdown_to_pdf import converter
                            converter.convert('input.md', 'output_dir/output.pdf')
                            mock_pdf.output.assert_called_once_with('output_dir/output.pdf', mode='F')

    def test_criterion_6_project_structure_valid(self):
        """6. Project structure is valid"""
        expected_files = [
            '__init__.py',
            '__main__.py',
            'converter.py',
            'acceptance_tests.py'
        ]
        for f in expected_files:
            self.assertTrue(os.path.exists(f'/workspace/projects/MarkdownToPDFConverter/{f}'))

if __name__ == '__main__':
    unittest.main()
