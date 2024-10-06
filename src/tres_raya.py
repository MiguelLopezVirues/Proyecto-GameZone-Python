
import random 
from functools import reduce
from operator import itemgetter

class Tres_raya():
    def __init__(self) -> None:
        self.posiciones = [[" " for i in range(3)] for j in range(3)]
        self.lista_coordenadas = [f"{fila},{columna}" for columna in range(3) for fila in range(3)]
        self.matriz_coordenadas = [[f"{fila},{columna}" for columna in range(3)] for fila in range(3)]
        self.n_jugadores = 1
        self.ficha_jugador = {
            "jugador_1": "X",
            "jugador_2": "O"
        }
        self.turno = "jugador_1"
        self.lista_jugadores = ["jugador_1","jugador_2"]
        self.modo_automatico = False
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

    def jugar(self):
        self.pintar_tablero()
        self.elegir_jugadores()
        if self.modo_automatico == True:
            self.elegir_dificultad()
        self.elegir_turnos()
        self.elegir_ficha()
        while not all(posicion != " " for fila in self.posiciones for posicion in fila):
            if self.modo_automatico == True and self.turno == "jugador_2":
                coordenada = self.estrategia_maquina(self.modo_dificultad)
            else:
                coordenada = input(f"{self.turno.title()}, introduce una coordenada de dos numeros, separados por una coma: ")
            self.introducir_ficha(coordenada)
            self.pintar_tablero()
            if self.comprobar_victoria() == True:
                print(f"¡VICTORIA DEL {self.turno.upper()}")
                break
            self.actualizar_turno()

        self.reset()


    def elegir_jugadores(self):
        self.n_jugadores = int(input("¿Cuantos jugadores sois?"))
        if self.n_jugadores == 1:
            print("De acuerdo. El jugador 2 será la máquina.")
            self.modo_automatico = True
        else:
            print("Demostrad vuestro fair play y que gane el mejor.")

    
    def elegir_turnos(self):
        eleccion_turnos = int(input("""¿Quien empieza, el Jugador 1 o el Jugador 2? Introduce un número:
                            1. Jugador_1
                            2. Jugador_2
                            3. Aleatorio"""))
        if eleccion_turnos == 1:
            pass
        elif eleccion_turnos == 2:
            self.actualizar_turno()
        elif random.choice([0,1]) == 1:
            self.actualizar_turno()

        
    def actualizar_turno(self):
        print("Cambio turno")
        self.lista_jugadores = list(reversed(self.lista_jugadores))
        self.turno = self.lista_jugadores[0]
        pass
    
    def elegir_ficha(self):
        eleccion_fichas = int(input("""Jugador 1. ¿Con que ficha quieres jugar? Introduce el número correspondiente a tu elección:
                                1. X
                                2. O
                                3. Aleatorio"""))
        fichas_posibles = ["X","0"]
        
        opciones_fichas = {
            1: 0,
            2: 1,
            3: random.choice([0,1])}
        
        print(opciones_fichas[eleccion_fichas])
        
        self.ficha_jugador = {
            "jugador_1": fichas_posibles.pop(opciones_fichas[eleccion_fichas]),
            "jugador_2": fichas_posibles[0]
        }
    
    def elegir_dificultad(self):
        seguir_jugando = input("¿Deseas jugar en modo fácil? [Y/N]")
        if seguir_jugando.upper()[0] == "Y":
            self.modo_dificultad = False
        else:
            self.modo_dificultad = True

    ## ESTRATEGIA MAQUINA
    def encontrar_coordenadas_celdas_vacias(self,coordenada):
        fila = int(coordenada.split(",")[0])
        columna = int(coordenada.split(",")[1])
        if self.posiciones[fila][columna] == " ":
            return True
        
    def evaluar_celdas_vacias(self,lista_puntuaciones,coordenada):
        def filtrar_lineas(lista, linea):
            if coordenada in self.lineas_coordenadas[linea]:
                lista.append(self.lineas[linea])
            return lista
            
        
        nombres_lineas = list(self.lineas.keys())
        lineas_de_coordenada = list(reduce(filtrar_lineas,nombres_lineas,list()))

        def puntuar_coordenada(acumulado,linea):
            # print("Printeando linea:",linea)
            acumulado[1] = list(acumulado[1])
            if linea.count(self.ficha_jugador["jugador_2"]) == 2: # Ganar partida
                acumulado[1][0] = str(int(acumulado[1][0]) + 1)
            elif linea.count(self.ficha_jugador["jugador_1"]) == 2: # Enemigo a punto de ganar partida
                acumulado[1][1] = str(int(acumulado[1][1]) + 1)
            elif linea.count(self.ficha_jugador["jugador_2"]) == 1 and linea.count(" ") == 2: # Acumular estrategia
                acumulado[1][2] = str(int(acumulado[1][2]) + 1)
            elif linea.count(self.ficha_jugador["jugador_1"]) == 1 and linea.count(" ") == 2: # Bloquear estrategia
                acumulado[1][3] = str(int(acumulado[1][3]) + 1)
            elif linea.count(" ") == 3: # Linea vacía
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
            return coordenada_optima
        
        else: # aleatoria
            return random.choice(celdas_disponibles)


    def introducir_ficha(self, coordenada):
        print("Lineas antes de introducir", self.lineas)
        fila, columna = coordenada.split(",")
        fila = int(coordenada.split(",")[0])
        columna = int(coordenada.split(",")[1])
        if self.posiciones[fila][columna] == " ":
            self.posiciones[fila][columna] = self.ficha_jugador[self.turno]
        else:
            coordenada = input("La coordenada introducida ya está ocupada. Por favor introduce otra distinta: ")
            self.introducir_ficha(coordenada)
    
    def pintar_tablero(self):
        [print(f"({fila[0]}) ({fila[1]}) ({fila[2]})") for fila in self.posiciones]
        print("\n ---")

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
            # print(linea,contenido_linea)
            if all([posicion == "X" for posicion in contenido_linea]) or all([posicion == "O" for posicion in contenido_linea]):
                return True
        return False


    def reset(self):
        seguir_jugando = input("¿Deseas volver a jugar? [Y/N]")
        if seguir_jugando.upper()[0] == "Y":
            self.__init__()
            self.jugar()
        else:
            print("¡Ha sido un placer!")
    


