import markdown
from fpdf import FPDF, HTMLMixin

def convert_md_to_html(md_content):
    """Convert Markdown content to HTML."""
    return markdown.markdown(md_content)

def convert_html_to_pdf(html_content, output_path):
    """Convert HTML content to PDF and save to output_path."""
    class PDF(FPDF, HTMLMixin):
        pass
    
    pdf = PDF()
    pdf.add_page()
    pdf.write_html(html_content)
    pdf.output(output_path)
