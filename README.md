# Examen Ordinario 2023-2024
 Judith M.ª Salas

Descripcion de los ejercicios.

### Ejercicio 3.

En este ejercicio se ha simulado un juego de ajedrez entre los jugadores Magnus Crlsen y Hikaru Nakamura, con tiempos iniciales de 3 minutos para cada uno.
Cada turno, muestra el tiempo actial de ambos jugadores y el nombre del jugador al que le toca jugar. 

El usuario ingrsa el nombre del jugador que quiere realizar un movimiento, y el programa verifica si es el turno correcto antes de reducir el tiempo del jugado en turno de acuerdo con el tiempo de movimiento se reduce a 5 segundos por movimiento. El juego finaliza cuando uno de los jugadores alcanza 0 segundos, es decir, se queda sin tiempo o cuando el usuario ingresa 'Salir'. 

Al finalizar la partida, se muestra un mensaje indicando quién ganó o si fue un empate, basándose en los tiempos restantes de los jugadores. Se ha utilizado un bucle principal (while) que se ejecuta hasta que se cumple una condición de finalización.
