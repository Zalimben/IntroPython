from intro.decoradores import log
from poo.controlRemoto.controlRemoto import ControlRemoto


class ControlLG(ControlRemoto):
    """
    Implementa/hereda los métodos de la interfaz. Se define la implementación de los métodos (el cómo).
    """
    def siguiente_canal(self):
        print("LG->Siguiente")

    def canal_anterior(self):
        print("LG->Anterior")

    def subir_volumen(self):
        print("LG->Subir")

    @log
    def bajar_volumen(self):
        print("LG->Bajar")
