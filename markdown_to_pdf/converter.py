import markdown
from weasyprint import HTML

def convert_md_to_html(md_content):
    return markdown.markdown(md_content)

def convert_html_to_pdf(html_content, output_path):
    HTML(string=html_content).write_pdf(output_path)
