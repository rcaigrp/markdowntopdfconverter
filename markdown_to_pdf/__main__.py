import sys
import os
import json

# Ensure the module's parent directory is on the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_dir, 'config.json')
    
    if not os.path.exists(config_path):
        print(f'Config file not found: {config_path}')
        sys.exit(1)
        
    with open(config_path, 'r') as f:
        config = json.load(f)
        
    input_path = config.get('input_path')
    output_path = config.get('output_path')
    
    if not input_path or not output_path:
        print('Missing input_path or output_path in config')
        sys.exit(1)
        
    # Ensure paths are absolute
    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)
    
    from markdown_to_pdf import convert
    convert.process(input_path, output_path)

if __name__ == '__main__':
    main()
