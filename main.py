from Planetas import PlanetaConcordia, PlanetaIlum, PlanetaKamino
from EstrellaDeLaMuerte import EstrellaDeLaMuerte

def main():
    # Crear instancias de planetas y la Estrella de la Muerte
    concordia = PlanetaConcordia()
    ilum = PlanetaIlum()
    kamino = PlanetaKamino()
    estrella_de_la_muerte = EstrellaDeLaMuerte()

    # Llamar al método destruir_planeta para cada planeta
    estrella_de_la_muerte.destruir_planeta(concordia)
    estrella_de_la_muerte.destruir_planeta(ilum)
    estrella_de_la_muerte.destruir_planeta(kamino)

if __name__ == "__main__":
    main()
