import time
import PySimpleGUI as sg

class Reloj ():
    def __init__(self):
        self.contadorTiempo = 0
        self.tiempoActual = int(round(time.time() * 100))
        self.tiempoFinalizacion = time.time() + 60
        self.pausado = False

    def getPausa (self):
        return self.pausado
    def getTiempoActual (self):
        return self.tiempoActual
    def getContadorTiempo(self):
        return self.contadorTiempo
    
    def actualizarContadorTiempo(self):
        self.contadorTiempo = int(round(time.time() * 100)) - self.getTiempoActual()
    
    def resetTiempo(self):
        self.contadorTiempo = 0
        self.tiempoActual = int(round(time.time() * 100))
    
    def seTerminoTimer(self):
        return time.time() > self.tiempoFinalizacion

'''
reloj = Reloj()
#tiempoActual = 0
paused = False
#tiempoInicio = int(round(time.time() * 100))

def actualizarTimer(ven,cont):
    ven['text'].update('{:02d}:{:02d}.{:02d}'.format((cont // 100) // 60,(cont // 100) % 60,cont % 100))


layout = [[sg.Text('')],
         [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [sg.Button('Pause', key='Pause', button_color=('white', '#001480')),
         sg.Button('Run', key='Run', button_color=('white', '#001480')),
          sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

ven = sg.Window ('timer',layout,size=(300,300))
ven.Finalize()
while True:
    if not paused:
        e,v = ven.read(timeout=10)
        reloj.actualizarTiempoActual()
    else:
        e,v = ven.read()
    if (e == None or e =='Exit'):
        break
    if (e == 'Pause'):
        if paused == False:
            paused = True
            tiempoPausa = int(round(time.time() * 100))
        else:
            paused = False
            tiempoActual = int(round(time.time() * 100)) - tiempoPausa
        #actualizarTimer(ven,tiempoActual)
        
        actualizarTimer(ven,reloj.getTiempoEnCero())
    if (e== 'Reset'):
        tiempoInicio = int(round(time.time() * 100))
        tiempoActual: 0
        tiempoPausa = tiempoInicio 
    actualizarTimer(ven,reloj.getTiempoEnCero())
    #actualizarTimer(ven,tiempoActual)
ven.Close()
'''