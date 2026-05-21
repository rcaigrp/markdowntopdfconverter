import markdown
import json
import os
from fpdf import FPDF


def convert_markdown_to_pdf(input_path, output_path):
    """Convert markdown file to PDF."""
    # Read markdown content
    with open(input_path, 'r') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)
    
    # Create PDF from HTML
    pdf = FPDF()
    pdf.add_page()
    pdf.html(html_content)
    
    # Save PDF
    pdf.output(output_path)


def read_config(config_path='config.json'):
    """Read input/output paths from config file."""
    with open(config_path) as f:
        config = json.load(f)
    return config.get('input_path', 'input.md'), config.get('output_path', 'output.pdf')
