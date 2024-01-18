'''
En Naves.py, crea dos subclases de la clase EstrellaDeLaMuerte 
para representar naves aliadas más pequeñas y grandes. 
Estas subclases serán NavePequena y NaveGrande. 
Cada una de ellas debe tener su propio constructor que inicialice 
el nombre de la nave y sus puntos de vida.

'''

class NavePequena:
    def __init__(self, nombre, puntos_de_vida):
        self.nombre = nombre
        self.puntos_de_vida = puntos_de_vida


class NaveGrande:
    def __init__(self, nombre, puntos_de_vida):
        self.nombre = nombre
        self.puntos_de_vida = puntos_de_vida
