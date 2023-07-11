from poo.animales.animal import Animal
from poo.animales.perro import Perro
from poo.jugadores.arquero import Arquero
from poo.jugadores.volante import Volante


class ArqueroVolante(Arquero, Volante):
    def __init__(self, nombre, nro):
        self.nombre = nombre
        self.nro = nro
