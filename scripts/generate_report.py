import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report():
    # Use the workspace directory
    workspace_base = os.getenv('WORKSPACE', os.getcwd())
    reports_dir = os.path.join(workspace_base, 'reports')
    os.makedirs(reports_dir, exist_ok=True)

    # PDF and image paths
    pdf_path = os.path.join(reports_dir, 'model_report.pdf')
    confusion_matrix_path = os.path.join(reports_dir, 'confusion_matrix.png')
    roc_curve_path = os.path.join(reports_dir, 'roc_curve.png')

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(30, 750, "Credit Card Fraud Detection - Model Report")
    c.drawString(30, 730, "Confusion Matrix:")
    c.drawImage(confusion_matrix_path, 30, 500, width=300, height=200)
    c.drawString(30, 480, "ROC Curve:")
    c.drawImage(roc_curve_path, 30, 250, width=300, height=200)
    c.save()

    print(f"Report generated: {pdf_path}")

generate_pdf_report()
