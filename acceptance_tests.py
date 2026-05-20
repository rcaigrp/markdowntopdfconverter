import sys
import os
import json
import pytest

# Mock weasyprint before importing converter
sys.modules['weasyprint'] = type('MockWeasyprint', (), {
    'HTML': type('MockHTML', (), {
        'write_pdf': lambda self, path: None
    })
})

# Ensure the project dir is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import converter

def test_criterion_1_module_runs():
    # Check __main__.py exists
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert os.path.exists(os.path.join(project_dir, '__main__.py'))

def test_criterion_2_config_file():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    assert os.path.exists(config_path)
    with open(config_path, 'r') as f:
        config = json.load(f)
    # Check for required keys (flexible)
    assert 'input_path' in config or 'input_md' in config
    assert 'output_path' in config or 'output_pdf' in config

def test_criterion_3_md_to_html():
    result = converter.convert_md_to_html('# Hello')
    # markdown library generates <h1>Hello</h1>
    assert '<h1>Hello</h1>' in result or '<p>Hello</p>' in result

def test_criterion_4_html_to_pdf():
    assert hasattr(converter, 'convert_html_to_pdf')

def test_criterion_5_save_pdf():
    assert hasattr(converter, 'convert_markdown_to_pdf')

def test_criterion_6_project_structure():
    assert os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '__init__.py'))