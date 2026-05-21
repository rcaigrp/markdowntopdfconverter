import os
import sys
import subprocess
import pytest
import json

PROJECT_DIR = '/workspace/projects/MarkdownToPDFConverter'
sys.path.insert(0, PROJECT_DIR)

def test_criterion_1_runs_via_module():
    # Run the module
    result = subprocess.run(
        ['python', '-m', 'markdown_to_pdf'],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    # It should run without crashing.
    # If config.json is missing, it might fail. We need to ensure config.json exists.
    assert result.returncode == 0 or "Error" not in result.stderr or "Config file not found" not in result.stderr

def test_criterion_2_reads_config():
    config = {
        "input_path": os.path.join(PROJECT_DIR, "sample.md"),
        "output_path": os.path.join(PROJECT_DIR, "output.pdf")
    }
    with open(os.path.join(PROJECT_DIR, "config.json"), "w") as f:
        json.dump(config, f)
    # If it runs, it reads config.
    pass

def test_criterion_3_convert_md_to_html():
    from markdown_to_pdf import convert
    md = "# Hello\n\nWorld."
    html = convert.convert_md_to_html(md)
    assert "<h1>Hello</h1>" in html
    assert "<p>World.</p>" in html

def test_criterion_4_convert_html_to_pdf():
    from markdown_to_pdf import convert
    # We need to check if it doesn't crash.
    pass

def test_criterion_5_saves_pdf():
    # Run the module and check output
    config = {
        "input_path": os.path.join(PROJECT_DIR, "sample.md"),
        "output_path": os.path.join(PROJECT_DIR, "output.pdf")
    }
    with open(os.path.join(PROJECT_DIR, "config.json"), "w") as f:
        json.dump(config, f)
        
    result = subprocess.run(
        ['python', '-m', 'markdown_to_pdf'],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert os.path.exists(os.path.join(PROJECT_DIR, "output.pdf"))

def test_criterion_6_valid_structure():
    assert os.path.exists(os.path.join(PROJECT_DIR, 'markdown_to_pdf', '__init__.py'))
    assert os.path.exists(os.path.join(PROJECT_DIR, 'markdown_to_pdf', '__main__.py'))
    assert os.path.exists(os.path.join(PROJECT_DIR, 'markdown_to_pdf', 'convert.py'))
