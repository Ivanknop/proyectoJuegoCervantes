import PySimpleGUI as sg
from tema import *
from interfazCargaConsignas import *
from interfazJuego import *
import os 
from jugadorBeta import *
from cargaDeConsignas import *
from nivelesEnJuego import *

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

def interfazDeInicio(imgBoton,jugador,consignas):
    colInicial = interfazInicial(imgBoton)
    colJugar = interfazJuego(imgBoton,jugador,consignas)

    layout = [
            
            [sg.Column(colInicial,visible=True,justification='center',key='colInicio'),
            sg.Column(colJugar,visible=False,justification='center',key='colJugar')]
    ]
    return layout

def principal():
    alto = 500
    ancho = 700
    tema()
    consignas = AlmacenamientoConsignas()
    jugador = JugadorBeta ('Iván')
    imgBoton = os.path.join('multimedia','cuadro.png')
    nivelesJugando = NivelesEnJuego (3)
    
    ventana = sg.Window ('Juego Cervantes: Inicio',interfazDeInicio(imgBoton,jugador,consignas), size = (ancho,alto),element_justification='center')
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
        #if (ventana['colJugar'].Visible==True):
        if (evento == '0'):
            jugador.incrementarNivel() 
            print (jugador.getNivel())
            try:           #Permite controlar el máximo de consignas cargadas
                pasarNivel(ventana,True,jugador,imgBoton,consignas,nivelesJugando)
            except:
                print (nivelesJugando.resultadoFinal())
                #actualizarColumna(ventana,'colInicio')
        #else: pasarNivel(ventana,False,jugador,imgBoton,consignas,nivelesJugando)
    ventana.Close()

principal()