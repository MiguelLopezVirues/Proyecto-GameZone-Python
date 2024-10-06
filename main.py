from src.ahorcado import Ahorcado
from src.tres_raya import Tres_raya
from src.preguntados import Preguntados
from src.piedra_papel_tijera import Piedra_papel_tijera

def mostrar_menu():
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
    juegos = {
        "1": Ahorcado(),
        "2": Tres_raya(),
        "3": Preguntados(),
        "4": Piedra_papel_tijera()
    }

    juego_seleccionado = input("\n\n¿A qué juego quieres jugar? Introduce el número que le corresponde:")
    juego_en_curso = juegos[juego_seleccionado]
    juego_en_curso.jugar()
    if input("\n¿Quieres jugar a algún otro juego?").lower()[0] == "y":
        main()
    else: 
        print("Nos vemos pronto :)")



if __name__ == "__main__":
    print("¡Bienvenido a la GameZone!")
    main()