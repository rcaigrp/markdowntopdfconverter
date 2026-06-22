import markdown
import json
import os
from fpdf import FPDF


def convert_markdown_to_html(markdown_text):
    """Convert Markdown text to HTML."""
    return markdown.markdown(markdown_text)


def convert_html_to_pdf(html_text, output_path):
    """Convert HTML text to PDF and save to output_path."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.html(html_text)
    pdf.output(output_path)


def load_config(config_path):
    """Load configuration from JSON file."""
    with open(config_path, 'r') as f:
        return json.load(f)


def process(input_path, output_path):
    """Main processing function: read markdown, convert to PDF."""
    with open(input_path, 'r') as f:
        markdown_text = f.read()
    html_text = convert_markdown_to_html(markdown_text)
    convert_html_to_pdf(html_text, output_path)
