import os
import pytest
import markdown_to_pdf

def test_criterion_1_convert_markdown_to_pdf():
    # Create a temporary markdown file
    with open('/tmp/test.md', 'w') as f:
        f.write('# Hello World\n\nThis is a test.')
    
    output_path = '/tmp/test.pdf'
    
    # Convert
    converter = markdown_to_pdf.MarkdownToPDFConverter('/tmp/test.md', output_path)
    converter.convert()
    
    # Check output exists
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0
    
    # Cleanup
    os.remove('/tmp/test.md')
    os.remove(output_path)

