import PySimpleGUI as sg

def interfazJuego():
    titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
    layout = [
        [sg.Text(titulo,font='Italic 16'),
        sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver')],
        [sg.HorizontalSeparator(pad=None)],
        [sg.Text('CONSIGNAS Y PREGUNTAS'),sg.VerticalSeparator(pad=(100,10)),sg.Text('ESPACIO PARA EL JUGADOR')]
    ]

    return layout