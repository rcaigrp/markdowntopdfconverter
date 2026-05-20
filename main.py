import json
import markdown
from fpdf import FPDF

def convert_md_to_pdf(input_path, output_path):
    with open(input_path, 'r') as f:
        md_text = f.read()
    html_text = markdown.markdown(md_text)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.from_html(html_text, target_page="current")
    pdf.output(output_path)

if __name__ == "__main__":
    config_path = "/workspace/projects/MarkdownToPDFConverter/config.json"
    with open(config_path, 'r') as f:
        config = json.load(f)
    convert_md_to_pdf(config['input'], config['output'])
