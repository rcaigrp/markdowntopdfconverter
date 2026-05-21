import markdown
from fpdf import FPDF
from fpdf import HTMLMixin

class PDF(HTMLMixin, FPDF):
    pass

def convert(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    html_text = markdown.markdown(md_text)
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    pdf.add_html(html_text)
    pdf.output(output_path)
