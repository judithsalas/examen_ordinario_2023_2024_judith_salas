
def generar_piramide(n):
    # Genera cada nivel de la pirámide
    for i in range(1, n + 1, 2):  # Comienza con 1 asterisco, aumenta en 2 por nivel
        espacios = (n - i) // 2  # Calcula la cantidad de espacios antes de los asteriscos
        print(" " * espacios + "*" * i + " " * espacios)  # Imprime el nivel

def main():
    # Bucle para solicitar un número entero mayor o igual a 1
    while True:
        try:
            n = int(input("Ingrese un número entero mayor o igual a 1 para la altura de la pirámide: "))
            if n >= 1:
                break
            else:
                print("Por favor, ingrese un número mayor o igual a 1.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    print(f"\nPirámide de asteriscos con {n} niveles:\n")
    generar_piramide(n)

if __name__ == "__main__":
    main()
