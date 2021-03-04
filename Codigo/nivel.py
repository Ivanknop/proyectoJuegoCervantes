"""
Esta clase modela un Nivel. Se conoce el rango de dificultad, la puntuación,
qué consigna posee y cuál es la respuesta válida. 
Los niveles son creados a partir de una base de datos que almacena las consignas.
No pueden modificarse los atributos
"""
class Nivel():

    def __init__(self, pregunta,respuestaValida,respuestasPosibles, nivel='fácil'):
        self._nroNivel = nivel
        self._puntaje = 50
        self._pregunta = pregunta
        self._respuestaValida = respuestaValida
        self._respuestasPosibles = respuestasPosibles
    
    def infoNivel(self):
        return  f"{self._pregunta} - {self._respuestaValida}- {self._respuestasPosibles}"

    def getDificultad(self):
        return self._dificultad

    def getPuntaje(self):
        return self._puntaje
    
    def getNivel(self):
        return self._nroNivel

    def getPregunta(self):
        return self._pregunta

    def getRespuestaValida (self):
        return self._respuestaValida
    
    def getRespuestasPosibles(self):
        return self._respuestasPosibles

    def evaluarRespuesta (self,respuesta):
        if (respuesta == self.getRespuestaValida()):
            return self.getPuntaje()
        else: return 0
