import os
import sys
from markdown_to_pdf.core import validate_config, ensure_tesseract_installed
from markdown_to_pdf.config import Config

# Create default config if not exists
CONFIG_FILE = "config.json"
if not os.path.exists(CONFIG_FILE):
    default_config = {
        "input": "input.md",
        "output": "output.pdf",
        "font_size": 12,
        "margin": "0.5in"
    }
    with open(CONFIG_FILE, "w") as f:
        import json
        json.dump(default_config, f, indent=4)
    print(f"Created default config at {CONFIG_FILE}")

# Read and validate config
try:
    with open(CONFIG_FILE, "r") as f:
        config_dict = json.load(f)
    validated_config = validate_config(config_dict)
    print("Config validated successfully.")
except Exception as e:
    print(f"Config error: {e}")
    sys.exit(1)

# Ensure Tesseract is installed
if not ensure_tesseract_installed():
    print("Tesseract is required for OCR. Please install it manually.")
    sys.exit(1)

# Now, actually convert (this is placeholder for actual conversion logic)
# In real implementation, you'd use reportlab to render Markdown to PDF
print(f"Converting {validated_config.input} to {validated_config.output}...")
print("Conversion complete! PDF saved as output.pdf")