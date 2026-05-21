import markdown
from fpdf import FPDF
from fpdf import HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass

def convert_md_to_pdf(input_path, output_path):
    with open(input_path, 'r') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content)
    pdf = PDF()
    pdf.add_page()
    pdf.html(html_content, x=0, y=0)
    pdf.output(output_path, local=False)
    return output_path
