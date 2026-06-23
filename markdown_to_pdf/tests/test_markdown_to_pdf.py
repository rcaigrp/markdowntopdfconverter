import pytest
from markdown_to_pdf.main import convert_markdown_to_pdf


def test_convert_markdown_to_pdf():
    convert_markdown_to_pdf('test_input.md', 'test_output.pdf')
    assert True
