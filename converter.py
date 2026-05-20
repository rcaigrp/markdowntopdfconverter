import markdown
import weasyprint
import os


def convert_markdown_to_html(md_content):
    return markdown.markdown(md_content)


def convert_html_to_pdf(html_content, output_path):
    weasyprint.HTML(string=html_content).write_pdf(output_path)


def process(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, 'r') as f:
        md_content = f.read()

    html_content = convert_markdown_to_html(md_content)

    if os.path.dirname(output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
    convert_html_to_pdf(html_content, output_path)
