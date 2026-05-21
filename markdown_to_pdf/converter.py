import markdown
import fpdf

def convert_md_to_html(md_content):
    return markdown.markdown(md_content)

def convert_html_to_pdf(html_content, output_path):
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.html(html_content, link='https://example.com')
    pdf.output(output_path)
