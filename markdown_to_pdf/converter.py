from fpdf import FPDF
import os

def convert_md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            pdf.ln(5)
            continue
            
        if line.startswith('# '):
            pdf.set_font("Helvetica", "B", 16)
            pdf.cell(0, 10, line[2:])
            pdf.ln(10)
        elif line.startswith('## '):
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(0, 10, line[3:])
            pdf.ln(10)
        elif line.startswith('- '):
            pdf.set_font("Helvetica", size=12)
            pdf.cell(0, 10, f"- {line[2:]}")
            pdf.ln(5)
        elif line.startswith('* ') or line.startswith('_ '):
            pdf.set_font("Helvetica", "I", 12)
            pdf.cell(0, 10, line[2:])
            pdf.ln(5)
        elif line.startswith('**') and line.endswith('**'):
            pdf.set_font("Helvetica", "B", 12)
            pdf.cell(0, 10, line[2:-2])
            pdf.ln(5)
        else:
            pdf.set_font("Helvetica", size=12)
            pdf.cell(0, 10, line)
            pdf.ln(5)
            
    pdf.output(pdf_path)