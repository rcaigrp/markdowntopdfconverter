import os
from markdown_to_pdf.config import read_config
from markdown_to_pdf.converter import md_to_html, html_to_pdf

def run(input_path, output_path, config_path):
    config = read_config(config_path)
    with open(input_path, 'r') as f:
        md_text = f.read()
    html_text = md_to_html(md_text)
    html_to_pdf(html_text, output_path)
