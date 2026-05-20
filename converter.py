import markdown
import fpdf
import os
import re
import json

class MarkdownToPDFConverter:
    def __init__(self, config_path=None):
        self.config = {}
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = json.load(f)

    def convert(self, input_path, output_path=None):
        if output_path is None:
            output_path = self.config.get('output_path', 'output.pdf')
            
        with open(input_path, 'r') as f:
            md_text = f.read()
            
        html = markdown.markdown(md_text)
        
        # Extract text from HTML for PDF content
        text = re.sub('<[^]*>', '', html)
        
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(output_path, 'F')
        
        return output_path
