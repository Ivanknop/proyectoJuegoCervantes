import PySimpleGUI as sg
from cargaDeConsignas import *
from interfazConsignas import *
from tema import *
import random


def interfazPrincipal ():
    layout = [
        [sg.Text('Agregue una nueva pregunta',font='MedievalSharp 10',key='consignas')],
        [sg.InputText('',font='MedievalSharp 10',key='newPreg',do_not_clear=False)],
        [sg.Text('Agregue la respuesta correcta',font='MedievalSharp 10',key='respuestas')],
        [sg.InputText('',font='MedievalSharp 10',key='newRta',do_not_clear=False)],
        [sg.Text('Respuesta Incorrecta 1',font='MedievalSharp 10',key='mal1')],
        [sg.InputText('',font='MedievalSharp 10',key='inc1',do_not_clear=False)],
        [sg.Text('Respuesta Incorrecta 2',font='MedievalSharp 10',key='mal2')],
        [sg.InputText('',font='MedievalSharp 10',key='inc2',do_not_clear=False)],
        [sg.Text('Respuesta Incorrecta 3',font='MedievalSharp 10',key='mal3')],
        [sg.InputText('',font='MedievalSharp 10',key='inc3',do_not_clear=False)]
    ]
    layoutBotones = [
        [sg.Button('Agregar Consigna',font='MedievalSharp 10',size=(10,2),border_width=1,key = 'preguntas'),
        sg.Button('ver preguntas',font='MedievalSharp 10',size=(10,2),border_width=1,key = 'imprimir'),
        sg.Button('Vacias Consginas',font='MedievalSharp 10',size=(10,2),border_width=1,key ='vaciar'),
        sg.Button('Salir',font='MedievalSharp 10',size=(10,2),border_width=1,key = 'salir')
        ]
    ]
    colPreguntas= layout
    colBotones = layoutBotones

    layout3 = [
            
            [sg.Column(colPreguntas,justification='center',key='colPreg'),
            sg.Column(colBotones,justification='center',key='colBot')]
    ]
    return layout3  

def verConsignas (archivo):
    listado2 = list(archivo.preguntas)
    random.shuffle(listado2)
    listaFinal = ''
    for p in listado2:
        listaFinal = listaFinal + str(p)+ '\n' 
    consignas(listaFinal)
    
def inicioConsignas():
    altura = 500
    largo = 450
    tema()
    archivo = AlmacenamientoConsignas()
    ventana = sg.Window ('Juego Cervantes',interfazPrincipal(), size = (altura,largo))
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir') :
            break
        if (evento == 'preguntas'):
            archivo.agregarConsigna(value['newPreg'],value['newRta'],value['inc1'],value['inc2'],value['inc3'])
        if (evento == 'imprimir'):
            verConsignas(archivo)
        if (evento =='vaciar'):
            decision = aviso('Realmente desea borrar las consignas cargadas?',['SI','NO'])
            if (decision == '_SI'):
                print ('ok')    
                archivo.vaciarConsignas()
            else:
                print (archivo.imprimirPreguntas())
    ventana.Close()

#inicio()