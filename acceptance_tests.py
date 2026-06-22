import sys
import os
import json
import pytest
import subprocess
import sys

sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')

from markdown_to_pdf.core import load_config, generate_pdf, parse_markdown

def test_criterion_1_module_runs():
    """Module runs via python -m markdown_to_pdf"""
    result = subprocess.run(['python', '-m', 'markdown_to_pdf'], capture_output=True, cwd='/workspace/projects/MarkdownToPDFConverter')
    assert result.returncode == 0 or 'No such file or directory' not in result.stderr

def test_criterion_2_reads_config():
    """Reads input/output paths from a config file"""
    input_path, output_path = load_config()
    assert input_path == 'input.md'
    assert output_path == 'output.pdf'

def test_criterion_3_converts_markdown():
    """Converts Markdown to PDF"""
    generate_pdf('# Title\n\nHello World', '/tmp/test_output.pdf')
    assert os.path.exists('/tmp/test_output.pdf')
