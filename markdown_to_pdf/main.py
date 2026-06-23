import json
import os
import sys
from pathlib import Path

from markdown_to_pdf.config import Config


def main():
    try:
        config_file = Path("config.json")
        if not config_file.exists():
            print("Error: config.json not found.")
            sys.exit(1)

        with open(config_file, "r") as f:
            config = json.load(f)

        config_obj = Config(**config)

        input_file = Path(config_obj.input_path)
        if not input_file.exists():
            print(f"Error: {input_file} not found.")
            sys.exit(1)

        output_file = Path(config_obj.output_path)

        # Use markdown2pdf to convert
        result = subprocess.run([
            "markdown2pdf",
            str(input_file),
            "-o",
            str(output_file)
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            sys.exit(1)

        print(f"PDF created successfully at {output_file}")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
