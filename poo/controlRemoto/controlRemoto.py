from abc import abstractmethod, ABCMeta


class ControlRemoto(metaclass=ABCMeta):
    """
        Interfaz de Control Remoto. Se definen los métodos comunes (el qué)
    """
    @abstractmethod
    def siguiente_canal(self):
        # Métodos vacíos
        pass

    @abstractmethod
    def canal_anterior(self):
        # Métodos vacíos
        pass

    @abstractmethod
    def subir_volumen(self):
        # Métodos vacíos
        pass

    @abstractmethod
    def bajar_volumen(self):
        # Métodos vacíos
        pass
