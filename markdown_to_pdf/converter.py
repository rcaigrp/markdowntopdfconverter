import markdown
from fpdf import FPDF
import re

def convert_md_to_pdf(input_path, output_path):
    with open(input_path, 'r') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content)
    
    text_content = re.sub('<[^<]+>', '', html_content)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text_content)
    
    pdf.output(output_path, dest='F')
