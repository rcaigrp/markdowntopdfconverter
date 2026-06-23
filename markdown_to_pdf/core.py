import os
import subprocess
import sys
import shutil
import json
from typing import Optional
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from markdown import markdown
import tempfile

# Import config validation
from .config import Config


def detect_tesseract() -> str:
    """Detect Tesseract installation on Linux/macOS. Returns path or raises error."""
    if sys.platform in ["linux", "darwin"]:
        try:
            result = subprocess.run([
                "which",
                "tesseract"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                raise RuntimeError("Tesseract not found. Please install it.")
        except Exception as e:
            raise RuntimeError(f"Failed to detect Tesseract: {e}")
    else:
        raise RuntimeError("Tesseract is only supported on Linux and macOS.")


def validate_config(config_path: str) -> Config:
    """Validate and load config from JSON."""
    try:
        config = Config.load(config_path)
        return config
    except Exception as e:
        raise RuntimeError(f"Config validation failed: {str(e)}")


def convert_markdown_to_pdf(input_file: str, config: Config):
    """Convert Markdown to PDF using ReportLab."""
    # Read Markdown content
    with open(input_file, 'r') as f:
        markdown_text = f.read()

    # Convert to HTML
    html_text = markdown(markdown_text)

    # Create PDF
    doc = SimpleDocTemplate(config.output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Add paragraph with HTML content
    p = Paragraph(html_text, styles['Normal'])
    story.append(p)
    story.append(Spacer(1, 12))

    # Build PDF
    doc.build(story)

    print(f"✅ PDF saved to {config.output_path}")


def main(input_file: str, config_path: str = "config.json"):
    """Main entry point."""
    try:
        # Validate config
        config = validate_config(config_path)

        # Detect Tesseract (optional)
        if config.tesseract_path == "":  # auto-detect
            tesseract_path = detect_tesseract()
            config.tesseract_path = tesseract_path
            print(f"Tesseract detected at: {tesseract_path}")

        # Convert Markdown to PDF
        convert_markdown_to_pdf(input_file, config)

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert Markdown to PDF.")
    parser.add_argument("--input", required=True, help="Input Markdown file")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    main(args.input, args.config)