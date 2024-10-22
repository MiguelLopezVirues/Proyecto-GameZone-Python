import random 
from functools import reduce
from operator import itemgetter
from .recursos.battleship_ressources import sea_icon, water_icon, touched_icon,sunk_icon,ship_icon
import os 
import pyfiglet
from colorama import Fore, Style, init

class Battleship():
    def __init__(self) -> None:
        self.lines_player = None
        self.lines_machine = None
        self.board_player = [[sea_icon for i in range(10)] for j in range(10)]
        self.board_machine = self.board_player.copy()
        self.board_coordinates = [[f"{row},{column}" for column in range(10)] for row in range(10)]
        self.player_ship_coordinates = {"aircraft_carrier": None, 
                      "battleship": None,
                      "submarine": None,
                      "cruiser": None,
                      "destroyer": None}
        self.machine_ship_coordinates = self.player_ship_coordinates.copy()
        pass

    def welcome(self) -> None:
        """Muestra un mensaje de bienvenida con el título del juego."""
        self.limpiar_pantalla()
        init(autoreset=True)
        self.titulo = pyfiglet.figlet_format("BATTLESHIP", font="slant")
        print(Fore.BLUE + self.titulo)
    

    def jugar(self):
        self.print_board()
        print("Let's place your fleet!")
        self.place_fleet()

        self.choose_difficulty()
        while not any(all(),all()):
            pass


    def print_board(self):
        for row in self.board_player:
            print(''.join(cell for cell in row))
    





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
                self.limpiar_pantalla()
                self.print_board()
                ship_coordinates_list = self.ask_ship_position_direction(ship_name=ship_name, ship_length=ship_length)
                self.place_ship(ship_name,ship_coordinates_list)
            else:
                ship_coordinates_list = self.decide_ship_position_machine(ship_name=ship_name, ship_length=ship_length)
                self.place_ship(ship_name,ship_coordinates_list)



    def ask_ship_position(self, ship, retry = False, who="player"):
        if who == "player":
            if not retry:
                ship_name = ship.replace("_"," ").title()
                coordinates_1 = input(f"Choose and write a first coordinate to place your {ship_name} by introducing two integers separated by a comma:")
            else: 
                coordinates_1 = input(f"")
        else:
            pass

        try:
            x1, y1 = coordinates_1.split(",")
            x1 = int(x1)
            y1 = int(y1)
            
            if any([x1 <0, x1 > 9, y1 < 0, y1 > 9]):
                raise IndexError("The coordinates suggested jump out of the board.")
            elif self.touches([f"{x1},{y1}"], self.player_ship_coordinates):
                raise IndexError("The coordinates are already taken by another ship.")
            
        except ValueError:
            if who == "player":
                print("Wrong value for a coordinate introduced. Please, enter a correct value.")
                self.ask_ship_position(ship,retry=True)
            else:
                self.ask_ship_position(ship,retry=True,who="machine")

        except IndexError:
            if who == "player":
                print("The coordinates suggested jump out of the board or are already taken.")
                self.ask_ship_position(ship,retry=True)
            else:
                self.ask_ship_position(ship,retry=True,who="machine")
        
        return x1,y1

    def ask_ship_direction(self,x1,y1, ship_name, ship_length, retry = False, who = "player"):
        if who == "player":
            if not retry:
                direction = input(f"""Choose a direction to continue to place your {ship_name.replace("_"," ").title()} by writing a number:
                                    1. Left 
                                    2. Right
                                    3. Up
                                    4. Down""")
            else:
                direction = input("")
        else:
            direction = random.choice[1,2,3,4]
        try:
            direction = int(direction)
            if direction < 0 or direction > 4:
                raise ValueError("Answer out of permitted range.")
            self.direction_options = {
                1: [x1 - ship_length-1, y1],
                2: [x1 + ship_length-1, y1],
                3: [x1, y1 - ship_length-1],
                4: [x1, y1 + ship_length-1]
            }
            x2, y2 = self.direction_options[direction]
            if any([x2 <0, x2 > 9, y2 < 0, y2 > 9]):
                print("Wrong calculation of direction",x2,y2)
                raise IndexError("The coordinates suggested jump out of the board.")
            
            elif self.touches([f"{x2},{y2}"], self.player_ship_coordinates):
                raise IndexError("The coordinates are already taken by another ship.")
            
        except ValueError: 
            if who == "player":
                print("Please introduce a valid number from the options.")
                self.ask_ship_direction(x1,y1,ship_name,ship_length,retry=True,who="player")
            else:
                self.ask_ship_direction(x1,y1,ship_name,ship_length,retry=True,who="machine")

        except IndexError: 
            if who == "player":
                print("One of these coordinates are already taken by another one of your ships.")
                self.ask_ship_direction(x1,y1,ship_name,ship_length,retry=True,who="player")
            else:
                self.ask_ship_direction(x1,y1,ship_name,ship_length,retry=True,who="machine")
        return x2,y2
        
    def ask_ship_position_direction(self,ship_name,ship_length):
        x1, y1 = self.ask_ship_position(ship_name)
        x2, y2 = self.ask_ship_direction(x1,y1,ship_name,ship_length)
        ship_coordinates_list = [f"{x1 + i},{y1+j}" for j in range(y2 - y1 + 1) for i in range(x2 - x1 + 1)]
        if self.touches(ship_coordinates_list, self.player_ship_coordinates):
            print("There are collisions with your previous ships. Please try again at a different location.")
            self.ask_ship_position_direction(ship_name,ship_length)
        return ship_coordinates_list
    
    def place_ship(self,ship_name,ship_coordinates_list, player=False):
        if player:
            self.player_ship_coordinates[ship_name] = ship_coordinates_list
            for coordinate in ship_coordinates_list:
                x, y = coordinate.split(",")
                self.board_player[int(y)][int(x)] = ship_icon
        else:
            self.machine_ship_coordinates[ship_name] = ship_coordinates_list
            for coordinate in ship_coordinates_list:
                x, y = coordinate.split(",")
                self.board_machine[int(y)][int(x)] = ship_icon

            
        
    def touches(self, coordinates, fleet_coordinates_dict):
        if any(list(map(self.map_filter_coordinates,fleet_coordinates_dict,coordinates))):
            return True
    

    def map_filter_coordinates(self, coordinates,ship_coordinates):
        for coordinate in coordinates:
            if coordinate in ship_coordinates:
                return True

    def decide_ship_position_machine(self):
        # aleatorio
        x1, y1 = [random.randint(0,9),random.randint(0,9)]
        direction = random.choice[1,2,3,4]
        x2, y2 = self.direction_options[direction]
        while self.touches(ship_coordinates_list, self.player_ship_coordinates):
            ship_coordinates_list = [f"{x1 + i},{y1+j}" for j in range(y2 - y1 + 1) for i in range(x2 - x1 + 1)]
            if not self.touches(ship_coordinates_list, self.player_ship_coordinates):
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