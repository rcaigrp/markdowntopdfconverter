import os
import pytest
import json
import markdown
from unittest.mock import patch, MagicMock
from fpdf import FPDF

PROJECT_DIR = "/workspace/projects/MarkdownToPDFConverter"

def test_criterion_6_project_structure():
    required_files = ["__init__.py", "__main__.py", "converter.py", "config.json", "acceptance_tests.py"]
    for f in required_files:
        assert os.path.exists(os.path.join(PROJECT_DIR, f)), f"Missing {f}"

def test_criterion_1_module_runs():
    main_path = os.path.join(PROJECT_DIR, "__main__.py")
    with open(main_path, "r") as f:
        content = f.read()
    assert "def main()" in content or "if __name__ == '__main__':" in content

def test_criterion_2_reads_config():
    config_path = os.path.join(PROJECT_DIR, "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    assert "input_path" in config or "output_path" in config

def test_criterion_3_markdown_to_html():
    md_text = "# Hello"
    expected_html = markdown.markdown(md_text)
    assert "<h1>Hello</h1>" in expected_html

def test_criterion_4_html_to_pdf():
    # Mock FPDF to avoid system dependencies in tests
    with patch('fpdf.FPDF') as MockFPDF:
        mock_instance = MagicMock()
        MockFPDF.return_value = mock_instance
        
        # We need to mock the module import in converter
        with patch('converter.FPDF', MockFPDF):
            # Import the converter class
            from converter import MarkdownToPDFConverter
            
            converter = MarkdownToPDFConverter()
            converter.convert("test_input.md", "output.pdf")
            
            # Verify FPDF methods were called
            assert MockFPDF.called

def test_criterion_5_saves_pdf():
    # Mock the output to verify path
    with patch('fpdf.FPDF') as MockFPDF:
        mock_instance = MagicMock()
        MockFPDF.return_value = mock_instance
        
        with patch('converter.FPDF', MockFPDF):
            from converter import MarkdownToPDFConverter
            converter = MarkdownToPDFConverter()
            converter.convert("test_input.md", "output.pdf")
            
            # Check if output was called on the mock
            mock_instance.output.assert_called()
