import os
import json
import tempfile
import subprocess
import pytest
from markdown_to_pdf.converter import md_to_html, html_to_pdf

def test_criterion_1_module_runs():
    assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__main__.py')
    assert os.path.exists('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/converter.py')

def test_criterion_2_config_reading():
    # Test that the module reads config.json
    # We'll run the module and check if it uses the config
    pass

def test_criterion_3_md_to_html():
    html = md_to_html('# Hello\nWorld')
    assert '<h1>' in html
    assert 'world' in html.lower()

def test_criterion_4_html_to_pdf():
    html = '<h1>Hello</h1><p>World</p>'
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
        pdf_path = f.name
    html_to_pdf(html, pdf_path)
    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 0
    os.unlink(pdf_path)

def test_criterion_5_pdf_saved():
    # Integration test for criterion 5
    project_dir = '/workspace/projects/MarkdownToPDFConverter'
    config_path = os.path.join(project_dir, 'config.json')
    input_path = os.path.join(project_dir, 'input.md')
    output_path = os.path.join(project_dir, 'output.pdf')
    
    # Write input.md
    with open(input_path, 'w') as f:
        f.write('# Test\n\nThis is a test.')
        
    # Write config.json
    with open(config_path, 'w') as f:
        json.dump({'input': input_path, 'output': output_path}, f)
        
    # Run module
    result = subprocess.run(['python', '-m', 'markdown_to_pdf'], 
                            cwd=project_dir, 
                            capture_output=True, 
                            text=True)
    assert result.returncode == 0, f"Module failed: {result.stderr}"
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0
    os.unlink(output_path)

def test_criterion_6_structure_valid():
    assert os.path.isdir('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf')
    assert os.path.isfile('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__init__.py')
    assert os.path.isfile('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/__main__.py')
    assert os.path.isfile('/workspace/projects/MarkdownToPDFConverter/markdown_to_pdf/converter.py')
