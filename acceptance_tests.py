import os
import pytest
import sys

sys.path.insert(0, '/workspace/projects/MarkdownToPDFConverter')

from converter import convert_md_to_pdf
import io

def test_criterion_1_pdf_created():
    """Test that a PDF file is created."""
    input_md = '/workspace/projects/MarkdownToPDFConverter/input.md'
    output_pdf = '/workspace/projects/MarkdownToPDFConverter/output.pdf'
    if os.path.exists(output_pdf):
        os.remove(output_pdf)
    
    convert_md_to_pdf(input_md, output_pdf)
    assert os.path.exists(output_pdf)

def test_criterion_2_pdf_content():
    """Test that PDF content is not empty."""
    input_md = '/workspace/projects/MarkdownToPDFConverter/input.md'
    output_pdf = '/workspace/projects/MarkdownToPDFConverter/output.pdf'
    
    convert_md_to_pdf(input_md, output_pdf)
    assert os.path.getsize(output_pdf) > 100  # Minimal PDF size

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
