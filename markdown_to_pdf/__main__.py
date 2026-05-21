import sys
import os
import json
import markdown
from fpdf import FPDF, HTMLMixin

class PDF(HTMLMixin, FPDF):
    pass

def main():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
    
    with open(config_path) as f:
        config = json.load(f)
        
    input_path = config['input_path']
    output_path = config['output_path']
    
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        sys.exit(1)
        
    with open(input_path) as f:
        md_content = f.read()
        
    html = markdown.markdown(md_content)
    
    pdf = PDF()
    pdf.add_page()
    pdf.write_html(html)
    
    pdf.output(output_path)
    print(f"PDF saved to {output_path}")

if __name__ == "__main__":
    main()
