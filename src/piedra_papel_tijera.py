import random
import sys
from .recursos.piedra_papel_tijera_recursos import figures_ascii_art, welcome_banner
import pyfiglet
from colorama import Fore, Style, init
import os
class Piedra_papel_tijera():
    def __init__(self) -> None:
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
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("PIEDRA-PAPEL-TIJERA", font="rounded")
        print(Fore.BLUE + titulo)

    def jugar(self):
        self.definir_rondas()
        puntos_victoria = int(self.rondas/2 + 1)
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
        try:
            self.rondas = int(input("\n¿Al mejor de cuántas rondas quieres jugar?"))
        except ValueError:
            print("\nDebes introducir un número válido. Inténtalo de nuevo.")
            self.definir_rondas()

    def elegir_luchador(self):
        self.luchador_jugador = input("\nElige a tu luchador introduciendo su nombre:\n- rock\n- paper \n- scissors\n- lizard\n- Spock\n").lower()
        try:
            self.interacciones_lucha_texto[self.luchador_jugador]
        except:
            print("\nHas introducido un valor incorrecto para el luchador. Inténtalo de nuevo.")
            self.elegir_luchador()
        self.luchador_maquina = random.choice(list(self.interacciones_lucha_texto.keys()))

        print(f"\nHas elegido: {self.luchador_jugador.title()}. La máquina ha elegido: {self.luchador_maquina}.")
        print(f"{figures_ascii_art[self.luchador_jugador]}\n\n     VS.    \n\n{figures_ascii_art[self.luchador_maquina]}")

    def comprobar_ganador_ronda(self):
        if self.luchador_jugador == self.luchador_maquina:
            print("\n¡Ha habido un empate!")
        elif self.luchador_maquina in list(self.interacciones_lucha_texto[self.luchador_jugador].keys()):
            print(f"\n{self.interacciones_lucha_texto[self.luchador_jugador][self.luchador_maquina]}. Ganas esta ronda, eres un luchador feroz... ")
            self.puntuacion_jugador +=1
        else:
            print(f"\n{self.interacciones_lucha_texto[self.luchador_maquina][self.luchador_jugador]}. Pierdes esta ronda, te falta entrenamiento... ")
            self.puntuacion_maquina +=1

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def reset(self):
        seguir_jugando = input("\n¿Deseas volver a jugar? [Y/N]\n")
        if seguir_jugando.upper()[0] == "Y":
            self.__init__()
            self.jugar()
        else:
            print("\n¡Ha sido un placer!\n")
    

