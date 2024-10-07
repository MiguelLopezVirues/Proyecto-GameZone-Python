# 🕹️ Sala de juegos con Python: Programación orientada a objetos de juegos clásicos

## 📖 Descripción
Este proyecto realiza el desarrollo de una Sala de Juegos con 4 juegos clásicos, cuyas lógicas de juego individuales están gestionadas por sus clases de Python independientes. Cada uno de los juegos se orquesta desde un script central que hace la función de Sala de Juegos, donde el usuario tiene la opción de jugar al juego que elija.

## 🗂️ Estructura del Proyecto
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

## 🛠️ Instalación y Requisitos
Este proyecto require Python 3.9 y requiere de forma adicional únicamente de la librería pyfiglet, para el estilo de los banners utilizados en las presentaciones de los juegos. El archivo requirements.txt puede utilizarse para instalarlas con el comando:
```bash
pip install requirements.txt
```
## ⚙️ Funcionalidades
- Modo inteligente en el juego contra la máquina para el Tres en Raya.

## 🔄 Próximos Pasos
- Añadir juego hundir la flota.
- Refactorizar código para simplificar y mejorar la lógica, evitando redundancias.
- Retocar los estilos del juego, para hacerlos más atractivos al usuario.
- Traducir el código a inglés para adaptarlo al mercado actual.
- Concretar más el error-handling.
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
