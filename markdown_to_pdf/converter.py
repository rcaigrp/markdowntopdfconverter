import markdown
from fpdf import FPDF


class PDF(FPDF, HTMLMixin):
    pass


def convert_md_to_html(md_text):
    """Convert Markdown text to HTML."""
    return markdown.markdown(md_text)


def html_to_pdf(html, output_path):
    """Convert HTML to PDF and save to output_path."""
    pdf = PDF()
    pdf.add_page()
    pdf.html(html)
    pdf.output(output_path)


def convert_md_to_pdf(md_content, output_path):
    """Convert Markdown content to PDF."""
    html = convert_md_to_html(md_content)
    html_to_pdf(html, output_path)
