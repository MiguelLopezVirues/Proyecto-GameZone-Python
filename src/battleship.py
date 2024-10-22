import random 
import copy
from functools import reduce
from operator import itemgetter
from .recursos.battleship_ressources import sea_icon, water_icon, touched_icon,sunk_icon,ship_icon, board_numbers, enemy_ship_icon
import os 
import pyfiglet
from colorama import Fore, Style, init

class Battleship():
    def __init__(self) -> None:
        self.lines_player = None
        self.lines_machine = None
        self.board_player = [[sea_icon for i in range(10)] for j in range(10)]
        self.board_player_visible = copy.deepcopy(self.board_player)
        self.board_machine = copy.deepcopy(self.board_player)  # Deep copy for independent boards
        self.board_machine_visible = copy.deepcopy(self.board_player)  # Deep copy for independent boards
        self.board_coordinates = [[f"{row},{column}" for column in range(10)] for row in range(10)]
        self.board_list = [f"{row},{column}" for column in range(10) for row in range(10)]
        self.player_ship_coordinates = {"aircraft_carrier": None, 
                      "battleship": None,
                      "submarine": None,
                      "cruiser": None,
                      "destroyer": None}
        self.machine_ship_coordinates = copy.deepcopy(self.player_ship_coordinates)

    def welcome(self) -> None:
        """Muestra un mensaje de bienvenida con el título del juego."""
        self.limpiar_pantalla()
        init(autoreset=True)
        self.titulo = pyfiglet.figlet_format("BATTLESHIP", font="slant")
        print(Fore.BLUE + self.titulo)
    

    def jugar(self):
        self.print_board()
        print("Let's place your fleet!")
        self.place_fleet(player=False)
        # We're not here yet
        self.choose_difficulty()
        self.place_fleet(player=True)
        self.war()


    def print_board(self):
        for row_number,row in enumerate(self.board_player):
            print(''.join(cell for cell in row))

    def print_board_machine(self):
        for row_number,row in enumerate(self.board_machine):
            print(''.join(cell for cell in row),"|",''.join(cell for cell in self.board_machine_visible[row_number]))
    
    
    def war(self):
        while True:
            self.player_attack()
            if self.all_sunk(self.machine_ship_coordinates, self.board_machine_visible):
                print("You win.")
                break
            self.print_board_machine()
            self.machine_attack()
            if self.all_sunk(self.player_ship_coordinates, self.board_player):
                print("You lose.")
                break
        return False

    def player_attack(self):
        print("Introduce a coordinate:\n")
        x_attack, y_attack = None, None
        while not all([x_attack in range(10), y_attack in range(10)]):
            try:
                attack_coordinate = input()
                x_attack = int(attack_coordinate.split(",")[0]) - 1
                y_attack = int(attack_coordinate.split(",")[1]) - 1
            except ValueError:
                print("Enter a coordinate within the board.")
                continue

            if self.board_machine_visible[y_attack][x_attack] == water_icon or self.board_machine_visible[y_attack][x_attack] == touched_icon:
                print("You had already tried this spot.")
                self.player_attack()
            
            elif self.touches(self.machine_ship_coordinates,[f"{x_attack},{y_attack}"]):
                print("Touched!")
                self.board_machine_visible[y_attack][x_attack] = touched_icon

            else:
                print("Water...")
                self.board_machine_visible[y_attack][x_attack] = water_icon

    def machine_attack(self):
        available_coordinates = list(filter(self.find_empty,self.board_list))
        attack_coordinates = random.choice(available_coordinates)
        x_attack = int(attack_coordinates.split(",")[0])
        y_attack = int(attack_coordinates.split(",")[1])
        if self.touches(self.machine_ship_coordinates,[f"{x_attack},{y_attack}"]):
            print("The machine touched you!")
            self.board_player[y_attack][x_attack] = touched_icon
        else:
            print("The machine shot to water...")
            self.board_player[y_attack][x_attack] = water_icon

    def find_empty(self,coordinate):
        """
        Verifica si una coordenada específica está vacía.

        Parameters:
        coordenada (str): Coordenada en formato "fila,columna"

        Returns:
        bool: True si la celda está vacía, False de lo contrario.
        """
        x = int(coordinate.split(",")[0])
        y = int(coordinate.split(",")[1])
        if self.board_player_visible[y][x] == sea_icon:
            return True

    def update_turn(self):
        """
        Cambia el turno al otro jugador.
        """
        self.lista_jugadores = list(reversed(self.lista_jugadores))
        self.turno = self.lista_jugadores[0]
        pass


    def choose_difficulty(self):
        pass

    def place_fleet(self, player = True):
        self.lines_player = None
        self.lines_enemy = None
        self.ships = {"aircraft_carrier": 5, 
                      "battleship": 4,
                      "submarine": 3,
                      "cruiser": 3,
                      "destroyer": 2}
        for ship_name, ship_length in self.ships.items():
            if player:
                # self.limpiar_pantalla()
                self.print_board()
                ship_coordinates_list = self.ask_ship_position_direction(ship_name, ship_length)
                self.place_ship(ship_name,ship_coordinates_list,player=True)
            else:
                # self.limpiar_pantalla()
                self.print_board_machine()
                ship_coordinates_list = self.decide_ship_position_machine(ship_name, ship_length)
                self.place_ship(ship_name,ship_coordinates_list,player=False)

    def ask_ship_position_direction(self,ship_name,ship_length):
        x1, y1 = self.ask_ship_position(ship_name)
        ship_coordinates_list = self.ask_ship_direction(x1,y1,ship_name,ship_length)

        if self.touches(self.player_ship_coordinates, ship_coordinates_list):
            print("There are collisions with your previous ships. Please try again at a different location.")
            self.ask_ship_position_direction(ship_name,ship_length)
        return ship_coordinates_list


    def ask_ship_position(self, ship_name):
        ship_name_formatted = ship_name.replace("_"," ").title()
        x1, y1 = None, None

        print(f"Choose and write a first coordinate to place your {ship_name_formatted} by introducing two integers separated by a comma:\n")

        while not all([x1 in range(10), y1 in range(10)]):
            try:
                x1, y1 = input().split(",")
                x1 = int(x1) - 1
                y1 = int(y1) - 1

            except ValueError:
                print("""Wrong value for a coordinate introduced. Please, enter values between 0 and 9, separated by a comma.""")
                continue

            if self.touches(self.player_ship_coordinates, [f"{x1},{y1}"]): # inside lists, we first access the row (y-axis), then the column (x-axis)
                print("This coordinate is already taken by one of your ships. Enter a coordinate not already taken.")
                x1, y1 = None, None

            elif not all([x1 in range(10), y1 in range(10)]):
                print("The coordinate is incorrect or out of the board.")
   
        return x1,y1
    
    def ask_ship_direction(self,x1,y1, ship_name, ship_length):

        x2, y2 = None, None

        print(f"""Choose a direction to continue to place your {ship_name.replace("_"," ").title()} by writing a number:
                                        1. Left 
                                        2. Right
                                        3. Up
                                        4. Down\n""")
        
        while any([x2 not in range(10), y2 not in range(10)]): 

            try:
                direction = int(input())
                
                self.direction_options = {
                    1: [x1 - ship_length+1, y1],
                    2: [x1 + ship_length-1, y1],
                    3: [x1, y1 - ship_length+1], # up
                    4: [x1, y1 + ship_length-1] # down
                }
                x2, y2 = self.direction_options[direction]

                ship_coordinates_list = [f"{i},{j}" for j in range(min(y1,y2),max(y1,y2)+1) for i in range(min(x1,x2),max(x1,x2)+1)]
                

                if direction not in range(1, 5):
                    print("Please choose a valid direction between 1 and 4.")

            except (ValueError or KeyError or UnboundLocalError):
                print("Invalid input. Please enter a number.")
                continue

            else:
                if any([x2 not in range(10), y2 not in range(10)]):

                    print(x2,y2,"The coordinates jump out of the board. Enter a value within the board.")


                elif self.touches(self.player_ship_coordinates, ship_coordinates_list): 
                    print("There is a collision with another one of your ships.")
                    x2, y2 = None, None # restarts loop
            

        return ship_coordinates_list

    
    def place_ship(self,ship_name,ship_coordinates_list, player=True):
        if player:
            self.player_ship_coordinates[ship_name] = ship_coordinates_list
            for coordinate in ship_coordinates_list:
                x, y = coordinate.split(",")
                # invert x and y
                # the user enters (x, y) or (column, row) coordinates, 
                # but 2D lists are [list][element] or [row][column]
                self.board_player[int(y)][int(x)] = ship_icon 
        else:
            self.machine_ship_coordinates[ship_name] = ship_coordinates_list
            for coordinate in ship_coordinates_list:
                # invert x and y
                # the user enters (x, y) or (column, row) coordinates, 
                # but 2D lists are [list][element] or [row][column]
                x, y = coordinate.split(",")
                self.board_machine[int(y)][int(x)] = enemy_ship_icon

    def all_sunk(self, fleet_coordinates_dict, board):
        ship_cells = [board[int(coordinate.split(",")[1])][int(coordinate.split(",")[0])] for ship_coordinates in fleet_coordinates_dict.values() for coordinate in ship_coordinates]
        if all([ship_cell == touched_icon for ship_cell in ship_cells]):
            return True

        
    def touches(self, fleet_coordinates_dict, coordinates_list):
        for ship_coordinates in fleet_coordinates_dict.values():
            if ship_coordinates is not None:
                if self.check_coordinates_in_ship(ship_coordinates, coordinates_list):
                    return True
    

    def check_coordinates_in_ship(self, ship_coordinates, coordinates_list):
        for coordinate in coordinates_list:
            if coordinate in ship_coordinates:
                return True
            

    def decide_ship_position_machine(self, ship_name, ship_length):

        while True:
            x1, y1 = [random.randint(0,9),random.randint(0,9)]
            direction = random.randint(1,4)
            self.direction_options = {
                    1: [x1 - ship_length+1, y1],
                    2: [x1 + ship_length-1, y1],
                    3: [x1, y1 - ship_length+1],
                    4: [x1, y1 + ship_length-1]
            }
            x2, y2 = self.direction_options[direction]
            ship_coordinates_list = [f"{i},{j}" for j in range(min(y1,y2),max(y1,y2)+1) for i in range(min(x1,x2),max(x1,x2)+1)]

            if not self.touches(self.machine_ship_coordinates, ship_coordinates_list) and not any([x2 not in range(10), y2 not in range(10)]):
                break

        return ship_coordinates_list
    
 


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