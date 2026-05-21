import json
import markdown
import html2text
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def read_config(path='config.json'):
    with open(path, 'r') as f:
        return json.load(f)

def md_to_html(md_content):
    return markdown.markdown(md_content)

def html_to_text(html_content):
    h = html2text.HTML()
    h.body_width = 0
    return h.process_text(html_content).strip()

def create_pdf(text, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

def convert(input_path, output_path, config_path='config.json'):
    config = read_config(config_path)
    md_content = config.get('input', input_path)
    
    with open(md_content, 'r') as f:
        md_text = f.read()
        
    html = md_to_html(md_text)
    text = html_to_text(html)
    
    create_pdf(text, output_path)
