import markdown
import re
from fpdf import FPDF


def read_md(path):
    """Read markdown file."""
    with open(path, 'r') as f:
        return f.read()


def md_to_html(text):
    """Convert markdown text to HTML."""
    return markdown.markdown(text)


def strip_html(html):
    """Extract plain text from HTML by stripping tags."""
    text = re.sub(r'<br\s*/>', '\n', html, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\n\s*\n', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def html_to_pdf(html, output_path):
    """Convert HTML (plain text extracted) to PDF."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', size=12)
    text = strip_html(html)
    lines = text.split('\n')
    for line in lines:
        pdf.multi_cell(w=180, h=10, text=line, align='L')
    pdf.output(output_path)
