import PySimpleGUI as sg
import random
from nivel import *
import pickle
from cargaDeConsignas import *
from nivelesEnJuego import *

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

def interfazJuego(imgBoton,jugador,consignas):
    nivelActual = jugador.getNivel()
    nivel = Nivel (jugador.getNivel(),consignas.consignaEnPosicion(nivelActual)['pregunta'],consignas.consignaEnPosicion(nivelActual)['respuesta1']
    ,[consignas.consignaEnPosicion(nivelActual)['respuesta2'],consignas.consignaEnPosicion(nivelActual)['respuesta3']
    ,consignas.consignaEnPosicion(nivelActual)['respuesta4']])
    print (nivel)
    titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
    botonesPreguntas = crearBotones(imgBoton,consignas.consignaEnPosicion(0))   
    layout = [
        [sg.Text(titulo,font='Italic 16'),
        sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver'),sg.Button('salir',key='salir2')],
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('NIVEL'+str(jugador.getNivel()),key='nivel')],
        [sg.Text(consignas.consignaEnPosicion(0)['pregunta'],key='nroPregunta')],
        botonesPreguntas,
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('JUGADOR '+ jugador.getNombre().upper(),key='jugNombre'),sg.Text('Puntaje: '+str(jugador.getPuntaje()),key='jugPje')],
        [sg.Button('BONUS 1',key='bonus1'),sg.Button('BONUS 2',key='bonus1')]
    
    ]
    return layout