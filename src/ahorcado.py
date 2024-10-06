import random
import sys
from .recursos.ahorcado_recursos import HANGMANPICS, HANGMANPIC_SUCCESS, HANGMANPIC_DEATH, palabras_ahorcado
import pyfiglet
from colorama import Fore, Style, init
import os

class Ahorcado:
    """
    Representa el juego del Ahorcado, donde el jugador debe adivinar una palabra secreta eligiendo letras
    dentro de un número limitado de intentos.

    Atributos:
    ----------
    intentos : list[str]
        Lista que almacena los intentos realizados por el jugador.
    display_palabra_lista : list[str]
        Lista que representa el estado actual de la palabra a adivinar, mostrando letras acertadas y guiones bajos.
    dibujo : str
        Representación visual del estado actual del ahorcado.

    Métodos:
    --------
    __init__() -> None:
        Inicializa los atributos del juego.

    welcome() -> None:
        Muestra un mensaje de bienvenida con el título del juego.

    jugar() -> None:
        Ejecuta el ciclo principal del juego, gestionando la selección de dificultad, la generación de la palabra,
        y el flujo del juego hasta que el jugador gana o pierde.

    seleccionar_dificultad(retry: bool = False) -> None:
        Permite al jugador seleccionar la dificultad del juego a través del número de vidas. Si la entrada es
        inválida, se le pide que lo intente de nuevo.

    pintar_dibujo() -> None:
        Muestra en pantalla la representación visual del ahorcado.

    pintar_display() -> None:
        Muestra en pantalla la palabra a adivinar en su estado actual y el número de vidas restantes.

    generar_palabra() -> None:
        Selecciona aleatoriamente una palabra de la lista de palabras del juego y establece su estado inicial
        con guiones bajos en la lista de visualización.

    introducir_letra(retry: bool = False) -> bool:
        Permite al jugador introducir una letra para adivinar. Verifica si la entrada es válida y si la letra
        está presente en la palabra a adivinar.

    actualizar_display() -> None:
        Actualiza la lista de visualización de la palabra, reemplazando los guiones bajos por la letra adivinada
        en las posiciones correctas.

    actualizar_dibujo(resultado: str = "error") -> None:
        Actualiza la representación visual del ahorcado según el resultado del intento actual (ganar, perder o error).

    limpiar_pantalla() -> None:
        Limpia la pantalla en sistemas Windows o Unix.

    reset() -> None:
        Ofrece la opción de reiniciar el juego o finalizarlo.
    """

    def __init__(self) -> None:
        """Inicializa los atributos del juego."""
        self.intentos = list()
        self.display_palabra_lista = list()
        self.dibujo = ""

    def welcome(self) -> None:
        """Muestra un mensaje de bienvenida con el título del juego."""
        init(autoreset=True)
        self.titulo = pyfiglet.figlet_format("HANGMAN", font="poison")
        print(Fore.LIGHTRED_EX + self.titulo)

    def jugar(self) -> None:
        """
        Ejecuta el ciclo principal del juego, gestionando la selección de dificultad, la generación de la palabra,
        y el flujo del juego hasta que el jugador gana o pierde.

        El jugador debe intentar adivinar la palabra oculta eligiendo letras, con un número limitado de intentos.
        Si el jugador adivina correctamente todas las letras antes de agotar los intentos, gana el juego. 
        De lo contrario, si se quedan sin intentos, el jugador pierde.
        """
        self.seleccionar_dificultad()
        self.generar_palabra()
        self.pintar_dibujo()
        self.pintar_display()
        while "_" in self.display_palabra_lista and self.vidas_restantes > 0:
            self.introducir_letra()
            if "_" not in self.display_palabra_lista:
                self.actualizar_dibujo("win")
                print("\n¡Enhorabuena, has ganado!")
            elif self.vidas_restantes == 0:
                self.actualizar_dibujo("loss")
                print("\n¡NOOOO, has matado al ahorcado!")
                self.pintar_dibujo()
                print("\nHas perdido.")
                break
            else:
                self.actualizar_dibujo(self.vidas_restantes)

            self.actualizar_display()
            self.pintar_dibujo()
            self.pintar_display()

        self.reset()

    def seleccionar_dificultad(self, retry: bool = False) -> None:
        """
        Permite al jugador seleccionar la dificultad del juego a través del número de vidas. Si la entrada es
        inválida, se le pide que lo intente de nuevo.

        Parameters:
            retry (bool): Indica si se está intentando nuevamente después de una entrada inválida.
        """
        if not retry:
            self.vidas_restantes = input("""\nElige tu dificultad introduciendo el número de vidas:                                
            Insecto: 6 vidas
            Principiante: 5 vidas
            Corriente: 4 vidas
            Atrevido: 3 vidas
            Leyenda: 2 vidas
            Puto colgao: 1 vida
            """)
        else:
            self.vidas_restantes = input("\n")
        try:
            self.vidas_restantes = int(self.vidas_restantes)
            if self.vidas_restantes < 1 or self.vidas_restantes > 6:
                raise IndexError("Valor fuera de rango.")
        except IndexError:
            print("El valor que has introducido está fuera del rango permitido. Inténtalo de nuevo.")
            self.seleccionar_dificultad(retry=True)
        except:
            print("El valor que has introducido no es correcto. Inténtalo de nuevo.")
            self.seleccionar_dificultad(retry=True)

        self.dibujo = HANGMANPICS[-self.vidas_restantes - 1]

    def pintar_dibujo(self) -> None:
        """Muestra en pantalla la representación visual del ahorcado."""
        print(self.dibujo)

    def pintar_display(self) -> None:
        """Muestra en pantalla la palabra a adivinar en su estado actual y el número de vidas restantes."""
        display_palabra = "".join(self.display_palabra_lista)
        print(display_palabra)
        print(f"Te quedan {self.vidas_restantes} vidas restantes.")

    def generar_palabra(self) -> None:
        """Selecciona aleatoriamente una palabra de la lista de palabras del juego y establece su estado inicial
        con guiones bajos en la lista de visualización."""
        self.palabra_turno_lista = list(random.choice(palabras_ahorcado).lower())
        self.display_palabra_lista = list("_" * len(self.palabra_turno_lista))

    def introducir_letra(self, retry: bool = False) -> bool:
        """
        Permite al jugador introducir una letra para adivinar. Verifica si la entrada es válida y si la letra
        está presente en la palabra a adivinar.

        Parameters:
            retry (bool): Indica si se está intentando nuevamente después de una entrada inválida.

        Returns:
            bool: True si la letra fue un intento exitoso, False en caso contrario.
        """
        if not retry:
            self.letra_ultimo_intento = input("\n\nEscribe una letra:")
        else:
            self.letra_ultimo_intento = input("\n")
        try:
            if not self.letra_ultimo_intento.isalpha():
                raise ValueError("El valor introducido no es una letra.")
        except:
            print("No has introducido una letra válida. Inténtalo de nuevo.")
            self.introducir_letra(retry=True)
            return False  # Indica que el intento fue inválido.
        if self.letra_ultimo_intento in self.palabra_turno_lista:
            print("¡Acierto!")
            return True  # Indica que la letra fue correcta.
        else:
            print("¡Error!")
            self.vidas_restantes -= 1
            return False  # Indica que la letra fue incorrecta.

    def actualizar_display(self) -> None:
        """Actualiza la lista de visualización de la palabra, reemplazando los guiones bajos por la letra adivinada
        en las posiciones correctas."""
        while self.letra_ultimo_intento in self.palabra_turno_lista:
            posicion_letra = self.palabra_turno_lista.index(self.letra_ultimo_intento)
            self.display_palabra_lista[posicion_letra] = self.letra_ultimo_intento.upper()
            self.palabra_turno_lista[posicion_letra] = "_"

    def actualizar_dibujo(self, resultado: str = "error") -> None:
        """
        Actualiza la representación visual del ahorcado según el resultado del intento actual (ganar, perder o error).

        Parameters:
            resultado (str): Indica el resultado del intento, puede ser "win", "loss" o "error".
        """
        if resultado == "win":
            self.dibujo = HANGMANPIC_SUCCESS
        elif resultado == "loss":
            self.dibujo = HANGMANPIC_DEATH
        else:
            self.dibujo = HANGMANPICS[-self.vidas_restantes - 1]

    def limpiar_pantalla(self) -> None:
        """Limpia la pantalla en sistemas Windows o Unix."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def reset(self) -> None:
        """Ofrece la opción de reiniciar el juego o finalizarlo."""
        seguir_jugando = input("\n¿Deseas volver a jugar? [Y/N]\n")
        if seguir_jugando.upper()[0] == "Y":
            self.__init__()
            self.jugar()
        else:
            print("\n¡Ha sido un placer!\n")
