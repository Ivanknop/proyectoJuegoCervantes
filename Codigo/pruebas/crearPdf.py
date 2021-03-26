from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
c = canvas.Canvas("hola-mundo.pdf",pagesize=A4)
c.drawString(25,20,'nuevo texto')
c.drawString(50,100,'otro texto')
c.save()