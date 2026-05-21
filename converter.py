import json
import os
import markdown
from fpdf import FPDF

def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        return json.load(f)

def markdown_to_html(md_text: str) -> str:
    return markdown.markdown(md_text)

def html_to_pdf(html_content: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.html(html_content, x=0, y=0)
    return pdf.output(dest="S")

def convert(input_path: str, output_path: str, config_path: str = "config.json"):
    config = load_config(config_path)
    with open(input_path, "r") as f:
        md_text = f.read()
    
    html_content = markdown_to_html(md_text)
    pdf_bytes = html_to_pdf(html_content)
    
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)
