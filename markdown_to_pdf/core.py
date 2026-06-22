import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

def load_config(config_path='config.json'):
    """Load configuration from config.json."""
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config['input_path'], config['output_path']

def parse_markdown(md_text):
    """Convert basic Markdown to a list of (text, style) tuples."""
    elements = []
    lines = md_text.split('\n')
    for line in lines:
        if line.startswith('# '):
            elements.append((line[2:], 'Heading1'))
        elif line.startswith('## '):
            elements.append((line[3:], 'Heading2'))
        elif line.startswith('**') and line.endswith('**'):
            elements.append((line[2:-2], 'Bold'))
        elif line.startswith('- '):
            elements.append((line[2:], 'Bullet'))
        else:
            elements.append((line, 'Normal'))
    return elements

def generate_pdf(input_text, output_path):
    """Generate a PDF from parsed markdown elements."""
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y_start = height - 50
    
    elements = parse_markdown(input_text)
    for text, style in elements:
        if style == 'Heading1':
            c.setFont('Helvetica-Bold', 16)
        elif style == 'Heading2':
            c.setFont('Helvetica-Bold', 14)
        elif style == 'Bold':
            c.setFont('Helvetica-Bold', 12)
        elif style == 'Bullet':
            c.setFont('Helvetica', 12)
        else:
            c.setFont('Helvetica', 12)
        c.drawString(50, y_start, text)
        y_start -= 20
        if y_start < 50:
            c.showPage()
            y_start = height - 50
    
    c.save()

def main():
    """Main entry point."""
    input_path, output_path = load_config()
    with open(input_path, 'r') as f:
        md_text = f.read()
    generate_pdf(md_text, output_path)
