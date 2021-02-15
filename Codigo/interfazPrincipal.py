import PySimpleGUI as sg
from tema import *
from interfazCargaConsignas import *
from interfazJuego import *
import os 
from jugadorBeta import *
from cargaDeConsignas import *

def actualizarColumna(ventana,*columna):
    for e in ventana.element_list():
        if e.Type == 'column':
            if e.Visible == False and e.Key in columna:
                ventana.FindElement (e.Key).update(visible=True)
            elif e.Key in columna:
                ventana.FindElement(e.Key).update(visible=True)
            else:
                ventana.FindElement(e.Key).update(visible=False)


def interfazInicial(imgBoton):
    
    layout= [
        [sg.Text ('BIENVENIDE!!',font=('Arial 30'),justification='center',key='bienvenido')],
        [sg.Button('Jugar',image_filename=imgBoton,font=('Arial 16'),size=(12,3),key='jugar'),
        sg.Button('Ingresar como Docente',image_filename=imgBoton,font=('Arial 14'),size=(12,3),key='docente'),
        sg.Button('Puntuaciones',image_filename=imgBoton,font=('Arial 16'),size=(12,3),key='puntos'),
        sg.Button('Salir',image_filename=imgBoton,font=('Arial 16'),size=(12,3),key='salir')]
    ]
    return layout

def interfazDeInicio(nivel,imgBoton,jugador,consignas):
    colInicial = interfazInicial(imgBoton)
    colJugar = interfazJuego(nivel,imgBoton,jugador,consignas)

    layout = [
            
            [sg.Column(colInicial,visible=True,justification='center',key='colInicio'),
            sg.Column(colJugar,visible=False,justification='center',key='colJugar')]
    ]
    return layout

def principal():
    alto = 500
    ancho = 700
    tema()
    nivel = 1
    consignas = AlmacenamientoConsignas()
    jugador = JugadorBeta ('Iván')
    imgBoton = os.path.join('multimedia','cuadro.png')
    ventana = sg.Window ('Juego Cervantes: Inicio',interfazDeInicio(nivel,imgBoton,jugador,consignas), size = (ancho,alto),element_justification='center')
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir' or evento=='salir2') :
            break
        if (evento == 'docente'):
            clave = sg.popup_get_text('Ingrese la clave',password_char='*')
            if (clave=='ivan'):
                inicio()
            else:
                sg.popup('clave incorrecta \n Intente nuevamente')
        if (evento == 'jugar'):
            actualizarColumna(ventana,'colJugar')
        if (evento == 'puntos'):
            sg.popup('PUNTAJES en construcción')
        if (evento == 'volver'):
            actualizarColumna (ventana,'colInicio')
        if (ventana['colInicio'].Visible==True):
            if (evento =='1'):
                jugador.incrementarNivel()
                pasarNivel(ventana,jugador.getNivel(),imgBoton)
            else: print('chau')
            
    ventana.Close()

principal()