# Proyecto Módulo 1
![imagen](https://s3-eu-west-1.amazonaws.com/files.olearyssportsbar.com/gamezone_4.jpg.1200x630_q85.jpg)
Welcome to... our first proyect! En este primer proyecto una empresa nos ha contactado para desarrollar una serie de videojuegos clásicos para su plataforma usando Python. Para llevar a cabo esta tarea tendremos que poner en práctica todos nuestros conocimientos de Python.

Los juegos que la empresa quiere desarrollar son los siguientes:

- **Preguntados** : En este juego tendremos que ir haciendo preguntas al usuario sobre una variedad de temas y el usuario tendrá que ir respondiendo correctamente para avanzar. Las preguntas podrán ser de distintas categorías: cultura general, historia, entretenimiento, actualidad, etc. El usuario ganará el juego si consigue adivinar 10 preguntas seguidas.

- **Tres en raya** : Mítico juego donde el primero que consiga colocar tres fichas seguidas(en horizontal, vertical o diagonal) en un tablero 3x3 gana la partida. En nuestro caso, la empresa nos ha pedido que el usuario juegue contra la máquina.

- **Ahorcado**: El usuario juega contra la máquina. En este juego el usuario tendrá que adivinar una palabra elegida al azar por la máquina de entre una lista que nosotros definiremos previamente. Cada vez que el usuario se equivoque, mostraremos una nueva parte del personaje del ahorcado en una horca. Si el usuario consigue adivinar la palabra antes de que se le acaben las oportunidades, gana el juego.

- **Piedra-papel-tijera** : en este juego el usuario tendrá que elegir una de las opciones y después la máquina eligirá otra al azar. Gana el primero que gane tres rondas en total. Además la empresa nos ha pedido que, además del juego clásico, el usuario pueda elegir la opción de jugar a **piedra-papel-tijera-lagarto-spock**. 

- **Hundir la flota** : En este juego queremos que el usuario juegue contra la máquina este mítico juego de estrategia. El usuario tiene que tratar de encontrar los barcos de la máquina en un tablero 10x10 antes de que la máquina encuentre los suyos.

*Las características de cada juego las encontraréis más adelante*


# Objetivos del proyecto

- De los juegos planteados tendréis que elegir al menos cuatro de los cinco juegos.

- Cada juego tiene que estar programado como una clase y recogido dentro de un archivo ` .py` en la carpeta `src`.

- Tenemos que tener un archivo .py que nos permita elegir entre los juegos que hemos desarrollado y jugarlos sin necesidad de ir a cada archivo del juego.

- Una vez que acabe, cada juego tiene que dar la opción de volver a jugar al mismo juego, volver a la elección de juegos o terminar el programa.



# Reglas de cada juego

## Preguntados

- El juego consiste en hacer preguntas al usuario sobre una variedad de temas. Las preguntas se dividen en distintas categorías como **cultura general**, **historia**, **entretenimiento**, **actualidad**, entre otras.

- El objetivo del jugador es responder correctamente a las preguntas para avanzar en el juego.

- El jugador gana si logra responder correctamente 10 preguntas consecutivas. Si falla una pregunta, el juego termina.

**Pistas para desarrollar el juego**

- Comienza creando un conjunto de categorías como "Cultura General", "Historia", "Entretenimiento", "Ciencia", etc. Dentro de cada categoría, define un conjunto de preguntas con sus respectivas respuestas correctas y algunas opciones incorrectas.

- Implementa una lógica para seleccionar preguntas aleatorias de las distintas categorías. Esto asegura que cada partida sea diferente y mantiene el interés del jugador.

- Cada pregunta debe presentarse con un conjunto de opciones de respuesta (por ejemplo, A, B, C, D), donde solo una de ellas es correcta.

- Permite que el jugador elija su respuesta indicando la opción (A, B, C o D). Verifica que la opción ingresada sea válida antes de evaluarla.

- Después de que el jugador seleccione una opción, verifica si es correcta. Si acierta, continúa con la siguiente pregunta. Si falla, el juego termina y se informa al jugador que ha perdido.

- Lleva un registro de cuántas preguntas ha respondido correctamente el jugador de forma consecutiva. El objetivo es llegar a 10 aciertos seguidos.

- Si el jugador responde correctamente 10 preguntas seguidas, declara al jugador como ganador y termina el juego.

- Después de cada pregunta, informa al jugador si su respuesta fue correcta o incorrecta. También puedes mostrar cuántas respuestas correctas lleva acumuladas.

- Al final de la partida, ofrece la opción de jugar de nuevo. Si el jugador decide volver a intentarlo, reinicia el conteo y comienza con nuevas preguntas.


## Tres en Raya

- El juego se juega en un tablero de 3x3.

- Dos jugadores (el jugador y la máquina, o dos jugadores humanos) se alternan para colocar sus símbolos en el tablero: **X** o **O**.

- El objetivo del juego es conseguir alinear tres de tus símbolos de manera horizontal, vertical o diagonal antes que el oponente.

- El juego puede terminar de tres maneras:

  - Un jugador logra alinear tres de sus símbolos y gana.

  - El tablero se llena sin que ningún jugador logre alinear tres símbolos (empate).

  - Se puede establecer una condición de finalización si uno de los jugadores abandona.

**Pistas para desarrollar el juego**

- Representa el tablero de 3x3 como una lista de listas (o un array) donde cada casilla puede contener un espacio vacío (" "), una "X" o una "O". Muestra el tablero al jugador después de cada turno.

- Determina quién comienza el juego. Puede ser aleatorio o seguir una lógica establecida.

- Permite al jugador seleccionar una posición en el tablero para colocar su símbolo. Verifica que la posición elegida esté vacía antes de permitir la jugada.

- Si juegas contra la máquina, implementa una lógica para que elija una casilla disponible de manera estratégica. Puede ser simple (elegir una casilla aleatoria) o más avanzada (bloquear al jugador o buscar ganar).

- Después de cada movimiento, verifica si algún jugador ha conseguido una línea de tres símbolos consecutivos en horizontal, vertical o diagonal.

- Si todas las casillas están ocupadas y ningún jugador ha ganado, declara un empate.

- Usa un bucle `while` para permitir que el juego continúe hasta que se cumpla una condición de victoria o empate.

- Al final de la partida, ofrece la opción de jugar otra ronda, reiniciando el tablero.


## Ahorcado


- La máquina selecciona una palabra secreta, y se representa cada letra con un espacio en blanco o un guion bajo ("_").

- El objetivo del jugador que adivina es descubrir la palabra intentando adivinar una letra en cada turno.

- Si el jugador elige una letra correcta, se muestra en su posición correcta dentro de la palabra.

- Si la letra adivinada no está en la palabra, se dibuja una parte del cuerpo en la horca como penalización.

- El juego termina cuando el jugador adivina la palabra completa o cuando se dibuja por completo la figura en la horca (en este caso tendremos que indicar que el jugador ha sido derrotado por la máquina). 

**Pistas para desarrollar el juego**

- Comienza definiendo una lista de palabras y haz que la máquina eliga una de manera aleatoria para que el jugador intente adivinar.

-  Usa una lista para representar las letras no adivinadas con guiones bajos ("_") y muéstralo al jugador.

- Usa un bucle `while` para que el jugador pueda seguir adivinando hasta que descubra la palabra o alcance el número máximo de intentos permitidos.

- Compara cada letra adivinada por el jugador con las letras de la palabra secreta. Si la letra está presente, actualiza el tablero con esa letra en las posiciones correspondientes.

- Mantén un registro de las letras que el jugador ya ha adivinado y cuenta los intentos fallidos.

- Establece las condiciones para que el juego termine, ya sea porque el jugador adivinó la palabra correctamente o porque alcanzó el número máximo de intentos fallidos.



## Piedra, Papel, Tijera, Lagarto, Spock

- En este juego, tanto el jugador como la máquina eligen una opción entre **piedra**, **papel**, **tijera**, **lagarto** y **Spock**.

- Las interacciones entre las opciones se resuelven de la siguiente manera:

  - **Piedra** aplasta a **tijera** y aplasta a **lagarto**.

  - **Papel** envuelve a **piedra** y refuta a **Spock**.

  - **Tijera** corta a **papel** y decapita a **lagarto**.

  - **Lagarto** envenena a **Spock** y devora a **papel**.

  - **Spock** aplasta a **tijera** y vaporiza a **piedra**.

- El juego se basa en rondas, donde en cada una, el jugador selecciona una opción y la máquina elige otra aleatoriamente.

- El ganador de cada ronda se determina según las reglas mencionadas. El juego continúa hasta que se cumple una condición de victoria o derrota, como alcanzar un número determinado de victorias.

**Pistas para desarrollar el juego**

- Comienza definiendo una lista con las cinco opciones: **piedra**, **papel**, **tijera**, **lagarto** y **Spock**.

- Implementa una función que permita al jugador seleccionar una opción y a la máquina elegir una opción aleatoria.

- Usa un bucle `while` para ejecutar múltiples rondas hasta que se alcance la condición de finalización (por ejemplo, el primero en ganar 3 rondas).

- Implementa la lógica de comparación para determinar quién gana cada ronda, basándote en las interacciones entre las opciones.

- Mantén un registro de las victorias de cada jugador y muéstralo en cada ronda.

- Establece las condiciones para que el juego termine, ya sea cuando uno de los jugadores alcance el número de victorias necesarias o cuando decidas implementar una cantidad fija de rondas.


## Hundir la Flota

- El juego se desarrolla en un tablero de 10x10, tanto para el jugador como para la máquina.

- Cada jugador coloca una serie de barcos en su tablero de forma estratégica. Los barcos tienen diferentes tamaños:

  - **Portaviones** (5 casillas)

  - **Acorazado** (4 casillas)

  - **Submarino** (3 casillas)

  - **Destructor** (3 casillas)

  - **Patrullero** (2 casillas)

- Una vez que los barcos están colocados, los jugadores se turnan para atacar, eligiendo coordenadas en el tablero del oponente para intentar "hundir" sus barcos.

- Si el ataque acierta (es decir, si golpea un barco), se marca en el tablero y el jugador que ataca puede seguir intentando hasta fallar. Si el ataque falla, el turno pasa al otro jugador.

- El juego termina cuando un jugador logra hundir todos los barcos del oponente.

**Pistas para desarrollar el juego**

- Crea un tablero de 10x10 representado como una lista de listas (o un array). Puedes usar caracteres como "-" para representar agua, "B" para representar las posiciones de los barcos, y "X" para los impactos.

- Implementa una función que permita al jugador y a la máquina colocar sus barcos en el tablero. Los barcos deben ocupar posiciones contiguas en línea recta, ya sea en dirección horizontal o vertical.

- La colocación de los barcos de la máquina debe realizarse aleatoriamente, respetando las reglas de alineación y evitando superposiciones.

- Implementa la lógica para que el jugador elija coordenadas para atacar. La máquina también puede seleccionar coordenadas aleatorias para atacar en su turno.

- Cada vez que se elige una coordenada para atacar, verifica si se golpeó un barco. Si un barco recibe un número de impactos igual a su tamaño, se considera hundido.

- Usa un bucle `while` para mantener el juego activo hasta que uno de los jugadores haya hundido todos los barcos del oponente.

- Muestra un resumen del tablero tras cada turno, indicando las posiciones de los barcos, los impactos y los intentos fallidos.

- El juego termina cuando todos los barcos de un jugador han sido hundidos. Establece un mensaje para indicar quién ha ganado la partida.


# Entrega del Proyecto

La entrega del proyecto se realizará a través de una **issue en GitHub**, trabajando en un repositorio propio en tu cuenta personal. Los pasos que deberás seguir para hacer la entrega del proyecto son:


- **Crear un nuevo repositorio en tu cuenta de GitHub:**

   - Crea un nuevo repositorio llamado `Proyecto1-Juegos-Python`. Este nombre es obligatorio, no podremos llamarlo de otra forma. 

   - Configuralo como público. 


- **Desarrolla el proyecto:**

   - Implementa el código de los juegos según las especificaciones y guías proporcionadas.

   - Recuerda hacer commits regulares mientras avanzas en el desarrollo:

     ```bash
     git add .
     git commit -m "Descripción del avance"
     git push
     ```


- **Crear una issue en el repositorio original del curso:**

   - Ve al repositorio original del curso y dirígete a la pestaña de **Issues**.

- **Abrir una nueva issue para tu entrega:**

   - Haz clic en **New Issue** y llena los siguientes campos:

     - **Título:** Usa el formato "Entrega Proyecto: ProyectoJuegos - [Tu Nombre]".

     - **Descripción:** En la descripción, incluye:

       - Una breve explicación de tu proyecto.

       - Instrucciones para ejecutar tu código (si aplica).

       - Un enlace a tu repositorio personal donde está alojado el proyecto.


# 🚀 Entrega del Proyecto 🚀

**Fecha y hora límite:**

🗓️ **Lunes a las 9:00 AM.**


**Nota importante:**

⚠️ **Todos los proyectos que sean entregados o modificados después de la hora límite (lunes a las 9:00 AM) se considerarán como no entregados.** Por favor, asegúrate de completar y enviar tu trabajo a tiempo para evitar problemas.


# 🎤 Presentación de Proyectos 🎤

El lunes a primera hora tendremos las **presentaciones de los proyectos**. La dinámica será la siguiente:

- De forma **aleatoria**, seleccionaremos entre **3 y 5 alumnos** para presentar su proyecto.

- Cada alumno tendrá **5 minutos** para explicar su proyecto y hacer una demo en vivo. Durante este tiempo podrán mostrar cómo funciona su juego y resaltar las características principales.

**Detalles importantes:**
- Es importante que lleguéis puntuales, ya que comenzaremos las presentaciones de inmediato.

- Asegúrate de que tu código esté listo y funcional para la demo.

- Todos debemos estar preparados para presentar, ya que la selección será completamente aleatoria.

