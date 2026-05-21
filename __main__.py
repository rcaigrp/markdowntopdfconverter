import json
from converter import convert_markdown_to_pdf

def main():
    with open('config.json') as f:
        config = json.load(f)
    
    input_path = config['input_path']
    output_path = config['output_path']
    
    with open(input_path) as f:
        md_content = f.read()
    
    convert_markdown_to_pdf(md_content, output_path)

if __name__ == '__main__':
    main()
