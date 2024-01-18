import time

def main():
    # Inicializar variables
    tiempo_carlsen = 180
    tiempo_nakamura = 180
    tiempo_movimiento = 10
    turno = "Carlsen"

    while True:
        # Mostrar estado actual
        print(f"\nTiempo actual - Carlsen: {tiempo_carlsen} segundos, Nakamura: {tiempo_nakamura} segundos")
        print(f"Es el turno de: {turno}")

        # Verificar si se ha alcanzado el tiempo límite o si un jugador ha ganado
        if tiempo_carlsen <= 0 or tiempo_nakamura <= 0:
            print("La partida ha finalizado.")
            if tiempo_carlsen < tiempo_nakamura:
                print("¡Magnus Carlsen ha ganado!")
            elif tiempo_nakamura < tiempo_carlsen:
                print("¡Hikaru Nakamura ha ganado!")
            else:
                print("¡Es un empate!")
            break

        # Solicitar movimiento al usuario
        movimiento = input("Ingrese el nombre del jugador para realizar un movimiento (Carlsen/Hikaru/Salir): ").capitalize()

        # Validar el nombre ingresado
        if movimiento == "Salir":
            print("La partida ha sido cancelada.")
            break
        elif movimiento != turno:
            print(f"No es el turno de {movimiento}. Inténtalo de nuevo.")
            continue

        # Realizar el movimiento y reducir el tiempo
        if turno == "Carlsen":
            tiempo_carlsen -= tiempo_movimiento
            turno = "Nakamura"
        else:
            tiempo_nakamura -= tiempo_movimiento
            turno = "Carlsen"

        # Cambiar el tiempo de movimiento si es necesario
        if tiempo_carlsen <= 60 or tiempo_nakamura <= 60:
            tiempo_movimiento = 5

if __name__ == "__main__":
    main()
