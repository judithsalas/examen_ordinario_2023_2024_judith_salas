# Examen Ordinario 2023-2024
 Judith M.ª Salas

### Ejercicio 2.1
El código consta de tres archivos: **Planetas.py**, **EstrellaDeLaMuerte.py**, y el script principal **main.py**.

En **Planetas.py**, se define un enumerado Clasificacion para asignar números a los planetas. La clase base Planeta y sus subclases (PlanetaConcordia, PlanetaIlum, PlanetaKamino) representan planetas con atributos como nombre, volumen y clasificación.

En **EstrellaDeLaMuerte.py**, la clase EstrellaDeLaMuerte tiene un atributo para los puntos de vida y un método destruir_planeta que evalúa si puede destruir un planeta en función de su clasificación.

El script principal **main.py** importa las clases y crea instancias de planetas y la Estrella de la Muerte, llamando al método destruir_planeta para cada planeta. Este diseño modular y orientado a objetos facilita la comprensión y extensión del sistema, permitiendo simular la destrucción de planetas por parte de la Estrella de la Muerte.

### Ejercicio 2.2

Este ejercicio también se desglosa en tres archivos:

El archivo **Naves.py** define dos subclases de la clase EstrellaDeLaMuerte llamadas NavePequeña y NaveGrande, cada una representando naves aliadas con sus propios nombres y puntos de vida.

En **EstrellaDeLaMuerte.py**, la clase EstrellaDeLaMuerte es modificada para incluir métodos que permiten a la estación espacial atacar naves aliadas y verificar si puede destruirlas.

El script principal **main.py** crea instancias de la Estrella de la Muerte, una NavePequeña y una NaveGrande, y ejecuta los métodos correspondientes para simular ataques y mostrar mensajes en la terminal. Este diseño facilita la interacción entre objetos en el espacio interestelar, proporcionando una estructura modular y orientada a objetos para representar diferentes entidades y sus relaciones.
