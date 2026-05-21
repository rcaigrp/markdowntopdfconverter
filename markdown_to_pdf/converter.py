import markdown
from fpdf import FPDF

def convert_md_to_html(md_text):
    return markdown.markdown(md_text)

def convert_html_to_pdf(html_text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', size=12)
    pdf.html(html_text, x=10, y=10)
    pdf.output(output_path, dest='F')