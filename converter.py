import json
import markdown
import html2text
from fpdf import FPDF

def read_config(path):
    with open(path, 'r') as f:
        return json.load(f)

def md_to_html(md_text):
    return markdown.markdown(md_text)

def html_to_text(html_text):
    return html2text.html2text(html_text)

def text_to_pdf(text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(output_path)
