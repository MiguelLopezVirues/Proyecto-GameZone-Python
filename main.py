from src.ahorcado import Ahorcado
from src.tres_raya import Tres_raya
from src.preguntados import Preguntados
from src.piedra_papel_tijera import Rock_paper_scissors

def mostrar_menu():
    print(""" 
 ██████╗  █████╗ ███╗   ███╗███████╗███████╗ ██████╗ ███╗   ██╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝╚══███╔╝██╔═══██╗████╗  ██║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗    ███╔╝ ██║   ██║██╔██╗ ██║█████╗
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝   ███╔╝  ██║   ██║██║╚██╗██║██╔══╝
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████╗╚██████╔╝██║ ╚████║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝""")
    print("\nEstán disponibles los siguientes juegos:")
    # for i, archivo in enumerate(archivos):
    # print(f"{i}. {archivo}")
    # provisional:
    print("1. Ahorcado")
    print("2. Tres en raya")
    print("3. Preguntados")
    print("4. Piedra-papel-tijera-lagarto-Spock")

def main():
    mostrar_menu()

    print("\n\n¿A qué juego quieres jugar?")
    
    juego_en_curso = elegir_juego()
    juego_en_curso.welcome()
    juego_en_curso.jugar()
    if input("\n¿Quieres jugar a algún otro juego?").lower()[0] == "y":
        main()
    else: 
        print("Nos vemos pronto :)")


def elegir_juego():
    juegos = {
        "1": Ahorcado(),
        "2": Tres_raya(),
        "3": Preguntados(),
        "4": Rock_paper_scissors()
    }
    try:
        juego_seleccionado = input("\nIntroduce el número que corresponde con el juego al que quieres jugar:")
        return juegos[juego_seleccionado]
    except:
        print("\nEl valor introducido no se corresponde con ningún juego.")
        elegir_juego()


if __name__ == "__main__":
    print("¡Bienvenido a la GameZone!")
    main()