import pytest
import markdown
from unittest.mock import patch, mock_open

def test_convert_md_to_pdf():
    md_content = "# Hello\n\nWorld."
    html_content = markdown.markdown(md_content)
    with patch('converter.markdown.markdown', return_value=html_content):
        with patch('builtins.open', mock_open(read_data=md_content)):
            from converter import convert_md_to_pdf
            result = convert_md_to_pdf('input.md', 'output.pdf')
            assert result == 'output.pdf'
