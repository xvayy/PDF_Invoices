import pandas
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx*")
print(filepaths)

for filepath in filepaths:
    pdf = FPDF(orientation="p", unit="mm", format="a4")

    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Data {invoice_date}", ln=2)

    # Create data frame
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    names = list(df.columns)
    modify_names = []

    # Remove underline
    for name in names:
        print(name)
        print(type(name))
        new_name = name.replace("_", " ").title()
        print(new_name)
        modify_names.append(new_name)



    print(names)
    # Add a header
    pdf.set_font(family="Times", size=9, style="B")
    pdf.cell(w=30, h=8, txt=modify_names[0], border=1)
    pdf.cell(w=70, h=8, txt=modify_names[1], border=1)
    pdf.cell(w=30, h=8, txt=modify_names[2], border=1)
    pdf.cell(w=30, h=8, txt=modify_names[3], border=1)
    pdf.cell(w=30, h=8, txt=modify_names[4], border=1, ln=1)

    print(df)

    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=8, )
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Add last row to the table with total price
    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=8, )
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)


    # Add sentance with total price and logo
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is: {total_sum}", ln=1)

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=45, h=8, txt="PythonHow Company")
    pdf.image("pythonhow.png", w=8)

    pdf.output(f"pdfs/{filename}.pdf")
