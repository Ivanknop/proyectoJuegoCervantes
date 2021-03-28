import time
import PySimpleGUI as sg
class Reloj():
    def __init__(self,tiempoFinal):
        self.tiempoInicial = 0
        self.tiempoFinal = tiempoFinal*60
        self.tiempoPC = int(round(time.time() * 100))

    def getTiempoInicial(self):
        return self.tiempoInicial
    def getTiempoFinal(self):
        return self.tiempoFinal
    def getTiempoPC(self):
        return self.tiempoPC
    def setTiempoInicial(self,nuevoTiempo):
        self.tiempoInicial=nuevoTiempo
    def setTiempoFinal(self,nuevoTiempo):
        self.tiempoFinal=nuevoTiempo

    def actualizarTiempo(self):      
        self.setTiempoInicial(int(round(time.time() * 100)) - self.getTiempoPC())

    def resetTiempo(self):
        self.setTiempoInicial(0)
        self.tiempoPC = int(round(time.time() * 100))
    
    def terminoTimer(self):
        return self.getTiempoInicial() > self.getTiempoFinal()*100
