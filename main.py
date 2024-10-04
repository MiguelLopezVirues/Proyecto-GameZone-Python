from src.ahorcado import Ahorcado

def mostrar_menu():
    print("Bienvenido a la GameZone")
    print("Están disponibles los siguientes juegos:")
    # for i, archivo in enumerate(archivos):
    # print(f"{i}. {archivo}")
    # provisional:
    print("1. Ahorcado")

def main():
    mostrar_menu()

    juegos = {
        "1": Ahorcado()
    }

    juego_seleccionado = input("¿A qué juego quieres jugar? Introduce el número que le corresponde:")
    juego_en_curso = juegos[juego_seleccionado]
    juego_en_curso.jugar()
    pass 



if __name__ == "__main__":
    main()