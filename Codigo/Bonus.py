class BonusTime():
    def __init__(self,habilitado):
        self.habilitado= habilitado

    def getHabilitado(self):
        return self.habilitado
    def desHabilitar(self):
        self.habilitado = False

    def usarBonus(self):
        self.desHabilitar()
        return self.getHabilitado()

'''
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