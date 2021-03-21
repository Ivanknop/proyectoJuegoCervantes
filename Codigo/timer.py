import time
import PySimpleGUI as sg

tiempoActual = 0
tiempoFinal = 20
while (tiempoActual < 10) :
    print (tiempoActual%60)
    tiempoActual = tiempoFinal +time.time()

def actualizarTimer(ven,cont):
    ven['timer'].Update('{:02d}'.format(int(cont%60)))

contenedor = [
    [sg.Text(tiempoActual,size=(10,2),font=('Italic 12'),key='timer')],
    [sg.Button('oprimir',key='oprimir')]
]
ven = sg.Window ('timer',contenedor,size=(300,300))
ven.Finalize()
while True:
    e,v = ven.read()
    while tiempoActual <10:
        actualizarTimer(ven,tiempoActual)
        tiempoActual = time.time()
    if (e == None):
        break
    if (e == 'oprimir'):
        actualizarTimer(ven,tiempoActual)
        tiempoActual = time.time()
ven.Close()