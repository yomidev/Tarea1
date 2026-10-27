class Temperatura:
    #Atributo de clase
    CERO_ABSOLUTO_K = 0.0
    
    def __init__(self, kelvin):
        if not Temperatura.es_valido(kelvin):
            raise ValueError(f"Kelvin invalido: {kelvin}. Debe de ser >= 0.")
        self._kelvin = float(kelvin)
        
    #Metodo Estatico
    @staticmethod
    def es_valido(kelvin):
        """Devuelve True si el valor es un numero >= 0"""
        return isinstance(kelvin, (int, float)) and kelvin >= Temperatura.CERO_ABSOLUTO_K
    
    #Metodos de clase
    @classmethod
    def desde_celsius(cls, celsius):
        """Crea una temperatura a partir de grados Celsius"""
        kelvin = celsius + 273.15
        return cls(kelvin)
    
    @classmethod
    def desde_fahrenheit(cls, fahrenheit):
        """Crea una temperatura a partir de grados Fahrenheit"""
        celsius = (fahrenheit - 32) * 5/9
        return cls.desde_celsius(celsius)
    
    #Property
    @property
    def celsius(self):
        return round(self._kelvin - 273.15, 2)
    
    @property
    def fahrenheit(self):
        return round((self._kelvin - 273.15) * 9 / 5 +32, 2)
    
    @property
    def kelvin(self):
        return round(self._kelvin, 2)
    
    @property
    def celsius_set(self):
        return self.celsius
    
    @celsius_set.setter
    def celsius_set(self, valor):
        if not Temperatura.es_valido(valor + 273.15):
            raise ValueError(f"Celsius invalido: {valor}")
        self._kelvin = valor + 273.15
        
    #Metodos de instancia
    def aumentar(self, grados_celsius):
        """Sube la temperatura en grados Celsius"""
        nueva_k = self._kelvin + grados_celsius
        if not Temperatura.es_valido(nueva_k):
            raise ValueError("La operación lleva la temperatura por debajo de cero absoluto")
        self._kelvin = nueva_k
        return self._kelvin
    
    def describir(self):
        return (f"{self.celsius} C -- {self.fahrenheit} F -- {self.kelvin} K")
    
t1 = Temperatura(300)
print(t1.describir())

t2 = Temperatura.desde_celsius(25) #Constructor auxiliar
t3 = Temperatura.desde_fahrenheit(98.6)
print(t2.describir())
print(t3.describir())

print(t2.celsius)
print(t2.fahrenheit)
print(t2.kelvin)

t2.aumentar(10)
print(t2.celsius)

t2.celsius_set = 100
print(t2.celsius)

try:
    t2.celsius_set = -500
except ValueError as e:
    print("Error capturado: ", e)
    
try:
    Temperatura(-10)
except ValueError as e:
    print("Error Capturado: ", e)
    
print(Temperatura.es_valido(100))
print(Temperatura.es_valido(-5))