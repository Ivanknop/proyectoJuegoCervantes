import PySimpleGUI as sg

def tema():
    '''
    Configuración genérica del diseño de las interfaces que facilita el diseño. 
    Después se adapta a la especificidad de cada pestaña.
    '''
    sg.LOOK_AND_FEEL_TABLE['juego'] = {'BACKGROUND': '#133d51', #f9e4b7', #'#4f280a'
                                            'TEXT': '#fff4c9',
                                            'INPUT': '#c7e78b',
                                            'TEXT_INPUT': '#000000',
                                            'SCROLL': '#c7e78b',
                                            'BUTTON': ('black','#afad71'),
                                            'PROGRESS': ('#01826B', '#D0D0D0'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                            }
    sg.theme('juego')