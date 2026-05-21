import os
import pytest
from markdown_to_pdf import convert_md_to_pdf


def test_convert_md_to_pdf():
    md = "# Hello\nWorld"
    output_path = "/tmp/test_output.pdf"
    if os.path.exists(output_path):
        os.remove(output_path)
    convert_md_to_pdf(md, output_path)
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0
    os.remove(output_path)
