class JugadorBeta():
    def __init__(self,nombre):
        self._nombre = nombre
        self._puntaje = 0
        self._nivel = 0
    
    def getPuntaje (self):
        return self._puntaje
    
    def getNombre (self):
        return self._nombre
    
    def getNivel(self):
        return self._nivel
    
    def incrementarNivel (self):
        self._nivel += 1

    def sumarPuntaje (self,nuevoPuntaje):
        self._puntaje += nuevoPuntaje
    
    def restarPuntaje (self,nuevoPuntaje):
        self._puntaje -= nuevoPuntaje
    
