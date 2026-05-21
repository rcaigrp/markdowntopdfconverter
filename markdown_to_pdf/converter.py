import markdown
from fpdf import FPDF

def md_to_html(md_text):
    """Convert markdown text to HTML."""
    return markdown.markdown(md_text)

def html_to_pdf(html, output_path):
    """Convert HTML string to a PDF file."""
    pdf = FPDF()
    pdf.add_page()
    pdf.html(html, home_dir='.')