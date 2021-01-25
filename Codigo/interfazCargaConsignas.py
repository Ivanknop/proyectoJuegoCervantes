import PySimpleGUI as sg
from cargaDeConsignas import *


def interfazPrincipal ():
    layout = [
        [sg.Text('Agregue una nueva pregunta',font = ('Italic 16'),key='consignas')],
        [sg.InputText('',font=('Italic 10'),background_color='#ea899a',key='newPreg')],
        [sg.Text('Agregue la respuesta correcta',font = ('Italic 16'),key='respuestas')],
        [sg.InputText('',font=('Italic 10'),background_color='#ea899a',key='newRta')],
        [sg.Button('Agregar Consigna',size=(10,2),border_width=1,button_color=('black','#afad71'),key = 'preguntas'),
        sg.Button('ver preguntas',size=(10,2),border_width=1,button_color=('black','#afad71'),key = 'imprimir'),
        sg.Button('Salir',size=(10,2),border_width=1,button_color=('black','#afad71'),key = 'salir'),
        ]
    ]
    return layout  

def verConsignas (archivo):
    listadoClave = []
    listadoValor = []
    for preg in range(len(archivo.preguntas)):
        listadoClave = listadoClave + list(archivo.preguntas[preg].keys())
        #listadoCOnsignas = listadoCOnsignas + 'Pregunta '+str(preg+1)+': '+ list(archivo.preguntas.keys())
        listadoValor=listadoValor + list(archivo.preguntas[preg].values())
    listado = ''
    for p in range(len(archivo.preguntas)):
        listado = listado + ' ' +str(listadoClave[p])+': '+str(listadoValor[p])
    print (listado)
    print(archivo.imprimirPreguntas())

def inicio():
    altura = 400
    largo = 200
    archivo = AlmacenamientoConsignas()
    ventana = sg.Window ('Juego Cervantes',interfazPrincipal(), size = (altura,largo),background_color='#f9e4b7')
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir') :
            break
        if (evento == 'preguntas'):
            archivo.agregarConsigna(value['newPreg'],value['newRta'])
        if (evento == 'imprimir'):
            verConsignas(archivo)
    ventana.Close()

inicio()