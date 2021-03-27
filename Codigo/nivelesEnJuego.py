from nivel import *
from cargaDeConsignas import *
import random

'''
Una lista de los niveles en juego disponibles
Se crea al inicializar una partida. 
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

    def puntuarNivel (self,pos,puntos):
        self._correctos[pos] = puntos
    
    def verRespuestas(self):
        return self._correctos
    
    def agregarNivel(self,nivel):
        self._niveles.append(nivel)
    
    def resultadoFinal (self):
        return sum(self.verRespuestas())
    
    def getNiveles(self):
        return self._niveles
    
    def nivelEnPosicion(self,pos):
        return self._niveles[pos]
    
    def crearNiveles(self,consignas):
        '''
        Se utiliza índices para armar de forma aleatoria las posibles respuestas que luego se usarán en el juego
        Válidas es una lista de las respuestas válidas en el juego, su índice indica cada nivel
        listaPregs es una lista de niveles [nivelActual][respuesta[indices]]
        nuevoNivel es de tipo Nivel y almacena los datos de la consigna del nivel correspondiente
        Se usa nuevoNivel para agregar a la lista de niveles del juego concreto
        retorna la lista de válidas. Se usará para evaluar las respuestas
        ''' 
        indices = [1,2,3,4]
        random.shuffle(indices)
        listaPregs = []
        validas = []
        preguntas = []
        for i in range(self.getTotalNiveles()):
            validas.append(consignas.consignaEnPosicion(i)['respuesta1'])
            preguntas.append(consignas.consignaEnPosicion(i)['pregunta'])
            preguntaNivel=[]
            for j in range(4):
                preguntaNivel.append(consignas.consignaEnPosicion(i)['respuesta' + str(indices[j])])
            listaPregs.append(preguntaNivel)
            random.shuffle(indices)

        for i in range(self.getTotalNiveles()):
            nuevoNivel = Nivel(consignas.consignaEnPosicion(i)['pregunta'],validas[i],listaPregs[i])
            self.agregarNivel(nuevoNivel.getRespuestasPosibles())
        return validas, preguntas