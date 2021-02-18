class Jugador():
    def __init__(self, nombre, puntaje = 0, respuestas = [False, False, False, False, False]):
        self.__nombre = nombre
        self.__puntuacion = puntaje
        self.__respuestas= respuestas 

    def __str__(self):
        return f"{self.__nombre} - {self.__puntuacion}- {self.__respuestas}"
    def infoJugador(self):
        return f"{self.__nombre}   -   {self.__puntuacion} - {self.__respuestas}"

    def getNombre(self):
        return self.__nombre
    
    def getPuntaje(self):
        return self.__puntuacion

    def getRespuestas(self):
        return self.__respuestas

    def responder (self, posicion, ok):
        self.__respuestas[posicion]= ok
      
    def cantrespuestas(self):
        return sum(self.__respuestas)


jug=Jugador("Nico")
print(jug.infoJugador())
jug.responder(2,True)
print(jug.infoJugador())     
print(jug.cantrespuestas())
