class Jugador():
    def __init__(self, nombre, puntaje = 0, respuestas = [False, False, False, False, False]):
        self.__nombre = nombre
        self.__puntuacion = puntaje
        self.__respuestas= respuestas 
        self.__nivel = 1

    def __str__(self):
        return f"{self.__nombre} - {self.__puntuacion}- {self.__respuestas}"
    def infoJugador(self):
        return f"{self.__nombre}   -   {self.__puntuacion} - {self.__respuestas}"

    def getNombre(self):
        return self.__nombre
    
    def getNivel(self):
        return self.__nivel
    
    def incrementarNivel(self):
        self.__nivel +=1
    
    def getPuntaje(self):
        return self.__puntuacion

    def getRespuestas(self):
        return self.__respuestas

    def responder (self, posicion, ok):
        self.__respuestas[posicion]= ok
      
    def cantrespuestas(self):
        return sum(self.__respuestas)

lista = list(range(4))
print (lista)