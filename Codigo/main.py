from interfazPrincipal import principal
from interfazJuego import inicio
import random
from ayuda import explicacionJuego

def main():

    while True:
        try:
            jugador, consignas = principal()
            explicacionJuego((jugador.getNombre()))
            inicio(jugador,consignas)
        except:
            break
        
if __name__ == '__main__':
    main()

