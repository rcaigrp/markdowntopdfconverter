from markdown_to_pdf.core import validate_config, ensure_tesseract, convert_markdown_to_pdf

if __name__ == '__main__':
    import json
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python -m markdown_to_pdf <config.json>')
        sys.exit(1)
    
    config_path = sys.argv[1]
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f'Config file {config_path} not found')
        sys.exit(1)
    
    validate_config(config)
    ensure_tesseract()
    convert_markdown_to_pdf(config)
    print('PDF generated successfully!')
