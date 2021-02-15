import PySimpleGUI as sg
import random
#from nivel import *
import pickle
from cargaDeConsignas import *

def crearBotones2(imgBoton,consignas):
    botones = [
        sg.Button(consignas['respuesta1'],key = '1')
        ]

    return botones

def crearBotones(imgBoton,consignas):
    botones = []
    print (consignas['pregunta'])
    for i in range(4):
        botones.append(sg.Button(consignas['respuesta'+str(i+1)],image_filename=imgBoton,key=str(i)))
    random.shuffle(botones)
    return botones

def pasarNivel(ven,nivel,imgBoton):
    ven['nivel'].Update('NIVEL'+str(nivel))

def interfazJuego(nivel,imgBoton,jugador,consignas):
    print(consignas.consignaEnPosicion(0))
    titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
    botonesPreguntas = crearBotones(imgBoton,consignas.consignaEnPosicion(1))   
    layout = [
        [sg.Text(titulo,font='Italic 16'),
        sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver'),sg.Button('salir',key='salir2')],
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('NIVEL'+str(nivel),key='nivel')],
        [sg.Text(consignas.consignaEnPosicion(1)['pregunta'])],
        botonesPreguntas,
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('JUGADOR '+ jugador.getNombre().upper(),key='jugNombre'),sg.Text('Puntaje: '+str(jugador.getPuntaje()),key='jugPje')],
        [sg.Button('BONUS 1',key='bonus1'),sg.Button('BONUS 2',key='bonus1')]
    
    ]
    return layout