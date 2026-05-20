import unittest
import json
import os
import ast
from unittest.mock import patch, mock_open

class TestMarkdownToPDFConverter(unittest.TestCase):
    def setUp(self):
        self.config_path = '/tmp/config.json'
        self.input_path = '/tmp/input.md'
        self.output_path = '/tmp/output.pdf'
        
        with open(self.config_path, 'w') as f:
            json.dump({'input_path': self.input_path, 'output_path': self.output_path}, f)
            
        with open(self.input_path, 'w') as f:
            f.write('# Hello\n\nWorld')

    def test_criterion_1_module_runs(self):
        with open('/workspace/projects/MarkdownToPDFConverter/__main__.py') as f:
            tree = ast.parse(f.read())
        has_main = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'main':
                has_main = True
        self.assertTrue(has_main)

    def test_criterion_2_reads_config(self):
        from converter import load_config
        input_path, output_path = load_config(self.config_path)
        self.assertEqual(input_path, self.input_path)
        self.assertEqual(output_path, self.output_path)

    def test_criterion_3_convert_md_to_html(self):
        from converter import convert_markdown_to_html
        html = convert_markdown_to_html('# Hello\n\nWorld')
        self.assertIn('<h1>', html)
        self.assertIn('<p>', html)

    @patch('weasyprint.HTML')
    def test_criterion_4_convert_html_to_pdf(self, mock_html):
        from converter import convert_html_to_pdf
        mock_instance = mock_html.return_value
        mock_instance.write_pdf = mock_open()
        
        convert_html_to_pdf('<h1>Hello</h1>', self.output_path)
        mock_html.assert_called_once_with(string='<h1>Hello</h1>')

    def test_criterion_5_saves_pdf(self):
        with patch('weasyprint.HTML') as MockHTML:
            mock_instance = MockHTML.return_value
            mock_instance.write_pdf = mock_open()
            
            from converter import run
            run(self.input_path, self.output_path)
            
            MockHTML.assert_called_once()
            MockHTML.return_value.write_pdf.assert_called_once_with(self.output_path)

    def test_criterion_6_valid_structure(self):
        self.assertTrue(os.path.exists('/workspace/projects/MarkdownToPDFConverter/__main__.py'))
        self.assertTrue(os.path.exists('/workspace/projects/MarkdownToPDFConverter/converter.py'))
        self.assertTrue(os.path.exists('/workspace/projects/MarkdownToPDFConverter/config.json'))

if __name__ == '__main__':
    unittest.main()
