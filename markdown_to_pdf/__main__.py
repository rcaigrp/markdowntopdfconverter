import os
from markdown_to_pdf.core import load_config, convert_markdown_to_html, convert_html_to_pdf

def main():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.json")
    config = load_config(config_path)
    
    input_path = config["input"]
    output_path = config["output"]
    
    with open(input_path, 'r') as f:
        md_content = f.read()
        
    html_content = convert_markdown_to_html(md_content)
    pdf_bytes = convert_html_to_pdf(html_content)
    
    with open(output_path, 'wb') as f:
        f.write(pdf_bytes)

if __name__ == "__main__":
    main()
