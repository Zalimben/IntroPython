from intro.decoradores import log
from poo.controlRemoto.controlRemoto import ControlRemoto


class ControlSamsung(ControlRemoto):
    """
        Implementa/hereda los métodos de la interfaz. Se define la implementación de los métodos (el cómo).
    """
    @log
    def siguiente_canal(self):
        print("Samsung->Siguiente")

    @log
    def canal_anterior(self):
        print("Samsung->Anterior")

    @log
    def subir_volumen(self):
        print("Samsung->Subir")

    @log
    def bajar_volumen(self):
        print("Samsung->Bajar")