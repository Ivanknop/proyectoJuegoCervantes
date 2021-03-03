import random
class Bonus():
    def __init__(self, habilitado=False):
        self.hahilitado=habilitado

    def usarBonus(self):
        pass
    
    def gethabilitado(self):
        return self.hahilitado

    def setHabilitados(self):
        self.hahilitado=not self.hahilitado

class Time(Bonus):
    def __init__(self):
        Bonus.__init__(self,True)
        self.time=60

    def gethabilitado(self):
        return super().gethabilitado()

    def usarBonus(self):
        super().setHabilitados()
        return super().gethabilitado()


class Answer(Bonus):
    def __init__(self):
        Bonus.__init__(self,True)
        

    def gethabilitado(self):
        return super().gethabilitado()

    def usarBonus(self,rIncorrectas):
        super().setHabilitados()
        return self.eliminar(rIncorrectas)

    def eliminar(self,respuestasIncorrectas):
        l= respuestasIncorrectas
        random.shuffle(l)
        l.pop()
        l.pop()
        return l
'''
unaLista=list(range(5))
a=Answer()
print(a.gethabilitado())
print(unaLista)
l=a.usarBonus(unaLista)
print(l)
print(a.gethabilitado())
'''