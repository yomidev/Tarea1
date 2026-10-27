from .publicacion import Publicacion

class Libro(Publicacion):
    
    def __init__(self, titulo, year, autor, paginas):
        if not isinstance(autor, str) or not autor.strip():
            raise ValueError("El autor no puede estar vacio")
        if not isinstance(paginas, int) or paginas <= 0:
            raise ValueError("Las paginas deben de ser un numero y mayor que 0")
        
        super().__init__(titulo, year)
        
        self._autor = autor
        self._paginas = paginas
        
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El autor no puede estar vacio")
        self._autor = valor.strip()
        
    @property
    def pags(self):
        return self._paginas
    
    @pags.setter
    def pags (self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Las paginas deben de ser un numero y mayor que 0")
        self._paginas = int(valor)
        
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | Autor: {self._autor} | Paginas: {self._paginas}"
    
    def es_libro_largo(self):
        return self._paginas > 300