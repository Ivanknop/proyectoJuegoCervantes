import PySimpleGUI as sg
import random


def pasarNivel(ven,nivel):
    ven['nivel'].Update('NIVEL'+str(nivel))

def interfazJuego(nivel):
    titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
    colPreg1 = [
        sg.Button('lalala 1',key='1'),sg.Button('lalala 2',key='2')
        ]
    ladoJugador =[sg.Button('lalala 3',key='3'),sg.Button('lalala 4',key='4')]

    layout = [
        [sg.Text(titulo,font='Italic 16'),
        sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver'),sg.Button('salir',key='salir2')],
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('NIVEL'+str(nivel),key='nivel')]
    ]
    layout+=[colPreg1]
    layout+=[ladoJugador]
    return layout