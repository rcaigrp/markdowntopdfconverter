import json
import markdown
from fpdf import FPDF, HTMLMixin

class PDF(HTMLMixin, FPDF):
    pass

def load_config(path='config.json'):
    with open(path) as f:
        return json.load(f)

def md_to_html(md_text):
    return markdown.markdown(md_text)

def html_to_pdf(html, output_path):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.add_html(html, link_color='red')
    pdf.output(output_path)
