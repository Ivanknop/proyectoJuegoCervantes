import PySimpleGUI as sg
import random
from nivel import *
from tema import *
import pickle
from cargaDeConsignas import *
from nivelesEnJuego import *
from Jugador import *
from Bonus import *

class InterfazJuego ():
    '''Define la interfaz en la que se desarrolla la dinámica del juego
    consignas es una matriz de niveles y respuestas por nivel. Jugador es clase Jugador
    El resto son imágenes.
    '''
    def __init__(self, imgBoton,bonusTime,quijote,jugador,consignas):
        self._jugador = jugador
        self._consignas = consignas #ahora es una matriz
        self._imagenBoton = imgBoton
        self._imagenBonusTime = bonusTime
        self._logo = quijote
    
    def getJugador (self):
        return self._jugador

    def getInterfaz(self):
        return self.interfazJuego()
    
    def getConsignas(self):
        return self._consignas

    def getBoton (self):
        return self._imagenBoton
    
    def getBonusTimeImg (self):
        return self._imagenBonusTime
    
    def getLogo (self):
        return self._logo

    def crearBotones(self,nivel):
        '''
        Crea botones con key 0,1,2,3 que se usará para ubicar la respuesta seleccionada en cada nivel.
        '''
        botones = []
        for i in range(4):
            botones.append(sg.Button(nivel[i],image_filename=self.getBoton(),key=str(i)))
        random.shuffle(botones)
        return botones

    def interfazJuego(self):
        '''
        nivelActual almacena el nivel en Juego. Es para mejor lectura.
        jugador almacena al jugador en juego. Idem
        Crea las columnas que serán usadas para crear la interfaz
        colPregunta contiene los botones que sirven de respuesta a la pregunta principal. Utiliza el nivelActual
        para guiarse en la matriz de nivelesEnJuego
        '''
        nivelActual = self.getJugador().getNivel()
        jugador = self.getJugador()
        titulo = 'JUEGO DE PREGUNTAS SOBRE "EL QUIJOTE"'
        colJugador = [
            [sg.Text('JUGADOR '+ jugador.getNombre().upper(),key='jugNombre'),sg.Text('Puntaje: '+str(jugador.getPuntaje()),size=(10,2)   ,key='jugPje')],
            [sg.Button('BONUS 1',size=(10,2),key='bonus1'),sg.Button('',image_filename=self.getBonusTimeImg(),button_color=('black','#FF1133'),tooltip='MÁS TIEMPO',key='bonusTime')]            
        ]
        colSuperior=[
            [sg.Image(filename=self.getLogo(),size=(300,50)),
            sg.Button('MENÚ',key='menu'),sg.Button('volver',key='volver')]
        ]
        colPregunta =  [
            [sg.Text('NIVEL'+str(nivelActual),key='nivel')], 
            self.crearBotones(self.getConsignas()[nivelActual]) 
            ]
        layout = [
            [sg.Column(colSuperior,justification='center',key='colSup')],
            [sg.Column(colPregunta,justification='center',key='colPreg')],
            [sg.Column(colJugador,justification='center',key='colJug')]
            ]
        
        return layout
    
    def actualizarPuntaje (self,ven):
        ven['jugPje'].Update('Puntaje: '+str(self.getJugador().getPuntaje()))

    def actualizarBotones (self,ven):        
        for i in range(4):
            ven[str(i)].Update(self.getConsignas()[self.getJugador().getNivel()][i])

    def pasarNivel(self,ven,niveles,ok):
        '''
        si OK = True, habilita el nivelCorrecto del nivel en juego; si no, el incorrecto.
        jugador incrementa su nivel
        se actualizan las respuestas mostradas en los botones
        se actualiza el puntaje en pantalla
        '''
        if ok:
            puntos = 30
        else:
            puntos = -10
        niveles.puntuarNivel(self.getJugador().getNivel()-1,puntos)
        self.getJugador().sumarPuntaje(puntos)      
        self.getJugador().incrementarNivel()
        self.actualizarBotones(ven)
        self.actualizarPuntaje(ven)

    def evaluarRespuesta(self,respuestaJugador,valida):
        '''
        recibe una respuesta del jugador y la compara con la respuesta válida
        '''
        #print (respuestaJugador)
        #print (valida)
        #print (valida == respuestaJugador)
        return valida == respuestaJugador


def inicio(jugador,consignas):
    tema()
    bonusTime =os.path.join('multimedia','relojChico.png')  
    alto = 400
    ancho = 700
    imgBoton = os.path.join('multimedia','cuadro.png')  
    quijote= os.path.join('multimedia','quijoteLogo2.png')
    
    totalNiveles=5
    nivelActual = jugador.getNivel()
    nivelesJugados = NivelesEnJuego(totalNiveles)    
    validas = nivelesJugados.crearNiveles(consignas)
    interfaz = InterfazJuego (imgBoton,bonusTime,quijote,jugador,nivelesJugados.getNiveles())

    ventana = sg.Window ('Juego Cervantes: Inicio',interfaz.getInterfaz(), size = (ancho,alto),element_justification='center')
    ventana.Finalize()
    while True:
        evento, valor = ventana.read()
        if (evento == None):
            break
        
        if (evento == 'volver'):
            ok = sg.popup_ok_cancel('¿Realmente desea salir? Si lo hace perderá la puntuación actual')
            if ok=='OK':
                break
        
        if (evento in ['0','1','2','3']):
            print('NIVEL ACTUAL: '+ str(nivelActual))
            #Envía la lista de preguntas en la posición nivel Actual/Evento y la respuesta válida
            ok = interfaz.evaluarRespuesta(nivelesJugados.getNiveles()[nivelActual][int(evento)],validas[nivelActual])

            interfaz.pasarNivel(ventana,nivelesJugados,ok)
            nivelActual +=1
            print (nivelesJugados.verRespuestas())
        if (totalNiveles == nivelActual+1):
            sg.popup('Terminó \n RESULTADO FINAL: '+str(nivelesJugados.resultadoFinal()))
            
            break


    ventana.Close()