import unittest

from poo.animales.gato import Gato
from poo.animales.perro import Perro
from poo.animales.vaca import Vaca


class TestAnimales(unittest.TestCase):

    def test_perro_idioma(self):
        # Dado que...
        animal = Perro("Venom", 2, "Canis")
        # Cuando...
        idioma = animal.idioma()
        # Se obtiene...
        self.assertEqual(idioma, 'Guau! Guau!')

    def test_vaca_idioma(self):
        # Dado que...
        lola = Vaca("lechera")
        # Cuando...
        idioma = lola.idioma()
        # Se obtiene...
        self.assertEqual(idioma, "Muuu!")

    def test_gato_idioma(self):
        # Dado que...
        michi = Gato("Michifu", "Meztizo")
        # Cuando...
        idioma = michi.idioma()
        # Se obtiene...
        self.assertEqual(idioma, "Miau! Miau!")

