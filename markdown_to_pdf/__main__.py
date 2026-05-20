import sys
import os
import json

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

config_path = os.path.join(project_dir, "config.json")
with open(config_path, 'r') as f:
    config = json.load(f)

input_path = config['input']
output_path = config['output']

with open(input_path, 'r') as f:
    md_content = f.read()

html_content = markdown.markdown(md_content)

HTML(string=html_content).write_pdf(output_path)
