import subprocess
import sys
from pathlib import Path

from markdown_to_pdf.config import Config


def convert_markdown_to_pdf(input_path: str, output_path: str):
    # Check if markdown2pdf is installed
    try:
        result = subprocess.run(
            ["markdown2pdf", input_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Write output to file
        with open(output_path, "w") as f:
            f.write(result.stdout)
        return
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert Markdown to PDF: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"markdown2pdf not found. Install it using: pip install markdown2pdf", file=sys.stderr)
        sys.exit(1)
