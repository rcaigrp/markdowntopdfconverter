import json
import markdown
from fpdf2 import FPDF


def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return json.load(f)


def convert_md_to_html(md_text: str) -> str:
    return markdown.markdown(md_text)


def convert_html_to_pdf(html_text: str, output_path: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.html(html_text, x=10, y=10)
    pdf.output(fname=output_path)
