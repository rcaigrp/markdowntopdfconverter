import markdown
import html2text
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def convert_md_to_pdf(md_text, output_path):
    html_text = markdown.markdown(md_text)
    ht = html2text.HTMLParser()
    text = ht.handle(html_text)

    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont("Helvetica", 12)

    y = A4[1] - 50
    x = 50
    max_width = A4[0] - 100

    paragraphs = text.split('\n\n')
    for para in paragraphs:
        lines = para.split('\n')
        for line in lines:
            words = line.split()
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 > max_width // 10:
                    c.drawString(x, y, current_line)
                    y -= 14
                    current_line = word
                else:
                    current_line = current_line + " " + word if current_line else word
            if current_line:
                c.drawString(x, y, current_line)
                y -= 14

        if y < 50:
            c.showPage()
            c.drawString(x, A4[1] - 50, current_line)
            y = A4[1] - 50 - 14

    c.save()
