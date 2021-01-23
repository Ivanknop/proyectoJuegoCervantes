import random

niveles = [1,2,3]
preguntasNivelUno = ['pregunta 1','pregunta 2','pregunta 3','pregunta 4']
preguntasNivelDos = ['pregunta 1','pregunta 2','pregunta 3','pregunta 4']
preguntasNivelTres = ['pregunta 1','pregunta 2','pregunta 3','pregunta 4']

random.shuffle(preguntasNivelDos)
print (preguntasNivelDos)


"""def evaluarConsigna (consigna,respuesta):
    if (respuesta.lower() == consigna):
        return True
    else:
        return False

print(evaluarConsigna('hola','HOLa'))
"""
def agregarNuevaPregunta (nivel,pregunta):
    nivel.append(pregunta)

agregarNuevaPregunta(preguntasNivelDos,'hola')
print (preguntasNivelDos)