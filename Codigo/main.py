from interfazPrincipal import principal
from interfazJuego import inicio
import random

def main():

    while True:
        try:
            jugador, consignas = principal()
            juego = inicio(jugador,consignas)
        except:
            break
        
if __name__ == '__main__':
    main()

