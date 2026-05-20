import os
import json
import subprocess
import sys
import unittest
from unittest.mock import patch, MagicMock
import pytest

class TestMarkdownToPDFConverter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project_dir = os.path.dirname(os.path.abspath(__file__))
        cls.config_path = os.path.join(cls.project_dir, 'config.json')
        cls.input_path = os.path.join(cls.project_dir, 'test_input.md')
        cls.output_path = os.path.join(cls.project_dir, 'test_output.pdf')
        
        if not os.path.exists(cls.config_path):
            with open(cls.config_path, 'w') as f:
                json.dump({"input": "test_input.md", "output": "test_output.pdf"}, f)
        
        with open(cls.input_path, 'w') as f:
            f.write("# Test\n- Item 1")

    def test_criterion_1_module_runs(self):
        result = subprocess.run(
            [sys.executable, '-m', 'MarkdownToPDFConverter'],
            cwd=self.project_dir,
            capture_output=True,
            text=True,
            env={**os.environ, 'PYTHONPATH': self.project_dir}
        )
        assert result.returncode == 0, f"Module failed: {result.stderr}"

    def test_criterion_2_reads_config(self):
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        assert 'input' in config and 'output' in config

    def test_criterion_3_convert_md_to_html(self):
        import markdown
        html = markdown.markdown("# Test\n- Item 1")
        assert "<h1>Test</h1>" in html
        assert "<li>Item 1</li>" in html

    def test_criterion_4_html_to_pdf(self):
        from convert import PDFConverter
        html = "<html><body><h1>Test</h1></body></html>"
        pdf = PDFConverter()
        pdf.add_page()
        pdf.write_html(html)
        assert isinstance(pdf, PDFConverter)

    def test_criterion_5_saves_pdf(self):
        from convert import convert_md_to_pdf
        output_path = self.output_path
        if os.path.exists(output_path):
            os.remove(output_path)
        
        convert_md_to_pdf(self.input_path, output_path)
        assert os.path.exists(output_path)

    def test_criterion_6_valid_structure(self):
        assert os.path.exists(self.project_dir)
        assert os.path.exists(os.path.join(self.project_dir, '__main__.py'))
        assert os.path.exists(os.path.join(self.project_dir, 'convert.py'))

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
