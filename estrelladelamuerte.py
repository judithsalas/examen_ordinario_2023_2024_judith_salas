from Planetas import Planeta

# Clase EstrellaDeLaMuerte

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000 #tiene un atributo de puntos de vida que se inicializa en 1000

    def destruir_planeta(self, planeta):  #es un método de la clase que toma un objeto de la clase planeta como argumento
        #Con los condicionales, se comprueba si los puntos de la estrella de la muerte son suficentes como para destruir el planeta
        if planeta.volumen <= self.puntos_de_vida: 
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_de_vida -= planeta.volumen
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}. La clasificación es demasiado alta.")
