from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topicsPdf.csv")

# pdf.add_page()
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=15, h=12, txt="Order", align="C", ln=0, border=1)
# pdf.cell(w=60, h=12, txt="Topic", align="C", ln=0, border=1)
# pdf.cell(w=15, h=12, txt="Pages", align="C", ln=1, border=1)
#
# for index, row in df.iterrows():
#     pdf.set_font(family="Times", style="B", size=12)
#     order = str(row['Order'])
#     page = str(row['Pages'])
#     pdf.cell(w=15, h=12, txt=order, align="C", ln=0, border=1)
#     pdf.cell(w=60, h=12, txt=row['Topic'], align="C", ln=0, border=1)
#     pdf.cell(w=15, h=12, txt=page, align="C", ln=1, border=1)

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    for y in range(20, 298, 10):
        pdf.set_text_color(180, 180, 180)
        pdf.line(10, y, 200, y)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for y in range(20, 298, 10):
            pdf.set_text_color(180, 180, 180)
            pdf.line(10, y, 200, y)
        # set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")


pdf.output("output.pdf")
