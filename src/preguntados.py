import random
import sys
from .ressources.preguntados_recursos import actualidad, ciencia, historia, cultura_general, entretenimiento, welcome_banner
import pyfiglet
from colorama import Fore, Style, init
import os

class Preguntados():
    def __init__(self) -> None:
        self.rondas = [n for n in range(0,10)]
        self.puntuacion = 0

    def welcome(self):
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("PREGUNTADOS", font="starwars")
        print(Fore.RED + titulo)

    def jugar(self):
        self.crear_set_preguntas()
        self.correr_rondas()
        if self.puntuacion == len(self.rondas):
            print("¡VICTORIA! Has ganado al juego de Preguntados.")
        self.reset()

    def correr_rondas(self):
        for n_ronda,p_partida in enumerate(self.p_partida):
            print(f"""\n -----------------------------------------------\nRonda {n_ronda+1}.\n""")
            print("Pregunta:", p_partida["pregunta"])
            respuestas = p_partida["incorrecta"]
            respuestas.append(p_partida["correcta"])
            random.shuffle(respuestas)
            respuestas_dict = {
                "A": respuestas[0],
                "B": respuestas[1],
                "C": respuestas[2],
                "D": respuestas[3]
            }
            for letra, respuesta in respuestas_dict.items():
                print(f"{letra}) {respuesta}")
            
            if self.responder_pregunta(p_partida,respuestas_dict) == False:
                break

    def responder_pregunta(self, p_partida, respuestas_dict):
        respuesta_usuario = input("Introduce la letra que corresponde con tu respuesta:\n").upper()
        try:
            if self.verificar_respuesta(p_partida,respuestas_dict[respuesta_usuario]) == True:
                print("\n¡Correcto!")
                print("Puntuacion", self.puntuacion)
                self.puntuacion += 1
                return True
            else:
                print("\nOoooh ¡Has perdido!")
                return False
        except:
            print("\nLa respuesta que has introducido no es válida.")
            
    
    def verificar_respuesta(self, pregunta, respuesta):
        if respuesta == pregunta["correcta"]:
            self.puntuacion += 1
            return True
        else:
            return False
    
    def crear_set_preguntas(self):
        categorias = [actualidad,ciencia,historia,cultura_general,entretenimiento]
        self.p_partida = list()
        for categoria in categorias * int(len(self.rondas)/len(categorias)):
            self.p_partida.append(random.choice(categoria))
        
        random.shuffle(self.p_partida)
        return 
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def reset(self):
        seguir_jugando = input("\n¿Deseas volver a jugar? [Y/N]\n")
        if seguir_jugando.upper()[0] == "Y":
            self.__init__()
            self.jugar()
        else:
            print("\n¡Ha sido un placer!\n")
