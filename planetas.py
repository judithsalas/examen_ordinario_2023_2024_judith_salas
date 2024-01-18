from enum import Enum

# Enumerado para clasificar los planetas
class Clasificacion(Enum):
    CONCORDIA = 1
    ILUM = 2
    KAMINO = 3

# Clase base Planeta
class Planeta:
    def __init__(self, nombre, volumen, clasificacion): #Constructor de clase base, sus parámetros son los atributos
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion.value

# Subclases de Planeta
class PlanetaConcordia(Planeta):  #Hereda de la clase base Planeta, al igual que el resto de planetas.
    def __init__(self):
        super().__init__("Concordia", 500, Clasificacion.CONCORDIA)
    

class PlanetaIlum(Planeta):
    def __init__(self):
        super().__init__("Ilum", 1200, Clasificacion.ILUM) #Los atributos se han designado en el enunciado y son correspondientes a los de la clase base

class PlanetaKamino(Planeta):
    def __init__(self):
        super().__init__("Kamino", 800, Clasificacion.KAMINO)
