from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def crearPdf(nombre,respuestasJugador,validas,puntaje,tiempo):
    x, y = A4
    c = canvas.Canvas(str(nombre)+".pdf",pagesize=A4)    
    c.setFont("Times-Roman",20)
    y-=50
    c.drawString(250,y-20,'RESULTADOS OBTENIDOS')
    y-=30
    c.setFont("Times-Roman",10)
    c.drawString(50,y,'Jugador '+str(nombre))
    y-=30
    for i in range(len(respuestasJugador)):
        c.drawString(50,y,'Pregunta '+str(i+1)+': '+str(validas[i]))
        y -=20
        c.drawString(50,y,respuestasJugador[i])
        y -=20
    c.drawString(250,y,'PUNTAJE FINAL: '+str(puntaje))
    y-=25
    c.setFont("Times-Roman",8)
    c.drawString(400,y,'Horario de Finalización => '+str(tiempo))
    c.showPage()
    c.save()
