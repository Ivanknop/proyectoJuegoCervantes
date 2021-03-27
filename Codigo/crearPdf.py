from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def crearPdf(nombre,texto):
    x = 25
    y = 820
    c = canvas.Canvas(str(nombre)+".pdf",pagesize=A4)    
    c.setFont("Times-Roman",20)
    c.drawString(250,y,'RESULTADOS OBTENIDOS')
    y-=10
    c.setFont("Times-Roman",12)
    c.drawString(x,y,'Jugador '+str(nombre))
    y-=10
    for i in range(len(texto)):
        c.drawString(x,y,texto[i])
        y -=20
    c.showPage()
    c.save()