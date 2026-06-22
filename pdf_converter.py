import markdown
from fpdf import FPDF


def md_to_html(md_text):
    """Convert Markdown text to HTML."""
    return markdown.markdown(md_text)


def html_to_pdf(html, output_path):
    """Convert HTML string to PDF file."""
    pdf = FPDF()
    pdf.add_page()
    pdf.add_html(html)
    pdf.output(output_path)
    return output_path
