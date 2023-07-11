
class Pelota:
    """
    Clase Principal Pelota
    """
    def __init__(self, diametro, material):
        super().__init__()
        self.diametro = diametro
        self.material = material

    def description(self):
        print("El diametro es: ", self.diametro)
        print("El material es: ", self.material)
