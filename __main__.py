import sys
import os

# Add project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from converter import load_config, convert_markdown_to_pdf

def main():
    """Main entry point"""
    config = load_config()
    input_path = config['input_path']
    output_path = config['output_path']
    
    success = convert_markdown_to_pdf(input_path, output_path)
    if success:
        print(f"PDF saved to {output_path}")
    else:
        print("Conversion failed")

if __name__ == '__main__':
    main()
