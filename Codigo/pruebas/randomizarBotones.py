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


def actualizarLayout(textoParaBotones):
    layout =[
        [sg.Text('ACÁ VAMOS A RANDOMIZAR BOTONES',font=('Arial 12'),key='pato')],
        #[botones[0].button],[botones[1].button],[botones[2].button],[botones[3].button]
        crearBotones(textoParaBotones),
        [sg.Text('ACÁ VAMOS A RANDOMIZAR FOTONES',font=('Arial 12'),key='gato')]
    ]
    return layout

textoParaBotones = ['hola','chau','pato','araña']
totBot = 4
correcto = 'pato'
ven = sg.Window('',actualizarLayout(textoParaBotones),size=(600,200))
ven.Finalize()
while True:
    e ,value  = ven.read()
    if (e == None):
        break
    else:
        #ven[e].Update(visible=False)
        random.shuffle(textoParaBotones)
        for i in range (4):
            ven.FindElement(str(i)).Update(textoParaBotones[i]) 
        totBot -= 1
    if (totBot == 0):
        print('listo')
        break
    

    


ven.Close()