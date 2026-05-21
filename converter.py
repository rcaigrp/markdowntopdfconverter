import markdown
from reportlab.lib.colors import black
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas

def convert_md_to_pdf(input_md, output_pdf):
    """Converts a Markdown file to a PDF using reportlab."""
    # Read markdown
    with open(input_md, 'r') as f:
        md_content = f.read()

    # Parse markdown to HTML
    html = markdown.markdown(md_content)
    
    # Simple parser to extract text and headings
    # We will split by headings to handle them simply
    lines = md_content.split('\n')
    
    c = canvas.Canvas(output_pdf, pagesize=(595.28, 841.89))  # A4 size
    
    # Start at y position
    y = 780  # 841.89 - 60 (top margin)
    
    # Use a simple style
    c.setFont('Helvetica', 12)
    
    in_list = False
    for line in lines:
        if line.startswith('# '):
            # Heading
            y -= 10
            c.setFont('Helvetica-Bold', 14)
            c.setFillColor(black)
            c.drawString(40, y, line[2:])
            c.setFont('Helvetica', 12)
            y -= 20
        elif line.startswith('- '):
            # List item
            if not in_list:
                in_list = True
                y -= 5
            c.setFillColor(black)
            c.drawString(55, y, line[2:])
            y -= 15
        else:
            # Paragraph
            if in_list:
                in_list = False
            if line.strip():
                c.setFillColor(black)
                c.drawString(40, y, line)
                y -= 15

    c.save()

if __name__ == '__main__':
    convert_md_to_pdf('input.md', 'output.pdf')
