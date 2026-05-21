import markdown
import json
from fpdf2 import FPDF

class ConfigLoader:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    def get_input_path(self):
        return self.config.get('input_path')

    def get_output_path(self):
        return self.config.get('output_path')

class Converter:
    def __init__(self, config_path):
        self.config = ConfigLoader(config_path)

    def md_to_html(self, markdown_text):
        return markdown.markdown(markdown_text)

    def html_to_pdf(self, html):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.html(html)
        return pdf

    def save_pdf(self, pdf, path):
        pdf.output(path)