import markdown
import re

def markdown_to_html(md_text):
    return markdown.markdown(md_text)

def strip_html(html):
    return re.sub(r'<[^>]*>', '', html)

def html_to_pdf(html, output_path):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    text = strip_html(html)
    text = text.replace('\n', ' ')
    pdf.write(text)
    pdf.output(output_path, 'F')
