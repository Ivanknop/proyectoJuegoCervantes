import PySimpleGUI as sg
import random
from tema import tema
import pickle
from nivelesEnJuego import *
from Jugador import Jugador
from Bonus import BonusTime
import time
from timer import *
from Bonus import *
from ayuda import explicacionAyuda
from crearPdf import crearPdf

class InterfazJuego ():
    '''Define la interfaz en la que se desarrolla la dinámica del juego
    consignas es una matriz de niveles y respuestas por nivel. 
    :param jugador: Objeto Jugador que contiene la configuración del mismo
    :param consignas: Objeto que contiene las consignas que se usarán en la partida
    :param imagenes: una lista de todas las imágenes en juego
    '''
    def __init__(self, jugador,consignas,preguntas,imagenes=[]):
        self._jugador = jugador
        self._consignas = consignas
        self._logo = imagenes[0]
        self._imagenBoton = imagenes[1]
        self._imagenBonusTime = imagenes[2]
        self._imagenesNivelesJugados = [imagenes[3],imagenes[4],imagenes[5]]
        self._tiempoInicio = 0
        self._tiempoFinal = 0   
        self.bonusTiempo = BonusTime(True)
        self._preguntas = preguntas

    def getBonusTime(self):
        return self.bonusTiempo
    def getJugador (self):
        return self._jugador
    def getInterfaz(self):
        return self.interfazJuego()
    def getConsignas(self):
        return self._consignas
    def getPreguntas(self):
        return self._preguntas
    def getBoton (self):
        return self._imagenBoton
    def getBonusTimeImg (self):
        return self._imagenBonusTime
    def getLogo (self):
        return self._logo
    def getImagenesNivelesJugando (self,pos):
        return self._imagenesNivelesJugados[pos]
    def getTiempoFinal(self):
        return self._tiempoFinal
    def getTiempoInicial(self):
        return self._tiempoInicio
        
    def setTiempoFinal(self,nuevoTiempo):
        self._tiempoFinal = nuevoTiempo
    def setTiempoInicio(self,nuevoTiempo):
        self._tiempoInicio = nuevoTiempo

    def setTimer(self,minutos):
        self.setTiempoInicio(time.time())
        self.setTiempoFinal(self.getTiempoInicial() + minutos*60)
    
    def terminoTimer(self):
        return time.time() > self.getTiempoFinal()
    
    def desHabilitarBonus(self,ven,bonus):
        ven[bonus].update(visible=False)
    
    def crearBotones(self,nivel):
        '''
        Crea botones con key 0,1,2,3 que se usará para ubicar la respuesta seleccionada en cada nivel.
        '''
        botones = []
        for i in range(4):
            botones.append(sg.Button(nivel[i],image_filename=self.getBoton(),font='MedievalSharp 10',key=str(i)))
        random.shuffle(botones)
        return botones

    def crearImagenesNiveles(self,totNiveles = 5):
        imgNiveles = [sg.Text('NIVELES => ',font='MedievalSharp 15',tooltip='Gris = Sin jugar / Rojo = Mal / Azul = Bien',key='txtNiveles')]
        for i in range(totNiveles):
            imgNiveles.append(sg.Image(filename=self.getImagenesNivelesJugando(0),tooltip='Nivel '+str(i+1),size=(30,30),key='imagen'+str(i)))
        return imgNiveles
    
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
        colJugador = [
            [sg.Text('JUGADOR => '+ jugador.getNombre().upper(),font='MedievalSharp 15',auto_size_text=True,key='jugNombre')],
            [sg.Text('Puntaje => '+str(jugador.getPuntaje()),font='MedievalSharp 20',size=(10,1),key='jugPje')],
            self.crearImagenesNiveles(),
            [sg.Text('BONUS DE TIEMPO => ',font='MedievalSharp 12',key='txtBonusTiempo'),
            sg.Button('',image_filename=self.getBonusTimeImg(),button_color=('black','#FFAAFF'),tooltip='MÁS TIEMPO',key='bonusTime')]            
        ]
        colSuperior=[
            [sg.Image(filename=self.getLogo(),size=(300,50)),
            sg.Button('AYUDA',font='MedievalSharp 10',key='ayuda'),sg.Button('SALIR',font='MedievalSharp 10',key='volver')],
            
        ]
        colPregunta =  [
            [sg.Text('NIVEL '+str(nivelActual+1),font='MedievalSharp 20',key='nivel'),
            sg.Text('Tiempo Jugado: ',font='MedievalSharp 10',key='a'),
            sg.Text('00:00',font='MedievalSharp 20',key='timer')],
            [sg.Text('PREGUNTA => ',font='MedievalSharp 20',key='txtPregunta'),
            sg.Text(self.getPreguntas()[nivelActual],key='cambiarPreg')], 
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
    
    def actualizarTimer(self,ven,cont):
        ven['timer'].update('{:02d}:{:02d}'.format((cont // 100) // 60,(cont // 100) % 60))

    def actualizarBotones (self,ven):        
        for i in range(4):
            ven[str(i)].Update(self.getConsignas()[self.getJugador().getNivel()][i])

    def actualizarImagenesNiveles(self,ven,nivel,ok):
        if ok:
            ven['imagen'+str(nivel)].Update(self.getImagenesNivelesJugando(1))
        else:
            ven['imagen'+str(nivel)].Update(self.getImagenesNivelesJugando(2))

    def actualizarPreguntas(self,ven):
        ven['cambiarPreg'].Update(self.getPreguntas()[self.getJugador().getNivel()])

    def pasarNivel(self,ven,niveles,ok,reloj):
        '''
        si OK = True, habilita el nivelCorrecto del nivel en juego; si no, el incorrecto.
        jugador incrementa su nivel
        se actualizan las respuestas mostradas en los botones
        se actualiza el puntaje en pantalla
        '''
        if ok:
            puntos = 60-reloj.getContadorTiempo()//100
            
        else:
            puntos = -((60-reloj.getContadorTiempo()//100)//5)
        niveles.puntuarNivel(self.getJugador().getNivel()-1,puntos)
        self.actualizarImagenesNiveles(ven,self.getJugador().getNivel(),ok)
        self.getJugador().sumarPuntaje(puntos)      
        self.getJugador().incrementarNivel()
        self.actualizarBotones(ven)
        self.actualizarPuntaje(ven)
        self.actualizarPreguntas(ven)
        self.setTimer(1)
        self.actualizarTimer(ven,reloj.getContadorTiempo())

    def evaluarRespuesta(self,respuestaJugador,valida):
        '''
        recibe una respuesta del jugador y la compara con la respuesta válida
        '''
        sg.popup('La respuesta escogida '+str(respuestaJugador) + 'es '+ str(valida == respuestaJugador),font='MedievalSharp 10')
        return valida == respuestaJugador


def inicio(jugador,consignas):
    tema()
    imgBonusTime =os.path.join('multimedia','relojChico.png')  
    alto = 450
    ancho = 800
    imgBoton = os.path.join('multimedia','cuadro.png')  
    quijote= os.path.join('multimedia','quijoteLogo2.png')
    imgSinJugar = os.path.join('multimedia','sinJugar.png')
    imgCorrecto = os.path.join('multimedia','correctos.png')
    imgIncorrecto = os.path.join('multimedia','errores.png')

    listaImagenes = [quijote,imgBoton,imgBonusTime,imgSinJugar,imgCorrecto,imgIncorrecto]

    totalNiveles=5
    nivelActual = jugador.getNivel()
    nivelesJugados = NivelesEnJuego(totalNiveles)    
    validas, preguntas = nivelesJugados.crearNiveles(consignas)

    respuestasDelJugador = []

    interfaz = InterfazJuego (jugador,nivelesJugados.getNiveles(),preguntas,listaImagenes)


    ventana = sg.Window ('Juego Cervantes: Inicio',interfaz.getInterfaz(), size = (ancho,alto),element_justification='center')
    ventana.Finalize()
    interfaz.setTimer(1)
    reloj = Reloj()
    pausado = False
    while True:
        if not pausado:
            evento,valor = ventana.read(timeout=10)
            reloj.actualizarContadorTiempo()
        else:
            evento, valor = ventana.read()
        interfaz.actualizarTimer(ventana,reloj.getContadorTiempo())
        if (interfaz.terminoTimer()):
            ok = sg.popup_ok ('Se terminó el tiempo para este nivel',font='MedievalSharp 10')
            if ok:
                reloj.resetTiempo()
            nivelActual += 1
            interfaz.pasarNivel(ventana,nivelesJugados,False,reloj)
   
        if (evento == None):
            break
        
        if (evento == 'volver'):
            ok = sg.popup_ok_cancel('¿Realmente desea salir? Si lo hace perderá la puntuación actual',font='MedievalSharp 10')
            if ok=='OK':
                break
        
        if (evento == 'ayuda'):
            explicacionAyuda('ivan')

        if (evento == 'bonusTime'):
            ok = sg.popup_ok_cancel ('¿Realmente desea utilizar el Bonus de Tiempo?',font='MedievalSharp 10')
            if (ok=='OK' and interfaz.getBonusTime().getHabilitado()==True):
                interfaz.getBonusTime().usarBonus()
                reloj.resetTiempo()
                interfaz.desHabilitarBonus(ventana,evento)

        if (evento in ['0','1','2','3']):
            #Envía la lista de preguntas en la posición nivel Actual/Evento y la respuesta válida
            ok = interfaz.evaluarRespuesta(nivelesJugados.getNiveles()[nivelActual][int(evento)],validas[nivelActual])

            respuestasDelJugador.append(nivelesJugados.getNiveles()[nivelActual][int(evento)])
            try:
                interfaz.pasarNivel(ventana,nivelesJugados,ok,reloj)
                nivelActual +=1
                reloj.resetTiempo()
            except: 
                textoRespuestas = []
                for i in range(5):
                    textoRespuestas.append ('Respuesta '+str(i+1)+':' + respuestasDelJugador[i])
                sg.popup('Terminó \n RESULTADO FINAL: '+str(nivelesJugados.resultadoFinal()),font='MedievalSharp 10')
                
                crearPdf(jugador.getNombre(),textoRespuestas,validas,nivelesJugados.resultadoFinal(),time.strftime('%d/%m/%y %H:%M:%S'))
                break

    ventana.Close()