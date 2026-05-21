import markdown
from fpdf import FPDF

def convert_md_to_pdf(input_path: str, output_path: str) -> None:
    with open(input_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html_text = markdown.markdown(md_text)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.html(html_text)
    
    pdf.output(output_path)
