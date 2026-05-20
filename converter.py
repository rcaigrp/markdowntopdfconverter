import markdown
import weasyprint

def convert_md_to_html(md_text):
    """Converts markdown text to HTML."""
    return markdown.markdown(md_text)

def convert_html_to_pdf(html_content, output_path):
    """Converts HTML content to PDF using weasyprint."""
    # Weasyprint's HTML class takes a string via the 'string' argument
    HTML = weasyprint.HTML(string=html_content)
    HTML.write_pdf(output_path)

def convert_markdown_to_pdf(md_text, output_path):
    """End-to-end conversion from markdown to PDF."""
    html = convert_md_to_html(md_text)
    convert_html_to_pdf(html, output_path)