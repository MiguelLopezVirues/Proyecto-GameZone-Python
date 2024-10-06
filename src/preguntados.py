import random
import sys
from .recursos.preguntados_recursos import actualidad, ciencia, historia, cultura_general, entretenimiento, welcome_banner
import pyfiglet
from colorama import Fore, Style, init
import os

class Preguntados():
    """
    Representa el juego de preguntas y respuestas 'Preguntados', donde los jugadores deben responder correctamente
    preguntas de diferentes categorías para ganar puntos.

    Atributos:
    -----------
    rondas : list[int]
        Lista de rondas, representando cuántas rondas tendrá el juego.
    puntuacion : int
        Puntuación actual del jugador, que se incrementa con cada respuesta correcta.

    Métodos:
    --------
    __init__() -> None:
        Inicializa las rondas y la puntuación.

    welcome() -> None:
        Muestra un mensaje de bienvenida con el título del juego.

    jugar() -> None:
        Ejecuta el ciclo principal del juego, creando un conjunto de preguntas y corriendo todas las rondas.

    correr_rondas() -> None:
        Recorre cada ronda del juego, presentando la pregunta y las opciones de respuesta al jugador.

    responder_pregunta(p_partida: dict, respuestas_dict: dict) -> bool:
        Recibe la respuesta del jugador y verifica si es correcta. Retorna True si la respuesta es correcta, de lo
        contrario, retorna False.

    verificar_respuesta(pregunta: dict, respuesta: str) -> bool:
        Verifica si la respuesta seleccionada por el jugador es correcta en base a la pregunta.

    crear_set_preguntas() -> None:
        Genera un conjunto de preguntas a partir de varias categorías y lo baraja para presentar durante el juego.

    limpiar_pantalla() -> None:
        Limpia la pantalla en sistemas Windows o Unix.

    reset() -> None:
        Ofrece la opción de reiniciar el juego o finalizarlo.
    """

    def __init__(self) -> None:
        """
        Inicializa las rondas y la puntuación.
        Atributos:
        -----------
        rondas : list[int]
            Lista de rondas, representando cuántas rondas tendrá el juego.
        puntuacion : int
            Puntuación actual del jugador, que se incrementa con cada respuesta correcta.

        """
        self.rondas = [n for n in range(0,10)]
        self.puntuacion = 0

    def welcome(self):
        """
        Muestra un mensaje de bienvenida con el título del juego.
        """
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("PREGUNTADOS", font="starwars")
        print(Fore.RED + titulo)

    def jugar(self):
        """
        Ejecuta el ciclo principal del juego, creando un conjunto de preguntas y corriendo todas las rondas.
        Al finalizar, se muestra un mensaje de victoria o derrota y se da la opción de reiniciar el juego.
        """
        self.crear_set_preguntas()
        self.correr_rondas()
        if self.puntuacion == len(self.rondas):
            print("¡VICTORIA! Has ganado al juego de Preguntados.")
        self.reset()


    def correr_rondas(self) -> None:
        """
        Recorre cada ronda del juego, presentando la pregunta y las opciones de respuesta al jugador.
        Si el jugador comete un error antes de la última ronda, corta la partida.
        """
        for n_ronda, p_partida in enumerate(self.p_partida):
            print(f"""\n -----------------------------------------------\nRonda {n_ronda + 1}.\n""")
            print("Pregunta:", p_partida["pregunta"])
            respuestas = p_partida["incorrecta"]
            respuestas.append(p_partida["correcta"])
            random.shuffle(respuestas)
            respuestas_dict = {
                "A": respuestas[0],
                "B": respuestas[1],
                "C": respuestas[2],
                "D": respuestas[3]
            }
            for letra, respuesta in respuestas_dict.items():
                print(f"{letra}) {respuesta}")

            if self.responder_pregunta(p_partida, respuestas_dict) == False:
                break

    def responder_pregunta(self, p_partida: dict, respuestas_dict: dict) -> bool:
        """
        Recibe la respuesta del jugador y verifica si es correcta. Retorna True si la respuesta es correcta, de lo
        contrario, imprime un mensaje de derrota y retorna False.

        Parameters:
            p_partida (dict): Diccionario que contiene la pregunta actual y sus respuestas.
            respuestas_dict (dict): Diccionario de respuestas posibles con sus respectivas letras.

        Returns:
            bool: True si la respuesta es correcta, False si el jugador pierde.
        """
        respuesta_usuario = input("Introduce la letra que corresponde con tu respuesta:\n").upper()
        try:
            if self.verificar_respuesta(p_partida, respuestas_dict[respuesta_usuario]) == True:
                print("\n¡Correcto!")
                print("Puntuacion", self.puntuacion)
                self.puntuacion += 1
                return True
            else:
                print("\nOoooh ¡Has perdido!")
                return False
        except:
            print("\nLa respuesta que has introducido no es válida.")

    def verificar_respuesta(self, pregunta: dict, respuesta: str) -> bool:
        """
        Verifica si la respuesta seleccionada por el jugador es correcta en base a la pregunta.

        Parameters:
            pregunta (dict): Diccionario que contiene la pregunta y sus respuestas.
            respuesta (str): Respuesta seleccionada por el jugador.

        Returns:
            bool: True si la respuesta es correcta, False en caso contrario.
        """
        if respuesta == pregunta["correcta"]:
            self.puntuacion += 1
            return True
        else:
            return False

    def crear_set_preguntas(self) -> None:
        """Genera un conjunto de preguntas a partir de varias categorías y lo baraja para presentar durante el juego."""
        categorias = [actualidad, ciencia, historia, cultura_general, entretenimiento]
        self.p_partida = list()
        for categoria in categorias * int(len(self.rondas) / len(categorias)):
            self.p_partida.append(random.choice(categoria))

        random.shuffle(self.p_partida)
        return

    def limpiar_pantalla(self) -> None:
        """
        Limpia la pantalla de la consola para hacer más fácil la visualización.
        Funciona tanto en sistemas Windows como en Unix.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def reset(self) -> None:
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