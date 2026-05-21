import markdown
import os
from fpdf import FPDF

def convert_markdown_to_pdf(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', size=12)
    pdf.html(html_content, x=10, y=10)
    pdf.output(output_path)

def read_config(config_path='config.json'):
    import json
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config.get('input_path', 'input.md'), config.get('output_path', 'output.pdf')
