"""
Esta clase modela un Nivel. Se conoce el rango de dificultad, la puntuación,
qué consigna posee y cuál es la respuesta válida. 
Los niveles son creados a partir de una base de datos que almacena las consignas.
No pueden modificarse los atributos
"""
class Nivel():

    def __init__(self, nivel, pregunta,respuestaValida,respuestasIncorrectas):
        self.__nroNivel = nivel
        self.__puntaje = 50
        self.__pregunta = pregunta
        self.__respuestaValida = respuestaValida
        self.__respuestasIncorrectas = respuestasIncorrectas
    
    def getDificultad(self):
        return self.__dificultad

    def getPuntaje(self):
        return self.__puntaje
    
    def getNivel(self):
        return self.__nroNivel

    def getPregunta(self):
        return self.__pregunta

    def getRespuestaValida (self):
        return self.__respuestaValida
    
    def getRespuestasIncorrectas(self):
        return self.__respuestasIncorrectas

    def evaluarRespuesta (self,respuesta):
        if (respuesta == self.getRespuestaValida()):
            return self.getPuntaje()
        else: return 0

#nuevoNivel = Nivel ('fácil',10,'¿cómo te llamás?','ivan')

#print (nuevoNivel.evaluarRespuesta('ivan'))
