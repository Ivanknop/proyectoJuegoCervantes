import PySimpleGUI as sg
import random


def pasarNivel(ven,nivel):
    ven['nivel'].Update('NIVEL'+str(nivel))

def interfazJuego(nivel,imgBoton):
    titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
    colPreg1 = [
        sg.Button('lalala 1',image_filename=imgBoton,key='1'),sg.Button('lalala 2',image_filename=imgBoton,key='2')
        ]
    ladoJugador =[sg.Button('lalala 3',image_filename=imgBoton,key='3'),sg.Button('lalala 4',image_filename=imgBoton,key='4')]

    layout = [
        [sg.Text(titulo,font='Italic 16'),
        sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver'),sg.Button('salir',key='salir2')],
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('NIVEL'+str(nivel),key='nivel')]
    ]
    layout+=[colPreg1]
    layout+=[ladoJugador]
    return layout