from poo.animales.perro import Animal


class Vaca(Animal):
    def hablar(self):
        print("Muuu!")

    def idioma(self):
        return "Muuu!"

    def moverse(self):
        print("Caminando con 4 patas")
