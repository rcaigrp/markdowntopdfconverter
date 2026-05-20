import markdown
import re
import html as html_mod
from fpdf import FPDF

def read_md(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def md_to_html(text):
    return markdown.markdown(text)

def html_to_pdf(html, output_path):
    # Strip HTML tags
    text = html_mod.unescape(html)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    pdf = FPDF(charset='UTF8')
    pdf.add_page()
    pdf.set_font('Helvetica', size=12)
    
    # Split by lines to handle page breaks manually if needed
    lines = text.split('\n')
    for line in lines:
        if line.strip():
            # Use multi_cell. It stops at the bottom of the page.
            # To avoid crash on long text, we can add pages if y > 270 (approx)
            # But for simplicity, we'll rely on short text or catch exception.
            try:
                pdf.multi_cell(w=0, h=10, text=line)
            except:
                pdf.add_page()
                pdf.multi_cell(w=0, h=10, text=line)
                
    pdf.output(output_path)
