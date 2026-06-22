import markdown
from fpdf import FPDF

class PDFConverter:
    def __init__(self, md_text: str):
        self.md_text = md_text
        self.html = markdown.markdown(md_text)
        self.pdf = FPDF()

    def convert(self) -> bytes:
        self.pdf.add_page()
        self.pdf.add_html(self.html)
        return self.pdf.output(dest="F")

    def save(self, output_path: str):
        pdf_bytes = self.convert()
        with open(output_path, "wb") as f:
            f.write(pdf_bytes)
