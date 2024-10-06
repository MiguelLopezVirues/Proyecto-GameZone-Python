
import random 
from functools import reduce
from operator import itemgetter
from .ressources.tic_tac_toe_recursos import welcome_banner, fichas_tic_tac_toe
import os 
import pyfiglet
from colorama import Fore, Style, init
class Tres_raya():
    def __init__(self) -> None:
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
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("TIC-TAC-TOE", font="bulbhead")
        print(Fore.BLUE + titulo)

    def jugar(self):
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
        self.lista_jugadores = list(reversed(self.lista_jugadores))
        self.turno = self.lista_jugadores[0]
        pass
    
    def elegir_ficha(self):
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
        fila = int(coordenada.split(",")[0])
        columna = int(coordenada.split(",")[1])
        if self.posiciones[fila][columna] == self.celda_vacia:
            return True
        
    def evaluar_celdas_vacias(self,lista_puntuaciones,coordenada):

        def filtrar_lineas(lista, linea):
            if coordenada in self.lineas_coordenadas[linea]:
                lista.append(self.lineas[linea])
            return lista
            
        
        nombres_lineas = list(self.lineas.keys())
        lineas_de_coordenada = list(reduce(filtrar_lineas,nombres_lineas,list()))

        def puntuar_coordenada(acumulado,linea):
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
        fila, columna = coordenada.split(",")
        fila = int(coordenada.split(",")[0])
        columna = int(coordenada.split(",")[1])
        if self.posiciones[fila][columna] == self.celda_vacia:
            self.posiciones[fila][columna] = self.ficha_jugador[self.turno]
        else:
            coordenada = input("\nLa coordenada introducida ya está ocupada. Por favor introduce otra distinta: ")
            self.introducir_ficha(coordenada)
    
    def pintar_tablero(self):
        print("\n")
        print(f"{self.posiciones[0][0]}❕{self.posiciones[0][1]}❕{self.posiciones[0][2]}")
        print("➖➕➖➕➖")
        print(f"{self.posiciones[1][0]}❕{self.posiciones[1][1]}❕{self.posiciones[1][2]}")
        print("➖➕➖➕➖")
        print(f"{self.posiciones[2][0]}❕{self.posiciones[2][1]}❕{self.posiciones[2][2]}")
        print("\n")

    def actualizar_lineas(self):
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
        os.system('cls' if os.name == 'nt' else 'clear')


    def reset(self):
        seguir_jugando = input("\n¿Deseas volver a jugar? [Y/N]\n")
        if seguir_jugando.upper()[0] == "Y":
            self.__init__()
            self.jugar()
        else:
            print("\n¡Ha sido un placer!\n")
    


