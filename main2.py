'''
En main.py, crea instancias de la Estrella de la Muerte, una NavePequena, y una NaveGrande. 
Llama a los métodos correspondientes para que la Estrella de la Muerte ataque a sus naves aliadas y 
muestra los mensajes en la terminal.
'''

from Naves import NavePequeña, NaveGrande
from EstrellaDeLaMuerte import EstrellaDeLaMuerte

def main():
    # Crear instancias de la Estrella de la Muerte, NavePequeña y NaveGrande
    estrella_de_la_muerte = EstrellaDeLaMuerte(500)
    nave_pequeña = NavePequeña("X-Wing", 100)
    nave_grande = NaveGrande("Star Destroyer", 300)

    # Llamar a los métodos correspondientes para que la Estrella de la Muerte ataque a sus naves aliadas
    estrella_de_la_muerte.atacar_nave_aliada(nave_pequeña)
    estrella_de_la_muerte.atacar_nave_aliada(nave_grande)

if __name__ == "__main__":
    main()
