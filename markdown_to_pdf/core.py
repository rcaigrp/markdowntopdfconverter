import json
import markdown
from fpdf import FPDF, HTMLMixin

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return json.load(f)

def convert_markdown_to_html(md_content: str) -> str:
    return markdown.markdown(md_content)

class PDF(FPDF, HTMLMixin):
    pass

def convert_html_to_pdf(html_content: str) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.html(html_content)
    return pdf.output(dest="S")
