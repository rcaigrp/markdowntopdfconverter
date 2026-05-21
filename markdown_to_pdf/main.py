import markdown
import json
from fpdf2 import FPDF

def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def md_to_html(md_text):
    return markdown.markdown(md_text)

def html_to_pdf(html_text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.html(html_text, x=0, y=0)
    pdf.output(output_path)