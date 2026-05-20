import markdown
import json
import os
import weasyprint

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config['input_path'], config['output_path']

def convert_markdown_to_html(md_content):
    return markdown.markdown(md_content)

def convert_html_to_pdf(html_content, output_path):
    weasyprint.HTML(string=html_content).write_pdf(output_path)

def run(input_path, output_path):
    with open(input_path, 'r') as f:
        md_content = f.read()
    html_content = convert_markdown_to_html(md_content)
    convert_html_to_pdf(html_content, output_path)
