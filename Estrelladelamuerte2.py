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
