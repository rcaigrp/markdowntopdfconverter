import markdown
from fpdf import html2pdf

def md_to_html(md_text):
    return markdown.markdown(md_text)

def html_to_pdf(html_text, output_path):
    html2pdf(html_text, output_path)
