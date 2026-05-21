"""Markdown to PDF converter implementation."""
import markdown
from fpdf import FPDF
import os

def markdown_to_html(markdown_text):
    """Convert markdown text to HTML.
    
    Args:
        markdown_text: String containing markdown content
        
    Returns:
        str: HTML string
    """
    html = markdown.convert(markdown_text)
    return html

def html_to_pdf(html_content, output_path):
    """Convert HTML content to PDF file.
    
    Args:
        html_content: String containing HTML content
        output_path: Path where PDF file will be saved
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', size=12)
    
    # Clean HTML for PDF conversion
    # Remove HTML tags but keep content
    import re
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    
    # Add text to PDF
    pdf.multi_cell(0, 10, clean_text)
    pdf.output(output_path)

def convert_markdown_to_pdf(input_path, output_path):
    """Convert markdown file to PDF.
    
    Args:
        input_path: Path to input markdown file
        output_path: Path where PDF file will be saved
    """
    # Read markdown file
    with open(input_path, 'r') as f:
        markdown_content = f.read()
    
    # Convert to HTML
    html_content = markdown_to_html(markdown_content)
    
    # Convert to PDF and save
    html_to_pdf(html_content, output_path)
