from reportlab.pdfgen import canvas
pdf_file = canvas.Canvas("example.pdf")

a=5
b=6
c=a+b
d=a*b

c2=str(c)
d2=str(d)

pdf_file.drawString(72,720,(c2))
pdf_file.drawString(72,700,(d2))

pdf_file.save()
