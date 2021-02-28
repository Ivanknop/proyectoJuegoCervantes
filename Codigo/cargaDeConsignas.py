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
        self.cargar()

    def crearArchivo (self):
        fichero = open (self.rutaGuardado, 'wb')
        fichero.close()
    
    def agregarConsigna (self,pregunta,respuesta,mal1,mal2,mal3):
        self.preguntas.append ({'pregunta':pregunta,'respuesta1':respuesta,
        'respuesta2':mal1,'respuesta3':mal2,'respuesta4':mal3})
        self.__guardar()
    
    def __guardar(self):
        fichero = open(self.rutaGuardado, 'wb')
        pickle.dump(self.preguntas, fichero)
        fichero.close()

    def cargar(self):
        try:
            fichero = open(self.rutaGuardado, 'rb')
            self.preguntas = pickle.load(fichero)
            fichero.close()
        except:
            self.crearArchivo()
    
    def imprimirPreguntas (self):
        self.cargar()
        for e in self.preguntas:
            print(e)
    
    def buscarPregunta (self,pregunta):
        self.cargar()
        preg = {}
        for e in self.preguntas:
            if (e['pregunta']==pregunta):
                preg = e
                break
        return preg
    
    def consignaEnPosicion(self,pos):
        return self.preguntas[pos]

    def borrarPregunta (self,pos):
        self.cargar()
        self.preguntas.pop(pos)
        self.__guardar()

    def vaciarConsignas (self):
        self.cargar()
        self.preguntas=[]
        self.__guardar()

#pregunta = ''
#respuesta = ''
##nivelInicial = []
#seguir = ''
#ok = True
#archivo = AlmacenamientoConsignas()
#archivo.imprimirPreguntas()
#print (archivo.buscarPregunta('dos'))
#print(archivo.consignaEnPosicion(1))
#archivo.borrarPregunta(1)
#archivo.imprimirPreguntas()
'''
while ok:
    pregunta=    input ('Ingrese una consigna: ')
    respuesta = input ('Ingrese la respuesta correcta: ')
    archivo.agregarConsigna(pregunta,respuesta)
    seguir = input ('¿continuar? ')
    if (seguir != 's'):
        ok = not ok
'''