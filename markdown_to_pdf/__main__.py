import json
import markdown
import converter


def main():
    # Load configuration
    with open('config.json') as f:
        config = json.load(f)

    input_path = config['input_path']
    output_path = config['output_path']

    # Read markdown content
    with open(input_path) as f:
        content = f.read()

    # Convert markdown to HTML
    html = markdown.markdown(content)

    # Generate PDF
    pdf = converter.FPDF()
    pdf.output(filename=output_path, dest='F')


if __name__ == '__main__':
    main()
