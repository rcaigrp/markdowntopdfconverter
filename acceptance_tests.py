import os
import pytest

from converter import convert_md_to_pdf


def test_criterion_1_create_pdf():
    md_text = "# Hello\nWorld"
    output_path = '/tmp/test_output.pdf'
    convert_md_to_pdf(md_text, output_path)
    assert os.path.exists(output_path)


def test_criterion_2_pdf_content():
    md_text = "# Hello\nWorld"
    output_path = '/tmp/test_content.pdf'
    convert_md_to_pdf(md_text, output_path)
    # Check file size > 0
    assert os.path.getsize(output_path) > 100
