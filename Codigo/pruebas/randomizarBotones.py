import PySimpleGUI as sg
import random

class NuevoBoton():
    def __init__ (self,texto,clave):  
        self.name = texto
        self.key = clave
        self.font = ('Arial',15)   
        self.button = sg.Button(self.name,size=(10,2),font = self.font,key=self.key
        )
    def get_L (self):
        return self.name

    def get_key(self): #lo uso para acceder al boton pero creo es innecesario
        return self.key
    
    def set_key(self,nuevaKey):
        self.key = nuevaKey

def crearBotones(textoParaBotones):
    random.shuffle(textoParaBotones)
    botones = []
    for i in range(4):
        b = NuevoBoton(textoParaBotones[i],str(i))
        botones.append(b)
        #botones.append(sg.Button(textoParaBotones[i],size=(10,2),key='boton',visible=True))
    bot = [botones[0].button,botones[1].button,botones[2].button,botones[3].button]
    #bot.append (botones[0].button)
    return bot
#    return botones

def randomizarBotones (ven,botones,pos):
    ven[e].Update(botones[e].set_key('A'))


def actualizarLayout(textoParaBotones):
    layout =[
        [sg.Text('ACÁ VAMOS A RANDOMIZAR BOTONES',font=('Arial 12'),key='pato')],
        crearBotones(textoParaBotones),
    ]
    return layout

respuestas = ['respuesta1','respuesta2','respuesta3']
preguntas = [
    ['respuesta1','respuestaA','respuestaB','respuestaC'],
    ['respuesta2','respuestaD','respuestaE','respuestaF'],
    ['respuesta3','respuestaG','respuestaH','respuestaI']
    ]




textoParaBotones = ['hola','chau','pato','araña']
totBot = 4
correcto = 'pato'
ven = sg.Window('',actualizarLayout(textoParaBotones),size=(600,200))
ven.Finalize()
while True:
    e ,value  = ven.read()
    if (e == None):
        break
    if (e in ['0','1','2']):
        print ('RESPUESTA: ' + str(respuestas[0]==preguntas[0][int(e)]))
        #print (respuestas[int(e)])
        #print (preguntas[0][1])
        #print (respuestas[2]==preguntas[2][2])
        randomizarBotones(ven,ven.FindElement('0'),e)
        


    #if (e == 'ok'):
     #   if (ven.FindElement('c').Get()==True): #Busca la key 'c' y si está habilitada, entra al if
      #      print ('GANASTE')
       # else:
        #    print('PERDISTE')


ven.Close()