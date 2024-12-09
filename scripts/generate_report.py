from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report():
    c = canvas.Canvas("./reports/model_report.pdf", pagesize=letter)
    c.drawString(30, 750, "Credit Card Fraud Detection - Model Report")
    c.drawString(30, 730, "Confusion Matrix:")
    c.drawImage('./reports/confusion_matrix.png', 30, 500, width=300, height=200)
    c.drawString(30, 480, "ROC Curve:")
    c.drawImage('./reports/roc_curve.png', 30, 250, width=300, height=200)
    c.save()

generate_pdf_report()
