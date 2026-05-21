from markdown_to_pdf.core import Converter
import sys

def main():
    config_path = "config.json"
    converter = Converter(config_path)
    print("Converter initialized.")

if __name__ == "__main__":
    main()