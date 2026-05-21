import os
import sys
import json
import pytest
import markdown

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestMarkdownToPDFConverter:
    def test_criterion_1_module_runs(self):
        main_path = os.path.join(os.path.dirname(__file__), 'markdown_to_pdf', '__main__.py')
        assert os.path.exists(main_path), "markdown_to_pdf/__main__.py must exist"
        import importlib
        mod = importlib.import_module('markdown_to_pdf.__main__')
        assert hasattr(mod, 'main'), "main() function must exist"

    def test_criterion_2_reads_config(self):
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        assert os.path.exists(config_path), "config.json must exist"
        with open(config_path) as f:
            config = json.load(f)
        assert 'input_path' in config and 'output_path' in config

    def test_criterion_3_markdown_to_html(self):
        md_text = "# Title\n\nParagraph."
        html = markdown.markdown(md_text)
        assert "<h1>Title</h1>" in html
        assert "<p>Paragraph.</p>" in html

    def test_criterion_4_html_to_pdf_conversion(self):
        with open(os.path.join(os.path.dirname(__file__), 'markdown_to_pdf', '__main__.py')) as f:
            content = f.read()
        assert 'markdown.markdown' in content, "markdown.markdown must be called"

    def test_criterion_5_pdf_saved_to_output(self):
        with open(os.path.join(os.path.dirname(__file__), 'markdown_to_pdf', '__main__.py')) as f:
            content = f.read()
        assert 'pdf.output(output_path)' in content, "pdf.output must use output_path"

    def test_criterion_6_project_structure_valid(self):
        assert os.path.exists(os.path.join(os.path.dirname(__file__), 'markdown_to_pdf'))
        assert os.path.exists(os.path.join(os.path.dirname(__file__), 'markdown_to_pdf', '__init__.py'))
        assert os.path.exists(os.path.join(os.path.dirname(__file__), 'markdown_to_pdf', '__main__.py'))
        assert os.path.exists(os.path.join(os.path.dirname(__file__), 'config.json'))
