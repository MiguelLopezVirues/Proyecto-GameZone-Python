import random
import sys
from .recursos.piedra_papel_tijera_recursos import figures_ascii_art, welcome_banner
import pyfiglet
from colorama import Fore, Style, init
import os
class Piedra_papel_tijera:
    """
    Clase que implementa el juego de 'Piedra, papel, tijeras, lagarto, Spock'.

    Atributos:
    ----------
    interacciones_lucha_texto : dict
        Diccionario que define las interacciones y resultados de las luchas entre los distintos personajes.
        Las claves son los nombres de los luchadores, y los valores son subdiccionarios que indican qué luchador derrota a otro, junto con el mensaje correspondiente.
    rondas : int
        Número de rondas en la partida. El valor por defecto es 3.
    puntuacion_jugador : int
        Puntuación actual del jugador. El valor por defecto es 0.
    puntuacion_maquina : int
        Puntuación actual de la máquina. El valor por defecto es 0.
    
    Métodos:
    --------
    __init__() -> None:
        Inicializa el juego con las interacciones de lucha y restablece las puntuaciones y rondas.

    welcome() -> None:
        Muestra un mensaje de bienvenida utilizando arte ASCII.

    jugar() -> None:
        Ejecuta la lógica del juego. Define las rondas, controla las puntuaciones y determina el ganador de la partida.
    
    definir_rondas() -> None:
        Permite al jugador definir el número de rondas que se jugarán. Si el valor ingresado no es válido, lo solicita nuevamente.

    elegir_luchador() -> None:
        Permite al jugador seleccionar un luchador y genera aleatoriamente la elección de la máquina. 
        También muestra la representación visual de ambos luchadores.

    comprobar_ganador_ronda() -> None:
        Comprueba quién ha ganado la ronda basándose en las interacciones predefinidas entre los luchadores y actualiza las puntuaciones.
        Imprime el resultado de la ronda.

    limpiar_pantalla() -> None:
        Limpia la pantalla de la consola para facilitar la visualización durante el juego.

    reset() -> None:
        Permite al jugador reiniciar el juego desde el principio o terminar la partida. Restablece las variables del juego si el jugador elige continuar.
    """

    def __init__(self) -> None:
        """
        Inicializa los atributos del juego. Define las interacciones entre los luchadores, el número de rondas, y las puntuaciones iniciales del jugador y la máquina.
        """
        self.interacciones_lucha_texto = {
                "piedra": {
                    "tijeras": "¡piedra aplasta tijeras!",
                    "lagarto": "¡piedra aplasta lagarto!"
                },
                "papel": {
                    "piedra": "¡papel cubre piedra!",
                    "spock": "¡papel refuta a Spock!"
                },
                "tijeras": {
                    "papel": "¡tijeras corta papel!",
                    "lagarto": "¡tijeras decapita lagarto!"
                },
                "lagarto": {
                    "spock": "¡lagarto envenena a Spock!",
                    "papel": "¡lagarto come papel!"
                },
                "spock": {
                    "tijeras": "¡Spock rompe tijeras!",
                    "piedra": "¡Spock vaporiza piedra!"
                }}

        self.rondas = 3
        self.puntuacion_jugador = 0
        self.puntuacion_maquina = 0

    def welcome(self):
        """
        Muestra un banner de bienvenida al juego.
        """
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("PIEDRA-PAPEL-TIJERA", font="rounded")
        print(Fore.BLUE + titulo)

    def jugar(self):
        """
        Inicia el ciclo principal del juego, donde el jugador y la máquina seleccionan sus luchadores.
        Tras cada ronda se comprueban los ganadores.
        La partida continúa hasta que un jugador alcanza el número de puntos necesarios para ganar.
        Al finalizar, se muestra un mensaje de victoria o derrota y se da la opción de reiniciar el juego.
        """
        self.definir_rondas()
        puntos_victoria = int(self.rondas / 2 + 1)
        while self.puntuacion_jugador < puntos_victoria and self.puntuacion_maquina < puntos_victoria:
            print(f"\nJugador vs. máquina: {self.puntuacion_jugador} - {self.puntuacion_maquina}")
            self.elegir_luchador()
            self.comprobar_ganador_ronda()
        
        if self.puntuacion_jugador >= puntos_victoria and self.puntuacion_maquina == 0:
            print("\n¡VICTORIA IMPECABLE! Eres el favorito de los dioses guerrero.")
        elif self.puntuacion_jugador >= puntos_victoria:
            print("\n¡VICTORIA! Tus maestros están orgullosos.")
        else:
            print("\nHas luchado con honor... pero has fracasado.")

        self.reset()

    def definir_rondas(self):
        """
        Permite al jugador definir cuántas rondas desea jugar. Si el valor ingresado no es un número válido, 
        se solicita al jugador que lo introduzca nuevamente.
        """
        try:
            self.rondas = int(input("\n¿Al mejor de cuántas rondas quieres jugar?"))
        except ValueError:
            print("\nDebes introducir un número válido. Inténtalo de nuevo.")
            self.definir_rondas()

    def elegir_luchador(self):
        """
        Permite al jugador elegir su luchador y selecciona aleatoriamente un luchador para la máquina.
        Si el jugador introduce un valor incorrecto, se le solicita que elija nuevamente.
        También imprime la representación visual de ambos luchadores.
        """
        self.luchador_jugador = input("\nElige a tu luchador introduciendo su nombre:\n- piedra\n- papel\n- tijeras\n- lagarto\n- spock\n").lower()
        try:
            self.interacciones_lucha_texto[self.luchador_jugador]
        except KeyError:
            print("\nHas introducido un valor incorrecto para el luchador. Inténtalo de nuevo.")
            self.elegir_luchador()
        self.luchador_maquina = random.choice(list(self.interacciones_lucha_texto.keys()))

        print(f"\nHas elegido: {self.luchador_jugador.title()}. La máquina ha elegido: {self.luchador_maquina}.")
        print(f"{figures_ascii_art[self.luchador_jugador]}\n\n     VS.    \n\n{figures_ascii_art[self.luchador_maquina]}")

    def comprobar_ganador_ronda(self):
        """
        Verifica el resultado de la ronda actual, comparando los luchadores del jugador y de la máquina.
        Actualiza las puntuaciones según el resultado de la ronda (ganar, perder o empatar).
        """
        if self.luchador_jugador == self.luchador_maquina:
            print("\n¡Ha habido un empate!")
        elif self.luchador_maquina in self.interacciones_lucha_texto[self.luchador_jugador]:
            print(f"\n{self.interacciones_lucha_texto[self.luchador_jugador][self.luchador_maquina]}. Ganas esta ronda, eres un luchador feroz... ")
            self.puntuacion_jugador += 1
        else:
            print(f"\n{self.interacciones_lucha_texto[self.luchador_maquina][self.luchador_jugador]}. Pierdes esta ronda, te falta entrenamiento... ")
            self.puntuacion_maquina += 1

    def limpiar_pantalla(self):
        """
        Limpia la pantalla de la consola para hacer más fácil la visualización.
        Funciona tanto en sistemas Windows como en Unix.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def reset(self):
        """
        Pregunta al jugador si desea reiniciar el juego. Si elige continuar, reinicia las variables del juego; 
        si no, termina el programa con un mensaje de despedida.
        """
        seguir_jugando = input("\n¿Deseas volver a jugar? [Y/N]\n")
        if seguir_jugando.upper()[0] == "Y":
            self.__init__()
            self.jugar()
        else:
            print("\n¡Ha sido un placer!\n")
