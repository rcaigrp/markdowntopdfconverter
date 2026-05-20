import sys
import os
import json

def main():
    # Look for config.json in the project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, 'config.json')
    
    if not os.path.exists(config_path):
        print(f"Config file not found at {config_path}")
        sys.exit(1)
        
    with open(config_path, 'r') as f:
        config = json.load(f)
        
    input_path = config.get('input_path')
    output_path = config.get('output_path')
    
    if not input_path:
        print("No input_path in config")
        sys.exit(1)
        
    with open(input_path, 'r') as f:
        md_content = f.read()
        
    from markdown_to_pdf.converter import convert_md_to_pdf
    convert_md_to_pdf(md_content, output_path)
    print(f"PDF generated at {output_path}")

if __name__ == '__main__':
    main()
