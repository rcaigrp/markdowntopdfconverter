import sys
from markdown_to_pdf.core import load_config, convert_md_to_html, convert_html_to_pdf


def main():
    if len(sys.argv) < 4:
        print("Usage: python -m markdown_to_pdf <config.json> <input.md> <output.pdf>")
        sys.exit(1)
    config_path = sys.argv[1]
    input_md = sys.argv[2]
    output_pdf = sys.argv[3]

    config = load_config(config_path)
    with open(input_md, 'r') as f:
        md_text = f.read()

    html_text = convert_md_to_html(md_text)
    convert_html_to_pdf(html_text, output_pdf)


if __name__ == '__main__':
    main()
