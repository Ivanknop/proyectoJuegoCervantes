import PySimpleGUI as sg
import random
from nivel import *
from tema import *
import pickle
from cargaDeConsignas import *
from nivelesEnJuego import *
from Jugador import *

class InterfazJuego ():
    '''Mega clase'''
    def __init__(self, imgBoton,jugador,consignas):
        self._jugador = jugador
        self._consignas = consignas
        self._imagenBoton = imgBoton
    
    def getJugador (self):
        return self._jugador

    def getInterfaz(self):
        return self.interfazJuego()
    
    def getConsignas(self):
        return self._consignas

    def getBoton (self):
        return self._imagenBoton

    def interfazJuego(self):
        nivelActual = self.getJugador().getNivel()
        jugador = self.getJugador()
        print(self.getConsignas().consignaEnPosicion(nivelActual))
        titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
        botonesPreguntas = self.crearBotones(self.getConsignas().consignaEnPosicion(nivelActual))   
        layout = [
            [sg.Text(titulo,font='Italic 16'),
            sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver'),sg.Button('salir',key='salir')],
            #[sg.HorizontalSeparator(pad=None)],
            [sg.Text('NIVEL'+str(nivelActual),key='nivel')],
            [sg.Text(self.getConsignas().consignaEnPosicion(0)['pregunta'],key='nroPregunta')],
            botonesPreguntas,
            [sg.Text('JUGADOR '+ jugador.getNombre().upper(),key='jugNombre'),sg.Text('Puntaje: '+str(jugador.getPuntaje()),key='jugPje')],
            [sg.Button('BONUS 1',key='bonus1'),sg.Button('BONUS 2',key='bonus1')]
            ]
        
        return layout

    def crearBotones(self,c):
        botones = []
        for i in range(4):
            botones.append(sg.Button(c['respuesta'+str(i+1)],image_filename=self.getBoton(),key=str(i)))
        random.shuffle(botones)
        return botones

    def pasarNivel(self,ven):
        nivelActual = self.getJugador().getNivel()
        ven['nivel'].Update('NIVEL'+str(nivelActual))
        ven['nroPregunta'].Update(self.getConsignas().consignaEnPosicion(nivelActual)['pregunta'])
        indices = [0,1,2,3]
        random.shuffle(indices)
        #print (indices) #No logro que se randomice la actualización de los botones
        for i in range(3):
            ven[str(indices[i+1])].Update(self.getConsignas().consignaEnPosicion(nivelActual)['respuesta'+str(indices[i]+1)])
        #if ok:
         #   niveles.nivelCorrecto(jugador.getNivel())
        #else:
         #   niveles.nivelIncorrecto(jugador.getNivel())
        self.getJugador().incrementarNivel()
        #return nivelActual

def inicio(jugador,consignas):
    tema()
    alto = 500
    ancho = 700
    imgBoton = os.path.join('multimedia','cuadro.png')  
    interfaz = InterfazJuego (imgBoton,jugador,consignas) 
    ventana = sg.Window ('Juego Cervantes: Inicio',interfaz.getInterfaz(), size = (ancho,alto),element_justification='center')
    ventana.Finalize()
    while True:
        evento, valor = ventana.read()
        if (evento == None or evento =='salir'):
            break
        if (evento == '0'):
            print('NIVEL ACTUAL: '+ str(interfaz.getJugador().getNivel()))
            interfaz.pasarNivel(ventana)
    ventana.Close()

''' LO QUE SIGUE ABAJO VA EN ALGÚN LADO DE LA VENTANA'''
       # if (evento == 'volver'):
        #    actualizarColumna (ventana,'colInicio')
        #if (ventana['colJugar'].Visible==True):
       # if (evento == '0'):
        #    jugador.incrementarNivel() 
         #   print (jugador.getNivel())
          #  try:           #Permite controlar el máximo de consignas cargadas
           #     pasarNivel(ventana,True,jugador,imgBoton,consignas,nivelesJugando)
            #except:
             #   print (nivelesJugando.resultadoFinal())
                #actualizarColumna(ventana,'colInicio')
        #else: pasarNivel(ventana,False,jugador,imgBoton,consignas,nivelesJugando)