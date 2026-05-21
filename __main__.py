import sys
import os

# Ensure imports work regardless of execution context
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from converter import read_config, md_to_html, html_to_text, text_to_pdf

def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    config = read_config(config_path)
    input_path = config["input"]
    output_path = config["output"]
    
    with open(input_path) as f:
        md_content = f.read()
        
    html = md_to_html(md_content)
    text = html_to_text(html)
    text_to_pdf(text, output_path)
    print(f"PDF generated at {output_path}")

if __name__ == "__main__":
    main()
