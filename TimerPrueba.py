import time
run = input("Start? > ")
seg = 0
# Only run if the user types in "start"
if run == "ok":
    # Loop until we reach 20 minutes running
    while seg != 10:
        print (">>>>>>>>>>>>>>>>>>>>>" + str(seg))
        # Sleep for a minute
        time.sleep(1)
        # Increment the minute total
        seg += 1
    # Bring up the dialog box here

'''
class Reloj ():
    def __init__(self):
        self.contadorTiempo = 0 #atributo para contar el tiempo
        self.tiempoActual = int(round(time.time() * 100)) #registra el tiempo del computador en que empieza el timer

        self.pausado = False
        self.tiempoPausado = 0
    
    def getPausa (self):
        return self.pausado
    def getTiempoActual (self):
        return self.tiempoActual
    def getContadorTiempo(self):
        return self.contadorTiempo
    def getTiempoPausado(self):
        return self.tiempoPausado

    def setContadorTiempo(self,tiempo):
        self.contadorTiempo = tiempo
    def setTiempoActual (self,tiempo):
        self.tiempoActual = tiempo
    def setTiempoPausado (self,tiempo):
        self.tiempoPausado = tiempo
    def setPausar(self):
        self.pausado = not self.pausado        
    
    
    def pausar(self,instante):
        self.setPausar()
        self.setTiempoPausado(instante)
        self.tiempoActual = int(round(time.time() * 100)) - instante
        
    
    def retomar(self):
        self.setPausar()
        self.contadorTiempo = int(round(time.time() * 100)) - self.getTiempoPausado()     

    def actualizarContadorTiempo(self):
        self.contadorTiempo = int(round(time.time() * 100)) - self.getTiempoActual()
    
    def resetTiempo(self):
        self.contadorTiempo = 0
        self.tiempoActual = int(round(time.time() * 100))
    


reloj = Reloj()
#reloj.setearTimer(1)
#tiempoActual = 0
paused = False
#tiempoInicio = int(round(time.time() * 100))
reloj.resetTiempo()
def actualizarTimer(ven,cont):
    ven['text'].update('{:02d}:{:02d}.{:02d}'.format((cont // 100) // 60,(cont // 100) % 60,cont % 100))


layout = [[sg.Text('')],
         [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [sg.Button('Pause', key='Pause', button_color=('white', '#001480')),
         sg.Button('Run', key='Run', button_color=('white', '#001480')),
          sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]
instante =  int(round(time.time() * 100))

ven = sg.Window ('timer',layout,size=(300,300))
ven.Finalize()
while True:
    if reloj.getPausa():
        e,v = ven.read(timeout=10)
        reloj.actualizarContadorTiempo()
    else:
        e,v = ven.read()
    if (e == None or e =='Exit'):
        break
    if (e == 'Pause'):
        instante = int(round(time.time() * 100))
        if reloj.getPausa():
            
            #reloj.pausado() = True
            #reloj.setPausar()
            #instante = int(round(time.time() * 100))
            
            reloj.pausar(instante)
            #tiempoPausa = int(round(time.time() * 100))
        else:
            #reloj.pausar()
            reloj.retomar()
            #reloj.setContadorTiempo (int(round(time.time() * 100)) - instante)
            #reloj.setPausar()
            #tiempoActual = int(round(time.time() * 100)) - tiempoPausa
        #actualizarTimer(ven,tiempoActual)
        
        actualizarTimer(ven,int(reloj.getContadorTiempo()))
    if (e== 'Reset'):
        reloj.resetTiempo()
        tiempoInicio = int(round(time.time() * 100))
        tiempoActual: 0
        tiempoPausa = tiempoInicio 
    actualizarTimer(ven,int(reloj.getContadorTiempo()))
    #actualizarTimer(ven,tiempoActual)
ven.Close()
'''