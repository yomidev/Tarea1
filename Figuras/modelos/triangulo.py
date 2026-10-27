import math
from .figura import Figura

class Triangulo(Figura):
    
    def __init__(self, lado_a, lado_b, lado_c):
        for nombre, lado in [("a", lado_a), ("b", lado_b), ("c", lado_c)]:
            if not Figura.es_numero_positivo(lado):
                raise ValueError(f"El lado {nombre} no es un numero positivo")
        if not self.__es_triangulo_valido(lado_a, lado_b, lado_c):
            raise ValueError(f"Los lados {lado_a}, {lado_b}, {lado_c} no forman un triangulo valido")
        super().__init__(f"Triangulo {lado_a} - {lado_b} -{lado_c}")
        self._lado_a = lado_a
        self._lado_b = lado_b
        self._lado_c = lado_c
    
    def __es_triangulo_valido(self, a, b, c):
        return (a+b > c) and (a + c > b) and (b+c >a)
    
    def area(self):
        s = self.perimetro()/2
        return math.sqrt(s - self._lado_a)*(s - self._lado_b)*(s-self._lado_c)
    
    def perimetro(self):
        return self._lado_a + self._lado_b + self._lado_c