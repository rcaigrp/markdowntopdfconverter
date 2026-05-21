import sys
import os

def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    config = {}
    try:
        with open(config_path, "r") as f:
            config = __import__("json").load(f)
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
        sys.exit(1)
    
    input_path = config.get("input")
    output_path = config.get("output")
    
    if not input_path or not output_path:
        print("Missing input or output path in config.json")
        sys.exit(1)
        
    from markdown_to_pdf import converter
    converter.convert(input_path, output_path, config_path)

if __name__ == "__main__":
    main()
