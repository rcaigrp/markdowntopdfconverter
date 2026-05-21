import markdown
import html2text
from fpdf import FPDF
import os


def convert(input_path, output_path):
    """Converts a Markdown file to a PDF file."""
    with open(input_path, 'r') as f:
        md_content = f.read()

    # Step 1: Convert Markdown to HTML
    html = markdown.markdown(md_content)

    # Step 2: Convert HTML to plain text
    converter = html2text.HTML2Text()
    converter.body_width = 0  # Disable line wrapping
    text = converter.handle(html)

    # Step 3: Convert text to PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    pdf.multi_cell(w=0, h=5, text=text)

    # Step 4: Save PDF
    dir_path = os.path.dirname(output_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    pdf.output(output_path, mode="F")
