class Nivel():

    def __init__(self, id, dificultad, puntaje, consigna,respuestaValida):
        self.__id = id
        self.__dificultad = dificultad
        self.__puntaje = puntaje
        self.__consigna = consigna
        self.__respuestaValida = respuestaValida
        self.__correcta = False
    
    def getId(self):
        return self.__id
    
    def getDificultad(self):
        return self.__dificultad

    def getPuntaje(self):
        return self.__puntaje

    def getConsigna(self):
        return self.__consigna

    def getCorrecta(self):
        return self.__correcta

    def getRespuestaValida (self):
        return self.__respuestaValida
    
    def __setCorrecta(self): #Método privado
        self.__correcta = not self.__correcta

    def evaluarRespuesta (self,respuesta):
        if (respuesta == self.getRespuestaValida()):
            self.__setCorrecta()
        return self.getCorrecta()

nuevoNivel = Nivel (1,'fácil',10,'patito','patote')

print (nuevoNivel.evaluarRespuesta('patoite'))
print (nuevoNivel.getCorrecta())
