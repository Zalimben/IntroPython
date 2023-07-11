from poo.animales.animal import Animal


class Perro(Animal):
    """Modelo lógico de un perro."""
    # Atributo privado
    __especie = "Canis Lupus Familiaris"

    def __init__(self, nombre, anho, raza):
        """Constructor"""
        super().__init__(raza)
        self.name = nombre
        self.age = anho

    def hablar(self):
        print("Guau! Guau!")

    def sentado(self):
        """Acción de sentarse"""
        print(self.name.title() + " está sentado.")

    def vueltas(self):
        """Acción de dar vueltas."""
        print(self.name.title() + " dá vueltas!")

    # Método para recuperar atributo privado
    def recuperar_especie_completa(self):
        print("La especie es: ", self.__recuperar_especie())

    # Método privado
    def __recuperar_especie(self):
        return self.recuperar_dominio() + ' ' + self.__especie
