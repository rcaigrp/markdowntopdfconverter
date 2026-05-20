import markdown

def convert_md_to_html(md_content: str) -> str:
    return markdown.convert(md_content)

def convert_html_to_pdf(html_content: str) -> bytes:
    from html2pdf import HTML2PDF
    return HTML2PDF().convert(html_content)
