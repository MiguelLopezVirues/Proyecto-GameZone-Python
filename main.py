from src.ahorcado import Ahorcado
from src.tres_raya import Tres_raya
from src.preguntados import Preguntados
from src.piedra_papel_tijera import Piedra_papel_tijera
import time
import pyfiglet
from colorama import Fore, Style, init
import os

def mostrar_menu():
    print(Fore.BLUE + """ 
 ██████╗  █████╗ ███╗   ███╗███████╗███████╗ ██████╗ ███╗   ██╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝╚══███╔╝██╔═══██╗████╗  ██║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗    ███╔╝ ██║   ██║██╔██╗ ██║█████╗
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝   ███╔╝  ██║   ██║██║╚██╗██║██╔══╝
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████╗╚██████╔╝██║ ╚████║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝""")

    print(Fore.WHITE + "\nEstán disponibles los siguientes juegos:")
    # for i, archivo in enumerate(archivos):
    # print(f"{i}. {archivo}")
    # provisional:
    print("1. Ahorcado")
    print("2. Tres en raya")
    print("3. Preguntados")
    print("4. Piedra-papel-tijera-lagarto-Spock")
    print("5. Salir")

def main():

    mostrar_menu()

    print("\n\n¿A qué juego quieres jugar?")
    
    juego_en_curso = elegir_juego()
    if juego_en_curso == "salir":
        print("De acuerdo. ¡Vuelve cuado quieras!")
        exit()
    juego_en_curso.limpiar_pantalla()
    juego_en_curso.welcome()

    time.sleep(1.5)
    juego_en_curso.jugar()
    reset()



def elegir_juego():
    juegos = {
        "1": Ahorcado(),
        "2": Tres_raya(),
        "3": Preguntados(),
        "4": Piedra_papel_tijera(),
        "5": "salir"
    }
    try:
        juego_seleccionado = input("\nIntroduce el número que corresponde con el juego al que quieres jugar:").strip()
        return juegos[juego_seleccionado]
    except KeyError:
        print("\nEl valor introducido no se corresponde con ningún juego.")
        return elegir_juego()

def reset():
    if input("\n¿Quieres jugar a algún otro juego?[Y/N]").lower()[0] == "y":
        main()
    else:
        print("\nSaliendo de GameZone :)")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print("¡Bienvenido a la GameZone!")
        main()
    except KeyboardInterrupt:
        print("\nSaliendo de GameZone. ¡Nos vemos pronto!")