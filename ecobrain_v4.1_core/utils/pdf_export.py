from fpdf import FPDF

def generate_pdf(score_summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Rapport EcoBrain", ln=True, align='C')
    pdf.multi_cell(0, 10, score_summary)
    pdf.output("rapport_eco.pdf")
