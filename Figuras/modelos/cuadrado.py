from .rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    
    def __init__(self, lado):
        if not Rectangulo.es_numero_positivo(lado):
            raise ValueError("El numero debe de ser positivo")
        super().__init__(base=lado, altura=lado)
        self.nombre = f"Cuadrado l={lado}"
    
    @property
    def lado(self):
        return self._base
    
    @lado.setter
    def lado(self, valor):
        if not Rectangulo.es_numero_positivo(valor):
            raise ValueError("El numero debe de ser positivo")
        self._base = float(valor)
        self._altura = float(valor)
        self.nombre = f"Cuadrado l={valor}"