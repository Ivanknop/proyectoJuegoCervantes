"""
Esta clase modela un Nivel. Se conoce el rango de dificultad, la puntuación,
qué consigna posee y cuál es la respuesta válida. 
Los niveles son creados a partir de una base de datos que almacena las consignas.
No pueden modificarse los atributos
"""
class Nivel():

    def __init__(self, dificultad, puntaje, consigna,respuestaValida):
        self.__dificultad = dificultad
        self.__puntaje = puntaje
        self.__consigna = consigna
        self.__respuestaValida = respuestaValida
    
    def getDificultad(self):
        return self.__dificultad

    def getPuntaje(self):
        return self.__puntaje

    def getConsigna(self):
        return self.__consigna

    def getRespuestaValida (self):
        return self.__respuestaValida

    def evaluarRespuesta (self,respuesta):
        if (respuesta == self.getRespuestaValida()):
            return self.getPuntaje()
        else: return 0

nuevoNivel = Nivel ('fácil',10,'¿cómo te llamás?','ivan')

print (nuevoNivel.evaluarRespuesta('ivan'))
