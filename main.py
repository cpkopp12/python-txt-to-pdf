
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("txts/*.txt")
# print(filepaths)

pdf = FPDF(orientation="P", unit="mm", format="A4")

for path in filepaths:
    pdf.add_page()

    filename = Path(path).stem
    name = filename.title()
    # print(name)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{name}", ln=1)

    # get content of txt file
    with open(path, "r") as file:
        content = file.read()
    # add txt to pdfs
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("pdfs/output.pdf")





