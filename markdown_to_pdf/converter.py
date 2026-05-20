import markdown

def md_to_html(md_text):
    return markdown.markdown(md_text)

def html_to_pdf(html_content, output_path):
    from weasyprint import HTML
    HTML(string=html_content).write_pdf(output_path)

def convert_md_to_pdf(md_content, output_path):
    html = md_to_html(md_content)
    html_to_pdf(html, output_path)
