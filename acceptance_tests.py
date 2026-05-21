import os
import json
import unittest
from unittest.mock import patch, MagicMock

class TestMarkdownToPDF(unittest.TestCase):
    def test_criterion_1_module_runs(self):
        import markdown_to_pdf.__main__
        self.assertTrue(hasattr(markdown_to_pdf.__main__, "main"))

    def test_criterion_2_reads_config(self):
        from markdown_to_pdf.core import ConfigLoader
        config_path = "config.json"
        with open(config_path, 'w') as f:
            json.dump({"input_path": "input.md", "output_path": "output.pdf"}, f)
        
        config_loader = ConfigLoader(config_path)
        self.assertEqual(config_loader.get_input_path(), "input.md")
        self.assertEqual(config_loader.get_output_path(), "output.pdf")

    def test_criterion_3_md_to_html(self):
        from markdown_to_pdf.core import Converter
        converter = Converter("config.json")
        html = converter.md_to_html("# Hello\n\nWorld")
        self.assertIn("<h1>", html)
        self.assertIn("<p>", html)

    def test_criterion_4_html_to_pdf(self):
        from markdown_to_pdf.core import Converter
        converter = Converter("config.json")
        html = converter.md_to_html("# Hello")
        with patch('markdown_to_pdf.core.FPDF') as MockFPDF:
            mock_pdf = MagicMock()
            MockFPDF.return_value = mock_pdf
            pdf = converter.html_to_pdf(html)
            self.assertEqual(pdf, mock_pdf)

    def test_criterion_5_saves_pdf(self):
        from markdown_to_pdf.core import Converter
        converter = Converter("config.json")
        with patch('markdown_to_pdf.core.FPDF') as MockFPDF:
            mock_pdf = MagicMock()
            MockFPDF.return_value = mock_pdf
            converter.save_pdf(mock_pdf, "output.pdf")
            mock_pdf.output.assert_called_once_with("output.pdf")

    def test_criterion_6_project_structure_valid(self):
        self.assertTrue(os.path.exists("markdown_to_pdf/__init__.py"))
        self.assertTrue(os.path.exists("markdown_to_pdf/__main__.py"))
