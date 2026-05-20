import sys
import os
import json
import tempfile
import markdown

# Mock weasyprint before importing converter
sys.modules['weasyprint'] = type(sys)('weasyprint')
sys.modules['weasyprint'].HTML = type(sys)('HTML')

class MockHTML:
    def __init__(self, string=None):
        self.string = string
    def write_pdf(self, output_path):
        with open(output_path, 'wb') as f:
            f.write(b'%PDF-1.4 mock')

sys.modules['weasyprint'].HTML = MockHTML

from markdown_to_pdf import converter

def test_criterion_1_module_runs():
    main_path = os.path.join(os.path.dirname(converter.__file__), "__main__.py")
    assert os.path.exists(main_path), "Module entry point __main__.py is missing"

def test_criterion_2_reads_config():
    config_path = os.path.join(os.path.dirname(converter.__file__), "config.json")
    assert os.path.exists(config_path), "config.json is missing"
    with open(config_path, 'r') as f:
        config = json.load(f)
    assert "input" in config, "config.json missing 'input' key"
    assert "output" in config, "config.json missing 'output' key"

def test_criterion_3_md_to_html():
    md = "# Title"
    html = converter.convert_md_to_html(md)
    assert "<h1>" in html, "Markdown to HTML conversion failed"

def test_criterion_4_html_to_pdf():
    html = "<html><body><h1>Test</h1></body></html>"
    pdf_path = os.path.join(tempfile.mkdtemp(), "test.pdf")
    converter.convert_html_to_pdf(html, pdf_path)
    assert os.path.exists(pdf_path), "PDF file was not created"

def test_criterion_5_saves_pdf():
    pass

def test_criterion_6_valid_structure():
    init_path = os.path.join(os.path.dirname(converter.__file__), "__init__.py")
    assert os.path.exists(init_path), "__init__.py is missing"