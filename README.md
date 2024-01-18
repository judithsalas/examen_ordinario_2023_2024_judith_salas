# Examen Ordinario 2023-2024
 Judith M.ª Salas

Descripcion de los ejercicios.

### Ejercicio 1.

El código de la pirámide consta de dos funciones principales:

La función **generar_piramide** toma un número entero n como entrada y utiliza un bucle **for** para generar cada nivel de la pirámide. Se calcula la cantidad de espacios antes de los asteriscos para centrar la pirámide y se imprime cada nivel con una **combinación de espacios y asteriscos**. 

La función **main** es el punto de entrada del programa, donde se solicita al usuario ingresar un número entero mayor o igual a 1. Se utiliza un bucle **while** para asegurar que la entrada sea válida. Después de recibir el número, se llama a **generar_piramide** con el valor ingresado para crear y mostrar la pirámide en la consola.

### Ejercicio 2.
El código consta de tres archivos: **Planetas.py**, **EstrellaDeLaMuerte.py**, y el script principal **main.py**. 

En **Planetas.py**, se define un enumerado Clasificacion para asignar números a los planetas. La clase base Planeta y sus subclases (PlanetaConcordia, PlanetaIlum, PlanetaKamino) representan planetas con atributos como nombre, volumen y clasificación. 

En **EstrellaDeLaMuerte.py**, la clase EstrellaDeLaMuerte tiene un atributo para los puntos de vida y un método destruir_planeta que evalúa si puede destruir un planeta en función de su clasificación. 

El script principal **main.py** importa las clases y crea instancias de planetas y la Estrella de la Muerte, llamando al método destruir_planeta para cada planeta. Este diseño modular y orientado a objetos facilita la comprensión y extensión del sistema, permitiendo simular la destrucción de planetas por parte de la Estrella de la Muerte.

### Ejercicio 3.

El archivo **Naves.py** define dos subclases de la clase **EstrellaDeLaMuerte** llamadas **NavePequeña** y **NaveGrande**, cada una representando naves aliadas con sus propios nombres y puntos de vida. 

En **EstrellaDeLaMuerte.py**, la clase EstrellaDeLaMuerte es modificada para incluir métodos que permiten a la estación espacial atacar naves aliadas y verificar si puede destruirlas. 

El script principal **main.py** crea instancias de la Estrella de la Muerte, una NavePequeña y una NaveGrande, y ejecuta los métodos correspondientes para simular ataques y mostrar mensajes en la terminal. Este diseño facilita la interacción entre objetos en el espacio interestelar, proporcionando una estructura modular y orientada a objetos para representar diferentes entidades y sus relaciones.

