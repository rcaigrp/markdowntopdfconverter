import sys
import os
from converter import MarkdownToPDFConverter

def main():
    if len(sys.argv) < 3:
        print("Usage: python -m markdown_to_pdf <input_path> <output_path>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Try to find config relative to script or project dir
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')
    converter = MarkdownToPDFConverter(config_path)
    converter.convert(input_path, output_path)
    print(f"Saved PDF to {output_path}")

if __name__ == '__main__':
    main()
