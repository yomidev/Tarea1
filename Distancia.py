class Distancia:
    
    METROS_POR_KM = 1000.00
    METROS_POR_MILLA = 1609.344
    
    def __init__(self, metros):
        if not Distancia.es_valido(metros):
            raise ValueError(f"Distancia invalida{metros}. Debe ser un numero mayor o igual a cero")
        self._metros = float(metros)
    
    @staticmethod
    def es_valido(metros):
        return isinstance(metros, (int, float)) and metros >= 0
    
    @classmethod
    def desde_km(cls, km):
        return cls (km * cls.METROS_POR_KM)
    
    @classmethod
    def desde_milla(cls, milla):
        return cls (milla * cls.METROS_POR_MILLA)
    @property
    def metros(self):
        return round(self._metros,2)
    @property
    def kilometros (self):
        return round(self._metros / Distancia.METROS_POR_KM,2)
    @property
    def millas(self):
        return round(self._metros/Distancia.METROS_POR_MILLA, 2)
    
    @kilometros.setter
    def kilometros(self,valor):
        if not Distancia.es_valido(valor):
            raise ValueError("kilometros invalidos. Debe de ser un valor numerico")
        self._metros = Distancia.METROS_POR_KM*valor
        
    def sumar(self,otra_distancia):
        if not isinstance (otra_distancia,Distancia):
            raise TypeError("solo se puede sumar otra distancia")
        self._metros += otra_distancia._metros
        return self._metros
    
    def describir(self):
        return (f"{self.metros} m -- {self.kilometros} k -- {self.millas} mi --")
    
    @property
    def yardas(self):
        return self._metros * 0.9144
    
    @classmethod
    def desde_yardas(cls,yardas):
        return cls(yardas*0.9144)
    
    def restar(self, valor):
        if not isinstance (valor,Distancia):
            raise TypeError("solo se puede restar otra distancia")
        self._metros = self._metros - valor
        return self._metros
    
d1 = Distancia(1500)
print(d1.describir())

d2 = Distancia.desde_km(5)
d3 = Distancia.desde_milla(1)
print(d2.describir())
print(d3.describir())

print(d2.kilometros)
print(d2.millas)

d1.sumar(d2)
print(d1.describir())

try:
    Distancia(-5)
except ValueError as e:
    print("Error: ", e)
    
try:
    d1.kilometros = -1
except ValueError as e:
    print("Error: ", e)