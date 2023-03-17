
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
    pdf.cell(w=50, h=8, txt=f"{name}")

pdf.output("pdfs/output.pdf")





