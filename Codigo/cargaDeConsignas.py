import pickle
import os

class AlmacenamientoConsignas():
    '''
    Almacena en un .pckl las consignas que se agregan.
    Resta organizarlas por nivel de dificultad
    '''
    rutaGuardado = os.path.join ("guardados","consignas.pckl")

    def __init__(self):
        self.preguntas = []

    def crearArchivo (self):
        fichero = open (self.rutaGuardado, 'wb')
        fichero.close()
    
    def agregarConsigna (self,pregunta,respuesta):
        self.preguntas.append ({'pregunta':pregunta,'respuesta':respuesta})
        self.guardar()
    
    def guardar(self):
        fichero = open(self.rutaGuardado, 'wb')
        pickle.dump(self.preguntas, fichero)
        fichero.close()

    def cargar(self):
        try:
            fichero = open(self.rutaGuardado, 'rb')
            self.preguntas = pickle.load(fichero)
            for e in self.preguntas:
                print (e)
            fichero.close()
        except:
            self.crearArchivo()
    
pregunta = ''
respuesta = ''
nivelInicial = []
seguir = ''
ok = True
archivo = AlmacenamientoConsignas()
archivo.cargar()
'''
while ok:
    pregunta=    input ('Ingrese una consigna: ')
    respuesta = input ('Ingrese la respuesta correcta: ')
    archivo.agregarConsigna(pregunta,respuesta)
    seguir = input ('¿continuar? ')
    if (seguir != 's'):
        ok = not ok
'''