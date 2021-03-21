class Jugador():
    def __init__(self, nombre, puntaje = 0, respuestas = [False, False, False, False, False]):
        
        self._nombre = nombre
        self._puntuacion = puntaje
        self._respuestas= respuestas 
        self._nivel = 0

    def __str__(self):
        return f"{self._nombre} - {self._puntuacion}- {self._respuestas}"
    def infoJugador(self):
        return f"{self._nombre}   -   {self._puntuacion} - {self._respuestas}"

    def getNombre(self):
        return self._nombre
    
    def getNivel(self):
        return self._nivel
    
    def incrementarNivel(self):
        self._nivel +=1
    
    def getPuntaje(self):
        return self._puntuacion
    
    def sumarPuntaje(self,puntos):
        self._puntuacion +=puntos

    def getRespuestas(self):
        return self._respuestas

    def responder (self, posicion, ok):
        self._respuestas[posicion]= ok
      
    def cantrespuestas(self):
        return sum(self._respuestas)
