from poo.animales.animal import Animal


class Gato(Animal):
    """
        Clase para modeloar un gato
    """

    def __init__(self, nombre, raza):
        super().__init__(raza)
        self.nombre = nombre

    def hablar(self):
        print("Miau! Miau!")
