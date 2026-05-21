import markdown

def convert_md_to_html(md_text: str) -> str:
    return markdown.markdown(md_text)

def convert_html_to_pdf(html: str, output_path: str):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    # Wrap HTML to ensure proper document structure for fpdf2
    full_html = f"<html><body>{html}</body></html>"
    pdf.add_html(full_html)
    pdf.output(dest='F', file=output_path)

def process(input_path: str, output_path: str):
    with open(input_path, 'r') as f:
        md_text = f.read()
    html = convert_md_to_html(md_text)
    convert_html_to_pdf(html, output_path)
