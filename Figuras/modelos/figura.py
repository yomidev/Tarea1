class Figura:
    
    total_figuras = 0
    
    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la figura no debe de estar vacio.")
        Figura.total_figuras += 1
        self.nombre = nombre
        
        print(f"[Figura] Creada: {self.nombre}")
        
    def __del__(self):
        nombre = getattr(self, "nombre", "?")
        print(f"[Figura] {nombre} ha sido eliminada")
        
    @property
    def tipo(self):
        return type(self.__name__)
    
    def area(self):
        raise NotImplementedError("El metodo se debe de ejecutar en las clases hijas")
    
    def perimetro(self):
        raise NotImplementedError("El metodo se debe de ejecutar en las clases hijas")
    
    def describir(self):
        return (f"{self.nombre} // Area: {self.area()} Perimetro: {self.perimetro()}")
    
    @classmethod
    def num_figuras(cls):
        return cls.total_figuras
    
    @staticmethod
    def es_numero_positivo(valor):
        return isinstance(valor, (int, float)) and valor > 0