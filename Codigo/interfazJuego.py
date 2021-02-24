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
    def __init__(self, imgBoton,nombreJugador):
        self.__jugador = Jugador (nombreJugador)
        self.__interfaz = interfazJuego2(imgBoton)
        self.__consignas = AlmacenamientoConsignas()


def crearBotones(imgBoton,consignas):
    botones = []
    print (consignas['pregunta'])
    for i in range(4):
        botones.append(sg.Button(consignas['respuesta'+str(i+1)],image_filename=imgBoton,key=str(i)))
    random.shuffle(botones)
    return botones

def pasarNivel(ven,ok,jugador,imgBoton,consignas,niveles):
    nivelActual = jugador.getNivel()
    ven['nivel'].Update('NIVEL'+str(nivelActual))
    ven['nroPregunta'].Update(consignas.consignaEnPosicion(nivelActual)['pregunta'])
    indices = [0,1,2,3]
    random.shuffle(indices)
    print (indices) #No logro que se randomice la actualización de los botones
    for i in range(4):
        ven[str(indices[i])].Update(consignas.consignaEnPosicion(nivelActual)['respuesta'+str(indices[i]+1)])
    if ok:
        niveles.nivelCorrecto(jugador.getNivel())
    else:
        niveles.nivelIncorrecto(jugador.getNivel())

    return nivelActual

def interfazJuego(imgBoton, jugador,consignas): 
    
    nivelActual = jugador.getNivel()
    nivel = Nivel (jugador.getNivel(),consignas.consignaEnPosicion(nivelActual)['pregunta'],consignas.consignaEnPosicion(nivelActual)['respuesta1']
    ,[consignas.consignaEnPosicion(nivelActual)['respuesta2'],consignas.consignaEnPosicion(nivelActual)['respuesta3']
    ,consignas.consignaEnPosicion(nivelActual)['respuesta4']])
    print (nivel)
    titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
    botonesPreguntas = crearBotones(imgBoton,consignas.consignaEnPosicion(0))   
    layout = [
        [sg.Text(titulo,font='Italic 16'),
        sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver'),sg.Button('salir',key='salir')],
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('NIVEL'+str(jugador.getNivel()),key='nivel')],
        [sg.Text(consignas.consignaEnPosicion(0)['pregunta'],key='nroPregunta')],
        botonesPreguntas,
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('JUGADOR '+ jugador.getNombre().upper(),key='jugNombre'),sg.Text('Puntaje: '+str(jugador.getPuntaje()),key='jugPje')],
        [sg.Button('BONUS 1',key='bonus1'),sg.Button('BONUS 2',key='bonus1')]
    
    ]
    return layout

def inicio(jugador,consignas):
    tema()
    alto = 500
    ancho = 700
    imgBoton = os.path.join('multimedia','cuadro.png')   
    ventana = sg.Window ('Juego Cervantes: Inicio',interfazJuego(imgBoton,jugador,consignas), size = (ancho,alto),element_justification='center')
    ventana.Finalize()
    while True:
        evento, valor = ventana.read()
        if (evento == None or evento =='salir'):
            break
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