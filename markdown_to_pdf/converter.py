import markdown
from fpdf import FPDF

class MarkdownToPDFConverter:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def convert(self):
        with open(self.input_path, 'r') as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content)
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica")
        pdf.html(html_content)
        pdf.output(self.output_path)
