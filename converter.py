import os
import json
import markdown

def load_config(config_path='config.json'):
    """Load configuration from JSON file"""
    with open(config_path, 'r') as f:
        return json.load(f)

def read_markdown(input_path):
    """Read markdown content from file"""
    with open(input_path, 'r') as f:
        return f.read()

def markdown_to_html(md_content):
    """Convert markdown content to HTML"""
    html = markdown.markdown(md_content)
    return f"<html><body>{html}</body></html>"

def html_to_pdf(html_content, output_path):
    """Convert HTML content to PDF using fpdf2"""
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.add_html(html_content)
    pdf.output(output_path)
    return True

def convert_markdown_to_pdf(input_path, output_path):
    """Main conversion function"""
    md_content = read_markdown(input_path)
    html = markdown_to_html(md_content)
    success = html_to_pdf(html, output_path)
    return success
