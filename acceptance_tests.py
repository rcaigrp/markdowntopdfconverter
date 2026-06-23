import pytest

def test_criterion_1_parse_markdown_file():
    """Test that markdown file is parsed correctly."""
    from markdown_to_pdf import parse_markdown
    assert parse_markdown('test.md') == 'PDF generated'


def test_criterion_2_generate_pdf_report():
    """Test that PDF is generated from parsed markdown."""
    from markdown_to_pdf import generate_pdf
    assert generate_pdf('test.md', 'output.pdf') == True