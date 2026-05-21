import markdown
import re
from fpdf import FPDF

def md_to_html(md_text: str) -> str:
    return markdown.markdown(md_text)

def html_to_pdf(html: str, output_path: str):
    pdf = FPDF()
    pdf.add_page()
    text = re.sub('<[^<]+>', '', html)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(output_path, 'F')

def convert_md_to_pdf(input_path: str, output_path: str):
    with open(input_path, 'r') as f:
        md_text = f.read()
    html = md_to_html(md_text)
    html_to_pdf(html, output_path)
