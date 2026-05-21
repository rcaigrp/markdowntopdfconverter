import sys
import os
import pytest

sys.path.insert(0, '/workspace')

from markdown_to_pdf.converter import convert_md_to_pdf

@pytest.fixture
def sample_md(tmp_path):
    md_path = tmp_path / "test.md"
    md_path.write_text("# Title\n\nHello World\n\n- Item 1\n\n**Bold**")
    return md_path

@pytest.fixture
def pdf_path(tmp_path):
    return tmp_path / "test.pdf"

def test_conversion_creates_pdf(sample_md, pdf_path):
    convert_md_to_pdf(str(sample_md), str(pdf_path))
    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 100

def test_pdf_contains_text(sample_md, pdf_path):
    convert_md_to_pdf(str(sample_md), str(pdf_path))
    with open(pdf_path, 'rb') as f:
        content = f.read()
    assert b"Hello World" in content
    assert b"Title" in content