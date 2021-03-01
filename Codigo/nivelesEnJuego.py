from nivel import *

'''
Una lista de los niveles en juego disponibles
Se crea al inicializar una partida. 
Debe resetearse cada vez que se oprime en 'JUGAR'
'''
class NivelesEnJuego():
    def __init__(self,totalNiveles):
        self._niveles = []
        self._correctos = []
        self._totalNiveles = totalNiveles
        self.inicializarCorrectos()
    
    def inicializarCorrectos(self):
        for i in range(self.getTotalNiveles()):
            self._correctos.append(0)

    def getTotalNiveles(self):
        return self._totalNiveles

    def nivelCorrecto(self,pos,puntos):
        self._correctos[pos] = puntos
    
    def nivelIncorrecto(self,pos):
        self._correctos[pos]=-10
    
    def verRespuestas(self):
        return self._correctos
    
    def agregarNivel(self,nivel):
        self._niveles.append(nivel)
    
    def resultadoFinal (self):
        return sum(self.verRespuestas())
    

    

