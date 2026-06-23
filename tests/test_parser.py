import pytest
from markdown_to_pdf.parser import parse_markdown

def test_parse_markdown():
    assert parse_markdown('test.md') == 'PDF generated'

def test_parse_empty_file():
    assert parse_markdown('') == 'No content'

def test_parse_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        parse_markdown('nonexistent.md')