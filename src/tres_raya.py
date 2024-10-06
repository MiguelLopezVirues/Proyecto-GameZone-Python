
import random 

class Tres_raya():
    def __init__(self) -> None:
        self.posiciones = [[" " for i in range(3)] for j in range(3)]
        self.lista_coordenadas = [f"{fila},{columna}" for columna in range(3) for fila in range(3)]
        self.n_jugadores = 1
        self.ficha_jugador = {
            "jugador_1": "X",
            "jugador_2": "O"
        }
        self.turno = "jugador_1"
        self.lista_jugadores = ["jugador_1","jugador_2"]
        self.modo_automatico = False


    def jugar(self):
        
        self.pintar_tablero()
        self.elegir_jugadores()
        while not all(posicion != " " for fila in self.posiciones for posicion in fila):
            if self.modo_automatico == True and self.turno == "jugador_2":
                coordenada = self.estrategia_maquina()
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
        eleccion_turnos = int(input("""¿Quien empieza? Introduce un número
                            1. Jugador_1
                            2. Jugador_2
                            3. Aleatorio"""))
        
    def actualizar_turno(self):
        print("Cambio turno")
        self.lista_jugadores = list(reversed(self.lista_jugadores))
        self.turno = self.lista_jugadores[0]
        pass
    
    # def elegir_ficha(self):
    #     eleccion_fichas = int(input("""¿Con que ficha quieres jugar? Introduce un número
    #                             1. X
    #                             2. O
    #                             3. Aleatorio"""))
    #     opciones_fichas = {
    #         1: "X",
    #         2: "O",
    #         3: random.choice(["X","O"])
           
    #     self.fichas = {
    #         "jugados_1": ,
    #         "jugador_2": "O"
    #     }
        
        
    def estrategia_maquina(self):
        # aleatoria
        def coordenadas_celdas_vacias(coordenada):
            fila = int(coordenada.split(",")[0])
            columna = int(coordenada.split(",")[1])
            if self.posiciones[fila][columna] == " ":
                return True
            
        celdas_disponibles = list(filter(coordenadas_celdas_vacias,self.lista_coordenadas))

        return random.choice(celdas_disponibles)

        

    def introducir_ficha(self, coordenada):
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

    def comprobar_victoria(self):
        lineas = {
            "vertical_0": [fila[0] for fila in self.posiciones],
            "vertical_1": [fila[1] for fila in self.posiciones],
            "vertical_2": [fila[2] for fila in self.posiciones],
            "horizontal_0": self.posiciones[0],
            "horizontal_1": self.posiciones[1],
            "horizontal_2": self.posiciones[2],
            "diagonal_0,0": [fila[posicion] for posicion,fila in enumerate(self.posiciones)],
            "diagonal_2,0": [fila[posicion] for posicion,fila in enumerate(reversed(self.posiciones))]
        }


        for linea, contenido_linea in lineas.items():
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
    


