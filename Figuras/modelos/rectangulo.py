from .figura import Figura

class Rectangulo(Figura):
    
    def __init__(self, base, altura):
        if not Figura.es_numero_positivo(base):
            raise ValueError("El numero debe de ser positivo")
        if not Figura.es_numero_positivo(altura):
            raise ValueError("El numero debe de ser positivo")
        super().__init__(f"Rectangulo b={base}, h={altura}")
        self._base = float(base)
        self._altura = float(altura)
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if not Figura.es_numero_positivo(valor):
            raise ValueError("El numero debe de ser positivo")
        self._base = float(valor)
        self.nombre = f"Rectangulo b={valor} h={self._altura}"
        
    @property
    def altura(self):
            return self._altura
        
    @altura.setter
    def altura(self, valor):
        if not Figura.es_numero_positivo(valor):
            raise ValueError("El numero debe de ser positivo")
        self._altura = float(valor)
        self.nombre = f"Rectangulo b={self._base} h={valor}"
    
    def area(self):
        return self._base * self._altura
    def perimetro(self):
        return 2 * (self._base + self._altura)