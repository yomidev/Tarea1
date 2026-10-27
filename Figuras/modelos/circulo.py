import math
from .figura import Figura

class Circulo(Figura):
    
    def __init__(self, radio):
        if not Figura.es_numero_positivo(radio):
            raise ValueError("El numero debe de ser positivo y valor numerico")
        super().__init__(f"Circulo r={radio}")
        self._radio = float(radio)
        
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, valor):
        if not Figura.es_numero_positivo(valor):
            raise ValueError("El numero debe de ser positivo")
        self._radio = float(valor)
        self.nombre = f"Circulo r={valor}"
        
    def area(self):
        return math.pi * self._radio ** 2
    def perimetro(self):
        return 2 * math.pi * self._radio