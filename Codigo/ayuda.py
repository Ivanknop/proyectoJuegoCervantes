import PySimpleGUI as sg
from tema import *

def presentacion(nombre):
    layout = [
        [sg.Text('BIENVENIDE AL JUEGO DE PREGUNTAS Y RESPUESTAS',font='MedievalSharp 20')],
        [sg.Text('A lo largo de 5 niveles debereis comprobar vuestro saber y valía. \n'
        'Debereis escoger, para cada pregunta, 1 y sólo 1 de las respuestas posibles. \n '
        'Si escogeis bien, sumarais. Pero si no, restarais. \n'
        'CUIDADO!!! El tiempo para responder cada consigna es solo de 1 minuto. Si demorais más, perderais. \n'
        'Os he otorgado un bonus especial para resetear el tiempo... PERO VALE PARA UN ÚNICO NIVEL \n'
        ,font='MedievalSharp 15',size=(45,10),auto_size_text=True,justification='center')],
        [sg.Text('            ¡BUENA VENTURA '+nombre.upper()+' !',font='MedievalSharp 20',justification='right')],
        [sg.Button('Continuar',size = (10,2),pad=(200,0),key='continuar')]
    ]
    return layout

def ayuda(nombre):
    layout = [
        [sg.Text('¿NECESITAS AYUDA?'+str(nombre),font='MedievalSharp 20')],
        [sg.Text('DESPUÉS TE DIGO COMO... JEJE\n'
        ,font='MedievalSharp 15',size=(45,10),auto_size_text=True,justification='center')],
        [sg.Text('            ¡BUENA VENTURA '+nombre.upper()+' !',font='MedievalSharp 20',justification='right')],
        [sg.Button('Continuar',size = (10,2),pad=(200,0),key='continuar')]
    ]
    return layout    

def explicacionJuego(nombre):
    altura = 500
    largo = 400
    tema()
    ventana = sg.Window ('Juego Cervantes',presentacion(nombre), size = (altura,largo))
    ventana.Finalize()
    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'continuar') :
            break
        
    ventana.Close()

def explicacionAyuda(nombre):
    altura = 500
    largo = 400
    tema()
    ventana = sg.Window ('Juego Cervantes',ayuda(nombre), size = (altura,largo))
    ventana.Finalize()
    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'continuar') :
            break
        
    ventana.Close()

#explicacionJuego('lala')
