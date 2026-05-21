import json
import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import subprocess

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestMarkdownToPDFConverter(unittest.TestCase):
    def setUp(self):
        self.project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_path = os.path.join(self.project_dir, "config.json")
        self.input_path = os.path.join(self.project_dir, "input.md")
        self.output_path = os.path.join(self.project_dir, "output.pdf")
        
        with open(self.config_path, "w") as f:
            json.dump({"input": self.input_path, "output": self.output_path}, f)
        with open(self.input_path, "w") as f:
            f.write("# Test\nHello World!")

    def tearDown(self):
        for path in [self.config_path, self.input_path, self.output_path]:
            if os.path.exists(path):
                os.remove(path)

    def test_criterion_1_module_runs(self):
        result = subprocess.run(
            [sys.executable, "-m", "markdown_to_pdf"],
            capture_output=True,
            timeout=10
        )
        self.assertEqual(result.returncode, 0, f"Module failed: {result.stderr}")

    def test_criterion_2_reads_config(self):
        from markdown_to_pdf import converter
        config = converter.load_config(self.config_path)
        self.assertEqual(config["input"], self.input_path)
        self.assertEqual(config["output"], self.output_path)

    def test_criterion_3_markdown_to_html(self):
        from markdown_to_pdf import converter
        html = converter.markdown_to_html("# Hello\nWorld")
        self.assertIn("<h1>", html)
        self.assertIn("<p>", html)

    @patch("fpdf.FPDF")
    def test_criterion_4_html_to_pdf(self, mock_fpdf_class):
        mock_pdf = MagicMock()
        mock_fpdf_class.return_value = mock_pdf
        mock_pdf.output.return_value = b"%PDF-1.4"
        
        from markdown_to_pdf import converter
        pdf_bytes = converter.html_to_pdf("<h1>Test</h1>")
        self.assertEqual(pdf_bytes, b"%PDF-1.4")
        mock_fpdf_class.assert_called_once()

    def test_criterion_5_saves_pdf(self):
        with patch("fpdf.FPDF") as mock_fpdf_class:
            mock_pdf = MagicMock()
            mock_fpdf_class.return_value = mock_pdf
            mock_pdf.output.return_value = b"%PDF-1.4"
            
            from markdown_to_pdf import converter
            converter.convert(self.input_path, self.output_path, self.config_path)
            self.assertTrue(os.path.exists(self.output_path))

    def test_criterion_6_project_structure_valid(self):
        required_files = [
            "__init__.py",
            "__main__.py",
            "converter.py",
            "acceptance_tests.py",
            "config.json",
            "input.md"
        ]
        for f in required_files:
            self.assertTrue(os.path.exists(os.path.join(self.project_dir, f)), f"Missing {f}")

if __name__ == "__main__":
    unittest.main()
