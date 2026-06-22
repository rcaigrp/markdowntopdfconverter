import markdown
from html2pdf import html2pdf
import json
import os

def read_config(path='config.json'):
    with open(path, 'r') as f:
        return json.load(f)

def md_to_html(md_text):
    return markdown.markdown(md_text)

def html_to_pdf(html_text, output_path):
    html2pdf(html=html_text, output=output_path)

def convert(input_path, output_path, config_path='config.json'):
    config = read_config(config_path)
    input_file = config.get('input', input_path)
    output_file = config.get('output', output_path)
    
    with open(input_file, 'r') as f:
        md_text = f.read()
        
    html_text = md_to_html(md_text)
    html_to_pdf(html_text, output_file)
    
    return output_file
