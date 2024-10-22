# 🕹️ Sala de juegos con Python: Programación orientada a objetos aplicada
<p align="center">
  <img src="assets/gamezone.gif" alt="alt text" title="Title">
</p>

## 📖 Descripción
Este proyecto realiza el desarrollo de una Sala de Juegos con 4 (un 5º en construcción) juegos clásicos, cuyas lógicas de juego individuales están gestionadas por sus clases de Python independientes. El objetivo es practicar Python con la filosofía de la programación orientada a objetos, sin hacer uso de librerías externas como Pandas o Numpy, para favorecer la comprensión base del lenguaje.

Cada uno de los juegos programados se orquesta desde un script central que hace la función de Sala de Juegos, donde el usuario tiene la opción de jugar al juego que elija. Los juegos incluidos son:

- ❌⭕ Tres en raya (con IA): El clásico estrategia en el que debes alinear los tres símbolos en una cuadrícula de 3x3. Incluye un modo contra la máquina con Inteligencia Artificial para desafiar al jugador.

- 🪨🖖✂️🦎🖖 Piedra-papel-tijera-lagarto-Spock: Una variante divertida del clásico juego de Piedra, Papel y Tijeras, donde se agregan nuevas opciones más frikis: Lagarto y Spock, ¡ampliando la estrategia!

- 𓍯😵 Ahorcado: Adivina la palabra antes de quedarte sin vidas. Cada fallo acerca más al pobre muñeco a su destino final.

- ❓🧠 Preguntados: Pone a prueba tus conocimientos en varias rondas de preguntas de distintas categorías, desde historia hasta entretenimiento.
  
- 🚢 Battleship (En construcción): El mítico hundir la flota en un tablero de 10x10

## 🗂️ Estructura del Proyecto
```python
├── src/  # Directorio de scripts con las lógicas de cada juego
│   ├── ahorcado.py
│   ├── piedra_papel_tijera.py
│   ├── preguntados.py
│   ├── tres_raya.py            
│   └── recursos/   # Archivos almacenadores de variables estáticas de cada uno de los juegos 
│       ├── ahorcado_recursos.py     
│       ├── piedra_papel_tijera.py   
│       ├── preguntados.py          
│       └── tres_raya_recursos.py    
├── main.py               # Script central de Sala de Juego
├── requirements.txt      # Paquetes requeridos para la ejecución y reproducción del proyecto
├── README.md             # Descripción del proyecto
```
## 🛠️ Instalación y Requisitos
[Response #1]

Este proyecto fue desarrollado utilizando Python 3.9 y requiere de forma adicional únicamente de la librería pyfiglet, que se utiliza para los banners en las presentaciones de los juegos. Para ejecutar el proyecto, sigue estos pasos:

Clona el repositorio:

```bash
git clone https://github.com/MiguelLopezVirues/Proyecto-GameZone-Python
```

Navega al directorio del proyecto:

```bash
cd Proyecto-GameZone-Python
```

Instala las dependencias desde el archivo `requirements.txt` con pip:

```bash
pip install -r requirements.txt
```

Ejecuta el menú principal para seleccionar un juego:

```bash
python main.py
```

Puedes consultar la documentación de pyfiglet [aquí](https://github.com/pwaller/pyfiglet).

## ⚙️ Funcionalidades
- **Tres en raya - Inteligencia Artificial**: El juego del tres en raya puede elegir ser jugado en modo difícil, lo cual activa la inteligencia artificial de la máquina, prácticamente imposibilitando la victoria.
- **Preguntados**: Durante 10 rondas, se lanzan preguntas aleatorias de distintas categorías (Historia, Ciencia, Cultura General, etc). Si el usuario llega hasta la ronda 10 sin fallar, gana la partida.
- **Piedra papel tijera, largarto spock**: Se puede elegir entre 1 o 2 jugadores. En caso de elegir 1 jugador, se juega contra la máquina. Acto seguido, se elige al mejro de cuantas rondas jugar y comienza la batalla.
- **Ahorcado**: Se puede elegir entre 7 modos de dificultad, en función de las vidas restantes del ahorcado.
- **Hundir la flota**: En construcción.

## 🔄 Próximos Pasos
- **Hundir la flota**:
  - Terminar construcción.
  - Añadir modo Inteligencia Artificial
- **Ahorcado**:
  - Añadir opción para introducir palabras nuevas mediante la consola por el usuario.
- **Preguntados**
  - Añadir opción de introducción de nuevas preguntas por  el usuario.
- **General**:
  - Refactorizar código para simplificar y mejorar la lógica, evitando redundancias.
  - Perfeccionar la estética en consola de los juegos, para hacerlos más atractivos al usuario.
  - Traducir el código a inglés para adaptarlo al mercado actual.
  - Incluir testing.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.

## ✒️ Autor
- **Miguel López** - Github: [@miguellopezvirues](https://github.com/miguellopezvirues). LinkedIn: [Miguel López Virues](https://www.linkedin.com/in/miguellopezvirues/)

## ⚖️ License
The MIT License (MIT)

Copyright (c) 2024 Miguel López Virués

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
