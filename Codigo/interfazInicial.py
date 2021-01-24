import PySimpleGUI as sg


def interfazPrincipal ():
    layout = [
        [sg.Button(size=(5,5),key = 'preguntas'),
        sg.Button(size=(5,5),key = 'jugador')]
    ]
    return layout

def inicio():
    altura = 900
    largo = 700

    ventana = sg.Window ('Juego Cervantes',interfazPrincipal(), size = (altura,largo))
    ventana.Finalize()

    while True:
        event, value = ventana.read()
        if (event == None):
            break
    ventana.Close()

inicio()