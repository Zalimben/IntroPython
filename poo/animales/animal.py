class Animal:
    """Modelo lógico de Animal."""
    __dominio = "Animalia"

    def __init__(self, raza):
        self.raza = raza

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo:", type(self).__name__)
        print("Mi especie es:", self.raza)

    def sentado(self):
        print("El animal se sienta!")

    def comer(self):
        pass

    def dormir(self):
        pass

    def recuperar_dominio(self):
        return self.__dominio
