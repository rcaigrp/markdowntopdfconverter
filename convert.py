import os
import markdown
from fpdf2 import FPDF
from fpdf2.html import HtmlMixin

class PDFConverter(HtmlMixin, FPDF):
    pass

def convert_md_to_pdf(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html_text = markdown.markdown(md_text)
    
    pdf = PDFConverter()
    pdf.add_page()
    pdf.write_html(html_text)
    
    pdf.output(output_path)
