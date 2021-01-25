import PySimpleGUI as sg

def interfaz(texto):
    col = [
        [sg.Text('CONSGINAS ALMACENADAS',font = ('Italic 16'),key='consignas')],
        [sg.Text(texto,font=('Italic 10'),auto_size_text=True)]
        ]
    layout = [
        [sg.Column(col, scrollable=(True),vertical_scroll_only=True)],
        [sg.Button('Salir',size=(5,1),border_width=1,button_color=('black','#afad71'),key = 'salir'),
        sg.Button('Borrar consigna',size=(12,1),border_width=1,button_color=('black','#afad71'),key = 'borrar'),
        ]
    ]
    return layout

def borrarConsigna():
    return sg.popup_get_text('Qué consigna desea borrar')

def esNumeroValido(cadena,almacenamiento):
    if (cadena.isdigit()) and (int(cadena)<=len(almacenamiento)):
        return cadena
    else:
        return ('No entiendo')

def consignas(texto):
    altura = 400
    largo = 200
    ventana = sg.Window ('Juego Cervantes: Consignas',interfaz(texto), size = (altura,largo),background_color='#f9e4b7',)
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir') :
            break
        if (evento == 'borrar'):
            borrar = borrarConsigna()
            print (esNumeroValido(borrar,texto))
    ventana.Close()