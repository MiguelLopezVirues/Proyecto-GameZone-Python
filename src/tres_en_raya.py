
import random 
from functools import reduce
from operator import itemgetter
from .recursos.tres_en_raya_recursos import welcome_banner, fichas_tic_tac_toe
import os 
import pyfiglet
from colorama import Fore, Style, init
class Tres_raya():
    """
    Clase que gestiona el funcionamiento del juego de Tres en Raya (Tic-Tac-Toe).

    Attributes:
    -----------
    celda_vacia : str
        Representa una celda vacía en el tablero.
    posiciones : list[list[str]]
        Matriz 3x3 que representa el tablero de juego.
    lista_coordenadas : list[str]
        Lista con las coordenadas posibles del tablero en formato "fila,columna".
    matriz_coordenadas : list[list[str]]
        Matriz con las coordenadas del tablero en formato "fila,columna".
    n_jugadores : int
        Número de jugadores en la partida (1 o 2).
    ficha_jugador : dict
        Diccionario que asocia cada jugador con su ficha ("x" o "o").
    turno : str
        Indica qué jugador tiene el turno actual ("jugador_1" o "jugador_2").
    lista_jugadores : list[str]
        Lista que contiene los nombres de los jugadores.
    modo_automatico : bool
        Indica si el segundo jugador es la máquina.
    lineas_coordenadas : dict
        Diccionario que contiene las diferentes líneas (horizontales, verticales y diagonales) del tablero con sus respectivas coordenadas.
    lineas : dict
        Diccionario que contiene las posiciones actuales en el tablero para cada línea (horizontal, vertical y diagonal).
    modo_dificultad : bool
        Indica la dificultad de la IA (True para inteligente, False para aleatorio).
    condiciones_victoria : dict
        Diccionario que almacena las condiciones de victoria o empate.

    Methods:
    --------
    __init__():
        Inicializa el tablero y todos los atributos necesarios para empezar el juego.
    
    welcome():
        Muestra el título de bienvenida del juego en la consola.
    
    jugar():
        Inicia el flujo principal del juego, gestionando el número de jugadores, turnos y verificando las condiciones de victoria o empate.
    
    introducir_ficha_jugador():
        Solicita la coordenada del jugador para introducir una ficha en el tablero.
    
    elegir_jugadores():
        Permite al usuario elegir si habrá 1 o 2 jugadores y, si es 1, activa el modo automático para que la máquina sea el segundo jugador.
    
    elegir_turnos():
        Permite elegir qué jugador empieza, con opción aleatoria por defecto.
    
    actualizar_turno():
        Alterna el turno entre los jugadores.
    
    elegir_ficha():
        Permite al jugador 1 elegir qué ficha usar ("x" o "o"), con una opción aleatoria por defecto.
    
    elegir_dificultad():
        Establece el nivel de dificultad para la máquina.
    
    encontrar_coordenadas_celdas_vacias(coordenada):
        Verifica si una celda está vacía según la coordenada proporcionada.
    
    evaluar_celdas_vacias(lista_puntuaciones, coordenada):
        Evalúa las celdas vacías y asigna puntuaciones a las coordenadas en función de las estrategias de la máquina.
    
    estrategia_maquina(modo_dificultad):
        Define el movimiento de la máquina, ya sea usando una estrategia inteligente o eligiendo una celda al azar.
    
    introducir_ficha(coordenada):
        Introduce una ficha en la posición indicada por la coordenada.
    
    pintar_tablero():
        Muestra el tablero actual en la consola.
    
    actualizar_lineas():
        Actualiza las líneas del tablero (horizontal, vertical y diagonal) con las posiciones actuales.
    
    comprobar_victoria():
        Verifica si algún jugador ha ganado o si ha habido un empate.
    
    limpiar_pantalla():
        Limpia la pantalla de la consola.
    
    reset():
        Reinicia el juego si el jugador decide volver a jugar después de una partida.
    """
    def __init__(self) -> None:
        """
        Inicializa el tablero de juego, fichas y configuraciones del Tres en Raya.
        """
        self.celda_vacia = "  "
        self.posiciones = [[self.celda_vacia for i in range(3)] for j in range(3)]
        self.lista_coordenadas = [f"{fila},{columna}" for columna in range(3) for fila in range(3)]
        self.matriz_coordenadas = [[f"{fila},{columna}" for columna in range(3)] for fila in range(3)]
        self.n_jugadores = 1
        self.ficha_jugador = {
            "jugador_1": fichas_tic_tac_toe["x"],
            "jugador_2": fichas_tic_tac_toe["o"]
        }
        self.turno = "jugador_1"
        self.lista_jugadores = ["jugador_1","jugador_2"]
        self.modo_automatico = False
        self.lineas_coordenadas = {
            "vertical_0": [fila[0] for fila in self.matriz_coordenadas],
            "vertical_1": [fila[1] for fila in self.matriz_coordenadas],
            "vertical_2": [fila[2] for fila in self.matriz_coordenadas],
            "horizontal_0": self.matriz_coordenadas[0],
            "horizontal_1": self.matriz_coordenadas[1],
            "horizontal_2": self.matriz_coordenadas[2],
            "diagonal_0,0": [fila[posicion] for posicion,fila in enumerate(self.matriz_coordenadas)],
            "diagonal_2,0": [fila[posicion] for posicion,fila in enumerate(reversed(self.matriz_coordenadas))]
        }

    def welcome(self):
        """
        Muestra un banner de bienvenida al juego.
        """
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("TIC-TAC-TOE", font="bulbhead")
        print(Fore.BLUE + titulo)

    def jugar(self):
        """
        Inicia el ciclo principal del juego de tres en raya (Tic-Tac-Toe), donde los jugadores seleccionan el número
        de jugadores, la dificultad, el tipo de fichas y los turnos. Luego, se ejecuta la partida hasta que haya un
        ganador o un empate.

        Detalles:
        - Se permite la selección del número de jugadores: 1 o 2.
        - Se define si se juega contra la máquina o entre jugadores humanos.
        - Los jugadores eligen qué fichas utilizar (X o O).
        - Se alternan turnos entre los jugadores o la máquina.
        - La partida continúa hasta que uno de los jugadores logre alinear tres fichas seguidas (horizontal, vertical o diagonalmente)
        o hasta que se acaben las casillas disponibles (empate).
        - Al final del juego, se muestra un mensaje indicando si hay un ganador o si la partida ha terminado en empate.
        
        La función también incluye:
        - Manejo de los turnos, incluida la IA para el jugador controlado por la máquina en dificultades superiores.
        - Restablecimiento del juego después de cada partida.
        """
        self.elegir_jugadores()
        if self.modo_automatico == True:
            self.elegir_dificultad()
        self.elegir_turnos()
        self.elegir_ficha()
        self.limpiar_pantalla()
        self.pintar_tablero()
        self.actualizar_lineas()
        while not all(posicion != self.celda_vacia for fila in self.posiciones for posicion in fila):
            if self.modo_automatico == True and self.turno == "jugador_2":
                print("Turno del Jugador 2.")
                self.estrategia_maquina(self.modo_dificultad)
            else:
                self.introducir_ficha_jugador()
            self.pintar_tablero()
            if self.comprobar_victoria() == True:
                break
            self.actualizar_turno()

        self.reset()

    def introducir_ficha_jugador(self):
        """
        Permite al jugador introducir las coordenadas para colocar su ficha, 
        realizando una llamada al método introducir_ficha(coordenada).
        Si la coordenada no es válida, se vuelve a realizar la petición.
        """
        coordenada = input(f"{self.turno.title()}, introduce una coordenada de dos numeros, separados por una coma: \n")
        try:
            self.introducir_ficha(coordenada)
        except IndexError:
            print("\nHas introducido una coordenada fuera de rango. El rango es de 0,0 a 2,2.")
            self.introducir_ficha_jugador()
        except:
            print("\nNo has introducido una coordenada")
            self.introducir_ficha_jugador()
        
            

    def elegir_jugadores(self):
        """
        Permite al usuario seleccionar el número de jugadores.
        Si solo hay uno, activa el modo de juego contra la máquina.
        """
        try:
            self.n_jugadores = int(input("¿Cuantos jugadores sois?[1/2]\n"))
            if self.n_jugadores < 1 or self.n_jugadores > 2:
                    raise ValueError("El valor introducido está fuera de rango. Por favor introduce un numero del 1 al 2.")
        except ValueError:
            print("\nEl valor introducido está fuera de rango. Por favor introduce un numero del 1 al 2.")
            self.elegir_jugadores()
        else:
            if self.n_jugadores == 1:
                print("\nDe acuerdo. El jugador 2 será la máquina.")
                self.modo_automatico = True
            else:
                print("\nDemostrad vuestro fair play y que gane el mejor.")


    
    def elegir_turnos(self):
        """
        Elige quién comenzará la partida. El usuario puede escoger entre
        Jugador 1, Jugador 2 o una selección aleatoria, que es el valor 
        por defecto en caso de haber introducido un valor incorrecto.
        """
        try:
            eleccion_turnos = int(input("""\n¿Quien empieza, el Jugador 1 o el Jugador 2? Introduce un número:
                            1. Jugador_1
                            2. Jugador_2
                            3. [Por defecto] Aleatorio
                            \n"""))
            if eleccion_turnos < 1 or eleccion_turnos > 3:
                    raise ValueError("El valor introducido está fuera de rango o no es correcto.")
        except:
            print("\nHas introducido un valor incorrecto. Se pasa al modo Aleatorio por defecto.")
        
        if eleccion_turnos == 1:
            pass
        elif eleccion_turnos == 2:
            self.actualizar_turno()
        elif random.choice([0,1]) == 1:
            self.actualizar_turno()

        
    def actualizar_turno(self):
        """
        Cambia el turno al otro jugador.
        """
        self.lista_jugadores = list(reversed(self.lista_jugadores))
        self.turno = self.lista_jugadores[0]
        pass
    
    def elegir_ficha(self):
        """
        Permite a los jugadores seleccionar sus fichas (X o O). Si el valor 
        introducido es incorrecto, se elige aleatoriamente por defecto.
        """
        eleccion_fichas = int(input(f"""\nJugador 1. ¿Con que ficha quieres jugar? Introduce el número correspondiente a tu elección:
                                1. {fichas_tic_tac_toe["x"]}
                                2. {fichas_tic_tac_toe["o"]}
                                3. [Por defecto] Aleatorio
                                \n"""))
        
        fichas_posibles = [fichas_tic_tac_toe["x"],fichas_tic_tac_toe["o"]]


        opciones_fichas = {
            1: 0,
            2: 1,
            3: random.choice([0,1])}
        
        try:
            ficha_jugador_1 = opciones_fichas[eleccion_fichas]
        except:
            print("\nHas introducido un valor incorrecto. Se pasa al modo Aleatorio por defecto.")
            ficha_jugador_1 = random.choice([0,1])
        
        self.ficha_jugador = {
            "jugador_1": fichas_posibles.pop(ficha_jugador_1),
            "jugador_2": fichas_posibles[0]
        }
    
    def elegir_dificultad(self):
        """
        Permite al usuario elegir la dificultad en el modo contra la máquina.
        """
        seguir_jugando = input("\n¿Deseas jugar en modo fácil? [Y/N]\n")
        try:
            if seguir_jugando.upper()[0] == "Y":
                self.modo_dificultad = False
            else:
                self.modo_dificultad = True
        except:
            print("\nDebes introducir 'Y' o 'N' para que se registre tu eleccion.")
            self.elegir_dificultad()

    ## ESTRATEGIA MAQUINA
    def encontrar_coordenadas_celdas_vacias(self,coordenada):
        """
        Verifica si una coordenada específica está vacía.

        Parameters:
        coordenada (str): Coordenada en formato "fila,columna"

        Returns:
        bool: True si la celda está vacía, False de lo contrario.
        """
        fila = int(coordenada.split(",")[0])
        columna = int(coordenada.split(",")[1])
        if self.posiciones[fila][columna] == self.celda_vacia:
            return True
        
    def evaluar_celdas_vacias(self,lista_puntuaciones,coordenada):
        """
        Evalúa las celdas vacías y les asigna puntuaciones en función de las líneas de juego.

        Parameters:
        lista_puntuaciones (list): Lista con puntuaciones de las celdas.
        coordenada (str): Coordenada de la celda a evaluar.

        Returns:
        list: Lista con las puntuaciones actualizadas.
        """
        def filtrar_lineas(lista, linea):
            """
            Filtra las líneas del tablero que contienen la coordenada dada.

            Parameters:
            -----------
            lista : list
                Lista de líneas que han sido filtradas y que contienen la coordenada.
            linea : str
                Nombre de la línea actual (horizontal, vertical o diagonal) a verificar.

            Returns:
            --------
            list
                Lista actualizada con las líneas que contienen la coordenada.
            """
            if coordenada in self.lineas_coordenadas[linea]:
                lista.append(self.lineas[linea])
            return lista
            
        nombres_lineas = list(self.lineas.keys())
        lineas_de_coordenada = list(reduce(filtrar_lineas,nombres_lineas,list()))

        def puntuar_coordenada(acumulado,linea):
            """
            Asigna una puntuación a una coordenada en función de las fichas en una línea.

            Parameters:
            -----------
            acumulado : list
                Lista con la coordenada en evaluación y su puntuación en formato de cadena.
            linea : list[str]
                Lista que contiene las fichas en una línea específica del tablero (puede ser una fila, columna o diagonal).

            Returns:
            --------
            list
                Lista que contiene la coordenada y su puntuación acumulada en formato de cadena "xxxxx", donde cada posición de la cadena indica:
                    - Posición 0: Jugador 2 está a punto de ganar.
                    - Posición 1: Jugador 1 está a punto de ganar.
                    - Posición 2: Jugador 2 tiene una ficha y puede acumular estrategia.
                    - Posición 3: Jugador 1 tiene una ficha y debe ser bloqueado.
                    - Posición 4: Línea completamente vacía.
            """
            acumulado[1] = list(acumulado[1])
            if linea.count(self.ficha_jugador["jugador_2"]) == 2: # Ganar partida
                acumulado[1][0] = str(int(acumulado[1][0]) + 1)
            elif linea.count(self.ficha_jugador["jugador_1"]) == 2: # Enemigo a punto de ganar partida
                acumulado[1][1] = str(int(acumulado[1][1]) + 1)
            elif linea.count(self.ficha_jugador["jugador_2"]) == 1 and linea.count(self.celda_vacia) == 2: # Acumular estrategia
                acumulado[1][2] = str(int(acumulado[1][2]) + 1)
            elif linea.count(self.ficha_jugador["jugador_1"]) == 1 and linea.count(self.celda_vacia) == 2: # Bloquear estrategia
                acumulado[1][3] = str(int(acumulado[1][3]) + 1)
            elif linea.count(self.celda_vacia) == 3: # Linea vacía
                acumulado[1][4] = str(int(acumulado[1][4]) + 1)
            acumulado[1] = ("").join(acumulado[1])
            return acumulado

        puntuacion_coordenada = reduce(puntuar_coordenada,lineas_de_coordenada,[coordenada,"00000"])
        lista_puntuaciones.append(puntuacion_coordenada)
        return lista_puntuaciones

    
    def estrategia_maquina(self,modo_dificultad):
        """
        Estrategia de la máquina para jugar. Puede ser aleatoria o basada en
        una evaluación inteligente según la dificultad seleccionada.

        Parameters:
        modo_dificultad (bool): Indica si se está jugando en modo fácil o difícil.
        """
        celdas_disponibles = list(filter(self.encontrar_coordenadas_celdas_vacias,self.lista_coordenadas))

        # inteligente
        if modo_dificultad == True: 
            
            # print("Celdas disponibles", celdas_disponibles)
            puntuacion_celdas = reduce(self.evaluar_celdas_vacias, celdas_disponibles,list())
            puntuacion_celdas_descendente = list(reversed(sorted(puntuacion_celdas, key=itemgetter(1))))
            # print("Puntuacion celdas:", puntuacion_celdas_descendente)
            coordenada_optima = puntuacion_celdas_descendente[0][0]
            self.introducir_ficha(coordenada_optima)
        
        else: # aleatoria
            self.introducir_ficha(celdas_disponibles)


    def introducir_ficha(self, coordenada):
        """
        Coloca la ficha del jugador en la coordenada seleccionada.

        Parameters:
        coordenada (str): Coordenada donde se introducirá la ficha.
        """
        fila, columna = coordenada.split(",")
        fila = int(coordenada.split(",")[0])
        columna = int(coordenada.split(",")[1])
        if self.posiciones[fila][columna] == self.celda_vacia:
            self.posiciones[fila][columna] = self.ficha_jugador[self.turno]
        else:
            coordenada = input("\nLa coordenada introducida ya está ocupada. Por favor introduce otra distinta: ")
            self.introducir_ficha(coordenada)
    
    def pintar_tablero(self):
        """
        Dibuja el tablero actual en la pantalla con las posiciones ocupadas por las fichas.
        """
        print("\n")
        print(f"{self.posiciones[0][0]}❕{self.posiciones[0][1]}❕{self.posiciones[0][2]}")
        print("➖➕➖➕➖")
        print(f"{self.posiciones[1][0]}❕{self.posiciones[1][1]}❕{self.posiciones[1][2]}")
        print("➖➕➖➕➖")
        print(f"{self.posiciones[2][0]}❕{self.posiciones[2][1]}❕{self.posiciones[2][2]}")
        print("\n")

    def actualizar_lineas(self):
        """
        Actualiza las líneas horizontales, verticales y diagonales con las fichas
        colocadas en el tablero.
        """
        self.lineas = {
            "vertical_0": [fila[0] for fila in self.posiciones],
            "vertical_1": [fila[1] for fila in self.posiciones],
            "vertical_2": [fila[2] for fila in self.posiciones],
            "horizontal_0": self.posiciones[0],
            "horizontal_1": self.posiciones[1],
            "horizontal_2": self.posiciones[2],
            "diagonal_0,0": [fila[posicion] for posicion,fila in enumerate(self.posiciones)],
            "diagonal_2,0": [fila[posicion] for posicion,fila in enumerate(reversed(self.posiciones))]
        }

    def comprobar_victoria(self):
        """
        Comprueba si hay un ganador o si la partida ha terminado en empate.

        Returns:
        bool: True si hay un ganador o empate, False si la partida continúa.
        """
        self.actualizar_lineas()
        for linea, contenido_linea in self.lineas.items():
            self.condiciones_victoria = {
            "jugador_1": all([posicion == self.ficha_jugador["jugador_1"] for posicion in contenido_linea]),
            "jugador_2": all([posicion == self.ficha_jugador["jugador_2"] for posicion in contenido_linea]),
            "empate": all([columna != self.celda_vacia for fila in self.posiciones for columna in fila])
            }
            if self.condiciones_victoria["jugador_1"] or self.condiciones_victoria["jugador_2"]:
                if self.condiciones_victoria["jugador_1"]:
                    ganador = "Jugador 1"

                elif self.condiciones_victoria["jugador_2"]:
                    ganador = "Jugador 2"
                
                print(f"\n¡Enhorabuena {ganador}, ganas la partida!")
                return True
            elif self.condiciones_victoria["empate"]:
                print("\n¡Ha habido un empate!")
                return True
        return False
    
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
    


