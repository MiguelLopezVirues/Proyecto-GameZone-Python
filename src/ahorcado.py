import random
import sys
from .ressources.ahorcado_recursos import HANGMANPICS, HANGMANPIC_SUCCESS, HANGMANPIC_DEATH, palabras_ahorcado

### Apuntes
# Valorar si hay forma mejor deshacerme del uso de la copia lista por su método remove
#

class Ahorcado():
    def __init__(self) -> None:
        self.intentos = list()
        self.display_palabra_lista = list()
        self.dibujo = ""

    def jugar(self):
        self.seleccionar_dificultad()
        self.generar_palabra()
        self.pintar_dibujo()
        self.pintar_display()
        while "_" in self.display_palabra_lista and self.vidas_restantes > 0:
            letra_intento = input("\n\nEscribe una letra:")
            self.comprobar_letra(letra_intento)
            if "_" not in self.display_palabra_lista:
                self.actualizar_dibujo("win")
                print("\n¡Enhorabuena, has ganado!")
            elif self.vidas_restantes == 0:
                self.actualizar_dibujo("loss")
                print("\n¡NOOOO, has matado al ahorcado!")
            else:
                print("Actualiza dibujo")
                self.actualizar_dibujo(self.vidas_restantes)

            self.actualizar_display(letra_intento)
            self.pintar_dibujo()
            self.pintar_display()

        self.reset()

    
    def seleccionar_dificultad(self):
        self.vidas_restantes = int(input("""Elige tu dificultad introduciendo el número de vidas:
        Patético: 6 vidas
        Principiante: 5 vidas
        Corriente: 4 vidas
        Atrevido: 3 vidas
        Leyenda: 2 vidas
        Puto colgao: 1 vida
        """))
        self.dibujo = HANGMANPICS[-self.vidas_restantes-1]


    def pintar_dibujo(self):
        """"""
        print(self.dibujo)

    def pintar_display(self):
        """"""
        display_palabra = "".join(self.display_palabra_lista)
        print(display_palabra)
        print(f"Te quedan {self.vidas_restantes} vidas restantes.")





    def generar_palabra(self) -> None:
        """"""
        self.palabra_turno_lista = list(random.choice(palabras_ahorcado).lower()) 
        self.display_palabra_lista = list("_"*len(self.palabra_turno_lista))



    def comprobar_letra(self, letra_intento) -> bool:
        """"""
        if letra_intento in self.palabra_turno_lista:
            print("¡Acierto!")
                
        else: 
            print("¡Error!")
            self.vidas_restantes -= 1
            resultado = "error"
            
            

    def actualizar_display(self,letra_intento):
        while letra_intento in self.palabra_turno_lista:
            posicion_letra = self.palabra_turno_lista.index(letra_intento)
            self.display_palabra_lista[posicion_letra] = letra_intento.upper()
            self.palabra_turno_lista[posicion_letra] = "_"

    
    def actualizar_dibujo(self,resultado="error") -> None:
        """"""
        if resultado == "win":
            self.dibujo = HANGMANPIC_SUCCESS
        elif resultado == "loss":
            self.dibujo = HANGMANPIC_DEATH
        else:
            self.dibujo = HANGMANPICS[-self.vidas_restantes-1]

    def reset(self):
        seguir_jugando = input("\n¿Deseas volver a jugar? [Y/N]\n")
        if seguir_jugando.upper()[0] == "Y":
            self.__init__()
            self.jugar()
        else:
            print("\n¡Ha sido un placer!\n")