import os
import subprocess
import sys
from typing import Optional


def detect_tesseract() -> Optional[str]:
    """Auto-detect Tesseract path on Linux/macOS."""
    system = sys.platform
    if system == "darwin":  # macOS
        try:
            result = subprocess.run([
                "which",
                "tesseract"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
        except Exception:
            pass
    elif system == "linux":  # Linux
        try:
            result = subprocess.run([
                "which",
                "tesseract"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
        except Exception:
            pass
    return None


def prompt_tesseract_installation():
    """Prompt user to install Tesseract on Linux/macOS."""
    print("Tesseract not found. Please install it first.")
    print("Linux (Debian/Ubuntu): sudo apt-get install tesseract-ocr")
    print("macOS (Homebrew): brew install tesseract")
    sys.exit(1)


def validate_config(config_path: str) -> dict:
    """Validate config file using Pydantic."""
    from markdown_to_pdf.config import MarkdownToPDFConfig
    try:
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        config = MarkdownToPDFConfig(**config_data)
        return config.dict()
    except Exception as e:
        print(f"Config validation failed: {str(e)}")
        sys.exit(1)


def convert_markdown_to_pdf(input_path: str, output_path: str, tesseract_path: str):
    """Convert Markdown to PDF using reportlab."""
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    import markdown

    # Read Markdown content
    with open(input_path, 'r') as f:
        md_text = f.read()
    
    # Convert to HTML
    html_text = markdown.markdown(md_text)
    
    # Generate PDF
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Add paragraph
    p = Paragraph(html_text, styles['Normal'])
    story.append(p)
    
    # Build PDF
    doc.build(story)
    
    print(f"PDF generated at: {output_path}")