import pandas
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx*")
print(filepaths)

for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    pdf = FPDF(orientation="p", unit="mm", format="a4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Data {invoice_date}", ln=2)
    pdf.output(f"pdfs/{filename}.pdf")
