import PySimpleGUI as sg
import random

def crearBotones(imgBoton):
    botones = []
    for i in range(4):
        botones.append(sg.Button('Respuesta'+str(i),image_filename=imgBoton,key=str(i)))
    random.shuffle(botones)
    return botones

def pasarNivel(ven,nivel,imgBoton):
    ven['nivel'].Update('NIVEL'+str(nivel))

def interfazJuego(nivel,imgBoton,jugador):
    titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
    botonesPreguntas = crearBotones(imgBoton)   
    layout = [
        [sg.Text(titulo,font='Italic 16'),
        sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver'),sg.Button('salir',key='salir2')],
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('NIVEL'+str(nivel),key='nivel')],
        [sg.Text('ESTA ES LA PREGUNTA')],
        botonesPreguntas,
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('JUGADOR '+ jugador.getNombre().upper(),key='jugNombre'),sg.Text('Puntaje: '+str(jugador.getPuntaje()),key='jugPje')],
        [sg.Button('BONUS 1',key='bonus1'),sg.Button('BONUS 2',key='bonus1')]
    
    ]
    return layout