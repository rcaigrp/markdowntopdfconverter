import json
import os

def main():
    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, 'config.json')
    with open(config_path) as f:
        config = json.load(f)
    
    input_path = config['input']
    output_path = config['output']
    
    with open(input_path) as f:
        md_text = f.read()
        
    from markdown_to_pdf.converter import convert_md_to_pdf
    convert_md_to_pdf(md_text, output_path)

if __name__ == '__main__':
    main()
