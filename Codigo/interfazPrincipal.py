import PySimpleGUI as sg
from tema import tema
from interfazCargaConsignas import *
from interfazJuego import *
import os 
from Jugador import *
from cargaDeConsignas import *
from nivelesEnJuego import *

def interfazInicial(imgBoton,quijote):
    
    layout= [
        [sg.Image (filename=quijote,size=(600,200),key='bienvenido')],
        [sg.Button('Jugar',image_filename=imgBoton,font='MedievalSharp 20',size=(12,3),key='jugar'),
        sg.Button('Puntuaciones',image_filename=imgBoton,font='MedievalSharp 16',size=(12,3),key='puntos'),
        sg.Button('Salir',image_filename=imgBoton,font='MedievalSharp 20',size=(12,3),key='salir')]
    ]
    version = [
        [sg.Text('Versión 0.1 beta',pad=(50,50),justification='left')],
        [sg.Button('Ingresar como Docente',image_filename=imgBoton,font='MedievalSharp 8',size=(10,2),key='docente')]
        ]
    return layout + version

def principal():
    alto = 500
    ancho = 700
    tema()
    consignas = AlmacenamientoConsignas()
    imgBoton = os.path.join('multimedia','cuadro.png')
    quijote = os.path.join('multimedia','quijoteLogo.png')
    
    ventana = sg.Window ('Juego Cervantes: Inicio',interfazInicial(imgBoton,quijote), size = (ancho,alto),element_justification='center')
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir' or evento=='salir2') :
            break
        if (evento == 'docente'):
            clave = sg.popup_get_text('Ingrese la clave',password_char='*',font='MedievalSharp 10')
            if (clave=='reshu'):
                inicioConsignas()
            else:
                sg.popup('clave incorrecta \n Intente nuevamente',font='MedievalSharp 10')
        if (evento == 'jugar'):
            
            nombre = sg.popup_get_text('Ingrese su nombre',font='MedievalSharp 10')
            if (nombre != '') and (len(nombre)>2) and (len(nombre)<20):
                jugador = Jugador(nombre)
                break
            else:
                sg.popup('El nombre debe tener entre 3 y 30 caracteres',font='MedievalSharp 10')
        if (evento == 'puntos'):
            sg.popup('PUNTAJES en construcción',font='MedievalSharp 10')
    ventana.Close()
    return jugador, consignas
