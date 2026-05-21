import markdown


def convert_md_to_html(md_text):
    """Convert Markdown text to HTML."""
    return markdown.markdown(md_text)


def convert_html_to_pdf(html, output_path):
    """Convert HTML string to PDF using fpdf2."""
    from fpdf2 import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.html(html, safe_mode='escape')
    pdf.output(output_path)
