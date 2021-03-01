import PySimpleGUI as sg
import random
from nivel import *
from tema import *
import pickle
from cargaDeConsignas import *
from nivelesEnJuego import *
from Jugador import *

class InterfazJuego ():
    '''Mega clase'''
    def __init__(self, imgBoton,jugador,consignas):
        self._jugador = jugador
        self._consignas = consignas
        self._imagenBoton = imgBoton
    
    def getJugador (self):
        return self._jugador

    def getInterfaz(self):
        return self.interfazJuego()
    
    def getConsignas(self):
        return self._consignas

    def getBoton (self):
        return self._imagenBoton

    def nuevaPregunta (self):
        nivelActual = self.getJugador().getNivel()
        botonesPreguntas = self.crearBotones(self.getConsignas().consignaEnPosicion(nivelActual))   
        
        colPregunta =  [
            [sg.Text('NIVEL'+str(nivelActual),key='nivel')],
            [sg.Text(self.getConsignas().consignaEnPosicion(0)['pregunta'],key='nroPregunta')],
            botonesPreguntas                  
        ]

        nuevaPregunta = [sg.Column(colPregunta,justification='center',visible=True,key='colPreg')]
        return nuevaPregunta

    def interfazJuego(self):
        nivelActual = self.getJugador().getNivel()
        jugador = self.getJugador()
        titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
        colJugador = [
            [sg.Text('JUGADOR '+ jugador.getNombre().upper(),key='jugNombre'),sg.Text('Puntaje: '+str(jugador.getPuntaje()),size=(10,2)   ,key='jugPje')],
            [sg.Button('BONUS 1',key='bonus1'),sg.Button('BONUS 2',key='bonus1')]            
        ]
        colSuperior=[
            [sg.Text(titulo,font='Italic 16'),
            sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver')]
        ]
        layout = [
            [sg.Column(colSuperior,justification='center',key='colSup')],
            self.nuevaPregunta(),
            [sg.Column(colJugador,justification='center',key='colJug')]
            ]
        
        return layout

    def crearBotones(self,c):
        botones = []
        for i in range(4):
            botones.append(sg.Button(c['respuesta'+str(i+1)],image_filename=self.getBoton(),key=str(i)))
        random.shuffle(botones)
        return botones
    
    def actualizarPuntaje (self,ven):
        ven['jugPje'].Update('Puntaje: '+str(self.getJugador().getPuntaje()))

    def pasarNivel(self,ven,niveles,ok):
        nivelActual = self.getJugador().getNivel()
        if ok:
            niveles.nivelCorrecto(nivelActual-1,30)
            self.getJugador().sumarPuntaje(30)
        else:
            niveles.nivelIncorrecto(nivelActual-1)
            self.getJugador().sumarPuntaje(-10)        
        self.getJugador().incrementarNivel()
        ven['nivel'].Update('NIVEL'+str(nivelActual))
        ven['nroPregunta'].Update(self.getConsignas().consignaEnPosicion(nivelActual)['pregunta'])
        indices = [0,1,2,3]
        random.shuffle(indices)
        for i in range(4):
            ven[str(indices[i])].Update(self.getConsignas().consignaEnPosicion(nivelActual)['respuesta'+str(indices[i]+1)])

        self.actualizarPuntaje(ven)

    def evaluarRespuesta(self,ven,e,p,ok):
        if (p[int(e)] == ok):
            return True
        else:
            return False

def inicio(jugador,consignas):
    tema()
    alto = 500
    ancho = 700
    imgBoton = os.path.join('multimedia','cuadro.png')  
    interfaz = InterfazJuego (imgBoton,jugador,consignas)
    totalNiveles=5
    nivelActual = 0
    '''
    LO QUE SIGUE A CONTINUACION ES PRUEBA
    validas = [consignas.consignaEnPosicion(0)['respuesta1'],
    consignas.consignaEnPosicion(1)['respuesta1'],
    consignas.consignaEnPosicion(2)['respuesta1'],
    consignas.consignaEnPosicion(3)['respuesta1'],
    consignas.consignaEnPosicion(4)['respuesta1']]
    

    preg1 = [consignas.consignaEnPosicion(0)['respuesta1'],consignas.consignaEnPosicion(0)['respuesta2'],
    consignas.consignaEnPosicion(0)['respuesta3'],consignas.consignaEnPosicion(0)['respuesta4']]
    preg2 = [consignas.consignaEnPosicion(1)['respuesta1'],consignas.consignaEnPosicion(1)['respuesta2'],
    consignas.consignaEnPosicion(1)['respuesta3'],consignas.consignaEnPosicion(1)['respuesta4']]
    preg3 = [consignas.consignaEnPosicion(2)['respuesta1'],consignas.consignaEnPosicion(2)['respuesta2'],
    consignas.consignaEnPosicion(2)['respuesta3'],consignas.consignaEnPosicion(2)['respuesta4']]
    preg4 = [consignas.consignaEnPosicion(3)['respuesta1'],consignas.consignaEnPosicion(3)['respuesta2'],
    consignas.consignaEnPosicion(3)['respuesta3'],consignas.consignaEnPosicion(3)['respuesta4']]
    preg5 = [consignas.consignaEnPosicion(4)['respuesta1'],consignas.consignaEnPosicion(4)['respuesta2'],
    consignas.consignaEnPosicion(4)['respuesta3'],consignas.consignaEnPosicion(4)['respuesta4']]

    listaPregs = [preg1,preg2,preg3,preg4,preg5]
    '''
    nivelesJugados = NivelesEnJuego(totalNiveles)
    ventana = sg.Window ('Juego Cervantes: Inicio',interfaz.getInterfaz(), size = (ancho,alto),element_justification='center')
    ventana.Finalize()
    while True:
        evento, valor = ventana.read()
        if (evento == None):
            break
        
        if (evento == 'volver'):
            ok = aviso('¿Realmente desea salir? Si lo hace perderá la puntuación actual',['sí','no'])
            if ok=='_sí':
                break
        
        if (evento in ['0','1','2','3']):
            #print (preg1)
            print('NIVEL ACTUAL: '+ str(interfaz.getJugador().getNivel()))
            if (evento =='0'):
                interfaz.pasarNivel(ventana,nivelesJugados,True)
            else:
                interfaz.pasarNivel(ventana,nivelesJugados,False)
            nivelActual +=1
        if (totalNiveles == nivelActual):
            sg.popup('Terminó \n RESULTADO FINAL: '+str(nivelesJugados.resultadoFinal()))
            
            break
        '''
        if (evento in ['0','1','2','3']):
            #if (interfaz.evaluarRespuesta(ventana,evento,listaPregs[nivelActual],validas[nivelActual])):
            interfaz.pasarNivel(ventana,True)
                #print (validas[nivelActual])
                #print (listaPregs[nivelActual][int(evento)])
            nivelActual +=1
            #else:
                #print ('Error')
        '''

    ventana.Close()