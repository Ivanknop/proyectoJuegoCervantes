import PySimpleGUI as sg
from tema import *
from interfazCargaConsignas import *

def interfaz():
    col1 = [
        [sg.Button('Jugar',font=('Arial 16'),size=(12,3),key='jugar'),
        sg.Button('Ingresar como Docente',font=('Arial 16'),size=(12,3),key='docente'),
        sg.Button('Puntuaciones',font=('Arial 16'),size=(12,3),key='puntos'),
        sg.Button('Salir',font=('Arial 16'),size=(12,3),key='salir')]
    ]
    layout = [
            [sg.Text ('BIENVENIDE!!',font=('Arial 30'),justification='center',key='bienvenido')],
            [sg.Column(col1,justification='center')]
    ]
    return layout


def principal():
    alto = 500
    ancho = 700
    tema()
    ventana = sg.Window ('Juego Cervantes: Inicio',interfaz(), size = (ancho,alto),element_justification='center')
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir') :
            break
        if (evento == 'docente'):
            clave = sg.popup_get_text('Ingrese la clave',password_char='*')
            if (clave=='ivan'):
                inicio()
            else:
                print('No entiendo')
            
    ventana.Close()

principal()