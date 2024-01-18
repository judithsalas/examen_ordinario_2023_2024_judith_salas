'''
En EstrellaDeLaMuerte.py, modifica la clase EstrellaDeLaMuerte para que 
pueda interactuar con sus naves aliadas. Añade métodos para atacar naves aliadas y 
verificar si pueden ser destruidas. Si la vida de la nave aliada es menor o igual 
a los puntos de vida de la Estrella de la Muerte, muestra un mensaje por terminal que 
diga que la Estrella de la Muerte ha destruido la nave aliada y resta los puntos de vida correspondientes. 
Si la vida es mayor, muestra un mensaje que diga que la Estrella de la Muerte no puede destruir la nave aliada.
'''

class EstrellaDeLaMuerte:
    def __init__(self, puntos_de_vida):
        self.puntos_de_vida = puntos_de_vida

    def atacar_nave_aliada(self, nave_aliada):
        if self.puede_destruir_nave_aliada(nave_aliada):
            print(f"La Estrella de la Muerte ha destruido la nave {nave_aliada.nombre}.")
            nave_aliada.puntos_de_vida -= self.puntos_de_vida
        else:
            print(f"La Estrella de la Muerte no puede destruir la nave {nave_aliada.nombre}.")

    def puede_destruir_nave_aliada(self, nave_aliada):
        return nave_aliada.puntos_de_vida <= self.puntos_de_vida
