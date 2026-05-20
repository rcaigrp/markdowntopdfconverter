import json
import os
from pathlib import Path
from converter import convert_md_to_html, convert_html_to_pdf

def main():
    project_root = Path(__file__).parent.parent
    config_path = project_root / "config.json"
    
    if not config_path.exists():
        config_path = Path("config.json")
    
    with open(config_path) as f:
        config = json.load(f)
    
    input_path = config["input_path"]
    output_path = config["output_path"]
    
    with open(input_path) as f:
        md_content = f.read()
    
    html_content = convert_md_to_html(md_content)
    pdf_bytes = convert_html_to_pdf(html_content)
    
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)

if __name__ == "__main__":
    main()
