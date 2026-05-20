import os
import pytest
import sys
sys.path.append("/workspace/projects/MarkdownToPDFConverter")
from main import convert_md_to_pdf

def test_criterion_1_pdf_generated():
    input_path = "/workspace/projects/MarkdownToPDFConverter/input.md"
    output_path = "/workspace/projects/MarkdownToPDFConverter/output.pdf"
    convert_md_to_pdf(input_path, output_path)
    assert os.path.exists(output_path)
