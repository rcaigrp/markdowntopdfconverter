import sys
import os
from config import load_config
from converter import md_to_html, html_to_pdf

def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)
        
    input_path, output_path = load_config(config_path)
    
    with open(input_path, 'r') as f:
        md_content = f.read()
        
    html_content = md_to_html(md_content)
    html_to_pdf(html_content, output_path)
    
    print(f"PDF generated at {output_path}")

if __name__ == '__main__':
    main()
