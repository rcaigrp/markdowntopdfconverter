import os
import pytest
import markdown_to_pdf.converter as converter

def test_criterion_1_convert_markdown_to_pdf():
    input_md = '/workspace/projects/MarkdownToPDFConverter/input.md'
    output_pdf = '/workspace/projects/MarkdownToPDFConverter/output.pdf'
    
    with open(input_md, 'w') as f:
        f.write('# Test\n\nHello **World**\n\nParagraph.')
    
    converter.convert_markdown_to_pdf(input_md, output_pdf)
    
    assert os.path.exists(output_pdf)
    with open(output_pdf, 'rb') as f:
        header = f.read(4)
        assert header == b'%PDF', 'Output is not a valid PDF'
    
    os.remove(input_md)
    os.remove(output_pdf)

def test_criterion_2_read_config():
    config_path = '/workspace/projects/MarkdownToPDFConverter/config.json'
    with open(config_path, 'w') as f:
        f.write('{"input_path": "test.md", "output_path": "test.pdf"}')
    
    input_path, output_path = converter.read_config(config_path)
    assert input_path == 'test.md'
    assert output_path == 'test.pdf'
    os.remove(config_path)
